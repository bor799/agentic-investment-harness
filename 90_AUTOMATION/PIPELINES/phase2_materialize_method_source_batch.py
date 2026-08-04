from __future__ import annotations

import csv
import shutil
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATE = "2026-07-24"
PLAN = "分析报告/archive/260723系统_Murphy投资系统工程重构方案.md"
BACKLOG = ROOT / "05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.csv"
METHOD_QUEUE = ROOT / "02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE"
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
    dest = METHOD_QUEUE / source_rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return {
        "source": source_rel,
        "mirror": str(dest.relative_to(ROOT)),
        "title": read_title(src),
        "primary_role": row["primary_role"],
        "migration_target": row["migration_target"],
    }


def table(rows: list[dict[str, str]]) -> str:
    return "\n".join(
        f"| [[{row['mirror']}]] | [[{row['source']}]] | {row['title']} | `{row['primary_role']}` | `{row['migration_target']}` |"
        for row in rows
    )


def main() -> None:
    rows = [
        copy_row(row)
        for row in read_rows()
        if row["next_action"] == "merge_relevant_rules_into_canonical_skill_then_archive_source"
    ]
    METHOD_QUEUE.mkdir(parents=True, exist_ok=True)
    (ROOT / "02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE_INDEX.md").write_text(
        f"""---
title: method_source_review_queue_index
date: {DATE}
updated: {DATE}
layer: METHOD
primary_role: method_source_review_queue_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - {PLAN}
  - 05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.md
---

# Method Source Review Queue Index

## 先说人话

**今天发生了什么：**44 个旧方法来源已镜像进入 Method Source Review Queue。

**为什么重要：**这些文件是旧方法正文的来源，不应继续散落在旧结构里；但复制入队不等于已经逐段合并进 canonical Skill。

**现在做什么：**后续逐个抽取规则、反例、适用范围和失败条件，再写入对应 Skill；未合并前，旧方法只作来源。

| 镜像副本 | 原始路径 | 标题 | 旧角色 | 目标 |
|---|---|---|---|---|
{table(rows)}

## 边界

- Review Queue 不等于 canonical Skill。
- 旧方法中的旧参数、旧评分、旧自动晋升逻辑不能直接恢复。
- 合并时必须写清：输入、输出、不能证明什么、失败条件和来源回链。
""",
        encoding="utf-8",
    )

    roles = Counter(row["primary_role"] for row in rows)
    role_rows = "\n".join(f"| `{role}` | {count} |" for role, count in sorted(roles.items()))
    targets = Counter(row["migration_target"] for row in rows)
    target_rows = "\n".join(f"| `{target}` | {count} |" for target, count in sorted(targets.items()))
    (REPORT_DIR / "PHYSICAL_MIGRATION_BATCH5_REPORT.md").write_text(
        f"""---
title: physical_migration_batch5_report
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

# Physical Migration Batch 5 Report

## 先说人话

**今天发生了什么：**执行第五批可逆物理迁移：44 个旧方法来源已镜像到 Method Source Review Queue。

**为什么重要：**至此 backlog 中 611 个旧 Markdown 都已有新结构接入点；但旧方法全文合并仍未完成，需要逐段吸收。

**现在做什么：**下一步应按 canonical Skill 分组做全文合并和回执，不再新增孤立方法页。

| 批次 | 数量 | 索引 |
|---|---:|---|
| Method Source Review Queue | {len(rows)} | [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE_INDEX]] |

## 按旧角色

| 旧角色 | 数量 |
|---|---:|
{role_rows}

## 按目标

| 目标 | 数量 |
|---|---:|
{target_rows}

## 边界

- 本批次只完成可逆物理接入，不代表方法正文合并完成。
- 合并前旧方法仍为 `decision_authority: none` 或来源材料。
- 旧方法进入 canonical Skill 后必须保留来源回链和失败条件。
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
