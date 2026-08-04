---
title: ai_cycle_runtime_index
date: 2026-07-23
updated: 2026-07-23
layer: AUTOMATION
primary_role: ai_cycle_runtime_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# AI Cycle Runtime Index

## 先说人话

**今天发生了什么：**旧 queue、run log、watchlist 和评分表接入 runtime/state 区。

**为什么重要：**运行态会过期，只说明某次自动化跑到了哪里，不说明研究结论有效。

**现在做什么：**自动化复跑前先检查这些状态是否过期。

| 文件 | 旧位置 | 状态 |
|---|---|---|
| `cn_consumer_refresh_queue.md` | [[兴趣领域/股票投资/归档/AI周期探索/0_总览/cn_consumer_refresh_queue]] | `runtime_or_state` |
| `company_queue.md` | [[兴趣领域/股票投资/归档/AI周期探索/0_总览/company_queue]] | `runtime_or_state` |
| `company_score_table.md` | [[兴趣领域/股票投资/归档/AI周期探索/0_总览/company_score_table]] | `runtime_or_state` |
| `cross_market_queue_v2.json` | [[cross_market_queue_v2.json]] | `runtime_or_state` |
| `new_company_intake_queue.md` | [[兴趣领域/股票投资/归档/AI周期探索/0_总览/new_company_intake_queue]] | `runtime_or_state` |
| `run_log.md` | [[兴趣领域/股票投资/归档/AI周期探索/0_总览/run_log]] | `runtime_or_state` |
| `v2_last_outcome.json` | [[v2_last_outcome.json]] | `runtime_or_state` |
| `v2_run_log.jsonl` | [[v2_run_log.jsonl]] | `runtime_or_state` |
| `watchlist_master.md` | [[兴趣领域/股票投资/归档/AI周期探索/0_总览/watchlist_master]] | `runtime_or_state` |
