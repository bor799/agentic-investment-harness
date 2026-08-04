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
legacy_path: "AI周期探索/02_公司研究/NuScale Power/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# NuScale Power Evidence Log (PRO Updated 2026-05-17)

## MCP Sources

| source_name | source_tab | source_id | item_id | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|---|---|
| Yahoo Finance | review | — | — | finance.yahoo.com (NuScale Oklo comparison) | 2026-04-04 | NuScale 市值~$3.7B，面临延期和不确定性；Oklo 更接近商业化(2027首堆)，BofA 买入 $127 目标价 | 中 | source_id/item_id 在上下文压缩中丢失 |
| CNBC | media | — | — | cnbc.com (X-energy IPO) | 2026-04-24 | X-energy IPO 募资$1B+，涨27%，80MW xe-100反应堆，11GW管道含Amazon/Dow/Centrica | 中 | 竞争对手证据 |
| Seeking Alpha | review | — | — | seekingalpha.com (Oklo Q1 inflection) | 2026-05-08 | Oklo Q1 是"SMR交易转折点"，$2.5B流动性，Meta预付款协议 | 中 | 竞争对手证据 |
| Seeking Alpha | review | — | — | seekingalpha.com (American Century NuScale) | 2026-03-06 | American Century 基金指出 NuScale "弱势" | 中 | 直接负面信号 |
| CNBC | media | — | — | cnbc.com (Maine data center ban) | 2026-04-09 | 缅因州成首个禁止数据中心建设的州，临时禁令至2027年11月 | 中 | 监管逆风 |

## Agent-Reach Sources (PRO Fallback)

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| **StockAnalysis (SEC filings)** | TTM: Revenue $18.67M(-61.93%), GM 23.84%, OM -3813%, NI -$385.80M, FCF -$753.39M | 财务核心 | 极高 | Period ending Mar 31, 2026 |
| **StockAnalysis (SEC filings)** | FY2025: Revenue $31.48M(-15.02%), GM 36.31%, OM -2191%, NI -$355.79M, FCF -$460.12M | 年度数据 | 极高 | |
| **StockAnalysis (SEC filings)** | FY2024: Revenue $37.05M(+62.41%), GM 86.67%, OM -374.5%, NI -$136.62M, FCF -$108.71M | 历史对比 | 极高 | |
| **StockAnalysis (SEC filings)** | FY2021-FY2023: Revenue $2.86M→$11.80M→$22.81M | 早期趋势 | 极高 | |
| **StockAnalysis (balance sheet)** | TTM: Cash+ST Inv $890M, Debt $0, Net Cash $890M, BVPS $7.03 | 资产负债 | 极高 | 14个月跑道 |
| **StockAnalysis (balance sheet)** | FY2025: Cash $1,254M(含股权融资$1.3B) → TTM $890M, 季度烧$364M | 资本轨迹 | 极高 | |
| **StockAnalysis (analysts)** | Hold consensus(11人): PT $18.10(+61%), Citi Strong Sell $7, B.Riley Buy $19 | 分析师估值 | 高 | |
| **StockAnalysis (forecast)** | FY2026E: Revenue $96.67M(+207%), EPS -$0.90; FY2027E: $269.22M(+179%), EPS -$0.53 | 预测 | 高 | 仍亏损 |

## PRO source coverage

- Mindspace status: 5条 review/media 级别，source_id 全部丢失（上下文压缩）
- Mindspace gap: 零财报/估值数据，搜索全部返回0（数据轮换）
- agent-reach triggered: yes
- fallback reason: MCP搜索0结果+source_id丢失+零财务数据
- fallback queries: StockAnalysis overview, financials, balance sheet, cash flow, forecast
- fallback links:
  - stockanalysis.com/stocks/smr/ (overview+market data)
  - stockanalysis.com/stocks/smr/financials/ (FY2021-TTM)
  - stockanalysis.com/stocks/smr/financials/balance-sheet/ (资产负债)
  - stockanalysis.com/stocks/smr/forecast/ (FY2026-2027预测)
- final evidence status: evidence_complete
- remaining gaps: CFPP/RoPower 项目具体进度、客户签约细节、季度收入趋势细节

## Evidence Assessment: PRO evidence_complete

覆盖4/4证据桶：
1. **财报/经营**: TTM+FY2021-2025完整数据（收入/利润率/FCF/资产负债/5年趋势）
2. **估值/市场预期**: Market Cap $4.10B/Hold consensus/PT $18.10(+61%)/Citi Strong Sell $7/FY2026-2027E预测
3. **结构性变化**: SMR+AI电力需求+NRC设计认证（但转变未验证）
4. **失败条件**: Oklo/X-energy领先+Citi Strong Sell+14个月跑道+收入下降+监管逆风
