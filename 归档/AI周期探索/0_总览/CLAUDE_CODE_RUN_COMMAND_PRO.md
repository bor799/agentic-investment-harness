---
title: "CLAUDE_CODE_RUN_COMMAND_PRO"
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
legacy_path: "AI周期探索/0_总览/CLAUDE_CODE_RUN_COMMAND_PRO.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Claude Code 启动命令：AI 投资研究循环 PRO

> [!warning] 历史命令，不再授权当前判断
> 保留用于追溯旧 PRO 循环。新的跨市场 v2 入口是 `run_nightly_research_loop.sh`；不要用本命令生成当前投资结论。

用途：修复普通循环中“Mindspace MCP 覆盖不足就直接给框架结论”的问题。PRO 模式会先 MCP-first；当 MCP 覆盖不足但问题关键时，强制使用 `agent-reach` skill 联网补证据。

```text
/ralph-loop "读取 /Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索/0_总览/LOOP_PROMPT_PRO.md。你是 AI_RESEARCH_LOOP_PRO：每轮只处理一个公司；pending 优先；无 pending 时扫描 company_score_table.md 中 MCP无覆盖/数据不足/覆盖不足的公司做 PRO 修复。必须 MCP-first；MCP health_check 失败则 blocked；MCP 覆盖不足且问题关键时必须加载 agent-reach skill 联网补证据；禁止内置 web_search；没有 agent-reach 尝试记录不得把公司标为数据不足完成。" --max-iterations 120 --completion-promise "AI_RESEARCH_LOOP_PRO_COMPLETE"
```

如果只想修复当前这批覆盖不足公司，可以在 Claude Code 中运行项目命令：

```text
/ai-research-loop-pro data-gap
```
