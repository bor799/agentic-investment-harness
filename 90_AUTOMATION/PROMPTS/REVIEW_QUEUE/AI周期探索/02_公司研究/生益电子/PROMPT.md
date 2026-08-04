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
legacy_path: "AI周期探索/02_公司研究/生益电子/PROMPT.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 生益电子 调研执行 Prompt

你现在只研究这一家公司，不要顺手研究其他公司。

公司：生益电子
代码：688183.SH
市场/板块：A股 / 上交所科创板
交易权限：requires_star_permission
是否可直接买：未开科创板则不能直接买；权限问题不影响本轮研究。
初始分组：高端PCB/服务器与通信设备

核心问题：
> 生益电子是否能借 AI 服务器、通信设备和高端 PCB 升级周期，从周期性 PCB 制造商转为高附加值供给方？

必须验证：
- AI服务器、通信设备、网络设备 PCB 的收入占比和订单趋势。
- 与生益科技材料协同是否形成真实优势。
- 再融资扩产是否改善产品结构，还是带来稀释和产能风险。
- 科创板权限只作为交易限制，不作为研究结论。

执行规则：
- 先读取 `../../0_总览/MINDSPACE_SOURCE_MCP_SOP.md`。
- 必须先调用 Mindspace Source MCP `health_check`。
- MCP 覆盖不足时必须加载 `agent-reach` skill，优先查上交所、巨潮资讯、公司公告、年报、季报、募集说明书和投资者关系记录。
- 禁止内置 `web_search`。
- 不要因为科创板权限问题跳过研究，只在输出中标注交易权限。

输出文件：
- `company_research.md`
- `scorecard.md`
- `evidence_log.md`
- `next_questions.md`
- 同步更新 `../../0_总览/new_company_intake_queue.md`、`../../0_总览/company_score_table.md`、`../../0_总览/run_log.md`
