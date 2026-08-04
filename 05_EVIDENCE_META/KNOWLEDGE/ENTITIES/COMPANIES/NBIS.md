---
knowledge:
  knowledge_id: ENTITY-NBIS
  knowledge_type: entity_knowledge
  entity_id: NBIS
  entity_name: Nebius
  belief_ids: [NBIS-B01, NBIS-B02, NBIS-B03]
  decision_authority: none
layer: KNOWLEDGE
primary_role: entity_knowledge
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
last_reviewer: "PASS | injected | 2026-07-28"
---

# Nebius｜稳定实体知识

Nebius 是对 AI-B04 更纯粹、也更危险的检验：它先建设容量，再等待锚定客户与利用率把重资本转成重复利润。需求增长若慢于容量与融资，飞轮会反向旋转。

### NBIS-B01｜容量必须获得锚定客户与利用率

```yaml
belief:
  claim_id: NBIS-B01
  proposition: Nebius 的 AI 云只有在新增容量获得锚定客户并形成持续利用率时，才从建设故事变成经营资产。
  origin: co_created
  origin_ref: 05_EVIDENCE_META/KNOWLEDGE/DOMAINS/AI/README.md#AI-B04
  state: working
  mechanism: 数据中心和算力在投入后产生固定成本，利用率决定单位经济。
  supports_if: 锚定客户、已交付容量、使用量和利用率同步提升。
  weakens_if: 容量上线快于客户交付，闲置或价格竞争扩大。
  cannot_prove: ARR 或合同宣布等于容量已被使用。
  alternative_model: AI 云供给过剩使容量成为低回报商品。
  source_refs:
    - 05_EVIDENCE_META/EVIDENCE/COMPANIES/Nebius/README.md
    - 05_EVIDENCE_META/EVIDENCE/THEMES/260726AI基础设施_CurrentThesis重置证据.md
  latest_moment: MOM-260728-AI-CTRL-01
```

### NBIS-B02｜ARR 必须穿透到收入与 AI 云利润

```yaml
belief:
  claim_id: NBIS-B02
  proposition: Nebius 的 ARR 只有在转成确认收入、云毛利、经营利润和现金时，才证明需求质量与飞轮。
  origin: co_created
  origin_ref: 05_EVIDENCE_META/KNOWLEDGE/DOMAINS/AI/README.md#AI-B04
  state: working
  mechanism: ARR 是运行率指标，仍受交付、客户集中、定价和直接成本影响。
  supports_if: ARR 转收入稳定、AI 云利润改善、经营现金缺口收窄。
  weakens_if: ARR 高增长但收入转化、毛利或现金持续低于建设速度。
  cannot_prove: ARR 是客户现金或自由现金流。
  alternative_model: 大客户合同带来低毛利收入，规模扩大但资本回报不改善。
  source_refs:
    - 05_EVIDENCE_META/EVIDENCE/THEMES/260726AI基础设施_CurrentThesis重置证据.md
    - 03_STATE/HYPOTHESIS_QUEUE/CURRENT/NBIS.md
  latest_moment: MOM-260728-AI-CTRL-01
```

### NBIS-B03｜融资与摊薄不能先于飞轮

```yaml
belief:
  claim_id: NBIS-B03
  proposition: Nebius 必须在闲置、债务、项目融资和股权摊薄伤害每股价值前，证明容量利用率与云利润。
  origin: co_created
  origin_ref: 05_EVIDENCE_META/KNOWLEDGE/ENTITIES/COMPANIES/NBIS.md#NBIS-B01
  state: working
  mechanism: 资本先建容量，客户与利润后到；时间差由现金和融资承担。
  supports_if: 存量现金和客户资金覆盖建设，后续融资可控，每股收入与现金改善。
  weakens_if: 建设持续依赖大额股权融资或项目负债，而利用率和利润未兑现。
  cannot_prove: 现金余额等于经营造血，也不能把正式融资当客户需求。
  alternative_model: 资本市场长期补贴建设，使收入增长但股东索取权被稀释。
  source_refs:
    - 05_EVIDENCE_META/EVIDENCE/THEMES/260726AI基础设施_CurrentThesis重置证据.md
    - 03_STATE/HYPOTHESIS_QUEUE/CURRENT/NBIS.md
  latest_moment: MOM-260728-AI-CTRL-01
```

## 资金分账

| 项目 | 含义 | 不能混成什么 |
|---|---|---|
| 锚定客户承诺/ARR | 需求与运行率线索 | 不是客户现金或利润 |
| 实际客户资金 | 已收到且可定位的客户付款 | 不能由 ARR 自动推导 |
| 存量现金 | 历史融资与经营形成的现金池 | 不等于经营造血 |
| 债务/项目融资/股权 | 建设资金来源 | 不能更新客户需求或利用率 |
| 股价、成交、机构流入 | 市场预期与资金行为 | 不能更新经营 belief |

当前带时效判断：[[03_STATE/HYPOTHESIS_QUEUE/CURRENT/NBIS]]。冻结预期：[[03_STATE/EXPECTATIONS/AI/NBIS_NEXT_EARNINGS_v1]]。

