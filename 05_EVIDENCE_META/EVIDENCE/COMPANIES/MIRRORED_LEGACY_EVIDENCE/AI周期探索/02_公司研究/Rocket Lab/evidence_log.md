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
legacy_path: "AI周期探索/02_公司研究/Rocket Lab/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Rocket Lab Evidence Log (PRO Updated 2026-05-16)

## MCP搜索记录

### PRO修复搜索（2026-05-16）
1. health_check → 通过
2. search_channels("Rocket Lab RKLB space launch") → 10 channels, X sources (candidate_score 600, 120 matched)
3. search_articles(channel=b0e8adcc, X sources) → 1条RKLB相关（CEO薪酬），其余为SpaceX/NASA背景

## MCP Evidence

| source_name | source_tab | source_id | item_id | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|---|---|
| Ted Zhang | official_press | 9a18e631-46c1-4ed9-b9a1-c8b4ffe58a14 | 2039740135110062150 | twitter.com | 2026-04-02 | CEO薪酬：CEO更关注使命而非个人报酬 | 低 | 仅推文片段 |
| a16z | official_press | 6f3fde4b-7fbe-4002-8dc0-5adf0046f7b4 | 2036442912419094597 | twitter.com | 2026-03-24 | 行业背景：太空经济有地面基础设施问题 | 中 | 行业趋势 |

## Agent-Reach Fallback 证据

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| StockAnalysis.com | 市值$73.55B(+555%), 价格~$127 | 估值基准 | 高 | |
| StockAnalysis.com | TTM营收$679.58M(+45.8%) | 核心财务 | 高 | |
| StockAnalysis.com | FY2025营收$601.80M(+37.96%) | 年度趋势 | 高 | |
| StockAnalysis.com | 净亏损$182.62M, EPS -$0.33 | 盈利状态 | 高 | |
| StockAnalysis.com | 15位分析师Strong Buy, 目标$86.86 | 市场预期 | 高 | 目标低于现价32% |
| StockAnalysis.com | 员工2,600, Aerospace & Defense | 公司信息 | 高 | |

## PRO source coverage

- Mindspace status: ✅ 通过（覆盖极低，1条相关推文）
- Mindspace gap: 无财报/发射数据/Neutron进展/太空系统收入
- agent-reach triggered: yes
- fallback reason: MCP几乎零覆盖
- fallback queries: Rocket Lab RKLB stock analysis
- fallback links: stockanalysis.com/stocks/rklb/
- final evidence status: evidence_complete（财务数据）
- remaining gaps: Neutron开发进展、发射频率精确数据、太空系统收入占比
