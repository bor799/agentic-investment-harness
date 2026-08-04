---
title: "CLAUDE_CODE_RUN_COMMAND"
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
legacy_path: "AI周期探索/0_总览/CLAUDE_CODE_RUN_COMMAND.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Claude Code 启动命令

```text
/ralph-loop "读取 /Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索/0_总览/LOOP_PROMPT.md。你是循环调度器：每轮只找 company_queue.md 的第一个 pending 公司，先按 Mindspace Source MCP SOP 做 health_check，再执行该公司自己的 PROMPT.md。禁止使用内置 web_search；MCP 覆盖不足时只能用 agent-reach 做 fallback 联网搜索。" --max-iterations 80 --completion-promise "AI_RESEARCH_LOOP_COMPLETE"
```
