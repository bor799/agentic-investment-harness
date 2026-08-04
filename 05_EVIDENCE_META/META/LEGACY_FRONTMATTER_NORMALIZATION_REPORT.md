---
title: legacy_frontmatter_normalization_report
date: 2026-07-24
updated: 2026-07-24
layer: META
primary_role: legacy_frontmatter_normalization_report
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# Legacy Frontmatter Normalization Report

## 先说人话

**今天发生了什么：**已有 YAML frontmatter 的旧文件已补齐 `layer / primary_role / decision_authority` 等权限字段；旧 `status` 如与迁移权限冲突，已写入 `legacy_status` 保留原语义。

**为什么重要：**旧研究报告、旧观察状态和旧方法草稿仍可作为证据、案例或历史来源被检索，但不会因为原来的 `status` 或标题误拿当前决策权限。

**现在做什么：**继续按新前台工作；需要引用旧材料时，优先通过新索引、dossier、Case Gym 或吸收回执进入，而不是直接把旧文件当当前系统。

## 结果

| 指标 | 数量 |
|---|---:|
| 旧结构 Markdown | 612 |
| 有 frontmatter（不含特殊跳过） | 611 |
| 本次规范化文件 | 128 |
| 缺 `layer` | 0 |
| 缺 `primary_role` | 0 |
| 缺 `status` | 0 |
| 缺 `decision_authority` | 0 |

CSV 明细：[[05_EVIDENCE_META/META/LEGACY_FRONTMATTER_NORMALIZATION_REPORT.csv]]

## 特殊说明

- `AGENTS.md` 仍作为 Codex 操作规则文件保留原样，不在顶部加入 YAML。
- 本脚本不移动、不删除旧正文；它只补权限 metadata 与迁移目标。
- `legacy_status` 是旧文件自己的历史状态，不再授权当前交易动作。
