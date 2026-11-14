(function (root) {
  'use strict';
  const instruments = [
    ['SPY', '标普 500 · ETF代理', 'market'], ['QQQ', '纳斯达克 100 · ETF代理', 'market'],
    ['IWM', '小盘股 · ETF代理', 'market'], ['GLD', '黄金 · ETF代理', 'metal'],
    ['SLV', '白银 · ETF代理', 'metal'], ['CPER', '铜 · 期货基金代理', 'metal'],
    ['JNK', '高收益债 · JNK', 'credit'], ['HYG', '高收益债 · HYG', 'credit'],
    ['^VIX', 'VIX · 隐含波动率', 'volatility'], ['^VIX3M', 'VIX3M · 三月隐含波动率', 'volatility'],
    ['XLK', '科技 · ETF代理', 'sector'], ['XLF', '金融 · ETF代理', 'sector'],
    ['XLE', '能源 · ETF代理', 'sector'], ['XLI', '工业 · ETF代理', 'sector'],
    ['XLV', '医疗 · ETF代理', 'sector'], ['XLY', '可选消费 · ETF代理', 'sector'],
    ['XLP', '必选消费 · ETF代理', 'sector'], ['XLU', '公用事业 · ETF代理', 'sector'],
    ['XLC', '通信 · ETF代理', 'sector'], ['XLB', '材料 · ETF代理', 'sector'],
    ['XLRE', '房地产 · ETF代理', 'sector']
  ].map(([symbol, label, kind]) => ({symbol, label, kind}));
  const finite = n => typeof n === 'number' && Number.isFinite(n);
  const percent = (a, b) => finite(a) && finite(b) && b > 0 ? (a / b - 1) * 100 : null;
  function parseChart(payload, instrument, now = Date.now()) {
    const chart = payload && payload.chart;
    if (chart?.error) throw new Error(chart.error.description || '行情源返回错误');
    const r = chart?.result?.[0];
    if (!r?.timestamp?.length || !r.indicators?.quote?.[0]) throw new Error('行情源缺少日线数据');
    const q = r.indicators.quote[0], adjusted = r.indicators.adjclose?.[0]?.adjclose;
    const regular = r.meta?.currentTradingPeriod?.regular;
    const clockKnown=finite(regular?.start)&&finite(regular?.end);
    // Without a verified exchange close clock, today's bar is provisional.
    const today=new Date(now).toISOString().slice(0,10);
    const rows = r.timestamp.map((t, i) => ({t, date:finite(t)?new Date(t * 1000).toISOString().slice(0, 10):'', raw:q.close[i], adjusted:adjusted?.[i]}))
      .filter(p => finite(p.t) && p.t * 1000 <= now)
      .filter(p => clockKnown ? !(now < regular.end * 1000 && p.t >= regular.start) : p.date < today);
    while(rows.length && !(finite(rows.at(-1).raw)&&rows.at(-1).raw>0))rows.pop();
    if (rows.length < 2) throw new Error('已完成交易日日线不足');
    const valid=p=>finite(p.raw)&&p.raw>0;
    const hasAdjusted = !!adjusted && rows.filter(valid).every(p => finite(p.adjusted) && p.adjusted > 0);
    const series = rows.filter(valid).map(p => ({date:p.date, value:hasAdjusted ? p.adjusted : p.raw}));
    const last = rows.at(-1), end = series.at(-1).value;
    const ret = n => rows.length > n && rows.slice(-n-1).every(valid) ? percent(end, hasAdjusted?rows.at(-n-1).adjusted:rows.at(-n-1).raw) : null;
    const raw = rows.map(p => p.raw), mean = ns => ns.reduce((a,b) => a+b,0)/ns.length;
    const last21=raw.slice(-21), logs=last21.slice(1).map((v,i)=>Math.log(v/last21[i]));
    const vol20 = logs.length === 20 && rows.slice(-21).every(valid) ? Math.sqrt(logs.reduce((a,v)=>a+(v-mean(logs))**2,0)/19)*Math.sqrt(252)*100 : null;
    return {...instrument, currency:r.meta?.currency || '未知', asOf:last.date, observedAt:new Date(last.t*1000).toISOString(),
      close:last.raw, change1d:ret(1), return5d:ret(5), return21d:ret(21), return63d:ret(63),
      ma50Distance:raw.length >= 50 && rows.slice(-50).every(valid) ? percent(last.raw,mean(raw.slice(-50))) : null,
      drawdown63:raw.length >= 63 && rows.slice(-63).every(valid) ? percent(last.raw,Math.max(...raw.slice(-63))) : null,
      missingBars:rows.filter(p=>!valid(p)).length,
      volatility20:vol20, series, basis:(hasAdjusted ? '回报与曲线：供应商复权收盘（含分配调整）' : '回报与曲线：收盘价格（不含分配）')+'；现价、MA50距离、63日回撤及RV20：未复权收盘。',
      sourceUrl:'https://finance.yahoo.com/quote/'+encodeURIComponent(instrument.symbol)+'/',
      status:now-last.t*1000 > 5*86400000 ? 'stale' : 'available',
      freshnessNote:'已完成的日线；不是实时盘口。超过5个日历日标记陈旧；休市与发布日需结合来源核对。'};
  }
  root.DeskMarket = {instruments, parseChart, percent};
  if (typeof module !== 'undefined') module.exports = root.DeskMarket;
})(globalThis);
