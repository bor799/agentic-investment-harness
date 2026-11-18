(function (root) {
  'use strict';
  /* instruments: symbol → 展示与采集分组。
   * kind: market/metal/credit/volatility/sector/pool/aux
   * history: 'core3y'（核心序列，3 年）| 'pool10mo'（研究池，约 10 个月）
   * volatility 系列不走 Alpaca/Yahoo，由 CBOE 官方 CSV 接入。 */
  const instruments = [
    ['SPY', '标普 500 · ETF代理', 'market', 'core3y'], ['QQQ', '纳斯达克 100 · ETF代理', 'market', 'core3y'],
    ['IWM', '小盘股 · ETF代理', 'market', 'core3y'], ['GLD', '黄金 · ETF代理', 'metal', 'core3y'],
    ['SLV', '白银 · ETF代理', 'metal', 'core3y'], ['CPER', '铜 · 期货基金代理', 'metal', 'core3y'],
    ['JNK', '高收益债 · JNK', 'credit', 'core3y'], ['HYG', '高收益债 · HYG', 'credit', 'core3y'],
    ['^VIX', 'VIX · 隐含波动率', 'volatility', 'core3y'], ['^VIX3M', 'VIX3M · 三月隐含波动率', 'volatility', 'core3y'], ['^VVIX', 'VVIX · 波动率的波动率', 'volatility', 'core3y'],
    ['XLK', '科技 · ETF代理', 'sector', 'core3y'], ['XLF', '金融 · ETF代理', 'sector', 'core3y'],
    ['XLE', '能源 · ETF代理', 'sector', 'core3y'], ['XLI', '工业 · ETF代理', 'sector', 'core3y'],
    ['XLV', '医疗 · ETF代理', 'sector', 'core3y'], ['XLY', '可选消费 · ETF代理', 'sector', 'core3y'],
    ['XLP', '必选消费 · ETF代理', 'sector', 'core3y'], ['XLU', '公用事业 · ETF代理', 'sector', 'core3y'],
    ['XLC', '通信 · ETF代理', 'sector', 'core3y'], ['XLB', '材料 · ETF代理', 'sector', 'core3y'],
    ['XLRE', '房地产 · ETF代理', 'sector', 'core3y'],
    ['TSLL', '特斯拉杠杆 · 辅助观察', 'aux', 'pool10mo'], ['SOXX', '半导体 · 辅助观察', 'aux', 'pool10mo'],
    ['IEF', '中期国债 · 辅助观察', 'aux', 'pool10mo'],
    ['TER', 'Teradyne', 'pool', 'pool10mo'], ['AVGO', 'Broadcom', 'pool', 'pool10mo'],
    ['UNH', 'UnitedHealth', 'pool', 'pool10mo'], ['SILJ', '白银矿商', 'pool', 'pool10mo'],
    ['APP', 'AppLovin', 'pool', 'pool10mo'], ['BWXT', 'BWX Technologies', 'pool', 'pool10mo'],
    ['VST', 'Vistra', 'pool', 'pool10mo'], ['LMT', 'Lockheed Martin', 'pool', 'pool10mo'],
    ['LNN', 'Lindsay', 'pool', 'pool10mo'], ['LIN', 'Linde', 'pool', 'pool10mo'],
    ['TRP', 'TC Energy', 'pool', 'pool10mo'], ['WDC', 'Western Digital', 'pool', 'pool10mo'],
    ['CRWV', 'CoreWeave', 'pool', 'pool10mo'], ['MOS', 'Mosaic', 'pool', 'pool10mo'],
    ['GEV', 'GE Vernova', 'pool', 'pool10mo'], ['RCL', 'Royal Caribbean', 'pool', 'pool10mo'],
    ['XAR', 'SPDR 航天国防', 'pool', 'pool10mo'], ['NLR', '铀/核电 ETF', 'pool', 'pool10mo'],
    ['TSLA', 'Tesla', 'pool', 'pool10mo']
  ].map(([symbol, label, kind, history]) => ({ symbol, label, kind, history }));
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

  /* ---- CBOE 官方指数 CSV ----
   * VIX/VIX3M: DATE,OPEN,HIGH,LOW,CLOSE；VVIX: DATE,VVIX。
   * 不套统一 OHLC 模板，两式分别解析；坏行跳过并在 note 中计数。 */
  function parseCboeCsv(text, symbol) {
    const rows = [];
    let bad = 0;
    const lines = String(text || '').split(/\r?\n/);
    for (const line of lines) {
      if (!line || /^[Dd]ATE/.test(line)) continue;
      const cols = line.split(',');
      if (cols.length < 2) { bad++; continue; }
      const date = cols[0].trim();
      if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) { bad++; continue; }
      const closeStr = cols.length >= 5 ? cols[4] : cols[1];
      const close = Number(closeStr);
      if (!finite(close) || close <= 0) { bad++; continue; }
      rows.push({ date, close });
    }
    if (rows.length < 2) throw new Error(symbol + ' CBOE CSV 缺少可用日线');
    rows.sort((a, b) => a.date < b.date ? -1 : 1);
    return { symbol, rows, bad };
  }

  /* ---- FRED CSV ----
   * 形如 observation_date,DGS10；缺失值 '.' 跳过。 */
  function parseFredCsv(text, seriesId) {
    const rows = [];
    let bad = 0;
    const lines = String(text || '').split(/\r?\n/);
    for (const line of lines) {
      if (!line || /^(observation_date|DATE)/i.test(line)) continue;
      const cols = line.split(',');
      if (cols.length < 2) continue;
      const date = cols[0].trim();
      if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) { bad++; continue; }
      const value = Number(cols[1]);
      if (!finite(value)) { bad++; continue; }
      rows.push({ date, value });
    }
    if (rows.length < 2) throw new Error(seriesId + ' FRED CSV 缺少可用观测');
    rows.sort((a, b) => a.date < b.date ? -1 : 1);
    return { seriesId, rows, bad };
  }

  /* 把 CBOE/FRED 行裁剪到最近 N 个日历日，转成 observations */
  function toObservations(rows, valueKey, keepDays) {
    const cutoff = new Date(Date.now() - keepDays * 86400000).toISOString().slice(0, 10);
    return rows.filter(r => r.date >= cutoff).map(r => ({ date: r.date, value: r[valueKey] }));
  }

  root.DeskMarket = { instruments, parseChart, parseCboeCsv, parseFredCsv, toObservations, percent };
  if (typeof module !== 'undefined' && module.exports) module.exports = root.DeskMarket;
})(globalThis);
