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
legacy_path: "AI周期探索/02_公司研究/Vistra/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Vistra Evidence Log (PRO Updated 2026-05-17)

## MCP Sources

| source_name | source_tab | source_id | item_id | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|---|---|
| Yahoo Finance | review | 4986cd10 | 1413fba7 | finance.yahoo.com/vistra-vst-best-power-generation | 2026-05-09 | TD Cowen $230/RJ $208/MS $208均下调但维持正面，ERCOT逆风 | 中高 | |
| Yahoo Finance | review | c987783f | 06492b26 | finance.yahoo.com/vistra-corp-vst-bull-case | 2026-02-28 | Meta 20年2,609MW PPA+$15.8B债务/2.8x杠杆 | 中高 | |
| Yahoo Finance | review | c987783f | 5b3a8d37 | finance.yahoo.com/jim-cramer-vistra-vst | 2026-04-18 | Jim Cramer看好 | 低 | |
| CNBC | media | 2a2b77c4 | 1fb0b593 | cnbc.com/ai-data-centers-pennsylvania | 2026-04-24 | 宾州数据中心地方反对 | 中 | |
| CNBC | media | 04cf5234 | c98137bd | cnbc.com/maine-data-center-ban | 2026-04-09 | 缅因州禁止数据中心 | 中 | |
| Seeking Alpha | review | aef5cdc3 | 97b554d7 | seekingalpha.com/data-center-infrastructure-stock | 2026-03-28 | Vistra列为主要数据中心电力股 | 中 | |

## Agent-Reach Sources (PRO Fallback)

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| **StockAnalysis (SEC filings)** | TTM: Revenue $19.45B(+7.41%), GM 29.32%, NI $2.05B(PM 11.52%), FCF $1.80B(9.27%) | 财务核心 | 极高 | Period ending Mar 31, 2026 |
| **StockAnalysis (SEC filings)** | FY2025: Revenue $17.74B(+2.98%), GM 23.23%, NI $752M(PM 5.32%), FCF $1.32B(7.43%) | FY2025严重下滑 | 极高 | |
| **StockAnalysis (SEC filings)** | FY2024: Revenue $17.22B(+16.54%), GM 34.39%, NI $2.47B(16.33%), FCF $2.49B(14.43%) | 基准年 | 极高 | |
| **StockAnalysis** | Market Cap $47.10B, Forward P/E 14.75, 52-Week $138-$220, Dividend $0.91(0.65%) | 估值 | 极高 | |
| **StockAnalysis** | Strong Buy共识, PT $233.00(+66.81%) | 分析师估值 | 极高 | |

## PRO source coverage

- Mindspace status: 6条(review/media级别)，有PPA/债务/竞争数据
- Mindspace gap: 无财报数据(营收/利润率/FCF)、无估值
- agent-reach triggered: yes
- fallback reason: MCP无Vistra财报覆盖，补充完整财务和估值数据
- fallback queries: StockAnalysis financials, StockAnalysis overview
- fallback links:
  - stockanalysis.com/stocks/vst/financials/ (TTM+FY2021-2025)
  - stockanalysis.com/stocks/vst/ (概览/估值)
- final evidence status: evidence_complete
- remaining gaps: 核能业务细节(Comanche Peak运营/扩产)、零售电力业务拆分、季度趋势

## Evidence Assessment: PRO evidence_complete

覆盖4/4证据桶：
1. **财报/经营**: TTM+FY2024-2025完整数据（收入/利润率/FCF/趋势）
2. **估值/市场预期**: Market Cap $47.1B/Forward P/E 14.75/Strong Buy/67%上行
3. **结构性变化**: PPA锁定(Meta 2,609MW)+合同驱动型电力平台转型
4. **失败条件**: FY2025利润率暴跌(OM 24%→11%)+ERCOT电价波动+$15.8B债务

**评分影响**: 40/70不变。FY2025暴跌验证ERCOT逆风风险，但TTM恢复+Strong Buy+67%上行确认期权价值。
