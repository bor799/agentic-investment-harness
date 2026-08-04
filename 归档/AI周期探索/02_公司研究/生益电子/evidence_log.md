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
legacy_path: "AI周期探索/02_公司研究/生益电子/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 生益电子 Evidence Log

## PRO source coverage

- Mindspace status: 弱覆盖 — DIGITIMES PCB行业报告提供CCL短缺+AI服务器PCB需求背景，无生益电子直接数据
- Mindspace gap: 无生益电子财报/估值/客户数据，MCP无法提供直接证据
- agent-reach triggered: true
- fallback reason: MCP无生益电子直接覆盖，PCB行业频道搜索无相关结果
- fallback queries:
  - 同花顺：生益电子688183个股页面
  - 东方财富：生益电子688183行情页面
- fallback links:
  - 同花顺：FY2025营收24.11亿，净利4.45亿(+122.16%)，EPS 0.54，6研报看多
  - 东方财富：股价97.61，市值811.9亿，P/E 47.27，P/B 13.24，624家机构持仓82.74%
- final evidence status: evidence_limited_after_fallback
- remaining gaps:
  - Q1 2026具体营收和净利润数据
  - 核心ASIC客户具体名称和订单规模
  - 新产能投产具体时间表
  - AI服务器PCB收入占比

## MCP行业背景证据

### 证据0：DIGITIMES CCL短缺+AI PCB需求

| 字段 | 内容 |
|---|---|
| source_name | DIGITIMES Asia |
| source_tab | review |
| source_id | mindspace-mcp-pcb-channel |
| item_id | digitimes-ccl-shortage-ai-pcb |
| link | DIGITIMES多篇文章 |
| published_at | 2026-03/05 |
| evidence_use | 支撑"母公司CCL协同是独特优势"判断 |
| confidence | 中 |
| notes | CCL交期延至6个月+配额制度，AI服务器驱动高端PCB需求暴增，高速互联对PCB提出更高要求 |

## 关键证据列表

### 证据1：同花顺FY2025财报+研报

| 字段 | 内容 |
|---|---|
| source_name | 同花顺 |
| source_tab | data aggregator |
| source_id | agent-reach-jina |
| item_id | 10jqka-688183-fy2025 |
| link | 同花顺生益电子个股页 |
| published_at | 2026-04-24 |
| evidence_use | 支撑"高增长"和"盈利改善"判断 |
| confidence | 高 |
| notes | FY2025营收24.11亿，净利4.45亿(+122.16%)，EPS 0.54，Q1 GM突破35%创新高，6研报看多 |

### 证据2：东方财富估值+机构持仓

| 字段 | 内容 |
|---|---|
| source_name | 东方财富 |
| source_tab | data aggregator |
| source_id | agent-reach-jina |
| item_id | eastmoney-688183 |
| link | 东方财富生益电子个股页 |
| published_at | 2026-05-15 |
| evidence_use | 支撑"估值"和"机构认可度"判断 |
| confidence | 高 |
| notes | 股价97.61，市值811.9亿，P/E 47.27，P/B 13.24，624家机构持仓82.74%，融资余额18.20亿 |
