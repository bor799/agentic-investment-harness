---
title: portfolio_ledger_index
date: 2026-07-23
updated: 2026-07-23
layer: STATE
primary_role: portfolio_ledger_index
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

# Portfolio Ledger

当前持仓、成交和账户事实只认券商回报。历史主账 [[兴趣领域/股票投资/归档/📈 个人交易手册]] 仍是来源，但其中的方法、人格推断和单次 Case 规则不再拥有长期权限。

## 最小记录

| 字段 | 含义 |
|---|---|
| data_cutoff | 数据截止时间 |
| expires_at | 失效时间 |
| broker_fact | 成交、撤单、废单、到账等券商事实 |
| thesis_state | 当前 thesis 状态 |
| allowed_action | 六档动作之一 |
