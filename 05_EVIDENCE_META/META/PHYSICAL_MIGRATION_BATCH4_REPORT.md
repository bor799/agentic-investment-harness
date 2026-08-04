---
title: physical_migration_batch4_report
date: 2026-07-24
updated: 2026-07-24
layer: META
primary_role: physical_migration_batch_report
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
  - 05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.md
---

# Physical Migration Batch 4 Report

## 先说人话

**今天发生了什么：**执行第四批可逆物理迁移：治理历史镜像、自动化 review queue 和当前自动化候选副本已接入新结构。

**为什么重要：**这一步处理的是最容易误升权的材料：旧认知模型、旧审计表、旧 prompt 和旧命令。它们现在有明确位置，但仍没有当前交易权限。

**现在做什么：**后续继续处理方法正文全文合并、Case 结算和吸收回执；自动化 review queue 需要逐项审查后才能晋升 canonical。

| 批次 | 数量 | 索引 |
|---|---:|---|
| 治理历史镜像 | 7 | [[05_EVIDENCE_META/META/MIRRORED_LEGACY_GOVERNANCE_INDEX]] |
| 自动化 Review Queue | 72 | [[90_AUTOMATION/PROMPTS/AUTOMATION_REVIEW_QUEUE_INDEX]] |
| 当前自动化候选 | 2 | [[90_AUTOMATION/PROMPTS/CURRENT_CANDIDATES_INDEX]] |

## 按旧角色

| 旧角色 | 数量 |
|---|---:|
| `audit_proposal` | 1 |
| `legacy_ai_hypothesis_redirect` | 1 |
| `legacy_claim_ledger_redirect` | 1 |
| `legacy_claude_automation` | 3 |
| `legacy_codex_automation_design` | 2 |
| `legacy_company_prompt` | 53 |
| `legacy_coverage_redirect` | 1 |
| `legacy_home_redirect` | 1 |
| `legacy_ploymarket_automation` | 2 |
| `legacy_prompt_or_command` | 13 |
| `legacy_provenance_redirect` | 1 |
| `legacy_redirect` | 1 |
| `legacy_rules_redirect` | 1 |

## 边界

- Review Queue 不等于当前有效 prompt。
- Current Candidates 仍需手工边界核验。
- 治理历史镜像不进入 MINDSET / Constitution。
