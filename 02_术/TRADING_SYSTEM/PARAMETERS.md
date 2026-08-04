---
title: parameters
date: 2026-07-23
updated: 2026-07-24
layer: METHOD
primary_role: parameters
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: operational
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/05_资本纪律.md
---

# Parameters

## 文件性质

这里保存会随经验和资本状态变化的参数。参数不是 Constitution，不是长期哲学，也不能从旧报告自动继承。

| 参数 | 当前状态 | 来源 | 权限 |
|---|---|---|---|
| 24 小时冷静期 | active_operational | AGENTS 与行为纪律系统 | operational |
| `uncalibrated` 概率状态 | active_operational | AGENTS 与重构方案 | operational |
| 生活资金隔离 | active_operational | AGENTS 与资本纪律系统 | operational |
| `90%/10%` 职责桶 | active_operational | AGENTS 与资本纪律系统 | operational |
| O 侧旧 `3%R` 滚动最大损失预算 | active_operational_if_current_authority_confirms | 资本纪律系统 | operational_guardrail |
| O 单笔、同 thesis、单标的、集群和压力损失护栏 | active_operational_if_current_authority_confirms | 资本纪律系统 | operational_guardrail |
| 旧 `/70` 评分 | superseded | AI 周期旧 scorecard | none |
| 固定 LR / 固定加分 | retired | 旧报告 | none |
| 未校准单点概率 | retired | 旧报告 | none |
| 旧仓位比例 | superseded | 历史报告 | none |

新增或改变参数时，必须写清依据、适用范围、失效条件和回滚方式。

本文件记录参数权限，不由 AI 合并动作产生新仓位授权。任何 `active_operational_if_current_authority_confirms` 的条目，在真实交易前必须回查当前资本纪律权威、最新 `R`、唯一主账和 Murphy 明确确认。
