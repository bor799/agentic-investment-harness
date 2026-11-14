'use strict';
const ready = new Promise((resolve,reject) => {
  const script=document.createElement('script');script.src='market.js';
  script.onload=resolve;script.onerror=()=>reject(new Error('行情计算模块加载失败'));document.head.append(script);
});
const channel=new BroadcastChannel('murphy-research-desk-v1');
let snapshot=null, inFlight=null;
const replies=new Map();
async function loadSnapshot(){
  if(!snapshot)try { const kv=await (await fetch('/kv')).json(); if(kv?.snapshot?.quotes) snapshot=kv.snapshot; } catch (_) {}
  if(snapshot)snapshot={...snapshot,quotes:snapshot.quotes.map(q=>({...q,status:q.status==='available' && (!Number.isFinite(Date.parse(q.observedAt)) || Date.now()-Date.parse(q.observedAt)>5*86400000)?'stale':q.status}))};
  return snapshot || {fetchedAt:null,quotes:[],errors:[],note:'尚未获取行情，请点击刷新。'};
}
async function refresh(callId){
  if(inFlight) return inFlight;
  inFlight=(async()=>{
    await ready;
    const previous=await loadSnapshot(), quotes=[], errors=[];
    // Reuse Murphy's existing local read-only Alpaca connection. Credentials stay
    // inside the Node process and go only to data.alpaca.markets.
    try {
      const local=await cindy.node.request({method:'market.refresh',params:{},timeoutMs:45000,...(callId?{callId}:{})});
      if(!local.ok || !local.result?.quotes)throw new Error(local.message||'本机行情连接未返回数据');
      quotes.push(...local.result.quotes);
    }catch(e){errors.push({symbol:'Alpaca SIP',error:'本机已有行情连接暂不可用；尝试公开行情。'});}
    const pending=DeskMarket.instruments.filter(item=>!quotes.some(q=>q.symbol===item.symbol));
    let cursor=0;
    await Promise.all(Array.from({length:3},async()=>{
      while(cursor<pending.length){
        const item=pending[cursor++];
        try {
          const response=await cindy.fetch({url:'https://query1.finance.yahoo.com/v8/finance/chart/'+encodeURIComponent(item.symbol)+'?interval=1d&range=6mo',
            method:'GET',as:'text',timeoutMs:6000,...(callId?{callId}:{})});
          if(!response.ok || response.status!==200 || response.truncated) throw new Error(response.message || '行情请求失败 HTTP '+response.status);
          quotes.push(DeskMarket.parseChart(JSON.parse(response.body),item));
        }catch(e){
          const error=String(e.message||e).slice(0,200), old=previous.quotes.find(q=>q.symbol===item.symbol);
          quotes.push(old ? {...old,status:'stale',error} : {...item,status:'missing',close:null,asOf:null,series:[],error});
          errors.push({symbol:item.symbol,error});
        }
      }
    }));
    quotes.sort((a,b)=>DeskMarket.instruments.findIndex(x=>x.symbol===a.symbol)-DeskMarket.instruments.findIndex(x=>x.symbol===b.symbol));
    snapshot={fetchedAt:new Date().toISOString(),quotes,errors,note:'已完成日线及部分派生观测；本机 Alpaca SIP 优先，缺项尝试 Yahoo。保守排除 UTC 当天未核验收盘的日线。信用利差、公司财务和完整市场广度尚未接入。'};
    try {
      const cached={...snapshot,quotes:snapshot.quotes.map(q=>({...q,series:q.series.slice(-32).map(p=>({...p,value:Number(p.value.toFixed(6))}))}))};
      const body=JSON.stringify({snapshot:cached});
      if(new TextEncoder().encode(body).length>64000) throw new Error('快照超过存储上限');
      const r=await fetch('/kv',{method:'POST',headers:{'Content-Type':'application/json'},body});if(!r.ok) throw new Error('HTTP '+r.status);
    }
    catch(e){ snapshot.storageWarning='快照保存失败；本次显示有效，重开后需重新刷新：'+e.message; }
    return snapshot;
  })().finally(()=>{inFlight=null;});
  return inFlight;
}
channel.onmessage=async({data:m})=>{
  if(m?.type!=='desk-request'||typeof m.id!=='string'||!['snapshot','refresh'].includes(m.action))return;
  if(replies.has(m.id)){const cached=replies.get(m.id);if(cached)channel.postMessage(cached);return;}
  replies.set(m.id,null);
  let answer;
  try{answer={type:'desk-response',id:m.id,ok:true,snapshot:await(m.action==='refresh'?refresh():loadSnapshot())};}
  catch(e){answer={type:'desk-response',id:m.id,ok:false,error:'数据更新失败：'+e.message+'。请稍后重试，原有指标目录仍可浏览。'};}
  replies.set(m.id,answer);if(replies.size>100)replies.delete(replies.keys().next().value);channel.postMessage(answer);
};
cindy.onHostMessage(async msg=>{
  if(msg.type!=='tool-call')return;
  try{
    if(!['get_snapshot','refresh_market'].includes(msg.tool))throw new Error('未知工具');
    const data=await(msg.tool==='refresh_market'?refresh(msg.callId):loadSnapshot());
    const compact={...data,quotes:data.quotes.map(({series,...q})=>({...q,observations:series?.length||0}))};
    await cindy.send({type:'tool-result',callId:msg.callId,ok:true,result:compact});
  }catch(e){await cindy.send({type:'tool-result',callId:msg.callId,ok:false,message:'获取观察台数据失败：'+e.message+'。请稍后重试。'});}
});
