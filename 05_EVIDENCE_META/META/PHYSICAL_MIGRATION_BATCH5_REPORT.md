---
title: physical_migration_batch5_report
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

# Physical Migration Batch 5 Report

## 先说人话

**今天发生了什么：**执行第五批可逆物理迁移：44 个旧方法来源已镜像到 Method Source Review Queue。

**为什么重要：**至此 backlog 中 611 个旧 Markdown 都已有新结构接入点；但旧方法全文合并仍未完成，需要逐段吸收。

**现在做什么：**下一步应按 canonical Skill 分组做全文合并和回执，不再新增孤立方法页。

| 批次 | 数量 | 索引 |
|---|---:|---|
| Method Source Review Queue | 44 | [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE_INDEX]] |

## 按旧角色

| 旧角色 | 数量 |
|---|---:|
| `legacy_ai_cycle_method` | 12 |
| `legacy_analysis_method_source` | 5 |
| `legacy_basic_method_source` | 15 |
| `legacy_method_source` | 7 |
| `legacy_options_method` | 4 |
| `legacy_root_framework` | 1 |

## 按目标

| 目标 | 数量 |
|---|---:|
| `02_术/SKILLS` | 27 |
| `02_术/SKILLS + 01_道/PHILOSOPHY_INBOX + 05_EVIDENCE_META/EVIDENCE` | 1 |
| `02_术/SKILLS + 90_AUTOMATION` | 12 |
| `02_术/SKILLS/OPTIONS` | 4 |

## 边界

- 本批次只完成可逆物理接入，不代表方法正文合并完成。
- 合并前旧方法仍为 `decision_authority: none` 或来源材料。
- 旧方法进入 canonical Skill 后必须保留来源回链和失败条件。
