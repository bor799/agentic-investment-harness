#!/usr/bin/env python3
"""Normalize completed X captures and build a validated Research Desk batch.

No network or database access. The scheduled Agent supplies the interpretation
and sends the resulting batch through the installed plugin.
"""

import argparse
import datetime as dt
import hashlib
import json
import math
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit
from zoneinfo import ZoneInfo

SHANGHAI = ZoneInfo("Asia/Shanghai")
CAPTURE_ROOT = Path.home() / ".agent-reach" / "x_digest_261105" / "weekly"
HANDLE = re.compile(r"[a-z0-9_]{1,15}")
POST_ID = re.compile(r"[0-9]{1,25}")
STANCES = ("bull", "bear", "mixed", "unknown")


def load(path):
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def dump(path, obj):
    with path.open("x", encoding="utf-8") as stream:
        json.dump(obj, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")


def stamp(value):
    parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("时间戳缺时区")
    return parsed.astimezone(dt.timezone.utc)


def day_label(day):
    return day.strftime("%Y%m%d")


def days_in_window(day):
    return (day - dt.timedelta(days=offset) for offset in range(7))


def capture(root, day):
    """Read only the success-marked formats used by B and its historical backfill."""
    folder = root / day_label(day)
    marker = load(folder / "DONE.json")
    manifest = load(folder / "manifest.json")
    if marker.get("status") != "complete":
        raise ValueError("采集未完成")
    if "accounts" in manifest:
        entries = manifest["accounts"]
        names = [e["handle"] for e in entries if e["status"] == "fetched" and not e.get("write_error")]
        counts = manifest["summary"]
        denominator = counts["denominator"]
        cutoff = stamp(manifest["started_at"])
        failures = []
        if counts.get("rate_limited") or counts.get("errors"):
            failures.append(f"限流 {counts.get('rate_limited', 0)}，错误 {counts.get('errors', 0)}")
    else:
        names = marker["successful_accounts"]
        denominator = len(manifest["expected_accounts"])
        cutoff = stamp(manifest["as_of"])
        failures = []
    if cutoff.astimezone(SHANGHAI).date() != day:
        raise ValueError("采集目录与上海日期不符")
    if not isinstance(denominator, int) or isinstance(denominator, bool) or not 0 < denominator <= 1000:
        raise ValueError("采集账号分母无效")
    return folder, cutoff, names, denominator, failures


def read_capture(folder, names, start, end):
    posts, authors, seen = {}, set(), set()
    capped = invalid_files = mismatched = 0
    for name in names:
        if not isinstance(name, str) or not HANDLE.fullmatch(name.lower()) or name.lower() in seen:
            invalid_files += 1
            continue
        handle = name.lower()
        seen.add(handle)
        try:
            raw = load(folder / "posts" / f"{name}.json")
            if raw.get("ok") is not True or not isinstance(raw.get("data"), list):
                raise ValueError("原帖响应不是成功列表")
            rows = raw["data"]
        except (OSError, ValueError, AttributeError):
            invalid_files += 1
            continue
        authors.add(handle)
        capped += len(rows) >= 200
        for row in rows:
            try:
                text = row["text"].strip()
                if row.get("isRetweet") or re.match(r"^RT\s+@", text, re.IGNORECASE):
                    continue
                author = row["author"]["screenName"].lower()
                if author != handle:
                    mismatched += 1
                    continue
                when = stamp(row["createdAtISO"])
                post_id = row["id"]
                if (
                    not isinstance(post_id, str) or not POST_ID.fullmatch(post_id)
                    or not text or not start <= when < end
                ):
                    continue
            except (KeyError, ValueError, TypeError, AttributeError):
                mismatched += 1
                continue
            posts.setdefault(post_id, dict(
                id=post_id, author=author, published_at=when.isoformat(),
                url=f"https://x.com/{author}/status/{post_id}", text=text,
            ))
    return posts, authors, capped, invalid_files, mismatched


def prepare(root, day):
    label = day_label(day)
    default_cutoff = dt.datetime.combine(day, dt.time(5, 30), tzinfo=SHANGHAI)
    coverage = dict(denominator=0, succeeded=0, missing=[], errors=[])
    try:
        latest = capture(root, day)
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        coverage["errors"] = ["当日没有可读的已完成采集；等待 B 组或检查采集回执"]
        cutoff = default_cutoff
        return dict(
            day=label, status="missing", data_cutoff=cutoff.isoformat(),
            window=dict(start=(cutoff - dt.timedelta(days=7)).isoformat(), end=cutoff.isoformat()),
            coverage=coverage, capture_days=0, window_authors=0, posts=[],
        )
    cutoff = latest[1]
    start = cutoff - dt.timedelta(days=7)
    posts, authors, capture_days = {}, set(), 0
    for capture_day in days_in_window(day):
        try:
            folder, _, names, denominator, notes = latest if day == capture_day else capture(root, capture_day)
        except (OSError, ValueError, KeyError, TypeError, AttributeError):
            continue
        rows, ok_authors, capped, bad_files, mismatched = read_capture(folder, names, start, cutoff)
        capture_days += 1
        authors.update(ok_authors)
        for post_id, row in rows.items():
            posts.setdefault(post_id, row)
        if capture_day == day:
            coverage.update(denominator=denominator, succeeded=len(ok_authors))
            missing_count = max(denominator - len(ok_authors), 0)
            if missing_count:
                coverage["missing"].append(f"{missing_count} 个账号本次未成功取得可读响应")
            coverage["errors"].extend(notes)
        if capped or bad_files or mismatched:
            coverage["errors"].append(
                f"{day_label(capture_day)}：{capped} 个达到 200 条上限，"
                f"{bad_files} 个原始文件不可用，{mismatched} 条来源或格式不符"
            )
    if capture_days < 7:
        coverage["missing"].append(f"七个计划采集日中有 {capture_days} 日的完成材料可用")
    status = "ready" if coverage["succeeded"] > 0 else "missing"
    return dict(
        day=label, status=status, data_cutoff=cutoff.isoformat(),
        window=dict(start=start.isoformat(), end=cutoff.isoformat()),
        coverage=coverage, capture_days=capture_days, window_authors=len(authors),
        posts=sorted(posts.values(), key=lambda p: (p["published_at"], p["id"])),
    )


def required_text(obj, key, limit):
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip() or len(value) > limit:
        raise ValueError(f"{key} 必须为非空文本，最多 {limit} 字")
    return value.strip()


def bounded_list(obj, key, limit, optional=False):
    value = obj.get(key, [] if optional else None)
    if not isinstance(value, list) or len(value) > limit or not all(isinstance(item, dict) for item in value):
        raise ValueError(f"{key} 必须为对象数组，最多 {limit} 项")
    return value


def number(obj, key):
    value = obj.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{key} 必须为有限数字")
    return value


def https_source(obj, key):
    value = required_text(obj, key, 500)
    url = urlsplit(value)
    if url.scheme != "https" or not url.hostname or url.username or url.password or any(c.isspace() for c in value):
        raise ValueError(f"{key} 必须为无凭据的 HTTPS 链接")
    return value


def disclosure_date(obj, cutoff):
    date_text = required_text(obj, "source_date", 10)
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_text):
        raise ValueError("披露日期须为 YYYY-MM-DD")
    date = dt.date.fromisoformat(date_text)
    if date > cutoff.astimezone(SHANGHAI).date():
        raise ValueError("披露日期超过数据截止")
    return date


def impact_lines(impact, cutoff, symbols):
    symbol = required_text(impact, "symbol", 12)
    if symbol not in symbols:
        raise ValueError(f"标的不在 Desk 研究池：{symbol}")
    assessment = required_text(impact, "assessment", 220)
    counterpoint = required_text(impact, "counterpoint", 140)
    next_check = required_text(impact, "next_check", 150)
    status = impact.get("status")
    metrics = bounded_list(impact, "metrics", 2)
    if status not in ("supported", "pending") or (status == "supported" and not metrics):
        raise ValueError("有量化支撑的判断必须有至少一条可比指标；其余标记 pending")
    lines = [f"{symbol}｜{'有量化支撑' if status == 'supported' else '待验证'} · {assessment}"]
    sources = []
    for metric in metrics:
        name = required_text(metric, "name", 50)
        unit = required_text(metric, "unit", 24)
        period = required_text(metric, "period", 36)
        baseline_period = required_text(metric, "baseline_period", 36)
        basis = required_text(metric, "basis", 100)
        value = number(metric, "value")
        baseline = number(metric, "baseline_value")
        source_url = https_source(metric, "source_url")
        source_date = disclosure_date(metric, cutoff)
        lines.append(
            f"{name}：{period} {value} {unit}，对照 {baseline_period} {baseline} {unit}。"
            f"口径：{basis}。来源（{source_date}）：{source_url}"
        )
        sources.append(dict(title=name, url=source_url))
    lines.extend((f"反证：{counterpoint}", f"下次验证：{next_check}"))
    return symbol, lines, sources


def resolve_claims(theme, posts):
    """Count an author once for the same question, even after several posts."""
    by_author = {}
    seen_posts = set()
    for claim in bounded_list(theme, "claims", 160):
        post_id = required_text(claim, "post_id", 25)
        if post_id not in posts or post_id in seen_posts:
            raise ValueError(f"原帖不存在或在同一论题重复：{post_id}")
        seen_posts.add(post_id)
        stance = claim.get("stance")
        if stance not in STANCES:
            raise ValueError("stance 不在允许范围")
        post = posts[post_id]
        by_author.setdefault(post["author"], []).append(
            (stance, required_text(claim, "summary", 100), post)
        )
    if not by_author:
        raise ValueError("有主题时须至少引用一条窗口内原帖")
    counts = dict.fromkeys(STANCES, 0)
    representatives = {key: [] for key in STANCES}
    for claims in by_author.values():
        known = {stance for stance, _, _ in claims} - {"unknown"}
        stance = "mixed" if len(known) > 1 else next(iter(known), "unknown")
        counts[stance] += 1
        representatives[stance].extend(
            claim for claim in claims if claim[0] == stance or (stance == "mixed" and claim[0] != "unknown")
        )
    return counts, representatives


def follow_up_lines(analysis):
    lines = []
    for key, heading in (("review", "上期核验"), ("calendar", "未来事项")):
        rows = bounded_list(analysis, key, 8, optional=True)
        if not rows:
            continue
        lines.append(heading)
        for row in rows:
            summary = required_text(row, "summary", 180)
            date = dt.date.fromisoformat(required_text(row, "date", 10))
            url = https_source(row, "url") if row.get("url") else ""
            lines.append(f"{date} {summary}" + (f"｜{url}" if url else ""))
    return lines


def build(preview, analysis, symbols, job_id=None, run_id=None):
    if not isinstance(analysis, dict):
        raise ValueError("分析必须为 JSON 对象")
    day = preview["day"]
    window = preview["window"]
    cutoff = stamp(preview["data_cutoff"])
    coverage = preview["coverage"]
    prefix = f"x-consensus-{day}"
    ready = preview["status"] == "ready"
    themes = bounded_list(analysis, "themes", 3)
    if themes and not ready:
        raise ValueError("本期无完整采集回执，不能发布观点")
    posts = {p["id"]: p for p in preview["posts"]}
    cutoff_label = cutoff.astimezone(SHANGHAI).strftime("%m-%d %H:%M")
    sample = (
        f"本次可读账号 {coverage['succeeded']}/{coverage['denominator']}，"
        f"七天内 {preview['capture_days']} 日有采集材料、{preview['window_authors']} 个账号取数成功，"
        f"筛出 {len(posts)} 条窗口内帖子"
        f"（北京 {cutoff_label} 截止）。取数成功率不代表帖子全量覆盖。"
    ) if coverage["denominator"] else "本期未取得完成采集，覆盖未知。"
    batch = dict(batch_id=prefix if ready else f"x-consensus-health-{day}",
                 kind="twitter", window=window, data_cutoff=preview["data_cutoff"],
                 coverage=coverage, sources=[], items=[])
    if job_id:
        batch["job_id"] = job_id
    if run_id:
        batch["run_id"] = run_id
    items = batch["items"]
    registered = {}

    def register_disclosure(url, title):
        digest = hashlib.sha256(url.encode()).hexdigest()[:24]
        registered.setdefault(url, dict(root_id=f"filing:{digest}", title=title, url=url, provider="原始披露"))

    def item(suffix, kind, category, title, body, **extra):
        if len(body) > 8000:
            raise ValueError("报告超过 Desk 正文上限，请缩短")
        document = dict(logical_id=f"{prefix}-{suffix}", kind=kind, category=category, title=title,
                        body=body, event_time=preview["data_cutoff"], importance=2,
                        topics=["X 关注圈", "周报"], coverage_note=sample, **extra)
        items.append(document)
        return document

    used_themes = set()
    sections = [sample, "以下为关注样本中的论点。市场预期需用独立资料验证。"]
    for theme in themes:
        theme_id = required_text(theme, "id", 32)
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", theme_id) or theme_id in used_themes:
            raise ValueError("主题 ID 须为不重复的英文 slug")
        used_themes.add(theme_id)
        label = required_text(theme, "label", 40)
        horizon = required_text(theme, "horizon", 28)
        scope = required_text(theme, "scope", 120)
        gap = required_text(theme, "gap", 220)
        counts, representatives = resolve_claims(theme, posts)
        counts_label = f"{sum(counts.values())} 位被归入此论题：多 {counts['bull']} / 空 {counts['bear']} / 混合 {counts['mixed']} / 未知 {counts['unknown']}"
        split = bool(counts["bull"] and counts["bear"])
        lines = [f"{scope}｜期限 {horizon}", counts_label]
        lines.append(f"{'在争什么' if split else '观察到的论点'}：{gap}")
        if not split:
            lines.append("本期未观察到两边均有独立作者明确表态。")
        theme_symbols = []
        evidence_url = None
        for impact in bounded_list(theme, "impacts", 2):
            symbol, details, sources = impact_lines(impact, cutoff, symbols)
            if symbol in theme_symbols:
                raise ValueError("主题内同一标的影响重复")
            theme_symbols.append(symbol)
            lines.extend(details)
            for source in sources:
                url = source["url"]
                evidence_url = evidence_url or url
                register_disclosure(url, source["title"])
        for check in bounded_list(theme, "cross_checks", 2, optional=True):
            finding = required_text(check, "finding", 200)
            url = https_source(check, "url")
            date = disclosure_date(check, cutoff)
            evidence_url = evidence_url or url
            register_disclosure(url, f"{label}｜交叉核验")
            lines.append(f"交叉核验（{date}）：{finding}｜{url}")
        title = f"{'关注圈共识差' if split else '关注圈观察'}｜{label}"
        analysis_card = item(f"topic-{theme_id}", "opinion", "ai_explainer", title,
                             "\n".join(lines), symbols=theme_symbols,
                             **({"url": evidence_url} if evidence_url else {}))
        analysis_card["topics"].append(label)
        sections.append(f"{label}\n" + "\n".join(lines))
        for options in representatives.values():
            if not options:
                continue
            post_stance, summary, post = options[0]
            url = post["url"]
            root_id = f"x:{post['id']}"
            registered[url] = dict(root_id=root_id, title=f"@{post['author']} 原帖", url=url, provider="X")
            source_card = item(
                f"{theme_id}-{post['id']}", "opinion", "external_opinion",
                f"@{post['author']}｜{label}", summary, author=post["author"], stance=post_stance,
                published_at=post["published_at"], url=url, root_source_id=root_id, symbols=theme_symbols,
            )
            source_card["event_time"] = post["published_at"]
            source_card["topics"].append(label)

    if not themes or coverage["missing"] or coverage["errors"]:
        message = (
            "当日采集未完成或原始文件不可用，等待采集回执；未发布本期共识差。" if not ready
            else "没有足够可追溯的观点支撑本期共识差。" if not themes
            else "已发布本期观察，解读须结合以下覆盖缺口。"
        )
        item("coverage" if ready else "failed-capture", "health", "fact", "X 关注圈｜本期覆盖与缺口",
             "\n".join([message, sample, *coverage["missing"], *coverage["errors"]]), actionable=not ready)
    follow_up = follow_up_lines(analysis) if ready else []
    if themes or follow_up:
        sections.extend(follow_up)
        item("weekly", "report", "ai_explainer", "X 关注圈共识差周报", "\n\n".join(sections))
    batch["sources"] = list(registered.values())
    return {"batch": batch}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(required=True, dest="command")
    prep = commands.add_parser("prepare")
    prep.add_argument("--root", type=Path, default=CAPTURE_ROOT)
    prep.add_argument("--day", help="YYYYMMDD 历史回放；默认上海当日")
    prep.add_argument("--output", type=Path, required=True)
    pack = commands.add_parser("build")
    for arg in ("input", "analysis", "output"):
        pack.add_argument(f"--{arg}", type=Path, required=True)
    pack.add_argument("--symbols", default="", help="逗号分隔，由当前 Desk 研究池提供")
    pack.add_argument("--job-id")
    pack.add_argument("--run-id")
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            day = dt.datetime.strptime(args.day, "%Y%m%d").date() if args.day else dt.datetime.now(SHANGHAI).date()
            result = prepare(args.root, day)
            dump(args.output, result)
            print(f"{result['status']} {len(result['posts'])} 条 · {args.output}")
        else:
            symbols = {symbol.strip() for symbol in args.symbols.split(",") if symbol.strip()}
            if any(not re.fullmatch(r"[A-Z0-9.^-]{1,12}", symbol) for symbol in symbols):
                raise ValueError("研究池含非法标的代码")
            result = build(load(args.input), load(args.analysis), symbols, args.job_id, args.run_id)
            dump(args.output, result)
            print(f"{result['batch']['batch_id']} {len(result['batch']['items'])} 项 · {args.output}")
    except (OSError, ValueError, KeyError, TypeError, AttributeError, OverflowError) as error:
        print(f"Desk X 流程失败：{error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
