from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from phase2_patch_legacy_frontmatter import DATE, PLAN, SKIP_TOP_METADATA, classify, legacy_files


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"')
    return values


def next_action(layer: str, primary_role: str, status: str) -> str:
    if status == "active" and layer == "AUTOMATION":
        return "promote_or_copy_current_runtime_after_manual_check"
    if layer == "METHOD":
        return "merge_relevant_rules_into_canonical_skill_then_archive_source"
    if layer == "STATE":
        return "snapshot_into_state_archive_or_watchlist_then_expire_legacy"
    if layer == "CASE":
        return "extract_case_card_then_keep_source_as_evidence"
    if primary_role.endswith("ai_long_report"):
        return "copy_to_ai_long_report_archive_with_backlink"
    if layer == "EVIDENCE":
        return "attach_to_company_or_theme_dossier_without_rewriting_thesis"
    if layer == "META":
        return "keep_as_governance_history_or_superseded_state"
    return "review_before_move"


def deletion_flag(path: Path, primary_role: str) -> str:
    rel = str(path.relative_to(ROOT))
    if path.name == ".DS_Store":
        return "X?"
    if "merged_sources/2026-06-06/" in rel and "结构窗口与财务窗口判断" in path.name:
        return "X?_semantic_diff_required"
    if rel.endswith(("Hang Seng Tech Index/next_questions.md", "TQQQ/next_questions.md", "Hang Seng Tech Index/scorecard.md", "TQQQ/scorecard.md")):
        return "X?_directory_ownership_required"
    if primary_role in {"legacy_ai_long_report", "legacy_company_evidence", "legacy_analysis_evidence", "legacy_company_case_source"}:
        return "never_auto_delete"
    return "not_reviewed_for_deletion"


def main() -> None:
    rows = []
    skipped = []
    for path in legacy_files():
        rel = str(path.relative_to(ROOT))
        if rel in SKIP_TOP_METADATA:
            skipped.append(rel)
            continue
        fm = parse_frontmatter(path)
        meta = classify(path)
        layer = fm.get("layer") or meta["layer"]
        role = fm.get("primary_role") or meta["primary_role"]
        status = fm.get("status") or meta["status"]
        authority = fm.get("decision_authority") or meta["decision_authority"]
        target = fm.get("migration_target") or meta["target"]
        rows.append(
            {
                "path": rel,
                "layer": layer,
                "primary_role": role,
                "status": status,
                "decision_authority": authority,
                "migration_target": target,
                "next_action": next_action(layer, role, status),
                "deletion_flag": deletion_flag(path, role),
            }
        )

    rows.sort(key=lambda r: (r["layer"], r["migration_target"], r["path"]))
    report_dir = ROOT / "05_EVIDENCE_META/META"
    report_dir.mkdir(parents=True, exist_ok=True)
    csv_path = report_dir / "PHYSICAL_MIGRATION_BACKLOG.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "path",
                "layer",
                "primary_role",
                "status",
                "decision_authority",
                "migration_target",
                "next_action",
                "deletion_flag",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    by_layer = Counter(r["layer"] for r in rows)
    by_action = Counter(r["next_action"] for r in rows)
    by_delete = Counter(r["deletion_flag"] for r in rows)

    def table(counter: Counter[str]) -> str:
        return "\n".join(f"| `{key}` | {counter[key]} |" for key in sorted(counter))

    report = f"""---
title: physical_migration_backlog
date: {DATE}
updated: {DATE}
layer: META
primary_role: physical_migration_backlog
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - {PLAN}
  - 05_EVIDENCE_META/META/LEGACY_FRONTMATTER_NORMALIZATION_REPORT.md
---

# Physical Migration Backlog

## 先说人话

**今天发生了什么：**旧结构文件已进入物理迁移 backlog；本文件只排队，不移动、不删除。

**为什么重要：**后续搬文件必须先知道每个旧文件应该去 Evidence、State、Case、Method 还是 Automation；否则最容易把历史材料误当当前判断。

**现在做什么：**继续把旧结构当只读来源；真正移动前，按 `next_action` 逐批执行，并保留原路径回链。

## 总览

| 指标 | 数量 |
|---|---:|
| backlog 文件 | {len(rows)} |
| 特殊跳过 | {len(skipped)} |

CSV 明细：[[05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.csv]]

## 按层级

| layer | 数量 |
|---|---:|
{table(by_layer)}

## 按下一动作

| next_action | 数量 |
|---|---:|
{table(by_action)}

## 按删除标记

| deletion_flag | 数量 |
|---|---:|
{table(by_delete)}

## 只读冻结规则

1. 旧结构文件默认只读，允许补 metadata、链接回链和迁移标记，不把旧文件继续当当前前台维护。
2. 物理搬迁时优先复制/抽取到新结构，再把旧路径改为 redirect 或 archive pointer。
3. `never_auto_delete` 不能自动删除；它们包括 AI 长报告、公司证据、分析原文和 Case 来源。
4. `X?` 只能表示删除候选，不是删除授权。
5. `decision_authority: none` 的旧文件不得直接授权交易、仓位、MINDSET 或 Constitution。
"""
    (report_dir / "PHYSICAL_MIGRATION_BACKLOG.md").write_text(report, encoding="utf-8")


if __name__ == "__main__":
    main()
