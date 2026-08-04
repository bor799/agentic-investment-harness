from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATE = "2026-07-24"
PLAN = "分析报告/archive/260723系统_Murphy投资系统工程重构方案.md"

LEGACY_ROOTS = [
    "AGENTS.md",
    "我的投资框架：从宏观到企业的系统思考.md",
    "📈 个人交易手册.md",
    "📊 股票投资看板.md",
    ".claude",
    "AI周期探索",
    "交易宪法",
    "分析报告",
    "基础概念",
    "codeex 版本",
]

SKIP_TOP_METADATA = {
    "AGENTS.md",
}


def quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def legacy_files() -> list[Path]:
    files: list[Path] = []
    for item in LEGACY_ROOTS:
        path = ROOT / item
        if path.is_file() and path.suffix == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend([p for p in path.rglob("*.md") if p.is_file()])
    return sorted(set(files), key=lambda p: str(p.relative_to(ROOT)))


def has_frontmatter(path: Path) -> bool:
    return path.read_text(encoding="utf-8", errors="replace").startswith("---")


def classify(path: Path) -> dict[str, str]:
    rel = str(path.relative_to(ROOT))
    name = path.name

    meta = {
        "layer": "EVIDENCE",
        "primary_role": "legacy_evidence",
        "status": "archived",
        "decision_authority": "none",
        "target": "05_EVIDENCE_META/EVIDENCE",
    }

    if rel == "我的投资框架：从宏观到企业的系统思考.md":
        meta.update(layer="METHOD", primary_role="legacy_root_framework", status="superseded", target="02_术/SKILLS + 01_道/PHILOSOPHY_INBOX + 05_EVIDENCE_META/EVIDENCE")
    elif rel == "📈 个人交易手册.md":
        meta.update(layer="CASE", primary_role="legacy_trade_manual", status="superseded", target="03_STATE + 04_CASE_GYM + 02_术")
    elif rel == "📊 股票投资看板.md":
        meta.update(layer="META", primary_role="legacy_home_redirect", status="superseded", target="00_HOME/HOME")
    elif rel.startswith(".claude/"):
        authority = "operational" if "ai-cycle-cross-market-v2" in rel else "none"
        meta.update(layer="AUTOMATION", primary_role="legacy_claude_automation", status="active" if authority == "operational" else "superseded", decision_authority=authority, target="90_AUTOMATION/PROMPTS")
    elif rel.startswith("交易宪法/skills/"):
        meta.update(layer="METHOD", primary_role="legacy_method_source", status="superseded", target="02_术/SKILLS")
    elif rel.startswith("交易宪法/每日投资观察和思考/"):
        meta.update(layer="STATE", primary_role="legacy_daily_state", status="superseded", target="03_STATE")
    elif rel.startswith("交易宪法/"):
        meta.update(layer="META", primary_role="legacy_constitution_meta", status="superseded", target="01_道/_HISTORY + 05_EVIDENCE_META/META")
    elif rel.startswith("AI周期探索/0_总览/"):
        if name.startswith("LOOP_PROMPT") or name.startswith("CLAUDE_CODE_RUN_COMMAND"):
            meta.update(layer="AUTOMATION", primary_role="legacy_prompt_or_command", status="superseded", decision_authority="operational", target="90_AUTOMATION/PROMPTS")
        elif name.endswith((".py", ".sh")):
            meta.update(layer="AUTOMATION", primary_role="legacy_pipeline", status="active", decision_authority="operational", target="90_AUTOMATION/PIPELINES")
        elif "queue" in name or "log" in name or "watchlist" in name or "score" in name:
            meta.update(layer="STATE", primary_role="legacy_automation_state", status="superseded", target="90_AUTOMATION/RUNTIME + 03_STATE")
        else:
            meta.update(layer="METHOD", primary_role="legacy_ai_cycle_method", status="superseded", target="02_术/SKILLS + 90_AUTOMATION")
    elif rel.startswith("AI周期探索/01_赛道研究/"):
        meta.update(layer="EVIDENCE", primary_role="legacy_theme_evidence", status="archived", target="05_EVIDENCE_META/EVIDENCE/THEMES")
    elif rel.startswith("AI周期探索/04_投资池/"):
        meta.update(layer="STATE", primary_role="legacy_watchlist_state", status="superseded", target="03_STATE/WATCHLISTS")
    elif rel.startswith("AI周期探索/02_公司研究/") or rel.startswith("AI周期探索/标的研究/"):
        if name == "PROMPT.md":
            meta.update(layer="AUTOMATION", primary_role="legacy_company_prompt", status="superseded", decision_authority="operational", target="90_AUTOMATION/PROMPTS")
        elif name in {"research_task.md", "next_questions.md", "next_signals.md"}:
            meta.update(layer="STATE", primary_role="legacy_company_question_state", status="superseded", target="03_STATE/HYPOTHESIS_QUEUE")
        elif name == "scorecard.md":
            meta.update(layer="META", primary_role="legacy_scorecard", status="superseded", target="05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE")
        elif "AI长报告原文" in name:
            meta.update(layer="EVIDENCE", primary_role="legacy_ai_long_report", status="archived", target="05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS")
        elif name == "README.md":
            meta.update(layer="EVIDENCE", primary_role="legacy_company_router", status="archived", target="05_EVIDENCE_META/EVIDENCE/COMPANIES")
        else:
            meta.update(layer="EVIDENCE", primary_role="legacy_company_evidence", status="archived", target="05_EVIDENCE_META/EVIDENCE/COMPANIES")
    elif rel.startswith("分析报告/"):
        if "AI长报告原文" in name:
            meta.update(layer="EVIDENCE", primary_role="legacy_ai_long_report", status="archived", target="05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS")
        elif "每日决策简报" in name or "每日假设跟踪" in name or "监控" in name or "基线" in name:
            meta.update(layer="STATE", primary_role="legacy_analysis_state", status="superseded", target="05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE")
        elif "行为纠偏" in name or "资本纪律" in name or "训练" in name or "框架" in name or "体系" in name:
            meta.update(layer="METHOD", primary_role="legacy_analysis_method_source", status="superseded", target="02_术/SKILLS")
        else:
            meta.update(layer="EVIDENCE", primary_role="legacy_analysis_evidence", status="archived", target="05_EVIDENCE_META/EVIDENCE/THEMES")
    elif rel.startswith("基础概念/交易策略组合/"):
        if "期权" in name or "Roll" in name or "波动率" in name:
            meta.update(layer="METHOD", primary_role="legacy_options_method", status="superseded", target="02_术/SKILLS/OPTIONS")
        elif "AI长报告原文" in name:
            meta.update(layer="EVIDENCE", primary_role="legacy_ai_long_report", status="archived", target="05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS")
        else:
            meta.update(layer="METHOD", primary_role="legacy_basic_method_source", status="superseded", target="02_术/SKILLS")
    elif rel.startswith("基础概念/实体商/"):
        if name.endswith(".org"):
            meta.update(layer="EVIDENCE", primary_role="legacy_raw_evidence", status="archived", target="05_EVIDENCE_META/EVIDENCE/COMPANIES")
        elif "投资决策" in name or "交易方案" in name or "未命名" in name:
            meta.update(layer="CASE", primary_role="legacy_company_case_source", status="archived", target="04_CASE_GYM")
        else:
            meta.update(layer="EVIDENCE", primary_role="legacy_company_evidence", status="archived", target="05_EVIDENCE_META/EVIDENCE/COMPANIES")
    elif rel.startswith("基础概念/IP 消费类/"):
        meta.update(layer="CASE", primary_role="legacy_ip_case_source", status="archived", target="04_CASE_GYM + 01_道/PHILOSOPHY_INBOX")
    elif rel.startswith("基础概念/ploymarket/"):
        meta.update(layer="AUTOMATION", primary_role="legacy_ploymarket_automation", status="archived", target="90_AUTOMATION/RUNTIME")
    elif rel.startswith("codeex 版本/"):
        meta.update(layer="AUTOMATION", primary_role="legacy_codex_automation_design", status="archived", target="90_AUTOMATION + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS")

    return meta


def make_frontmatter(path: Path, meta: dict[str, str]) -> str:
    rel = str(path.relative_to(ROOT))
    title = path.stem
    lines = [
        "---",
        f"title: {quote(title)}",
        f"date: {DATE}",
        f"updated: {DATE}",
        f"layer: {meta['layer']}",
        f"primary_role: {meta['primary_role']}",
        f"status: {meta['status']}",
        "authored_by: human_ai",
        "source_type: PX",
        "human_reviewed: false",
        f"decision_authority: {meta['decision_authority']}",
        "legacy_metadata_added: true",
        f"legacy_path: {quote(rel)}",
        f"migration_target: {quote(meta['target'])}",
        "source_paths:",
        f"  - {PLAN}",
        "---",
        "",
    ]
    return "\n".join(lines)


def patch_file(path: Path) -> bool:
    rel = str(path.relative_to(ROOT))
    if rel in SKIP_TOP_METADATA:
        return False
    if has_frontmatter(path):
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    meta = classify(path)
    path.write_text(make_frontmatter(path, meta) + text, encoding="utf-8")
    return True


def main() -> None:
    before = legacy_files()
    patched = []
    skipped = []
    for path in before:
        rel = str(path.relative_to(ROOT))
        if rel in SKIP_TOP_METADATA:
            skipped.append((rel, "special_operational_file"))
            continue
        if has_frontmatter(path):
            continue
        if patch_file(path):
            patched.append(path)

    report_dir = ROOT / "05_EVIDENCE_META/META"
    report_dir.mkdir(parents=True, exist_ok=True)
    csv_path = report_dir / "LEGACY_FRONTMATTER_PATCH_REPORT.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["path", "layer", "primary_role", "status", "decision_authority", "migration_target"])
        for path in patched:
            meta = classify(path)
            writer.writerow([str(path.relative_to(ROOT)), meta["layer"], meta["primary_role"], meta["status"], meta["decision_authority"], meta["target"]])

    total = len(before)
    with_fm = sum(1 for path in before if has_frontmatter(path))
    without = total - with_fm
    report = f"""---
title: legacy_frontmatter_patch_report
date: {DATE}
updated: {DATE}
layer: META
primary_role: legacy_frontmatter_patch_report
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - {PLAN}
---

# Legacy Frontmatter Patch Report

## 先说人话

**今天发生了什么：**旧结构中缺少 YAML frontmatter 的 Markdown 已批量补上 legacy metadata。

**为什么重要：**旧文件即使被搜索到，也会明确显示自己的层级、迁移目标和权限，不会因为旧标题或旧内容获得当前决策授权。

**现在做什么：**后续继续补齐已有 frontmatter 旧文件的字段一致性；`AGENTS.md` 暂不在顶部加 YAML，以免影响 Codex 规则读取。

## 结果

| 指标 | 数量 |
|---|---:|
| 旧结构 Markdown | {total} |
| 已有或已补 frontmatter | {with_fm} |
| 仍无 frontmatter | {without} |
| 本次新增 legacy metadata | {len(patched)} |
| 特殊跳过 | {len(skipped)} |

CSV 明细：[[05_EVIDENCE_META/META/LEGACY_FRONTMATTER_PATCH_REPORT.csv]]

## 跳过原因

| 文件 | 原因 |
|---|---|
""" + "\n".join(f"| `{path}` | `{reason}` |" for path, reason in skipped) + "\n"
    (report_dir / "LEGACY_FRONTMATTER_PATCH_REPORT.md").write_text(report, encoding="utf-8")


if __name__ == "__main__":
    main()
