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
legacy_path: "AI周期探索/02_公司研究/胜宏科技/PROMPT.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 胜宏科技 调研执行 Prompt

你现在只研究这一家公司，不要顺手研究其他公司。

公司：胜宏科技
代码：300476.SZ
市场/板块：A股 / 深交所创业板
交易权限：requires_chinext_permission
是否可直接买：需确认创业板权限；权限问题不影响本轮研究。
初始分组：AI服务器PCB/高密度互联

核心问题：
> 胜宏科技是否正在从传统 PCB 制造商，转向 AI 服务器高密度 PCB 的核心供给方？

必须验证：
- AI服务器PCB收入占比、订单增速、客户结构和扩产兑现。
- 高多层板、HDI、GPU/服务器相关产品是否带来毛利率抬升。
- 与沪电股份、深南电路、广合科技、台系 PCB 厂的竞争位置。
- 估值是否已经透支 AI PCB 预期。

执行规则：
- 先读取 `../../0_总览/MINDSPACE_SOURCE_MCP_SOP.md`。
- 必须先调用 Mindspace Source MCP `health_check`。
- MCP 覆盖不足时必须加载 `agent-reach` skill，优先查巨潮资讯、深交所、公司公告、年报、季报、投资者关系记录和行业数据。
- 禁止内置 `web_search`。
- 不要因为创业板权限问题跳过研究，只在输出中标注交易权限。

输出文件：
- `company_research.md`
- `scorecard.md`
- `evidence_log.md`
- `next_questions.md`
- 同步更新 `../../0_总览/new_company_intake_queue.md`、`../../0_总览/company_score_table.md`、`../../0_总览/run_log.md`
