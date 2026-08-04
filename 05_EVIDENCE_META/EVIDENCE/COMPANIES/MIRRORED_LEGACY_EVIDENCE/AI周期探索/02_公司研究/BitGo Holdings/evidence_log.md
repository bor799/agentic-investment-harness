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
legacy_path: "AI周期探索/02_公司研究/BitGo Holdings/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# BitGo Holdings Evidence Log (PRO Updated 2026-05-16)

## MCP搜索记录

### PRO修复搜索（2026-05-16）
1. health_check → 通过
2. search_channels("BitGo BTGO digital asset custody institutional") → 10 channels, X信源(candidate_score 400, 80 matched)
3. search_articles(channel=037b5b7d, X信源) → 0 BitGo直接相关，全部为其他公司custody内容

## Agent-Reach Fallback 证据

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| StockAnalysis.com | IPO 2026-01-22, NYSE:BTGO | 公司基本信息 | 高 | |
| StockAnalysis.com | 市值$1.02B, 价格$8.84 | 估值基准 | 高 | |
| StockAnalysis.com | TTM营收$18.15B(+293.6%) | ⚠️可疑数据 | 低 | 可能含交易总额而非净收入 |
| StockAnalysis.com | 净亏损$49.72M, EPS -$1.17 | 盈利状态 | 高 | |
| StockAnalysis.com | Forward PE 818.52 | 估值水平 | 高 | 极贵 |
| StockAnalysis.com | 9位分析师Strong Buy, 目标$14.61 | 市场预期 | 高 | +64.71%上行 |
| StockAnalysis.com | 员工603, 行业Capital Markets | 公司规模 | 高 | |

## PRO source coverage

- Mindspace status: ✅ 通过（但零BitGo直接覆盖）
- Mindspace gap: 完全无BitGo相关文章，仅行业背景
- agent-reach triggered: yes
- fallback reason: MCP完全零覆盖
- fallback queries: BitGo BTGO stock, BitGo IPO revenue valuation
- fallback links: stockanalysis.com/stocks/btgo/
- final evidence status: evidence_limited_after_fallback
- remaining gaps: 营收构成验证、AUC数据、竞争格局、季度财报趋势
