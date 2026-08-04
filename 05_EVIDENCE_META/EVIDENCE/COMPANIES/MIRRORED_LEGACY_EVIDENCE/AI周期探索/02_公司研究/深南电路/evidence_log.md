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
legacy_path: "AI周期探索/02_公司研究/深南电路/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 深南电路 Evidence Log

## PRO source coverage

- Mindspace status: 零覆盖 — 搜索无深南电路直接数据
- Mindspace gap: 无深南电路财报/估值/载板数据，MCP无法提供直接证据
- agent-reach triggered: true
- fallback reason: MCP无深南电路直接覆盖
- fallback queries:
  - 同花顺：深南电路002916个股页面
  - 东方财富：深南电路002916行情页面
- fallback links:
  - 同花顺：Q1营收65.96亿(+38%)，净利8.50亿(+73%)，1103家机构，6研报买入
  - 东方财富：股价323.25，市值2202亿，P/E 64.74，GM 29.17%，行业第3/65
- final evidence status: evidence_limited_after_fallback
- remaining gaps:
  - IC载板(FC-BGA)具体良率和产能利用率
  - 无锡46亿扩产项目具体投产时间
  - AI PCB收入占比
  - 载板业务盈亏平衡点和利润率

## 关键证据列表

### 证据1：同花顺Q1 2026财报+研报

| 字段 | 内容 |
|---|---|
| source_name | 同花顺 |
| source_tab | data aggregator |
| source_id | agent-reach-jina |
| item_id | 10jqka-002916-q1-2026 |
| link | 同花顺深南电路个股页 |
| published_at | 2026-04-24 |
| evidence_use | 支撑"高增长"和"双轮驱动"判断 |
| confidence | 高 |
| notes | Q1营收65.96亿(+37.90%)，净利8.50亿(+73.01%)，EPS 1.28，1103家机构，6研报买入，无锡46亿扩产 |

### 证据2：东方财富估值+行业排名

| 字段 | 内容 |
|---|---|
| source_name | 东方财富 |
| source_tab | data aggregator |
| source_id | agent-reach-jina |
| item_id | eastmoney-002916 |
| link | 东方财富深南电路个股页 |
| published_at | 2026-05-15 |
| evidence_use | 支撑"估值"和"行业地位"判断 |
| confidence | 高 |
| notes | 股价323.25，市值2202亿，P/E 64.74，P/B 12.17，GM 29.17%，NM 12.91%，行业第3/65市值，负债率47.24% |
