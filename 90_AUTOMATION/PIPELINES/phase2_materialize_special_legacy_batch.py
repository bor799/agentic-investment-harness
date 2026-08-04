from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATE = "2026-07-24"
PLAN = "分析报告/archive/260723系统_Murphy投资系统工程重构方案.md"

TRADE_MANUAL_SRC = ROOT / "📈 个人交易手册.md"
DAILY_STATE_SRC = ROOT / "交易宪法/每日投资观察和思考/2026-07-22.md"
TRADE_MANUAL_DEST = ROOT / "04_CASE_GYM/TRADE_LOG/MIRRORED_LEGACY_TRADE_MANUAL/📈 个人交易手册.md"
DAILY_STATE_DEST = ROOT / "03_STATE/MARKET_STATE/MIRRORED_LEGACY_DAILY_STATE/交易宪法/每日投资观察和思考/2026-07-22.md"


def copy(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


def main() -> None:
    copy(TRADE_MANUAL_SRC, TRADE_MANUAL_DEST)
    copy(DAILY_STATE_SRC, DAILY_STATE_DEST)

    (ROOT / "04_CASE_GYM/TRADE_LOG/MIRRORED_LEGACY_TRADE_MANUAL_INDEX.md").write_text(
        f"""---
title: mirrored_legacy_trade_manual_index
date: {DATE}
updated: {DATE}
layer: CASE
primary_role: mirrored_legacy_trade_manual_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - {PLAN}
  - 📈 个人交易手册.md
---

# Mirrored Legacy Trade Manual Index

## 先说人话

**今天发生了什么：**旧个人交易手册全文已镜像进入 Case Gym。

**为什么重要：**手册里的 6 个核心样本已经拆成标准 Case；全文镜像用于追溯原始上下文，不再作为当前交易手册。

**现在做什么：**复盘具体样本时优先看标准 Case；需要查旧上下文时再看全文镜像。

| 镜像副本 | 原始路径 | 说明 |
|---|---|---|
| [[04_CASE_GYM/TRADE_LOG/MIRRORED_LEGACY_TRADE_MANUAL/📈 个人交易手册.md]] | [[📈 个人交易手册.md]] | 旧交易手册全文镜像 |
""",
        encoding="utf-8",
    )

    (ROOT / "03_STATE/MARKET_STATE/MIRRORED_LEGACY_DAILY_STATE_INDEX.md").write_text(
        f"""---
title: mirrored_legacy_daily_state_index
date: {DATE}
updated: {DATE}
layer: STATE
primary_role: mirrored_legacy_daily_state_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - {PLAN}
  - 交易宪法/每日投资观察和思考/2026-07-22.md
---

# Mirrored Legacy Daily State Index

## 先说人话

**今天发生了什么：**旧每日投资观察已镜像进入 Market State 历史区。

**为什么重要：**日报是短寿命状态和候选思考，不是长期方法或当前结论。

**现在做什么：**引用时必须保留日期和 data cutoff；重新使用前要刷新事实。

| 镜像副本 | 原始路径 | 说明 |
|---|---|---|
| [[03_STATE/MARKET_STATE/MIRRORED_LEGACY_DAILY_STATE/交易宪法/每日投资观察和思考/2026-07-22.md]] | [[交易宪法/每日投资观察和思考/2026-07-22.md]] | 旧 2026-07-22 日报全文镜像 |
""",
        encoding="utf-8",
    )

    (ROOT / "05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BATCH7_REPORT.md").write_text(
        f"""---
title: physical_migration_batch7_report
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
---

# Physical Migration Batch 7 Report

## 先说人话

**今天发生了什么：**执行第七批可逆物理迁移：旧个人交易手册全文和旧每日投资观察已镜像到新结构。

**为什么重要：**这两个文件是 backlog 里的特殊项，一个已被拆成 Case，一个是单日日报；补全文镜像后，611 个旧 Markdown 都有新结构接入点。

**现在做什么：**后续不再靠物理镜像推进，而要做旧方法全文合并、Case 结算、吸收回执和旧内链重写。

| 批次 | 数量 | 索引 |
|---|---:|---|
| 旧个人交易手册全文镜像 | 1 | [[04_CASE_GYM/TRADE_LOG/MIRRORED_LEGACY_TRADE_MANUAL_INDEX]] |
| 旧每日投资观察镜像 | 1 | [[03_STATE/MARKET_STATE/MIRRORED_LEGACY_DAILY_STATE_INDEX]] |
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
