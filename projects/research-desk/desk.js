'use strict';
const $ = selector => document.querySelector(selector);
const escapeHTML = value => String(value ?? '').replace(/[&<>"']/g, character => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[character]));
const number = value => typeof value === 'number' && Number.isFinite(value);
const format = value => number(value) ? value.toLocaleString('zh-CN', {maximumFractionDigits:2}) : '—';
const percent = value => number(value) ? `${value > 0 ? '+' : ''}${format(value)}%` : '—';
const state = {catalog:null, snapshot:{quotes:[]}, tab:'map', selected:null, group:'', search:'', core:false, direction:'down', dimension:'2d', rotation:0, busy:false, priceThreshold:2};
const motionQuery = matchMedia('(prefers-reduced-motion: reduce)');
let paused = motionQuery.matches;
try { paused = paused || localStorage.getItem('desk-motion') === 'paused'; } catch (_) {}
let channel;
const requests = new Map();
const labels = {available:'日线可用', stale:'陈旧 / 待复核', missing:'未接入'};
const metricSources = {
  A101:{symbols:['SPY','QQQ','IWM'],fields:['return5d','return21d','return63d'],note:'部分代理：实际复权方式逐项标在下方；不等同于原指数总回报。'},
  A102:{symbols:['SPY','QQQ','IWM'],fields:['ma50Distance'],note:'仅50日均线距离；均线方向尚未接入。'},
  A301:{symbols:['SPY','QQQ','IWM'],fields:['drawdown63'],note:'仅63个交易日收盘高点回撤；不代表完整历史回撤。'},
  E101:{symbols:['XLK','XLF','XLE','XLI','XLV','XLY','XLP','XLU','XLC','XLB','XLRE'],fields:['return21d'],note:'板块ETF回报代理；相对基准表现及内部扩散需另验。'},
  G101:{symbols:['^VIX','^VIX3M'],fields:['close'],note:'仅VIX与VIX3M两点，不代表完整波动率期限结构。'},
  G102:{symbols:['SPY','QQQ','IWM'],fields:['volatility20'],note:'仅20交易日日收盘实现波动率；与目录窗口差异需核对。'}
};
const fieldLabels = {close:'收盘',change1d:'1日',return5d:'5日',return21d:'21日',return63d:'63日',ma50Distance:'距MA50',drawdown63:'63日回撤',volatility20:'20日年化波动'};
// These are questions to investigate, never estimated causal edges.
const hypothesisEdges = [
 ['B101','B201'],['B101','B301'],['B101','C201'],['B301','F203'],['B301','D302'],['B301','A101'],
 ['C101','F301'],['C101','A101'],['C101','G101'],['D101','D103'],['D101','B102'],['D201','B302'],['D201','B102'],
 ['D302','E201'],['D302','E202'],['E201','F102'],['E202','F101'],['E203','E201'],['F101','F102'],
 ['F102','F103'],['F103','F301'],['F202','F203'],['F203','A101'],['E101','A101'],['G101','G103'],['G101','G303']
];
function metricNotice(id) {
 const map=metricSources[id];
 const qs=map ? state.snapshot.quotes.filter(q=>map.symbols.includes(q.symbol)&&quoteStatus(q)==='available') : [];
 const moved=qs.filter(q=>number(q.change1d)&&Math.abs(q.change1d)>=state.priceThreshold);
 return {partial:qs.length>0,attention:moved.length>0,text:moved.length ? `相关行情代理日变动达到 ${state.priceThreshold}%：${moved.map(q=>q.symbol+' '+percent(q.change1d)).join(' / ')}；仅提示查阅，不是风险信号。` : qs.length ? '部分行情代理可用；指标定义尚未完整覆盖' : '尚无完整观测'};
}
function quoteStatus(quote) {
  if (!quote || !number(quote.close) || !quote.asOf) return 'missing';
  const timestamp = Date.parse(quote.observedAt || quote.asOf);
  if (!Number.isFinite(timestamp) || Date.now() - timestamp > 5 * 86400000 || quote.status === 'stale') return 'stale';
  return quote.status === 'available' ? 'available' : 'missing';
}
function setStatus(message) { $('#status').textContent = message; }
function updateMotion() {
  document.body.classList.toggle('paused', paused || motionQuery.matches);
  $('#motion').textContent = paused || motionQuery.matches ? '动画已停止' : '停止动画';
  $('#motion').setAttribute('aria-pressed', String(paused || motionQuery.matches));
}
$('#motion').addEventListener('click', () => { paused = !paused; try { localStorage.setItem('desk-motion', paused ? 'paused' : 'running'); } catch (_) {} updateMotion(); });
motionQuery.addEventListener('change', updateMotion);
updateMotion();
function requestSnapshot(action) {
  return new Promise((resolve, reject) => {
    if (!channel) { reject(new Error('当前环境无法连接数据后台；目录仍可浏览。')); return; }
    const id = crypto.randomUUID();
    const controller = new AbortController();
    let retry;
    const finish = (error, snapshot) => {
      clearTimeout(timeout); clearInterval(retry); controller.abort(); requests.delete(id);
      if (error) reject(error); else resolve(snapshot);
    };
    const timeout = setTimeout(() => finish(new Error(action === 'refresh' ? '刷新超过100秒，已停止等待。可稍后重试，原有数据保留。' : '后台15秒内未回应。可点击刷新重试，目录仍可浏览。')), action === 'refresh' ? 100000 : 15000);
    requests.set(id, finish);
    fetch('/wake', {signal:controller.signal}).then(response => {
      if (!response.ok) throw new Error(`唤醒后台失败 HTTP ${response.status}，请稍后重试。`);
      if (!requests.has(id)) return;
      const send = () => channel.postMessage({type:'desk-request', id, action});
      send(); retry = setInterval(send, 700);
    }).catch(error => { if (requests.has(id)) finish(error); });
  });
}
try {
  channel = new BroadcastChannel('murphy-research-desk-v1');
  channel.onmessage = ({data}) => {
    if (data?.type !== 'desk-response' || !requests.has(data.id)) return;
    const finish = requests.get(data.id);
    if (!data.ok || !Array.isArray(data.snapshot?.quotes)) finish(new Error(data.error || '快照格式无效，请稍后重试。'));
    else finish(null, data.snapshot);
  };
} catch (_) {}
async function refresh(action = 'refresh') {
  if (state.busy) return;
  state.busy = true; $('#refresh').disabled = true; $('#refresh').textContent = '正在获取…';
  setStatus(action === 'refresh' ? '正在获取已完成日线，最多等待100秒；你可以继续浏览研究目录。' : '正在连接已有日线快照…');
  try {
    state.snapshot = await requestSnapshot(action);
    const errors = state.snapshot.errors?.length || 0;
    setStatus(`${errors ? `${errors} 个来源请求未成功，保留可用旧值；可稍后重试。` : '快照已读取。'} ${state.snapshot.note || '公开日线，不是实时盘口。'} ${state.snapshot.storageWarning || ''}`);
    renderSummary(); render();
  } catch (error) { setStatus(error.message); }
  finally { state.busy = false; $('#refresh').disabled = false; $('#refresh').textContent = '刷新日线'; }
}
$('#refresh').addEventListener('click', () => refresh());
function renderSummary() {
  if (!state.catalog) return;
  const quotes = state.snapshot.quotes;
  const available = quotes.filter(quote => quoteStatus(quote) === 'available').length;
  const stale = quotes.filter(quote => quoteStatus(quote) === 'stale').length;
  const cards = [
    [state.catalog.metrics.length, '研究指标', `${state.catalog.metrics.filter(metric => metric.core).length} 项核心 · 8 个研究分组`],
    [available, '可用行情代理', `${stale} 项陈旧 · 可用性不代表市场安全`],
    [Math.max(0,21 - available - stale), '行情代理缺失', '21 个计划行情代理 · 不等于71项指标覆盖'],
    [state.catalog.history?.items?.length || 0, '历史字段', `${state.catalog.history?.asOf || '无历史时点'} · 独立快照`]
  ];
  $('#summary').innerHTML = cards.map(([value,label,note]) => `<article class="stat"><strong>${value}</strong><span>${label}</span><p>${escapeHTML(note)}</p></article>`).join('');
  const dates = quotes.map(quote => quote.asOf).filter(Boolean).sort();
  $('#data-time').textContent = dates.length ? `数据时点 · ${dates[0]}${dates.at(-1) !== dates[0] ? ' 至 ' + dates.at(-1) : ''}` : '数据时点 · 尚未接入';
  $('#refresh-time').textContent = `最近刷新 · ${state.snapshot.fetchedAt ? new Date(state.snapshot.fetchedAt).toLocaleString('zh-CN') : '尚无记录'}`;
}
function switchTab(tab) {
  state.tab = tab;
  document.querySelectorAll('[data-tab]').forEach(button => { const selected = button.dataset.tab === tab; button.setAttribute('aria-selected', String(selected)); button.tabIndex = selected ? 0 : -1; });
  $('#workspace').setAttribute('aria-labelledby', `tab-${tab}`); render();
}
document.querySelector('.tabs').addEventListener('click', event => { const button = event.target.closest('[data-tab]'); if (button) switchTab(button.dataset.tab); });
document.querySelector('.tabs').addEventListener('keydown', event => {
  if (!['ArrowLeft','ArrowRight','Home','End'].includes(event.key)) return;
  const tabs = [...document.querySelectorAll('[data-tab]')];
  let index = tabs.indexOf(document.activeElement);
  if (index < 0) return;
  index = event.key === 'Home' ? 0 : event.key === 'End' ? tabs.length - 1 : (index + (event.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length;
  event.preventDefault(); switchTab(tabs[index].dataset.tab); tabs[index].focus();
});
function render() {
  if (!state.catalog) return;
  const active=document.activeElement;
  const focusKey=active && $('#workspace').contains(active) ? ['data-direction','data-dimension','data-group','data-rotate','id'].find(key=>active.hasAttribute(key)) : null;
  const focusValue=focusKey ? active.getAttribute(focusKey) : null;
  const views = {map:renderMap, metals:renderMetals, rules:renderRules, library:renderLibrary, history:renderHistory};
  $('#workspace').innerHTML = views[state.tab]();
  if (state.tab === 'map') applyRotation();
  if(focusKey)$('#workspace').querySelector(`[${focusKey}="${CSS.escape(focusValue)}"]`)?.focus({preventScroll:true});
}
function groupsHTML() {
  return `<aside class="panel"><div class="panel-head"><p class="eyebrow">RESEARCH LAYERS</p><h3>从哪里开始</h3></div><div class="group-list">${state.catalog.groups.map(group => `<button data-group="${escapeHTML(group.id)}" class="${state.group === group.id ? 'active' : ''}" aria-pressed="${state.group === group.id}"><span class="group-code">${escapeHTML(group.id)}</span><span class="group-name">${escapeHTML(group.name)}</span><span class="group-count">${state.catalog.metrics.filter(metric => metric.groupId === group.id).length}</span></button>`).join('')}</div><p class="note">分组与连线用于组织研究。<br>连线没有因果方向或强度含义。<br>节点灰色表示尚无完整观测。</p></aside>`;
}
function graphHTML() {
  const center = {x:370,y:285};
  let base = '<circle class="orbit" cx="370" cy="285" r="100"/><ellipse class="orbit" cx="370" cy="285" rx="300" ry="235"/>';
  let nodes = '', titles = '';
  state.catalog.groups.forEach((group, groupIndex) => {
    const angle = groupIndex * Math.PI / 4 - Math.PI / 2;
    const groupX = center.x + Math.cos(angle) * 240, groupY = center.y + Math.sin(angle) * 190;
    base += `<path class="connector" d="M370 285 L${groupX} ${groupY}"/>`;
    titles += `<text class="group-label" x="${groupX}" y="${groupY - 45}" text-anchor="middle">${escapeHTML(group.id + ' · ' + group.name.slice(0,8))}</text>`;
    const metrics = state.catalog.metrics.filter(metric => metric.groupId === group.id);
    metrics.forEach((metric,index) => {
      const notice=metricNotice(metric.id);
      const localAngle = index / metrics.length * Math.PI * 2;
      const nodeX = groupX + Math.cos(localAngle) * 60, nodeY = groupY + Math.sin(localAngle) * 31;
      base += `<path class="connector" d="M${groupX} ${groupY} L${nodeX} ${nodeY}"/>`;
      nodes += `<g class="node ${notice.partial ? 'partial' : ''} ${notice.attention ? 'attention' : ''} ${state.selected === metric.id ? 'selected' : ''}" role="button" tabindex="0" aria-label="${escapeHTML(metric.id + ' ' + metric.name)}" aria-pressed="${state.selected === metric.id}" data-metric="${escapeHTML(metric.id)}"><title>${escapeHTML(metric.name)} · ${escapeHTML(notice.text)}</title><circle cx="${nodeX}" cy="${nodeY}" r="${metric.core ? 7 : 5}"/><text x="${nodeX}" y="${nodeY + 18}" text-anchor="middle">${escapeHTML(metric.id)}</text></g>`;
    });
  });
  titles += '<circle class="hub" cx="370" cy="285" r="77"/><text class="hub-title" x="370" y="280" text-anchor="middle">研究地图</text><text class="hub-subtitle" x="370" y="303" text-anchor="middle">71 指标 · 证据优先</text>';
  return `<div class="map-stage" id="map-stage"><svg class="base-layer" viewBox="0 0 740 570" aria-hidden="true">${base}</svg><svg class="label-layer" viewBox="0 0 740 570" aria-hidden="true">${titles}</svg><svg class="metric-layer" viewBox="0 0 740 570" aria-label="71项研究指标节点">${nodes}</svg></div>`;
}
function renderMap() {
  return `<div class="research-grid">${groupsHTML()}<section class="panel"><div class="toolbar"><div class="segmented" aria-label="研究方向"><button data-direction="down" aria-pressed="${state.direction === 'down'}">从事件往下查</button><button data-direction="up" aria-pressed="${state.direction === 'up'}">从线索往上追</button></div><div class="segmented"><button data-dimension="2d" aria-pressed="${state.dimension === '2d'}">2D 地图</button><button data-dimension="3d" aria-pressed="${state.dimension === '3d'}">3D 探索</button></div><label class="threshold">相关代理日变化提示 ≥ <input id="price-threshold" type="number" min="0.1" max="20" step="0.1" value="${state.priceThreshold}" aria-label="行情代理日变化提示阈值百分比"> %</label><div class="rotation" ${state.dimension !== '3d' ? 'hidden' : ''}><button data-rotate="-15" aria-label="向左旋转15度">↶ 左转</button><button data-rotate="15" aria-label="向右旋转15度">右转 ↷</button><button data-rotate="reset">复位</button><small>空间层级仅为视觉组织</small></div></div><div class="map-viewport" aria-label="研究地图，可横向滚动">${graphHTML()}</div><p class="map-caption">灰：无完整观测 · 青：部分代理可用 · 呼吸点：相关代理日变化超过查阅阈值（非已验证风险信号）。大节点为核心指标；小屏可滚动或用指标库选择。</p></section><section class="panel detail" id="detail">${detailHTML()}</section></div>`;
}
function detailHTML() {
  const metric = state.catalog.metrics.find(item => item.id === state.selected);
  if (!metric) return '<h2>选择一条研究线索</h2><p class="muted">点击地图节点或分组，查看定义、证据边界与下一步验证。</p>';
  const mapping = metricSources[metric.id];
  const observations = mapping ? state.snapshot.quotes.filter(quote => mapping.symbols.includes(quote.symbol)) : [];
  const observationHTML = observations.map(quote => `<p class="note">${escapeHTML(quote.symbol)} · ${labels[quoteStatus(quote)]} · ${escapeHTML(quote.asOf || '无时点')}<br>${mapping.fields.map(field => `${fieldLabels[field]} ${field === 'close' ? format(quote[field]) : percent(quote[field])}`).join(' / ')}<br>${escapeHTML(quote.provider || 'Yahoo')} · ${escapeHTML(quote.basis || '口径未提供')}<br>${escapeHTML(quote.freshnessNote || '')}</p>`).join('');
  const links=hypothesisEdges.filter(([from,to])=>state.direction==='down'?to===metric.id:from===metric.id).map(([from,to])=>state.direction==='down'?from:to);
  const candidates=links.length ? links.map(id=>state.catalog.metrics.find(m=>m.id===id)).filter(Boolean) : state.catalog.metrics.filter(item=>item.groupId===metric.groupId && item.id!==metric.id).slice(0,3);
  const notice=metricNotice(metric.id);
  const fields = [['观察含义',metric.meaning],['定义与口径',metric.definition],['频率 / 单位',`${metric.frequency} / ${metric.unit}`],['数据可用时点',metric.availability],['证据状态',metric.evidenceStatus],['解释边界',metric.boundary]];
  return `<p class="eyebrow">${escapeHTML(metric.id)} / ${escapeHTML(metric.subgroup)}</p><h2>${escapeHTML(metric.name)}</h2><span class="pill">${metric.core ? '核心指标' : '补充指标'}</span><span class="pill review">${notice.attention ? '相关行情波动待复核' : notice.partial ? '部分代理可用' : '当前观测缺失'}</span><span class="pill">因果权重：不可识别</span><dl>${fields.map(([label,value]) => `<dt>${label}</dt><dd>${escapeHTML(value || '尚未提供')}</dd>`).join('')}</dl><h3>当前观测</h3>${notice.attention ? `<p class="boundary">${escapeHTML(notice.text)}</p>` : ''}${observationHTML || '<p class="note">暂无可映射的当前观测。缺失不代表正常；历史卡独立保存。</p>'}${mapping ? `<p class="note">${escapeHTML(mapping.note)}</p>` : ''}<div class="path"><h3>${state.direction === 'down' ? '下一步：为结果寻找候选解释' : '下一步：追查线索可能影响什么'}</h3><p class="muted">${state.direction === 'down' ? '从已发生的结果逆向核对驱动假设；每条路径都需要同一时钟的证据。' : '从当前线索沿待验证机制向前追踪；还没有发生的结果不能当作预测结论。'}</p>${candidates.map(item => `<button data-metric="${escapeHTML(item.id)}">${escapeHTML(item.id + ' · ' + item.name)} →</button>`).join('')}<p class="note">${links.length ? '跨指标机制假设，尚未识别因果或贡献权重' : '暂无预设跨组路径，以下为同组联看候选'}。下一验证：来源、同一时钟、替代解释、样本外证据。</p></div><button data-copy="true">复制讨论问题</button>`;
}
function quoteCard(symbol, label) {
  const quote = state.snapshot.quotes.find(item => item.symbol === symbol);
  const status = quoteStatus(quote);
  const series = (quote?.series || []).filter(point => number(point.value));
  let chart = '<div class="empty">暂无可绘制日线<br><small>公开来源可能限流；可稍后刷新</small></div>';
  if (series.length > 1) {
    const minimum = Math.min(...series.map(point => point.value)), maximum = Math.max(...series.map(point => point.value));
    const points = series.map((point,index) => `${index / (series.length - 1) * 300},${90 - (point.value - minimum) / (maximum - minimum || 1) * 80}`).join(' ');
    chart = `<svg class="sparkline" viewBox="0 0 300 100" role="img" aria-label="${escapeHTML(symbol)}日收盘走势，${escapeHTML(series[0].date)}至${escapeHTML(series.at(-1).date)}"><polyline points="${points}"/></svg><p class="chart-period">${escapeHTML(series[0].date)} → ${escapeHTML(series.at(-1).date)} · ${series.length} 个观测</p>`;
  }
  const sourceURL = quote?.sourceUrl && /^https:\/\//.test(quote.sourceUrl) ? `<a href="${escapeHTML(quote.sourceUrl)}" >核对原始来源 ↗</a>` : '';
  return `<article class="panel quote-card"><span class="symbol">${symbol}</span><h2>${label}</h2><span class="pill">${labels[status]}</span><p class="price">${format(quote?.close)}</p><small>${escapeHTML(quote?.currency || '币种待接入')} · ${escapeHTML(quote?.asOf || '无数据时点')} · 日收盘</small>${chart}<div class="quote-grid">${['change1d','return5d','return21d'].map(field => `<div><small>${fieldLabels[field]}回报</small>${percent(quote?.[field])}</div>`).join('')}</div><p class="note">${escapeHTML(quote?.basis || '回报口径尚未提供，未推定复权方式。')}<br>${escapeHTML(quote?.error || '')} ${sourceURL}</p></article>`;
}
function renderMetals() {
  return `<div class="section-heading"><div><p class="eyebrow">CROSS-ASSET OBSERVATORY</p><h2>黄金 · 白银 · 铜</h2><p>从价格分化提出问题，再回到实际利率、美元、需求与库存验证。</p></div><span class="pill">新建专题视图 · 旧专题未定位</span></div><div class="cards">${quoteCard('GLD','黄金')}${quoteCard('SLV','白银')}${quoteCard('CPER','铜')}</div><div class="boundary">GLD / SLV 是ETF价格代理，CPER 是铜期货基金代理，涉及换月。基金价格不能直接计算现货金银比或铜金比。三者同涨同跌也不能证明同一原因。</div><div class="cards">${[['实际利率与美元','B301','利率变化是否与金属价格同一时钟？美元、风险偏好能否提供替代解释？'],['通胀与需求','D302','价格变化是否有库存、期限结构与需求数据支持？'],['行业与供给','E203','供给约束、资本周期与换月效应能否解释分化？']].map(([title,id,question]) => `<article class="panel quote-card"><h3>${title}</h3><p class="note">${question}</p><button data-open-metric="${id}">查看研究指标 →</button></article>`).join('')}</div>`;
}
function renderRules() {
  const rule=state.catalog.rules?.[0];
  return `<div class="section-heading"><div><p class="eyebrow">INDEPENDENT RESEARCH RULE</p><h2>JNK–SPY 经验规则</h2><p>保留各版本的定义与验证边界，避免把记忆中的阈值混成一个触发器。</p></div><span class="pill review">当前触发计算未启用</span></div><div class="boundary">${escapeHTML(rule?.note || '规则目录尚未提供')}<br>${escapeHTML(rule?.status || '')}</div><div class="cards">${(rule?.versions || []).map(version=>`<article class="panel rule-card"><h3>${escapeHTML(version.name)}</h3><dl><dt>观察条件</dt><dd>${escapeHTML(version.threshold)}</dd><dt>验证状态</dt><dd>${escapeHTML(version.status)}</dd></dl><details><summary>原始文档位置</summary><p class="source-path">${escapeHTML(version.sourcePath)}</p></details></article>`).join('')}</div><div class="boundary">先核对版本、窗口、收益口径、阈值单位与可用时点。经验规则未经样本外验证不能转化为买卖指令；下方日线也不能替代规则需要的同步日内数据。</div><div class="rules-grid">${quoteCard('JNK','高收益债代理')}${quoteCard('SPY','美股大盘代理')}</div>`;
}
function filteredMetrics() {
  return state.catalog.metrics.filter(metric => (!state.group || metric.groupId === state.group) && (!state.core || metric.core) && `${metric.id} ${metric.name} ${metric.group} ${metric.subgroup} ${metric.fields}`.toLowerCase().includes(state.search.toLowerCase()));
}
function metricListHTML() {
  const metrics = filteredMetrics();
  return `<p class="note">显示 ${metrics.length} / ${state.catalog.metrics.length} 项 · 点击查看证据</p><div class="metric-list">${metrics.map(metric => `<button class="metric-card ${state.selected === metric.id ? 'active' : ''}" data-metric="${escapeHTML(metric.id)}"><span class="eyebrow">${escapeHTML(metric.id)} ${metric.core ? ' / 核心' : ''}</span><h3>${escapeHTML(metric.name)}</h3><p>${escapeHTML(metric.group + ' / ' + metric.subgroup)}</p></button>`).join('') || '<p class="empty">没有匹配指标，请调整关键词或筛选。</p>'}</div>`;
}
function renderLibrary() {
  return `<div class="section-heading"><div><p class="eyebrow">THE RESEARCH CATALOG</p><h2>指标库</h2><p>定义、可用时点与解释边界，比一个颜色更重要。</p></div></div><div class="filters"><input id="search" type="search" placeholder="搜索指标、编号、字段…" aria-label="搜索指标" value="${escapeHTML(state.search)}"><select id="group-filter" aria-label="按研究分组筛选"><option value="">全部分组</option>${state.catalog.groups.map(group => `<option value="${escapeHTML(group.id)}" ${state.group === group.id ? 'selected' : ''}>${escapeHTML(group.id + ' · ' + group.name)}</option>`).join('')}</select><label><input id="core-filter" type="checkbox" ${state.core ? 'checked' : ''}>只看核心</label></div><div class="library-grid"><section id="metric-list">${metricListHTML()}</section><section class="panel detail" id="detail">${detailHTML()}</section></div>`;
}
function renderHistory() {
  const history = state.catalog.history || {};
  return `<div class="section-heading"><div><p class="eyebrow">ARCHIVED OBSERVATIONS</p><h2>历史监测卡 · ${escapeHTML(history.asOf || '无时点')}</h2><p>${escapeHTML(history.status || '历史研究快照，非最新行情，非当前判断')}</p></div><span class="pill">${history.items?.length || 0} 个独立字段</span></div><div class="boundary">此处为固定历史快照，不随“刷新日线”更新。宏观发布时钟未经过历史验证；当时的观测状态不构成当前信号。展示值使用目录 display_value 与 display_unit，不重复乘100。</div><div class="cards history-grid">${(history.items || []).map(item => `<article class="panel history-card"><h3>${escapeHTML(item.field)}</h3><strong>${escapeHTML(item.display_value)} <small>${escapeHTML(item.display_unit)}</small></strong><p>来源观测日 ${escapeHTML(item.source_observation_date || '未知')}</p><p>快照交易日 ${escapeHTML(item.asof_session || history.asOf)}</p><details><summary>口径与时钟</summary><p>${escapeHTML(item.publication_clock)}</p><p>${escapeHTML(item.status)}</p></details></article>`).join('')}</div>`;
}
function applyRotation() {
  const stage = $('#map-stage');
  if (!stage) return;
  stage.classList.toggle('is-3d', state.dimension === '3d');
  stage.style.transform = state.dimension === '3d' ? `rotateX(28deg) rotateZ(${state.rotation - 8}deg)` : '';
}
function selectMetric(id) {
  state.selected = id;
  if ($('#detail')) $('#detail').innerHTML = detailHTML();
  document.querySelectorAll('[data-metric]').forEach(node => { node.classList.toggle('selected',node.dataset.metric === id); if (node.matches('.node')) node.setAttribute('aria-pressed',String(node.dataset.metric === id)); });
}
async function copyQuestion() {
  const metric = state.catalog.metrics.find(item => item.id === state.selected);
  if (!metric) return;
  const dates = [...new Set(state.snapshot.quotes.map(quote => quote.asOf).filter(Boolean))].sort();
  const question = `请围绕 ${metric.id}「${metric.name}」讨论。\n研究方向：${state.direction === 'down' ? '从事件往下查' : '从线索往上追'}。\n数据时点：${dates.join(' / ') || '当前观测缺失'}；历史卡：${state.catalog.history?.asOf || '无'}（独立历史快照）。\n定义：${metric.definition}\n证据：${metric.evidenceStatus}\n边界：${metric.boundary}\n请先区分已知事实、假设与缺失数据，再列可能传导路径；关联不等于因果，权重不可识别。\n替代解释：共同驱动、反向关系、时钟错配、分红复权与样本偏差。\n下一验证：需要什么来源、什么观测、何时可用，怎样证伪？不生成买卖指令。`;
  try { await navigator.clipboard.writeText(question); setStatus('讨论问题已复制；由你决定在哪里粘贴。'); }
  catch (_) { $('#copy-text').value = question; $('#copy-dialog').showModal(); $('#copy-text').focus(); $('#copy-text').select(); }
}
$('#close-copy').addEventListener('click', () => $('#copy-dialog').close());
$('#workspace').addEventListener('click', event => {
  const target = event.target.closest('button,[data-metric]');
  if (!target) return;
  if (target.dataset.metric) selectMetric(target.dataset.metric);
  else if (target.dataset.openMetric) { state.selected = target.dataset.openMetric; state.group = state.catalog.metrics.find(metric => metric.id === state.selected)?.groupId || ''; switchTab('map'); }
  else if (target.dataset.group) { state.group = target.dataset.group; state.selected = state.catalog.metrics.find(metric => metric.groupId === state.group)?.id; render(); }
  else if (target.dataset.direction) { state.direction = target.dataset.direction; render(); }
  else if (target.dataset.dimension) { state.dimension = target.dataset.dimension; render(); }
  else if (target.dataset.rotate) { state.rotation = target.dataset.rotate === 'reset' ? 0 : state.rotation + Number(target.dataset.rotate); applyRotation(); }
  else if (target.dataset.copy) copyQuestion();
});
$('#workspace').addEventListener('keydown', event => {
  if (event.target.matches('.node') && ['Enter',' '].includes(event.key)) { event.preventDefault(); selectMetric(event.target.dataset.metric); }
});
$('#workspace').addEventListener('input', event => {
  if (event.target.id === 'search') { state.search = event.target.value; $('#metric-list').innerHTML = metricListHTML(); }
});
$('#workspace').addEventListener('change', event => {
  if (event.target.id === 'group-filter') state.group = event.target.value;
  else if (event.target.id === 'price-threshold') { const n=Number(event.target.value); if(Number.isFinite(n))state.priceThreshold=Math.min(20,Math.max(0.1,n));render();return; }
  else if (event.target.id === 'core-filter') state.core = event.target.checked;
  else return;
  $('#metric-list').innerHTML = metricListHTML();
});
const autoRefresh = setInterval(() => { if (!document.hidden && state.catalog) refresh(); }, 15 * 60 * 1000);
window.addEventListener('pagehide', () => { clearInterval(autoRefresh); for (const finish of [...requests.values()]) finish(new Error('页面已关闭，已停止等待。')); channel?.close(); });
async function initialize() {
  try {
    const response = await fetch('./data/catalog.json');
    if (!response.ok) throw new Error(`目录读取失败 HTTP ${response.status}`);
    const catalog = await response.json();
    if (!Array.isArray(catalog.metrics) || !Array.isArray(catalog.groups)) throw new Error('研究目录格式不完整');
    state.catalog = catalog; state.selected = catalog.metrics[0]?.id || null;
    renderSummary(); render(); refresh('snapshot');
  } catch (error) { setStatus(`${error.message}。请重新打开页面或检查随包目录。`); $('#workspace').innerHTML = '<div class="panel empty"><strong>研究目录暂时无法打开</strong>请检查 data/catalog.json 后重新打开。没有用模拟数据替代。</div>'; }
}
initialize();
