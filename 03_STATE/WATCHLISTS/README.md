---
title: watchlist_index
date: 2026-07-23
updated: 2026-07-24
layer: STATE
primary_role: watchlist_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/README.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/refresh_targets_2026-05-24.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/研究对象清单.md
data_cutoff:
expires_at:
---

# Watchlists

观察池、核心池、暂不研究池和投资池都属于 State，不拥有交易授权。

## 入口

| 入口 | 用途 |
|---|---|
| [[03_STATE/WATCHLISTS/AI_CYCLE_WATCHLISTS_INDEX]] | 旧 AI 周期投资池 |
| [[03_STATE/WATCHLISTS/MIRRORED_LEGACY_WATCHLISTS_INDEX]] | 已镜像入新结构的旧投资池原文 |

观察池只改变研究优先级。进入动作前必须回到 [[02_术/TRADING_SYSTEM/00_DECISION_CONTRACT]]。

## 旧 AI 周期清单边界

`研究对象清单`、旧投资池、refresh targets 和 company queue 只说明当时被纳入观察或刷新计划，不说明当前仍值得研究，更不说明可以建立风险。

清单类 State 必须补：

```yaml
watchlist_item:
  canonical_id:
  name:
  ticker:
  market:
  current_bucket:
  reason_to_watch:
  next_number:
  data_cutoff:
  expires_at:
  refresh_status: current | stale | evidence_limited_after_fallback
```

旧 AI 周期标的若重新进入当前系统，先写 `refresh_status: stale`，再按 [[05_EVIDENCE_META/META/PROVENANCE_SCHEMA]] 回源刷新。没有新证据时，只能 `继续观察` 或 `不投入`。
