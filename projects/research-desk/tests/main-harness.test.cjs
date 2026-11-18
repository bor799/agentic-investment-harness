'use strict';
/* main-harness.test.cjs — 在 vm 沙箱里跑真实 main.js，fake cindy.host 由 node:sqlite 支撑。
 * 覆盖：库迁移、批次幂等/版本化、日记保存与冲突、消息查询与状态、上下文计数、
 * 行情管线（Alpaca fixture + CBOE 成功 + FRED 失败保留缺口）。 */
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const { DatabaseSync } = require('node:sqlite');

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'desk-harness-'));
const db = new DatabaseSync(path.join(tmp, 'desk.sqlite'));

/* ---- fake library（与宿主 db.* 同语义：exec 支持参数、batch 原子） ---- */
function execOne(sql, params) {
  const first = sql.trimStart().split(/\s+/)[0].toUpperCase();
  if (first === 'SELECT' || first === 'WITH') return { rows: db.prepare(sql).all(...(params || [])) };
  const info = db.prepare(sql).run(...(params || []));
  return { changes: info.changes };
}
const fakeLibrary = async req => {
  switch (req.op) {
    case 'open': case 'status': return { ok: true, state: 'ready' };
    case 'db.open': return { ok: true };
    case 'db.migrate': {
      const current = db.prepare('PRAGMA user_version').get().user_version;
      for (const step of req.steps) {
        if (step.toVersion <= current) continue;
        for (const sql of step.sql) db.exec(sql);
        db.exec(`PRAGMA user_version = ${Number(step.toVersion)}`);
      }
      return { ok: true };
    }
    case 'db.exec': return { ok: true, ...execOne(req.sql, req.params) };
    case 'db.batch': {
      db.exec('BEGIN');
      try { for (const s of req.statements) db.prepare(s.sql).run(...(s.params || [])); db.exec('COMMIT'); return { ok: true }; }
      catch (e) { db.exec('ROLLBACK'); return { ok: false, message: e.message }; }
    }
    default: return { ok: false, errorCode: 'UNSUPPORTED', message: 'fake: ' + req.op };
  }
};

/* ---- fixtures ---- */
const CBOE_FIXTURES = {
  'https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv': 'DATE,OPEN,HIGH,LOW,CLOSE\n2026-11-14,16.8,17.2,16.5,17.0\n2026-11-17,17.1,17.4,16.9,17.3\n',
  'https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VIX3M_History.csv': 'DATE,OPEN,HIGH,LOW,CLOSE\n2026-11-14,18.0,18.3,17.8,18.1\n2026-11-17,18.1,18.4,17.9,18.2\n',
  'https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VVIX_History.csv': 'DATE,VVIX\n2026-11-14,85.1\n2026-11-17,84.2\n'
};
const cindyFetchLog = [];
const fakeCindyFetch = async req => {
  cindyFetchLog.push(req.url);
  if (CBOE_FIXTURES[req.url]) return { ok: true, status: 200, truncated: false, body: CBOE_FIXTURES[req.url] };
  if (req.url.includes('fred.stlouisfed.org')) return { ok: false, status: 0, message: 'FRED 请求超时（模拟）' };
  return { ok: false, status: 404, message: 'no fixture ' + req.url };
};
const alpacaQuote = {
  symbol: 'SPY', label: '标普 500 · ETF代理', kind: 'market', status: 'available',
  asOf: '2026-11-17', observedAt: '2026-11-17T21:00:00Z', close: 590.1, change1d: 0.4, return5d: 1.2, return21d: 2.8,
  series: [{ date: '2026-11-14', value: 588.0 }, { date: '2026-11-17', value: 590.1 }],
  provider: 'Alpaca SIP', basis: '回报与曲线：供应商复权收盘', sourceUrl: 'https://docs.alpaca.markets/reference/stockbars'
};

/* ---- captured channel & tool calls ---- */
const posted = [];
const bcInstances = [];
class FakeBC { constructor() { this.onmessage = null; bcInstances.push(this); } postMessage(m) { posted.push(m); } }
const sentResults = [];
let hostHandler = null;
const fakeCindy = {
  library: fakeLibrary,
  fetch: fakeCindyFetch,
  node: { request: async ({ method }) => {
    if (method === 'market.refresh') return { ok: true, result: { quotes: [alpacaQuote] } };
    if (method === 'market.indices') return { ok: true, result: {
      indices: [
        { key: 'VIX', label: 'VIX · 隐含波动率', unit: '点', rows: [{ date: '2026-11-14', close: 17 }, { date: '2026-11-17', close: 17.3 }], bad: 0 },
        { key: 'VIX3M', label: 'VIX3M · 三月隐含波动率', unit: '点', rows: [{ date: '2026-11-14', close: 18.1 }, { date: '2026-11-17', close: 18.2 }], bad: 0 },
        { key: 'VVIX', label: 'VVIX · 波动率的波动率', unit: '点', rows: [{ date: '2026-11-14', close: 85.1 }, { date: '2026-11-17', close: 84.2 }], bad: 0 }
      ],
      macro: [],
      errors: [{ source: 'FRED DGS10', error: '请求超时（模拟）' }]
    } };
    return { ok: false, message: 'unknown method ' + method };
  } },
  send: async m => { sentResults.push(m); },
  onHostMessage: fn => { hostHandler = fn; }
};
const fakeDocument = {
  head: { append(el) { queueMicrotask(() => el.onload && el.onload()); } },
  createElement: () => ({ src: '', onload: null, onerror: null })
};
const context = {
  console, Date, Math, JSON, Map, Set, Promise, Object, Array, Number, String, Boolean, Error,
  TextEncoder, crypto, queueMicrotask, setTimeout, clearTimeout,
  document: fakeDocument, BroadcastChannel: FakeBC,
  DeskMarket: require('../market.js'),
  DeskCore: require('../desk-core.js'),
  fetch: async url => { if (url === '/kv') return { ok: true, json: async () => ({}) }; return { ok: false }; },
  cindy: fakeCindy
};
context.globalThis = context;
vm.createContext(context);
vm.runInContext(fs.readFileSync(path.join(__dirname, '..', 'main.js'), 'utf8'), context);

function toolCall(tool, args) {
  return new Promise(async (resolve, reject) => {
    const callId = 'c' + (sentResults.length + 1);
    await hostHandler({ type: 'tool-call', tool, args, callId });
    const r = sentResults.find(m => m.callId === callId);
    if (!r) { reject(new Error(tool + ' 未交卷')); return; }
    r.ok ? resolve(r.result) : reject(new Error(r.message));
  });
}
async function pageRequest(action, payload) {
  const id = 'p' + (posted.length + 1) + '-' + Math.random().toString(36).slice(2, 6);
  const bc = bcInstances.at(-1);
  return new Promise((resolve, reject) => {
    const started = Date.now();
    const timer = setInterval(() => {
      const hit = posted.find(m => m.type === 'desk-response' && m.id === id);
      if (hit) { clearInterval(timer); hit.ok ? resolve(hit.result) : reject(new Error(hit.error)); }
      else if (Date.now() - started > 5000) { clearInterval(timer); reject(new Error(action + ' 页面请求超时')); }
    }, 5);
    bc.onmessage({ data: { type: 'desk-request', id, action, ...(payload || {}) } });
  });
}
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  await sleep(50); // 等 boot() 完成（脚本 onload + 库迁移）
  /* 迁移生效 */
  assert.equal(db.prepare('PRAGMA user_version').get().user_version >= 1, true);
  assert.ok(db.prepare("SELECT name FROM sqlite_master WHERE type='table' AND name='messages'").get(), 'messages 表已建');
  assert.ok(db.prepare("SELECT name FROM sqlite_master WHERE type='table' AND name='notes'").get());

  /* ---- 1. 批次入库与幂等 ---- */
  const batch1 = {
    batch_id: 'twitter-weekly-20261116', kind: 'twitter',
    data_cutoff: '2026-11-15T16:14:48Z',
    coverage: { denominator: 26, succeeded: 21, missing: ['returnoncap', 'ValueStockGeek', 'MicroCapClub', 'lfg_cap', 'riyadosofian'], errors: [] },
    items: [
      { logical_id: 'tw-bull-oguzerkan-20261116', kind: 'opinion', category: 'external_opinion', title: 'oguzerkan：AI capex 仍看多', body: '代表论点…', author: 'oguzerkan', stance: 'bull', topics: ['AI capex'], symbols: ['AVGO'], importance: 2 },
      { logical_id: 'tw-bear-realroseceline-20261116', kind: 'opinion', category: 'external_opinion', title: 'realroseceline：质疑回报周期', body: '代表论点…', author: 'realroseceline', stance: 'bear', topics: ['AI capex'], importance: 3 }
    ]
  };
  let receipt = await toolCall('ingest_batch', { batch: batch1 });
  assert.equal(receipt.ok, true); assert.equal(receipt.replayed, false);
  assert.equal(receipt.written, 2); assert.equal(receipt.duplicates, 0);
  /* 重放同一批次 → 幂等 */
  receipt = await toolCall('ingest_batch', { batch: batch1 });
  assert.equal(receipt.replayed, true, '同 batch_id 重放应返回原回执');
  assert.equal(db.prepare('SELECT COUNT(*) c FROM messages').get().c, 2, '不产生重复卡');
  /* 同 logical_id 内容变化 → 新版本；查询只见最新版 */
  receipt = await toolCall('ingest_batch', { batch: { batch_id: 'twitter-weekly-20261116-fix', kind: 'twitter', items: [{ ...batch1.items[1], body: '补充论据后的修订' }] } });
  assert.equal(receipt.versioned, 1);
  let updates = await toolCall('list_updates', { view: 'opinions' });
  assert.equal(updates.messages.length, 2);
  const bear = updates.messages.find(m => m.logical_id === 'tw-bear-realroseceline-20261116');
  assert.equal(bear.version, 2); assert.equal(bear.body, '补充论据后的修订');
  /* 非法条目被拒绝并给原因 */
  receipt = await toolCall('ingest_batch', { batch: { batch_id: 'bad-batch-001', kind: 'manual', items: [{ logical_id: 'x', kind: 'event', category: 'fact', title: '', symbols: ['spy'] }] } });
  assert.equal(receipt.rejected.length, 1);
  await assert.rejects(() => toolCall('ingest_batch', { batch: { batch_id: 'bad', kind: 'nope' } }), /批次校验失败/);

  /* ---- 2. 序列入库与查询 ---- */
  receipt = await toolCall('ingest_batch', { batch: { batch_id: 'semis-manual-20261117', kind: 'semis', series: [{ key: 'SEMIS_AI', label: '半导体 AI 主导情绪', provider: 'semiconductor.feargreedchart.com', observations: [{ date: '2026-11-14', value: 71 }] }, { key: 'BAD', observations: [{ date: '2026-13-99', value: 1 }] }] } });
  assert.equal(receipt.rejected.length, 1, '坏观测拒绝');
  assert.equal(db.prepare("SELECT COUNT(*) c FROM observations WHERE series_key='SEMIS_AI'").get().c, 1);
  const semisContext = await toolCall('get_desk_context', {});
  const aiSlot = semisContext.slots.find(s => s.id === 'semi-ai');
  assert.equal(aiSlot.status, 'ok', '已入库情绪指标必须在观察槽位可见');
  assert.equal(aiSlot.parts[0].value, 71);
  assert.equal(aiSlot.parts[0].date, '2026-11-14');
  assert.equal(aiSlot.parts[0].provider, 'semiconductor.feargreedchart.com');

  /* ---- 3. 日记：通道保存 → 更新 → 冲突 ---- */
  const bc = bcInstances.at(-1);
  assert.ok(bc, '应有通道实例');
  let note = await pageRequest('notes.save', { input: { text: '观察：金银比走高，我想验证是否压制白银。', topics: ['金银'], verify_date: '2026-11-10', verify_question: '比值是否回落' } });
  assert.equal(note.action, 'insert'); assert.equal(note.revision, 1);
  const noteId = note.note_id;
  note = await pageRequest('notes.save', { input: { note_id: noteId, base_revision: 1, text: '补充：如果 SLV 相对 GLD 走弱则减仓观察。' } });
  assert.equal(note.action, 'update'); assert.equal(note.revision, 2);
  note = await pageRequest('notes.save', { input: { note_id: noteId, base_revision: 1, text: '过期的编辑' } });
  assert.equal(note.action, 'conflict', '旧 base 修订必须冲突，不静默覆盖');
  assert.ok(note.server.text.includes('补充'));
  const notes = await pageRequest('notes.list', { query: {} });
  assert.equal(notes.notes.length, 1); assert.equal(notes.notes[0].revision, 2);
  /* 到期验证进入 needs 视图与上下文计数 */
  const ctx = await toolCall('get_desk_context');
  assert.equal(ctx.counts.verify_due, 1, 'verify_date 已过期应计入到期');
  assert.equal(ctx.counts.verify_open, 1);
  assert.ok(ctx.slots.length === 12);
  assert.ok(Array.isArray(ctx.pool_symbols) && ctx.pool_symbols.length === 20);

  /* ---- 4. 消息状态 ---- */
  await pageRequest('message.mark', { input: { logical_id: 'tw-bull-oguzerkan-20261116', action: 'read' } });
  updates = await toolCall('list_updates', { view: 'opinions' });
  assert.equal(updates.messages.find(m => m.logical_id === 'tw-bull-oguzerkan-20261116').read, true);

  /* ---- 5. AI 草稿：独立保存，不覆盖原文 ---- */
  const draft = await toolCall('submit_note_draft', { text: 'AI 整理：观察=金银比走高；待验证=11-30 比值', topics: ['金银'], symbols: ['SLV'] });
  assert.equal(draft.ok, true);
  const activeNotes = await pageRequest('notes.list', { query: {} });
  assert.equal(activeNotes.notes.length, 1, '草稿不进入 active 日记列表');

  /* ---- 6. 行情管线：Alpaca fixture + CBOE 成功 + FRED 失败保留缺口 ---- */
  const snap = await toolCall('refresh_market', {});
  assert.equal(snap.quotes.filter(q => q.status !== 'missing').length, 1, '只有 SPY 可用，其余 Yahoo 失败保留缺口');
  assert.equal(snap.quotes.length, 41, '缺项以 missing 条目保留（41 个非波动率标的），不静默消失');
  assert.equal(snap.indices.length, 3, 'CBOE 三指数');
  assert.equal(snap.macro.length, 0, 'FRED 失败 → 宏观缺口，不冒充');
  assert.ok(snap.errors.some(e => (e.source || '').includes('FRED')), 'FRED 失败要留下缺口记录');
  const spy = db.prepare("SELECT COUNT(*) c FROM observations WHERE series_key='SPY'").get().c;
  assert.ok(spy >= 2, 'SPY 观测入库');
  const vix = db.prepare("SELECT value FROM observations WHERE series_key='VIX' AND date='2026-11-17'").get();
  assert.equal(vix.value, 17.3);
  const runs = await pageRequest('runs.list', {});
  assert.ok(runs.runs.length >= 1 && runs.runs[0].summary.includes('宏观 0/4'));
  /* 同日重复刷新 → 同 batch_id 幂等，观测不翻倍 */
  await toolCall('refresh_market', {});
  const spy2 = db.prepare("SELECT COUNT(*) c FROM observations WHERE series_key='SPY'").get().c;
  assert.equal(spy2, spy, 'INSERT OR REPLACE 不产生重复观测');

  /* ---- 7. get_snapshot 兼容 ---- */
  const cached = await toolCall('get_snapshot', {});
  assert.equal(cached.db_ready, true);
  assert.ok(Array.isArray(cached.quotes));

  console.log('PASS: 迁移、幂等与版本化、序列校验、日记保存/更新/冲突、needs 计数、消息状态、AI 草稿隔离、行情管线缺口诚实、观测不重复');
})().catch(e => { console.error('FAIL:', e.message, e.stack); process.exit(1); });
