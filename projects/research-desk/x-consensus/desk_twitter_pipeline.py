#!/usr/bin/env python3
"""Desk 推特周报管线（调度 E 组）：X 关注圈 → 共识差 → Research Desk Board。

prepare：读取近七天已完成（DONE.json）的 B 组采集批次，按 ID 去重、过滤转推与
账号错配，输出预览 JSON（window / data_cutoff / coverage / posts）。
build：预览 + AI 萕取 JSON → 严格校验（post_id 存在、立场合法、反证非空、
supported 必须有完整可比数值、证据日期不得来自未来、同主题同作者只计一次），
生成既有 Board 公开 schema 的 {"batch":{...}} 包（kind=twitter，
batch_id 稳定为 x-consensus-<上海日期>）。

边界：只读原始采集目录，不做网络请求；同日重跑覆盖自己的产物，批次 id 不变。
覆盖（coverage）只表示采集成功，与"参与讨论人数"在输出里分开表达。
"""
import argparse
import datetime
import json
import os
import pathlib
import re
import sys
import tempfile

DEFAULT_ROOT = pathlib.Path.home() / '.agent-reach' / 'x_digest_261105' / 'weekly'
TZ_SH = datetime.timezone(datetime.timedelta(hours=8), name='Asia/Shanghai')
WINDOW_DAYS = 7
POSTS_PER_ACCOUNT_CAP = 200  # 与采集端 -n 一致，仅用于合理性检查
MAX_THEMES = 12
MAX_CLAIMS_SHOWN = 6
EVIDENCE_PER_THEME = 3

# Board 公开 schema 硬约束（镜像 desk-core.js validateBatch/validateItem）
RE_BATCH_ID = re.compile(r'^[A-Za-z0-9._:-]{4,128}$')
RE_LOGICAL_ID = re.compile(r'^[A-Za-z0-9._:-]{3,160}$')
RE_SYMBOL = re.compile(r'^[A-Z0-9.^-]{1,12}$')
RE_HTTPS = re.compile(r'^https://')
RE_THEME_ID = re.compile(r'^[a-z0-9][a-z0-9._-]{0,39}$')
STANCES = ('bull', 'bear', 'mixed', 'unknown')
TITLE_MAX = 300
BODY_MAX = 8000
NOTE_MAX = 500
# 自我收敛的展示上限（Board 上限之外的进一步瘦身，防单条消息过长）
SHOW_TITLE_MAX = 120
SHOW_BODY_THEME = 1600
SHOW_BODY_EVIDENCE = 600
SHOW_BODY_REPORT = 1200
SUMMARY_MAX = 500
METRIC_FIELDS = ('name', 'value', 'unit', 'period', 'baseline_value', 'baseline_period', 'basis', 'source_url', 'source_date')


def fail(errors):
    sys.stdout.write(json.dumps({'ok': False, 'errors': errors}, ensure_ascii=False) + '\n')
    sys.exit(1)


def ok(payload):
    sys.stdout.write(json.dumps({'ok': True, **payload}, ensure_ascii=False) + '\n')


def sh_date(dt):
    return dt.strftime('%Y%m%d')


def now_sh():
    return datetime.datetime.now(TZ_SH)


def iso_sh(dt):
    return dt.isoformat(timespec='seconds')


def parse_day_token(name):
    """目录名 → 规范 YYYYMMDD；兼容旧 YYMMDD（261108→20261108）。非法返回 None。"""
    raw = name.strip()
    if len(raw) == 6:
        raw = '20' + raw
    if not (len(raw) == 8 and raw.isdigit()):
        return None
    try:
        datetime.datetime.strptime(raw, '%Y%m%d')
    except ValueError:
        return None
    return raw


def day_range(end_day):
    """以 end_day（YYYYMMDD，上海日）为最后一格的 7 天窗口：返回 (start, end, days)。"""
    end = datetime.datetime.strptime(end_day, '%Y%m%d').replace(tzinfo=TZ_SH, hour=23, minute=59, second=59)
    start = end.replace(hour=0, minute=0, second=0) - datetime.timedelta(days=WINDOW_DAYS - 1)
    days = [(start + datetime.timedelta(days=i)).strftime('%Y%m%d') for i in range(WINDOW_DAYS)]
    return start, end, days


def parse_iso(text):
    if not isinstance(text, str) or not text:
        return None
    try:
        return datetime.datetime.fromisoformat(text.replace('Z', '+00:00'))
    except ValueError:
        return None


# ---------------------------- prepare ----------------------------

def load_batch_dirs(root, days_wanted):
    """返回 (batches, skipped)。batches: [{day, dir, manifest}]；skipped: 记录在窗但不完整的目录。"""
    if not root.is_dir():
        return [], [{'dir': str(root), 'reason': 'root_missing'}]
    wanted = set(days_wanted)
    batches, skipped = [], []
    for entry in sorted(root.iterdir()):
        day = parse_day_token(entry.name)
        if day is None or day not in wanted or not entry.is_dir():
            continue
        if not (entry / 'DONE.json').exists():
            skipped.append({'dir': entry.name, 'reason': 'no_done'})
            continue
        manifest_path = entry / 'manifest.json'
        if not manifest_path.exists():
            skipped.append({'dir': entry.name, 'reason': 'manifest_missing'})
            continue
        try:
            manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        except (OSError, json.JSONDecodeError) as e:
            skipped.append({'dir': entry.name, 'reason': 'manifest_unreadable', 'detail': str(e)[:120]})
            continue
        if not isinstance(manifest, dict):
            skipped.append({'dir': entry.name, 'reason': 'manifest_invalid'})
            continue
        if isinstance(manifest.get('accounts'), list):
            batches.append({'day': day, 'dir': entry, 'manifest': manifest, 'legacy': False})
        elif isinstance(manifest.get('expected_accounts'), list):
            # 上一代采集器：无逐账号状态，只有 expected_accounts + posts/*.json
            batches.append({'day': day, 'dir': entry, 'manifest': manifest, 'legacy': True})
        else:
            skipped.append({'dir': entry.name, 'reason': 'manifest_invalid'})
    batches.sort(key=lambda b: b['day'])
    return batches, skipped


def posts_from_file(path, handle, window_start, problems):
    """读取单账号原始文件 → (规范化帖子列表, 文件是否可用)。读取问题只记录，不中断。"""
    try:
        raw = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as e:
        problems.append({'handle': handle, 'error': 'read_failed', 'detail': str(e)[:120]})
        return [], False
    data = raw.get('data') if isinstance(raw, dict) else None
    if not isinstance(data, list):
        problems.append({'handle': handle, 'error': 'data_missing'})
        return [], False
    if len(data) > POSTS_PER_ACCOUNT_CAP:
        problems.append({'handle': handle, 'error': 'count_suspicious', 'detail': f'n={len(data)}'})
    out = []
    handle_lc = handle.lower()
    for p in data:
        if not isinstance(p, dict) or p.get('isRetweet'):
            continue
        author = p.get('author') or {}
        screen = author.get('screenName')
        pid = p.get('id')
        text = p.get('text')
        if not isinstance(screen, str) or not isinstance(pid, str) or not pid.isdigit():
            continue
        if screen.lower() != handle_lc:
            continue  # 账号错配（同文件内他人内容）
        if not isinstance(text, str) or not text.strip():
            continue
        when = parse_iso(p.get('createdAtISO'))
        if when is None:
            try:
                when = datetime.datetime.strptime(p.get('createdAt', ''), '%a %b %d %H:%M:%S %z %Y')
            except (TypeError, ValueError):
                when = None
        if when is None or when < window_start:
            continue
        out.append({'id': pid, 'author': screen, 'published_at': when.astimezone(datetime.timezone.utc).isoformat(timespec='seconds'),
                    'url': f'https://x.com/{screen}/status/{pid}', 'text': text.strip()})
    return out, True


def cmd_prepare(args):
    root = pathlib.Path(args.root) if args.root else DEFAULT_ROOT
    ref_day = parse_day_token(args.day) if args.day else sh_date(now_sh())
    if args.day and ref_day is None:
        fail([f'--day 非法：{args.day}（需 YYYYMMDD）'])
    window_start, window_end_default, days_wanted = day_range(ref_day)
    window_end = window_end_default if args.day else now_sh()

    batches, skipped = load_batch_dirs(root, days_wanted)
    if not batches:
        fail([f'窗口 {days_wanted[0]}~{days_wanted[-1]} 内没有已完成（DONE）批次，不复用旧成果冒充新一期；'
              f'root={root}，跳过目录：{skipped or "无"}'])

    coverage = {'denominator': 0, 'succeeded': 0, 'missing': 0, 'errors': 0,
                'days_expected': WINDOW_DAYS, 'days_completed': len(batches),
                'days_missing': [d for d in days_wanted if d not in {b["day"] for b in batches}],
                'skipped_incomplete': skipped, 'batches': []}
    problems = []
    by_id = {}
    data_cutoff = None
    for b in batches:
        m = b['manifest']
        posts_dir = b['dir'] / 'posts'
        if not posts_dir.is_dir():
            problems.append({'day': b['day'], 'error': 'posts_dir_missing'})
            continue
        if b['legacy']:
            # 上一代格式：无逐账号状态。denominator 取 expected_accounts，
            # succeeded 只数真实可读文件，缺口记 missing（不猜限流/错误明细）。
            expected = m.get('expected_accounts') or []
            files_ok = 0
            for f in sorted(posts_dir.glob('*.json')):
                got, file_ok = posts_from_file(f, f.stem, window_start, problems)
                files_ok += 1 if file_ok else 0
                for post in got:
                    by_id[post['id']] = post
            coverage['denominator'] += len(expected)
            coverage['succeeded'] += files_ok
            coverage['missing'] += max(0, len(expected) - files_ok)
            coverage['batches'].append({'day': b['day'], 'finished_at': m.get('as_of'), 'legacy': True,
                                        'denominator': len(expected), 'succeeded': files_ok,
                                        'missing': max(0, len(expected) - files_ok), 'errors': None})
            finished = parse_iso(m.get('as_of'))
            if finished is not None and (data_cutoff is None or finished > data_cutoff):
                data_cutoff = finished
            continue
        accounts = m.get('accounts') or []
        fetched = sum(1 for a in accounts if a.get('status') == 'fetched')
        limited = sum(1 for a in accounts if a.get('status') == 'rate_limited')
        errs = sum(1 for a in accounts if a.get('status') in ('error', 'auth_failed'))
        coverage['denominator'] += len(accounts)
        coverage['succeeded'] += fetched
        coverage['missing'] += limited
        coverage['errors'] += errs
        coverage['batches'].append({'day': b['day'], 'finished_at': m.get('finished_at'),
                                    'denominator': len(accounts), 'succeeded': fetched,
                                    'missing': limited, 'errors': errs})
        finished = parse_iso(m.get('finished_at'))
        if finished is not None and (data_cutoff is None or finished > data_cutoff):
            data_cutoff = finished
        for a in accounts:
            if a.get('status') != 'fetched' or not a.get('handle'):
                continue
            # 防孤儿/缺文件/权限：读取失败只降级为该账号问题记录，不中断
            got, _file_ok = posts_from_file(posts_dir / f'{a["handle"]}.json', a['handle'], window_start, problems)
            for post in got:  # 后到的批次覆盖同 ID，保留最新采集版本
                by_id[post['id']] = post
    coverage['read_problems'] = problems[:20]

    posts = sorted(by_id.values(), key=lambda p: (p['published_at'], p['id']), reverse=True)
    if data_cutoff is None:
        data_cutoff = window_end
    preview = {'schema': 'twitter-preview/1',
               'window': {'start': iso_sh(window_start), 'end': iso_sh(window_end)},
               'data_cutoff': data_cutoff.isoformat(timespec='seconds') if hasattr(data_cutoff, 'isoformat') else str(data_cutoff),
               'coverage': coverage,
               'posts': posts}
    out = pathlib.Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(out, preview)
    ok({'output': str(out), 'posts': len(posts), 'window': preview['window'],
        'coverage': {k: coverage[k] for k in ('denominator', 'succeeded', 'missing', 'errors', 'days_completed')}})


def atomic_write(path, payload):
    tmp_fd, tmp_name = tempfile.mkstemp(dir=str(path.parent), prefix=path.name, suffix='.tmp')
    try:
        with os.fdopen(tmp_fd, 'w', encoding='utf-8') as f:
            json.dump(payload, f, ensure_ascii=False, indent=1)
        os.replace(tmp_name, path)
    finally:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)


# ---------------------------- build ----------------------------

def clamp(text, limit):
    text = (text or '').strip()
    return text if len(text) <= limit else text[:limit - 1] + '…'


def num_str(v):
    if isinstance(v, bool):
        return str(v)
    if isinstance(v, int):
        return str(v)
    return f'{v:.6g}'


def is_number(v):
    return not isinstance(v, bool) and isinstance(v, (int, float)) and v == v and v not in (float('inf'), float('-inf'))


def is_metric_complete(metric):
    for key in ('name', 'unit', 'period', 'basis', 'source_url', 'source_date'):
        if not isinstance(metric.get(key), str) or not metric[key].strip():
            return False
    if not RE_HTTPS.match(metric['source_url']):
        return False
    return (is_number(metric.get('value')) and is_number(metric.get('baseline_value'))
            and isinstance(metric.get('baseline_period'), str) and metric['baseline_period'].strip())


def metric_missing_fields(metric):
    missing = []
    for key in METRIC_FIELDS:
        if key in ('value', 'baseline_value'):
            if not is_number(metric.get(key)):
                missing.append(key)
        elif not isinstance(metric.get(key), str) or not metric[key].strip():
            missing.append(key)
    if isinstance(metric.get('source_url'), str) and metric['source_url'] and not RE_HTTPS.match(metric['source_url']):
        missing.append('source_url(非https)')
    return missing


def validate_theme(theme, posts_index, today, errors, prefix):
    def err(msg):
        errors.append(f'{prefix}: {msg}')

    if not isinstance(theme, dict):
        err('主题不是对象')
        return None
    for key in ('id', 'label', 'horizon', 'scope', 'gap'):
        v = theme.get(key)
        if not isinstance(v, str) or not v.strip():
            err(f'{key} 缺失或为空')
    tid = theme.get('id')
    if isinstance(tid, str) and not RE_THEME_ID.match(tid):
        err(f'id 非法（小写字母/数字/._- ，≤40 位）：{tid!r}')
    claims = theme.get('claims')
    if not isinstance(claims, list) or not claims:
        err('claims 必须是非空数组（无证据的主题不应存在）')
        claims = []
    seen = set()
    for i, c in enumerate(claims):
        if not isinstance(c, dict):
            err(f'claims[{i}] 不是对象')
            continue
        pid = c.get('post_id')
        if not isinstance(pid, str) or not pid.isdigit():
            err(f'claims[{i}].post_id 必须是数字字符串')
        elif pid not in posts_index:
            err(f'claims[{i}].post_id 不在预览中：{pid}')
        elif pid in seen:
            err(f'claims[{i}].post_id 重复：{pid}')
        else:
            seen.add(pid)
        if c.get('stance') not in STANCES:
            err(f'claims[{i}].stance 非法：{c.get("stance")!r}')
        s = c.get('summary')
        if not isinstance(s, str) or not s.strip() or len(s) > SUMMARY_MAX:
            err(f'claims[{i}].summary 缺失、为空或超过 {SUMMARY_MAX} 字')
    impacts = theme.get('impacts')
    if not isinstance(impacts, list):
        err('impacts 必须是数组（可为空）')
        impacts = []
    symbols = []
    for i, imp in enumerate(impacts):
        if not isinstance(imp, dict):
            err(f'impacts[{i}] 不是对象')
            continue
        sym = imp.get('symbol')
        if not isinstance(sym, str) or not RE_SYMBOL.match(sym):
            err(f'impacts[{i}].symbol 非法：{sym!r}')
        else:
            symbols.append(sym)
        for key in ('assessment', 'counterpoint', 'next_check'):
            v = imp.get(key)
            if not isinstance(v, str) or not v.strip():
                err(f'impacts[{i}].{key} 缺失或为空' + ('（反证不得为空）' if key == 'counterpoint' else ''))
        status = imp.get('status')
        if status not in ('supported', 'pending'):
            err(f'impacts[{i}].status 非法：{status!r}')
        metrics = imp.get('metrics')
        if not isinstance(metrics, list):
            err(f'impacts[{i}].metrics 必须是数组')
            metrics = []
        complete = 0
        for j, m in enumerate(metrics):
            if not isinstance(m, dict):
                err(f'impacts[{i}].metrics[{j}] 不是对象')
                continue
            missing = metric_missing_fields(m)
            if missing:
                err(f'impacts[{i}].metrics[{j}] 不完整：缺 {missing}')
            sd = m.get('source_date') if isinstance(m, dict) else None
            if isinstance(sd, str) and re.match(r'^\d{4}-\d{2}-\d{2}$', sd):
                try:
                    if datetime.date.fromisoformat(sd) > today:
                        err(f'impacts[{i}].metrics[{j}].source_date 来自未来：{sd}')
                except ValueError:
                    err(f'impacts[{i}].metrics[{j}].source_date 非法：{sd}')
            elif isinstance(sd, str) and sd.strip():
                err(f'impacts[{i}].metrics[{j}].source_date 必须 YYYY-MM-DD：{sd}')
            if isinstance(m, dict) and is_metric_complete(m):
                complete += 1
        if status == 'supported' and complete < 1:
            err(f'impacts[{i}] status=supported 但没有一条完整可比数值（value+baseline+口径+来源），降为 pending 或补齐量化')
    if errors and any(e.startswith(prefix) for e in errors):
        return None
    return {'theme': theme, 'claims': claims, 'impacts': impacts, 'symbols': symbols}


def merge_author_stances(claims, posts_index):
    """同主题同作者归并只计一次；bull+bear → mixed；与 unknown 并存 → unknown。"""
    authors = {}
    for c in claims:
        pid = c.get('post_id')
        post = posts_index.get(pid)
        if not post:
            continue
        authors.setdefault(post['author'], set()).add(c.get('stance'))
    merged = {}
    for author, stances in authors.items():
        if 'bull' in stances and 'bear' in stances:
            merged[author] = 'mixed'
        elif 'unknown' in stances:
            merged[author] = 'unknown'
        elif len(stances) == 1:
            merged[author] = stances.pop()
        else:
            merged[author] = 'mixed'
    return merged


def theme_stance(merged):
    """主题立场 = 作者归并立场集合：单一则该值，多种并存则 mixed。"""
    values = set(merged.values())
    if len(values) == 1:
        return values.pop()
    return 'mixed'


def metric_line(m):
    return (f"· {m['name']}：{num_str(m['value'])} {m['unit']}（{m['period']}）"
            f"vs 基线 {num_str(m['baseline_value'])}（{m['baseline_period']}）；"
            f"口径 {m['basis']}；来源 {m['source_url']}（{m['source_date']}）")


def build_items(batch_id, ref_day, preview, themes_ok, posts_index):
    coverage = preview['coverage']
    cov_note = (f"采集覆盖 {coverage['succeeded']}/{coverage['denominator']} 账号日成功"
                f"（近 {coverage['days_completed']}/{coverage['days_expected']} 天有完成批次）；覆盖只代表采集，参与人数另计。")
    items = [{
        'logical_id': f'{batch_id}-health',
        'kind': 'health', 'category': 'fact', 'title': clamp(f'X 关注圈周报健康度：{coverage["succeeded"]}/{coverage["denominator"]} 账号日采集成功', SHOW_TITLE_MAX),
        'body': clamp(f"窗口 {preview['window']['start']} ~ {preview['window']['end']}；数据截止 {preview['data_cutoff']}。"
                      f"缺 {coverage['missing']} 个账号日（限流/错误 {coverage['errors']}），缺整天 {len(coverage['days_missing'])} 天。"
                      f"覆盖≠参与讨论，也非全量抽样。", SHOW_BODY_THEME),
        'coverage_note': clamp(cov_note, NOTE_MAX), 'importance': 1, 'topics': ['X 关注圈', '周报'],
    }]
    for entry in themes_ok:
        t, claims, impacts, symbols = entry['theme'], entry['claims'], entry['impacts'], entry['symbols']
        merged = merge_author_stances(claims, posts_index)
        participants = len(merged)
        tstance = theme_stance(merged)
        counts = {s: sum(1 for v in merged.values() if v == s) for s in STANCES}
        lines = [f"范围：{t['scope']}", f"争议：{t['gap']}",
                 f"参与：{participants} 位作者（牛 {counts['bull']} / 熊 {counts['bear']} / 混合 {counts['mixed']} / 未知 {counts['unknown']}，同作者只计一次）",
                 '—— 代表论点 ——']
        shown_authors = set()
        shown = 0
        for c in claims:
            post = posts_index.get(c.get('post_id'))
            if not post or post['author'] in shown_authors:
                continue
            lines.append(f"· {post['author']}（{c['stance']}）：{clamp(c['summary'], 90)} {post['url']}")
            shown_authors.add(post['author'])
            shown += 1
            if shown >= MAX_CLAIMS_SHOWN:
                lines.append('…（其余论点见证据条目）')
                break
        if impacts:
            lines.append('—— 标的影响 ——')
            for imp in impacts:
                lines.append(f"· {imp['symbol']}（{imp['status']}）：{clamp(imp['assessment'], 140)}")
                lines.append(f"  反证：{clamp(imp['counterpoint'], 90)}")
                lines.append(f"  下一验证：{clamp(imp['next_check'], 90)}")
        items.append({
            'logical_id': f'{batch_id}-{t["id"]}',
            'kind': 'opinion', 'category': 'ai_explainer',
            'title': clamp(f"{t['label']}｜共识差：{t['gap']}", SHOW_TITLE_MAX),
            'body': clamp('\n'.join(lines), SHOW_BODY_THEME),
            'stance': tstance, 'coverage_note': clamp(f"{cov_note}；本主题参与 {participants} 位作者。", NOTE_MAX),
            'importance': 2, 'topics': ['X 关注圈', '周报', clamp(t['label'], 40)], 'symbols': sorted(set(symbols))[:12],
        })
        # 少量原帖证据：作者不重复，按 claims 顺序
        seen_authors = set()
        picked = 0
        for c in claims:
            if picked >= EVIDENCE_PER_THEME:
                break
            post = posts_index.get(c.get('post_id'))
            if not post or post['author'] in seen_authors:
                continue
            seen_authors.add(post['author'])
            picked += 1
            items.append({
                'logical_id': f'{batch_id}-{t["id"]}-{post["id"]}',
                'kind': 'opinion', 'category': 'external_opinion',
                'title': clamp(f"{post['author']}（{c['stance']}）：{c['summary']}", SHOW_TITLE_MAX),
                'body': clamp(post['text'], SHOW_BODY_EVIDENCE),
                'url': post['url'], 'author': post['author'], 'stance': c['stance'],
                'published_at': post['published_at'],
                'coverage_note': clamp(f"原帖全文见链接；采集于 {ref_day} 批次。", NOTE_MAX),
                'importance': 2, 'topics': ['X 关注圈', '周报', clamp(t['label'], 40)], 'symbols': sorted(set(symbols))[:12],
            })
        # 量化报告：只有 supported（即已保证完整数值）才出
        for imp in impacts:
            if imp.get('status') != 'supported':
                continue
            complete = [m for m in imp.get('metrics', []) if isinstance(m, dict) and is_metric_complete(m)]
            if not complete:
                continue
            rlines = [f"{t['label']} → {imp['symbol']}（{imp['status']}）：{imp['assessment']}", '—— 量化证据 ——']
            rlines.extend(metric_line(m) for m in complete)
            rlines.append(f"反证：{imp['counterpoint']}")
            rlines.append(f"下一验证：{imp['next_check']}")
            items.append({
                'logical_id': f'{batch_id}-{t["id"]}-{imp["symbol"]}',
                'kind': 'report', 'category': 'fact',
                'title': clamp(f"{imp['symbol']}·{t['label']}·量化证据", SHOW_TITLE_MAX),
                'body': clamp('\n'.join(rlines), SHOW_BODY_REPORT),
                'coverage_note': clamp(cov_note, NOTE_MAX),
                'importance': 2, 'topics': ['X 关注圈', '周报', clamp(t['label'], 40)], 'symbols': [imp['symbol']],
            })
    return items


def self_check(batch, errors):
    """镜像 Board validateBatch/validateItem，写盘前自检。"""
    if not RE_BATCH_ID.match(batch.get('batch_id') or ''):
        errors.append(f'自检失败：batch_id 非法 {batch.get("batch_id")!r}')
    if batch.get('kind') != 'twitter':
        errors.append('自检失败：kind 必须 twitter')
    if len(batch.get('items') or []) > 500:
        errors.append('自检失败：items 超 500')
    for i, item in enumerate(batch.get('items') or []):
        if not RE_LOGICAL_ID.match(item.get('logical_id') or ''):
            errors.append(f'自检失败：items[{i}].logical_id 非法')
        if not item.get('title'):
            errors.append(f'自检失败：items[{i}].title 缺失')
        if len(item.get('title') or '') > TITLE_MAX or len(item.get('body') or '') > BODY_MAX or len(item.get('coverage_note') or '') > NOTE_MAX:
            errors.append(f'自检失败：items[{i}] 字段超长')
        url = item.get('url')
        if url and not RE_HTTPS.match(url):
            errors.append(f'自检失败：items[{i}].url 必须 https')
        for s in item.get('symbols') or []:
            if not RE_SYMBOL.match(s):
                errors.append(f'自检失败：items[{i}].symbols 含非法代码 {s!r}')


def cmd_build(args):
    try:
        preview = json.loads(pathlib.Path(args.input).read_text(encoding='utf-8'))
        analysis = json.loads(pathlib.Path(args.analysis).read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as e:
        fail([f'读取输入失败：{e}'])
    if not isinstance(preview, dict) or not isinstance(preview.get('posts'), list) or not isinstance(preview.get('window'), dict):
        fail(['预览文件结构非法：需 window 与 posts（请先运行 prepare）'])
    posts_index = {p['id']: p for p in preview['posts'] if isinstance(p, dict) and isinstance(p.get('id'), str)}
    themes = analysis.get('themes') if isinstance(analysis, dict) else None
    if not isinstance(themes, list):
        fail(['analysis JSON 需要 themes 数组（允许为空）'])
    if len(themes) > MAX_THEMES:
        fail([f'themes 超过上限 {MAX_THEMES}'])
    errors = []
    today = now_sh().date()
    themes_ok = []
    for i, theme in enumerate(themes):
        got = validate_theme(theme, posts_index, today, errors, f'themes[{i}]')
        if got:
            themes_ok.append(got)
    if errors:
        fail(errors)

    ref_day = (parse_iso(preview['window']['end']) or now_sh()).astimezone(TZ_SH).strftime('%Y%m%d')
    batch_id = f'x-consensus-{ref_day}'
    batch = {'batch_id': batch_id, 'kind': 'twitter',
             'window': preview['window'], 'data_cutoff': preview['data_cutoff'],
             'items': build_items(batch_id, ref_day, preview, themes_ok, posts_index)}
    self_check(batch, errors)
    if errors:
        fail(errors)
    out = pathlib.Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(out, {'batch': batch})
    kind_counts = {}
    for item in batch['items']:
        kind_counts[f'{item["kind"]}/{item["category"]}'] = kind_counts.get(f'{item["kind"]}/{item["category"]}', 0) + 1
    ok({'output': str(out), 'batch_id': batch_id, 'items': len(batch['items']), 'kinds': kind_counts})


def main(argv):
    parser = argparse.ArgumentParser(description='X 关注圈 → 共识差 → Research Desk Board 管线（E 组）')
    sub = parser.add_subparsers(dest='cmd', required=True)
    p_prepare = sub.add_parser('prepare', help='近七天完成批次 → 预览 JSON')
    p_prepare.add_argument('--output', required=True)
    p_prepare.add_argument('--day', help='历史窗口末日 YYYYMMDD（缺省今天，上海时区）')
    p_prepare.add_argument('--root', help='采集 weekly 根目录（缺省 ~/.agent-reach/x_digest_261105/weekly；测试用）')
    p_build = sub.add_parser('build', help='预览 + AI 萕取 → Board 批次 JSON')
    p_build.add_argument('--input', required=True, help='prepare 输出的预览文件')
    p_build.add_argument('--analysis', required=True, help='AI 萕取 JSON')
    p_build.add_argument('--output', required=True)
    args = parser.parse_args(argv)
    if args.cmd == 'prepare':
        cmd_prepare(args)
    else:
        cmd_build(args)


if __name__ == '__main__':
    main(sys.argv[1:])
