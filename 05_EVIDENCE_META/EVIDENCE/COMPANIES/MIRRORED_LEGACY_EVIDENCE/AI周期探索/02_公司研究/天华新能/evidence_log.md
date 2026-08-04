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
legacy_path: "AI周期探索/02_公司研究/天华新能/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 天华新能 Evidence Log

## PRO source coverage

- Mindspace status: 零覆盖 — 碳酸锂频道搜索返回0条文章，无天华新能相关内容
- Mindspace gap: 无任何MCP数据（财报/估值/竞争/客户），完全依赖agent-reach
- agent-reach triggered: true
- fallback reason: Mindspace碳酸锂频道（唯一相关频道）返回空结果，无一手事实源
- fallback queries:
  - 同花顺：天华新能300390个股页面
  - 东方财富：天华新能300390行情页面
- fallback links:
  - 同花顺：Q1 2026净利润9.689亿（+1472%），GM 46.99%，NM 34.73%，P/E 21.19
  - 东方财富：收入结构（锂电87.77%），MSCI纳入（5/29生效），氢氧化锂17.2万/吨
- final evidence status: evidence_limited_after_fallback
- remaining gaps:
  - H股上市具体进度和预计时间表
  - CATL客户集中度精确数据
  - 氢氧化锂产能利用率和扩产计划
  - 自有锂矿储量/产量/成本具体数据

## 关键证据列表

### 证据1：同花顺Q1 2026财报数据

| 字段 | 内容 |
|---|---|
| source_name | 同花顺 |
| source_tab | data aggregator |
| source_id | agent-reach-jina |
| item_id | 10jqka-300390-q1-2026 |
| link | 同花顺天华新能个股页 |
| published_at | 2026-04-24 |
| evidence_use | 支撑"利润爆发"和"极高利润率"判断 |
| confidence | 高 |
| notes | 净利润9.689亿（+1472%），GM 46.99%，NM 34.73%，P/E 21.19，市值821亿 |

### 证据2：东方财富收入结构+MSCI纳入

| 字段 | 内容 |
|---|---|
| source_name | 东方财富 |
| source_tab | data aggregator |
| source_id | agent-reach-jina |
| item_id | eastmoney-300390 |
| link | 东方财富天华新能个股页 |
| published_at | 2026-05-13 |
| evidence_use | 支撑"收入结构"、"MSCI催化"和"锂价数据"判断 |
| confidence | 高 |
| notes | 锂电材料87.77%，MSCI中国新纳入（5/29生效），氢氧化锂17.2万/吨（+10.26%），碳酸锂19.2万/吨（+8.47%） |

### 证据3：国盛证券研报

| 字段 | 内容 |
|---|---|
| source_name | 国盛证券（via同花顺） |
| source_tab | report |
| source_id | agent-reach-jina |
| item_id | 10jqka-300390-report |
| link | 同花顺研报 |
| published_at | 2026-04-14 |
| evidence_use | 支撑"资源自给战略"和"主业盈利好转"判断 |
| confidence | 中 |
| notes | 标题"公司主业盈利能力大幅好转，资源自给战略稳步推进"，评级买入 |
