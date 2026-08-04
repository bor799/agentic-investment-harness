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
legacy_path: "AI周期探索/02_公司研究/Figure Technology/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Figure Technology Evidence Log (PRO Updated 2026-05-16)

## MCP搜索记录

### PRO修复搜索（2026-05-16）
1. health_check → 通过
2. search_channels("Figure AI humanoid robot FIGR") → 10 channels, high candidate scores
3. search_articles(X信源 b0e8adcc, "Figure Technology FIGR fintech lending") → 2 条 Brett Adcock 推文（注：为 Figure AI 人形机器人公司，非 FIGR）
4. search_articles(ai market trends f6760f0f, "Figure AI humanoid robot") → 10 条行业文章，无 FIGR 直接相关
5. search_articles(ai ethics e23018dd, "Figure AI robot humanoid") → 10 条行业文章，无 FIGR 直接相关
6. get_article_detail(ae7495d8, 2053234021182898234) → Brett Adcock "Figure is giving AI a body" — 确认为 Figure AI（人形机器人），非 Figure Technology Solutions（区块链金融）
7. get_article_detail(ae7495d8, 2052770989944242335) → Brett Adcock "Figure taught two robots to make a bed" — 同上

**结论**: MCP 零 FIGR（Figure Technology Solutions 区块链金融公司）直接覆盖。Brett Adcock 推文属于同名不同公司（Figure AI 人形机器人）。

## Agent-Reach Fallback 证据

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| StockAnalysis.com | 市值$9.81B, 价格$44.42 | 估值基准 | 高 | |
| StockAnalysis.com | TTM营收$589.36M(+68.33%) | 核心财务验证 | 高 | 极强增速 |
| StockAnalysis.com | FY2025营收$506.87M(+48.69%) | 年度财务验证 | 高 | |
| StockAnalysis.com | FY2024营收$340.89M(+62.68%) | 增长趋势 | 高 | |
| StockAnalysis.com | FY2023营收$209.55M | 基准年 | 高 | |
| StockAnalysis.com | TTM净利$187.36M(31.86%) | 盈利验证 | 高 | 极强利润率 |
| StockAnalysis.com | FY2025净利$133.86M(26.49%) | 年度盈利验证 | 高 | |
| StockAnalysis.com | 毛利率100%（三年一贯） | 平台模型验证 | 高 | 无COGS |
| StockAnalysis.com | 营业利润率25.71%TTM | 运营效率 | 高 | 从-23.59%跃升 |
| StockAnalysis.com | P/E 77.02, Forward P/E 44.14 | 估值水平 | 高 | 高增长合理 |
| StockAnalysis.com | 9位分析师Buy, 目标$54.33(+22%) | 市场预期 | 高 | |
| StockAnalysis.com | Mizuho $55 Outperform, BofA $33 Underperform | 分歧信号 | 高 | |
| StockAnalysis.com | IPO 2025-09-11, $25.00 | 公司信息 | 高 | |
| StockAnalysis.com | CEO Tannenbaum, 创始人Cagney(SoFi创始人) | 治理信息 | 高 | |
| StockAnalysis.com | 员工602, 行业Capital Markets | 公司信息 | 高 | |
| StockAnalysis.com | ⚠️ TTM FCF -$1,907M | 现金流红旗 | 中 | 原因待查 |
| StockAnalysis.com | ⚠️ 股份稀释 51M→179M(3.5x) | 稀释风险 | 高 | |

## PRO source coverage

- Mindspace status: ✅ 通过（零 FIGR 覆盖）
- Mindspace gap: 完全无 Figure Technology Solutions 相关文章（搜索命中均为 Figure AI 人形机器人公司）
- agent-reach triggered: yes
- fallback reason: MCP 完全零覆盖
- fallback queries: stockanalysis.com/stocks/figr/ + financials + company
- fallback links: stockanalysis.com/stocks/figr/, stockanalysis.com/stocks/figr/financials/, stockanalysis.com/stocks/figr/company/
- final evidence status: evidence_complete
- remaining gaps: 收入构成（贷款发起 vs 市场交易 vs 数字资产）、FCF 负值原因、Provenance 链采纳数据
