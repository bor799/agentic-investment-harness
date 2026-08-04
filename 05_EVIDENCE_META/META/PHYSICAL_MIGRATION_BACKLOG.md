---
title: physical_migration_backlog
date: 2026-07-24
updated: 2026-07-24
layer: META
primary_role: physical_migration_backlog
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
  - 05_EVIDENCE_META/META/LEGACY_FRONTMATTER_NORMALIZATION_REPORT.md
---

# Physical Migration Backlog

## 先说人话

**今天发生了什么：**旧结构文件已进入物理迁移 backlog；本文件只排队，不移动、不删除。

**为什么重要：**后续搬文件必须先知道每个旧文件应该去 Evidence、State、Case、Method 还是 Automation；否则最容易把历史材料误当当前判断。

**现在做什么：**继续把旧结构当只读来源；真正移动前，按 `next_action` 逐批执行，并保留原路径回链。

## 总览

| 指标 | 数量 |
|---|---:|
| backlog 文件 | 611 |
| 特殊跳过 | 1 |

CSV 明细：[[05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.csv]]

## 按层级

| layer | 数量 |
|---|---:|
| `AUTOMATION` | 73 |
| `CASE` | 9 |
| `CONSTITUTION` | 1 |
| `EVIDENCE` | 250 |
| `META` | 61 |
| `METHOD` | 44 |
| `STATE` | 173 |

## 按下一动作

| next_action | 数量 |
|---|---:|
| `attach_to_company_or_theme_dossier_without_rewriting_thesis` | 236 |
| `copy_to_ai_long_report_archive_with_backlink` | 14 |
| `extract_case_card_then_keep_source_as_evidence` | 9 |
| `keep_as_governance_history_or_superseded_state` | 61 |
| `merge_relevant_rules_into_canonical_skill_then_archive_source` | 44 |
| `promote_or_copy_current_runtime_after_manual_check` | 2 |
| `review_before_move` | 72 |
| `snapshot_into_state_archive_or_watchlist_then_expire_legacy` | 173 |

## 按删除标记

| deletion_flag | 数量 |
|---|---:|
| `X?_directory_ownership_required` | 4 |
| `X?_semantic_diff_required` | 2 |
| `never_auto_delete` | 242 |
| `not_reviewed_for_deletion` | 363 |

## 只读冻结规则

1. 旧结构文件默认只读，允许补 metadata、链接回链和迁移标记，不把旧文件继续当当前前台维护。
2. 物理搬迁时优先复制/抽取到新结构，再把旧路径改为 redirect 或 archive pointer。
3. `never_auto_delete` 不能自动删除；它们包括 AI 长报告、公司证据、分析原文和 Case 来源。
4. `X?` 只能表示删除候选，不是删除授权。
5. `decision_authority: none` 的旧文件不得直接授权交易、仓位、MINDSET 或 Constitution。
