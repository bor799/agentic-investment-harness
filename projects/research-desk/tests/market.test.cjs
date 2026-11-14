const assert=require('node:assert/strict');
const {parseChart,instruments}=require('../market.js');
const base=Date.UTC(2025,0,1)/1000;
function payload(n=70){return {chart:{result:[{timestamp:Array.from({length:n},(_,i)=>base+i*86400),meta:{currency:'USD'},indicators:{quote:[{close:Array.from({length:n},(_,i)=>100+i)}],adjclose:[{adjclose:Array.from({length:n},(_,i)=>50+i/2)}]}}]}};}
const now=(base+72*86400)*1000;
let p=payload(),q=parseChart(p,instruments[0],now);
assert.equal(q.close,169);assert.ok(Math.abs(q.return5d-(169/164-1)*100)<1e-10);assert.equal(q.drawdown63,0);assert.equal(q.series.length,70);
p=payload();p.chart.result[0].indicators.quote[0].close[69]=null;q=parseChart(p,instruments[0],now);assert.equal(q.close,168);assert.equal(q.series.length,69);
p=payload();p.chart.result[0].indicators.adjclose[0].adjclose[0]=null;q=parseChart(p,instruments[0],now);assert.ok(q.basis.includes('不含分配'));assert.equal(q.series[0].value,100);
p=payload();p.chart.result[0].meta.currentTradingPeriod={regular:{start:base+69*86400,end:base+69*86400+23400}};q=parseChart(p,instruments[0],(base+69*86400+1000)*1000);assert.equal(q.close,168);
q=parseChart(payload(2),instruments[0],now);assert.equal(q.return21d,null);assert.equal(q.ma50Distance,null);assert.equal(q.drawdown63,null);assert.equal(q.volatility20,null);assert.equal(q.status,'stale');
assert.throws(()=>parseChart({chart:{error:{description:'rate limited'}}},instruments[0],now),/rate limited/);
console.log('PASS: returns, missing values, adjustment fallback, unfinished session exclusion, insufficient history, stale data, provider errors');
