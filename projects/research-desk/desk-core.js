/* desk-core.js — Murphy Research Desk 共享核心（浏览器 + Node 双端）
 * 纯逻辑，不做 IO：槽位与池定义、库迁移 SQL、批次契约校验、
 * 幂等/版本化决策、日记冲突判定、视图分流、覆盖率计算。
 * 被 main.js（沙箱）与 tests/*.test.cjs（Node）共同加载。
 */
(function (root) {
  'use strict';

  /* ---------- 常量：固定观察槽位（顺序固定，不随涨跌重排） ---------- */
  const SLOTS = [
    { id: 'market', title: '大盘趋势', theme: 'market', series: ['SPY'], expand: 'JNK–SPY 经验规则可在主题页展开；QQQ/IWM 为辅助代理。' },
    { id: 'vix', title: 'VIX', theme: 'market', series: ['VIX'] },
    { id: 'vvix', title: 'VVIX', theme: 'market', series: ['VVIX'] },
    { id: 'vix3m', title: 'VIX3M 与期限', theme: 'market', series: ['VIX3M'], derived: 'vix_ratio', derivedNote: 'VIX/VIX3M 比值按同时点收盘相除，缺任一项则不显示。' },
    { id: 'credit', title: '高收益信用利差', theme: 'market', series: ['BAMLH0A0HYM2'], gapNote: '首选 FRED ICE BofA 美国高收益利差；JNK/HYG 是价格代理，不冒充利差。' },
    { id: 'rates', title: '美债 10 年利率', theme: 'market', series: ['DGS10', 'DFII10'], labels: { DGS10: '名义', DFII10: '实际' } },
    { id: 'dollar', title: '广义美元指数', theme: 'market', series: ['DTWEXBGS'], gapNote: 'FRED 广义贸易加权美元指数；不是 DXY。' },
    { id: 'metals', title: '黄金 · 白银', theme: 'metals', series: ['GLD', 'SLV'], expand: '铜（CPER）在金银主题页辅助区。' },
    { id: 'gsr', title: '金银比', theme: 'metals', series: ['GLD', 'SLV'], derived: 'gsr', derivedNote: 'ETF 价格比（GLD/SLV），口径显式标注；不是现货金银比。' },
    { id: 'semi-ai', title: '半导体 AI 主导情绪', theme: 'semis', series: ['SEMIS_AI'], sourceCard: { provider: 'semiconductor.feargreedchart.com', url: 'https://semiconductor.feargreedchart.com/', note: '外部模型观点，非官方统计。数值未接入时显示来源卡与最后人工导入日期。' } },
    { id: 'semi-broad', title: '半导体广泛情绪', theme: 'semis', series: ['SEMIS_BROAD'], sourceCard: { provider: 'semiconductor.feargreedchart.com', url: 'https://semiconductor.feargreedchart.com/', note: '同上，广泛口径。' } },
    { id: 'semi-cycle', title: '半导体周期情绪', theme: 'semis', series: ['SEMIS_CYCLE'], sourceCard: { provider: 'semiconductor.feargreedchart.com', url: 'https://semiconductor.feargreedchart.com/', note: '同上，周期口径。' } }
  ];

  /* ---------- 常量：研究池（不是持仓） ---------- */
  const POOL = {
    version: '2026-11-16',
    symbols: ['TER', 'AVGO', 'UNH', 'SILJ', 'APP', 'BWXT', 'VST', 'LMT', 'LNN', 'LIN', 'TRP', 'WDC', 'CRWV', 'MOS', 'GEV', 'RCL', 'SLV', 'XAR', 'NLR', 'TSLA'],
    auxiliary: ['TSLL', 'SPY', 'QQQ', 'SOXX', 'JNK', 'HYG', 'IEF'],
    note: '研究池 ≠ 持仓。辅助观察保留角色，不扩写成持仓。'
  };

  /* ---------- 常量：消息视图与种类 ---------- */
  const VIEWS = ['needs', 'updates', 'opinions', 'health'];
  const MESSAGE_KINDS = ['event', 'fact', 'opinion', 'report', 'health', 'verify'];
  const CATEGORIES = ['fact', 'external_opinion', 'ai_explainer'];
  const BATCH_KINDS = ['market', 'metals', 'semis', 'pool', 'sentinel', 'calendar', 'earnings', 'aicapex', 'power', 'twitter', 'expiry', 'diary-clock', 'material-gap', 'health', 'report', 'manual'];

  /* ---------- 库迁移（宿主按 user_version 幂等续跑） ---------- */
  const MIGRATIONS = [
    {
      toVersion: 1,
      sql: [
        'CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL)',
        'CREATE TABLE IF NOT EXISTS batches (batch_id TEXT PRIMARY KEY, job_id TEXT, run_id TEXT, kind TEXT, window_start TEXT, window_end TEXT, data_cutoff TEXT, sources_json TEXT, coverage_json TEXT, errors_json TEXT, received_at TEXT NOT NULL, item_count INTEGER NOT NULL DEFAULT 0, written INTEGER NOT NULL DEFAULT 0, duplicates INTEGER NOT NULL DEFAULT 0, rejected_json TEXT)',
        'CREATE TABLE IF NOT EXISTS sources (root_id TEXT PRIMARY KEY, title TEXT, url TEXT, provider TEXT, kind TEXT, first_seen TEXT, last_seen TEXT)',
        'CREATE TABLE IF NOT EXISTS series (key TEXT PRIMARY KEY, label TEXT, provider TEXT, unit TEXT, basis TEXT, source_url TEXT, latest_date TEXT, latest_value REAL, updated_at TEXT, status TEXT)',
        'CREATE TABLE IF NOT EXISTS observations (series_key TEXT NOT NULL, date TEXT NOT NULL, value REAL NOT NULL, PRIMARY KEY (series_key, date))',
        'CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, logical_id TEXT NOT NULL, version INTEGER NOT NULL, content_hash TEXT NOT NULL, batch_id TEXT, root_source_id TEXT, kind TEXT, category TEXT, title TEXT NOT NULL, body TEXT, url TEXT, author TEXT, stance TEXT, event_time TEXT, published_at TEXT, topics_json TEXT, symbols_json TEXT, importance INTEGER NOT NULL DEFAULT 2, actionable INTEGER NOT NULL DEFAULT 0, coverage_note TEXT, created_at TEXT NOT NULL, UNIQUE (logical_id, version))',
        'CREATE TABLE IF NOT EXISTS message_status (logical_id TEXT PRIMARY KEY, read_at TEXT, handled_at TEXT, handle_action TEXT, snooze_until TEXT)',
        'CREATE TABLE IF NOT EXISTS notes (id TEXT PRIMARY KEY, created_at TEXT NOT NULL, updated_at TEXT NOT NULL, revision INTEGER NOT NULL DEFAULT 1, text_original TEXT NOT NULL, topics_json TEXT, symbols_json TEXT, context_json TEXT, verify_date TEXT, verify_question TEXT, status TEXT NOT NULL DEFAULT \'active\', outcome TEXT)',
        'CREATE TABLE IF NOT EXISTS note_versions (id INTEGER PRIMARY KEY AUTOINCREMENT, note_id TEXT NOT NULL, version INTEGER NOT NULL, origin TEXT NOT NULL, text TEXT NOT NULL, context_json TEXT, created_at TEXT NOT NULL, UNIQUE (note_id, version, origin))',
        'CREATE TABLE IF NOT EXISTS runs (id TEXT PRIMARY KEY, task_key TEXT, batch_id TEXT, started_at TEXT, finished_at TEXT, status TEXT, coverage_json TEXT, errors_json TEXT, summary TEXT)',
        'CREATE TABLE IF NOT EXISTS tasks (task_key TEXT PRIMARY KEY, group_id TEXT, name TEXT, schedule_id TEXT, cron_expr TEXT, timezone TEXT, execution TEXT, status TEXT, device TEXT, last_run_json TEXT, verified_at TEXT, source TEXT)'
      ]
    },
    {
      toVersion: 2,
      sql: [
        'CREATE INDEX IF NOT EXISTS idx_messages_created ON messages (created_at DESC)',
        'CREATE INDEX IF NOT EXISTS idx_messages_kind ON messages (kind)',
        'CREATE INDEX IF NOT EXISTS idx_observations_key_date ON observations (series_key, date)',
        'CREATE INDEX IF NOT EXISTS idx_notes_updated ON notes (updated_at DESC)',
        'CREATE INDEX IF NOT EXISTS idx_runs_started ON runs (started_at DESC)'
      ]
    }
  ];
  const DB_VERSION = MIGRATIONS[MIGRATIONS.length - 1].toVersion;

  /* ---------- 小工具 ---------- */
  const nowISO = () => new Date().toISOString();
  const isISO = v => typeof v === 'string' && /^\d{4}-\d{2}-\d{2}(T[\d:.]+(Z|[+-]\d{2}:?\d{2})?)?$/.test(v);
  /* 日历真校验：正则过 + Date 解析回同一日期（拒绝 2026-13-99 这类格式正确但不存在的日期） */
  const isDate = v => {
    if (typeof v !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(v)) return false;
    const d = new Date(v + 'T00:00:00Z');
    return Number.isFinite(d.getTime()) && d.toISOString().slice(0, 10) === v;
  };
  const isFiniteNumber = v => typeof v === 'number' && Number.isFinite(v);
  const clampText = (v, max) => typeof v === 'string' && v.trim() ? v.trim().slice(0, max) : null;

  /* 稳定哈希（djb2，32 位十六进制）。用于内容版本判定，不用于安全。 */
  function hashString(input) {
    let h = 5381;
    const s = String(input);
    for (let i = 0; i < s.length; i++) h = ((h << 5) + h + s.charCodeAt(i)) | 0;
    return (h >>> 0).toString(16).padStart(8, '0');
  }

  /* 条目内容哈希：与 batch_id / 入库时间无关的稳定指纹 */
  function itemContentHash(item) {
    const stable = {
      logical_id: item.logical_id, root_source_id: item.root_source_id || '', kind: item.kind,
      category: item.category, title: item.title, body: item.body || '', url: item.url || '',
      author: item.author || '', stance: item.stance || '', event_time: item.event_time || '',
      published_at: item.published_at || '', topics: (item.topics || []).slice().sort(),
      symbols: (item.symbols || []).slice().sort(), importance: item.importance,
      actionable: item.actionable ? 1 : 0, coverage_note: item.coverage_note || ''
    };
    return hashString(JSON.stringify(stable));
  }

  /* ---------- 批次契约校验（§6.2 最小契约） ---------- */
  const MAX_ITEMS = 500;
  function validateBatch(batch) {
    const errors = [];
    if (!batch || typeof batch !== 'object') return { ok: false, errors: ['批次必须是对象'] };
    const batch_id = typeof batch.batch_id === 'string' ? batch.batch_id.trim() : '';
    if (!/^[A-Za-z0-9._:-]{4,128}$/.test(batch_id)) errors.push('batch_id 必须是 4–128 位稳定标识');
    if (!BATCH_KINDS.includes(batch.kind)) errors.push('kind 不在支持的批次类型内');
    if (batch.window && ((batch.window.start && !isISO(batch.window.start)) || (batch.window.end && !isISO(batch.window.end)))) errors.push('window.start/end 必须是 ISO 日期时间');
    if (batch.data_cutoff && !isISO(batch.data_cutoff)) errors.push('data_cutoff 必须是 ISO 日期时间');
    if (batch.items && !Array.isArray(batch.items)) errors.push('items 必须是数组');
    if (Array.isArray(batch.items) && batch.items.length > MAX_ITEMS) errors.push(`单批 items 超过 ${MAX_ITEMS} 条上限`);
    return { ok: errors.length === 0, errors };
  }

  function validateItem(item, index) {
    const rejects = [];
    if (!item || typeof item !== 'object') return { ok: false, rejects: [`items[${index}] 不是对象`] };
    if (typeof item.logical_id !== 'string' || !/^[A-Za-z0-9._:-]{3,160}$/.test(item.logical_id)) rejects.push(`items[${index}].logical_id 必须是 3–160 位稳定标识`);
    if (!MESSAGE_KINDS.includes(item.kind)) rejects.push(`items[${index}].kind 非法`);
    if (!CATEGORIES.includes(item.category)) rejects.push(`items[${index}].category 非法`);
    if (!clampText(item.title, 300)) rejects.push(`items[${index}].title 缺失`);
    if (item.event_time && !isISO(item.event_time)) rejects.push(`items[${index}].event_time 非法`);
    if (item.published_at && !isISO(item.published_at)) rejects.push(`items[${index}].published_at 非法`);
    if (item.url && !/^https:\/\//.test(item.url)) rejects.push(`items[${index}].url 必须是 https`);
    if (item.topics && !Array.isArray(item.topics)) rejects.push(`items[${index}].topics 必须是数组`);
    if (item.symbols && (!Array.isArray(item.symbols) || item.symbols.some(s => typeof s !== 'string' || !/^[A-Z0-9.^-]{1,12}$/.test(s)))) rejects.push(`items[${index}].symbols 含非法代码`);
    if (item.importance != null && ![1, 2, 3].includes(item.importance)) rejects.push(`items[${index}].importance 只能是 1–3`);
    if (item.stance && !['bull', 'bear', 'mixed', 'unknown'].includes(item.stance)) rejects.push(`items[${index}].stance 非法`);
    return { ok: rejects.length === 0, rejects };
  }

  function normalizeItem(item, batch) {
    return {
      logical_id: item.logical_id, root_source_id: clampText(item.root_source_id, 160) || batch.batch_id,
      kind: item.kind, category: item.category, title: clampText(item.title, 300),
      body: clampText(item.body, 8000), url: item.url || null, author: clampText(item.author, 120),
      stance: item.stance || null, event_time: item.event_time || null, published_at: item.published_at || null,
      topics: (item.topics || []).filter(t => typeof t === 'string').slice(0, 8),
      symbols: (item.symbols || []).slice(0, 12), importance: item.importance || 2,
      actionable: item.actionable ? 1 : 0, coverage_note: clampText(item.coverage_note, 500),
      content_hash: itemContentHash(item)
    };
  }

  /* 序列观测校验 */
  function validateSeries(s, index) {
    const rejects = [];
    if (!s || typeof s !== 'object') return { ok: false, rejects: [`series[${index}] 不是对象`] };
    if (!/^[A-Z0-9._^-]{1,24}$/.test(s.key || '')) rejects.push(`series[${index}].key 非法`);
    if (!Array.isArray(s.observations)) rejects.push(`series[${index}].observations 必须是数组`);
    else {
      if (s.observations.length > 1200) rejects.push(`series[${index}].observations 超过 1200 点上限`);
      for (let i = 0; i < s.observations.length; i++) {
        const o = s.observations[i];
        if (!o || !isDate(o.date) || !isFiniteNumber(o.value)) { rejects.push(`series[${index}].observations[${i}] 需要 YYYY-MM-DD 日期与有限数值`); break; }
      }
    }
    return { ok: rejects.length === 0, rejects };
  }

  /* ---------- 槽位状态计算（纯函数：由序列快照推导） ---------- */
  function slotStatus(slot, seriesMap) {
    const out = { id: slot.id, title: slot.title, theme: slot.theme, series: slot.series || [], status: 'missing', parts: [], note: slot.gapNote || null, expand: slot.expand || null };
    if (slot.sourceCard) { out.sourceCard = slot.sourceCard; }
    if (Array.isArray(slot.series) && slot.series.length) {
      const parts = slot.series.map(key => {
        const s = seriesMap[key] || null;
        if (!s || !s.observations || s.observations.length === 0) return { key, status: 'missing', label: (slot.labels && slot.labels[key]) || key };
        const last = s.observations[s.observations.length - 1], prev = s.observations[s.observations.length - 2] || null;
        const change = prev && prev.value !== 0 ? (last.value / prev.value - 1) * 100 : null;
        return { key, label: (slot.labels && slot.labels[key]) || key, status: s.status === 'stale' ? 'stale' : 'ok', date: last.date, value: last.value, change1d: change, provider: s.provider || null, basis: s.basis || null, unit: s.unit || null, points: s.observations.length };
      });
      out.parts = parts;
      const ok = parts.filter(p => p.status === 'ok').length;
      out.status = ok === parts.length ? 'ok' : ok > 0 ? 'partial' : parts.some(p => p.status === 'stale') ? 'stale' : 'missing';
      if (slot.derived === 'vix_ratio') {
        const vix = seriesMap.VIX, v3 = seriesMap.VIX3M;
        if (vix && v3 && vix.observations.length && v3.observations.length) {
          const d = vix.observations[vix.observations.length - 1].date === v3.observations[v3.observations.length - 1].date ? vix.observations[vix.observations.length - 1].date : null;
          const r = d ? vix.observations[vix.observations.length - 1].value / v3.observations[v3.observations.length - 1].value : null;
          out.derived = r != null && isFiniteNumber(r) ? { label: 'VIX/VIX3M', date: d, value: Math.round(r * 1000) / 1000 } : null;
        }
      }
      if (slot.derived === 'gsr') {
        const g = seriesMap.GLD, s2 = seriesMap.SLV;
        if (g && s2 && g.observations.length && s2.observations.length) {
          const d = g.observations[g.observations.length - 1].date === s2.observations[s2.observations.length - 1].date ? g.observations[g.observations.length - 1].date : null;
          const r = d ? g.observations[g.observations.length - 1].value / s2.observations[s2.observations.length - 1].value : null;
          out.derived = r != null && isFiniteNumber(r) ? { label: '金银比（ETF 价格比）', date: d, value: Math.round(r * 1000) / 1000, note: slot.derivedNote } : null;
        }
      }
    }
    return out;
  }

  /* ---------- 日记保存计划（冲突 = 保留两版，不静默覆盖） ---------- */
  function noteSavePlan(existing, incoming) {
    if (!existing) return { action: 'insert' };
    const incomingHash = hashString(incoming.text || '');
    const currentHash = hashString(existing.text_original || '');
    if (incoming.base_revision === existing.revision) {
      if (incomingHash === currentHash) return { action: 'noop' };
      return { action: 'update', from_revision: existing.revision, to_revision: existing.revision + 1 };
    }
    if (incoming.base_revision == null || incoming.base_revision < existing.revision) {
      if (incomingHash === currentHash) return { action: 'noop' };
      return { action: 'conflict', server_revision: existing.revision, base_revision: incoming.base_revision == null ? -1 : incoming.base_revision };
    }
    return { action: 'update', from_revision: existing.revision, to_revision: existing.revision + 1, out_of_order: true };
  }

  /* ---------- 日记导出 Markdown ---------- */
  function notesToMarkdown(notes, generatedAt) {
    const lines = [`# 投资日记导出`, ``, `- 导出时间：${generatedAt}`, `- 条数：${notes.length}`, `- 说明：原文与 AI 草稿分开；本导出仅含用户原文与验证信息。`, ``];
    for (const n of notes) {
      lines.push(`---`, ``, `## ${n.created_at.slice(0, 10)} · ${n.id}`, ``);
      if (n.topics && n.topics.length) lines.push(`主题：${n.topics.join('、')}`);
      if (n.symbols && n.symbols.length) lines.push(`标的：${n.symbols.join(' ')}`);
      if (n.verify_date) lines.push(`下一验证：${n.verify_date}${n.verify_question ? ' — ' + n.verify_question : ''}`);
      if (n.outcome) lines.push(`结果：${n.outcome}`);
      if (n.context && n.context.sources && n.context.sources.length) {
        lines.push(``, `记录时上下文：`);
        for (const s of n.context.sources.slice(0, 8)) lines.push(`- ${s.title || s.url || ''}${s.url ? '（' + s.url + '）' : ''}`);
      }
      lines.push(``, (n.text_original || '').trim(), ``);
    }
    return lines.join('\n');
  }

  /* ---------- 覆盖率计算 ---------- */
  function coverageSummary(coverage) {
    if (!coverage || typeof coverage !== 'object') return { denominator: 0, succeeded: 0, pct: null, missing: [], errors: [] };
    const denominator = isFiniteNumber(coverage.denominator) ? coverage.denominator : 0;
    const succeeded = isFiniteNumber(coverage.succeeded) ? coverage.succeeded : 0;
    const pct = denominator > 0 ? Math.round(succeeded / denominator * 1000) / 10 : null;
    return { denominator, succeeded, pct, missing: coverage.missing || [], errors: coverage.errors || [] };
  }

  /* SQL 字符串字面量安全转义（db.exec 支持参数，读取尽量用参数；
   * 此函数只用于无法参数化的少数场景，值域受上游格式校验约束）。 */
  function sqlText(value) {
    return '\'' + String(value == null ? '' : value).replace(/'/g, '\'\'') + '\'';
  }

  const DeskCore = {
    SLOTS, POOL, VIEWS, MESSAGE_KINDS, CATEGORIES, BATCH_KINDS, MIGRATIONS, DB_VERSION,
    nowISO, isISO, isDate, isFiniteNumber, clampText, hashString, itemContentHash,
    validateBatch, validateItem, normalizeItem, validateSeries,
    slotStatus, noteSavePlan, notesToMarkdown, coverageSummary, sqlText
  };

  root.DeskCore = DeskCore;
  if (typeof module !== 'undefined' && module.exports) module.exports = DeskCore;
})(globalThis);
