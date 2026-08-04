---
title: "BTGO双轨综合投资分析（v6） legacy source case"
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
settlement_status: partially_settled_price_path
settlement_rule: price_path_and_business_retest
review_date: 2026-08-26
legacy_path: "基础概念/实体商/BItGO/BTGO_投资决策.md"
source_paths:
  - 基础概念/实体商/BItGO/BTGO_投资决策.md
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# BTGO双轨综合投资分析（v6） Legacy Source Case

## 先说人话

**今天发生了什么：**旧文件 `基础概念/实体商/BItGO/BTGO_投资决策.md` 已抽成 Case Gym 来源卡，原文继续保留在旧路径。

**为什么重要：**这类材料往往混有公司判断、交易方案、情绪反应和方法观察。进入 Case Gym 后，它只能训练方法，不能直接升级成 MINDSET、Constitution 或交易授权。

**现在做什么：**旧结论已完成价格路径的部分结算；经营票仍等下一次财报验证。

## Source

| 字段 | 内容 |
|---|---|
| 原始文件 | [[BTGO_投资决策]] |
| 原始标题 | BTGO双轨综合投资分析（v6） |
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
| 验证期限 | 2026-08-26 下一次估算财报日前后复核 |
| 结算结果 | 价格路径部分结算：旧文判断“观望、暂不买入”，2026-07 中下旬 BTGO 在约 $5.06-$5.65 区间，进入旧文 $5-7 观察区，但这只验证价格回落，不验证业务改善 |
| 可写入位置 | `04_CASE_GYM / 02_术 / METHOD_TESTS` |
| 不可写入位置 | `01_道/MINDSET / 01_道/CONSTITUTION / 当前交易授权` |

## Settlement Snapshot

| 项目 | 内容 |
|---|---|
| 事前日期 | 2026-03-30 |
| 事前动作 | 观望，暂不买入 |
| 事前价格 | $7.67 |
| 观察区 | $5-7 |
| 后验价格事实 | StockAnalysis 显示 2026-07-15 收盘 $5.16；Marketscreener 显示 2026-07-21 最新 $5.65 |
| 业务待验证 | AoP、DAS 毛利率、真服务收入、经营现金流、下一次财报 |
| 方法结论 | 不追破发反弹是正确流程；价格进入观察区后也不能自动转买入，必须重开经营票和估值票 |

## Review Gate

1. 先确认这是实际交易、未成交、研究判断、错过机会还是情绪短记。
2. 再补 `business_horizon / thesis_horizon / execution_horizon / review_date`。
3. 只有形成跨案例稳定反例或方法修正，才允许进入 Skill 更新。
4. 即使形成候选哲学，也只能进入 Philosophy Inbox，不能自动进入 MINDSET。
