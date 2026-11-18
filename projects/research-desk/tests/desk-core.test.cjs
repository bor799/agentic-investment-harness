const assert = require('node:assert/strict');
const Core = require('../desk-core.js');

/* ---- 批次契约 ---- */
assert.equal(Core.validateBatch({ batch_id: 'market-2026-11-17', kind: 'market' }).ok, true);
assert.equal(Core.validateBatch({ batch_id: 'x', kind: 'market' }).ok, false, 'batch_id 过短要拒绝');
assert.equal(Core.validateBatch({ batch_id: 'market-2026-11-17', kind: 'nonsense' }).ok, false);
assert.equal(Core.validateBatch({ batch_id: 'a;b', kind: 'market' }).ok, false, '非法字符要拒绝');
assert.equal(Core.validateBatch({ batch_id: 'ok-batch', kind: 'manual', window: { start: 'not-a-date' } }).ok, false);

let r = Core.validateItem({ logical_id: 'evt-1', kind: 'event', category: 'fact', title: '测试' }, 0);
assert.equal(r.ok, true);
r = Core.validateItem({ logical_id: 'evt-1', kind: 'event', category: 'rumor', title: 'x' }, 0);
assert.equal(r.ok, false);
r = Core.validateItem({ logical_id: 'evt-1', kind: 'event', category: 'fact', title: 'x', url: 'http://insecure' }, 0);
assert.equal(r.ok, false, 'http url 拒绝');
r = Core.validateItem({ logical_id: 'evt-1', kind: 'event', category: 'fact', title: 'x', symbols: ['SPY', ' lowercase'] }, 0);
assert.equal(r.ok, false, '小写 symbols 拒绝');

/* 内容哈希稳定性：字段顺序无关，批次无关 */
const a = Core.normalizeItem({ logical_id: 'x1', kind: 'opinion', category: 'external_opinion', title: 'A', body: 'b', topics: ['t1', 't2'], symbols: ['SPY'] }, { batch_id: 'B1' });
const b = Core.normalizeItem({ logical_id: 'x1', kind: 'opinion', category: 'external_opinion', title: 'A', body: 'b', topics: ['t2', 't1'], symbols: ['SPY'] }, { batch_id: 'B2' });
assert.equal(a.content_hash, b.content_hash, 'topics 排序后哈希应一致');
const c = Core.normalizeItem({ ...a, body: 'changed' }, { batch_id: 'B1' });
assert.notEqual(a.content_hash, c.content_hash);

/* ---- 序列校验 ---- */
assert.equal(Core.validateSeries({ key: 'SPY', observations: [{ date: '2026-11-14', value: 570 }] }, 0).ok, true);
assert.equal(Core.validateSeries({ key: 'SPY', observations: [{ date: '2026/11/14', value: 1 }] }, 0).ok, false);
assert.equal(Core.validateSeries({ key: 'SPY', observations: [{ date: '2026-11-14', value: NaN }] }, 0).ok, false);

/* ---- 槽位状态：缺失保留槽位、诚实缺口；金银比显式口径 ---- */
const slots = Core.SLOTS;
assert.equal(slots.length, 12, '固定 12 个槽位');
assert.deepEqual(slots.map(s => s.id), ['market', 'vix', 'vvix', 'vix3m', 'credit', 'rates', 'dollar', 'metals', 'gsr', 'semi-ai', 'semi-broad', 'semi-cycle'], '槽位顺序固定');
let st = Core.slotStatus(slots[1], {});
assert.equal(st.status, 'missing');
st = Core.slotStatus(slots[8], { GLD: { observations: [{ date: '2026-11-14', value: 300 }, { date: '2026-11-17', value: 305 }], provider: 'Alpaca' }, SLV: { observations: [{ date: '2026-11-14', value: 30 }, { date: '2026-11-17', value: 31 }], provider: 'Alpaca' } });
assert.equal(st.status, 'ok');
assert.equal(st.derived.value, 9.839);
assert.ok(st.derived.note.includes('ETF'), '金银比必须注明 ETF 口径');
/* 日期不齐 → 不显示派生值 */
st = Core.slotStatus(slots[8], { GLD: { observations: [{ date: '2026-11-17', value: 305 }] }, SLV: { observations: [{ date: '2026-11-14', value: 31 }] } });
assert.equal(st.derived, null);
/* VIX/VIX3M 比值同理 */
st = Core.slotStatus(slots[3], { VIX: { observations: [{ date: '2026-11-14', value: 16 }] }, VIX3M: { observations: [{ date: '2026-11-14', value: 18 }] } });
assert.equal(st.derived.value, 0.889);

/* 半导体三槽位读取已登记序列；缺失时保留原来源卡。 */
for (const [id, key, value] of [['semi-ai', 'SEMIS_AI', 38], ['semi-broad', 'SEMIS_BROAD', 41], ['semi-cycle', 'SEMIS_CYCLE', 81]]) {
  const slot = slots.find(s => s.id === id);
  assert.equal(Core.slotStatus(slot, {}).status, 'missing');
  const visible = Core.slotStatus(slot, { [key]: { observations: [{ date: '2026-11-17', value }], provider: 'semiconductor.feargreedchart.com', basis: '外部模型观点，非官方统计' } });
  assert.equal(visible.status, 'ok');
  assert.equal(visible.parts[0].value, value);
  assert.equal(visible.parts[0].date, '2026-11-17');
  assert.equal(visible.parts[0].basis, '外部模型观点，非官方统计');
  assert.equal(visible.sourceCard.provider, 'semiconductor.feargreedchart.com');
}

/* ---- 日记冲突：不静默最后写入覆盖 ---- */
assert.equal(Core.noteSavePlan(null, { text: 'a' }).action, 'insert');
const existing = { revision: 3, text_original: 'server text' };
assert.equal(Core.noteSavePlan(existing, { text: 'server text', base_revision: 3 }).action, 'noop');
assert.equal(Core.noteSavePlan(existing, { text: 'new', base_revision: 3 }).action, 'update');
assert.equal(Core.noteSavePlan(existing, { text: 'new', base_revision: 1 }).action, 'conflict');
assert.equal(Core.noteSavePlan(existing, { text: 'server text', base_revision: 1 }).action, 'noop', '内容一致时旧 base 也无害');

/* ---- 覆盖率：21/26 不能叫全量 ---- */
const cov = Core.coverageSummary({ denominator: 26, succeeded: 21, missing: ['returnoncap'], errors: [] });
assert.equal(cov.pct, 80.8);
assert.deepEqual(cov.missing, ['returnoncap']);

/* ---- 导出 markdown 结构 ---- */
const md = Core.notesToMarkdown([{ id: 'n1', created_at: '2026-11-17T09:00:00Z', text_original: '观察：金银比走高', topics: ['金银'], symbols: ['SLV'], verify_date: '2026-11-30', verify_question: '比值是否回落', outcome: null, context: { sources: [{ title: 'CBOE VIX', url: 'https://x' }] } }], '2026-11-17T12:00:00Z');
assert.ok(md.includes('# 投资日记导出'));
assert.ok(md.includes('下一验证：2026-11-30 — 比值是否回落'));
assert.ok(md.includes('观察：金银比走高'));
assert.ok(md.includes('https://x'));

console.log('PASS: 批次契约、哈希稳定性、槽位固定顺序与诚实缺口、金银比口径、日记冲突、覆盖率口径、导出结构');
