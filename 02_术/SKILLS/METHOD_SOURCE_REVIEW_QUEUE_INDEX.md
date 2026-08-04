---
title: method_source_review_queue_index
date: 2026-07-24
updated: 2026-07-24
layer: METHOD
primary_role: method_source_review_queue_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
  - 05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.md
---

# Method Source Review Queue Index

## 先说人话

**今天发生了什么：**44 个旧方法来源已镜像进入 Method Source Review Queue。

**为什么重要：**这些文件是旧方法正文的来源，不应继续散落在旧结构里；但复制入队不等于已经逐段合并进 canonical Skill。

**现在做什么：**后续逐个抽取规则、反例、适用范围和失败条件，再写入对应 Skill；未合并前，旧方法只作来源。

合并状态：[[02_术/SKILLS/METHOD_SOURCE_MERGE_STATUS]]

| 镜像副本 | 原始路径 | 标题 | 旧角色 | 目标 |
|---|---|---|---|---|
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/01_投资主框架.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/01_投资主框架]] | 投资主框架 | `legacy_method_source` | `02_术/TRADING_SYSTEM/01_RESEARCH_FLOW` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/02_泊松供需闭环.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/02_泊松供需闭环]] | 泊松供需闭环 | `legacy_method_source` | `02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/03_流动性过滤器.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/03_流动性过滤器]] | 流动性过滤器 | `legacy_method_source` | `02_术/SKILLS/LIQUIDITY_TRANSMISSION` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/04_行为纠偏系统.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/04_行为纠偏系统]] | 行为纠偏系统 | `legacy_method_source` | `02_术/SKILLS/BEHAVIOR_REVIEW` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/05_资本纪律.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/05_资本纪律]] | 资本纪律 | `legacy_method_source` | `02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION + PARAMETERS` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/06_认知训练协议.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/06_认知训练协议]] | 认知训练协议 | `legacy_method_source` | `02_术/TRADING_SYSTEM/03_FEEDBACK_LOOP` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/07_认知模型维护协议.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/07_认知模型维护协议]] | 认知模型维护协议 | `legacy_method_source` | `05_EVIDENCE_META/META/PROVENANCE_SCHEMA + CLAIM_LEDGER + CONFLICT_REGISTER` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260617AI算力连接与材料瓶颈_挖掘端框架.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260617AI算力连接与材料瓶颈_挖掘端框架]] | 260617AI算力连接与材料瓶颈_挖掘端框架 | `legacy_analysis_method_source` | `02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260617AI算力链_训练集溯源.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260617AI算力链_训练集溯源]] | AI 算力链训练集溯源：两篇文章信息单元 → SOP 映射 + 漏检项 | `legacy_analysis_method_source` | `02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260630财报季_经营验证与定时任务体系.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260630财报季_经营验证与定时任务体系]] | 260630财报季_经营验证与定时任务体系 | `legacy_analysis_method_source` | `02_术/SKILLS/COMPANY_FUNDAMENTALS + 90_AUTOMATION/README` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260719组合_行为纠偏与资本纪律操作系统.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260719组合_行为纠偏与资本纪律操作系统]] | 组合：行为纠偏与资本纪律操作系统 | `legacy_analysis_method_source` | `02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION + 02_术/SKILLS/BEHAVIOR_REVIEW` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260721组合_交易认知体系首轮训练.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260721组合_交易认知体系首轮训练]] | 组合：交易认知体系首轮训练 | `legacy_analysis_method_source` | `02_术/TRADING_SYSTEM/03_FEEDBACK_LOOP + 02_术/SKILLS/LIQUIDITY_TRANSMISSION + 02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260606投资框架_供需泊松闭环.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260606投资框架_供需泊松闭环]] | 投资框架：宏观供需泊松交易闭环 | `legacy_basic_method_source` | `02_术/TRADING_SYSTEM/01_RESEARCH_FLOW + 02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617三大材料链对照表_AI_储能_铜.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617三大材料链对照表_AI_储能_铜]] | 三大材料链对照表：AI 算力 / 储能 / 铜 | `legacy_basic_method_source` | `02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端SOP_v1.1.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端SOP_v1.1]] | 挖掘端工作流 SOP v1.1 | `legacy_basic_method_source` | `02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端三分布应用决策表.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端三分布应用决策表]] | 挖掘端三分布应用决策表 | `legacy_basic_method_source` | `02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端工作流SOP_v1.0.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端工作流SOP_v1.0]] | 挖掘端工作流 SOP v1.0 | `legacy_basic_method_source` | `02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端训练完成报告.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端训练完成报告]] | 挖掘端训练循环完成报告（F1-F10） | `legacy_basic_method_source` | `02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端训练循环与评估手册.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260617挖掘端训练循环与评估手册]] | 挖掘端训练循环与评估手册 | `legacy_basic_method_source` | `02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260622基金与个股_从个人约束出发的1至3年框架.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260622基金与个股_从个人约束出发的1至3年框架]] | 260622基金与个股_从个人约束出发的1至3年框架 | `legacy_basic_method_source` | `02_术/TRADING_SYSTEM/01_RESEARCH_FLOW + 02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260622电解液_需求强度非线性信号框架.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260622电解液_需求强度非线性信号框架]] | 260622电解液_需求强度非线性信号框架 | `legacy_basic_method_source` | `02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND + 02_术/SKILLS/GROWTH_TECH` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260624电解液_物理需求线性与利润估值非线性.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260624电解液_物理需求线性与利润估值非线性]] | 260624电解液_物理需求线性与利润估值非线性 | `legacy_basic_method_source` | `02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND + 02_术/SKILLS/EXPECTATIONS_VALUATION + 02_术/SKILLS/GROWTH_TECH` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260709投资框架_股价三层肉估值三段式与不做清单.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260709投资框架_股价三层肉估值三段式与不做清单]] | 投资框架：股价三层肉、估值三段式与不做清单 | `legacy_basic_method_source` | `02_术/SKILLS/EXPECTATIONS_VALUATION + 02_术/SKILLS/LIQUIDITY_TRANSMISSION` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260713AI_Token需求增长与稀缺性迁移投资框架.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260713AI_Token需求增长与稀缺性迁移投资框架]] | AI Token需求增长与稀缺性迁移投资框架 | `legacy_basic_method_source` | `02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND + 02_术/SKILLS/GROWTH_TECH` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260720投资框架_宏观流动性过滤器与认知退出纪律.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260720投资框架_宏观流动性过滤器与认知退出纪律]] | 宏观流动性过滤器与退出纪律 | `legacy_basic_method_source` | `02_术/SKILLS/LIQUIDITY_TRANSMISSION` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/稳定币与财务指标概念路径.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/稳定币与财务指标概念路径]] | 稳定币与财务指标概念路径 | `legacy_basic_method_source` | `02_术/SKILLS/GROWTH_TECH + 02_术/SKILLS/COMPANY_FUNDAMENTALS` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/量化交易数学基础设施.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/量化交易数学基础设施]] | 量化交易数学基础设施 | `legacy_basic_method_source` | `02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/我的投资框架：从宏观到企业的系统思考.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/我的投资框架：从宏观到企业的系统思考]] | 我的投资框架：从宏观到企业的系统思考 | `legacy_root_framework` | `02_术/TRADING_SYSTEM/01_RESEARCH_FLOW + 01_道/PHILOSOPHY_INBOX/CANDIDATE_CLAIMS + 05_EVIDENCE_META/EVIDENCE/THEMES/README` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/AI投资主线.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/AI投资主线]] | AI投资主线 | `legacy_ai_cycle_method` | `02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/BOTTLENECK_3X_FRAMEWORK.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/BOTTLENECK_3X_FRAMEWORK]] | BOTTLENECK_3X_FRAMEWORK | `legacy_ai_cycle_method` | `02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/CROSS_MARKET_V2_RUN_BOUNDARIES.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/CROSS_MARKET_V2_RUN_BOUNDARIES]] | CROSS_MARKET_V2_RUN_BOUNDARIES | `legacy_ai_cycle_method` | `90_AUTOMATION/README` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/ENGINEER_SIGNAL_3X_RADAR.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/ENGINEER_SIGNAL_3X_RADAR]] | ENGINEER_SIGNAL_3X_RADAR | `legacy_ai_cycle_method` | `02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/FRAMEWORK_TRAINING_LOG.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/FRAMEWORK_TRAINING_LOG]] | 框架训练日志 | `legacy_ai_cycle_method` | `02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK + 02_术/TRADING_SYSTEM/03_FEEDBACK_LOOP` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/MINDSPACE_SOURCE_MCP_SOP.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/MINDSPACE_SOURCE_MCP_SOP]] | MINDSPACE_SOURCE_MCP_SOP | `legacy_ai_cycle_method` | `05_EVIDENCE_META/META/PROVENANCE_SCHEMA + 90_AUTOMATION/README` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/README.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/README]] | README | `legacy_ai_cycle_method` | `90_AUTOMATION/README + 03_STATE/WATCHLISTS/README` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/refresh_targets_2026-05-24.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/refresh_targets_2026-05-24]] | refresh_targets_2026-05-24 | `legacy_ai_cycle_method` | `90_AUTOMATION/README + 03_STATE/WATCHLISTS/README` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/source_health_2026-05-24.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/source_health_2026-05-24]] | source_health_2026-05-24 | `legacy_ai_cycle_method` | `05_EVIDENCE_META/META/PROVENANCE_SCHEMA + 90_AUTOMATION/README` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/信息重整与趋势刷新计划_2026-05-24.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/信息重整与趋势刷新计划_2026-05-24]] | 信息重整与趋势刷新计划_2026-05-24 | `legacy_ai_cycle_method` | `05_EVIDENCE_META/META/PROVENANCE_SCHEMA + 90_AUTOMATION/README` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/研究对象清单.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/研究对象清单]] | 研究对象清单 | `legacy_ai_cycle_method` | `03_STATE/WATCHLISTS/README` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/结构性转变判断框架.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/结构性转变判断框架]] | 结构性转变判断框架 | `legacy_ai_cycle_method` | `02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/期权卖方统计学与Roll策略实战.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/期权卖方统计学与Roll策略实战]] | 期权卖方统计学与Roll策略实战 | `legacy_options_method` | `02_术/SKILLS/OPTIONS` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/期权基础.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/期权基础]] | 期权基础 | `legacy_options_method` | `02_术/SKILLS/OPTIONS` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/期权策略与认知演进总结.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/期权策略与认知演进总结]] | 期权策略与认知演进总结 | `legacy_options_method` | `02_术/SKILLS/OPTIONS` |
| [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/波动率收割与期权量化策略体系.md]] | [[兴趣领域/股票投资/02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/波动率收割与期权量化策略体系]] | 波动率收割与期权量化策略体系 | `legacy_options_method` | `02_术/SKILLS/OPTIONS` |

## 边界

- Review Queue 不等于 canonical Skill。
- 旧方法中的旧参数、旧评分、旧自动晋升逻辑不能直接恢复。
- 合并时必须写清：输入、输出、不能证明什么、失败条件和来源回链。
