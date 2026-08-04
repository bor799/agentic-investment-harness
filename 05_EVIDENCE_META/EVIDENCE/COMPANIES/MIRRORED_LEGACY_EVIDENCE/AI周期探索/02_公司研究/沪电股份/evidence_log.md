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
legacy_path: "AI周期探索/02_公司研究/沪电股份/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 沪电股份 Evidence Log

## PRO source coverage

- Mindspace status: 零覆盖 — 搜索返回IDC中国电信AI报告，无沪电股份直接数据
- Mindspace gap: 无沪电股份财报/估值/竞争数据，MCP无法提供直接证据
- agent-reach triggered: true
- fallback reason: MCP搜索无PCB行业频道，IDC报告与沪电股份无直接关联
- fallback queries:
  - 同花顺：沪电股份002463个股页面
  - 东方财富：沪电股份002463行情页面
- fallback links:
  - 同花顺：Q1 2026营收62.14亿，净利12.42亿（+62.90%），EPS 0.65，股价~103，6研报看多
  - 东方财富：FY2025分红10派5.00元，深股通标的，密集机构调研(13+10+24+39+25家)
- final evidence status: evidence_limited_after_fallback
- remaining gaps:
  - AI服务器/交换机PCB收入占比精确数据
  - 毛利率具体数值和趋势
  - 与竞争对手(胜宏/深南/生益/广合)的详细技术对比
  - 大客户(Nvidia/超大规模厂商)具体订单数据

## 关键证据列表

### 证据1：同花顺Q1 2026财报数据

| 字段 | 内容 |
|---|---|
| source_name | 同花顺 |
| source_tab | data aggregator |
| source_id | agent-reach-jina |
| item_id | 10jqka-002463-q1-2026 |
| link | 同花顺沪电股份个股页 |
| published_at | 2026-04-29 |
| evidence_use | 支撑"Q1高增长"和"估值"判断 |
| confidence | 高 |
| notes | Q1营收62.14亿，净利12.42亿（+62.90%），EPS 0.65，股价~103，市值~1982亿，P/E 39.89，PB 12.52 |

### 证据2：东方财富FY2025分红+机构调研

| 字段 | 内容 |
|---|---|
| source_name | 东方财富 |
| source_tab | data aggregator |
| source_id | agent-reach-jina |
| item_id | eastmoney-002463 |
| link | 东方财富沪电股份个股页 |
| published_at | 2026-05-18 |
| evidence_use | 支撑"分红安全垫"和"市场关注度"判断 |
| confidence | 高 |
| notes | FY2025分红10派5.00元（股息率~4.85%），深股通标的，4-5月密集机构调研(13+10+24+39+25=111家) |

### 证据3：6份研报覆盖

| 字段 | 内容 |
|---|---|
| source_name | 招商/国海/国投/广发/华安/中邮证券（via同花顺） |
| source_tab | report |
| source_id | agent-reach-jina |
| item_id | 10jqka-002463-reports |
| link | 同花顺研报 |
| published_at | 2026-04/05 |
| evidence_use | 支撑"AI PCB景气"和"扩产周期"判断 |
| confidence | 中 |
| notes | 全部买入，关键标题：AI持续高景气、26Q1业绩落于指引上沿大规模扩产周期全面开启、AI需求高度景气 |
