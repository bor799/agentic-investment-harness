from __future__ import annotations

import csv
import shutil
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATE = "2026-07-24"
PLAN = "分析报告/archive/260723系统_Murphy投资系统工程重构方案.md"
BACKLOG = ROOT / "05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.csv"
COMPANY_MIRROR = ROOT / "05_EVIDENCE_META/EVIDENCE/COMPANIES/MIRRORED_LEGACY_EVIDENCE"
THEME_MIRROR = ROOT / "05_EVIDENCE_META/EVIDENCE/THEMES/MIRRORED_LEGACY_EVIDENCE"
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
        "migration_target": row["migration_target"],
    }


def materialize(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    company: list[dict[str, str]] = []
    theme: list[dict[str, str]] = []
    for row in rows:
        if row["next_action"] != "attach_to_company_or_theme_dossier_without_rewriting_thesis":
            continue
        target = row["migration_target"]
        if target.startswith("05_EVIDENCE_META/EVIDENCE/COMPANIES"):
            company.append(copy_row(row, COMPANY_MIRROR))
        elif target.startswith("05_EVIDENCE_META/EVIDENCE/THEMES"):
            theme.append(copy_row(row, THEME_MIRROR))
    return {"company": company, "theme": theme}


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
layer: EVIDENCE
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
        ROOT / "05_EVIDENCE_META/EVIDENCE/COMPANIES/MIRRORED_LEGACY_COMPANY_EVIDENCE_INDEX.md",
        "mirrored_legacy_company_evidence_index",
        "mirrored_legacy_company_evidence_index",
        "**今天发生了什么：**旧公司/标的 Evidence 已镜像复制到新 Evidence 层。\n\n**为什么重要：**这些文件保存公司研究、证据日志和旧 router 原文；镜像后仍只是证据来源，不是当前买卖结论。\n\n**现在做什么：**需要研究单一标的时，先从公司 dossier 进入，再引用镜像原文。",
        batches["company"],
    )
    write_index(
        ROOT / "05_EVIDENCE_META/EVIDENCE/THEMES/MIRRORED_LEGACY_THEME_EVIDENCE_INDEX.md",
        "mirrored_legacy_theme_evidence_index",
        "mirrored_legacy_theme_evidence_index",
        "**今天发生了什么：**旧主题/分析 Evidence 已镜像复制到新 Evidence 层。\n\n**为什么重要：**主题报告可能混有事实、方法和当时 State；镜像只保留证据线索，不授权当前判断。\n\n**现在做什么：**进入专题分析前，先萃取新增事实、证据链、失败条件和待验证信号。",
        batches["theme"],
    )

    roles = Counter(row["primary_role"] for rows in batches.values() for row in rows)
    role_rows = "\n".join(f"| `{role}` | {count} |" for role, count in sorted(roles.items()))
    target_rows = "\n".join(
        f"| `{target}` | {count} |"
        for target, count in sorted(Counter(row["migration_target"] for rows in batches.values() for row in rows).items())
    )
    (REPORT_DIR / "PHYSICAL_MIGRATION_BATCH3_REPORT.md").write_text(
        f"""---
title: physical_migration_batch3_report
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

# Physical Migration Batch 3 Report

## 先说人话

**今天发生了什么：**执行第三批可逆物理迁移：旧公司/标的 Evidence 与主题 Evidence 已镜像到新 Evidence 层。

**为什么重要：**这是旧库最大的证据块。镜像后，研究可以从新结构进入并追溯旧原文，但旧文件仍不拥有当前交易权限。

**现在做什么：**后续继续迁移方法正文、自动化 prompts 和历史治理材料；本批次只证明 Evidence 镜像完成。

| 批次 | 数量 | 索引 |
|---|---:|---|
| 公司/标的 Evidence 镜像 | {len(batches['company'])} | [[05_EVIDENCE_META/EVIDENCE/COMPANIES/MIRRORED_LEGACY_COMPANY_EVIDENCE_INDEX]] |
| 主题 Evidence 镜像 | {len(batches['theme'])} | [[05_EVIDENCE_META/EVIDENCE/THEMES/MIRRORED_LEGACY_THEME_EVIDENCE_INDEX]] |

## 按旧角色

| 旧角色 | 数量 |
|---|---:|
{role_rows}

## 按迁移目标

| 迁移目标 | 数量 |
|---|---:|
{target_rows}

## 边界

- 本批次复制旧原文，不删除、不移动旧文件。
- 镜像 Evidence 仍是 `decision_authority: none`。
- 旧研究结论重新进入正文前，必须按当前决策合同萃取证据链、失败条件和待验证信号。
""",
        encoding="utf-8",
    )


def main() -> None:
    batches = materialize(read_rows())
    write_outputs(batches)


if __name__ == "__main__":
    main()
