---
title: provenance_schema
date: 2026-07-23
updated: 2026-07-28
layer: META
primary_role: provenance_schema
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
supersedes:
  - 05_EVIDENCE_META/META/PROVENANCE_SCHEMA.md
---

# Provenance Schema

## 通用 frontmatter

```yaml
layer: MINDSET | CONSTITUTION | METHOD | STATE | CASE | KNOWLEDGE | MOMENT | SOURCE | META | AUTOMATION
primary_role: one_role_only
status: active | candidate | experimental | superseded | archived | retired
authored_by: murphy | human_ai | ai | external
source_type: P0 | P1 | P2 | P3 | PX
human_reviewed: true | false
decision_authority: none | operational | murphy_confirmed
research_authority: none | candidate_generation
data_cutoff:
expires_at:
supersedes:
source_paths:
```

`authored_by: murphy` 只用于可定位的 Murphy 原文。`human_reviewed: true` 不等于 Murphy 认同全部内容。Knowledge、Moment、Source 与 Case 都不能靠脚本把自己改成 `murphy_confirmed`。

## 四种研究知识类型

| 类型 | canonical path | 权限 |
|---|---|---|
| `domain_knowledge` | `05_EVIDENCE_META/KNOWLEDGE/DOMAINS/<domain>/README.md` | 研究导航，不产生动作 |
| `entity_knowledge` | `05_EVIDENCE_META/KNOWLEDGE/ENTITIES/{COMPANIES,ETFS}/` | 稳定商业结构，不保存当前估值 |
| `moment` | `05_EVIDENCE_META/MOMENTS/`；处理后到 `_ARCHIVE/MOMENTS/` | 只记录认知差分 |
| `source` | `05_EVIDENCE_META/SOURCES/<YYYY>/` | 只保存可追溯材料 |
| `active_expectation` | `03_STATE/EXPECTATIONS/<domain>/` | 冻结、版本化、可结算 |

## 来源身份

| source_type | 含义 | 可做什么 | 不能做什么 |
|---|---|---|---|
| P0 | 可定位 Murphy 原话、人工裁决、人工修订或本人数据 | 证明 Murphy 表达过什么 | 自动证明产业事实或覆盖新证据 |
| P1 | Murphy 指定的重要材料 | 进入候选差分 | 直接变成 confirmed |
| P2 | 公司、监管、交易所、基金公告、券商/TA 回报 | 更新事实和世界模型 | 自动代表 Murphy 认同 |
| P3 | AI 整理、二手材料、混合稿中的 AI 扩写 | 提供线索 | 更新人格、仓位、概率或四票 |
| PX | 纯 AI 自主探索或来源不明材料 | 保留线索或拒绝 | 进入决策权威层 |

混合文件按段落定权。P0 原话必须保存逐字节选、日期、`excerpt_id` 和关联 `claim_ids`；AI 摘要必须标 `authority: none`。

## 回源与去重

1. 先读本地索引，避免重复研究。
2. 再读公司 IR、监管、交易所、财报和可定位全文。
3. 搜索器或聚合摘要不能直接升为 P2。
4. 同一 `root_source_id + claim_id` 只产生一次有效更新；同根复述不增加置信。
5. 工具不可用时写 `evidence_limited_after_fallback`，不以 AI 记忆补事实。

## 证据六层

新材料拆成：事实、解释、假设、预测、情绪、权限。价格和市场资金只能更新市场预期、`H_R/H_L`；公司经营披露才可更新经营 belief。正式融资只可更新融资能力与资本成本，不能自动更新客户需求、利用率或利润。

## 数值取证

财务数字至少核对单位、基期、正负号、报告范围、一次性项目和口径。RPO、ARR、客户预付款、收入、经营现金、债务、股权、租赁和供应商融资必须分账，不得重复计算。

ETF 资料必须分开净值、份额、规模、申赎、实际持仓、基准、包装结构、交易时点、折溢价、买卖价差和退出深度。

