---
knowledge:
  knowledge_id: ENTITY-ORCL
  knowledge_type: entity_knowledge
  entity_id: ORCL
  entity_name: Oracle
  belief_ids: [ORCL-B01, ORCL-B02, ORCL-B03]
  decision_authority: none
layer: KNOWLEDGE
primary_role: entity_knowledge
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
last_reviewer: "PASS | injected | 2026-07-28"
---

# Oracle｜稳定实体知识

Oracle 在本领域的研究价值不是“也是一家云公司”，而是数据库、ERP、权限关系和企业合同可能形成 AI 数据引力；真正要验证的是这种引力能否在不伤害每股现金的情况下变成云收入。

### ORCL-B01｜企业数据与流程形成迁移入口

```yaml
belief:
  claim_id: ORCL-B01
  proposition: Oracle 的数据库与企业应用装机基础可能让客户更容易把受治理的数据和流程迁入 Oracle 的 AI 云任务。
  origin: co_created
  origin_ref: 05_EVIDENCE_META/KNOWLEDGE/DOMAINS/AI/README.md#AI-B01
  state: working
  mechanism: 数据位置、权限模型和业务流程降低同平台部署摩擦。
  supports_if: 数据库/应用客户转为 OCI AI 使用、跨云数据库使用和重复云合同。
  weakens_if: 客户把 AI 工作负载主要放到其他云，Oracle 数据不形成任务引力。
  cannot_prove: 装机基础必然带来高毛利 AI 收入。
  alternative_model: Oracle 只是用低价容量承接需求，数据引力不足以形成定价权。
  source_refs:
    - 05_EVIDENCE_META/EVIDENCE/COMPANIES/Oracle/README.md
    - 05_EVIDENCE_META/EVIDENCE/THEMES/260726AI基础设施_CurrentThesis重置证据.md
  latest_moment: MOM-260728-AI-CTRL-01
```

### ORCL-B02｜客户钱必须从承诺走到收入与经营现金

```yaml
belief:
  claim_id: ORCL-B02
  proposition: Oracle 的企业 AI 逻辑只有在合同承诺逐步变成云收入、经营利润和经营现金时才被验证。
  origin: co_created
  origin_ref: 05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源.md#EX-06
  state: working
  mechanism: RPO 只代表待履约承诺；收入确认、利润与现金回收取决于交付和成本。
  supports_if: RPO 转收入、IaaS 使用、云毛利与经营现金同步改善。
  weakens_if: RPO 增长但转收入放慢，现金流或单位资本回报持续恶化。
  cannot_prove: RPO 等于客户预付款或客户现金已经收到。
  alternative_model: 长合同主要锁定低回报容量，收入增长不能覆盖资本成本。
  source_refs:
    - 05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源.md#EX-06
    - 05_EVIDENCE_META/EVIDENCE/THEMES/260726AI基础设施_CurrentThesis重置证据.md
  latest_moment: MOM-260728-AI-CTRL-01
```

### ORCL-B03｜容量建设风险必须识别最终承担者

```yaml
belief:
  claim_id: ORCL-B03
  proposition: Oracle 的每股价值取决于客户、股东与债权人如何分担容量建设风险，以及利用率兑现是否快于融资成本。
  origin: co_created
  origin_ref: 05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源.md#EX-06
  state: working
  mechanism: 客户预付款或客户供货可降低 Oracle 前置资本，但债务、股权、租赁和供应商融资会产生不同成本与索取权。
  supports_if: 实际客户资金和利用率上升，资本开支强度下降，自由现金改善且稀释受控。
  weakens_if: 建设先于利用率，融资和摊薄持续扩大，客户承诺不能覆盖资本成本。
  cannot_prove: “大量资金进入”来自哪一类资金，也不能把融资能力当成客户需求。
  alternative_model: Oracle 依靠资产负债表补贴云容量，规模增长但每股回报下降。
  source_refs:
    - 05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源.md#EX-06
    - 03_STATE/HYPOTHESIS_QUEUE/CURRENT/ORCL.md
  latest_moment: MOM-260728-AI-CTRL-01
```

## 资金分账

| 项目 | 含义 | 不能混成什么 |
|---|---|---|
| RPO | 未履约合同承诺 | 不是现金 |
| 实际客户预付款/客户供货 | 客户已承担的部分建设资金或设备 | 不能由 RPO 自动推导 |
| 云收入、经营利润、经营现金 | 已交付后的经营兑现 | 不能由合同额替代 |
| 债务、股权、租赁、供应商融资 | 容量融资来源 | 不能当客户需求或利润 |
| 股价、成交、机构流入 | 市场预期与资金行为 | 不能更新经营 belief |

当前带时效判断：[[03_STATE/HYPOTHESIS_QUEUE/CURRENT/ORCL]]。冻结预期：[[03_STATE/EXPECTATIONS/AI/ORCL_FY27Q1_v1]]。

