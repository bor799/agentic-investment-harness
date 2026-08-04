---
title: "LMND 投资决策手册 legacy source case"
date: 2026-07-24
updated: 2026-07-24
layer: CASE
primary_role: migrated_legacy_source_case
status: active
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
case_type: research_or_decision_source
settlement_status: rule_defined_unsettled
settlement_rule: q1_q4_2026_business_and_price_retest
review_date: 2027-02-28
legacy_path: "基础概念/实体商/LMND/LMND_投资决策手册.md"
source_paths:
  - 基础概念/实体商/LMND/LMND_投资决策手册.md
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# LMND 投资决策手册 Legacy Source Case

## 先说人话

**今天发生了什么：**旧文件 `基础概念/实体商/LMND/LMND_投资决策手册.md` 已抽成 Case Gym 来源卡，原文继续保留在旧路径。

**为什么重要：**这类材料往往混有公司判断、交易方案、情绪反应和方法观察。进入 Case Gym 后，它只能训练方法，不能直接升级成 MINDSET、Constitution 或交易授权。

**现在做什么：**结算规则已定义；截至 2026-07 中下旬，价格仍高于旧买入区，业务结算要等 2026 全年财报链。

## Source

| 字段 | 内容 |
|---|---|
| 原始文件 | [[LMND_投资决策手册]] |
| 原始标题 | LMND 投资决策手册 |
| 来源角色 | `legacy_company_case_source` |
| 旧层级 | `CASE` |
| 原权限 | `none` |

## Case Capture

| 项目 | 当前状态 |
|---|---|
| 事前判断 | 待从原文萃取 |
| 当时价格 / 估值语法 | 待从原文萃取 |
| 核心证据链 | 待从原文萃取 |
| 行为信号 | 待复盘 |
| 验证期限 | Q1/Q2/Q3/Q4 2026 财报逐季复核，终局先看到 2027-02-28 |
| 结算结果 | 规则已定义但未终局结算：旧文要求 $42-50 才是买入区，2026-07 中下旬 LMND 约 $67，仍不在买入区；EBITDA 转正、GLR、IFP、运营费率仍需财报验证 |
| 可写入位置 | `04_CASE_GYM / 02_术 / METHOD_TESTS` |
| 不可写入位置 | `01_道/MINDSET / 01_道/CONSTITUTION / 当前交易授权` |

## Settlement Snapshot

| 项目 | 内容 |
|---|---|
| 事前日期 | 2026-03-31 |
| 事前动作 | HOLD / 等待回调，不追 |
| 事前价格 | $60.70 |
| 旧买入区 | $42-50 |
| 后验价格事实 | ChartExchange 显示 2026-07-20 LMND 约 $67.43；StockAnalysis 显示 2026-07-15 收盘 $66.05 |
| 业务待验证 | GLR < 60%、IFP 增速 > 20%、EBITDA 向转正收敛、运营费率下降 |
| 方法结论 | 不追高规则仍有效；价格没进买入区，不能用后续涨跌倒推旧估值规则对错 |

## Review Gate

1. 先确认这是实际交易、未成交、研究判断、错过机会还是情绪短记。
2. 再补 `business_horizon / thesis_horizon / execution_horizon / review_date`。
3. 只有形成跨案例稳定反例或方法修正，才允许进入 Skill 更新。
4. 即使形成候选哲学，也只能进入 Philosophy Inbox，不能自动进入 MINDSET。
