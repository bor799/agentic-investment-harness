---
knowledge:
  knowledge_id: DOMAIN-CONSUMER-IP
  knowledge_type: domain_pattern_map
  domain_id: CONSUMER_IP
  qualified_pattern_ids: [CIP-P01]
  candidate_pattern_ids: []
  decision_authority: none
  research_authority: structural_prior_only
layer: KNOWLEDGE
primary_role: domain_knowledge
status: active
authored_by: human_ai
source_type: P3
human_reviewed: false
last_reviewer: "PASS | independent_readonly | 2026-07-28"
---

# 消费与 IP 领域判断地图

## 60 秒入口

- 合格模式：`CIP-P01`
- 首要反模式：门店、热门角色或收入高速增长，但利润率、库存和自由现金恶化。
- 第一问题：增长是健康复购与周转，还是库存和渠道扩张？

## 合格模式

### CIP-P01｜热度必须穿透到周转与自由现金

```yaml
qualified_pattern:
  pattern_id: CIP-P01
  recognition_cues:
    - IP、爆品、门店或海外收入高速增长
    - 库存、渠道投入或营销费用同步上升
  causal_chain: 产品或 IP 命中 → 同店与复购 → 毛利覆盖渠道和营销 → 库存健康周转 → 自由现金增长
  payer_and_money_path: 消费者为产品与体验付费，门店和渠道扣除后形成经营现金
  profit_control: 同店、毛利、库存周转、减值、单店经济和自由现金流
  favorable_fit: 收入增长同时维持利润率，库存不快于收入，现金回收改善
  counterpattern_and_falsifier: 热度依赖单一 IP，库存快于收入，利润率或自由现金持续下降
  applicable_asset_types: [operating_company]
  linked_cases:
    - 04_CASE_GYM/TRADE_LOG/260226_miniso_ip_thesis_case.md
    - 04_CASE_GYM/RESEARCH_CASES/260226_popmart_missed_opportunity_case.md
  first_questions:
    - 同店和复购贡献多少？
    - 库存增长是否快于收入？
    - 自由现金能否覆盖扩店和渠道投入？
  root_sources:
    - https://ir.miniso.com/2026-05-26-MINISO-Group-Announces-March-Quarter-2026-Unaudited-Financial-Results
    - https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0325/2026032500285.pdf
    - https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0512/2026051200579.pdf
  reused_targets_or_settled_cases: [09896, 09992]
```

## 资产与 Case

- [[03_STATE/HYPOTHESIS_QUEUE/CURRENT/09896]]
- [[03_STATE/HYPOTHESIS_QUEUE/CURRENT/09992]]
- [[04_CASE_GYM/TRADE_LOG/260226_miniso_ip_thesis_case]]
- [[04_CASE_GYM/RESEARCH_CASES/260226_popmart_missed_opportunity_case]]
- dated synthesis：[[05_EVIDENCE_META/EVIDENCE/THEMES/260726中国消费与IP_CurrentThesis重置证据]]
