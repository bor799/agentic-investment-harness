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
legacy_path: "AI周期探索/02_公司研究/广合科技/PROMPT.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 广合科技 调研执行 Prompt

你现在只研究这一家公司，不要顺手研究其他公司。

公司：广合科技
代码：001389.SZ / 01989.HK
市场/板块：A股/H股 / 深交所主板/港股主板
交易权限：direct_buy_likely
是否可直接买：可直接买（A股主板或港股权限）；需分别比较 A/H 价格、流动性和估值差。
初始分组：算力服务器PCB/高速高频PCB

核心问题：
> 广合科技是否是算力服务器 PCB 需求爆发中，兼具 A/H 交易路径和高成长弹性的核心标的？

必须验证：
- 算力服务器 PCB 收入、全球客户、订单增速和产能利用率。
- A股与H股估值差、流动性差、港股通/交易可达性。
- 与沪电股份、胜宏科技、深南电路、台系 PCB 厂的竞争位置。
- 2026 Q1 高增速是否可持续，还是上市后情绪溢价。

执行规则：
- 先读取 `../../0_总览/MINDSPACE_SOURCE_MCP_SOP.md`。
- 必须先调用 Mindspace Source MCP `health_check`。
- MCP 覆盖不足时必须加载 `agent-reach` skill，优先查巨潮资讯、深交所、HKEXnews、公司公告、招股书、年报、季报和投资者关系记录。
- 禁止内置 `web_search`。
- 必须区分 A 股 `001389.SZ` 和 H 股 `01989.HK` 的交易路径、估值和流动性。

输出文件：
- `company_research.md`
- `scorecard.md`
- `evidence_log.md`
- `next_questions.md`
- 同步更新 `../../0_总览/new_company_intake_queue.md`、`../../0_总览/company_score_table.md`、`../../0_总览/run_log.md`
