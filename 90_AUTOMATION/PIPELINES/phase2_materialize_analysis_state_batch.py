from __future__ import annotations

import csv
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATE = "2026-07-24"
PLAN = "分析报告/archive/260723系统_Murphy投资系统工程重构方案.md"
BACKLOG = ROOT / "05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.csv"
STATE_MIRROR = ROOT / "05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/MIRRORED_LEGACY_ANALYSIS_STATE"
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


def copy_row(row: dict[str, str]) -> dict[str, str]:
    source_rel = row["path"]
    src = ROOT / source_rel
    dest = STATE_MIRROR / source_rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return {"source": source_rel, "mirror": str(dest.relative_to(ROOT)), "title": read_title(src)}


def table(rows: list[dict[str, str]]) -> str:
    return "\n".join(f"| [[{row['mirror']}]] | [[{row['source']}]] | {row['title']} |" for row in rows)


def main() -> None:
    rows = [
        copy_row(row)
        for row in read_rows()
        if row["next_action"] == "snapshot_into_state_archive_or_watchlist_then_expire_legacy"
        and row["primary_role"] == "legacy_analysis_state"
        and row["migration_target"].startswith("05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE")
    ]
    index = ROOT / "05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/MIRRORED_LEGACY_ANALYSIS_STATE_INDEX.md"
    index.write_text(
        f"""---
title: mirrored_legacy_analysis_state_index
date: {DATE}
updated: {DATE}
layer: META
primary_role: mirrored_legacy_analysis_state_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - {PLAN}
  - 05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.md
---

# Mirrored Legacy Analysis State Index

## 先说人话

**今天发生了什么：**旧每日假设跟踪、每日决策简报和组合基线已镜像进入 Superseded State Archive。

**为什么重要：**这些文件是当时状态，不是长期方法或当前结论；镜像后保留历史，但不授权今天交易。

**现在做什么：**引用它们时必须写明 data cutoff；若要重新启用，需要重新刷新事实和价格。

| 镜像副本 | 原始路径 | 标题 |
|---|---|---|
{table(rows)}
""",
        encoding="utf-8",
    )
    (REPORT_DIR / "PHYSICAL_MIGRATION_BATCH6_REPORT.md").write_text(
        f"""---
title: physical_migration_batch6_report
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

# Physical Migration Batch 6 Report

## 先说人话

**今天发生了什么：**执行第六批可逆物理迁移：41 个旧分析 State 已镜像到 Superseded State Archive。

**为什么重要：**这批文件包含每日判断和过期假设，最需要和当前 State 分开。

**现在做什么：**后续只剩方法全文合并、Case 结算、吸收回执和旧内链重写等非简单镜像工作。

| 批次 | 数量 | 索引 |
|---|---:|---|
| Analysis State 镜像 | {len(rows)} | [[05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/MIRRORED_LEGACY_ANALYSIS_STATE_INDEX]] |

## 边界

- 本批次不删除旧日报和旧假设跟踪。
- 镜像 State 不等于当前 State。
- 重新使用前必须刷新事实、价格和失效条件。
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
