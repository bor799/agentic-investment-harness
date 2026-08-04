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
legacy_path: "AI周期探索/02_公司研究/MongoDB/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# MongoDB Evidence Log (PRO Updated 2026-05-17)

## MCP Sources

| source_name | source_tab | source_id | item_id | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|---|---|
| All Articles - SA | review | 5304b53c | 7fd7fe62 | seekingalpha.com/article/4902172 | 2026-05-10 | Atlas驱动72%营收，AI+向量搜索差异化，公允价值$440 | 中 | review级别 |
| All Articles - SA | review | 5304b53c | cc2432ed | seekingalpha.com/article/4904333 | 2026-05-14 | Q1 2026全年营收指引低于共识，拖累Alger基金 | 中 | review级别 |
| MongoDB Blog | blog | — | — | mongodb.com/blog | 2026-03-31 | Agent Skills/MCP Server支持AI编码代理 | 中 | 前轮MCP证据 |
| MongoDB Blog | blog | — | — | mongodb.com/blog | 2026-04-07 | Atlas预测式自动扩缩容 | 中 | 前轮MCP证据 |
| InfoQ | review | — | — | infoq.com | 2026-04 | "便利变现而非锁定"策略 | 中 | 前轮MCP证据 |
| VentureBeat | review | — | — | venturebeat.com | 2026-04 | Qdrant $50M B轮竞争参考 | 中 | 前轮MCP证据 |

## Agent-Reach Sources (PRO Fallback)

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| **StockAnalysis (SEC filings)** | FY2026: Revenue $2,464M(+22.80%), GM 71.75%, NI -$71.15M, FCF $500.19M(20.30%) | 财务核心 | 极高 | Fiscal year ending Jan 31 |
| **StockAnalysis (SEC filings)** | FY2025: Revenue $2,006M(+19.22%), GM 73.32%, NI -$129.07M, FCF $120.64M(6.01%) | 年度趋势 | 极高 | |
| **StockAnalysis (SEC filings)** | FY2024: Revenue $1,683M(+31.07%), GM 74.78%, FCF $115.4M(6.86%) | 历史对比 | 极高 | |
| **StockAnalysis** | Market Cap $25.09B(+79.5%), Forward P/E 53.44, 52-Week $182-$445 | 估值 | 极高 | |
| **StockAnalysis (42 analysts)** | FY2027E: Revenue $2.92B(+18.68%), EPS $5.89(首次盈利); FY2028E: $3.42B(+17.10%), EPS $7.05 | 分析师预测 | 高 | 非GAAP EPS |
| **StockAnalysis** | Consensus Buy, PT $370.79(+18.78%) | 分析师估值 | 高 | |
| **PRNewswire** | MongoDB任命Ryan Mac Ban为新CRO(2026年4月27日生效) | 管理层变化 | 高 | |

## PRO source coverage

- Mindspace status: 6条(review+blog级别为主)，零filing/report级别
- Mindspace gap: 无财报数据、无估值、无客户指标、无毛利率/利润率数据
- agent-reach triggered: yes
- fallback reason: MCP无SEC财报覆盖，search_articles返回0条财务数据
- fallback queries: StockAnalysis financials, StockAnalysis forecast, StockAnalysis overview
- fallback links:
  - stockanalysis.com/stocks/mdb/financials/ (年报FY2022-2026)
  - stockanalysis.com/stocks/mdb/forecast/ (分析师预测FY2027-2028)
  - stockanalysis.com/stocks/mdb/ (概览/估值)
- final evidence status: evidence_complete
- remaining gaps: Atlas vs Non-Atlas收入拆分、>$100K ARR客户数、NRR具体数值

## Evidence Assessment: PRO evidence_complete

覆盖4/4证据桶：
1. **财报/经营**: FY2024-2026完整数据（收入/利润率/FCF/趋势）
2. **估值/市场预期**: Market Cap/P/E/Forward P/E/52周/42位分析师预测
3. **结构性变化**: Atlas 72%+MCP Server+Agent Skills+向量搜索
4. **失败条件**: GM下滑+pgvector竞争+增速放缓+Forward P/E压缩
