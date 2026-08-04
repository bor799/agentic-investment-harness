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
legacy_path: "AI周期探索/02_公司研究/Duolingo/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Duolingo Evidence Log (PRO Updated 2026-05-16)

## MCP搜索记录

### PRO修复搜索（2026-05-16）
1. health_check → 通过
2. search_articles(X信源 b0e8adcc, "Duolingo DUOL language learning AI education") → 0 DUOL 直接相关
3. search_articles(ai market trends f6760f0f, "Duolingo AI language learning subscription") → 1 条 TechCrunch 直接文章
4. get_article_detail(TechCrunch 7cea5b0a) → Duolingo 向免费用户开放 B2 (CEFR) 高级内容，DAU 5270 万，付费用户 1220 万

**结论**: MCP 有 1 条高质量直接文章（TechCrunch），补充了关键运营数据。

## MCP Direct Evidence

| source_name | source_tab | item_id | evidence_use | confidence |
|---|---|---|---|---|
| TechCrunch Apps | media | 7cea5b0a4463378166c45b0bc75e5423 | DAU 52.7M, 付费用户 12.2M, B2内容免费开放 | 高 |

## Agent-Reach Fallback 证据

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| StockAnalysis.com | 市值$5.22B(-70.6%), 价格$112.06 | 估值基准 | 高 | 从$541暴跌 |
| StockAnalysis.com | TTM营收$1,099M(+35.45%) | 核心财务验证 | 高 | |
| StockAnalysis.com | 5年营收$251M→$1,099M | 长期增长 | 高 | |
| StockAnalysis.com | TTM净利$422.39M | 盈利验证 | 中 | ⚠️ 受税收扭曲 |
| StockAnalysis.com | TTM税前利润$202.95M | 标准化盈利 | 高 | |
| StockAnalysis.com | TTM营业利润$156.5M(14.24%) | 运营效率 | 高 | |
| StockAnalysis.com | TTM FCF $416.04M(37.86%) | 现金流 | 高 | 极强 |
| StockAnalysis.com | 毛利率72.67% | 定价权 | 高 | 5年稳定 |
| StockAnalysis.com | 有效税率-108% | 税收扭曲 | 高 | P/E 12.84失真 |
| StockAnalysis.com | P/FCF ~12.5x | 估值 | 高 | 增长公司中罕见低 |
| StockAnalysis.com | 18位分析师Buy, 目标$175.75(+57%) | 市场预期 | 高 | |
| StockAnalysis.com | 52周$87.89-$541.46 | 价格波动 | 高 | 接近低点 |
| StockAnalysis.com | 员工900 | 公司规模 | 高 | |

## PRO source coverage

- Mindspace status: ✅ 通过（1条直接文章）
- Mindspace gap: 有 TechCrunch 运营数据，缺深度竞争分析和AI战略
- agent-reach triggered: yes
- fallback reason: MCP 仅1条文章，需补充完整财务
- fallback queries: stockanalysis.com/stocks/duol/ + financials
- fallback links: stockanalysis.com/stocks/duol/, stockanalysis.com/stocks/duol/financials/
- final evidence status: evidence_complete
- remaining gaps: Q1暴跌具体原因、AI辅导功能(Duolingo Max)收入贡献、标准化税率
