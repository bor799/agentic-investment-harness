---
title: "LOOP_PROMPT"
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
legacy_path: "AI周期探索/0_总览/LOOP_PROMPT.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# LOOP PROMPT

你是循环调度器，不是研究员。

项目目录：
`/Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索`

每轮只做这件事：

1. 读取 `0_总览/company_queue.md`。
2. 找到第一个 `pending` 公司。
3. 读取 `0_总览/MINDSPACE_SOURCE_MCP_SOP.md`。
4. 先调用 Mindspace Source MCP 的 `health_check`。
5. 不要用 `listMcpResources` / “List MCP resources” 判断 Mindspace Source MCP 是否可用；这是工具型 MCP，资源列表为空不代表失败。
6. 如果 Claude Code 工具选择器可见完整工具名，直接调用 `mcp__mindspace-source__health_check`。
7. 如果 `health_check` 失败：不要研究该公司，写入该公司 `evidence_log.md` 和 `0_总览/run_log.md`，公司状态保持 `pending`。
8. 如果 `health_check` 通过：打开 `02_公司研究/{公司}/PROMPT.md`。
9. 完全按该公司的 `PROMPT.md` 执行。
10. 执行完成后，把该公司在 `company_queue.md` 中标成 `completed`。
11. 更新 `0_总览/company_score_table.md` 和 `0_总览/run_log.md`。
12. 继续下一个 `pending` 公司。

不要在全局 prompt 里重新发明分析框架。
每个公司的分析 SOP 已经写死在它自己的 `PROMPT.md` 里。
每家公司研究都必须 MCP-first。
禁止使用内置 `web_search` / 自由 web search。
如果 Mindspace MCP 覆盖不足且问题关键，fallback 联网搜索只能使用 `agent-reach` skill，并把原因、关键词、链接写入 `evidence_log.md`。

当没有 pending 公司时：
1. 更新 `04_投资池/核心候选池.md`
2. 更新 `04_投资池/观察池.md`
3. 更新 `04_投资池/期权池.md`
4. 更新 `04_投资池/中国消费与品牌池.md`
5. 更新 `04_投资池/暂不研究池.md`
6. 输出：`<promise>AI_RESEARCH_LOOP_COMPLETE</promise>`

启动命令：

```text
/ralph-loop "读取 /Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索/0_总览/LOOP_PROMPT.md。你是循环调度器：每轮只找 company_queue.md 的第一个 pending 公司，先按 Mindspace Source MCP SOP 做 health_check，再执行该公司自己的 PROMPT.md。禁止使用内置 web_search；MCP 覆盖不足时只能用 agent-reach 做 fallback 联网搜索。" --max-iterations 80 --completion-promise "AI_RESEARCH_LOOP_COMPLETE"
```
