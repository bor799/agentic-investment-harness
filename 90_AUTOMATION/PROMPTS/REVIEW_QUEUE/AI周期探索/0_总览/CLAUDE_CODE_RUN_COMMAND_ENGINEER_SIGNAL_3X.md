---
title: "CLAUDE_CODE_RUN_COMMAND_ENGINEER_SIGNAL_3X"
date: 2026-07-24
updated: 2026-07-24
layer: AUTOMATION
primary_role: legacy_prompt_or_command
status: superseded
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: operational
legacy_metadata_added: true
legacy_path: "AI周期探索/0_总览/CLAUDE_CODE_RUN_COMMAND_ENGINEER_SIGNAL_3X.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# ENGINEER_SIGNAL_3X_LOOP 启动命令

用途：从工程师行为出发，发现“玩具 -> 企业工作流 -> 现实瓶颈 -> 可投资公司 -> 三年三倍反推”的新标的雷达。新标的先进入工程师信号覆盖层和三类 3X 池，不直接污染 70 分主评分表。

```text
/loop 20min "读取 /Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索/0_总览/LOOP_PROMPT_ENGINEER_SIGNAL_3X.md。你是 ENGINEER_SIGNAL_3X_LOOP：每轮只处理一家公司，不要进入 sandbox，全自动执行，不打断，自己调用 MCP 工具，不需要我同意，每轮只处理一个工程师信号主题；先用 Mindspace MCP，覆盖不足时必须使用 agent-reach 搜 GitHub/HN/Reddit/X/官方文档/IR/监管文件；把工程师行为映射到企业迁移、现实瓶颈、可投资标的和三年三倍反推；禁止内置 web_search；禁止无市值/收入/FCF反推就进入三倍候选池；每轮更新 ENGINEER_SIGNAL_3X_RADAR.md、BOTTLENECK_3X_FRAMEWORK.md、company_score_table.md 和对应投资池；完成首批信号后输出 <promise>ENGINEER_SIGNAL_3X_COMPLETE</promise>。" --max-iterations 30 --completion-promise "ENGINEER_SIGNAL_3X_COMPLETE"
```

完成条件：首批 8 个工程师信号都处理完，`ENGINEER_SIGNAL_3X_RADAR.md`、`company_score_table.md` 覆盖层、`三倍候选池.md`、`瓶颈观察池.md`、`证据不足池.md` 彼此一致，且没有无市值/收入/FCF反推的标的进入三倍候选池。

