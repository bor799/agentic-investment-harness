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
legacy_path: "AI周期探索/02_公司研究/Li Auto/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Li Auto Evidence Log (PRO Updated 2026-05-16)

## MCP搜索记录

### PRO修复搜索（2026-05-16）
1. health_check → 通过
2. search_articles(X信源 037b5b7d, "Li Auto LI 理想汽车 earnings revenue EV China") → 1条间接提及（Orange AI: CEO李想播客谈AI）
3. search_articles(ai market trends f6760f0f, "Li Auto 理想汽车 smart driving autonomous EV") → Wired提及北京车展drive-by-wire平台

**结论**: MCP对Li Auto覆盖极低，仅间接提及，无直接财报/产品/竞争分析文章。

## MCP Direct Evidence

| source_name | source_tab | evidence_use | confidence |
|---|---|---|---|
| Orange AI (X) | forum | CEO李想播客: "AI是生产力和劳动力的技术" — AI战略信号 | 低 |
| Wired | media | 北京车展展示drive-by-wire平台技术 | 低 |

## Agent-Reach Fallback 证据

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| StockAnalysis.com | 市值$18.93B(-22.7%), 价格$18.51 | 估值基准 | 高 | |
| StockAnalysis.com | TTM营收$16.06B(-22.3%) | 核心财务 | 高 | 营收持续下降 |
| StockAnalysis.com | FY2025营收¥112.31B(-22.25%) | 年度财务 | 高 | 人民币计同样下降 |
| StockAnalysis.com | TTM净利$160.76M(-86.0%) | 利润崩溃 | 高 | 近乎消失 |
| StockAnalysis.com | P/E 124.70, Forward P/E 88.61 | 极端估值 | 高 | |
| StockAnalysis.com | 10位分析师Hold, 目标$19.66(+6.21%) | 共识偏空 | 高 | 无强烈推荐 |
| StockAnalysis.com | 52周范围$15.71-$32.03, Beta 0.62 | 波动率低 | 高 | |
| StockAnalysis.com | 员工30,728 | 大型车企规模 | 高 | |

## PRO source coverage

- Mindspace status: ⚠️ 极低覆盖（2条间接提及，无直接分析）
- Mindspace gap: 无财报数据、无竞争分析、无产品评估
- agent-reach triggered: yes（补充完整财务数据）
- fallback queries: stockanalysis.com/stocks/li/
- fallback links: stockanalysis.com/stocks/li/
- final evidence status: evidence_complete（财务数据完整，MCP补充定性信号）
- remaining gaps: 智能驾驶ADAS能力详细对比、中国市场份额趋势
