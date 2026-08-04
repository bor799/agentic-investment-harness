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
legacy_path: "AI周期探索/02_公司研究/Coinbase/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Coinbase Evidence Log (PRO Updated 2026-05-16)

## MCP citation 规则

每条关键证据必须来自 Mindspace Source MCP，除非明确标注 fallback。

| source_name | source_tab | source_id | item_id | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|---|---|
| All Articles on SA | review | 5304b53c-632d-4b08-ac38-2f3721a3b5ad | 4511c741677de39b7e22571eb9eb6cbd | seekingalpha.com | 2026-02-13 | Q4 2025财报: EPS -$2.49, 营收$1.78B(-21.59%), Everything Exchange | 高 | 财报电话记录 |
| All Articles on SA | review | 5304b53c-632d-4b08-ac38-2f3721a3b5ad | 6c397029546a83a58f473ffe7a6d97c0 | seekingalpha.com | 2026-05-08 | Q1 2026财报: 新CBO/IR Shan Aggarwal, 管理层强化 | 高 | 最新财报电话 |
| CryptoSlate | review | f7ab30e1-7ecc-4844-8e95-69f4e2cd8b49 | 949d4790206f04966d0b5a325f3122ef | cryptoslate.com | 2026-05-14 | 行业背景: Clarity Act参议院银行委员会通过 | 中 | 上一轮证据 |

## Agent-Reach Fallback 证据

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| StockAnalysis.com | TTM营收$6.29B(-5.4%), 净利$800.60M(-45.5%) | 核心财务验证 | 高 | Jina Reader获取 |
| StockAnalysis.com | FY2025营收$6.88B(+9.38%), 盈利$1.26B(-51.11%) | 年度趋势 | 高 | |
| StockAnalysis.com | 市值$52.61B, P/E 69.71, Forward PE 85.61 | 估值基准 | 高 | |
| StockAnalysis.com | 30位分析师买入, 目标价$299.40(+49.94%) | 市场预期 | 高 | |
| StockAnalysis.com | Benchmark上调目标价至$270, Buy | 分析师动态 | 中 | |

## 搜索记录

### PRO修复搜索（2026-05-16 迭代）

#### MCP搜索
1. health_check → 通过
2. search_channels("Coinbase COIN crypto exchange Base layer2 institutional") → 15 channels, X信源(candidate_score 510, 102 matched)高度匹配
3. search_articles(channel=720f6626) → 找到Q4 2025和Q1 2026财报电话记录
4. get_article_detail(Q4 2025) → EPS -$2.49, $1.78B营收, Everything Exchange详情
5. get_article_detail(Q1 2026) → 新CBO/IR, 管理层变动

#### Agent-Reach Fallback
- **原因**: MCP无精确财务数据（TTM/年度营收、PE、市值）
- **Exa MCP**: 失败（DNS不可达）
- **Jina Reader**: 成功 → StockAnalysis获取完整财务
- **搜索链接**: stockanalysis.com/stocks/coin/

## PRO source coverage

- Mindspace status: ✅ 通过（找到2份财报电话记录+行业背景）
- Mindspace gap: Base L2 TVL/交易量、Q1 2026具体营收数字、机构客户数据
- agent-reach triggered: yes
- fallback reason: MCP有财报电话记录但缺精确TTM/年度财务和估值数据
- fallback queries: Coinbase COIN stock price earnings valuation revenue
- fallback links: stockanalysis.com/stocks/coin/
- final evidence status: evidence_complete
- remaining gaps: Base L2精确数据、Q1 2026具体EPS/营收数字、机构AUM
