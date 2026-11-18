const assert = require('node:assert/strict');
const { parseChart, parseCboeCsv, parseFredCsv, toObservations, instruments } = require('../market.js');

/* ---- parseChart（沿用 v1 全部边界用例） ---- */
const base = Date.UTC(2025, 0, 1) / 1000;
function payload(n = 70) { return { chart: { result: [{ timestamp: Array.from({ length: n }, (_, i) => base + i * 86400), meta: { currency: 'USD' }, indicators: { quote: [{ close: Array.from({ length: n }, (_, i) => 100 + i) }], adjclose: [{ adjclose: Array.from({ length: n }, (_, i) => 50 + i / 2) }] } }] } }; }
const now = (base + 72 * 86400) * 1000;
let p = payload(), q = parseChart(p, instruments[0], now);
assert.equal(q.close, 169); assert.ok(Math.abs(q.return5d - (169 / 164 - 1) * 100) < 1e-10); assert.equal(q.drawdown63, 0); assert.equal(q.series.length, 70);
p = payload(); p.chart.result[0].indicators.quote[0].close[69] = null; q = parseChart(p, instruments[0], now); assert.equal(q.close, 168); assert.equal(q.series.length, 69);
p = payload(); p.chart.result[0].indicators.adjclose[0].adjclose[0] = null; q = parseChart(p, instruments[0], now); assert.ok(q.basis.includes('不含分配')); assert.equal(q.series[0].value, 100);
p = payload(); p.chart.result[0].meta.currentTradingPeriod = { regular: { start: base + 69 * 86400, end: base + 69 * 86400 + 23400 } }; q = parseChart(p, instruments[0], (base + 69 * 86400 + 1000) * 1000); assert.equal(q.close, 168);
q = parseChart(payload(2), instruments[0], now); assert.equal(q.return21d, null); assert.equal(q.ma50Distance, null); assert.equal(q.drawdown63, null); assert.equal(q.volatility20, null); assert.equal(q.status, 'stale');
assert.throws(() => parseChart({ chart: { error: { description: 'rate limited' } } }, instruments[0], now), /rate limited/);
/* v2 边界：缺口不压缩、验证过的收盘纳入 */
const start = Date.UTC(2026, 9, 1) / 1000;
const chart = closes => ({ chart: { result: [{ timestamp: closes.map((_, i) => start + 86400 * i), meta: { currency: 'USD' }, indicators: { quote: [{ close: closes }], adjclose: [{ adjclose: closes }] } }] } });
q = parseChart(chart([100, null, 110]), instruments[0], (start + 86400 * 4) * 1000); assert.equal(q.change1d, null); assert.equal(q.missingBars, 1);
q = parseChart(chart([100, 105, 110]), instruments[0], (start + 86400 * 2 + 1000) * 1000); assert.equal(q.close, 105);
const p2 = chart([100, 105, 110]); p2.chart.result[0].meta.currentTradingPeriod = { regular: { start: start + 86400 * 2, end: start + 86400 * 2 + 500 } };
q = parseChart(p2, instruments[0], (start + 86400 * 2 + 1000) * 1000); assert.equal(q.close, 110);
/* 研究池与研究池辅助均已入 instruments */
for (const sym of ['TER', 'AVGO', 'CRWV', 'TSLA', 'SOXX', 'TSLL', 'IEF']) assert.ok(instruments.some(i => i.symbol === sym), sym + ' 应在 instruments');
assert.equal(instruments.filter(i => i.kind === 'volatility').length, 3, 'VIX/VIX3M/VVIX 三个波动率指数');

/* ---- CBOE CSV 解析：OHLC 与单列两种格式分别处理，不套统一模板 ---- */
const vixCsv = ['DATE,OPEN,HIGH,LOW,CLOSE', '2026-01-02,16.8,17.2,16.5,17.0', '2026-01-05,17.1,17.4,16.9,17.3', 'badline', '2026-01-06,17.3,,17.5,'].join('\n');
let parsed = parseCboeCsv(vixCsv, 'VIX');
assert.equal(parsed.rows.length, 2);   // 坏行与缺收流行跳过
assert.equal(parsed.bad, 2);
assert.deepEqual(parsed.rows[0], { date: '2026-01-02', close: 17 });
const vvixCsv = ['DATE,VVIX', '2026-01-02,85.1', '2026-01-05,84.2'].join('\n');
parsed = parseCboeCsv(vvixCsv, 'VVIX');
assert.deepEqual(parsed.rows, [{ date: '2026-01-02', close: 85.1 }, { date: '2026-01-05', close: 84.2 }]);
assert.throws(() => parseCboeCsv('DATE,CLOSE\nonly-header', 'VIX'), /缺少可用日线/);

/* ---- FRED CSV：缺失值 '.' 跳过，不补零不插值 ---- */
const fredCsv = ['observation_date,DGS10', '2026-01-02,4.25', '2026-01-05,.', '2026-01-06,4.31'].join('\n');
parsed = parseFredCsv(fredCsv, 'DGS10');
assert.equal(parsed.rows.length, 2);
assert.deepEqual(parsed.rows[1], { date: '2026-01-06', value: 4.31 });

/* ---- toObservations：按日历窗口裁剪 ---- */
const rows = [{ date: '2020-01-01', close: 1 }, { date: '2026-11-10', close: 2 }, { date: '2026-11-16', close: 3 }];
const obs = toObservations(rows, 'close', 30);
assert.equal(obs.length, 2);
assert.equal(obs[0].date, '2026-11-10');

console.log('PASS: parseChart 边界、池覆盖、CBOE 双格式、FRED 缺失值、观测裁剪');
