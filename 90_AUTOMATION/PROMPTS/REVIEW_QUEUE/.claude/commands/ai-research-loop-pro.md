---
description: Historical AI research loop PRO (no current authority)
argument-hint: [pending|data-gap|all|company name/ticker]
layer: AUTOMATION
primary_role: legacy_claude_automation
status: superseded
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
legacy_metadata_added: normalized
legacy_path: ".claude/commands/ai-research-loop-pro.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---


> 历史命令，不再授权当前判断。当前跨市场研究请使用 `ai-cycle-cross-market-v2` 的 dry-run 预检或手动执行 `AI周期探索/0_总览/run_nightly_research_loop.sh`。

读取 `/Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索/0_总览/LOOP_PROMPT_PRO.md`，并按 `AI_RESEARCH_LOOP_PRO` 模式执行。

用户参数：`$ARGUMENTS`

参数解释：
- `pending`：只处理 `company_queue.md` 中第一个 pending 公司。
- `data-gap`：只修复 `company_score_table.md` 中 `MCP无覆盖`、`数据不足`、`覆盖不足`、`路径待验证` 且缺少 agent-reach 证据链的公司。
- `all` 或空参数：pending 优先；没有 pending 时自动进入 data-gap 修复；全部完成后更新投资池并输出 `<promise>AI_RESEARCH_LOOP_PRO_COMPLETE</promise>`。
- 公司名或 ticker：只处理该公司，仍必须遵守 PRO 证据闭环规则。

执行硬约束：
- 你是循环调度器，不是随意发挥的研究员。
- 每轮只处理一个公司或对象。
- 必须 MCP-first，先读 `MINDSPACE_SOURCE_MCP_SOP.md`，再调用 Mindspace Source MCP `health_check`。
- 不要用 `listMcpResources` 判断 Mindspace Source MCP 是否可用。
- 如果 `health_check` 失败，本轮 blocked，写入 `evidence_log.md` 和 `run_log.md`，不要用联网搜索绕过 MCP health gate。
- 如果 Mindspace MCP 覆盖不足且问题关键，必须加载 `agent-reach` skill，用 agent-reach 的 Exa/Jina/web-reader 路径补证据。
- 禁止使用内置 `web_search`。
- 没有 agent-reach 尝试记录，不得把公司标为“数据不足完成”。
- 核心判断必须能追溯到 `evidence_log.md`。

完成前检查：
- `company_research.md`、`scorecard.md`、`evidence_log.md`、`next_questions.md` 已更新。
- `company_score_table.md` 已把可补足的 `MCP无覆盖` 替换成具体判断。
- fallback 后仍证据不足的公司，已明确写成 `evidence_limited_after_fallback`，并列出缺口、关键词和链接。
- `run_log.md` 已记录本轮对象、Mindspace 状态、agent-reach 状态和最终 evidence status。
- Codex/AI 生成的长篇调研报告必须保留为原始长文或证据底稿；最终进入分析体系的内容必须萃取成关键逻辑、证据链、论证结论、估值路径、失败条件和待验证信号。
- 单一标的输出放入该标的现有目录；多个标的、组合比较、场景分析放入 `/Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/分析报告/archive/`。
- 输出文件统一使用 `YYMMDD标的_内容.md`；若同时保留长报告原文，使用同前缀加 `_AI长报告原文.md`。
