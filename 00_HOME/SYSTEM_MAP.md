---
title: system_map
date: 2026-07-23
updated: 2026-07-23
layer: META
primary_role: system_map
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: operational
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# 系统地图

| 层 | 唯一主职责 | 不允许做什么 |
|---|---|---|
| `00_HOME` | 入口、路由、权限 | 不保存投资结论 |
| `01_道` | 已确认长期认知与禁止事项 | 不放 State、公司判断、参数、AI 推断 |
| `02_术` | 可进化的研究和交易方法 | 不自动升级成道 |
| `03_STATE` | 当前状态、待验证、观察池 | 不进入长期页面，必须过期 |
| `04_CASE_GYM` | 真实案例、训练样本、结算 | 单个 Case 不直接生成原则 |
| `05_EVIDENCE_META` | 证据、来源、冲突、覆盖 | 不替 Murphy 裁决 |
| `90_AUTOMATION` | prompts、脚本、测试、运行态 | 不与投资内容混放 |
| `99_ARCHIVE` | 旧结构、历史系统、待复核内容 | 不在前台授权 |

## 旧结构的状态

旧 `交易宪法/CONSTITUTION.md`、`MURPHY_CURRENT_COGNITIVE_MODEL.md` 和 `_meta` 账本已经降为兼容入口。完整历史原文保存在 [[01_道/_HISTORY]]，前台权威以本新结构为准。
