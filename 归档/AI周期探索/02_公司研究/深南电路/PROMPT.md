---
title: "PROMPT"
date: 2026-07-24
updated: 2026-07-24
layer: AUTOMATION
primary_role: legacy_company_prompt
status: superseded
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: operational
legacy_metadata_added: true
legacy_path: "AI周期探索/02_公司研究/深南电路/PROMPT.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 深南电路 调研执行 Prompt

你现在只研究这一家公司，不要顺手研究其他公司。

公司：深南电路
代码：002916.SZ
市场/板块：A股 / 深交所主板
交易权限：direct_buy_likely
是否可直接买：可直接买（A股主板权限）。
初始分组：PCB/封装基板/高速互联

核心问题：
> 深南电路是否能凭借 PCB、封装基板、电子装联三条线，在 AI 服务器和先进封装升级中形成更高估值中枢？

必须验证：
- AI服务器PCB、封装基板、FC-BGA/IC载板的订单、良率和利润率。
- 深南电路在通信、服务器、封装基板之间的结构升级是否真实。
- 与沪电股份、胜宏科技、广合科技、生益电子的竞争位置。
- 三年翻倍路径更依赖 PCB 放量还是封装基板突破。

执行规则：
- 先读取 `../../0_总览/MINDSPACE_SOURCE_MCP_SOP.md`。
- 必须先调用 Mindspace Source MCP `health_check`。
- MCP 覆盖不足时必须加载 `agent-reach` skill，优先查巨潮资讯、深交所、公司公告、年报、季报和投资者关系记录。
- 禁止内置 `web_search`。

输出文件：
- `company_research.md`
- `scorecard.md`
- `evidence_log.md`
- `next_questions.md`
- 同步更新 `../../0_总览/new_company_intake_queue.md`、`../../0_总览/company_score_table.md`、`../../0_总览/run_log.md`
