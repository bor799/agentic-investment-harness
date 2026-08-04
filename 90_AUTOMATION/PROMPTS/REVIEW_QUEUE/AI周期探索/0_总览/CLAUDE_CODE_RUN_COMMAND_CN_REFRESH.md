---
title: "CLAUDE_CODE_RUN_COMMAND_CN_REFRESH"
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
legacy_path: "AI周期探索/0_总览/CLAUDE_CODE_RUN_COMMAND_CN_REFRESH.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Loop 启动命令：中国消费品牌 Agent-Reach 刷新循环

用途：重新刷新 11 家中国消费/品牌/制造相关公司的研究证据，优先使用 agent-reach 读取官方 IR、交易所公告、年报/季报、监管文件和中文/英文证据，替换 Wikipedia 旧财务、Google Finance 单点数据和异常值；补证后必须重新使用 `ljg-invest` 和 `comprehensive-analysis` 做结构判断、财报/估值/情绪综合分析。

本循环不改动主队列 `company_queue.md`；它使用独立队列 `cn_consumer_refresh_queue.md`。

```text
/loop 20 min "读取 /Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索/0_总览/LOOP_PROMPT_CN_CONSUMER_REFRESH.md。你是 AI_CN_CONSUMER_REFRESH_LOOP：只刷新 Xiaomi、Pop Mart、Meituan、PDD、Beike、Bilibili、Miniso、CRRC、Fuyao Glass、Aux Electric、分众传媒。每轮只处理一家公司；使用当前工作环境，不进入额外 sandbox；全自动执行，不打断用户，不为常规工具调用请求确认；自行调用当前会话可用的 MCP 工具；先做一次 MCP/agent-reach/Jina/Exa 预检并缓存；agent-reach 为主要补证路径；不硬等 Exa；优先官方IR、交易所公告、年报/季报、公司公告和可信聚合源；替换 Wikipedia/Google Finance-only 的旧证据；补证后必须重新使用 ljg-invest 和 comprehensive-analysis 做结构判断、财报、估值、情绪和验证信号分析；每家公司更新 company_research.md、scorecard.md、evidence_log.md、next_questions.md、company_score_table.md；完成 11 家后按分数表同步 5 个投资池；全部完成且证据可追溯后输出 <promise>AI_CN_CONSUMER_REFRESH_COMPLETE</promise>。" --max-iterations 40 --completion-promise "AI_CN_CONSUMER_REFRESH_COMPLETE"
```

完成条件：只有 11 家目标公司都刷新完、`company_score_table.md` 与 5 个投资池同步、证据链接可追溯时，才能输出 `<promise>AI_CN_CONSUMER_REFRESH_COMPLETE</promise>`。
