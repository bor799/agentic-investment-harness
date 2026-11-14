'use strict';
const fs=require('node:fs');
const path=require('node:path');
const os=require('node:os');
const https=require('node:https');
const readline=require('node:readline');
const {instruments,parseChart}=require('../market.js');
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
function getBars(adjustment,headers,now){
  const params=new URLSearchParams({symbols:instruments.filter(x=>x.kind!=='volatility').map(x=>x.symbol).join(','),timeframe:'1Day',start:new Date(now-210*86400000).toISOString(),end:new Date(now).toISOString().slice(0,10)+'T00:00:00Z',adjustment,feed:'sip',sort:'asc',limit:'10000'});
  return new Promise((resolve,reject)=>{
    const req=https.get('https://data.alpaca.markets/v2/stocks/bars?'+params,{headers},res=>{
      if(res.statusCode!==200){res.resume();reject(new Error('Alpaca SIP 行情请求失败 HTTP '+res.statusCode));return;}
      let body='';
      res.setEncoding('utf8');res.on('data',chunk=>{body+=chunk;if(body.length>4000000)req.destroy(new Error('行情响应超出上限'));});
      res.on('end',()=>{try{const p=JSON.parse(body);if(p.next_page_token)throw new Error('行情响应未完整取回');if(!p.bars)throw new Error('行情响应缺少日线');resolve(p.bars);}catch(e){reject(new Error('Alpaca 行情结构不完整'));}});
      res.on('error',()=>reject(new Error('Alpaca 行情传输中断')));
    });
    req.setTimeout(20000,()=>req.destroy(new Error('Alpaca 行情请求超时')));
    req.on('error',()=>reject(new Error('Alpaca 行情连接失败，请检查本机连接后重试')));
  });
}
async function refresh(){
  const headers=credentials(),now=Date.now();
  const [raw,adjusted]=await Promise.all([getBars('raw',headers,now),getBars('all',headers,now)]);
  const quotes=[];
  for(const item of instruments.filter(x=>x.kind!=='volatility')){
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
if(require.main===module){
  readline.createInterface({input:process.stdin}).on('line',async line=>{
    let m;try{m=JSON.parse(line);}catch(_){return;}
    if(m.id==null)return;
    if(m.method!=='market.refresh'){process.stdout.write(JSON.stringify({jsonrpc:'2.0',id:m.id,error:{code:-32601,message:'未知只读行情方法'}})+'\n');return;}
    try{process.stdout.write(JSON.stringify({jsonrpc:'2.0',id:m.id,result:await refresh()})+'\n');}
    catch(e){process.stdout.write(JSON.stringify({jsonrpc:'2.0',id:m.id,error:{code:-32000,message:e.code==='ENOENT'?'未找到已有 Alpaca 本机配置':e.message}})+'\n');}
  });
}
module.exports={refresh};
