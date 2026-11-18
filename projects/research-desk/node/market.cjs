'use strict';
const fs=require('node:fs');
const path=require('node:path');
const os=require('node:os');
const http=require('node:http');
const https=require('node:https');
const tls=require('node:tls');
const readline=require('node:readline');
const {instruments,parseChart,parseCboeCsv,parseFredCsv}=require('../market.js');
// Reuse only these two keys from the existing local research connector.
// Never expose them through RPC, browser storage, logs, or the package.
function credentials(){
  const source=fs.readFileSync(path.join(os.homedir(),'Downloads','jnk spy','spy_jnk_data_ingestion_v1','.env'),'utf8');
  const values={};
  for(const line of source.split(/\r?\n/)){
    const m=line.match(/^\s*(?:export\s+)?(ALPACA_API_KEY|ALPACA_API_SECRET)\s*=\s*(.*)$/);
    if(!m)continue;
    let v=m[2].trim();
    if((v[0]==='"'&&v.endsWith('"'))||(v[0]==="'"&&v.endsWith("'")))v=v.slice(1,-1);
    else v=v.replace(/\s+#.*$/,'').trim();
    values[m[1]]=v;
  }
  if(!values.ALPACA_API_KEY||!values.ALPACA_API_SECRET)throw new Error('既有 Alpaca 连接缺少配置');
  return {'APCA-API-KEY-ID':values.ALPACA_API_KEY,'APCA-API-SECRET-KEY':values.ALPACA_API_SECRET};
}
/* 分块取日线：每块 ≤12 个标的，避免单响应超 10000 bar 上限。
 * 熔断：第一块 raw+adjustment 全部失败视为连接不可用，立即放弃剩余块（Yahoo 兜底）。 */
function getBars(adjustment,headers,now,symbols,startDays){
  const params=new URLSearchParams({symbols:symbols.join(','),timeframe:'1Day',start:new Date(now-startDays*86400000).toISOString(),end:new Date(now).toISOString().slice(0,10)+'T00:00:00Z',adjustment,feed:'sip',sort:'asc',limit:'10000'});
  return new Promise((resolve,reject)=>{
    const req=https.get('https://data.alpaca.markets/v2/stocks/bars?'+params,{headers},res=>{
      if(res.statusCode!==200){res.resume();reject(new Error('Alpaca SIP 行情请求失败 HTTP '+res.statusCode));return;}
      let body='';
      res.setEncoding('utf8');res.on('data',chunk=>{body+=chunk;if(body.length>12000000)req.destroy(new Error('行情响应超出上限'));});
      res.on('end',()=>{try{const p=JSON.parse(body);if(p.next_page_token)throw new Error('行情响应未完整取回');if(!p.bars)throw new Error('行情响应缺少日线');resolve(p.bars);}catch(e){reject(new Error('Alpaca 行情结构不完整'));}});
      res.on('error',()=>reject(new Error('Alpaca 行情传输中断')));
    });
    req.setTimeout(15000,()=>req.destroy(new Error('Alpaca 行情请求超时')));
    req.on('error',()=>reject(new Error('Alpaca 行情连接失败，请检查本机连接后重试')));
  });
}
function chunk(list,size){const out=[];for(let i=0;i<list.length;i+=size)out.push(list.slice(i,i+size));return out;}
async function refresh(){
  const headers=credentials(),now=Date.now();
  const fetchable=instruments.filter(x=>x.kind!=='volatility');
  const core=fetchable.filter(x=>x.history==='core3y'), pool=fetchable.filter(x=>x.history!=='core3y');
  const groups=[...chunk(core,12).map(symbols=>({symbols,startDays:1100})),{symbols:pool.map(x=>x.symbol),startDays:320}];
  const raw={},adjusted={};
  for(let gi=0;gi<groups.length;gi++){
    const g=groups[gi];
    try{
      const [r,a]=await Promise.all([getBars('raw',headers,now,g.symbols,g.startDays),getBars('all',headers,now,g.symbols,g.startDays)]);
      Object.assign(raw,r);Object.assign(adjusted,a);
    }catch(e){
      if(gi===0)throw new Error('本机 Alpaca 连接不可用（'+e.message+'）；由公开行情兜底。');
      /* 首块成功后的块失败：保留已取数据，缺项走兜底 */
    }
  }
  const quotes=[];
  for(const item of fetchable){
    const bars=raw[item.symbol]||[], byTime=new Map((adjusted[item.symbol]||[]).map(b=>[b.t,b.c]));
    if(bars.length<2)continue;
    try{
      const q=parseChart({chart:{result:[{timestamp:bars.map(b=>Date.parse(b.t)/1000),meta:{currency:'USD'},indicators:{quote:[{close:bars.map(b=>b.c)}],adjclose:[{adjclose:bars.map(b=>byTime.get(b.t))}]}}]}},item,now);
      quotes.push({...q,provider:'Alpaca SIP',sourceUrl:'https://docs.alpaca.markets/reference/stockbars',freshnessNote:'Alpaca SIP 日线；保守排除 UTC 当天未核验收盘的 bar。不是实时盘口；数据可用不代表市场安全。'});
    }catch(_){/* Missing instrument is handled by the background fallback. */}
  }
  if(!quotes.length)throw new Error('没有可展示的已完成日线');
  return {quotes};
}
/* ---- 指数与宏观 CSV：本机代理优先，直连兜底 ----
 * CBOE/FRED 在本机网络下直连常被重置或超时；节点进程有本机权限，
 * 经既有代理（127.0.0.1:7897，与 twitter CLI 同源）建立 CONNECT 隧道。
 * 所有路径都有硬超时，保证单源失败不拖垮整轮刷新。 */
const LOCAL_PROXY={host:'127.0.0.1',port:7897};
function connectViaProxy(hostname,{connectTimeoutMs=5000}={}){
  return new Promise((resolve,reject)=>{
    const req=http.request({host:LOCAL_PROXY.host,port:LOCAL_PROXY.port,method:'CONNECT',path:hostname+':443',timeout:connectTimeoutMs});
    req.on('connect',(resp,socket)=>{ resp.statusCode===200 ? resolve(socket) : (socket.destroy(), reject(new Error('代理 CONNECT 失败 HTTP '+resp.statusCode))); });
    req.on('timeout',()=>{try{req.destroy(new Error('代理连接超时'));}catch(_){}});
    req.on('error',e=>reject(e));
    req.end();
  });
}
function getOverSocket(url,tlsSocket,timeoutMs){
  return new Promise((resolve,reject)=>{
    let settled=false;
    const guard=setTimeout(()=>{ if(!settled){settled=true;try{tlsSocket.destroy();}catch(_){} reject(new Error('请求超时('+timeoutMs+'ms)'));} },timeoutMs);
    const done=(err,body)=>{ if(!settled){settled=true;clearTimeout(guard);try{tlsSocket.destroy();}catch(_){} err?reject(err):resolve(body);} };
    const req=https.get(url,{createConnection:()=>tlsSocket,agent:false,servername:new URL(url).hostname},resp=>{
      if(resp.statusCode!==200){resp.resume();done(new Error('HTTP '+resp.statusCode));return;}
      let body='';resp.setEncoding('utf8');
      resp.on('data',c=>{body+=c;if(body.length>3000000)done(new Error('响应超限'));});
      resp.on('end',()=>done(null,body));
      resp.on('error',e=>done(e));
    });
    req.on('timeout',()=>done(new Error('请求超时('+timeoutMs+'ms)')));
    req.on('error',e=>done(e));
    tlsSocket.on('error',e=>done(e));
  });
}
function httpsText(url,{timeoutMs=12000,proxyConnectMs=5000}={}){
  const target=new URL(url);
  const direct=()=>new Promise((resolve,reject)=>{
    const req=https.get(url,{servername:target.hostname,timeout:timeoutMs},resp=>{
      if(resp.statusCode!==200){resp.resume();reject(new Error('HTTP '+resp.statusCode));return;}
      let body='';resp.setEncoding('utf8');
      resp.on('data',c=>{body+=c;if(body.length>3000000)req.destroy(new Error('响应超限'));});
      resp.on('end',()=>resolve(body));
      resp.on('error',e=>reject(e));
    });
    req.on('timeout',()=>{try{req.destroy(new Error('请求超时('+timeoutMs+'ms)'));}catch(_){}});
    req.on('error',e=>reject(e));
  });
  const viaProxy=async()=>{
    const raw=await connectViaProxy(target.hostname,{connectTimeoutMs:proxyConnectMs});
    const sock=tls.connect({socket:raw,servername:target.hostname});
    sock.setTimeout(timeoutMs,()=>{try{sock.destroy(new Error('TLS 超时'));}catch(_){}});
    return getOverSocket(url,sock,timeoutMs+2000);
  };
  return viaProxy().catch(()=>direct());
}
const CBOE={
  VIX:{url:'https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv',label:'VIX · 隐含波动率',unit:'点'},
  VIX3M:{url:'https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VIX3M_History.csv',label:'VIX3M · 三月隐含波动率',unit:'点'},
  VVIX:{url:'https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VVIX_History.csv',label:'VVIX · 波动率的波动率',unit:'点'}
};
const FRED={
  DGS10:{url:'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10',label:'美债 10 年名义利率',unit:'%'},
  DFII10:{url:'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10',label:'美债 10 年实际利率',unit:'%'},
  BAMLH0A0HYM2:{url:'https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2',label:'ICE BofA 高收益利差',unit:'%'},
  DTWEXBGS:{url:'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DTWEXBGS',label:'广义贸易加权美元指数',unit:'指数'}
};
async function fetchIndices(){
  const errors=[],indices=[],macro=[];
  const cutoff=new Date(Date.now()-1100*86400000).toISOString().slice(0,10);
  const jobs=[];
  for(const [key,def] of Object.entries(CBOE)){
    jobs.push(httpsText(def.url,{timeoutMs:12000}).then(text=>{
      const parsed=parseCboeCsv(text,key);
      indices.push({key,...def,rows:parsed.rows.filter(r=>r.date>=cutoff),bad:parsed.bad});
    }).catch(e=>errors.push({source:'CBOE '+key,error:String(e.message||e).slice(0,160)})));
  }
  for(const [key,def] of Object.entries(FRED)){
    jobs.push(httpsText(def.url,{timeoutMs:10000}).then(text=>{
      const parsed=parseFredCsv(text,key);
      macro.push({key,...def,rows:parsed.rows.filter(r=>r.date>=cutoff),bad:parsed.bad});
    }).catch(e=>errors.push({source:'FRED '+key,error:String(e.message||e).slice(0,160)})));
  }
  await Promise.all(jobs);
  return {indices,macro,errors};
}
/* 宿主的 Node 运行时包装器把本文件作为模块 require 进来，process.stdin 被替换为宿主
 * 喂给的虚拟流；因此服务必须在模块加载时无条件启动，不能用 require.main === module
 * 守卫（被 require 时该判断恒为假，v2.0.0 曾因此整条 Node 通道静默超时）。
 * 测试进程用 DESK_NODE_TEST=1 跳过服务启动。 */
if(process.env.DESK_NODE_TEST!=='1'){
  process.stderr.write('[research-desk worker] up node='+process.version+' pid='+process.pid+'\n');
  readline.createInterface({input:process.stdin}).on('line',async line=>{
    let m;try{m=JSON.parse(line);}catch(_){return;}
    if(m.id==null)return;
    const reply=(ok,result)=>process.stdout.write(JSON.stringify({jsonrpc:'2.0',id:m.id,...(ok?{result}:{error:{code:-32000,message:result}})})+'\n');
    process.stderr.write('[research-desk worker] req '+m.method+'\n');
    try{
      if(m.method==='ping')reply(true,{pong:true,node:process.version,ts:Date.now()});
      else if(m.method==='market.refresh')reply(true,await refresh());
      else if(m.method==='market.indices')reply(true,await fetchIndices());
      else reply(false,'未知只读行情方法');
    }catch(e){reply(false,e.code==='ENOENT'?'未找到已有 Alpaca 本机配置':e.message);}
  });
}
module.exports={refresh,fetchIndices};
