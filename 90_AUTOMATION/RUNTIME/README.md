---
title: runtime_index
date: 2026-07-23
updated: 2026-07-23
layer: AUTOMATION
primary_role: runtime_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# Runtime

运行日志、queue、last outcome 和状态快照。

## 当前可运行入口

- [[90_AUTOMATION/RUNTIME/STAGING/README|STAGING]]：`AI_BELIEF_LOOP`
  的未核验候选；不是 Source、Moment 或当前判断。
- [[90_AUTOMATION/RUN_LOG/README|RUN_LOG]]：只保存哈希、模式、结果、
  创建路径与错误码，不保存原文。

任何 Staging 晋升都必须重新回源，并经过 Murphy 明确写入、Reviewer 与
Validator。系统没有安装定时任务时，不得把 runner 文件的存在描述为
“已经自动监控”。
