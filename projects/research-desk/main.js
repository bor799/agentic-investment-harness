'use strict';
/* Murphy Research Desk 电子脑 v2
 * 职责：Library 持久层（desk.sqlite）、批次入库与回执、消息/日记/验证/任务查询、
 * 行情采集（Alpaca 节点 + Yahoo 兜底 + CBOE 指数 + FRED 宏观）、页面通道。
 * 红线：不自动改投资规则与仓位；AI 草稿不覆盖用户原文；回执以持久化为准。
 */
const ready = new Promise((resolve, reject) => {
  let pending = 2;
  const done = () => { if (--pending === 0) resolve(); };
  for (const src of ['market.js', 'desk-core.js']) {
    const script = document.createElement('script');
    script.src = src;
    script.onload = done;
    script.onerror = () => reject(new Error('模块加载失败：' + src));
    document.head.append(script);
  }
});
const channel = new BroadcastChannel('murphy-research-desk-v2');
const DB_PATH = 'desk.sqlite';
const C = () => globalThis.DeskCore;
const M = () => globalThis.DeskMarket;

let booted = null;          // boot promise
let dbReady = false;
let dbDisabledReason = null;
let snapshot = null;        // 行情快照（KV 缓存 + 内存）
let inFlight = null;
const replies = new Map();  // 页面请求去重
const nodeDiag = { lastStatus: null, lastStatusAt: null, ping: null };

/* ---------------- Library DB 层 ---------------- */
async function lib(req) { return cindy.library(req); }
function rowsOf(reply) {
  if (!reply || reply.ok === false) return [];
  if (Array.isArray(reply)) return reply;
  for (const key of ['rows', 'results', 'data', 'statements']) if (Array.isArray(reply[key])) return reply[key];
  const vals = Object.values(reply).filter(Array.isArray);
  if (vals.length === 1) return vals[0];
  return [];
}
async function dbExec(sql, params) {
  const r = await lib({ op: 'db.exec', dbPath: DB_PATH, sql, params: params || [] });
  if (!r || r.ok === false) throw new Error((r && (r.message || r.errorCode)) || 'db.exec 失败');
  return r;
}
async function dbBatch(statements) {
  const r = await lib({ op: 'db.batch', dbPath: DB_PATH, statements });
  if (!r || r.ok === false) throw new Error((r && (r.message || r.errorCode)) || 'db.batch 失败');
  return r;
}
async function dbSelect(sql, params) { return rowsOf(await dbExec(sql, params)); }

async function boot() {
  if (booted) return booted;
  booted = (async () => {
    await ready;
    try {
      await lib({ op: 'open' });
      await lib({ op: 'db.open', dbPath: DB_PATH });
      await lib({ op: 'db.migrate', dbPath: DB_PATH, targetVersion: C().DB_VERSION, steps: C().MIGRATIONS });
      const existing = await dbSelect('SELECT value FROM meta WHERE key = ?', ['pool_version']);
      if (!existing.length) await dbBatch([{ sql: 'INSERT INTO meta (key, value) VALUES (?, ?)', params: ['pool_version', C().POOL.version] }]);
      dbReady = true;
    } catch (e) {
      dbDisabledReason = '持久库不可用：' + (e && e.message ? e.message : String(e)) + '。行情仍可看，日记与消息不可写；不做空库冒充恢复。';
    }
    try { const kv = await (await fetch('/kv')).json(); if (kv?.snapshot?.quotes) snapshot = kv.snapshot; } catch (_) {}
    return { dbReady, dbDisabledReason };
  })();
  return booted;
}

/* ---------------- 序列读取与缓存 ---------------- */
const seriesCache = new Map(); // key → {meta, observations}
const SERIES_TTL = 10 * 60 * 1000;
function parseJsonSafe(text, fallback) { try { return text == null ? fallback : JSON.parse(text); } catch (_) { return fallback; } }
async function getSeriesMap(keys, minPoints) {
  const now = Date.now(), wanted = new Set(keys);
  const result = {};
  const toFetch = [];
  for (const key of keys) {
    const hit = seriesCache.get(key);
    if (hit && now - hit.fetchedAt < SERIES_TTL) result[key] = hit.payload;
    else toFetch.push(key);
  }
  if (toFetch.length && dbReady) {
    const quoted = toFetch.map(k => C().sqlText(k)).join(',');
    const metas = await dbSelect(`SELECT key, label, provider, unit, basis, source_url, latest_date, latest_value, updated_at, status FROM series WHERE key IN (${quoted})`);
    const metaMap = new Map(metas.map(m => [m.key, m]));
    for (const key of toFetch) {
      const meta = metaMap.get(key);
      if (!meta) { seriesCache.set(key, { fetchedAt: now, payload: null }); result[key] = null; continue; }
      const points = await dbSelect(`SELECT date, value FROM observations WHERE series_key = ? ORDER BY date DESC LIMIT ?`, [key, Math.max(minPoints || 800, 30)]);
      const observations = points.reverse();
      const payload = { ...meta, observations };
      seriesCache.set(key, { fetchedAt: now, payload });
      result[key] = payload;
    }
  }
  return result;
}

/* ---------------- 批次入库（幂等 + 版本化） ---------------- */
async function ingestBatch(batch) {
  await boot();
  if (!dbReady) throw new Error(dbDisabledReason || '持久库未就绪');
  const v = C().validateBatch(batch);
  if (!v.ok) return { ok: false, errorCode: 'BATCH_INVALID', message: '批次校验失败：' + v.errors.join('；'), errors: v.errors };
  const existingBatch = await dbSelect('SELECT * FROM batches WHERE batch_id = ?', [batch.batch_id]);
  if (existingBatch.length) {
    const b = existingBatch[0];
    return { ok: true, batch_id: b.batch_id, replayed: true, written: b.written, duplicates: b.duplicates,
      rejected: parseJsonSafe(b.rejected_json, []), item_count: b.item_count,
      note: '相同 batch_id 已入库，返回原回执；未重复写入。' };
  }
  const rejected = [];
  const statements = [];
  const now = C().nowISO();
  let written = 0, duplicates = 0, versioned = 0;
  const items = Array.isArray(batch.items) ? batch.items : [];
  for (let i = 0; i < items.length; i++) {
    const check = C().validateItem(items[i], i);
    if (!check.ok) { rejected.push({ index: i, logical_id: items[i] && items[i].logical_id, reasons: check.rejects }); continue; }
    const item = C().normalizeItem(items[i], batch);
    const prior = await dbSelect('SELECT version, content_hash FROM messages WHERE logical_id = ? ORDER BY version DESC LIMIT 1', [item.logical_id]);
    if (prior.length && prior[0].content_hash === item.content_hash) { duplicates++; continue; }
    const version = prior.length ? prior[0].version + 1 : 1;
    if (prior.length) versioned++;
    statements.push({ sql: `INSERT INTO messages (logical_id, version, content_hash, batch_id, root_source_id, kind, category, title, body, url, author, stance, event_time, published_at, topics_json, symbols_json, importance, actionable, coverage_note, created_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)`,
      params: [item.logical_id, version, item.content_hash, batch.batch_id, item.root_source_id, item.kind, item.category, item.title, item.body, item.url, item.author, item.stance, item.event_time, item.published_at, JSON.stringify(item.topics), JSON.stringify(item.symbols), item.importance, item.actionable, item.coverage_note, now] });
    written++;
  }
  /* 序列观测 */
  const seriesList = Array.isArray(batch.series) ? batch.series : [];
  for (let i = 0; i < seriesList.length; i++) {
    const s = seriesList[i];
    const check = C().validateSeries(s, i);
    if (!check.ok) { rejected.push({ index: i, series: s && s.key, reasons: check.rejects }); continue; }
    const obs = s.observations.filter(o => C().isDate(o.date) && C().isFiniteNumber(o.value)).slice(-1200);
    if (!obs.length) { rejected.push({ index: i, series: s.key, reasons: ['无可写入观测'] }); continue; }
    statements.push({ sql: `INSERT INTO series (key, label, provider, unit, basis, source_url, latest_date, latest_value, updated_at, status) VALUES (?,?,?,?,?,?,?,?,?,?)
      ON CONFLICT(key) DO UPDATE SET label=excluded.label, provider=excluded.provider, unit=excluded.unit, basis=excluded.basis, source_url=excluded.source_url, latest_date=excluded.latest_date, latest_value=excluded.latest_value, updated_at=excluded.updated_at, status=excluded.status`,
      params: [s.key, s.label || s.key, s.provider || null, s.unit || null, s.basis || null, s.source_url || null, obs[obs.length - 1].date, obs[obs.length - 1].value, now, s.status || 'ok'] });
    /* 多行 INSERT：每条语句 ≤80 行观测，控制在宿主 db.batch 200 条语句上限内 */
    for (let i = 0; i < obs.length; i += 80) {
      const slice = obs.slice(i, i + 80);
      const params = [];
      for (const o of slice) params.push(s.key, o.date, o.value);
      statements.push({ sql: `INSERT OR REPLACE INTO observations (series_key, date, value) VALUES ${slice.map(() => '(?,?,?)').join(',')}`, params });
    }
    seriesCache.delete(s.key);
    written++;
  }
  /* 来源登记 */
  for (const src of (Array.isArray(batch.sources) ? batch.sources.slice(0, 60) : [])) {
    if (!src || typeof src.root_id !== 'string' || !src.root_id) continue;
    statements.push({ sql: `INSERT INTO sources (root_id, title, url, provider, kind, first_seen, last_seen) VALUES (?,?,?,?,?,?,?)
      ON CONFLICT(root_id) DO UPDATE SET title=excluded.title, url=excluded.url, provider=excluded.provider, kind=excluded.kind, last_seen=excluded.last_seen`,
      params: [String(src.root_id).slice(0, 160), C().clampText(src.title, 300), /^https:\/\//.test(src.url || '') ? src.url : null, C().clampText(src.provider, 120), C().clampText(src.kind, 40), now, now] });
  }
  statements.push({ sql: `INSERT INTO batches (batch_id, job_id, run_id, kind, window_start, window_end, data_cutoff, sources_json, coverage_json, errors_json, received_at, item_count, written, duplicates, rejected_json) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)`,
    params: [batch.batch_id, C().clampText(batch.job_id, 128), C().clampText(batch.run_id, 128), batch.kind,
      batch.window && batch.window.start || null, batch.window && batch.window.end || null, batch.data_cutoff || null,
      JSON.stringify((batch.sources || []).slice(0, 60)), JSON.stringify(batch.coverage || null), JSON.stringify(batch.errors || []),
      now, items.length + seriesList.length, written, duplicates, JSON.stringify(rejected)] });
  if (batch.run_id) statements.push({ sql: `INSERT OR REPLACE INTO runs (id, task_key, batch_id, started_at, finished_at, status, coverage_json, errors_json, summary) VALUES (?,?,?,?,?,?,?,?,?)`,
    params: [String(batch.run_id).slice(0, 128), C().clampText(batch.task_key, 64) || batch.kind, batch.batch_id, now, now, 'success', JSON.stringify(batch.coverage || null), JSON.stringify(batch.errors || []), `批次入库：写入 ${written}、重复 ${duplicates}、拒绝 ${rejected.length}`] });
  /* 分块写入：宿主 db.batch 单批上限 200 条语句；批次回执行在最后一块，未完成重试幂等 */
  for (let i = 0; i < statements.length; i += 180) await dbBatch(statements.slice(i, i + 180));
  return { ok: true, batch_id: batch.batch_id, replayed: false, written, duplicates, versioned, rejected, item_count: items.length + seriesList.length, received_at: now };
}

/* ---------------- 消息查询 ---------------- */
const VIEW_RULES = {
  needs: "kind IN ('verify','health') AND actionable = 1",
  updates: "kind IN ('event','fact')",
  opinions: "kind = 'opinion'",
  health: "kind = 'health'"
};
async function listUpdates(query) {
  await boot();
  if (!dbReady) throw new Error(dbDisabledReason || '持久库未就绪');
  const q = query || {};
  const limit = Math.min(Math.max(Number(q.limit) || 50, 1), 200);
  const offset = Math.max(Number(q.offset) || 0, 0);
  const where = []; const params = [];
  if (q.view && VIEW_RULES[q.view]) where.push('(' + VIEW_RULES[q.view] + ')');
  if (q.kind) { where.push('kind = ?'); params.push(q.kind); }
  if (q.topic) { where.push("topics_json LIKE ?"); params.push('%' + q.topic.replace(/[%_]/g, '') + '%'); }
  if (q.symbol) { where.push('symbols_json LIKE ?'); params.push('%"' + q.symbol.replace(/[^A-Z0-9.^-]/gi, '') + '"%'); }
  if (q.from) { where.push('created_at >= ?'); params.push(q.from); }
  if (q.to) { where.push('created_at <= ?'); params.push(q.to); }
  const whereSql = where.length ? 'WHERE ' + where.join(' AND ') : '';
  /* 每个逻辑事件取最高版本（修订后旧版本仍可按 logical_id 查询） */
  const rows = await dbSelect(`SELECT m.* FROM messages m JOIN (SELECT logical_id, MAX(version) AS v FROM messages GROUP BY logical_id) latest ON m.logical_id = latest.logical_id AND m.version = latest.v ${whereSql} ORDER BY m.created_at DESC LIMIT ? OFFSET ?`, [...params, limit, offset]);
  const statusRows = rows.length ? await dbSelect(`SELECT * FROM message_status WHERE logical_id IN (${rows.map(r => C().sqlText(r.logical_id)).join(',')})`) : [];
  const statusMap = new Map(statusRows.map(s => [s.logical_id, s]));
  return rows.map(r => ({
    logical_id: r.logical_id, version: r.version, kind: r.kind, category: r.category, title: r.title,
    body: r.body, url: r.url, author: r.author, stance: r.stance, event_time: r.event_time || r.published_at,
    created_at: r.created_at, topics: parseJsonSafe(r.topics_json, []), symbols: parseJsonSafe(r.symbols_json, []),
    importance: r.importance, actionable: !!r.actionable, coverage_note: r.coverage_note, root_source_id: r.root_source_id,
    read: !!(statusMap.get(r.logical_id) || {}).read_at, handled: !!(statusMap.get(r.logical_id) || {}).handled_at,
    handle_action: (statusMap.get(r.logical_id) || {}).handle_action || null, batch_id: r.batch_id
  }));
}

/* ---------------- 上下文（不给 AI 整本日记） ---------------- */
async function getDeskContext() {
  await boot();
  const slotKeys = [...new Set(C().SLOTS.flatMap(s => s.series || []))];
  const seriesMap = dbReady ? await getSeriesMap(slotKeys, 800) : {};
  const slots = C().SLOTS.map(s => C().slotStatus(s, seriesMap));
  const dates = Object.values(seriesMap).filter(Boolean).map(s => s.latest_date).filter(Boolean).sort();
  const out = { generated_at: C().nowISO(), db_ready: dbReady, db_note: dbDisabledReason, pool_version: C().POOL.version, pool_symbols: C().POOL.symbols,
    data_cutoff: dates.length ? dates[dates.length - 1] : null, slots,
    snapshot_fetched_at: snapshot?.fetchedAt || null };
  if (dbReady) {
    const needs = await dbSelect(`SELECT COUNT(*) AS c FROM notes WHERE status = 'active' AND verify_date IS NOT NULL AND verify_date <= date('now','localtime')`, []);
    const pendingVerify = await dbSelect(`SELECT COUNT(*) AS c FROM notes WHERE status = 'active' AND verify_date IS NOT NULL`, []);
    const counts = await dbSelect(`SELECT kind, COUNT(DISTINCT logical_id) AS c FROM messages WHERE created_at >= datetime('now','-7 days') GROUP BY kind`, []);
    const runs = await dbSelect(`SELECT COUNT(*) AS c FROM runs WHERE status = 'failed' AND started_at >= datetime('now','-3 days')`, []);
    const noteCount = await dbSelect(`SELECT COUNT(*) AS c FROM notes`, []);
    out.counts = {
      verify_due: needs[0]?.c || 0, verify_open: pendingVerify[0]?.c || 0, notes: noteCount[0]?.c || 0,
      recent_failures: runs[0]?.c || 0,
      by_kind: Object.fromEntries(counts.map(r => [r.kind, r.c]))
    };
  }
  return out;
}

/* ---------------- 日记 ---------------- */
async function noteGet(id) { const rows = await dbSelect('SELECT * FROM notes WHERE id = ?', [id]); return rows[0] || null; }
async function noteSave(input) {
  await boot();
  if (!dbReady) throw new Error(dbDisabledReason || '持久库未就绪');
  const text = typeof input.text === 'string' ? input.text : '';
  if (!text.trim() && !input.note_id) return { ok: false, errorCode: 'EMPTY_NOTE', message: '日记正文为空，未保存。' };
  const now = C().nowISO();
  const context = input.context && typeof input.context === 'object' ? JSON.stringify({ theme: input.context.theme || null, slot: input.context.slot || null, event: input.context.event || null, sources: (input.context.sources || []).slice(0, 8) }) : null;
  const topics = (input.topics || []).slice(0, 6), symbols = (input.symbols || []).slice(0, 10);
  const existing = input.note_id ? await noteGet(input.note_id) : null;
  const plan = C().noteSavePlan(existing, { text, base_revision: input.base_revision });
  if (plan.action === 'noop') return { ok: true, action: 'noop', note_id: existing.id, revision: existing.revision, saved_at: existing.updated_at };
  if (plan.action === 'conflict') {
    const drafts = await dbSelect(`SELECT version, origin, text, created_at FROM note_versions WHERE note_id = ? ORDER BY version DESC LIMIT 6`, [existing.id]);
    return { ok: true, action: 'conflict', note_id: existing.id, server: { revision: existing.revision, text: existing.text_original, updated_at: existing.updated_at, versions: drafts }, yours: { base_revision: input.base_revision, text }, message: '此日记已被另一端修改。两个版本都已保留，请选择保留哪一版。' };
  }
  if (plan.action === 'insert') {
    const id = input.note_id || ('n' + Date.now().toString(36) + Math.random().toString(36).slice(2, 7));
    await dbBatch([
      { sql: `INSERT INTO notes (id, created_at, updated_at, revision, text_original, topics_json, symbols_json, context_json, verify_date, verify_question, status) VALUES (?,?,?,?,?,?,?,?,?,?,'active')`,
        params: [id, now, now, 1, text, JSON.stringify(topics), JSON.stringify(symbols), context, C().isDate(input.verify_date) ? input.verify_date : null, C().clampText(input.verify_question, 300)] },
      { sql: `INSERT INTO note_versions (note_id, version, origin, text, context_json, created_at) VALUES (?,?, 'user', ?, ?, ?)`, params: [id, 1, text, context, now] }
    ]);
    return { ok: true, action: 'insert', note_id: id, revision: 1, saved_at: now };
  }
  /* update */
  const toRev = plan.to_revision;
  await dbBatch([
    { sql: `UPDATE notes SET updated_at = ?, revision = ?, text_original = ?, topics_json = ?, symbols_json = ?, context_json = COALESCE(?, context_json), verify_date = COALESCE(?, verify_date), verify_question = COALESCE(?, verify_question) WHERE id = ?`,
      params: [now, toRev, text, JSON.stringify(topics), JSON.stringify(symbols), context, C().isDate(input.verify_date) ? input.verify_date : null, C().clampText(input.verify_question, 300), existing.id] },
    { sql: `INSERT INTO note_versions (note_id, version, origin, text, context_json, created_at) VALUES (?,?, 'user', ?, ?, ?)`, params: [existing.id, toRev, text, context, now] }
  ]);
  return { ok: true, action: 'update', note_id: existing.id, revision: toRev, saved_at: now };
}
async function noteList(query) {
  await boot();
  if (!dbReady) return [];
  const limit = Math.min(Math.max(Number(query?.limit) || 60, 1), 300);
  const status = query?.status || 'active';
  const rows = await dbSelect(`SELECT id, created_at, updated_at, revision, text_original, topics_json, symbols_json, context_json, verify_date, verify_question, status, outcome FROM notes WHERE status = ? ORDER BY updated_at DESC LIMIT ?`, [status, limit]);
  return rows.map(r => ({ ...r, topics: parseJsonSafe(r.topics_json, []), symbols: parseJsonSafe(r.symbols_json, []), context: parseJsonSafe(r.context_json, null), text: r.text_original }));
}
async function noteDraft(input) {
  await boot();
  if (!dbReady) throw new Error(dbDisabledReason || '持久库未就绪');
  if (!input || typeof input.text !== 'string' || !input.text.trim()) return { ok: false, errorCode: 'EMPTY_DRAFT', message: '草稿正文为空。' };
  const now = C().nowISO();
  const draftMeta = JSON.stringify({ observation: C().clampText(input.observation, 2000), interpretation: C().clampText(input.interpretation, 2000), to_verify: C().clampText(input.to_verify, 1000), counter_move: C().clampText(input.counter_move, 1000), verify_hint: C().isDate(input.verify_hint) ? input.verify_hint : null });
  if (input.note_id) {
    const existing = await noteGet(input.note_id);
    if (!existing) return { ok: false, errorCode: 'NOTE_NOT_FOUND', message: '目标日记不存在，草稿未写入。' };
    const rows = await dbSelect(`SELECT MAX(version) AS v FROM note_versions WHERE note_id = ? AND origin = 'ai_draft'`, [input.note_id]);
    const v = (rows[0]?.v || 0) + 1;
    await dbBatch([{ sql: `INSERT INTO note_versions (note_id, version, origin, text, context_json, created_at) VALUES (?,?, 'ai_draft', ?, ?, ?)`, params: [input.note_id, v, input.text, draftMeta, now] }]);
    return { ok: true, note_id: input.note_id, draft_version: v, saved_at: now };
  }
  /* 生成锚定草稿：返回草稿 ID，由用户在页面接受后转正 */
  const id = 'd' + Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
  await dbBatch([
    { sql: `INSERT INTO notes (id, created_at, updated_at, revision, text_original, topics_json, symbols_json, context_json, verify_date, verify_question, status) VALUES (?,?,?,?,?,?,?,?,?,?,'draft')`,
      params: [id, now, now, 0, input.text, JSON.stringify((input.topics || []).slice(0, 6)), JSON.stringify((input.symbols || []).slice(0, 10)), draftMeta, null, null] },
    { sql: `INSERT INTO note_versions (note_id, version, origin, text, context_json, created_at) VALUES (?,0,'ai_draft',?,?,?)`, params: [id, input.text, draftMeta, now] }
  ]);
  return { ok: true, note_id: id, draft_version: 0, saved_at: now, message: 'AI 草稿已单独保存；不会覆盖任何用户原文。' };
}
async function noteAcceptDraft(noteId) {
  await boot();
  if (!dbReady) throw new Error(dbDisabledReason || '持久库未就绪');
  const note = await noteGet(noteId);
  if (!note) return { ok: false, errorCode: 'NOTE_NOT_FOUND', message: '日记不存在。' };
  const wasDraft = note.status === 'draft';
  const now = C().nowISO();
  const toRev = note.revision + 1;
  await dbBatch([
    { sql: `UPDATE notes SET status = 'active', revision = ?, updated_at = ? WHERE id = ?`, params: [toRev, now, noteId] },
    { sql: `INSERT INTO note_versions (note_id, version, origin, text, context_json, created_at) VALUES (?,?, 'user', ?, ?, ?)`, params: [noteId, toRev, note.text_original, note.context_json, now] }
  ]);
  return { ok: true, note_id: noteId, revision: toRev, accepted_draft: wasDraft, saved_at: now };
}
async function noteUpdate(input) {
  await boot();
  if (!dbReady) throw new Error(dbDisabledReason || '持久库未就绪');
  const note = input.note_id ? await noteGet(input.note_id) : null;
  if (!note) return { ok: false, errorCode: 'NOTE_NOT_FOUND', message: '日记不存在。' };
  const now = C().nowISO();
  const sets = ['updated_at = ?']; const params = [now];
  if (input.status && ['active', 'done', 'archived'].includes(input.status)) { sets.push('status = ?'); params.push(input.status); }
  if (typeof input.outcome === 'string') { sets.push('outcome = ?'); params.push(C().clampText(input.outcome, 2000)); }
  if (C().isDate(input.verify_date)) { sets.push('verify_date = ?'); params.push(input.verify_date); }
  if (input.verify_question != null) { sets.push('verify_question = ?'); params.push(C().clampText(input.verify_question, 300)); }
  params.push(input.note_id);
  await dbBatch([{ sql: `UPDATE notes SET ${sets.join(', ')} WHERE id = ?`, params }]);
  return { ok: true, note_id: input.note_id, saved_at: now };
}
async function noteExport() {
  await boot();
  if (!dbReady) throw new Error(dbDisabledReason || '持久库未就绪');
  const rows = await dbSelect(`SELECT * FROM notes ORDER BY created_at ASC`, []);
  const notes = rows.map(r => ({ ...r, topics: parseJsonSafe(r.topics_json, []), symbols: parseJsonSafe(r.symbols_json, []), context: parseJsonSafe(r.context_json, null) }));
  const md = C().notesToMarkdown(notes, C().nowISO());
  const path = `exports/diary-${new Date().toISOString().slice(0, 10)}.md`;
  const w = await lib({ op: 'write', path, content: md });
  if (!w || w.ok === false) throw new Error('导出写入 Library 失败：' + ((w && (w.message || w.errorCode)) || '未知'));
  return { ok: true, path, bytes: md.length, note: '已导出到作品库（Library）exports/ 目录；可在插件详情的 Library 中查看。' };
}

/* ---------------- 消息状态 ---------------- */
async function messageMark(input) {
  await boot();
  if (!dbReady) throw new Error(dbDisabledReason || '持久库未就绪');
  if (!input || typeof input.logical_id !== 'string') return { ok: false, errorCode: 'INVALID', message: '缺少 logical_id。' };
  const now = C().nowISO();
  const existing = await dbSelect('SELECT logical_id FROM message_status WHERE logical_id = ?', [input.logical_id]);
  const action = input.action || 'read';
  if (!existing.length) {
    await dbBatch([{ sql: 'INSERT INTO message_status (logical_id, read_at, handled_at, handle_action, snooze_until) VALUES (?,?,?,?,?)',
      params: [input.logical_id, action === 'unread' ? null : now, ['handle', 'snooze', 'dismiss'].includes(action) ? now : null, ['handle', 'snooze', 'dismiss'].includes(action) ? action : null, action === 'snooze' && C().isDate(input.snooze_until) ? input.snooze_until : null] }]);
  } else {
    const sets = [];
    const params = [];
    if (action === 'read') { sets.push('read_at = ?'); params.push(now); }
    if (action === 'unread') { sets.push('read_at = NULL'); }
    if (['handle', 'dismiss'].includes(action)) { sets.push('handled_at = ?', 'handle_action = ?'); params.push(now, action); }
    if (action === 'snooze' && C().isDate(input.snooze_until)) { sets.push('snooze_until = ?', 'handle_action = ?'); params.push(input.snooze_until, 'snooze'); }
    if (sets.length) { params.push(input.logical_id); await dbBatch([{ sql: `UPDATE message_status SET ${sets.join(', ')} WHERE logical_id = ?`, params }]); }
  }
  return { ok: true, logical_id: input.logical_id, action };
}

/* ---------------- 运行与任务 ---------------- */
async function recordRun(run) {
  await boot();
  if (!dbReady || !run || !run.id) return { ok: false };
  await dbBatch([{ sql: `INSERT OR REPLACE INTO runs (id, task_key, batch_id, started_at, finished_at, status, coverage_json, errors_json, summary) VALUES (?,?,?,?,?,?,?,?,?)`,
    params: [String(run.id).slice(0, 128), C().clampText(run.task_key, 64), run.batch_id || null, run.started_at || C().nowISO(), run.finished_at || C().nowISO(), run.status || 'success', JSON.stringify(run.coverage || null), JSON.stringify(run.errors || []), C().clampText(run.summary, 1000)] }]);
  return { ok: true, id: run.id };
}
async function runsList(limit) {
  await boot();
  if (!dbReady) return [];
  return dbSelect('SELECT * FROM runs ORDER BY started_at DESC LIMIT ?', [Math.min(limit || 40, 200)]);
}
async function syncAutomation(input) {
  await boot();
  if (!dbReady) throw new Error(dbDisabledReason || '持久库未就绪');
  const tasks = Array.isArray(input?.tasks) ? input.tasks.slice(0, 40) : [];
  const now = C().nowISO();
  const statements = [];
  const known = new Set();
  for (const t of tasks) {
    if (!t || typeof t.task_key !== 'string' || !t.task_key) continue;
    known.add(t.task_key);
    statements.push({ sql: `INSERT INTO tasks (task_key, group_id, name, schedule_id, cron_expr, timezone, execution, status, device, last_run_json, verified_at, source) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
      ON CONFLICT(task_key) DO UPDATE SET group_id=excluded.group_id, name=excluded.name, schedule_id=excluded.schedule_id, cron_expr=excluded.cron_expr, timezone=excluded.timezone, execution=excluded.execution, status=excluded.status, device=excluded.device, last_run_json=excluded.last_run_json, verified_at=excluded.verified_at, source=excluded.source`,
      params: [t.task_key.slice(0, 64), C().clampText(t.group_id, 8), C().clampText(t.name, 120), C().clampText(t.schedule_id, 64), C().clampText(t.cron, 40) || null, C().clampText(t.timezone, 40) || null, C().clampText(t.execution, 16) || 'agent', C().clampText(t.status, 16) || 'unknown', C().clampText(t.device, 64), JSON.stringify(t.last_run || null), now, C().clampText(t.source, 40) || 'host-verified'] });
  }
  if (statements.length) await dbBatch(statements);
  return { ok: true, synced: statements.length, verified_at: now, note: '任务状态来自宿主调度读回；不是插件缓存冒充的宿主真相。' };
}
async function tasksList() {
  await boot();
  if (!dbReady) return [];
  return dbSelect('SELECT * FROM tasks ORDER BY group_id, task_key', []);
}

/* ---------------- 行情采集管线 ---------------- */
async function loadSnapshotCache() {
  if (!snapshot) try { const kv = await (await fetch('/kv')).json(); if (kv?.snapshot?.quotes) snapshot = kv.snapshot; } catch (_) {}
  if (snapshot) {
    /* 读取时按 5 个日历日重新判定陈旧，避免把旧缓存看成当前盘面 */
    snapshot = { ...snapshot, quotes: snapshot.quotes.map(q => ({ ...q, status: q.status === 'available' && (!Number.isFinite(Date.parse(q.observedAt)) || Date.now() - Date.parse(q.observedAt) > 5 * 86400000) ? 'stale' : q.status })) };
  }
  return snapshot || { fetchedAt: null, quotes: [], indices: [], macro: [], errors: [], note: '尚未获取行情。' };
}
async function fetchText(url, timeoutMs, callId) {
  const response = await cindy.fetch({ url, method: 'GET', as: 'text', timeoutMs, ...(callId ? { callId } : {}) });
  if (!response.ok || response.status !== 200 || response.truncated) throw new Error(response.message || 'HTTP ' + response.status);
  return response.body;
}
async function refresh(callId) {
  if (inFlight) return inFlight;
  inFlight = (async () => {
    await boot();
    await ready;
    const previous = await loadSnapshotCache();
    const quotes = [], indices = [], macro = [], errors = [];
    const startedAt = C().nowISO();
    const runId = 'run-' + Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
    /* 0) 节点诊断探针：区分「worker 起不来」与「某方法慢」 */
    try {
      const ping = await cindy.node.request({ method: 'ping', params: {}, timeoutMs: 12000 });
      nodeDiag.ping = ping.ok ? ('ok ' + (ping.result?.node || '')) : ('fail ' + (ping.message || ''));
    } catch (e) { nodeDiag.ping = 'error ' + (e.message || e); }
    /* 1) Alpaca 节点（本机既有只读连接） */
    try {
      const local = await cindy.node.request({ method: 'market.refresh', params: {}, timeoutMs: 60000, ...(callId ? { callId } : {}) });
      if (!local.ok || !local.result?.quotes) throw new Error(local.message || '本机行情连接未返回数据');
      quotes.push(...local.result.quotes);
    } catch (e) { errors.push({ source: 'Alpaca SIP', error: '本机已有行情连接暂不可用；缺项尝试公开行情。' + (e.message || '') }); }
    /* 2) Yahoo 兜底（并发 3） */
    const pending = M().instruments.filter(item => item.kind !== 'volatility' && !quotes.some(q => q.symbol === item.symbol));
    let cursor = 0;
    await Promise.all(Array.from({ length: 3 }, async () => {
      while (cursor < pending.length) {
        const item = pending[cursor++];
        try {
          const body = await fetchText('https://query1.finance.yahoo.com/v8/finance/chart/' + encodeURIComponent(item.symbol) + '?interval=1d&range=6mo', 8000, callId);
          quotes.push(M().parseChart(JSON.parse(body), item));
        } catch (e) {
          const error = String(e.message || e).slice(0, 200), old = previous.quotes?.find(q => q.symbol === item.symbol);
          quotes.push(old ? { ...old, status: 'stale', error } : { ...item, status: 'missing', close: null, asOf: null, series: [], error });
          errors.push({ symbol: item.symbol, error });
        }
      }
    }));
    /* 3) CBOE 指数 + FRED 宏观：节点进程经本机代理取（沙箱直连常被重置/超时，且有并发上限） */
    try {
      const idx = await cindy.node.request({ method: 'market.indices', params: {}, timeoutMs: 110000, ...(callId ? { callId } : {}) });
      if (!idx.ok || !idx.result) throw new Error(idx.message || '指数/宏观源未返回');
      indices.push(...(idx.result.indices || []));
      macro.push(...(idx.result.macro || []));
      for (const e of (idx.result.errors || [])) errors.push(e);
    } catch (e) { errors.push({ source: 'CBOE/FRED 节点', error: String(e.message || e).slice(0, 160) + '；节点诊断 ping=' + nodeDiag.ping + '，status=' + (nodeDiag.lastStatus || '未知') }) }
    /* 3b) 波动率指数 Yahoo 兜底：CBOE 在本机网络被重置时，^VIX/^VIX3M/^VVIX 走已验证可用的 Yahoo */
    const haveIndex = new Set(indices.map(i => i.key));
    for (const item of M().instruments.filter(i => i.kind === 'volatility' && !haveIndex.has(i.symbol.replace('^', '')))) {
      try {
        const body = await fetchText('https://query1.finance.yahoo.com/v8/finance/chart/' + encodeURIComponent(item.symbol) + '?interval=1d&range=2y', 9000, callId);
        const q = M().parseChart(JSON.parse(body), item);
        indices.push({ key: item.symbol.replace('^', ''), label: item.label, unit: '点', provider: 'Yahoo（CBOE 直连不可用时的兜底）', rows: q.series.map(p => ({ date: p.date, close: p.value })), bad: 0 });
      } catch (e) { errors.push({ source: 'VIX 兜底 ' + item.symbol, error: String(e.message || e).slice(0, 160) }); }
    }
    quotes.sort((a, b) => M().instruments.findIndex(x => x.symbol === a.symbol) - M().instruments.findIndex(x => x.symbol === b.symbol));
    snapshot = { fetchedAt: C().nowISO(), quotes, indices, macro, errors,
      note: 'Alpaca SIP 优先、缺项 Yahoo 兜底；CBOE 官方 CSV 提供 VIX/VIX3M/VVIX；FRED 提供利率/利差/美元（经本机代理）。未接通的槽位如实保留缺口。' };
    try {
      /* KV 只存轻量元数据：图表序列一律走 Library 持久库（series 通道），避免 64KB 上限 */
      const cached = { ...snapshot, quotes: snapshot.quotes.map(({ series, ...q }) => q), indices: snapshot.indices.map(({ rows, ...i }) => ({ ...i, latest: rows.at(-1) || null, points: rows.length })), macro: snapshot.macro.map(({ rows, ...m }) => ({ ...m, latest: rows.at(-1) || null, points: rows.length })) };
      const body = JSON.stringify({ snapshot: cached });
      if (new TextEncoder().encode(body).length > 64000) throw new Error('快照超过 KV 存储上限');
      const r = await fetch('/kv', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body });
      if (!r.ok) throw new Error('HTTP ' + r.status);
    } catch (e) { snapshot.storageWarning = '快照缓存保存失败；本次显示有效，重开后需重新刷新：' + e.message; }
    /* 5) 观测入库 + 运行记录（真实持久回执） */
    let ingestReceipt = null;
    if (dbReady) {
      const series = [];
      for (const q of quotes) {
        if (!Array.isArray(q.series) || q.series.length < 2) continue;
        series.push({ key: q.symbol.replace('^', ''), label: q.label, provider: q.provider || 'Yahoo', unit: q.currency || null, basis: q.basis, source_url: q.sourceUrl, status: q.status === 'available' ? 'ok' : 'stale', observations: q.series.map(p => ({ date: p.date, value: p.value })) });
      }
      for (const idx of indices) series.push({ key: idx.key, label: idx.label, provider: idx.provider || 'CBOE 官方 CSV', unit: idx.unit, basis: idx.provider ? 'Yahoo 日收盘兜底；CBOE 不可用时替代，口径在卡上标明' : 'CBOE 日收盘；VVIX 为单列 CSV 单独解析', source_url: idx.url || 'https://finance.yahoo.com/quote/%5E' + idx.key + '/', status: 'ok', observations: M().toObservations(idx.rows, 'close', 1100) });
      for (const m of macro) series.push({ key: m.key, label: m.label, provider: 'FRED', unit: m.unit, basis: 'FRED 日频序列；缺失值跳过不插值', source_url: m.url, status: 'ok', observations: M().toObservations(m.rows, 'value', 1100) });
      const usable = quotes.filter(q => q.status !== 'missing');
      try {
        ingestReceipt = await ingestBatch({ batch_id: 'market-' + new Date().toISOString().slice(0, 10), kind: 'market', data_cutoff: snapshot.fetchedAt,
          coverage: { denominator: M().instruments.length, succeeded: usable.length + indices.length + macro.length, missing: quotes.filter(q => q.status === 'missing').map(q => q.symbol), errors: errors.slice(0, 20) },
          series });
      } catch (e) { errors.push({ source: 'desk.sqlite', error: String(e.message || e).slice(0, 200) }); }
      await recordRun({ id: runId, task_key: 'market-refresh', started_at: startedAt, finished_at: C().nowISO(), status: 'success', coverage: { denominator: M().instruments.length, succeeded: usable.length }, errors: errors.slice(0, 20), summary: `行情刷新：可用 ${usable.length}/${M().instruments.length}，指数 ${indices.length}/3，宏观 ${macro.length}/4，错误 ${errors.length}` });
    }
    return snapshot;
  })().finally(() => { inFlight = null; });
  return inFlight;
}

/* ---------------- 工具面 ---------------- */
async function handleTool(msg) {
  const args = msg.args || {};
  if (msg.tool === 'get_snapshot') {
    const data = await loadSnapshotCache();
    return { ...data, quotes: data.quotes.map(({ series, ...q }) => ({ ...q, observations: series?.length || 0 })), db_ready: dbReady };
  }
  if (msg.tool === 'refresh_market') {
    const data = await refresh(msg.callId);
    return { fetchedAt: data.fetchedAt, errors: data.errors, storageWarning: data.storageWarning || null, quotes: data.quotes.map(({ series, ...q }) => ({ ...q, observations: series?.length || 0 })), indices: data.indices.map(i => ({ key: i.key, latest: i.rows.at(-1), points: i.rows.length })), macro: data.macro.map(i => ({ key: i.key, latest: i.rows.at(-1), points: i.rows.length })), db_ready: dbReady, ingest: null };
  }
  if (msg.tool === 'get_desk_context') return await getDeskContext();
  if (msg.tool === 'ingest_batch') { const r = await ingestBatch(args.batch || args); if (r && r.ok === false) throw Object.assign(new Error(r.message), { errorCode: r.errorCode }); return r; }
  if (msg.tool === 'list_updates') return { messages: await listUpdates(args), query: args };
  if (msg.tool === 'submit_note_draft') return await noteDraft(args);
  if (msg.tool === 'sync_automation_status') return await syncAutomation(args);
  throw new Error('未知工具：' + msg.tool);
}
cindy.onHostMessage(async msg => {
  if (msg.type === 'event' && msg.name === 'node-status') { nodeDiag.lastStatus = (msg.state || '') + (msg.entry ? '@' + msg.entry : ''); nodeDiag.lastStatusAt = new Date().toISOString(); return; }
  if (msg.type !== 'tool-call') return;
  try { await boot(); const result = await handleTool(msg); await cindy.send({ type: 'tool-result', callId: msg.callId, ok: true, result }); }
  catch (e) { await cindy.send({ type: 'tool-result', callId: msg.callId, ok: false, errorCode: e.errorCode, message: '操作未完成：' + (e.message || e) + '。可重试；已入库内容不受影响。' }); }
});

/* ---------------- 页面通道（BroadcastChannel v2） ---------------- */
const PAGE_ACTIONS = ['snapshot', 'refresh', 'context', 'series', 'messages', 'message.mark', 'notes.list', 'notes.save', 'notes.update', 'notes.draft.accept', 'notes.export', 'tasks.list', 'runs.list'];
channel.onmessage = async ({ data: m }) => {
  if (m?.type !== 'desk-request' || typeof m.id !== 'string' || !PAGE_ACTIONS.includes(m.action)) return;
  if (replies.has(m.id)) { const cached = replies.get(m.id); if (cached) channel.postMessage(cached); return; }
  replies.set(m.id, null);
  let answer;
  try {
    await boot();
    let result;
    switch (m.action) {
      case 'snapshot': result = await loadSnapshotCache(); break;
      case 'refresh': result = await refresh(null); break;
      case 'context': result = await getDeskContext(); break;
      case 'series': result = await getSeriesMap(Array.isArray(m.keys) ? m.keys.slice(0, 12) : [], 800); break;
      case 'messages': result = { messages: await listUpdates(m.query || {}) }; break;
      case 'message.mark': result = await messageMark(m.input); break;
      case 'notes.list': result = { notes: await noteList(m.query || {}) }; break;
      case 'notes.save': result = await noteSave(m.input || {}); break;
      case 'notes.update': result = await noteUpdate(m.input || {}); break;
      case 'notes.draft.accept': result = await noteAcceptDraft(m.note_id); break;
      case 'notes.export': result = await noteExport(); break;
      case 'tasks.list': result = { tasks: await tasksList() }; break;
      case 'runs.list': result = { runs: await runsList(m.limit) }; break;
    }
    answer = { type: 'desk-response', id: m.id, ok: true, result };
  } catch (e) { answer = { type: 'desk-response', id: m.id, ok: false, error: '操作失败：' + (e.message || e) }; }
  replies.set(m.id, answer);
  if (replies.size > 200) replies.delete(replies.keys().next().value);
  channel.postMessage(answer);
};
boot();
