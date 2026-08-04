---
title: prompts_index
date: 2026-07-23
updated: 2026-07-24
layer: AUTOMATION
primary_role: prompts_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: operational
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# Prompts

当前有效 prompt 在这里 canonical 化，旧 prompt 进入历史。

| 入口 | 用途 |
|---|---|
| [[90_AUTOMATION/PROMPTS/AI_CYCLE_PROMPTS_INDEX]] | 旧 AI 周期 prompt / command 登记 |
| [[90_AUTOMATION/PROMPTS/AUTOMATION_REVIEW_QUEUE_INDEX]] | 待复核旧 prompt、旧命令和历史自动化设计 |
| [[90_AUTOMATION/PROMPTS/CURRENT_CANDIDATES_INDEX]] | 当前 Claude 自动化候选副本，未核验前不视为 canonical |

## 边界

- `REVIEW_QUEUE` 不等于当前有效 prompt。
- `CURRENT_CANDIDATES` 需要核验边界和原工具要求位置。
- 自动化不能写入 MINDSET / Constitution，最多进入 Philosophy Inbox 或生成回执。
