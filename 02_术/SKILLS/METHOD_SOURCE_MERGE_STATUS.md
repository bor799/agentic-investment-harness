---
title: method_source_merge_status
date: 2026-07-24
updated: 2026-07-24
layer: METHOD
primary_role: method_source_merge_status
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE_INDEX.md
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# Method Source Merge Status

## 先说人话

**今天发生了什么：**旧方法来源开始从 Review Queue 进入 canonical Skill 的逐段吸收。

**为什么重要：**复制入队只解决“找得到”；合并进 Skill 才解决“当前怎么用”。这张表防止把未合并的旧方法当当前方法。

**现在做什么：**下一批继续按 canonical Skill 分组合并，不新增孤立方法页。

## 总览

| 状态 | 数量 |
|---|---:|
| Review Queue 总数 | 44 |
| 已合并进 canonical Skill | 44 |
| 待合并 | 0 |

## 已合并

| 来源 | 写入 | 回执 | 状态 |
|---|---|---|---|
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/期权基础]] | [[02_术/SKILLS/OPTIONS]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/options_method_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/期权策略与认知演进总结]] | [[02_术/SKILLS/OPTIONS]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/options_method_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/期权卖方统计学与Roll策略实战]] | [[02_术/SKILLS/OPTIONS]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/options_method_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/波动率收割与期权量化策略体系]] | [[02_术/SKILLS/OPTIONS]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/options_method_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/01_投资主框架]] | [[02_术/TRADING_SYSTEM/01_RESEARCH_FLOW]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/constitution_skills_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/02_泊松供需闭环]] | [[02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/constitution_skills_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/03_流动性过滤器]] | [[02_术/SKILLS/LIQUIDITY_TRANSMISSION]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/constitution_skills_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/04_行为纠偏系统]] | [[02_术/SKILLS/BEHAVIOR_REVIEW]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/constitution_skills_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/05_资本纪律]] | [[02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION]] / [[02_术/TRADING_SYSTEM/PARAMETERS]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/constitution_skills_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/06_认知训练协议]] | [[02_术/TRADING_SYSTEM/03_FEEDBACK_LOOP]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/constitution_skills_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/07_认知模型维护协议]] | [[05_EVIDENCE_META/META/PROVENANCE_SCHEMA]] / [[05_EVIDENCE_META/META/CLAIM_LEDGER]] / [[05_EVIDENCE_META/META/CONFLICT_REGISTER]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/constitution_skills_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260617AI算力连接与材料瓶颈_挖掘端框架]] | [[02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/analysis_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260617AI算力链_训练集溯源]] | [[02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/analysis_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260630财报季_经营验证与定时任务体系]] | [[02_术/SKILLS/COMPANY_FUNDAMENTALS]] / [[90_AUTOMATION/README]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/analysis_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260719组合_行为纠偏与资本纪律操作系统]] | [[02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION]] / [[02_术/SKILLS/BEHAVIOR_REVIEW]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/analysis_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260721组合_交易认知体系首轮训练]] | [[02_术/TRADING_SYSTEM/03_FEEDBACK_LOOP]] / [[02_术/SKILLS/LIQUIDITY_TRANSMISSION]] / [[02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/analysis_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260606投资框架_供需泊松闭环]] | [[02_术/TRADING_SYSTEM/01_RESEARCH_FLOW]] / [[02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/basic_concepts_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617三大材料链对照表_AI_储能_铜]] | [[02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/basic_concepts_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端SOP_v1.1]] | [[02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/basic_concepts_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端三分布应用决策表]] | [[02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/basic_concepts_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端工作流SOP_v1.0]] | [[02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/basic_concepts_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端训练完成报告]] | [[02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/basic_concepts_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端训练循环与评估手册]] | [[02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/basic_concepts_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260622基金与个股_从个人约束出发的1至3年框架]] | [[02_术/TRADING_SYSTEM/01_RESEARCH_FLOW]] / [[02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/basic_concepts_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260622电解液_需求强度非线性信号框架]] | [[02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND]] / [[02_术/SKILLS/GROWTH_TECH]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/basic_concepts_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260624电解液_物理需求线性与利润估值非线性]] | [[02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND]] / [[02_术/SKILLS/EXPECTATIONS_VALUATION]] / [[02_术/SKILLS/GROWTH_TECH]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/basic_concepts_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260709投资框架_股价三层肉估值三段式与不做清单]] | [[02_术/SKILLS/EXPECTATIONS_VALUATION]] / [[02_术/SKILLS/LIQUIDITY_TRANSMISSION]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/basic_concepts_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260713AI_Token需求增长与稀缺性迁移投资框架]] | [[02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND]] / [[02_术/SKILLS/GROWTH_TECH]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/basic_concepts_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260720投资框架_宏观流动性过滤器与认知退出纪律]] | [[02_术/SKILLS/LIQUIDITY_TRANSMISSION]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/basic_concepts_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/稳定币与财务指标概念路径]] | [[02_术/SKILLS/GROWTH_TECH]] / [[02_术/SKILLS/COMPANY_FUNDAMENTALS]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/basic_concepts_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/量化交易数学基础设施]] | [[02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/basic_concepts_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/AI投资主线]] | [[02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/ai_cycle_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/BOTTLENECK_3X_FRAMEWORK]] | [[02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/ai_cycle_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/CROSS_MARKET_V2_RUN_BOUNDARIES]] | [[90_AUTOMATION/README]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/ai_cycle_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/ENGINEER_SIGNAL_3X_RADAR]] | [[02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/ai_cycle_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/FRAMEWORK_TRAINING_LOG]] | [[02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK]] / [[02_术/TRADING_SYSTEM/03_FEEDBACK_LOOP]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/ai_cycle_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/MINDSPACE_SOURCE_MCP_SOP]] | [[05_EVIDENCE_META/META/PROVENANCE_SCHEMA]] / [[90_AUTOMATION/README]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/ai_cycle_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/README]] | [[90_AUTOMATION/README]] / [[03_STATE/WATCHLISTS/README]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/ai_cycle_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/refresh_targets_2026-05-24]] | [[90_AUTOMATION/README]] / [[03_STATE/WATCHLISTS/README]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/ai_cycle_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/source_health_2026-05-24]] | [[05_EVIDENCE_META/META/PROVENANCE_SCHEMA]] / [[90_AUTOMATION/README]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/ai_cycle_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/信息重整与趋势刷新计划_2026-05-24]] | [[05_EVIDENCE_META/META/PROVENANCE_SCHEMA]] / [[90_AUTOMATION/README]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/ai_cycle_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/研究对象清单]] | [[03_STATE/WATCHLISTS/README]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/ai_cycle_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/结构性转变判断框架]] | [[02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/ai_cycle_method_sources_absorption_receipt]] | merged |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/我的投资框架：从宏观到企业的系统思考]] | [[02_术/TRADING_SYSTEM/01_RESEARCH_FLOW]] / [[01_道/PHILOSOPHY_INBOX/CANDIDATE_CLAIMS]] / [[05_EVIDENCE_META/EVIDENCE/THEMES/README]] | [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/root_framework_absorption_receipt]] | merged |

## 待合并分组

| 分组 | 数量 | 目标 |
|---|---:|---|
| 无 | 0 | Review Queue 方法源已全部合并 |

## 边界

- `merged` 只表示已经写入 canonical Skill，不表示 Murphy 确认为个人哲学。
- Review Queue 原文仍是 `decision_authority: none`。
- 合并时必须保留“吸收内容”和“降权内容”。
