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
legacy_path: "AI周期探索/02_公司研究/Palantir/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Palantir Evidence Log (PRO Updated 2026-05-17)

## MCP Sources

| source_name | source_tab | source_id | item_id | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|---|---|
| WIRED en Español | media | aaf70bd6 | a5f30323 | es.wired.com/palantir-devcon | 2026-03-23 | DevCon: 商业120%/公共60%，AIP/Foundry平台化，Mixology案例 | 高 | |
| WIRED | media | 63994be7 | b2172e3c | wired.com/palantir-employees-bad-guys | 2026-04-23 | 员工道德危机，ICE/伊朗打击争议，Slack删帖 | 高 | 风险证据 |
| WIRED en Español | media | 3cea7812 | 0ed025f1 | es.wired.com/palantir-irs-contract | 2026-03-30 | IRS $1.8M SNAP合同，累计>$200M | 中高 | |
| The Guardian | media | 49c2dc44 | 1cf5bd47 | theguardian.com/nhs-palantir | 2026-02-12 | NHS £330M FDP合同争议，使用率151/240低于目标 | 中高 | 客户风险 |
| The Guardian | media | 49c2dc44 | 9136181e | theguardian.com/met-police-palantir | 2026-02-22 | Met Police使用Palantir AI监控 | 中 | |
| The Guardian | media | 1b5510f5 | 938a7ebd | theguardian.com/met-police-hundreds | 2026-04-25 | Met Police一周内部署发现数百问题 | 中 | |
| The Guardian | media | a0e0d340 | a3a30453 | theguardian.com/nyc-hospitals-palantir | 2026-03-26 | NYC公立医院不续签(~$4M) | 中高 | 客户流失 |
| The Guardian | media | 1b5510f5 | c3c1c623 | theguardian.com/met-police-criminal | 2026-04-22 | Met Police刑事调查AI系统谈判，UK累计>£500M | 中 | |
| ZDNet | review | 806ed29f | 71b5c2ad | zdnet.com/government-ai-agents | 2026-04-24 | 82%政府机构已采用AI代理 | 中 | 行业背景 |
| WIRED en Español | media | 2b33d741 | d9bd5531 | es.wired.com/palantir-pentagon | 2026-03-13 | AIP嵌入LLM生成战场方案 | 中 | |

## Agent-Reach Sources (PRO Fallback)

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| **StockAnalysis (SEC filings)** | TTM: Revenue $5,224M(+67.71%), GM 84.07%, OM 38.13%, NI $2,282M(+299.78%), FCF $2,688M(51.46%) | 财务核心 | 极高 | Period ending Mar 31, 2026 |
| **StockAnalysis (SEC filings)** | FY2025: Revenue $4,475M(+56.18%), GM 82.37%, OM 31.60%, NI $1,625M, FCF $2,101M(46.94%) | 年度趋势 | 极高 | |
| **StockAnalysis (SEC filings)** | FY2024: Revenue $2,866M(+28.79%), GM 80.25%, OM 10.83%, NI $462M, FCF $1,141M(39.83%) | 历史对比 | 极高 | |
| **StockAnalysis (SEC filings)** | FY2021-FY2023: Revenue $1,542M→$1,906M→$2,225M, OM从-27%→5%→-8%→11%→32%→38% | 5年趋势 | 极高 | OM历史性转变 |
| **StockAnalysis** | Analyst Buy, PT $194.17(+44.91%), Citi PT $225(Buy) | 分析师估值 | 高 | |
| **StockAnalysis (forecast)** | FY2026E: Revenue $7.41B(+65.61%), EPS $1.34, Forward P/E 99.89; FY2027E: $10.57B(+42.54%), EPS $1.90, Forward P/E 70.70 | 预测 | 高 | |

## PRO source coverage

- Mindspace status: 10条media级别(DevCon+WIRED+Guardian+ZDNet)，产品/风险覆盖极好
- Mindspace gap: 零财报/估值数据（全media级别，无filing/report）
- agent-reach triggered: yes
- fallback reason: MCP有10条产品/风险证据但零财务/估值数据，证据_log承认"财务数据严重缺失"
- fallback queries: StockAnalysis financials, StockAnalysis forecast, StockAnalysis overview
- fallback links:
  - stockanalysis.com/stocks/pltr/financials/ (TTM+FY2021-2025)
  - stockanalysis.com/stocks/pltr/forecast/ (FY2026-2027预测)
- final evidence status: evidence_complete
- remaining gaps: 商业vs政府收入绝对拆分、SBC具体金额占收入比、季度趋势细节

## Evidence Assessment: PRO evidence_complete

覆盖4/4证据桶：
1. **财报/经营**: TTM+FY2021-2025完整数据（收入/利润率/FCF/5年趋势）
2. **估值/市场预期**: Forward P/E 99.89/70.70/Buy PT +44.91%/Citi $225
3. **结构性变化**: AIP/Foundry+Ontology+SAP合作+DevCon商业120%
4. **失败条件**: ICE伦理争议+NHS低使用率+NYC流失+员工道德危机+Forward P/E 100x
