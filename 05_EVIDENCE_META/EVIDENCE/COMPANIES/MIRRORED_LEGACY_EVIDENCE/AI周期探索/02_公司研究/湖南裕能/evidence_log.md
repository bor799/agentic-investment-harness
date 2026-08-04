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
legacy_path: "AI周期探索/02_公司研究/湖南裕能/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 湖南裕能 Evidence Log

## PRO source coverage

- Mindspace status: 弱覆盖 — 仅3条推文（川沐/Trumoo, 2026-04-29）
- Mindspace gap: 财报数据、估值指标、竞争格局、LMFP技术细节均无MCP覆盖
- agent-reach triggered: true
- fallback reason: Mindspace仅覆盖市场情绪（推文），缺少一手事实源（财报/公告/研报）
- fallback queries:
  - "湖南裕能 301358 2025年报 2026一季报 营收 利润 产能 客户集中度"
  - 同花顺个股页面（Q1 2026财务数据）
  - 东方财富个股页面（估值/研报/分红）
- fallback links:
  - 同花顺：湖南裕能Q1 2026财报数据（营收149.65亿/+121%，净利13.56亿/+1338%）
  - 东方财富：动态P/E 14.84，股价95.48，6份研报，10派3.56元分红
  - MCP推文：Q1利润爆发确认，宁德时代持股7.88%，储能板块结构性转变
- final evidence status: evidence_limited_after_fallback
- remaining gaps:
  - 客户集中度精确数据（CATL/BYD占比）
  - LMFP vs LFP技术路线详细对比
  - 竞争对手（德方纳米/万润新能）最新产能和市占率
  - 磷矿自给率和对成本的实际贡献

## 关键证据列表

### 证据1：Q1 2026利润爆发

| 字段 | 内容 |
|---|---|
| source_name | 同花顺 (via Jina Reader) |
| source_tab | data aggregator |
| source_id | agent-reach-jina |
| item_id | 10jqka-301358-q1-2026 |
| link | 同花顺湖南裕能个股页 |
| published_at | 2026-04-29 |
| evidence_use | 支撑"周期拐点确认"和"利润率大幅改善"判断 |
| confidence | 高 |
| notes | 同花顺数据来自公司正式财报，可靠性高 |

### 证据2：LFP价格翻倍+订单饱满

| 字段 | 内容 |
|---|---|
| source_name | 东方财富 (via Jina Reader) |
| source_tab | data aggregator |
| source_id | agent-reach-jina |
| item_id | eastmoney-301358 |
| link | 东方财富湖南裕能个股页 |
| published_at | 2026-05 |
| evidence_use | 支撑"供需反转"和"估值隐含预期"判断 |
| confidence | 高 |
| notes | LFP价格从3万→6万/吨，订单排至年底，6份研报全部看多 |

### 证据3：宁德时代持股+储能转型

| 字段 | 内容 |
|---|---|
| source_name | 川沐/Trumoo推文 |
| source_tab | forum |
| source_id | mindspace-twitter-trumoo |
| item_id | trumoo-2026-04-29-lfp |
| link | MCP推文 |
| published_at | 2026-04-29 |
| evidence_use | 支撑"客户绑定"和"储能结构性变化"判断 |
| confidence | 中 |
| notes | 推文为情绪源，核心财务数据已由同花顺/东方财富验证 |
