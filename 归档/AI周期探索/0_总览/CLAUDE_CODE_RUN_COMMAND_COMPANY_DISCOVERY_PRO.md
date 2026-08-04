---
title: "CLAUDE_CODE_RUN_COMMAND_COMPANY_DISCOVERY_PRO"
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
legacy_path: "AI周期探索/0_总览/CLAUDE_CODE_RUN_COMMAND_COMPANY_DISCOVERY_PRO.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# COMPANY_DISCOVERY_PRO_LOOP 启动命令

用途：把新发现公司纳入公司级研究循环，同时把交易权限和研究价值分开处理。创业板、科创板、港股、美股权限只作为输出字段，不作为跳过研究的理由。

```text
/loop 30min "读取 /Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索/0_总览/LOOP_PROMPT_COMPANY_DISCOVERY_PRO.md。你是 COMPANY_DISCOVERY_PRO_LOOP：每轮只处理一个公司；优先处理 new_company_intake_queue.md 中 pending_research 公司；不要因为创业板/科创板权限问题跳过研究，只在输出中标注交易权限；必须 MCP-first；MCP health_check 失败则 blocked；MCP 覆盖不足且问题关键时必须加载 agent-reach skill 联网补证据；禁止内置 web_search；没有 agent-reach 尝试记录不得把公司标为数据不足完成；每轮更新公司研究文件、company_score_table.md、new_company_intake_queue.md、run_log.md。" --max-iterations 120 --completion-promise "COMPANY_DISCOVERY_PRO_COMPLETE"
```

完成条件：
- `new_company_intake_queue.md` 中首批 8 家公司都变为 `research_complete`、`evidence_limited_after_fallback` 或 `blocked_mcp_unavailable`。
- 每家公司研究文件、`company_score_table.md`、`run_log.md` 已同步。
- 每家公司都明确写出交易权限状态，不把权限状态当作投资结论。
