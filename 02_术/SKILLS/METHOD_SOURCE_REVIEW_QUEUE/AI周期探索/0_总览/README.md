---
title: "README"
date: 2026-07-24
updated: 2026-07-24
layer: METHOD
primary_role: legacy_ai_cycle_method
status: superseded
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
legacy_metadata_added: true
legacy_path: "AI周期探索/0_总览/README.md"
migration_target: "02_术/SKILLS + 90_AUTOMATION"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# AI 周期探索

目标：持续寻找正在发生结构性转变的公司，而不是收集 AI 概念。

## 当前循环

当前判断入口是“跨市场证据与赔率循环 v2”：

- 主提示词：`LOOP_PROMPT_CROSS_MARKET_V2.md`
- 18 对象持久化队列：`cross_market_queue_v2.json`
- 运行边界：`CROSS_MARKET_V2_RUN_BOUNDARIES.md`
- 手动脚本：`run_nightly_research_loop.sh`
- 写路径守卫：`v2_write_guard.py`
- 项目 Agent：`.claude/agents/ai-cycle-cross-market-v2.md`
- 项目命令：`.claude/commands/ai-cycle-cross-market-v2.md`

旧 `LOOP_PROMPT_PRO.md` 和旧 PRO 命令保留为历史，不再授权当前概率、总分、仓位或交易判断。

安全预检：

```bash
AI周期探索/0_总览/run_nightly_research_loop.sh --dry-run
```

`--dry-run` 不调用 Claude、不写文件、不产生 API 费用。

本项目只保留四个目录：

```text
AI周期探索/
├─ 0_总览/
├─ 01_赛道研究/
├─ 02_公司研究/
└─ 04_投资池/
```

历史单公司循环仍可追溯 `0_总览/LOOP_PROMPT.md`；新的 18 对象首轮必须读取 v2 主提示词和持久化队列。
