---
title: phase2_materialization_log
date: 2026-07-23
updated: 2026-07-23
layer: META
primary_role: materialization_log
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# Phase 2 Materialization Log

## 先说人话

**今天发生了什么：**在权限接管之后，旧 AI 周期公司研究、问题队列、投资池和自动化运行材料被非破坏性接入新结构。

**为什么重要：**旧材料没有被删除或粗暴搬家，但现在已经能从新前台找到，并且每类材料的权限被分开。

**现在做什么：**后续物理迁移时，按这些索引逐批把旧文件移入 dossier、State Archive、Prompt Archive 或 Case Gym。

## 已物化索引

| 新索引 | 接管对象 | 状态 |
|---|---|---|
| [[05_EVIDENCE_META/EVIDENCE/COMPANIES/COMPANY_DOSSIER_INDEX]] | `AI周期探索/02_公司研究`、`AI周期探索/标的研究` | 62 个公司/标的 dossier |
| [[03_STATE/HYPOTHESIS_QUEUE/COMPANY_QUESTIONS_INDEX]] | `research_task.md`、`next_questions.md`、`next_signals.md` | State，2026-08-23 过期 |
| [[03_STATE/WATCHLISTS/AI_CYCLE_WATCHLISTS_INDEX]] | `AI周期探索/04_投资池/*.md` | State，2026-08-06 过期 |
| [[90_AUTOMATION/PROMPTS/AI_CYCLE_PROMPTS_INDEX]] | `LOOP_PROMPT*`、`CLAUDE_CODE_RUN_COMMAND*` | Automation |
| [[90_AUTOMATION/PIPELINES/AI_CYCLE_PIPELINES_INDEX]] | 旧 `.py/.sh` 脚本 | Automation |
| [[90_AUTOMATION/RUNTIME/AI_CYCLE_RUNTIME_INDEX]] | 旧 queue、run log、json/jsonl、watchlist | Runtime / State |
| [[05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/OLD_SCORECARDS_INDEX]] | 旧 `scorecard.md` | Superseded State，`decision_authority: none` |
| [[05_EVIDENCE_META/EVIDENCE/THEMES/ANALYSIS_REPORTS_INDEX]] | `分析报告/` 主题 Evidence 与方法报告 | Evidence / Method Source |
| [[05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/ANALYSIS_STATE_ARCHIVE_INDEX]] | 每日决策简报、每日假设跟踪、监控基线 | Superseded State |
| [[05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/AI_LONG_REPORTS_INDEX]] | `分析报告/` AI 长报告原文 | Evidence Archive |
| [[02_术/SKILLS/BASIC_CONCEPTS_METHOD_SOURCE_INDEX]] | `基础概念/交易策略组合` | Method Source |
| [[05_EVIDENCE_META/EVIDENCE/COMPANIES/BASIC_CONCEPTS_COMPANY_EVIDENCE_INDEX]] | `基础概念/实体商` 公司材料 | Company Evidence |
| [[04_CASE_GYM/TRADE_LOG/LEGACY_TRADE_CASES_INDEX]] | `📈 个人交易手册` 真实交易和未交易 Case | Case |
| [[04_CASE_GYM/CASE_FRONTSTAGE_INDEX]] | 501096、天赐、名创、地平线、LMND、泡泡玛特未买入对照 | Standardized Case |
| [[04_CASE_GYM/RESEARCH_CASES/BASIC_CONCEPTS_CASE_SOURCE_INDEX]] | 基础概念中的原始短记、IP 原文和公司决策短记 | Case Source |
| [[05_EVIDENCE_META/META/ROOT_LEGACY_INDEX]] | 根目录旧框架、交易手册、看板、AGENTS | Meta Router |
| [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS_INDEX]] | 8 个代表性材料/材料族 | Absorption Receipts |

## 生成脚本

第一批索引由 [[90_AUTOMATION/PIPELINES/phase2_materialize_indexes.py]] 生成。第二批旧报告、基础概念和 Case 分层由 [[90_AUTOMATION/PIPELINES/phase2_materialize_legacy_layers.py]] 生成。脚本只写新索引和 dossier README，不移动、不删除旧文件。

## 权限边界

- 公司 dossier 是 Evidence 入口，不是当前投资结论。
- 问题队列和投资池是 State，会过期。
- Prompt 和脚本是 Automation，不能自动写 MINDSET / Constitution。
- 旧 scorecard 是历史评分，不进入 EV、仓位或动作。
- 个人交易手册里的单个 Case 不能直接新增道，只能生成观察、临时防火墙、方法更新或候选。
- 分析报告里的每日简报和每日跟踪是 State，会过期。
- 吸收回执只说明材料改变了系统什么，不把外部作者或 AI 输出写成 Murphy 第一人称。
