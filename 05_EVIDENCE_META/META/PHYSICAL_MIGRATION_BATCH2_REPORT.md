---
title: physical_migration_batch2_report
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

# Physical Migration Batch 2 Report

## 先说人话

**今天发生了什么：**执行第二批可逆物理迁移：旧 Hypothesis Queue、Watchlists、Automation State 和 `/70` scorecard 已镜像到新结构。

**为什么重要：**这些文件最容易被误读为“当前排序”或“当前任务”。镜像后它们留作历史 State，不再拥有当前决策权限。

**现在做什么：**后续继续迁移公司 Evidence 和方法正文；本批次只证明 State/scorecard 镜像完成。

| 批次 | 数量 | 索引 |
|---|---:|---|
| Hypothesis Queue 镜像 | 117 | [[03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE_INDEX]] |
| Watchlists 镜像 | 8 | [[03_STATE/WATCHLISTS/MIRRORED_LEGACY_WATCHLISTS_INDEX]] |
| Automation State 镜像 | 6 | [[03_STATE/AUTOMATION_STATE/MIRRORED_LEGACY_RUNTIME_INDEX]] |
| Scorecards 镜像 | 54 | [[05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/MIRRORED_LEGACY_SCORECARDS_INDEX]] |

## 按旧角色

| 旧角色 | 数量 |
|---|---:|
| `legacy_automation_state` | 6 |
| `legacy_company_question_state` | 117 |
| `legacy_scorecard` | 54 |
| `legacy_watchlist_state` | 8 |

## 边界

- 本批次不改写旧文件，也不删除旧文件。
- Scorecard 镜像仍为旧评分历史，不得用于当前交易授权。
- 所有 State 镜像重新启用前，必须补 `data_cutoff / expires_at / refresh_trigger`。
