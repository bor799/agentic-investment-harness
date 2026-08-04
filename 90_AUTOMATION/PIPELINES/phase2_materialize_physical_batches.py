from __future__ import annotations

import csv
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATE = "2026-07-24"
PLAN = "分析报告/archive/260723系统_Murphy投资系统工程重构方案.md"
BACKLOG = ROOT / "05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.csv"
AI_ARCHIVE = ROOT / "05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS"
AI_MIRROR = AI_ARCHIVE / "MIRRORED_SOURCES"
CASE_DIR = ROOT / "04_CASE_GYM/RESEARCH_CASES"
REPORT_DIR = ROOT / "05_EVIDENCE_META/META"


def quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def read_rows() -> list[dict[str, str]]:
    with BACKLOG.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def slug(value: str) -> str:
    value = value.replace("&", "and")
    value = re.sub(r"[\\/:*?\"<>|#\[\]]+", "_", value)
    value = re.sub(r"\s+", "_", value)
    value = value.strip("._ ")
    return value or "untitled"


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


def mirror_ai_long_reports(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    mirrored = []
    for row in rows:
        if row["next_action"] != "copy_to_ai_long_report_archive_with_backlink":
            continue
        src_rel = row["path"]
        src = ROOT / src_rel
        dest = AI_MIRROR / src_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        mirrored.append(
            {
                "source": src_rel,
                "archive_copy": str(dest.relative_to(ROOT)),
                "title": read_title(src),
            }
        )
    return mirrored


def case_card_name(source_rel: str) -> str:
    parts = Path(source_rel).parts
    company = "unknown"
    if "实体商" in parts:
        i = parts.index("实体商")
        if i + 1 < len(parts):
            company = parts[i + 1]
    elif "IP 消费类" in parts:
        company = "IP消费"
    return f"260724_{slug(company).lower()}_{slug(Path(source_rel).stem).lower()}_legacy_source_case.md"


def write_case_cards(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    CASE_DIR.mkdir(parents=True, exist_ok=True)
    cards = []
    for row in rows:
        if row["next_action"] != "extract_case_card_then_keep_source_as_evidence":
            continue
        source_rel = row["path"]
        if source_rel == "📈 个人交易手册.md":
            continue
        src = ROOT / source_rel
        title = read_title(src)
        dest = CASE_DIR / case_card_name(source_rel)
        body = f"""---
title: {quote(title + " legacy source case")}
date: {DATE}
updated: {DATE}
layer: CASE
primary_role: migrated_legacy_source_case
status: active
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
case_type: research_or_decision_source
settlement_status: uncalibrated
legacy_path: {quote(source_rel)}
source_paths:
  - {source_rel}
  - {PLAN}
---

# {title} Legacy Source Case

## 先说人话

**今天发生了什么：**旧文件 `{source_rel}` 已抽成 Case Gym 来源卡，原文继续保留在旧路径。

**为什么重要：**这类材料往往混有公司判断、交易方案、情绪反应和方法观察。进入 Case Gym 后，它只能训练方法，不能直接升级成 MINDSET、Constitution 或交易授权。

**现在做什么：**后续复盘时先补齐事前假设、当时价格、验证期限、结算结果和失败条件；未结算前保持 `settlement_status: uncalibrated`。

## Source

| 字段 | 内容 |
|---|---|
| 原始文件 | [[{source_rel}]] |
| 原始标题 | {title} |
| 来源角色 | `{row['primary_role']}` |
| 旧层级 | `{row['layer']}` |
| 原权限 | `{row['decision_authority']}` |

## Case Capture

| 项目 | 当前状态 |
|---|---|
| 事前判断 | 待从原文萃取 |
| 当时价格 / 估值语法 | 待从原文萃取 |
| 核心证据链 | 待从原文萃取 |
| 行为信号 | 待复盘 |
| 验证期限 | 未校准 |
| 结算结果 | 未结算 |
| 可写入位置 | `04_CASE_GYM / 02_术 / METHOD_TESTS` |
| 不可写入位置 | `01_道/MINDSET / 01_道/CONSTITUTION / 当前交易授权` |

## Review Gate

1. 先确认这是实际交易、未成交、研究判断、错过机会还是情绪短记。
2. 再补 `business_horizon / thesis_horizon / execution_horizon / review_date`。
3. 只有形成跨案例稳定反例或方法修正，才允许进入 Skill 更新。
4. 即使形成候选哲学，也只能进入 Philosophy Inbox，不能自动进入 MINDSET。
"""
        dest.write_text(body, encoding="utf-8")
        cards.append({"source": source_rel, "case_card": str(dest.relative_to(ROOT)), "title": title})
    return cards


def write_indexes(mirrored: list[dict[str, str]], cards: list[dict[str, str]]) -> None:
    AI_ARCHIVE.mkdir(parents=True, exist_ok=True)
    ai_rows = "\n".join(
        f"| [[{r['archive_copy']}]] | [[{r['source']}]] | {r['title']} |"
        for r in mirrored
    )
    (AI_ARCHIVE / "MIRRORED_AI_LONG_REPORTS_INDEX.md").write_text(
        f"""---
title: mirrored_ai_long_reports_index
date: {DATE}
updated: {DATE}
layer: EVIDENCE
primary_role: mirrored_ai_long_reports_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - {PLAN}
  - 05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.md
---

# Mirrored AI Long Reports Index

## 先说人话

**今天发生了什么：**AI 长报告原文已镜像复制到 `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/MIRRORED_SOURCES/`。

**为什么重要：**长报告是历史推理底稿和证据线索，不是最终分析正文。镜像复制降低旧路径变动风险，但不提高任何交易权限。

**现在做什么：**需要引用长报告时优先引用镜像副本；进入分析正文前仍要萃取关键逻辑、证据链、失败条件和待验证信号。

| 镜像副本 | 原始路径 | 标题 |
|---|---|---|
{ai_rows}
""",
        encoding="utf-8",
    )

    case_rows = "\n".join(
        f"| [[{r['case_card']}]] | [[{r['source']}]] | {r['title']} |"
        for r in cards
    )
    (CASE_DIR / "MIGRATED_LEGACY_SOURCE_CASES_INDEX.md").write_text(
        f"""---
title: migrated_legacy_source_cases_index
date: {DATE}
updated: {DATE}
layer: CASE
primary_role: migrated_legacy_source_cases_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - {PLAN}
  - 05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.md
---

# Migrated Legacy Source Cases Index

## 先说人话

**今天发生了什么：**旧实体商和 IP 消费材料中带有交易方案、投资决策或情绪反应的来源，已抽成 Case Gym 卡片。

**为什么重要：**这些材料可以训练方法和复盘行为，但不能直接生成长期原则，也不能授权今天交易。

**现在做什么：**后续逐张补齐事前假设、期限、结算结果和方法版本。

| Case 卡 | 原始路径 | 标题 |
|---|---|---|
{case_rows}
""",
        encoding="utf-8",
    )

    report_rows = "\n".join(
        [
            f"| AI 长报告镜像 | {len(mirrored)} | [[05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/MIRRORED_AI_LONG_REPORTS_INDEX]] |",
            f"| Case 来源卡 | {len(cards)} | [[04_CASE_GYM/RESEARCH_CASES/MIGRATED_LEGACY_SOURCE_CASES_INDEX]] |",
        ]
    )
    (REPORT_DIR / "PHYSICAL_MIGRATION_BATCH1_REPORT.md").write_text(
        f"""---
title: physical_migration_batch1_report
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

# Physical Migration Batch 1 Report

## 先说人话

**今天发生了什么：**执行了第一批可逆物理迁移：AI 长报告镜像复制，旧 Case 来源抽成 Case 卡。

**为什么重要：**这一步把最需要保留的长报告和最容易训练方法的旧案例材料接入新结构，同时不删除、不移动旧原文。

**现在做什么：**后续继续按 backlog 迁移公司 Evidence、State Archive 和 canonical Skill；这份报告只证明第一批完成。

| 批次 | 数量 | 索引 |
|---|---:|---|
{report_rows}

## 边界

- 本批次不代表 611 个旧 Markdown 全量物理搬迁完成。
- 镜像副本不提高长报告权限，仍是 `decision_authority: none`。
- Case 来源卡仍是 `settlement_status: uncalibrated`，需要后续复盘结算。
""",
        encoding="utf-8",
    )


def main() -> None:
    rows = read_rows()
    mirrored = mirror_ai_long_reports(rows)
    cards = write_case_cards(rows)
    write_indexes(mirrored, cards)


if __name__ == "__main__":
    main()
