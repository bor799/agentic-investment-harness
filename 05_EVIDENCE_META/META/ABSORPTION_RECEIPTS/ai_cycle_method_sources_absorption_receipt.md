---
title: ai_cycle_method_sources_absorption_receipt
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
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/AI投资主线.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/BOTTLENECK_3X_FRAMEWORK.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/CROSS_MARKET_V2_RUN_BOUNDARIES.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/ENGINEER_SIGNAL_3X_RADAR.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/FRAMEWORK_TRAINING_LOG.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/MINDSPACE_SOURCE_MCP_SOP.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/README.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/refresh_targets_2026-05-24.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/source_health_2026-05-24.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/信息重整与趋势刷新计划_2026-05-24.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/研究对象清单.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/结构性转变判断框架.md
---

# AI Cycle Method Sources Absorption Receipt

```yaml
new_information: 12 个旧 AI 周期方法源
change: revise
affected_item:
  - 02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK.md
  - 02_术/TRADING_SYSTEM/03_FEEDBACK_LOOP.md
  - 03_STATE/WATCHLISTS/README.md
  - 05_EVIDENCE_META/META/PROVENANCE_SCHEMA.md
  - 90_AUTOMATION/README.md
result: METHOD_UPDATE
write_to:
  - Skills
  - Trading System
  - State
  - Evidence Meta
  - Automation
```

## 前台摘要

- **新东西是什么：**把旧 AI 周期探索里的主线框架、瓶颈三倍反推、工程师信号、训练日志、信源 SOP、refresh targets、source health 和研究对象清单拆分并入当前体系。
- **为什么重要：**旧 AI 周期是旧系统里最容易被误用的一组材料：既有好方法，也有过期公司清单、旧工具状态和旧运行命令。必须把方法保留，把历史状态降权。
- **现在做什么：**当前调用以 canonical 文件为准；旧 AI 周期原文只作来源和审计线索。

## 吸收映射

| 来源 | 写入 | 吸收内容 |
|---|---|---|
| `AI投资主线.md` | `STRUCTURAL_CHANGE_BOTTLENECK.md` | AI 研究不是找 AI 公司，而是找主矛盾迁移后的新瓶颈和收费权 |
| `BOTTLENECK_3X_FRAMEWORK.md` | `STRUCTURAL_CHANGE_BOTTLENECK.md` | 六类瓶颈测试、三年三倍反推过滤器、五层 AI 瓶颈和候选分类 |
| `ENGINEER_SIGNAL_3X_RADAR.md` | `STRUCTURAL_CHANGE_BOTTLENECK.md` | 工程师时间投票、toy 到 tool 到平台/基础设施、信号到公司映射 |
| `结构性转变判断框架.md` | `STRUCTURAL_CHANGE_BOTTLENECK.md` | 结构转变、飞轮、权力来源、公司类型框架适配 |
| `FRAMEWORK_TRAINING_LOG.md` | `STRUCTURAL_CHANGE_BOTTLENECK.md`、`03_FEEDBACK_LOOP.md` | 训练样本、新判别式、旧框架修正、下一队列和版本边界 |
| `MINDSPACE_SOURCE_MCP_SOP.md` | `PROVENANCE_SCHEMA.md`、`90_AUTOMATION/README.md` | 本地优先、source-first、回源、fallback 和证据日志字段 |
| `CROSS_MARKET_V2_RUN_BOUNDARIES.md` | `90_AUTOMATION/README.md` | dry-run、工具白名单、写入白名单、run_token、host validation 和失败态边界 |
| `README.md` | `90_AUTOMATION/README.md`、`WATCHLISTS/README.md` | 旧 AI 周期目标和历史队列的权限边界 |
| `refresh_targets_2026-05-24.md` | `90_AUTOMATION/README.md`、`WATCHLISTS/README.md` | refresh target 的运行形状、优先级和 stale 状态 |
| `source_health_2026-05-24.md` | `PROVENANCE_SCHEMA.md`、`90_AUTOMATION/README.md` | 工具健康检查要本轮验证，旧可用性只作历史记录 |
| `信息重整与趋势刷新计划_2026-05-24.md` | `PROVENANCE_SCHEMA.md`、`90_AUTOMATION/README.md` | 本地库、MCP/source、fallback、证据日志和产业层刷新链路 |
| `研究对象清单.md` | `WATCHLISTS/README.md` | 研究对象清单属于 State，只改变研究优先级 |

## 明确降权或废止

- 旧公司清单、旧 watchlist、旧 refresh targets、旧 source health、旧 score table 和旧队列状态都不是当前事实。
- 旧命令示例、旧工具路径和 Claude/MCP 桥接方式不作为当前执行指令；当前环境必须重新验证。
- 旧三倍候选、总分、分类、交易权限、AI 共识、固定分数和未校准概率不进入四票、EV、仓位或交易动作。
- 工程师信号、GitHub 活跃、社交热度和产品 demo 只更新研究问题；未进收入、毛利、经营利润、现金流和估值前，不更新经营票。
- 私有公司只能进入信号、产业图谱或 IPO 观察，不写当前交易动作。
- 自动化永远不能改主账、券商事实、仓位参数、ledger 或交易权限。

## 边界

- 本回执不授权交易、仓位、参数或主账修改。
- `merged` 只表示可复用方法已经进入当前体系，不表示 Murphy 确认旧 AI 周期所有公司判断。
- 重新使用任何旧 AI 周期公司结论前，必须按当前 provenance schema 回源刷新。
