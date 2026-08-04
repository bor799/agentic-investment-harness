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
legacy_path: "AI周期探索/02_公司研究/胜宏科技/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 胜宏科技 Evidence Log

## PRO source coverage

- Mindspace status: 弱覆盖 — 仅1篇ABF市场报告（间接相关），无胜宏科技具体数据
- Mindspace gap: 无胜宏科技财报/估值/竞争数据，MCP无法提供直接证据
- agent-reach triggered: true
- fallback reason: MCP无PCB行业频道，AI market trends频道搜索无胜宏科技相关结果
- fallback queries:
  - 同花顺：胜宏科技300476个股页面
  - 东方财富：胜宏科技300476行情页面
- fallback links:
  - 同花顺：Q1 2026营收55.19亿，净利12.88亿（+39.95%），EPS 1.48，6研报看多
  - 东方财富：FY2025营收192.93亿（PCB 93.74%），港股通调入05-15，169家机构调研
- final evidence status: evidence_limited_after_fallback
- remaining gaps:
  - AI服务器PCB收入占比精确数据
  - 海外大客户具体名单
  - 与竞争对手（沪电/深南/生益）的毛利率/技术对比
  - Nvidia Rubin平台PCB订单量和ASP

## 关键证据列表

### 证据1：同花顺Q1 2026财报数据

| 字段 | 内容 |
|---|---|
| source_name | 同花顺 |
| source_tab | data aggregator |
| source_id | agent-reach-jina |
| item_id | 10jqka-300476-q1-2026 |
| link | 同花顺胜宏科技个股页 |
| published_at | 2026-04-29 |
| evidence_use | 支撑"Q1增长"和"利润率"判断 |
| confidence | 高 |
| notes | Q1营收55.19亿，净利12.88亿（+39.95%），EPS 1.48，股价~345，市值~3391亿 |

### 证据2：东方财富FY2025收入结构+港股通

| 字段 | 内容 |
|---|---|
| source_name | 东方财富 |
| source_tab | data aggregator |
| source_id | agent-reach-jina |
| item_id | eastmoney-300476 |
| link | 东方财富胜宏科技个股页 |
| published_at | 2026-05-15 |
| evidence_use | 支撑"收入结构"和"A+H双上市"判断 |
| confidence | 高 |
| notes | FY2025营收192.93亿（PCB 180.84亿=93.74%），港股通调入05-15，169家机构调研05-11 |

### 证据3：6份研报覆盖

| 字段 | 内容 |
|---|---|
| source_name | 野村/招商/东北/财信/国海/华安证券（via同花顺） |
| source_tab | report |
| source_id | agent-reach-jina |
| item_id | 10jqka-300476-reports |
| link | 同花顺研报 |
| published_at | 2026-04/05 |
| evidence_use | 支撑"AI PCB龙头"和"Nvidia Rubin催化"判断 |
| confidence | 中 |
| notes | 全部增持/买入，关键标题：AI PCB全球龙头、Rubin备货、产能扩张、全球化布局 |
