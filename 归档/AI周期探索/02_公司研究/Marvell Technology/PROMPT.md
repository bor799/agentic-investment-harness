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
legacy_path: "AI周期探索/02_公司研究/Marvell Technology/PROMPT.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Marvell Technology 调研执行 Prompt

你现在只研究这一家公司，不要顺手研究其他公司。

公司：Marvell Technology
代码：MRVL
市场/板块：美股 / Nasdaq
交易权限：direct_buy_likely
是否可直接买：可直接买（取决于美股账户权限）。
初始分组：AI网络/定制芯片/数据中心互联瓶颈

核心问题：
> Marvell 是否正在从传统数据基础设施芯片公司，转向 AI 数据中心网络与定制 ASIC 的关键瓶颈供应商？

必须验证：
- AI data center、custom silicon、electro-optics、switching/DSP 的收入增速和订单可见度。
- 与 Broadcom、Nvidia、Astera Labs、Credo 等的竞争位置。
- 大客户集中度、定制芯片项目周期、毛利率和 FCF 变化。
- 三年翻倍路径是否被当前估值透支。

执行规则：
- 先读取 `../../0_总览/MINDSPACE_SOURCE_MCP_SOP.md`。
- 必须先调用 Mindspace Source MCP `health_check`。
- MCP 覆盖不足时必须加载 `agent-reach` skill，优先查公司 IR、SEC EDGAR、财报电话会、投资者日和 Nasdaq/主流财经源。
- 禁止内置 `web_search`。

输出文件：
- `company_research.md`
- `scorecard.md`
- `evidence_log.md`
- `next_questions.md`
- 同步更新 `../../0_总览/new_company_intake_queue.md`、`../../0_总览/company_score_table.md`、`../../0_总览/run_log.md`
