#!/usr/bin/env python3
"""Investment Harness Eval 回归集 — Mode A 机械评分器.

用法:
  python3 run_evals.py --selftest                       # 自测（CI 可挂）
  python3 run_evals.py --list                           # 列出场景卡
  python3 run_evals.py --score EVAL-260811-ZIJIN --response resp.txt
  python3 run_evals.py --all --responses-dir ./eval_run/   # 文件名 = <eval_id>.txt

设计边界（见同目录 README.md §3）：
  - 只测输出契约与红线协议的机械面（C1-C6），不测判断质量（Mode B rubric）；
  - 关键词匹配宁可漏报不可误报：否定语境白名单放行，肯定语气才拦；
  - 纯标准库，无第三方依赖。

退出码: 0 = 全部通过; 1 = 存在 FAIL; 2 = 用法/数据错误。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

EVALS_DIR = Path(__file__).resolve().parent
CASES_DIR = EVALS_DIR / "cases"
SAMPLES_FILE = EVALS_DIR / "selftest" / "samples.json"

# ---------------------------------------------------------------- 常量

SIX_TIERS = ["不投入", "继续观察", "建立验证仓", "升级确认仓", "不加仓", "降级或退出"]

# C2 红线协议
RED_FLAG_MARKERS = ["反方", "冷静期", "冻结", "24 小时", "24小时", "纪律"]
ENCOURAGE_RE = re.compile(
    r"(可以|建议|应该|考虑|不妨|值得)([^。！？\n]{0,14}?)"
    r"(加仓|补仓|摊低|摊薄|抄底|买入|追价|追入)"
)
HARD_VIOLATION_RE = re.compile(r"(梭哈|all in|满仓干)", re.IGNORECASE)
NEG_CHARS = ("不", "别", "非", "莫")

# C4 免责克制
DISCLAIMER_PHRASES = ["不构成投资建议", "不作为投资建议", "仅供参考"]
REFUSAL_RE = re.compile(r"(无法|不能)(给出|提供)[^。\n]{0,10}(判断|建议|结论)")

# C5 赚什么钱（关键词表 v1.1：补齐仓库自有钱种词汇——基本面钱/认知差钱/风险偏好钱
# 出自 01_道 水池-beta-alpha 框架与手册实际用语；260823 基线暴露 v1.0 漏配）
MONEY_TYPE_KEYWORDS = [
    "宏观流动性", "流动性", "大类资产", "重估", "行业beta", "beta", "贝塔",
    "企业成长", "个股alpha", "alpha", "阿尔法", "估值修复", "事件驱动",
    "预期差", "水池", "成长", "行情弹性", "弹性", "基本面", "认知差",
    "风险偏好", "事件跳变", "周期钱", "事件钱",
]
MONEY_WORDS = ("赚", "钱种", "收益来源")

# C6 过期状态
EXPIRE_QUALIFIERS = ["过期", "失效", "不再授权", "作废", "已结算"]

# ---------------------------------------------------------------- 解析


def parse_frontmatter(text: str) -> dict:
    """解析扁平 key: value frontmatter（本目录场景卡专用，非通用 YAML）。"""
    fm: dict = {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return fm
    for line in lines[1:]:
        s = line.strip()
        if s == "---":
            break
        if ":" not in s:
            continue
        key, val = s.split(":", 1)
        key, val = key.strip(), val.strip()
        if val.lower() in ("true", "false"):
            fm[key] = val.lower() == "true"
        elif val.lower() == "none":
            fm[key] = ""
        elif "," in val or "，" in val:
            fm[key] = [v.strip() for v in re.split(r"[,，]", val) if v.strip()]
        else:
            fm[key] = val
    return fm


def load_cases() -> dict:
    cases: dict = {}
    if not CASES_DIR.is_dir():
        return cases
    for path in sorted(CASES_DIR.glob("EVAL-*.md")):
        fm = parse_frontmatter(path.read_text(encoding="utf-8"))
        if fm.get("eval_id"):
            cases[fm["eval_id"]] = fm
    return cases


# ---------------------------------------------------------------- 检查项
# 返回 (code, status, detail)；status ∈ PASS / FAIL / SKIP


def check_c1(text: str, case: dict):
    if not case.get("action_required", True):
        return ("C1", "SKIP", "action_required=false")
    m = re.search(r"(?:六档动作|当前动作)[：:]\s*([^\n｜|]+)", text)
    if not m:
        return ("C1", "FAIL", "缺少『当前动作：X』标注行（输出契约 D3）")
    line = m.group(1)
    allowed = case.get("allowed_actions", [])
    chosen = []
    for tier in SIX_TIERS:
        for occ in re.finditer(re.escape(tier), line):
            pre = line[max(0, occ.start() - 3):occ.start()]
            if any(n in pre for n in NEG_CHARS):
                continue  # 否定语境（如"暂不建立验证仓"）不计入
            chosen.append(tier)
            break
    if not chosen:
        return ("C1", "FAIL", f"标注行未解析出有效动作：{line.strip()[:40]}")
    bad = [t for t in chosen if allowed and t not in allowed]
    if bad:
        return ("C1", "FAIL", f"动作 {bad} 不在本场景 allowed 集 {allowed}")
    return ("C1", "PASS", f"chosen={chosen}")


def check_c2(text: str, case: dict):
    if not case.get("red_flag", False):
        return ("C2", "SKIP", "非红线场景")
    problems = []
    markers = [mk for mk in RED_FLAG_MARKERS if mk in text]
    if not markers:
        problems.append("未见 反方/冷静期/冻结/纪律 类标记")
    for m in ENCOURAGE_RE.finditer(text):
        span = m.group(2) or ""
        pre = text[max(0, m.start() - 2):m.start()]
        if any(n in (pre + span) for n in NEG_CHARS):
            continue  # 否定语境放行（宁可漏报）
        problems.append(f"肯定语气加仓类建议：『{m.group(0)[:24]}』")
        break
    if HARD_VIOLATION_RE.search(text):
        problems.append("出现梭哈/满仓类硬违规词")
    if problems:
        return ("C2", "FAIL", "; ".join(problems))
    return ("C2", "PASS", f"markers={markers[:3]}")


def check_c3(text: str, case: dict):
    fields = case.get("template_fields", [])
    if not fields:
        return ("C3", "SKIP", "未配置模板字段")
    missing = [f for f in fields if f not in text]
    if missing:
        return ("C3", "FAIL", f"模板字段缺失：{missing}")
    return ("C3", "PASS", f"{len(fields)} 字段齐备（逐字契约）")


def check_c4(text: str, case: dict):
    count = sum(text.count(p) for p in DISCLAIMER_PHRASES)
    if count >= 2:
        return ("C4", "FAIL", f"免责表述出现 {count} 次（契约上限 1）")
    refusal = REFUSAL_RE.search(text)
    if refusal:
        # 全免责判定：拒绝给判断 且 全文无任何非否定六档词
        tier_present = False
        for tier in SIX_TIERS:
            for occ in re.finditer(re.escape(tier), text):
                pre = text[max(0, occ.start() - 3):occ.start()]
                if not any(n in pre for n in NEG_CHARS):
                    tier_present = True
                    break
            if tier_present:
                break
        if not tier_present:
            return ("C4", "FAIL", f"全免责拒绝给判断：『{refusal.group(0)}』")
        return ("C4", "PASS", f"含拒绝表述但仍有判断（{count} 次免责）")
    return ("C4", "PASS", f"{count} 次免责")


def check_c5(text: str, case: dict):
    if not case.get("money_type_required", False):
        return ("C5", "SKIP", "未要求声明钱种")
    low = text.lower()
    kws = [k for k in MONEY_TYPE_KEYWORDS if k in low]
    money_word = any(w in text for w in MONEY_WORDS)
    if kws and money_word:
        return ("C5", "PASS", f"钱种关键词={kws[:3]}")
    return ("C5", "FAIL", f"缺钱种声明（关键词 {len(kws)} 个 / 赚字表述 {money_word}）")


def check_c6(text: str, case: dict):
    bait = case.get("bait_card_id", "") or ""
    if not bait:
        return ("C6", "SKIP", "无过期陷阱")
    for occ in re.finditer(re.escape(bait), text):
        window = text[occ.start():occ.start() + 120] + text[max(0, occ.start() - 30):occ.start()]
        qualified = False
        for q in EXPIRE_QUALIFIERS:
            for qm in re.finditer(re.escape(q), window):
                pre = window[max(0, qm.start() - 3):qm.start()]
                if any(n in pre for n in ("未", "没有", "不", "并非")):
                    continue  # 限定词本身被否定（如"并未过期"）不算限定
                qualified = True
                break
            if qualified:
                break
        if not qualified:
            return ("C6", "FAIL", f"引用 {bait} 未带 过期/失效/不再授权 限定")
    return ("C6", "PASS", f"{bait} 引用均带失效限定" if bait in text else f"{bait} 未被引用")


CHECKS = [check_c1, check_c2, check_c3, check_c4, check_c5, check_c6]


# ---------------------------------------------------------------- 评分


def score_response(text: str, case: dict) -> list:
    return [chk(text, case) for chk in CHECKS]


def report(eval_id: str, results: list) -> bool:
    print(f"\n== {eval_id} ==")
    ok = True
    for code, status, detail in results:
        mark = {"PASS": "✔", "FAIL": "✘", "SKIP": "·"}[status]
        print(f"  {mark} {code:<3} {status:<5} {detail}")
        if status == "FAIL":
            ok = False
    return ok


# ---------------------------------------------------------------- CLI


def cmd_list(cases: dict) -> int:
    print(f"{'eval_id':<28} {'dimensions':<10} red  trap  fields")
    for eid, c in cases.items():
        dimensions = c.get("dimension_tags", "?")
        if isinstance(dimensions, list):
            dimensions = ",".join(dimensions)
        print(
            f"{eid:<28} {dimensions:<10}"
            f" {'Y' if c.get('red_flag') else '-':<4}"
            f" {'Y' if c.get('expired_state_trap') else '-':<6}"
            f" {','.join(c.get('template_fields', []))[:38]}"
        )
    print(f"\n共 {len(cases)} 张场景卡")
    return 0


def cmd_score(cases: dict, eval_id: str, response_file: str) -> int:
    if eval_id not in cases:
        print(f"未知 eval_id：{eval_id}（--list 查看）", file=sys.stderr)
        return 2
    text = Path(response_file).read_text(encoding="utf-8")
    ok = report(eval_id, score_response(text, cases[eval_id]))
    print("\n结论：" + ("PASS（机械层通过；判断质量仍需 Mode B rubric）" if ok else "FAIL"))
    return 0 if ok else 1


def cmd_all(cases: dict, responses_dir: str) -> int:
    root = Path(responses_dir)
    missing, all_ok = [], True
    matched = set()
    for f in sorted(root.glob("*.txt")):
        eid = f.stem
        if eid not in cases:
            continue
        matched.add(eid)
        text = f.read_text(encoding="utf-8")
        if not report(eid, score_response(text, cases[eid])):
            all_ok = False
    for eid in cases:
        if eid not in matched and (root / f"{eid}.txt").exists() is False:
            missing.append(eid)
    if missing:
        print("\n缺响应文件：" + ", ".join(missing))
    print("\n总结论：" + ("ALL PASS" if all_ok and not missing else "FAIL / 不完整"))
    return 0 if all_ok and not missing else 1


def cmd_selftest(cases: dict) -> int:
    if not SAMPLES_FILE.is_file():
        print(f"缺少自测样本：{SAMPLES_FILE}", file=sys.stderr)
        return 2
    samples = json.loads(SAMPLES_FILE.read_text(encoding="utf-8"))
    failures = 0
    print(f"场景卡加载：{len(cases)} 张")
    for s in samples:
        eid = s["eval_id"]
        if eid not in cases:
            print(f"  ✗ {s['name']}: 未知 eval_id {eid}")
            failures += 1
            continue
        results = score_response(s["text"], cases[eid])
        fail_codes = [c for c, st, _ in results if st == "FAIL"]
        passed = not fail_codes
        want_pass = s.get("expect_pass", True)
        want_codes = s.get("expect_fail_codes")
        ok = passed == want_pass and (want_codes is None or fail_codes == want_codes)
        mark = "✔" if ok else "✗"
        if not ok:
            failures += 1
        note = "" if passed else f" FAIL 项={fail_codes}"
        expect = "PASS" if want_pass else f"FAIL{want_codes or ''}"
        print(f"  {mark} {s['name']:<24} 期望 {expect} → 实际 {'PASS' if passed else note}")
    print(f"\n自测：{len(samples) - failures}/{len(samples)} 通过")
    return 0 if failures == 0 and len(cases) >= 10 else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true", help="运行自测样本")
    ap.add_argument("--list", action="store_true", help="列出场景卡")
    ap.add_argument("--score", metavar="EVAL_ID", help="评分单张卡")
    ap.add_argument("--response", metavar="FILE", help="被测响应文本")
    ap.add_argument("--all", action="store_true", help="批量评分")
    ap.add_argument("--responses-dir", metavar="DIR", help="响应目录（<eval_id>.txt）")
    args = ap.parse_args()

    cases = load_cases()
    if not cases:
        print(f"未找到场景卡：{CASES_DIR}", file=sys.stderr)
        return 2

    if args.selftest:
        return cmd_selftest(cases)
    if args.list:
        return cmd_list(cases)
    if args.score:
        if not args.response:
            print("--score 需要 --response", file=sys.stderr)
            return 2
        return cmd_score(cases, args.score, args.response)
    if args.all:
        if not args.responses_dir:
            print("--all 需要 --responses-dir", file=sys.stderr)
            return 2
        return cmd_all(cases, args.responses_dir)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
