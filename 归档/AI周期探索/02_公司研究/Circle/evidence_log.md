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
legacy_path: "AI周期探索/02_公司研究/Circle/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Circle Evidence Log (PRO Updated 2026-05-16)

## MCP citation 规则

每条关键证据必须来自 Mindspace Source MCP，除非明确标注 fallback。

| source_name | source_tab | source_id | item_id | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|---|---|
| Long Investing Ideas from SA | official_press | 21dc2b4b-cd73-49d3-a828-ee40e43a45e6 | 3ce641c01fbe13c1652b19cf945585cd | seekingalpha.com | 2026-03-27 | 核心分析：$139目标价, ~50% EBITDA, OCC牌照, EURC, Arc主网 | 高 | SA专文，数据详实 |
| All Articles on SA / ARK | review | 5304b53c-632d-4b08-ac38-2f3721a3b5ad | 68c5b4d2ac87cd64bc5880261222234e | seekingalpha.com | 2026-03-22 | 行业数据：法币抵押稳定币85%+供给(~$313B)，GENIUS Act | 中高 | ARK研究报告 |
| 吴说区块链 | official_press | ce68e1d6-2ec8-49c8-98c1-d4570ea41131 | 2041688127925055909 | twitter.com | 2026-04-08 | 产品动态：Circle新加坡稳定币支付服务上线 | 中 | X/Twitter |
| 吴说区块链 | official_press | ce68e1d6-2ec8-49c8-98c1-d4570ea41131 | 2045289577385255134 | twitter.com | 2026-04-17 | 产品动态：USDC Bridge上线，原生跨链转移 | 中 | X/Twitter |
| 吴说区块链 | official_press | ce68e1d6-2ec8-49c8-98c1-d4570ea41131 | 2047103018492219727 | twitter.com | 2026-04-22 | 采用信号：Pornhub从USDT转USDC | 中 | 实际采用验证 |
| 吴说区块链 | official_press | ce68e1d6-2ec8-49c8-98c1-d4570ea41131 | 2047069240700887043 | twitter.com | 2026-04-22 | DeFi生态：Aave v3 USDC池接近100%利用率 | 中 | 需求验证 |
| PANews | official_press | e8a8eaf1-7a7c-42cd-935e-c26c99bb97bf | 2039536902890799489 | twitter.com | 2026-04-02 | 风险信号：Drift攻击Circle冻结能力受质疑 | 中 | 负面证据 |
| CryptoSlate | review | f7ab30e1-7ecc-4844-8e95-69f4e2cd8b49 | 949d4790206f04966d0b5a325f3122ef | cryptoslate.com | 2026-05-14 | 行业背景：CLARITY Act参议院银行委员会通过 | 中 | 上一轮证据 |
| CryptoSlate | review | f7ab30e1-7ecc-4844-8e95-69f4e2cd8b49 | a30e24b879148282d622ad6e45b96994 | cryptoslate.com | 2026-05-14 | 行业背景：市场低估CLARITY Act通过概率 | 中 | 上一轮证据 |

## Agent-Reach Fallback 证据

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| StockAnalysis.com | 营收TTM $2.86B (+51.5%) | 核心财务验证 | 高 | Jina Reader获取 |
| StockAnalysis.com | 市值$28.64B, 净亏损$14.26M | 估值基准 | 高 | |
| StockAnalysis.com | 前瞻PE 93.62, 20分析师买入 | 市场预期 | 高 | |
| StockAnalysis.com | 52周$49.90-$298.99 | 波动性和估值区间 | 高 | |
| StockAnalysis.com | IPO 2025-06-05, 员工1,100 | 公司基本信息 | 高 | |
| StockAnalysis.com | Clarity Act cleared Senate banking committee | 监管催化剂 | 高 | 与MCP证据交叉验证 |

## 搜索记录

### PRO修复搜索（2026-05-16 迭代）

#### MCP搜索
1. health_check → 通过
2. search_channels("Circle USDC stablecoin CRCL IPO cryptocurrency payment") → 20 channels
3. search_articles(channel=720f6626 "追踪MDLN/UNH/VST/CRCL") → 找到SA Circle专文 + ARK稳定币指南
4. search_articles(channel=037b5b7d "X信源") → 找到吴说区块链/PANews Circle相关动态
5. inspect_source_coverage(channel=720f6626) → 10 sources, 76 identifiers, 1,386 articles
6. get_article_detail(SA Circle专文) → 完整分析摘要+AI解读

#### Agent-Reach Fallback
- **原因**: MCP无精确财务数据（营收、利润、市值、PE）
- **Exa MCP**: 失败（DNS ENOTFOUND mcp.exa.ai）
- **Web-reader MCP**: 失败（配额耗尽，2026-05-26重置）
- **Jina Reader**: 成功 → StockAnalysis.com获取完整财务数据
- **搜索链接**: stockanalysis.com/stocks/crcl/
- **SA文章**: 403 Forbidden（paywall）

## PRO source coverage

- Mindspace status: ✅ 通过（有Circle相关SA专文+X信源动态）
- Mindspace gap: 精确财务数据（营收/利润/PE）和USDC市值份额数据
- agent-reach triggered: yes
- fallback reason: MCP无精确财务和估值数据
- fallback queries: Circle CRCL stock price earnings valuation; USDC market cap supply
- fallback links: stockanalysis.com/stocks/crcl/, coingecko.com/en/coins/usdc (部分), circle.com/en/transparency (产品结构)
- final evidence status: evidence_complete
- remaining gaps: USDC vs USDT精确市场份额趋势、分季度营收EBITDA明细
