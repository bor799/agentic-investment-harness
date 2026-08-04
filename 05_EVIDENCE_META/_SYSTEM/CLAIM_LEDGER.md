---
title: claim_ledger
date: 2026-07-23
updated: 2026-07-28
layer: META
primary_role: claim_ledger
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
supersedes:
  - 05_EVIDENCE_META/META/CLAIM_LEDGER.md
---

# Claim Ledger

Claim Ledger 不给 belief 打机械总分。它只保证：命题可定位、更新可解释、同根不重复、预测能结算。

## Belief schema

```yaml
belief:
  claim_id:
  proposition:
  origin: murphy_explicit | co_created | ai_narrative | external_consensus
  origin_ref:
  state: candidate | working | supported | weakened | rejected
  mechanism:
  supports_if:
  weakens_if:
  cannot_prove:
  alternative_model:
  source_refs:
  latest_moment:
```

规则：

- `murphy_explicit` 表示来源身份，不表示命题已经被事实证明；
- `murphy_explicit` 必须指向逐字 `excerpt_id`；
- `working` 是允许犯错的工作假设，不是“高置信”；
- 前台建议同时维护约 4 条领域 belief、每个实体约 3 条 belief；这是注意力容量，不是知识上限。

## 唯一 belief update 接口

```yaml
belief_update:
  claim_id:
  root_source_id:
  direction: strong_support | support | no_change | weaken | strong_weaken
  independence: independent | same_root | unknown
  diagnosticity: high | medium | low
  evidence_channel: operating | customer_contract | customer_cash | formal_financing | market_price | market_flow | narrative
  updates_dimension: domain_model | demand | utilization | profit | cash | financing_capacity | capital_cost | market_expectation | H_R | H_L
  update_reason:
  counter_explanation:
  old_state:
  proposed_state:
  authority: suggestion_only
```

硬边界：

- 不允许自动应用 `proposed_state`；
- 不允许把方向映射成固定加减分、概率或权重；
- `same_root` 不得改变状态；
- `market_price/market_flow` 只能更新 `market_expectation/H_R/H_L`；
- `formal_financing` 只能更新 `financing_capacity/capital_cost`；
- RPO 或 ARR 不能标成 `customer_cash`；
- State、Knowledge 与资本动作仍需 Murphy + Reviewer + Validator。

## Active belief index

| Claim | 当前状态 | 唯一正文 |
|---|---|---|
| `AI-B01` | working | [[05_EVIDENCE_META/_SYSTEM/CLAIM_LEDGER#AI-B01｜生产级 Agent 需要模型之外的系统]] |
| `AI-B02` | working | [[05_EVIDENCE_META/_SYSTEM/CLAIM_LEDGER#AI-B02｜企业会为治理与私有部署持续付费]] |
| `AI-B03` | working | [[05_EVIDENCE_META/_SYSTEM/CLAIM_LEDGER#AI-B03｜普通智能商品化会迁移利润池]] |
| `AI-B04` | working | [[05_EVIDENCE_META/_SYSTEM/CLAIM_LEDGER#AI-B04｜只有“使用—合同—利润—现金”闭环才是新秩序飞轮]] |
| `ORCL-B01` | working | [[05_EVIDENCE_META/KNOWLEDGE/ENTITIES/COMPANIES/ORCL#ORCL-B01｜企业数据与流程形成迁移入口]] |
| `ORCL-B02` | working | [[05_EVIDENCE_META/KNOWLEDGE/ENTITIES/COMPANIES/ORCL#ORCL-B02｜客户钱必须从承诺走到收入与经营现金]] |
| `ORCL-B03` | working | [[05_EVIDENCE_META/KNOWLEDGE/ENTITIES/COMPANIES/ORCL#ORCL-B03｜容量建设风险必须识别最终承担者]] |
| `NBIS-B01` | working | [[05_EVIDENCE_META/KNOWLEDGE/ENTITIES/COMPANIES/NBIS#NBIS-B01｜容量必须获得锚定客户与利用率]] |
| `NBIS-B02` | working | [[05_EVIDENCE_META/KNOWLEDGE/ENTITIES/COMPANIES/NBIS#NBIS-B02｜ARR 必须穿透到收入与 AI 云利润]] |
| `NBIS-B03` | working | [[05_EVIDENCE_META/KNOWLEDGE/ENTITIES/COMPANIES/NBIS#NBIS-B03｜融资与摊薄不能先于飞轮]] |

## AI active belief bodies

以下四条是 Claim Ledger 内的唯一完整正文。领域地图只反向链接，不复制正文。

### AI-B01｜生产级 Agent 需要模型之外的系统

```yaml
belief:
  claim_id: AI-B01
  proposition: 企业生产级 Agent 需要持久状态、数据权限、审计、回退和人工接管；裸模型调用不足以独立承担生产责任。
  origin: murphy_explicit
  origin_ref: 05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源.md#EX-01
  state: working
  mechanism: 任务跨系统执行会产生权限、状态、责任与故障恢复要求。
  supports_if: 企业采购、部署或监管披露把权限、审计、回退、评测列为生产必需。
  weakens_if: 大量关键任务长期由裸模型或简单封装稳定运行，且无额外治理预算。
  cannot_prove: 第三方控制平面一定能收费，或某家公司一定受益。
  alternative_model: 模型供应商或云厂商把控制能力免费内置，独立控制平面无利润池。
  source_refs:
    - 05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源.md#EX-01
    - 05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源.md#EX-02
    - 05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源.md#EX-03
  latest_moment: MOM-260728-AI-CTRL-01
```

### AI-B02｜企业会为治理与私有部署持续付费

```yaml
belief:
  claim_id: AI-B02
  proposition: 当 AI 进入关键流程后，企业更可能为私有/混合部署、数据治理、存储、权限和审计持续付费，而不是永远接受免费打包。
  origin: murphy_explicit
  origin_ref: 05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源.md#EX-05
  state: working
  mechanism: 生产责任、数据安全与运维成本不会因模型调用价格下降而消失。
  supports_if: 独立合同、付费席位、按量任务、合同负债或续费披露持续扩张。
  weakens_if: 原生云/模型套件免费覆盖主要需求，第三方产品的续费与净留存走弱。
  cannot_prove: 免费方案一定消失，或合同额一定转成高毛利现金流。
  alternative_model: 治理成为云基础套餐的获客成本，客户没有独立付费意愿。
  source_refs:
    - 05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源.md#EX-05
  latest_moment: MOM-260728-AI-CTRL-01
```

### AI-B03｜普通智能商品化会迁移利润池

```yaml
belief:
  claim_id: AI-B03
  proposition: 开放权重与多模型替代会压低普通智能的定价权，并可能把部分利润池迁向数据语义、业务流程、权限、安全、路由和交付结果。
  origin: murphy_explicit
  origin_ref: 05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源.md#EX-04
  state: working
  mechanism: 替代选项增加会削弱单一模型议价权，但企业生产约束仍需被解决。
  supports_if: 多模型调用占比提高，同时治理、工作流与数据平台收入和客户支出增加。
  weakens_if: 前沿模型能力差距长期扩大，客户仍围绕单一模型形成不可替代工作流。
  cannot_prove: 模型公司利润绝对下降，或利润只会流向第三方控制平面。
  alternative_model: 模型公司前向整合 Agent、数据和工作流，继续捕获大部分利润。
  source_refs:
    - 05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源.md#EX-01
    - 05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源.md#EX-04
  latest_moment: MOM-260728-AI-CTRL-01
```

### AI-B04｜只有“使用—合同—利润—现金”闭环才是新秩序飞轮

```yaml
belief:
  claim_id: AI-B04
  proposition: AI 新秩序只有在使用量转成重复合同、容量利用率、利润和现金时才形成可投资飞轮；叙事与合同单独都不够。
  origin: co_created
  origin_ref: 05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源.md#EX-07
  state: working
  mechanism: 重复使用提高数据与流程黏性，但重资本扩张、推理成本和融资可能吞掉收入。
  supports_if: 使用、ARR 或 RPO 转收入，毛利与经营现金同步改善，单位资本产出上升。
  weakens_if: 合同增长依赖补贴或融资，利用率、利润和每股现金长期不改善。
  cannot_prove: 任何高增长 AI 云都已形成飞轮。
  alternative_model: 需求真实但供给竞争使云算力成为低回报公用事业。
  source_refs:
    - 05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源.md#EX-07
    - 05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源.md#EX-08
    - 05_EVIDENCE_META/EVIDENCE/THEMES/260726AI基础设施_CurrentThesis重置证据.md
  latest_moment: MOM-260728-AI-CTRL-01
```

## 兼容历史规则

旧 `evidence_status` 与 `murphy_status` 仅用于解释历史账本；“已吸收、已采纳、高置信”不映射为新 belief 的 `supported`。历史原文仍在 [[01_道/_HISTORY/260722旧认知命题证据账本_历史原文]]。

材料处理结果仍是 `absorb / revise / observe / reject`；没有改变“应该相信什么”的内容留在 Source 或拒绝，不创建重复 claim。
