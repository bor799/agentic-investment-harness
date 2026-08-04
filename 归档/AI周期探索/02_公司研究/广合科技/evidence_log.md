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
legacy_path: "AI周期探索/02_公司研究/广合科技/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 广合科技 Evidence Log

## PRO source coverage

- Mindspace status: 零覆盖 — 无广合科技直接数据
- Mindspace gap: 无广合科技财报/估值/客户数据，MCP无法提供直接证据
- agent-reach triggered: true
- fallback reason: MCP无广合科技直接覆盖
- fallback queries:
  - 同花顺：广合科技001389个股页面
  - 东方财富：广合科技001389行情页面
- fallback links:
  - 同花顺：Q1营收19.14亿(+71%)，净利3.93亿(+63%)，262机构，5研报买入，PCIE6.0 Q3量产
  - 东方财富：A股价180.68/H股价179.00，市值853.7亿，P/E 54.37，GM 36.93%，NM 20.51%
- final evidence status: evidence_limited_after_fallback
- remaining gaps:
  - Q1 AI算力PCB收入占比
  - PCIE6.0具体订单量和ASP提升幅度
  - 新客户认证进展具体名单
  - 限售股解禁时间表
  - 泰国工厂产能规划

## 关键证据列表

### 证据1：同花顺Q1 2026财报+客户信息

| 字段 | 内容 |
|---|---|
| source_name | 同花顺 |
| source_tab | data aggregator |
| source_id | agent-reach-jina |
| item_id | 10jqka-001389-q1-2026 |
| link | 同花顺广合科技个股页 |
| published_at | 2026-04-30 |
| evidence_use | 支撑"高增长"和"客户广度"判断 |
| confidence | 高 |
| notes | Q1营收19.14亿(+71.35%)，净利3.93亿(+63.31%)，EPS 0.93，PCIE6.0 Q3量产，TOP10服务器厂商8个是客户，5研报买入 |

### 证据2：东方财富估值+A/H价格

| 字段 | 内容 |
|---|---|
| source_name | 东方财富 |
| source_tab | data aggregator |
| source_id | agent-reach-jina |
| item_id | eastmoney-001389 |
| link | 东方财富广合科技个股页 |
| published_at | 2026-05-15 |
| evidence_use | 支撑"A/H估值"和"利润率最高"判断 |
| confidence | 高 |
| notes | A股价180.68/H股价179.00(几乎无溢价)，市值853.7亿，P/E 54.37，GM 36.93%，NM 20.51%，ROE 9.28%，负债率37.19%，流通盘仅32%，泰国工厂$8000万扩产 |
