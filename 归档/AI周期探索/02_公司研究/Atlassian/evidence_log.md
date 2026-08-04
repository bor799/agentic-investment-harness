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
legacy_path: "AI周期探索/02_公司研究/Atlassian/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Atlassian Evidence Log (PRO Updated 2026-05-17)

## MCP Sources

| source_name | source_tab | source_id | item_id | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|---|---|
| The Guardian (Technology) | media | 738f8624 | 0300e070 | theguardian.com/technology/2026/mar/12/atlassian-layoffs-software-technology-ai-push | 2026-03-12 | 裁员~1,600人(~10%)，CTO更换，AI转型+企业销售战略，$174M重组费用 | 中 | get_article_detail已回源 |
| The Guardian (Technology) | media | 1b5510f5 | b6e95e0b | theguardian.com/technology/2026/mar/21/atlassian-cuts-layoffs-staff-now-looking-for-work-ai | 2026-03-20 | ~500澳大利亚员工受影响，员工批评过程缺乏人性 | 中 | 员工视角 |
| Slashdot | review | 89d697fb | 7b9030d8 | slashdot.org/story/26/03/12/0722207/atlassian-ceo-cites-ai-shift | 2026-03-12 | 社区质疑"AI洗地"，Jira/Confluence定价和UX批评 | 低 | 情绪信号 |

## Agent-Reach Sources (PRO Fallback)

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| **StockAnalysis (SEC filings)** | TTM: Revenue $6,190M(+24.02%), GM 83.96%, NI -$216.81M, FCF $1,205M(19.46%), R&D $3,210M | 财务核心 | 极高 | Fiscal year Jul-Jun, TTM ending Mar 31, 2026 |
| **StockAnalysis (SEC filings)** | FY2025: Revenue $5,215M(+19.66%), GM 82.84%, NI -$256.69M, FCF $1,416M(27.14%) | 年度趋势 | 极高 | |
| **StockAnalysis (SEC filings)** | FY2024: Revenue $4,359M(+23.31%), GM 81.57%, FCF $1,415M(32.47%) | 历史对比 | 极高 | |
| **StockAnalysis** | Market Cap $22.19B(-63%), Forward P/E 14.42, P/S ~3.6x, 52-Week $56-$223 | 估值 | 极高 | May 15, 2026 |
| **StockAnalysis (35 analysts)** | FY2026E: Revenue $6.57B(+25.96%), EPS $5.36(首次盈利); FY2027E: $7.64B(+16.35%), EPS $6.17 | 分析师预测 | 高 | 非GAAP EPS |
| **StockAnalysis (analysts)** | Consensus Buy, PT $152.05(+73.85%); Oppenheimer $110, Barclays $112, BTIG $130, UBS $95 Hold | 分析师估值 | 高 | |
| **BusinessWire (官方PR)** | Team'26: Rovo 75%F500+90%企业云客户, 14M月度AI行动, 7x自动化增长, Teamwork Graph 150B连接开放MCP | AI产品验证 | 极高 | 2026-05-06官方发布 |
| **BusinessWire (官方PR)** | Rovo MCP Server(open beta)+CLI(open beta), Agents in Jira GA, Rovo Studio GA, DX AI GA | 产品发布 | 极高 | Team'26大会 |
| **BusinessWire** | 350K+客户, 85%F500, NASA/Rivian/Deutsche Bank/United Airlines/Bosch | 客户基础 | 极高 | |

## PRO source coverage

- Mindspace status: 3条media/review级别，零filing/report级别
- Mindspace gap: 无财报数据、无估值、无AI产品采用数据、无客户指标
- agent-reach triggered: yes
- fallback reason: MCP对Atlassian零财报覆盖，search_articles返回0结果
- fallback queries: StockAnalysis financials, StockAnalysis quarterly, StockAnalysis forecast, BusinessWire Team'26 PR
- fallback links:
  - stockanalysis.com/stocks/team/financials/ (年报+TTM)
  - stockanalysis.com/stocks/team/forecast/ (分析师预测)
  - stockanalysis.com/stocks/team/ (概览/估值)
  - businesswire.com/news/home/20260506556902/ (Team'26官方PR)
- final evidence status: evidence_complete
- remaining gaps: 季度具体数据(Q3 FY2026)、Cloud vs Data Center收入拆分、Rovo独立收入贡献

## Evidence Assessment: PRO evidence_complete

覆盖4/4证据桶：
1. **财报/经营**: TTM+FY2025+FY2024完整数据（收入/利润率/FCF/R&D趋势）
2. **估值/市场预期**: Market Cap/P/E/Forward P/E/52周/35位分析师预测
3. **结构性变化**: Teamwork Graph MCP开放+Rovo产品矩阵+AI转型
4. **失败条件**: FCF margin下滑+GAAP亏损+竞争+裁员信任赤字
