---
title: ai_active_expectations
date: 2026-07-28
updated: 2026-07-28
layer: STATE
primary_role: active_expectations_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
data_cutoff: 2026-07-28
review_date: 2026-08-15
---

# AI Active Expectations

这里冻结“我们在事件发生前相信什么”。它不追求伪精确概率，只保存方向区间、外部共识缺口、结算规则和版本。

- [[03_STATE/EXPECTATIONS/AI/ORCL_FY27Q1_v1]]
- [[03_STATE/EXPECTATIONS/AI/NBIS_NEXT_EARNINGS_v1]]

## 冻结规则

1. `state: frozen` 后，不覆盖 `own_range`、形成理由或 `frozen_as_of`。
2. 官方日期公布时，新建版本或受控元数据版本；v1 原文保留。
3. 结算写 `actual` 与 `resolution_source`，并把错误归因到：
   `mechanism / transmission / magnitude / timing / market_expectation / valuation / execution / unresolved`。
4. 预期结算只能提议 belief 更新，不能自动修改 Knowledge、Current 或资本。

