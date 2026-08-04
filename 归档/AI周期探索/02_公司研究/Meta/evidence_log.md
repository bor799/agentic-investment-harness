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
legacy_path: "AI周期探索/02_公司研究/Meta/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Meta Evidence Log (PRO Updated 2026-05-17)

## MCP Sources

| source_name | source_tab | source_id | item_id | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|---|---|
| All Articles - SA | review | 5304b53c | c5b6de43 | seekingalpha.com/article/4872832 | 2026-02-20 | FoA营收+25% YoY，AI广告优化+WhatsApp变现，CapEx $115-135B | 中高 | review级别 |
| Long Ideas - SA | official_press | 21dc2b4b | 5c40bd71 | seekingalpha.com/article/4886569 | 2026-03-27 | 16x forward P/E，30%回调，FY2028 EPS>$40 | 中高 | official_press级别 |

## Agent-Reach Sources (PRO Fallback)

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| **StockAnalysis (SEC filings)** | TTM: Revenue $214.96B(+26.18%), GM 81.94%, NI $70.59B(PM 32.84%), FCF $48.25B(22.45%) | 财务核心 | 极高 | Period ending Mar 31, 2026 |
| **StockAnalysis (SEC filings)** | FY2025: Revenue $200.97B(+22.17%), GM 82.00%, NI $60.46B(PM 30.08%), FCF $46.11B(22.94%) | 年度趋势 | 极高 | |
| **StockAnalysis (SEC filings)** | FY2024: Revenue $164.50B(+21.94%), NI $62.36B(PM 37.91%), FCF $54.07B(32.87%) | 历史对比 | 极高 | |
| **StockAnalysis** | Market Cap $1.56T(+8.4%), Forward P/E 18.50, 52-Week $520-$796 | 估值 | 极高 | |
| **StockAnalysis** | Strong Buy共识, PT $836.39(+36.17%) | 分析师估值 | 极高 | |

## PRO source coverage

- Mindspace status: 2条SA文章(review+official_press)，产品/战略覆盖好
- Mindspace gap: 无财报数据、无FCF/OM具体数字、无Reality Labs拆分
- agent-reach triggered: yes
- fallback reason: MCP无Meta财报覆盖，补充估值和财务数据
- fallback queries: StockAnalysis financials, StockAnalysis overview
- fallback links:
  - stockanalysis.com/stocks/meta/financials/ (TTM+FY2021-2025)
  - stockanalysis.com/stocks/meta/ (概览/估值)
- final evidence status: evidence_complete
- remaining gaps: Reality Labs收入/亏损拆分、Llama商业收入路径、CapEx具体数字($115-135B)验证

## Evidence Assessment: PRO evidence_complete

覆盖4/4证据桶：
1. **财报/经营**: TTM+FY2024-2025完整数据（收入/利润率/FCF/趋势）
2. **估值/市场预期**: Market Cap $1.56T/Forward P/E 18.50/Strong Buy/36%上行
3. **结构性变化**: AI广告+Llama开源+CapEx $115-135B
4. **失败条件**: FCF margin从33%降至22%+CapEx压力+反垄断

**评分影响**: 46/70不变。新数据确认原评估。Forward P/E 18.50（非16x）略微调低3年翻倍信心，但收入+26%加速和Strong Buy共识抵消。
