---
title: physical_migration_batch3_report
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

# Physical Migration Batch 3 Report

## 先说人话

**今天发生了什么：**执行第三批可逆物理迁移：旧公司/标的 Evidence 与主题 Evidence 已镜像到新 Evidence 层。

**为什么重要：**这是旧库最大的证据块。镜像后，研究可以从新结构进入并追溯旧原文，但旧文件仍不拥有当前交易权限。

**现在做什么：**后续继续迁移方法正文、自动化 prompts 和历史治理材料；本批次只证明 Evidence 镜像完成。

| 批次 | 数量 | 索引 |
|---|---:|---|
| 公司/标的 Evidence 镜像 | 191 | [[05_EVIDENCE_META/EVIDENCE/COMPANIES/MIRRORED_LEGACY_COMPANY_EVIDENCE_INDEX]] |
| 主题 Evidence 镜像 | 45 | [[05_EVIDENCE_META/EVIDENCE/THEMES/MIRRORED_LEGACY_THEME_EVIDENCE_INDEX]] |

## 按旧角色

| 旧角色 | 数量 |
|---|---:|
| `legacy_analysis_evidence` | 40 |
| `legacy_company_evidence` | 183 |
| `legacy_company_router` | 8 |
| `legacy_theme_evidence` | 5 |

## 按迁移目标

| 迁移目标 | 数量 |
|---|---:|
| `05_EVIDENCE_META/EVIDENCE/COMPANIES` | 191 |
| `05_EVIDENCE_META/EVIDENCE/THEMES` | 45 |

## 边界

- 本批次复制旧原文，不删除、不移动旧文件。
- 镜像 Evidence 仍是 `decision_authority: none`。
- 旧研究结论重新进入正文前，必须按当前决策合同萃取证据链、失败条件和待验证信号。
