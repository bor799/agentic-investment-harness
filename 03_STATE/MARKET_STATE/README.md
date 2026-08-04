---
title: market_state_index
date: 2026-07-23
updated: 2026-07-24
layer: STATE
primary_role: market_state_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
data_cutoff:
expires_at:
---

# Market State

保存会过期的宏观、市场、行业和标的水位。任何 State 必须有 `data_cutoff`、`expires_at` 或 `refresh_trigger`。

| 入口 | 用途 |
|---|---|
| [[03_STATE/MARKET_STATE/MIRRORED_LEGACY_DAILY_STATE_INDEX]] | 旧每日投资观察全文镜像 |

旧日报重新使用前必须刷新事实、价格和失效条件。
