---
title: superseded_state_archive
date: 2026-07-24
updated: 2026-07-24
layer: META
primary_role: superseded_state_archive
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# Superseded State Archive

## 先说人话

**今天发生了什么：**旧评分、旧每日判断和历史 State 被集中到 superseded archive。

**为什么重要：**这些材料能解释系统当时怎么想，但不能继续冒充当前判断、当前排序或当前仓位依据。

**现在做什么：**引用这里的材料时，只能作为历史 State、方法复盘或错误校准样本。

| 入口 | 用途 |
|---|---|
| [[05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/OLD_SCORECARDS_INDEX]] | 旧 `/70` scorecard 登记 |
| [[05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/MIRRORED_LEGACY_SCORECARDS_INDEX]] | 已镜像入新结构的旧 scorecard 原文 |
| [[05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/ANALYSIS_STATE_ARCHIVE_INDEX]] | 分析报告中的历史 State |
| [[05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/MIRRORED_LEGACY_ANALYSIS_STATE_INDEX]] | 已镜像入新结构的旧分析 State 原文 |

## 边界

- 旧 `/70`、固定 LR、AI 自评完成度都不得授权当前交易。
- State 重新启用前必须补 `data_cutoff / expires_at / refresh_trigger`。
- 历史判断不能自动进入 MINDSET。
