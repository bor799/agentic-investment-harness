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
legacy_path: "AI周期探索/02_公司研究/Tempus AI/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Tempus AI Evidence Log (PRO Updated 2026-05-16)

## MCP搜索记录

### PRO修复搜索（2026-05-16）
1. health_check → 通过
2. search_channels("Tempus AI TEM genomic data precision medicine") → 10 channels, high candidate scores (2910)
3. search_articles(channel=b0e8adcc) → 0 Tempus AI直接相关，全部为通用AI/healthcare内容

## Agent-Reach Fallback 证据

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| StockAnalysis.com | 市值$7.91B(-11.7%), 价格~$44 | 估值基准 | 高 | |
| StockAnalysis.com | TTM营收$1.36B(+69.8%) | 核心财务验证 | 高 | 极强增速 |
| StockAnalysis.com | 净亏损$302.91M, EPS -$1.72 | 盈利状态 | 高 | |
| StockAnalysis.com | P/S ~5.8x | 估值水平 | 高 | 高增长医疗科技合理 |
| StockAnalysis.com | 分析师Buy, 目标$69.31(+57.27%) | 市场预期 | 高 | |
| StockAnalysis.com | 行业Health Information Services | 公司信息 | 高 | |

## PRO source coverage

- Mindspace status: ✅ 通过（零TEM覆盖）
- Mindspace gap: 完全无Tempus AI相关文章
- agent-reach triggered: yes
- fallback reason: MCP完全零覆盖
- fallback queries: Tempus AI TEM stock analysis
- fallback links: stockanalysis.com/stocks/tem/
- final evidence status: evidence_complete
- remaining gaps: 收入构成（检测vs数据vs软件）、竞争格局细节、AI诊断监管
