---
title: basic_concepts_method_sources_absorption_receipt
date: 2026-07-24
updated: 2026-07-24
layer: META
primary_role: absorption_receipt
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260606投资框架_供需泊松闭环.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617三大材料链对照表_AI_储能_铜.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端SOP_v1.1.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端三分布应用决策表.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端工作流SOP_v1.0.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端训练完成报告.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端训练循环与评估手册.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260622基金与个股_从个人约束出发的1至3年框架.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260622电解液_需求强度非线性信号框架.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260624电解液_物理需求线性与利润估值非线性.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260709投资框架_股价三层肉估值三段式与不做清单.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260713AI_Token需求增长与稀缺性迁移投资框架.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260720投资框架_宏观流动性过滤器与认知退出纪律.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/稳定币与财务指标概念路径.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/量化交易数学基础设施.md
---

# Basic Concepts Method Sources Absorption Receipt

```yaml
new_information: 15 个基础概念普通方法源
change: revise
affected_item:
  - 02_术/TRADING_SYSTEM/01_RESEARCH_FLOW.md
  - 02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION.md
  - 02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK.md
  - 02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND.md
  - 02_术/SKILLS/EXPECTATIONS_VALUATION.md
  - 02_术/SKILLS/GROWTH_TECH.md
  - 02_术/SKILLS/COMPANY_FUNDAMENTALS.md
  - 02_术/SKILLS/LIQUIDITY_TRANSMISSION.md
result: METHOD_UPDATE
write_to:
  - Trading System
  - Skills
```

## 前台摘要

- **新东西是什么：**把 15 个基础概念方法源的可执行规则并入当前 canonical 体系。
- **为什么重要：**这些文件是旧系统的方法腹地，包含挖掘端 SOP、供需泊松、电解液状态机、估值三段式、宏观流动性、稳定币财务路径和量化边界。
- **现在做什么：**当前调用以 canonical 文件为准；旧源保留在 Review Queue 作为证据和版本来源。

## 吸收映射

| 分组 | 来源 | 写入 | 吸收内容 |
|---|---|---|---|
| 挖掘端训练 | SOP v1.0 / v1.1 / 三分布 / 训练手册 / 三链对照 / 训练完成报告 | `STRUCTURAL_CHANGE_BOTTLENECK.md` | 九步漏斗、七步瓶颈测试、四模型分布指纹、训练误差分析、跨链对照、版本边界 |
| 供需主链 | `260606投资框架_供需泊松闭环.md` | `RESEARCH_FLOW.md`、`INDUSTRY_SUPPLY_DEMAND.md` | 产业需求漏斗、供给锁死、财务验证、事件时钟、悬置容器 |
| 材料利润状态机 | 两份电解液文档 | `INDUSTRY_SUPPLY_DEMAND.md`、`EXPECTATIONS_VALUATION.md`、`GROWTH_TECH.md` | 物理需求线性、订单/价格/利润/估值非线性、六道闸门 |
| 工具选择 | `260622基金与个股...md` | `RESEARCH_FLOW.md`、`02_CAPITAL_AND_EXECUTION.md` | 宽基/主题基金/个股分层、可承受损失倒推、价格价值证据三表 |
| 估值和流动性 | `260709...md`、`260720...md` | `EXPECTATIONS_VALUATION.md`、`LIQUIDITY_TRANSMISSION.md` | 股价三层肉、估值三段式、四级水、四坐标、三种回报账户、退出复盘 |
| AI Token / 稳定币 | `260713AI_Token...md`、`稳定币与财务指标概念路径.md` | `GROWTH_TECH.md`、`COMPANY_FUNDAMENTALS.md` | Token 使用到硬件/利润闸门、稳定币/RWA 收费权路径、概念到财务路径 |
| 量化 | `量化交易数学基础设施.md` | `02_CAPITAL_AND_EXECUTION.md` | 过拟合、多重检验、执行深度、滑点、模型参数误差和 Kelly 降权 |

## 明确降权或废止

- 旧强制数字化贝叶斯、固定概率、固定证据加分、自评分、训练达标、早停条件不能进入 EV、排序或仓位。
- 旧主题仓位比例、计划仓位百分比、Kelly 仓位、订单簿深度比例和固定阈值不授权新交易。
- “训练循环达标”只说明方法训练完成，不说明任何公司、ETF、期权或主题可以建立风险。
- AI Token 使用量、稳定币发行量、RWA tokenised value、材料终端需求和量化回测结果，都必须继续走到收入、毛利、经营利润、现金流、估值和资本纪律。

## 边界

- 本回执不授权交易、仓位、参数或主账修改。
- 旧源中的实时数字、个案结论和当时市场状态只保留为历史线索。
- `merged` 只表示方法正文已经进入当前体系，不表示 Murphy 把全部内容确认为稳定哲学。
