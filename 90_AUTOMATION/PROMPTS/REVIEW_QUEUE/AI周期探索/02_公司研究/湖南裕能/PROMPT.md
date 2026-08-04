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
legacy_path: "AI周期探索/02_公司研究/湖南裕能/PROMPT.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 湖南裕能 调研执行 Prompt

你现在只研究这一家公司，不要顺手研究其他公司。

公司：湖南裕能
代码：301358.SZ
市场/板块：A股 / 深交所创业板
交易权限：requires_chinext_permission
是否可直接买：需确认创业板权限；权限问题不影响本轮研究。
初始分组：锂电材料/磷酸铁锂

核心问题：
> 湖南裕能是否从周期性磷酸铁锂材料供应商，转向能在新能源供需修复中重新获得利润弹性的龙头？

必须验证：
- 磷酸铁锂供需是否反转，行业价格/产能利用率是否改善。
- 宁德时代、比亚迪等核心客户集中度是护城河还是风险。
- 原材料价格、加工费、库存减值对利润率的影响。
- 2026 年 6-12 个月最关键的验证信号。

执行规则：
- 先读取 `../../0_总览/MINDSPACE_SOURCE_MCP_SOP.md`。
- 必须先调用 Mindspace Source MCP `health_check`。
- MCP 覆盖不足时必须加载 `agent-reach` skill，优先查巨潮资讯、深交所、公司公告、年报、季报和行业数据。
- 禁止内置 `web_search`。
- 不要因为创业板权限问题跳过研究，只在输出中标注交易权限。

输出文件：
- `company_research.md`
- `scorecard.md`
- `evidence_log.md`
- `next_questions.md`
- 同步更新 `../../0_总览/new_company_intake_queue.md`、`../../0_总览/company_score_table.md`、`../../0_总览/run_log.md`
