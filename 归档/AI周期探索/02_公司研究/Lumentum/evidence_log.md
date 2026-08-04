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
legacy_path: "AI周期探索/02_公司研究/Lumentum/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Lumentum Evidence Log

## MCP citation 规则

每条关键证据必须来自 Mindspace Source MCP，除非明确标注 fallback。

| source_name | source_tab | source_id | item_id | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|---|---|
| Long Investing Ideas from Seeking Alpha | official_press | 21dc2b4b-cd73-49d3-a828-ee40e43a45e6 | 50149fdb012aad924aba3ba186b7074d | seekingalpha.com/article/4886631 | 2026-03-27 | 核心证据：毛利率32.3%→42.5%，InP产能锁定至2027，OCS订单$400M+，营收$2.9B→$6.4B | 中高 | official_press级别，SA深度分析 |
| Long Investing Ideas from Seeking Alpha | official_press | 21dc2b4b-cd73-49d3-a828-ee40e43a45e6 | e406a0c1d8fbc21ab2481fe1e80ed6c6 | seekingalpha.com/article/4886906 | 2026-03-29 | 竞争背景：全球InP激光芯片短缺确认，Nvidia锁定供应，POET作为替代技术 | 中 | official_press级别，独立验证InP短缺 |

## 搜索记录

### 本轮搜索（2026-05-16 迭代 21）

MCP bridge via Bash：

1. search_articles("Lumentum LITE optical photonics laser transceiver data center", days_back=365) → 找到 1 篇直接相关 + 1 篇竞争背景
2. search_articles("Lumentum LITE earnings revenue optical laser", days_back=365) → 同样文章
3. get_article_detail(source_id=21dc2b4b, item_id=50149fdb) → 完整内容
4. get_article_detail(source_id=21dc2b4b, item_id=e406a0c1) → 完整内容

### 前轮搜索（2026-05-15 迭代 17）

前轮 9 组搜索全部返回 0（截断 channel id 误判问题，已修复）。本轮使用完整 channel id + bridge 重新搜索成功。

## 覆盖不足

- **无前瞻 P/E**：只有 ~100x 近期盈利估值
- **无营业利润率/净利率数据**：毛利率已知但净利率不明
- **无管理层指引原文**：营收路径来自 SA 分析师
- **无竞争对比**：vs Coherent (COHR)、Marvell

## fallback 记录

| fallback_reason | search_query | link | used_for | notes |
|---|---|---|---|---|
| 无需 fallback | N/A | N/A | N/A | MCP 数据充足完成研究 |

## Agent-Reach Sources (PRO Update 2026-05-17)

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| **StockAnalysis (SEC filings)** | TTM: Revenue $2.49B(+69%), GM 40.84%, OM 9.53%, NI $438.2M, FCF $114M(4.58%) | 财务核心 | 极高 | 从FY2024亏损-$546M扭转 |
| **StockAnalysis (forecast)** | FY2026E: Revenue $2.96B(+80%), EPS $7.76; FY2027E: $5.03B(+70%), EPS $16.13 | 预测 | 高 | |
| **StockAnalysis (analysts)** | Buy(16人), PT $830.07(-14.49%)⚠️, Range $145-$1,300 | 分析师估值 | 高 | PT低于现价 |

## PRO source coverage

- final evidence status: evidence_complete

## Evidence Assessment: PRO evidence_complete

覆盖4/4证据桶：
1. **财报/经营**: TTM Revenue $2.49B(+69%)/NI $438.2M(从-$546M扭亏)/FCF $114M(4.58%)
2. **估值/市场预期**: Market Cap $69.60B/Forward P/E 61.28/Buy PT -14.49%⚠️/FY2026-2027E
3. **结构性变化**: InP激光芯片短缺+产能锁定至2027+GM从24.7%→40.8%
4. **失败条件**: PT -14.5%低于现价+FCF margin仅4.58%+硅光子替代风险
