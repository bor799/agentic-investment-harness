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
legacy_path: "AI周期探索/02_公司研究/沪电股份/PROMPT.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 沪电股份 调研执行 Prompt

你现在只研究这一家公司，不要顺手研究其他公司。

公司：沪电股份
代码：002463.SZ
市场/板块：A股 / 深交所主板
交易权限：direct_buy_likely
是否可直接买：可直接买（A股主板权限）。
初始分组：AI服务器PCB/高速互联

核心问题：
> 沪电股份是否是 AI 服务器和高速交换机 PCB 升级周期中最纯正、利润留存最强的 A 股主板标的之一？

必须验证：
- AI服务器、交换机、数据中心相关 PCB 订单和收入占比。
- 高多层板、高速材料、海外客户是否带来毛利率中枢上移。
- 与胜宏科技、深南电路、广合科技、台系 PCB 厂的竞争位置。
- 当前估值是否已经定价 AI PCB 增长。

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
