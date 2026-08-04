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
legacy_path: "AI周期探索/02_公司研究/天华新能/PROMPT.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 天华新能 调研执行 Prompt

你现在只研究这一家公司，不要顺手研究其他公司。

公司：天华新能
代码：300390.SZ
市场/板块：A股 / 深交所创业板
交易权限：requires_chinext_permission; h_share_watch
是否可直接买：需确认创业板权限；H股已递表但尚未正式上市，后续需补 H 股代码和交易状态。
初始分组：锂电材料/氢氧化锂

核心问题：
> 天华新能是否能从锂价周期压力中走出来，凭借氢氧化锂产能、客户绑定和海外融资形成新的利润弹性？

必须验证：
- 电池级氢氧化锂供需、价格、产能利用率和库存周期。
- CATL/SK等客户绑定的稳定性和议价影响。
- H股上市进度、融资用途和 A/H 估值差。
- 2026 年 6-12 个月最关键的验证信号。

执行规则：
- 先读取 `../../0_总览/MINDSPACE_SOURCE_MCP_SOP.md`。
- 必须先调用 Mindspace Source MCP `health_check`。
- MCP 覆盖不足时必须加载 `agent-reach` skill，优先查巨潮资讯、深交所、港交所递表资料、公司公告、年报、季报和行业数据。
- 禁止内置 `web_search`。
- 不要因为创业板权限或 H 股尚未上市跳过研究，只在输出中标注交易权限。

输出文件：
- `company_research.md`
- `scorecard.md`
- `evidence_log.md`
- `next_questions.md`
- 同步更新 `../../0_总览/new_company_intake_queue.md`、`../../0_总览/company_score_table.md`、`../../0_总览/run_log.md`
