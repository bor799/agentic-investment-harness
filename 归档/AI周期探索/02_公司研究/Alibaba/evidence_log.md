---
title: "evidence_log"
date: 2026-07-24
updated: 2026-07-24
layer: EVIDENCE
primary_role: legacy_company_evidence
status: archived
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
legacy_metadata_added: true
legacy_path: "AI周期探索/02_公司研究/Alibaba/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Alibaba Evidence Log (PRO Updated 2026-05-16)

## MCP搜索记录

### PRO修复搜索（2026-05-16）
1. health_check → 通过
2. search_articles(NVDA频道 5931c9a3, "Alibaba BABA revenue profit earnings cloud AI 2025 2026") → ✅ CNBC财报详细报道 + Yahoo Finance完整财报电话记录
3. search_articles(X信源 b0e8adcc, "Alibaba 阿里巴巴 云计算 电商 AI revenue earnings profit 马云") → Qwen/阿里云间接提及
4. search_articles(ai market trends f6760f0f, "Alibaba Cloud AI Qwen model e-commerce Taobao Tmall") → 云计算行业背景

## MCP Direct Evidence

| source_name | source_tab | evidence_use | confidence |
|---|---|---|---|
| CNBC (2026-05-13) | media | Q4 FY2026: 调整后EBITA ¥5.1B(-84%), 云¥41.6B(+38%), AI收入¥9B, AI ARR目标¥10B→¥30B, 自研芯片, Qwen模型, 快消+57%, CMR+1% | 极高 |
| Yahoo Finance (2026-05-13) | review | 完整财报电话记录: 营收+11%, 云外部收入+40%, AI 11季三位数增长, AI占云30%→目标50%, T-head芯片, GAAP净利+96% | 极高 |

## Agent-Reach Fallback 证据

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| Google Finance | 分析师JP Morgan/Barclays: 目标$195-205, Overweight/Strong Buy | 分析师预期 | 高 | 30-45%上行 |
| Google Finance | 电商面临PDD/JD激烈竞争，commerce division earnings -47% | 竞争风险 | 高 | |

## PRO source coverage

- Mindspace status: ✅ 极丰富（CNBC详细财报+Yahoo Finance完整电话记录）
- Mindspace gap: 无 — MCP已覆盖财报、AI产品、芯片、竞争、分析师观点、战略指引
- agent-reach triggered: yes（补充分析师评级和竞争背景）
- fallback queries: google.com/finance/quote/BABA:NYSE
- fallback links: google.com/finance/quote/BABA:NYSE
- final evidence status: evidence_complete（4/4类别覆盖，证据极丰富）
- remaining gaps: 精确当前股价/市值（Google Finance Beta未渲染具体数字）
