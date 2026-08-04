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
legacy_path: "AI周期探索/02_公司研究/GitLab/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# GitLab Evidence Log (PRO Updated 2026-05-17)

## MCP Sources

| source_name | source_tab | source_id | item_id | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|---|---|
| All Articles - SA | review | 5304b53c | 578459f4 | seekingalpha.com/article/4886796 | 2026-03-28 | FY27指引$1.10-1.12B(+15-17%)，EV/营收2.1x，净现金$1.26B | 中 | review级别 |
| Long Ideas - SA | official_press | 21dc2b4b | e12d7e6a | seekingalpha.com/article/4873164 | 2026-02-21 | DBNRR 119%，13%客户$100K+/年，FCF转正 | 中 | official_press级别 |

## Agent-Reach Sources (PRO Fallback)

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| **StockAnalysis (SEC filings)** | FY2026: Revenue $955.22M(+25.81%), GM 87.36%, NI -$55.96M, FCF $222.03M(23.24%) | 财务核心 | 极高 | Fiscal year ending Jan 31 |
| **StockAnalysis (SEC filings)** | FY2025: Revenue $759.25M(+30.93%), GM 88.79%, FCF -$67.74M(-8.92%) | 年度趋势 | 极高 | |
| **StockAnalysis (SEC filings)** | FY2024: Revenue $579.91M(+36.66%), GM 89.70%, FCF $33.44M(5.77%) | 历史对比 | 极高 | |
| **StockAnalysis** | Market Cap $4.00B(-48.5%), Forward P/E 29.93, 52-Week $18.73-$53.82 | 估值 | 极高 | |
| **StockAnalysis** | Consensus Buy, PT $36.09(+52.54%) | 分析师估值 | 高 | |
| **BusinessWire** | GitLab与AWS Bedrock合作，Agentic DevSecOps企业集成 | AI合作验证 | 极高 | 2026-04-21 |
| **BusinessWire** | GitLab与Google Cloud Vertex AI合作，Agentic DevSecOps | AI合作验证 | 极高 | 2026-04-14 |

## PRO source coverage

- Mindspace status: 2条SA文章(review+official_press)，零SEC财报覆盖
- Mindspace gap: 无财报数据、无估值、无季度趋势、无竞争分析
- agent-reach triggered: yes
- fallback reason: MCP无GitLab财报覆盖，仅2条SA文章
- fallback queries: StockAnalysis financials, StockAnalysis overview
- fallback links:
  - stockanalysis.com/stocks/gtlb/financials/ (年报FY2022-2026)
  - stockanalysis.com/stocks/gtlb/ (概览/估值)
  - businesswire.com AWS合作PR
  - businesswire.com Google Cloud合作PR
- final evidence status: evidence_complete
- remaining gaps: 消费计费转型进度具体数据、NRR最新数值、季度细分

## Evidence Assessment: PRO evidence_complete

覆盖4/4证据桶：
1. **财报/经营**: FY2024-2026完整数据（收入/利润率/FCF/趋势）
2. **估值/市场预期**: Market Cap/Forward P/E/52周/分析师预测
3. **结构性变化**: AWS/Google Cloud AI合作+Agentic DevSecOps定位
4. **失败条件**: GitHub竞争+AI替代DevSecOps+增速继续放缓+估值压缩
