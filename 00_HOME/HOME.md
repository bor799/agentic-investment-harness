---
title: home
date: 2026-07-23
updated: 2026-07-25
layer: META
primary_role: home
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: operational
source_paths:
  - 90_AUTOMATION/DESIGN_NOTES/LEGACY_AUTOMATION_INVENTORY.md
---

# Murphy 投资系统 HOME

## 现在只从四个入口开始

| 我现在要做什么 | 入口 | 系统先做什么 |
|---|---|---|
| 判断一个新标的 | [[90_AUTOMATION/PROMPTS/INVESTMENT_HARNESS\|60 秒结构先验]] | 识别领域、匹配合格模式、给出反模式和最高信息问题 |
| 调用过去的领域知识 | [[05_EVIDENCE_META/KNOWLEDGE/DOMAINS/README\|领域判断地图]] | 读取稳定因果、钱路、失败条件和 Case |
| 查看当前正在验证什么 | [[03_STATE/HYPOTHESIS_QUEUE/README\|Current]] | 读取时点事实、唯一问题和到期状态 |
| 吸收一篇新材料 | [[00_HOME/CONTENT_ROUTER\|材料吸收]] | 判断它改变模式、State，还是 `NO_INCREMENT` |

白话解释：先用过去的知识形成结构先验，再让当前事实纠错，最后才进入四票和六档动作。结构先验本身没有投资或资本权限。

## 判断链

```text
研究触发
→ Domain Knowledge + 已结算 Case
→ structural_prior（uncalibrated）
→ Current + 新 Source
→ H_B / H_R / H_L / H_C
→ 六档动作
```

## 权威与历史

- 长期边界：[[01_道/CONSTITUTION]]、[[01_道/MINDSET]]
- 决策与资本合同：[[02_术/TRADING_SYSTEM/00_DECISION_CONTRACT]]
- 研究知识治理：[[05_EVIDENCE_META/HOME]]
- 真实案例：[[04_CASE_GYM/CASE_INDEX]]
- 旧原文与历史镜像只用于回源、反证和资本生存，不进入日常前台。

## 一句话规则

道由 Murphy 裁决；领域地图负责识别，Case 负责类比，State 负责当下，Source 负责纠错，四票才负责动作。
