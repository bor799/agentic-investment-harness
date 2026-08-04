from __future__ import annotations

import csv
import shutil
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATE = "2026-07-24"
PLAN = "分析报告/archive/260723系统_Murphy投资系统工程重构方案.md"
BACKLOG = ROOT / "05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.csv"
GOVERNANCE_MIRROR = ROOT / "05_EVIDENCE_META/META/MIRRORED_LEGACY_GOVERNANCE"
AUTOMATION_REVIEW = ROOT / "90_AUTOMATION/PROMPTS/REVIEW_QUEUE"
CURRENT_CANDIDATES = ROOT / "90_AUTOMATION/PROMPTS/CURRENT_CANDIDATES"
REPORT_DIR = ROOT / "05_EVIDENCE_META/META"


def read_rows() -> list[dict[str, str]]:
    with BACKLOG.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def read_title(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                if line.startswith("title:"):
                    return line.split(":", 1)[1].strip().strip('"')
            text = text[end + 4 :]
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def copy_row(row: dict[str, str], base: Path) -> dict[str, str]:
    source_rel = row["path"]
    src = ROOT / source_rel
    dest = base / source_rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return {
        "source": source_rel,
        "mirror": str(dest.relative_to(ROOT)),
        "title": read_title(src),
        "primary_role": row["primary_role"],
        "next_action": row["next_action"],
        "migration_target": row["migration_target"],
    }


def materialize(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    governance: list[dict[str, str]] = []
    review: list[dict[str, str]] = []
    current_candidates: list[dict[str, str]] = []
    for row in rows:
        if row["next_action"] == "keep_as_governance_history_or_superseded_state" and row["primary_role"] != "legacy_scorecard":
            governance.append(copy_row(row, GOVERNANCE_MIRROR))
        elif row["next_action"] == "review_before_move":
            review.append(copy_row(row, AUTOMATION_REVIEW))
        elif row["next_action"] == "promote_or_copy_current_runtime_after_manual_check":
            current_candidates.append(copy_row(row, CURRENT_CANDIDATES))
    return {"governance": governance, "review": review, "current_candidates": current_candidates}


def table(rows: list[dict[str, str]]) -> str:
    return "\n".join(
        f"| [[{row['mirror']}]] | [[{row['source']}]] | {row['title']} | `{row['primary_role']}` | `{row['next_action']}` |"
        for row in rows
    )


def write_index(path: Path, title: str, layer: str, primary_role: str, intro: str, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""---
title: {title}
date: {DATE}
updated: {DATE}
layer: {layer}
primary_role: {primary_role}
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - {PLAN}
  - 05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.md
---

# {title}

## 先说人话

{intro}

| 镜像副本 | 原始路径 | 标题 | 旧角色 | backlog 动作 |
|---|---|---|---|---|
{table(rows)}
""",
        encoding="utf-8",
    )


def write_outputs(batches: dict[str, list[dict[str, str]]]) -> None:
    write_index(
        ROOT / "05_EVIDENCE_META/META/MIRRORED_LEGACY_GOVERNANCE_INDEX.md",
        "mirrored_legacy_governance_index",
        "META",
        "mirrored_legacy_governance_index",
        "**今天发生了什么：**旧首页、旧认知模型、旧审计表和重构方案已镜像进入 Meta 治理历史区。\n\n**为什么重要：**这些文件可能包含旧权限词和历史 AI 判断；镜像后只能作为治理来源，不拥有当前 Constitution、MINDSET 或交易权限。\n\n**现在做什么：**需要追溯系统演化时查这里；当前入口仍是 `00_HOME/HOME.md`。",
        batches["governance"],
    )
    write_index(
        ROOT / "90_AUTOMATION/PROMPTS/AUTOMATION_REVIEW_QUEUE_INDEX.md",
        "automation_review_queue_index",
        "AUTOMATION",
        "automation_review_queue_index",
        "**今天发生了什么：**`review_before_move` 的旧 prompt、旧命令和历史自动化设计已复制进 Automation Review Queue。\n\n**为什么重要：**这些材料可能有可复用片段，但没有经过当前边界审查，不能直接当当前可执行 prompt。\n\n**现在做什么：**后续逐个判断：保留为 canonical、合并、归档，或只作为历史样本。",
        batches["review"],
    )
    write_index(
        ROOT / "90_AUTOMATION/PROMPTS/CURRENT_CANDIDATES_INDEX.md",
        "current_automation_candidates_index",
        "AUTOMATION",
        "current_automation_candidates_index",
        "**今天发生了什么：**两个当前 Claude 自动化候选已复制到 Current Candidates。\n\n**为什么重要：**它们可能仍是当前工具入口，但仍需核对边界和与 `90_AUTOMATION` canonical 说明是否一致。\n\n**现在做什么：**核验通过前，只把它们当候选副本；真正执行仍以原工具要求位置为准。",
        batches["current_candidates"],
    )

    all_rows = batches["governance"] + batches["review"] + batches["current_candidates"]
    roles = Counter(row["primary_role"] for row in all_rows)
    role_rows = "\n".join(f"| `{role}` | {count} |" for role, count in sorted(roles.items()))
    (REPORT_DIR / "PHYSICAL_MIGRATION_BATCH4_REPORT.md").write_text(
        f"""---
title: physical_migration_batch4_report
date: {DATE}
updated: {DATE}
layer: META
primary_role: physical_migration_batch_report
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - {PLAN}
  - 05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.md
---

# Physical Migration Batch 4 Report

## 先说人话

**今天发生了什么：**执行第四批可逆物理迁移：治理历史镜像、自动化 review queue 和当前自动化候选副本已接入新结构。

**为什么重要：**这一步处理的是最容易误升权的材料：旧认知模型、旧审计表、旧 prompt 和旧命令。它们现在有明确位置，但仍没有当前交易权限。

**现在做什么：**后续继续处理方法正文全文合并、Case 结算和吸收回执；自动化 review queue 需要逐项审查后才能晋升 canonical。

| 批次 | 数量 | 索引 |
|---|---:|---|
| 治理历史镜像 | {len(batches['governance'])} | [[05_EVIDENCE_META/META/MIRRORED_LEGACY_GOVERNANCE_INDEX]] |
| 自动化 Review Queue | {len(batches['review'])} | [[90_AUTOMATION/PROMPTS/AUTOMATION_REVIEW_QUEUE_INDEX]] |
| 当前自动化候选 | {len(batches['current_candidates'])} | [[90_AUTOMATION/PROMPTS/CURRENT_CANDIDATES_INDEX]] |

## 按旧角色

| 旧角色 | 数量 |
|---|---:|
{role_rows}

## 边界

- Review Queue 不等于当前有效 prompt。
- Current Candidates 仍需手工边界核验。
- 治理历史镜像不进入 MINDSET / Constitution。
""",
        encoding="utf-8",
    )


def main() -> None:
    write_outputs(materialize(read_rows()))


if __name__ == "__main__":
    main()
