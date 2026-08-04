---
title: legacy_frontmatter_patch_report
date: 2026-07-24
updated: 2026-07-24
layer: META
primary_role: legacy_frontmatter_patch_report
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# Legacy Frontmatter Patch Report

## 先说人话

**今天发生了什么：**旧结构中缺少 YAML frontmatter 的 Markdown 已批量补上 legacy metadata。

**为什么重要：**旧文件即使被搜索到，也会明确显示自己的层级、迁移目标和权限，不会因为旧标题或旧内容获得当前决策授权。

**现在做什么：**后续继续补齐已有 frontmatter 旧文件的字段一致性；`AGENTS.md` 暂不在顶部加 YAML，以免影响 Codex 规则读取。

## 结果

| 指标 | 数量 |
|---|---:|
| 旧结构 Markdown | 612 |
| 已有或已补 frontmatter | 611 |
| 仍无 frontmatter | 1 |
| 本次新增 legacy metadata | 483 |
| 特殊跳过 | 1 |

CSV 明细：[[05_EVIDENCE_META/META/LEGACY_FRONTMATTER_PATCH_REPORT.csv]]

## 跳过原因

| 文件 | 原因 |
|---|---|
| `AGENTS.md` | `special_operational_file` |
