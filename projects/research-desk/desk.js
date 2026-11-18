'use strict';
/* Research Desk v2 · 页面逻辑
 * 布局：左导航 / 中内容 / 右操作台。右操作台常驻，切换主题不清空正在写的日记。
 * 图表：SVG 自绘（坐标轴、网格、十字光标、区间、归一化对比、事件标记）。
 */
const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];
const esc = v => String(v ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const num = v => typeof v === 'number' && Number.isFinite(v);
const fmt = (v, dp = 2) => num(v) ? v.toLocaleString('zh-CN', { minimumFractionDigits: dp, maximumFractionDigits: dp }) : '—';
const pct = v => num(v) ? `${v > 0 ? '+' : ''}${fmt(v, 2)}%` : '—';
const fmtDate = d => typeof d === 'string' ? d.slice(0, 10) : '—';
const shortDate = d => typeof d === 'string' ? d.slice(5, 10) : '';

/* ---------------- 与电子脑通信 ---------------- */
let channel = null;
const requests = new Map();
function request(action, payload) {
  return new Promise((resolve, reject) => {
    if (!channel) { reject(new Error('数据后台未连接；稍后重试。')); return; }
    const id = crypto.randomUUID();
    const controller = new AbortController();
    let retry;
    const finish = (error, result) => { clearTimeout(timeout); clearInterval(retry); controller.abort(); requests.delete(id); error ? reject(error) : resolve(result); };
    const timeout = setTimeout(() => finish(new Error(action + ' 超时未响应；原有数据保留，可重试。')), action === 'refresh' ? 120000 : 20000);
    requests.set(id, finish);
    fetch('/wake', { signal: controller.signal }).then(r => {
      if (!r.ok) throw new Error('唤醒后台失败 HTTP ' + r.status);
      if (!requests.has(id)) return;
      const send = () => channel.postMessage({ type: 'desk-request', id, action, ...payload });
      send(); retry = setInterval(send, 900);
    }).catch(e => { if (requests.has(id)) finish(e); });
  });
}
try {
  channel = new BroadcastChannel('murphy-research-desk-v2');
  channel.onmessage = ({ data }) => {
    if (data?.type !== 'desk-response' || !requests.has(data.id)) return;
    const finish = requests.get(data.id);
    data.ok ? finish(null, data.result) : finish(new Error(data.error || '后台返回失败'));
  };
} catch (_) {}

/* ---------------- 状态 ---------------- */
const THEMES = {
  market: { title: '市场', sub: '全市场风险：趋势、波动率、信用、利率与美元' },
  metals: { title: '金银', sub: '黄金与白银：价格分化 → 实际利率、美元与库存验证' },
  semis: { title: '半导体', sub: '三个外部情绪视图与产业数据；情绪是模型观点，不是官方统计' }
};
const ROUTES = [
  { id: 'today', title: '今日' }, { id: 'market', title: '市场', theme: 'market' }, { id: 'metals', title: '金银', theme: 'metals' },
  { id: 'semis', title: '半导体', theme: 'semis' }, { id: 'pool', title: '20 标的' }, { id: 'diary', title: '日记本' },
  { id: 'reports', title: '报告' }, { id: 'automation', title: '自动化' }
];
const VIEW_META = { needs: '需我处理', updates: '重点更新', opinions: '观点流', health: '运行健康' };
const KIND_CN = { event: '事件', fact: '事实', opinion: '观点', report: '报告', health: '健康', verify: '验证' };
const CAT_CN = { fact: '官方事实', external_opinion: '外部观点', ai_explainer: 'AI 解释' };
const state = {
  route: 'today', focus: null, range: '1Y', compare: false, subtab: 'chart', view: 'updates',
  context: null, snapshot: null, catalog: null, series: {}, messages: [], messagesTotal: null,
  notes: [], noteSel: null, tasks: [], runs: [], boardPage: 0,
  chart: { hoverIdx: null, eventDate: null },
  busy: false, motionPaused: false
};
const motionQuery = matchMedia('(prefers-reduced-motion: reduce)');
try { state.motionPaused = localStorage.getItem('desk-motion') === 'paused'; } catch (_) {}
const RANGES = { '1M': 31, '3M': 93, '1Y': 366, '3Y': 1100 };

/* ---------------- 数据装载 ---------------- */
async function loadCatalog() { try { const r = await fetch('./data/catalog.json'); state.catalog = r.ok ? await r.json() : null; } catch (_) {} }
async function loadContext() { state.context = await request('context'); }
async function loadSnapshot() { state.snapshot = await request('snapshot'); }
async function loadMessages() { const r = await request('messages', { query: { view: state.view, limit: 60 } }); state.messages = r.messages; }
async function loadNotes() { const r = await request('notes.list', { query: { limit: 120 } }); state.notes = r.notes; }
async function loadTasks() { const [t, r] = await Promise.all([request('tasks.list'), request('runs.list', { limit: 40 })]); state.tasks = t.tasks; state.runs = r.runs; }
async function loadSeries(keys) {
  const missing = keys.filter(k => !state.series[k]);
  if (missing.length) Object.assign(state.series, await request('series', { keys: missing }));
}

/* ---------------- 通用小组件 ---------------- */
function chipStatus(st) { return st === 'ok' ? '<span class="chip ok"><i class="dot"></i>可用</span>' : st === 'stale' ? '<span class="chip stale"><i class="dot"></i>陈旧</span>' : st === 'partial' ? '<span class="chip partial"><i class="dot"></i>部分</span>' : '<span class="chip missing"><i class="dot"></i>未接入</span>'; }
function importanceDots(n) { n = n || 2; return `<span class="imp" title="重要性 ${n}/3">${[1, 2, 3].map(i => `<i class="${i <= n ? 'on' : ''}"></i>`).join('')}</span>`; }
function crumbsHTML(items) {
  return `<nav class="crumbs" aria-label="位置">${items.map((c, i) => i === items.length - 1
    ? `<span class="here">${esc(c.label)}</span>`
    : `<button data-nav="${esc(c.to)}">${esc(c.label)}</button><span class="sep">›</span>`).join('')}</nav>`;
}

/* ---------------- 图表 ---------------- */
const SERIES_COLORS = ['var(--accent)', 'var(--ok)', 'var(--warn)', 'var(--danger)'];
function unitOf(key) {
  if (/^(VIX|VIX3M|VVIX)/.test(key)) return { dp: 2, suffix: '' };
  if (/^(DGS10|DFII10|BAMLH0A0HYM2)/.test(key)) return { dp: 2, suffix: '%' };
  if (/^DTWEXBGS/.test(key)) return { dp: 1, suffix: '' };
  return { dp: 2, suffix: '' };
}
function fmtSeriesValue(key, v) { const u = unitOf(key); return fmt(v, u.dp) + u.suffix; }
function rangeCutoff() { return new Date(Date.now() - RANGES[state.range] * 86400000).toISOString().slice(0, 10); }
function chartDataFor(focus) {
  const keys = focus.series || [];
  return keys.map((key, i) => {
    const s = state.series[key];
    if (!s || !s.observations?.length) return { key, label: key, color: SERIES_COLORS[i % 4], points: [] };
    const cut = rangeCutoff();
    const points = s.observations.filter(p => p.date >= cut);
    return { key, label: (focus.labels && focus.labels[key]) || s.label || key, color: SERIES_COLORS[i % 4], points, unit: s.unit, provider: s.provider, basis: s.basis, source_url: s.source_url, status: s.status };
  });
}
function niceTicks(min, max, count) {
  const span = max - min || 1, step0 = span / count, mag = Math.pow(10, Math.floor(Math.log10(step0)));
  const norm = step0 / mag, step = (norm >= 5 ? 5 : norm >= 2 ? 2 : 1) * mag;
  const start = Math.ceil(min / step) * step, out = [];
  for (let v = start; v <= max + 1e-9; v += step) out.push(v);
  return out;
}
function renderChartSVG(w, h, datasets, events) {
  const ml = 56, mr = 14, mt = 16, mb = 30;
  const iw = Math.max(60, w - ml - mr), ih = Math.max(60, h - mt - mb);
  const dates = [...new Set(datasets.flatMap(d => d.points.map(p => p.date)))].sort();
  if (!dates.length) return { svg: `<div class="empty">该区间内没有观测。<br><small>数据不足时如实显示；不生成样本补全</small></div>`, dates: [] };
  const idxOf = new Map(dates.map((d, i) => [d, i]));
  const valAt = (d, p) => { const v = p.get(d); return v == null ? null : v; };
  const seriesMaps = datasets.map(d => ({ ...d, map: new Map(d.points.map(p => [p.date, p.value])) }));
  let values = [];
  if (state.compare) {
    for (const d of seriesMaps) { const first = d.points[0]?.value; if (first > 0) for (const p of d.points) values.push(p.value / first * 100); }
  } else for (const d of seriesMaps) for (const p of d.points) values.push(p.value);
  if (!values.length) return { svg: `<div class="empty">该区间内没有可绘数值。</div>`, dates };
  let vmin = Math.min(...values), vmax = Math.max(...values);
  if (vmin === vmax) { vmin -= 1; vmax += 1; }
  const pad = (vmax - vmin) * 0.06; vmin -= pad; vmax += pad;
  const X = i => ml + (dates.length > 1 ? i / (dates.length - 1) * iw : iw / 2);
  const Y = v => mt + ih - (v - vmin) / (vmax - vmin) * ih;
  const yTicks = niceTicks(vmin, vmax, 5);
  let svg = `<svg viewBox="0 0 ${w} ${h}" role="img" aria-label="趋势图，${dates.length} 个交易日" tabindex="0" data-chart>`;
  svg += `<rect x="${ml}" y="${mt}" width="${iw}" height="${ih}" fill="none" stroke="color-mix(in srgb,var(--line) 70%,transparent)"/>`;
  for (const t of yTicks) {
    const y = Y(t);
    svg += `<line class="grid-line" x1="${ml}" x2="${ml + iw}" y1="${y}" y2="${y}"/>`;
    svg += `<text class="axis-text" x="${ml - 6}" y="${y + 3}" text-anchor="end">${state.compare ? fmt(t, 0) : fmt(t, t >= 100 ? 0 : 2)}</text>`;
  }
  const xTickIdx = [];
  for (let k = 0; k <= 5; k++) { const i = Math.round(k / 5 * (dates.length - 1)); if (!xTickIdx.includes(i)) xTickIdx.push(i); }
  for (const i of xTickIdx) svg += `<text class="axis-text" x="${X(i)}" y="${h - 8}" text-anchor="middle">${shortDate(dates[i])}</text>`;
  for (const d of seriesMaps) {
    let seg = '', pen = false;
    const conv = v => state.compare && d.points[0]?.value > 0 ? v / d.points[0].value * 100 : v;
    for (const p of d.points) {
      const i = idxOf.get(p.date);
      const x = X(i), y = Y(conv(p.value));
      if (!pen) { seg += `M${x.toFixed(1)} ${y.toFixed(1)}`; pen = true; } else seg += ` L${x.toFixed(1)} ${y.toFixed(1)}`;
    }
    svg += `<path d="${seg}" fill="none" stroke="${d.color}" stroke-width="1.8" stroke-linejoin="round"/>`;
    const lastP = d.points[d.points.length - 1];
    if (lastP) svg += `<circle cx="${X(idxOf.get(lastP.date))}" cy="${Y(conv(lastP.value))}" r="2.6" fill="${d.color}"/>`;
  }
  const evs = (events || []).map(e => ({ ...e, i: nearestDateIdx(dates, e.date) })).filter(e => e.i != null);
  for (const e of evs) svg += `<g class="event-mark" data-event="${esc(e.logical_id)}" role="button" aria-label="事件：${esc(e.title)}"><line x1="${X(e.i)}" x2="${X(e.i)}" y1="${mt}" y2="${mt + ih}"/><circle cx="${X(e.i)}" cy="${mt + 6}" r="3"/></g>`;
  svg += `<line id="cross-line" class="cross-line" x1="-10" x2="-10" y1="${mt}" y2="${mt + ih}" hidden/>`;
  svg += `</svg>`;
  return { svg, dates, X, seriesMaps, conv: v => v, ml, iw, mt, ih };
}
function nearestDateIdx(dates, date) {
  if (!dates.length || !date) return null;
  const d = date.slice(0, 10);
  let lo = 0, hi = dates.length - 1;
  if (d <= dates[0]) return 0;
  if (d >= dates[hi]) return hi;
  while (lo < hi - 1) { const mid = (lo + hi) >> 1; dates[mid] < d ? lo = mid : hi = mid; }
  return hi - d < d - dates[lo] ? hi : lo;
}
function attachChartInteraction(wrap, model, events, focus) {
  const svg = wrap.querySelector('svg[data-chart]');
  if (!svg) return;
  const readout = $('#chart-readout');
  const show = i => {
    const line = svg.querySelector('#cross-line');
    if (i == null) { line.setAttribute('hidden', ''); readout.innerHTML = defaultReadout(model); return; }
    line.removeAttribute('hidden');
    line.setAttribute('x1', model.X(i)); line.setAttribute('x2', model.X(i));
    const date = model.dates[i];
    const parts = model.seriesMaps.filter(s => s.points.length).map(s => {
      const v = s.map.get(date);
      return `<span style="color:${s.color === 'var(--accent)' ? 'var(--accent)' : s.color}">${esc(s.label)} <b class="mono">${v == null ? '—' : (state.compare && s.points[0]?.value > 0 ? fmt(v / s.points[0].value * 100, 1) : fmtSeriesValue(s.key, v))}</b></span>`;
    });
    readout.innerHTML = `<span class="mono">${date}</span>${parts.map(p => ' · ' + p).join('')}`;
    state.chart.hoverIdx = i;
  };
  svg.addEventListener('pointermove', e => {
    const r = svg.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width * 1000;
    const i = Math.round((x - model.ml) / model.iw * (model.dates.length - 1));
    show(Math.max(0, Math.min(model.dates.length - 1, i)));
  });
  svg.addEventListener('pointerleave', () => show(null));
  svg.addEventListener('keydown', e => {
    if (!['ArrowLeft', 'ArrowRight'].includes(e.key)) return;
    e.preventDefault();
    const cur = state.chart.hoverIdx == null ? model.dates.length - 1 : state.chart.hoverIdx;
    show(Math.max(0, Math.min(model.dates.length - 1, cur + (e.key === 'ArrowRight' ? 1 : -1))));
  });
  svg.addEventListener('click', e => {
    const mark = e.target.closest('.event-mark');
    if (mark) { const ev = (events || []).find(x => x.logical_id === mark.dataset.event); if (ev) selectEvent(ev, focus); }
  });
  show(null);
}
function defaultReadout(model) {
  const last = model.dates.at(-1);
  return model.seriesMaps.filter(s => s.points.length).map(s => {
    const v = s.points.at(-1).value;
    return `<span>${esc(s.label)} <b class="mono">${fmtSeriesValue(s.key, v)}</b></span>`;
  }).join(' · ') + `<span class="muted">（${last}）</span>`;
}
function selectEvent(ev, focus) {
  state.chart.eventDate = ev.event_time || ev.created_at;
  state.focus = { ...(focus || state.focus), type: 'event', id: ev.logical_id };
  render(); updateSideContext();
  const note = $('#event-detail');
  if (note) note.scrollIntoViewIfNeeded ? note.scrollIntoViewIfNeeded() : note.scrollIntoView({ block: 'nearest' });
}

/* ---------------- 主题焦点定义 ---------------- */
function focusFor(route) {
  const defs = {
    market: { series: ['SPY', 'QQQ', 'IWM'], labels: { SPY: 'SPY', QQQ: 'QQQ', IWM: 'IWM' } },
    metals: { series: ['GLD', 'SLV', 'CPER'], labels: { GLD: '黄金 GLD', SLV: '白银 SLV', CPER: '铜 CPER' } },
    semis: { series: ['SOXX', 'AVGO', 'TER'], labels: { SOXX: '半导体 SOXX', AVGO: 'AVGO', TER: 'TER' } }
  };
  return defs[route] || null;
}
function slotFocus(slot) { return { type: 'slot', id: slot.id, series: slot.series, labels: null, slot }; }

/* ---------------- 事件与证据 ---------------- */
async function themeMessages(route) {
  const topicMap = { market: ['宏观', '市场', 'market'], metals: ['金银', '黄金', '白银', 'metals'], semis: ['半导体', 'semis', 'AI capex', '电力'] };
  const topics = topicMap[route] || [];
  let all = [];
  for (const t of topics) { try { const r = await request('messages', { query: { topic: t, limit: 40 } }); all.push(...r.messages); } catch (_) {} }
  const seen = new Set();
  return all.filter(m => !seen.has(m.logical_id) && seen.add(m.logical_id));
}

/* ---------------- 渲染：左导航 ---------------- */
function renderRail() {
  const now = new Date();
  const c = state.context;
  const due = c?.counts?.verify_due || 0;
  const failures = c?.counts?.recent_failures || 0;
  const unreadish = (c?.counts?.by_kind?.event || 0) + (c?.counts?.by_kind?.fact || 0);
  const badge = n => n ? `<span class="count">${n}</span>` : '';
  $('#rail').innerHTML = `
    <div class="rail-date"><b>${now.getMonth() + 1}月${now.getDate()}日</b>${'日一二三四五六'[now.getDay()]} · ${now.getFullYear()}</div>
    ${ROUTES.map(r => `<button class="nav ${state.route === r.id ? 'active' : ''}" data-route="${r.id}">${r.title}
      ${r.id === 'today' ? badge(unreadish) : ''}${r.id === 'diary' ? badge(due) : ''}${r.id === 'automation' ? badge(failures) : ''}</button>`).join('')}
    <p class="rail-note">研究池 v${esc(c?.pool_version || '?')} · 20 标的<br>数据截止 ${esc(fmtDate(c?.data_cutoff))}<br>${c?.db_ready ? '持久库正常' : '持久库不可用'}</p>`;
}

/* ---------------- 渲染：今日 ---------------- */
function renderToday() {
  const c = state.context;
  const slots = c?.slots || [];
  const updates = state.messages.filter(m => ['event', 'fact'].includes(m.kind)).slice(0, 5);
  return `${crumbsHTML([{ label: '今日总览', to: '' }])}
  <div class="page-head"><h2>今日总览</h2><span class="sub">12 个固定槽位 · 顺序稳定，不随涨跌重排</span>${chipStatus(slots.every(s => s.status === 'ok') ? 'ok' : 'partial')}</div>
  <section class="slots" aria-label="核心观察槽位">${slots.map((s, i) => slotCard(s, i)).join('')}</section>
  ${c?.db_note ? `<div class="gate">${esc(c.db_note)}</div>` : ''}
  <section class="board" aria-label="消息看板">
    <div class="page-head" style="margin-top:24px"><h2 style="font-size:18px">消息看板</h2><span class="sub">同根来源去重；AI 解释带标签</span></div>
    ${boardTabs()}
    ${state.messages.length ? state.messages.slice(0, 12).map(msgCard).join('') : `<div class="empty">该视图暂无消息。<br>刷新数据或等待定时任务入库后显示；不编造填充。</div>`}
    ${boardFoot(updates.length)}
  </section>`;
}
function slotCard(s, i) {
  const partsHtml = (s.parts || []).map(p => `<span class="v"><b class="${p.change1d > 0 ? 'chg up' : p.change1d < 0 ? 'chg down' : ''}">${p.status === 'missing' ? '—' : fmt(p.value, p.key === 'DTWEXBGS' ? 1 : 2)}</b><small>${esc(p.label)} ${p.change1d != null && p.status !== 'missing' ? pct(p.change1d) : ''}</small></span>`).join('');
  const derived = s.derived ? `<div class="derived">${esc(s.derived.label)}：<b class="mono">${fmt(s.derived.value, 3)}</b> <small>${fmtDate(s.derived.date)}${s.derived.note ? ' · ' + esc(s.derived.note) : ''}</small></div>` : '';
  const dates = (s.parts || []).map(p => p.date).filter(Boolean);
  return `<button class="slot ${s.status}" data-slot="${s.id}" aria-label="${esc(s.title)}，${s.status === 'ok' ? '数据可用' : s.status === 'missing' ? '未接入' : '部分可用'}">
    <span class="badge">${chipStatus(s.status)}</span>
    <span class="slot-head"><span class="slot-no">${String(i + 1).padStart(2, '0')}</span><span class="slot-title">${esc(s.title)}</span></span>
    ${s.parts?.length && s.status !== 'missing' ? `<span class="values">${partsHtml}</span>${derived}
      <span class="meta"><span>截至 ${esc(dates.at(-1) || '—')}</span>${(s.parts || []).map(p => p.provider ? `<span>${esc(p.provider)}</span>` : '').slice(0, 2).join('')}</span>`
      : `<span class="missing-note">${esc(s.sourceCard ? s.sourceCard.note : (s.gapNote || s.note || '该槽位尚未接入数据源；保留位置与口径说明。'))}${s.sourceCard ? `<br><a href="${esc(s.sourceCard.url)}" target="_blank" rel="noopener">来源：${esc(s.sourceCard.provider)} ↗</a>` : ''}</span>`}
  </button>`;
}
function boardTabs() {
  const counts = state.context?.counts || {};
  const n = { needs: counts.verify_due + (counts.recent_failures || 0), updates: (counts.by_kind?.event || 0) + (counts.by_kind?.fact || 0), opinions: counts.by_kind?.opinion || 0, health: counts.by_kind?.health || 0 };
  return `<div class="board-tabs" role="tablist">${Object.entries(VIEW_META).map(([id, title]) =>
    `<button role="tab" aria-selected="${state.view === id}" data-view="${id}">${title}${n[id] ? `<span class="n">${n[id]}</span>` : ''}</button>`).join('')}</div>`;
}
function boardFoot(shown) {
  return `<div class="board-foot"><span>首页最多展示 5 条重点更新，其余在对应视图；排序先按可处理性与重要性，再按时间。</span><span>互动量 ≠ 重要性</span></div>`;
}
function msgCard(m) {
  const cls = m.read ? '' : 'unread';
  const stance = m.stance ? ` <span class="stance-${m.stance}">${{ bull: '看多', bear: '看空', mixed: '混合', unknown: '未知' }[m.stance]}</span>` : '';
  return `<article class="msg ${cls} ${state.subtab === m.logical_id ? 'expanded' : ''}" data-msg="${esc(m.logical_id)}">
    <div class="msg-head">
      <span class="kind ${m.kind}">${KIND_CN[m.kind] || m.kind}</span>${importanceDots(m.importance)}
      <span class="msg-title">${esc(m.title)}</span>${stance}${m.category === 'ai_explainer' ? '<span class="cat">AI 解释</span>' : m.category === 'external_opinion' ? '<span class="cat">外部观点</span>' : ''}
    </div>
    <div class="msg-body">${esc(m.body || '（无正文）')}</div>
    <div class="msg-meta">
      ${m.event_time ? `<span>事件时间 ${esc(fmtDate(m.event_time))}</span>` : ''}
      <span>入库 ${esc((m.created_at || '').slice(0, 16).replace('T', ' '))}</span>
      ${m.author ? `<span>${esc(m.author)}</span>` : ''}
      ${m.topics?.length ? `<span>${m.topics.map(esc).join(' / ')}</span>` : ''}
      ${m.symbols?.length ? `<span class="mono">${m.symbols.join(' ')}</span>` : ''}
      ${m.url ? `<a href="${esc(m.url)}" target="_blank" rel="noopener">原文 ↗</a>` : ''}
      ${m.coverage_note ? `<span>${esc(m.coverage_note)}</span>` : ''}
    </div>
    <div class="msg-actions">
      <button data-msg-toggle="${esc(m.logical_id)}">${document.querySelector(`[data-msg="${CSS.escape(m.logical_id)}"]`)?.classList.contains('expanded') ? '收起' : '展开'}</button>
      <button data-msg-read="${esc(m.logical_id)}">${m.read ? '标为未读' : '标为已读'}</button>
      ${state.view === 'needs' ? `<button data-msg-handle="${esc(m.logical_id)}" data-act="handle">已处理</button><button data-msg-handle="${esc(m.logical_id)}" data-act="snooze">延后</button>` : ''}
      ${m.kind === 'opinion' ? `<button data-msg-note="${esc(m.logical_id)}">记我的应对</button>` : ''}
    </div>
  </article>`;
}

/* ---------------- 渲染：主题页（市场/金银/半导体） ---------------- */
function renderTheme(route) {
  const theme = THEMES[route];
  const defaultFocus = focusFor(route);
  const focus = state.focus?.series ? state.focus : defaultFocus;
  const datasets = chartDataFor(focus);
  const crumbs = [{ label: '今日', to: 'today' }, { label: theme.title, to: route }];
  if (state.focus?.slot?.title) crumbs.push({ label: state.focus.slot.title, to: route });
  if (state.focus?.type === 'event') crumbs.push({ label: '事件详情', to: route });
  const chart = renderChartSVG(chartWidth(), chartHeight(), datasets, state.themeEvents || []);
  return `${crumbsHTML(crumbs)}
  <div class="page-head"><h2>${theme.title}</h2><span class="sub">${theme.sub}</span></div>
  ${themeExtra(route)}
  <section class="panel" style="margin-top:14px">
    <div class="panel-head">
      <h3>${esc(focus.slot?.title || theme.title + ' · 趋势')}</h3>
      <div class="range-chips" role="group" aria-label="时间区间">${Object.keys(RANGES).map(r => `<button data-range="${r}" aria-pressed="${state.range === r}" ${datasets.every(d => !d.points.length) ? 'disabled' : ''}>${r}</button>`).join('')}</div>
      ${focus.series.length > 1 ? `<button data-compare aria-pressed="${state.compare}" title="区间起点归一化对比，不同量纲不叠轴">归一对比</button>` : ''}
      <span class="grow"></span>${chipStatus(datasets.some(d => d.points.length) ? (datasets.every(d => d.points.length > 200 || state.range !== '3Y') ? 'ok' : 'partial') : 'missing')}
    </div>
    <div class="chart-wrap" id="chart-wrap">${chart.svg}</div>
    <div class="chart-legend" id="chart-readout" role="status" aria-live="polite"></div>
    <div class="chart-note">${datasets.map(d => d.points.length ? `<b>${esc(d.label)}</b> ${d.points.length} 点（${d.points[0].date} → ${d.points.at(-1).date}）· ${esc(d.provider || '')}${d.basis ? ' · ' + esc(d.basis) : ''}` : `<b>${esc(d.label)}</b> 无数据`).join('<br>')}
    ${state.range === '3Y' && datasets.some(d => d.points.length && d.points.length < 300) ? '<br>注意：部分序列历史不足 3 年，已按实际长度缩短显示。' : ''}</div>
    <div class="subtabs" role="tablist">
      <button role="tab" aria-selected="${state.subtab === 'chart'}" data-subtab="chart">趋势</button>
      <button role="tab" aria-selected="${state.subtab === 'events'}" data-subtab="events">事件时间线</button>
      <button role="tab" aria-selected="${state.subtab === 'evidence'}" data-subtab="evidence">证据墙</button>
    </div>
    ${state.subtab === 'events' ? timelineHTML() : state.subtab === 'evidence' ? evidenceHTML(route) : `<div id="event-detail">${state.focus?.type === 'event' ? eventDetailHTML() : ''}</div>`}
  </section>
  ${route === 'metals' ? metalsExtras() : ''}${route === 'market' ? marketExtras() : ''}`;
}
function chartWidth() { const el = $('#center'); return Math.max(320, Math.min(980, el ? el.clientWidth - 44 : 760)); }
function chartHeight() { return innerWidth < 720 ? 220 : 300; }
function themeExtra(route) {
  if (route === 'semis') {
    const slots = (state.context?.slots || []).filter(s => s.theme === 'semis');
    return `<div class="cards2">${slots.map(s => `<div class="mini-card src-card"><h4>${esc(s.title)}</h4><p>${esc(s.sourceCard?.note || '')}</p><p class="muted">数值未接入时显示来源卡；由哨兵任务人工/AI 读页后经 ingest_batch 入库，不编造分数。</p><div class="go"><a href="${esc(s.sourceCard?.url)}" target="_blank" rel="noopener">打开 ${esc(s.sourceCard?.provider)} ↗</a></div></div>`).join('')}
      <div class="mini-card"><h4>产业基础数据</h4><p>SIA 月度销售、台湾月营收、韩国出口、存储价格与公司披露按原始发布频率接入；不生成假日更数值。</p><p class="muted">当前状态：待登记来源。</p></div></div>`;
  }
  return '';
}
function timelineHTML() {
  const evs = (state.themeEvents || []).slice().sort((a, b) => (b.event_time || b.created_at || '').localeCompare(a.event_time || a.created_at || ''));
  if (!evs.length) return `<div class="empty">当前主题暂无入库事件。<br>事件由官方哨兵与导入批次写入；时间线与图表共用时间窗口。</div>`;
  return `<div class="timeline" role="list">${evs.map(e => `<div class="tl-row ${state.chart.eventDate && (e.event_time || '').slice(0, 10) === state.chart.eventDate.slice(0, 10) ? 'selected' : ''}" role="listitem" tabindex="0" data-tl="${esc(e.logical_id)}">
    <span class="tl-date">${esc(fmtDate(e.event_time || e.created_at))}</span>
    <span class="tl-title">${esc(e.title)}</span>
    <span class="kind ${e.kind}">${KIND_CN[e.kind] || e.kind}</span>
  </div>`).join('')}</div>`;
}
function evidenceHTML(route) {
  const evs = state.themeEvents || [];
  const groups = { fact: [], external_opinion: [], ai_explainer: [] };
  for (const e of evs) (groups[e.category] || (groups[e.category] = [])).push(e);
  return `<div class="evidence">${Object.entries(groups).filter(([, list]) => list.length).map(([cat, list]) => `<div class="ev-group"><h4>${CAT_CN[cat] || cat} · ${list.length}</h4>${list.map(e => `<div class="ev-item"><div class="t">${esc(e.title)}</div><div class="m"><span>${esc(fmtDate(e.event_time || e.created_at))}</span>${e.author ? `<span>${esc(e.author)}</span>` : ''}${e.url ? `<a href="${esc(e.url)}" target="_blank" rel="noopener">原文 ↗</a>` : ''}<span class="mono">${esc(e.root_source_id || '')}</span></div></div>`).join('')}</div>`).join('') || '<div class="empty">暂无入库证据。</div>'}</div>`;
}
function eventDetailHTML() {
  const e = (state.themeEvents || []).find(x => x.logical_id === state.focus?.id) || state.messages.find(x => x.logical_id === state.focus?.id);
  if (!e) return '';
  return `<div class="ev-item" style="margin:12px 16px"><div class="t">${esc(e.title)}</div><div class="m"><span class="kind ${e.kind}">${KIND_CN[e.kind]}</span><span>${esc(fmtDate(e.event_time || e.created_at))}</span>${e.url ? `<a href="${esc(e.url)}" target="_blank" rel="noopener">原文 ↗</a>` : ''}</div>${e.body ? `<div class="msg-body" style="display:block;margin-top:8px">${esc(e.body)}</div>` : ''}</div>`;
}
function metalsExtras() {
  const s = state.context?.slots?.find(x => x.id === 'gsr');
  return `<section class="panel" style="margin-top:14px"><div class="panel-head"><h3>金银比</h3><span class="sub">${s?.derived ? `${fmt(s.derived.value, 3)}（${fmtDate(s.derived.date)}）` : '缺任一侧则不显示'}</span></div>
  <p class="chart-note" style="padding-top:12px">${esc(s?.derived?.note || 'ETF 价格比（GLD/SLV），显式口径；不是现货金银比。')}<br>GLD/SLV 是 ETF 价格代理；基金费用、换月与供求都会让比值偏离现货金银比。三资产同涨同跌不能证明同一驱动。</p></section>
  <div class="cards2">
    <div class="mini-card"><h4>下一步验证：实际利率与美元</h4><p>利率变化是否与金属价格同一时钟？美元与风险偏好能否提供替代解释？（B301 → A101）</p></div>
    <div class="mini-card"><h4>下一步验证：库存与期限结构</h4><p>价格变化是否有库存、期限结构与需求数据支持？供给约束与资本周期能否解释分化？（D302 / E203）</p></div>
  </div>`;
}
function marketExtras() {
  const rule = state.catalog?.rules?.[0];
  const jnk = state.series.JNK, spy = state.series.SPY;
  return `<section class="panel" style="margin-top:14px"><div class="panel-head"><h3>JNK–SPY 经验规则（展开）</h3><span class="sub">${esc(rule?.status || '')}</span></div>
  <p class="chart-note" style="padding-top:12px">${esc(rule?.note || '规则目录尚未提供')}<br>当前触发计算未启用；−1.5 是历史经验口径，不是价格跌幅阈值，更不是自动交易条件。日线不能替代规则需要的同步数据。</p>
  <div class="cards2" style="padding:0 16px 14px">${(rule?.versions || []).slice(0, 2).map(v => `<div class="mini-card"><h4>${esc(v.name)}</h4><p>${esc(v.threshold)}</p><p class="muted">${esc(v.status)}</p></div>`).join('')}</div></section>`;
}

/* ---------------- 渲染：研究池 ---------------- */
function renderPool() {
  const quotes = state.snapshot?.quotes || [];
  const pool = ['TER','AVGO','UNH','SILJ','APP','BWXT','VST','LMT','LNN','LIN','TRP','WDC','CRWV','MOS','GEV','RCL','SLV','XAR','NLR','TSLA'];
  const aux = ['TSLL','SPY','QQQ','SOXX','JNK','HYG','IEF'];
  const row = sym => {
    const q = quotes.find(x => x.symbol === sym);
    const status = !q || q.status === 'missing' ? 'missing' : q.status === 'stale' ? 'stale' : 'ok';
    return `<tr data-sym="${sym}"><td class="sym">${sym}</td><td>${esc(q?.label?.split('·')[0] || '—')}</td>
    <td>${q?.close != null ? fmt(q.close) : '—'}</td>
    <td class="${(q?.change1d || 0) > 0 ? 'up' : (q?.change1d || 0) < 0 ? 'down' : ''}">${pct(q?.change1d)}</td>
    <td class="${(q?.return21d || 0) > 0 ? 'up' : (q?.return21d || 0) < 0 ? 'down' : ''}">${pct(q?.return21d)}</td>
    <td class="${(q?.ma50Distance || 0) > 0 ? 'up' : (q?.ma50Distance || 0) < 0 ? 'down' : ''}">${pct(q?.ma50Distance)}</td>
    <td>${esc(q?.asOf || '—')}</td><td>${esc(status === 'ok' ? (q.provider || '') : { missing: '未接入', stale: '陈旧' }[status])}</td></tr>`;
  };
  return `${crumbsHTML([{ label: '今日', to: 'today' }, { label: '20 标的研究池', to: 'pool' }])}
  <div class="page-head"><h2>20 标的研究池</h2><span class="sub">版本 ${esc(state.context?.pool_version || '?')} · 研究池 ≠ 持仓 · 账户模块：未接入</span></div>
  <section class="panel"><div class="panel-head"><h3>主池</h3><span class="sub">复用既有观察条件；点击代码看趋势</span></div>
  <div style="overflow-x:auto"><table class="pool"><thead><tr><th>代码</th><th>名称</th><th>收盘</th><th>1日</th><th>21日</th><th>距MA50</th><th>数据日</th><th>来源</th></tr></thead><tbody>${pool.map(row).join('')}</tbody></table></div></section>
  <section class="panel" style="margin-top:14px"><div class="panel-head"><h3>辅助观察</h3><span class="sub">保留角色，不扩写成持仓</span></div>
  <div style="overflow-x:auto"><table class="pool"><thead><tr><th>代码</th><th>名称</th><th>收盘</th><th>1日</th><th>21日</th><th>距MA50</th><th>数据日</th><th>来源</th></tr></thead><tbody>${aux.map(row).join('')}</tbody></table></div></section>`;
}

/* ---------------- 渲染：日记本 ---------------- */
function renderDiary() {
  const list = state.notes;
  const sel = state.notes.find(n => n.id === state.noteSel);
  return `${crumbsHTML([{ label: '今日', to: 'today' }, { label: '投资日记', to: 'diary' }])}
  <div class="page-head"><h2>投资日记</h2><span class="sub">原文与 AI 草稿分开 · 停止输入约 1 秒自动保存 · 支持系统听写</span></div>
  <div class="diary-grid">
    <section>
      ${list.length ? list.map(n => `<div class="note-item ${n.id === state.noteSel ? 'selected' : ''}" data-note="${esc(n.id)}" tabindex="0" role="button">
        <div class="n-date">${esc((n.created_at || '').slice(0, 16).replace('T', ' '))} · v${n.revision}${n.status !== 'active' ? ' · ' + (n.status === 'done' ? '已复盘' : '已归档') : ''}${n.verify_date ? ' · 验证 ' + esc(n.verify_date) : ''}</div>
        <div class="n-text">${esc(n.text_original || '')}</div>
        ${n.topics?.length || n.symbols?.length ? `<div class="n-tags">${[...(n.topics || []), ...(n.symbols || [])].map(t => `<span class="chip">${esc(t)}</span>`).join('')}</div>` : ''}
      </div>`).join('') : `<div class="empty">还没有日记。右侧「快速记录」随时可写；写下判断与下一验证，到期会出现在「需我处理」。</div>`}
    </section>
    <section class="panel editor" id="diary-editor">${diaryEditorHTML(sel)}</section>
  </div>`;
}
function diaryEditorHTML(sel) {
  if (!sel) return `<div class="panel-head"><h3>日记详情</h3></div><p class="empty" style="border:0">选择左侧一条日记查看原文、版本与 AI 草稿。</p>`;
  return `<div class="panel-head"><h3>${esc((sel.created_at || '').slice(0, 10))} · ${esc(sel.id)}</h3><span class="sub">v${sel.revision}</span></div>
  <div style="padding:14px 16px">
    <textarea id="diary-text" aria-label="日记原文（编辑后自动保存新版本）">${esc(sel.text_original || '')}</textarea>
    <div class="row" style="display:flex;gap:8px;margin-top:9px;flex-wrap:wrap">
      <input type="date" id="diary-verify" value="${esc(sel.verify_date || '')}" aria-label="下一验证日期">
      <input type="text" id="diary-verify-q" placeholder="要验证什么（可证伪的问题）" value="${esc(sel.verify_question || '')}" style="flex:1">
    </div>
    <div class="save-state" id="diary-save">只读展示；编辑将在停止输入 1 秒后自动保存为新版本。</div>
    <div class="versions"><h4 style="font-size:12px;color:var(--muted);margin-bottom:8px">版本历史（原文不可倒改，复盘只写结果）</h4>
      <div class="version"><div class="v-head"><span>v${sel.revision} · 用户原文 · ${esc((sel.updated_at || '').slice(0, 16).replace('T', ' '))}</span></div><div class="v-text">${esc(sel.text_original || '')}</div></div>
      <div style="display:flex;gap:8px;margin-top:10px;flex-wrap:wrap">
        <button data-note-done="${esc(sel.id)}" ${sel.status === 'done' ? 'disabled' : ''}>标记已复盘</button>
        <button data-note-archive="${esc(sel.id)}">归档</button>
        <button data-note-outcome="${esc(sel.id)}">写复盘结果</button>
      </div>
    </div>
  </div>`;
}

/* ---------------- 渲染：报告 ---------------- */
function renderReports() {
  const reports = state.messages.filter(m => m.kind === 'report');
  return `${crumbsHTML([{ label: '今日', to: 'today' }, { label: '报告', to: 'reports' }])}
  <div class="page-head"><h2>日 · 周 · 月报</h2><span class="sub">报告可追溯到原事件与日记；未到期与不可判定明确标注</span></div>
  ${reports.length ? reports.map(m => `<article class="report-item"><h4>${esc(m.title)}</h4>
    <div class="msg-meta"><span>${esc(fmtDate(m.event_time || m.created_at))}</span>${m.url ? `<a href="${esc(m.url)}" target="_blank" rel="noopener">原文 ↗</a>` : ''}</div>
    <div class="report-body">${esc(m.body || '')}</div></article>`).join('') : `<div class="empty">还没有报告入库。<br>晨报（D 组任务）产出后会经 ingest_batch 进入这里；不会用旧报告冒充今日。</div>`}`;
}

/* ---------------- 渲染：自动化 ---------------- */
const GROUPS = { A: '市场与研究状态（08:10 / 20:10）', B: '推特增量采集（05:30）', C: '官方事件哨兵（08:35 / 16:35 / 23:35）', D: '投资晨报（09:00）', E: '投资周报（周日 18:00）', F: '投资月报（每月 1 日 10:00）' };
function renderAutomation() {
  const byGroup = {};
  for (const t of state.tasks) (byGroup[t.group_id] || (byGroup[t.group_id] = [])).push(t);
  const verified = state.tasks[0]?.verified_at;
  return `${crumbsHTML([{ label: '今日', to: 'today' }, { label: '自动化', to: 'automation' }])}
  <div class="page-head"><h2>自动化</h2><span class="sub">六组物理调度 · 状态来自宿主调度读回${verified ? ' · 最后核验 ' + esc(verified.slice(0, 16).replace('T', ' ')) : ''}</span></div>
  <div class="task-group">${Object.entries(GROUPS).map(([g, label]) => {
    const tasks = byGroup[g] || [];
    return `<div class="task-card"><span class="g">${g} 组</span><h4>${esc(label)}</h4>
      ${tasks.length ? tasks.map(t => `<div class="kv"><b>${esc(t.name)}</b><br>${esc(t.cron_expr || '')} ${esc(t.timezone || '')} · ${esc(t.execution || 'agent')} · <span class="${t.status === 'active' ? 'up' : ''}">${esc(t.status || '?')}</span>${t.last_run ? `<br>最近运行：${esc(String(t.last_run.firedAt || t.last_run.status || '')).slice(0, 40)}` : ''}${t.device ? '<br>设备：' + esc(t.device) : ''}</div>`).join('') : '<div class="kv">未登记（尚未创建或未同步）</div>'}
    </div>`;
  }).join('')}</div>
  <section class="panel" style="margin-top:14px"><div class="panel-head"><h3>最近运行</h3><span class="sub">含失败与恢复；成功恢复后同一问题闭环</span></div>
  <div style="padding:8px 16px 14px">${state.runs.length ? state.runs.map(r => `<div class="run-row"><span class="st ${esc(r.status)}">${esc(r.status)}</span><span>${esc((r.started_at || '').slice(0, 16).replace('T', ' '))}</span><span>${esc(r.task_key || '')}</span><span style="flex:1;min-width:200px">${esc(r.summary || '')}</span></div>`).join('') : '<p class="empty" style="border:0">暂无运行记录。</p>'}</div></section>
  <div class="gate">管理入口：任务的创建、暂停与修改在 Cindy 的原生任务页完成（不在插件里伪造管理按钮）。宿主应用退出或机器休眠时任务不会运行，恢复后只补最近一批必要工作。状态由 Agent 同步时经 sync_automation_status 写入，插件缓存不冒充宿主真相。</div>`;
}

/* ---------------- 渲染：右操作台 ---------------- */
let quick = { noteId: null, revision: null, timer: null, state: 'idle', lastError: null };
function initSide() {
  $('#side').innerHTML = `
    <section class="panel-s quick" aria-label="快速记录">
      <h3>快速记录 <small>投资日记</small></h3>
      <textarea id="quick-text" placeholder="记下你观察到的、想验证的、打算做的…（支持系统听写：输入法麦克风）" aria-label="日记正文"></textarea>
      <div class="row"><input type="text" id="quick-topics" placeholder="主题，逗号分隔（默认带当前上下文）" aria-label="主题"><input type="date" id="quick-verify" aria-label="下一验证日期"></div>
      <div class="row"><input type="text" id="quick-verify-q" placeholder="到那天要验证什么？" style="flex:1" aria-label="验证问题"></div>
      <div class="save-state" id="quick-save" role="status">开始输入后自动保存；只有写入成功才显示「已保存」。</div>
      <div class="row"><button id="quick-clear">写完清空</button><span class="grow" style="flex:1"></span><button id="quick-retry" hidden>重试保存</button></div>
      <div id="quick-conflict"></div>
    </section>
    <section class="panel-s" aria-label="当前上下文"><h3>当前上下文 <small>自动附加</small></h3><div class="ctx-list" id="side-ctx"></div></section>
    <section class="panel-s" aria-label="参考与观点"><h3>观点参考 <small>别人怎么想</small></h3><div id="side-refs"><p class="muted" style="font-size:12px">选择主题或事件后，这里显示相关外部观点与分歧；你的应对写在上面。</p></div></section>`;
  const text = $('#quick-text');
  try { const saved = JSON.parse(localStorage.getItem('desk-quick-v2') || 'null'); if (saved) { text.value = saved.text || ''; $('#quick-topics').value = saved.topics || ''; $('#quick-verify').value = saved.verify || ''; $('#quick-verify-q').value = saved.verifyQ || ''; quick.noteId = saved.noteId || null; quick.revision = saved.revision || null; if (saved.unsynced) setQuickState('failed', '上次保存未完成：内容已保留，点「重试保存」。'); } } catch (_) {}
  text.addEventListener('input', () => { mirrorQuick(true); clearTimeout(quick.timer); quick.timer = setTimeout(autoSaveQuick, 1000); });
  for (const id of ['quick-topics', 'quick-verify', 'quick-verify-q']) $('#' + id).addEventListener('input', () => { mirrorQuick(); clearTimeout(quick.timer); quick.timer = setTimeout(autoSaveQuick, 1000); });
  $('#quick-clear').addEventListener('click', () => {
    text.value = ''; $('#quick-topics').value = ''; $('#quick-verify').value = ''; $('#quick-verify-q').value = '';
    quick.noteId = null; quick.revision = null; $('#quick-conflict').innerHTML = ''; mirrorQuick(); setQuickState('idle', '开始输入后自动保存。');
  });
  $('#quick-retry').addEventListener('click', () => autoSaveQuick(true));
  updateSideContext(); updateSideRefs();
}
function mirrorQuick(unsynced) {
  try { localStorage.setItem('desk-quick-v2', JSON.stringify({ text: $('#quick-text').value, topics: $('#quick-topics').value, verify: $('#quick-verify').value, verifyQ: $('#quick-verify-q').value, noteId: quick.noteId, revision: quick.revision, unsynced: !!unsynced && $('#quick-text').value.trim() })); } catch (_) {}
}
function setQuickState(st, msg) { quick.state = st; const el = $('#quick-save'); el.className = 'save-state ' + st; el.textContent = msg; $('#quick-retry').hidden = st !== 'failed'; }
function currentContext() {
  const c = { theme: null, slot: null, event: null, sources: [] };
  const route = ROUTES.find(r => r.id === state.route);
  if (route?.theme) c.theme = THEMES[route.theme].title;
  if (state.focus?.slot?.title) c.slot = state.focus.slot.title;
  else if (state.focus?.type === 'slot') { const s = (state.context?.slots || []).find(x => x.id === state.focus.id); if (s) c.slot = s.title; }
  if (state.focus?.type === 'event') { const e = (state.themeEvents || []).find(x => x.logical_id === state.focus.id); if (e) { c.event = e.title; if (e.url) c.sources.push({ title: e.title, url: e.url }); } }
  if (state.chart.eventDate) c.as_of = state.chart.eventDate.slice(0, 10);
  return c;
}
function updateSideContext() {
  const el = $('#side-ctx'); if (!el) return;
  const c = currentContext();
  el.innerHTML = `<div>主题 <b>${esc(c.theme || '—')}</b> · 槽位 <b>${esc(c.slot || '—')}</b></div>
    ${c.event ? `<div>事件 <b>${esc(c.event)}</b>${c.as_of ? ' · ' + esc(c.as_of) : ''}</div>` : ''}
    <div>数据截止 <b>${esc(fmtDate(state.context?.data_cutoff))}</b>${state.snapshot?.fetchedAt ? ' · 刷新 ' + esc(state.snapshot.fetchedAt.slice(0, 16).replace('T', ' ')) : ''}</div>
    <div class="muted">保存日记时，以上下文与相关链接自动附加。</div>`;
}
async function autoSaveQuick(force) {
  const text = $('#quick-text').value;
  if (!text.trim()) { if (quick.noteId) setQuickState('idle', '正文为空；已保存的版本保留。'); return; }
  if (quick.state === 'saving') return;
  setQuickState('saving', '正在保存…');
  const input = {
    note_id: quick.noteId || undefined, base_revision: quick.noteId ? quick.revision : undefined, text,
    topics: ($('#quick-topics').value || '').split(/[,，]/).map(s => s.trim()).filter(Boolean),
    verify_date: $('#quick-verify').value || null, verify_question: $('#quick-verify-q').value || null,
    context: currentContext()
  };
  try {
    const r = await request('notes.save', { input });
    if (r.action === 'conflict') { showQuickConflict(r); setQuickState('failed', '两台端都改过这条日记；请在下方选择保留哪一版。'); return; }
    if (r.action === 'noop') { setQuickState('saved', '已保存（无变化）· ' + (r.saved_at || '').slice(11, 16)); }
    else { quick.noteId = r.note_id; quick.revision = r.revision; setQuickState('saved', '已保存 · ' + (r.saved_at || '').slice(11, 16) + ' · v' + r.revision); }
    mirrorQuick();
  } catch (e) { setQuickState('failed', '未同步：' + e.message); mirrorQuick(true); if (force) {} }
}
function showQuickConflict(r) {
  $('#quick-conflict').innerHTML = `<div class="conflict-box"><b>编辑冲突</b>：此日记在另一端被修改。两个版本都已保留，请选择：<pre><b>另一端的版本（v${r.server.revision}，${esc((r.server.updated_at || '').slice(0, 16).replace('T', ' '))}）：</b>\n${esc(r.server.text)}</pre><pre><b>你现在写的：</b>\n${esc(r.yours.text)}</pre>
  <div class="row"><button id="conflict-server">保留另一端</button><button id="conflict-mine">保留我写的</button></div></div>`;
  $('#conflict-server').addEventListener('click', async () => {
    const server = await request('notes.list', { query: { limit: 200 } });
    const note = server.notes.find(n => n.id === quick.noteId);
    if (note) { $('#quick-text').value = note.text_original; quick.revision = note.revision; }
    $('#quick-conflict').innerHTML = ''; setQuickState('saved', '已保留另一端版本。'); mirrorQuick();
  });
  $('#conflict-mine').addEventListener('click', async () => {
    const r2 = await request('notes.save', { input: { note_id: quick.noteId, base_revision: r.server.revision, text: $('#quick-text').value, context: currentContext() } });
    quick.revision = r2.revision; $('#quick-conflict').innerHTML = ''; setQuickState('saved', '已保留你写的版本 · v' + r2.revision); mirrorQuick();
  });
}
async function updateSideRefs() {
  const el = $('#side-refs'); if (!el) return;
  try {
    const r = await request('messages', { query: { view: 'opinions', limit: 6 } });
    el.innerHTML = r.messages.length ? r.messages.map(m => `<div class="ref"><b>${esc(m.author || '匿名')}</b> <span class="stance-${m.stance}">${m.stance ? { bull: '看多', bear: '看空', mixed: '混合', unknown: '' }[m.stance] : ''}</span><br>${esc(m.title)}<br><small>${esc(fmtDate(m.event_time || m.created_at))}${m.url ? ' · <a href="' + esc(m.url) + '" target="_blank" rel="noopener">原文 ↗</a>' : ''}</small></div>`).join('') + `<p class="muted" style="font-size:11px;margin-top:8px">立场按独立作者计数；同根信息只计一次。</p>` : '<p class="muted" style="font-size:12px">观点流暂无入库内容。</p>';
  } catch (_) {}
}

/* ---------------- 主渲染 ---------------- */
function render() {
  const views = { today: renderToday, market: renderTheme, metals: renderTheme, semis: renderTheme, pool: renderPool, diary: renderDiary, reports: renderReports, automation: renderAutomation };
  /* 视图函数需要路由参数（renderTheme 依赖它取主题与默认焦点）；漏传会让 focusFor 返回 null 导致整页导航静默失败 */
  $('#center').innerHTML = (views[state.route] || renderToday)(state.route);
  if (['market', 'metals', 'semis'].includes(state.route)) {
    const focus = state.focus?.series ? state.focus : focusFor(state.route);
    const datasets = chartDataFor(focus);
    const chart = renderChartSVG(chartWidth(), chartHeight(), datasets, state.themeEvents || []);
    const wrap = $('#chart-wrap');
    if (wrap) { wrap.innerHTML = chart.svg; attachChartInteraction(wrap, chart, state.themeEvents, focus); }
  }
  renderRail();
}
async function navigate(route, opts = {}) {
  state.route = route;
  state.focus = opts.focus || null; state.subtab = 'chart'; state.themeEvents = [];
  $('#center').innerHTML = '<p class="muted">载入中…</p>';
  try {
    if (['market', 'metals', 'semis'].includes(route)) {
      const focus = state.focus?.series ? state.focus : focusFor(route);
      await loadSeries(focus.series);
      state.themeEvents = (await themeMessages(route)).filter(m => m.event_time || m.created_at);
    }
    if (route === 'pool') await loadSnapshot();
    if (route === 'diary') await loadNotes();
    if (route === 'reports') await loadMessages();
    if (route === 'automation') await loadTasks();
    render(); updateSideContext();
    if (route === 'today') updateSideRefs();
  } catch (e) { $('#center').innerHTML = `<div class="empty"><strong>载入失败</strong>${esc(e.message)}</div>`; renderRail(); }
}

/* ---------------- 交互绑定 ---------------- */
$('#center').addEventListener('click', async e => {
  const t = e.target.closest('button,a,[data-sym],[data-tl],[data-note]');
  if (!t || t.tagName === 'A') return;
  if (t.dataset.route) { navigate(t.dataset.route); return; }
  if (t.dataset.nav != null) { const [route, slotId] = t.dataset.nav.split('|'); navigate(route, slotId ? { focus: { type: 'slot', id: slotId, series: ((state.context?.slots || []).find(s => s.id === slotId)?.series) || [] } } : {}); return; }
  if (t.dataset.slot) {
    const slot = (state.context?.slots || []).find(s => s.id === t.dataset.slot);
    if (slot) { await loadSeries(slot.series || []); state.focus = slotFocus(slot); state.route = slot.theme || 'market'; state.subtab = 'chart'; state.themeEvents = (await themeMessages(state.route)).filter(m => m.event_time || m.created_at); render(); updateSideContext(); $('#center').scrollTo({ top: 0 }); }
    return;
  }
  if (t.dataset.range) { state.range = t.dataset.range; render(); return; }
  if (t.hasAttribute('data-compare')) { state.compare = !state.compare; render(); return; }
  if (t.dataset.subtab) { state.subtab = t.dataset.subtab; render(); return; }
  if (t.dataset.view) { state.view = t.dataset.view; await loadMessages(); render(); return; }
  if (t.dataset.msgToggle) { const card = t.closest('.msg'); card.classList.toggle('expanded'); t.textContent = card.classList.contains('expanded') ? '收起' : '展开'; return; }
  if (t.dataset.msgRead) { await request('message.mark', { input: { logical_id: t.dataset.msgRead, action: 'read' } }).catch(() => {}); await loadContext(); await loadMessages(); render(); renderRail(); return; }
  if (t.dataset.msgHandle) {
    const act = t.dataset.act;
    if (act === 'snooze') { const until = new Date(Date.now() + 3 * 86400000).toISOString().slice(0, 10); await request('message.mark', { input: { logical_id: t.dataset.msgHandle, action: 'snooze', snooze_until: until } }).catch(() => {}); }
    else await request('message.mark', { input: { logical_id: t.dataset.msgHandle, action: 'handle' } }).catch(() => {});
    await loadContext(); await loadMessages(); render(); renderRail(); return;
  }
  if (t.dataset.msgNote) { const m = state.messages.find(x => x.logical_id === t.dataset.msgNote); if (m) { $('#quick-text').value = `对「${m.title}」（${m.author || ''}）我的看法 / 应对：\n`; $('#quick-text').focus(); } return; }
  if (t.dataset.sym) { state.focus = { type: 'series', id: t.dataset.sym, series: [t.dataset.sym] }; await loadSeries([t.dataset.sym]); state.route = 'market'; state.subtab = 'chart'; state.themeEvents = []; render(); updateSideContext(); return; }
  if (t.dataset.tl) { const ev = (state.themeEvents || []).find(x => x.logical_id === t.dataset.tl); if (ev) selectEvent(ev, state.focus?.series ? state.focus : focusFor(state.route)); return; }
  if (t.dataset.note) { state.noteSel = t.dataset.note; await loadNotes(); render(); return; }
  if (t.dataset.noteDone) { await request('notes.update', { input: { note_id: t.dataset.noteDone, status: 'done' } }).catch(() => {}); await loadNotes(); await loadContext(); render(); renderRail(); return; }
  if (t.dataset.noteArchive) { await request('notes.update', { input: { note_id: t.dataset.noteArchive, status: 'archived' } }).catch(() => {}); await loadNotes(); render(); return; }
  if (t.dataset.noteOutcome) { const n = state.notes.find(x => x.id === t.dataset.noteOutcome); const outcome = prompt('复盘结果（只写结果，不改原假设）：', n?.outcome || ''); if (outcome != null) { await request('notes.update', { input: { note_id: t.dataset.noteOutcome, outcome } }).catch(() => {}); await loadNotes(); render(); } return; }
});
$('#center').addEventListener('keydown', e => {
  if (e.key === 'Escape' && state.focus) { state.focus = null; render(); updateSideContext(); }
  if (e.key === 'Enter' && e.target.matches('.tl-row,[data-note]')) { e.target.click(); }
});
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && document.activeElement === document.body && !state.focus && state.route !== 'today') navigate('today');
});
$('#rail').addEventListener('click', e => { const b = e.target.closest('[data-route]'); if (b) navigate(b.dataset.route); });
let resizeTimer;
window.addEventListener('resize', () => { clearTimeout(resizeTimer); resizeTimer = setTimeout(() => { if (['market', 'metals', 'semis'].includes(state.route)) render(); }, 200); });
function updateMotion() { document.body.classList.toggle('paused', state.motionPaused || motionQuery.matches); const b = $('#motion'); b.textContent = state.motionPaused || motionQuery.matches ? '动画已停止' : '停止动画'; b.setAttribute('aria-pressed', String(state.motionPaused || motionQuery.matches)); }
$('#motion').addEventListener('click', () => { state.motionPaused = !state.motionPaused; try { localStorage.setItem('desk-motion', state.motionPaused ? 'paused' : 'running'); } catch (_) {} updateMotion(); });
motionQuery.addEventListener('change', updateMotion);
$('#refresh').addEventListener('click', async () => {
  if (state.busy) return;
  state.busy = true; const b = $('#refresh'); b.disabled = true; b.textContent = '正在获取…';
  try {
    state.snapshot = await request('refresh');
    state.series = {};
    await loadContext();
    if (state.context) await loadSeries((state.focus?.series) || focusFor(state.route)?.series || []);
    render(); updateSideContext();
  } catch (e) { alert('刷新失败：' + e.message + '。原有数据保留。'); }
  finally { state.busy = false; b.disabled = false; b.textContent = '刷新数据'; }
});
function updateTimestamps() {
  const dates = Object.values(state.series).map(s => s?.latest_date).filter(Boolean).sort();
  const cutoff = state.context?.data_cutoff || dates.at(-1);
  $('#data-time').textContent = cutoff ? fmtDate(cutoff) : '尚未接入';
  $('#refresh-time').textContent = state.snapshot?.fetchedAt ? state.snapshot.fetchedAt.slice(0, 16).replace('T', ' ') : '无记录';
}

/* ---------------- 启动 ---------------- */
(async function init() {
  updateMotion();
  initSide();
  try {
    await Promise.all([loadCatalog(), loadContext().catch(e => { throw e; })]);
    await loadSnapshot().catch(() => {});
    await loadMessages().catch(() => {});
    const slotKeys = [...new Set((state.context?.slots || []).flatMap(s => s.series || []))];
    await loadSeries(slotKeys).catch(() => {});
    render(); updateTimestamps(); updateSideContext();
    updateSideRefs().catch(() => {});
    setInterval(() => { if (!document.hidden) { loadContext().then(() => { renderRail(); updateTimestamps(); }).catch(() => {}); } }, 5 * 60 * 1000);
  } catch (e) {
    $('#center').innerHTML = `<div class="empty"><strong>工作台暂时无法载入</strong>${esc(e.message)}<br>目录与已缓存数据仍可重试；没有用模拟数据替代。</div>`;
  }
})();
