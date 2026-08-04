from __future__ import annotations

import csv
import shutil
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATE = "2026-07-24"
PLAN = "分析报告/archive/260723系统_Murphy投资系统工程重构方案.md"
BACKLOG = ROOT / "05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.csv"
HYPOTHESIS_MIRROR = ROOT / "03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE"
WATCHLIST_MIRROR = ROOT / "03_STATE/WATCHLISTS/MIRRORED_LEGACY_WATCHLISTS"
AUTOMATION_STATE_MIRROR = ROOT / "03_STATE/AUTOMATION_STATE/MIRRORED_LEGACY_RUNTIME"
SCORECARD_MIRROR = ROOT / "05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/MIRRORED_LEGACY_SCORECARDS"
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
        "status": row["status"],
    }


def materialize(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    batches = {
        "hypothesis_state": [],
        "watchlist_state": [],
        "automation_state": [],
        "scorecards": [],
    }
    for row in rows:
        if row["next_action"] == "snapshot_into_state_archive_or_watchlist_then_expire_legacy":
            target = row["migration_target"]
            if target.startswith("03_STATE/HYPOTHESIS_QUEUE"):
                batches["hypothesis_state"].append(copy_row(row, HYPOTHESIS_MIRROR))
            elif target.startswith("03_STATE/WATCHLISTS"):
                batches["watchlist_state"].append(copy_row(row, WATCHLIST_MIRROR))
            elif "AUTOMATION" in target:
                batches["automation_state"].append(copy_row(row, AUTOMATION_STATE_MIRROR))
        elif row["primary_role"] == "legacy_scorecard":
            batches["scorecards"].append(copy_row(row, SCORECARD_MIRROR))
    return batches


def table(rows: list[dict[str, str]]) -> str:
    return "\n".join(
        f"| [[{row['mirror']}]] | [[{row['source']}]] | {row['title']} | `{row['primary_role']}` |"
        for row in rows
    )


def write_index(path: Path, title: str, primary_role: str, intro: str, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""---
title: {title}
date: {DATE}
updated: {DATE}
layer: STATE
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

| 镜像副本 | 原始路径 | 标题 | 旧角色 |
|---|---|---|---|
{table(rows)}
""",
        encoding="utf-8",
    )


def write_outputs(batches: dict[str, list[dict[str, str]]]) -> None:
    write_index(
        ROOT / "03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE_INDEX.md",
        "mirrored_legacy_hypothesis_state_index",
        "mirrored_legacy_hypothesis_state_index",
        "**今天发生了什么：**旧公司研究任务、next questions 和 next signals 已镜像进入 Hypothesis Queue。\n\n**为什么重要：**这些是短寿命研究队列，不是公司长期结论；镜像后仍需要刷新、过期或结算。\n\n**现在做什么：**需要继续研究某公司时，先看新问题索引，再决定是否把旧问题转成当前待验证假设。",
        batches["hypothesis_state"],
    )
    write_index(
        ROOT / "03_STATE/WATCHLISTS/MIRRORED_LEGACY_WATCHLISTS_INDEX.md",
        "mirrored_legacy_watchlists_index",
        "mirrored_legacy_watchlists_index",
        "**今天发生了什么：**旧投资池已镜像进入 Watchlists。\n\n**为什么重要：**旧池子只说明历史关注顺序，不授权今天买入或加仓。\n\n**现在做什么：**重新使用前必须补 `data_cutoff / expires_at / refresh_trigger`。",
        batches["watchlist_state"],
    )
    write_index(
        ROOT / "03_STATE/AUTOMATION_STATE/MIRRORED_LEGACY_RUNTIME_INDEX.md",
        "mirrored_legacy_runtime_state_index",
        "mirrored_legacy_runtime_state_index",
        "**今天发生了什么：**旧自动化运行态 Markdown 已镜像进入 Automation State。\n\n**为什么重要：**运行态是过程记录，不是研究结论；它只能解释自动化当时如何运行。\n\n**现在做什么：**后续运行自动化时使用 `90_AUTOMATION/RUNTIME` 的当前入口。",
        batches["automation_state"],
    )

    score_index = ROOT / "05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/MIRRORED_LEGACY_SCORECARDS_INDEX.md"
    score_index.parent.mkdir(parents=True, exist_ok=True)
    score_index.write_text(
        f"""---
title: mirrored_legacy_scorecards_index
date: {DATE}
updated: {DATE}
layer: META
primary_role: mirrored_legacy_scorecards_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - {PLAN}
  - 05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.md
---

# Mirrored Legacy Scorecards Index

## 先说人话

**今天发生了什么：**旧 `/70` scorecard 已镜像进入 Superseded State Archive。

**为什么重要：**旧评分可以帮助复盘历史自动化怎么排序，但不能再给今天的仓位、买入或胜率背书。

**现在做什么：**若需要用旧 scorecard，只能当历史状态或错误校准样本；新的研究必须走四票、期限合同和 Case 结算。

| 镜像副本 | 原始路径 | 标题 | 旧角色 |
|---|---|---|---|
{table(batches['scorecards'])}
""",
        encoding="utf-8",
    )

    counts = {key: len(value) for key, value in batches.items()}
    roles = Counter(row["primary_role"] for rows in batches.values() for row in rows)
    role_rows = "\n".join(f"| `{role}` | {count} |" for role, count in sorted(roles.items()))
    (REPORT_DIR / "PHYSICAL_MIGRATION_BATCH2_REPORT.md").write_text(
        f"""---
title: physical_migration_batch2_report
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

# Physical Migration Batch 2 Report

## 先说人话

**今天发生了什么：**执行第二批可逆物理迁移：旧 Hypothesis Queue、Watchlists、Automation State 和 `/70` scorecard 已镜像到新结构。

**为什么重要：**这些文件最容易被误读为“当前排序”或“当前任务”。镜像后它们留作历史 State，不再拥有当前决策权限。

**现在做什么：**后续继续迁移公司 Evidence 和方法正文；本批次只证明 State/scorecard 镜像完成。

| 批次 | 数量 | 索引 |
|---|---:|---|
| Hypothesis Queue 镜像 | {counts['hypothesis_state']} | [[03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE_INDEX]] |
| Watchlists 镜像 | {counts['watchlist_state']} | [[03_STATE/WATCHLISTS/MIRRORED_LEGACY_WATCHLISTS_INDEX]] |
| Automation State 镜像 | {counts['automation_state']} | [[03_STATE/AUTOMATION_STATE/MIRRORED_LEGACY_RUNTIME_INDEX]] |
| Scorecards 镜像 | {counts['scorecards']} | [[05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/MIRRORED_LEGACY_SCORECARDS_INDEX]] |

## 按旧角色

| 旧角色 | 数量 |
|---|---:|
{role_rows}

## 边界

- 本批次不改写旧文件，也不删除旧文件。
- Scorecard 镜像仍为旧评分历史，不得用于当前交易授权。
- 所有 State 镜像重新启用前，必须补 `data_cutoff / expires_at / refresh_trigger`。
""",
        encoding="utf-8",
    )


def main() -> None:
    batches = materialize(read_rows())
    write_outputs(batches)


if __name__ == "__main__":
    main()
