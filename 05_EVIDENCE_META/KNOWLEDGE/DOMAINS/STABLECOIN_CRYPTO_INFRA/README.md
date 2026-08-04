---
knowledge:
  knowledge_id: DOMAIN-STABLECOIN-CRYPTO-INFRA
  knowledge_type: domain_pattern_map
  domain_id: STABLECOIN_CRYPTO_INFRA
  qualified_pattern_ids: [SCI-P01]
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

# 稳定币与加密基础设施领域判断地图

## 60 秒入口

- 合格模式：`SCI-P01`
- 首要反模式：把稳定币发行、托管交易和 BTC 资本结构载体当成同一种机会。
- 第一问题：普通股到底拥有哪一层收费权和索取顺位？

## 合格模式

### SCI-P01｜先分清收费池与普通股索取权

```yaml
qualified_pattern:
  pattern_id: SCI-P01
  recognition_cues:
    - 标的都被归入加密或稳定币主题
    - 收入可能来自储备利息、分发、交易、托管、质押或资产价格
  causal_chain: 底层活动增长 → 对应环节收费 → 分成、合规、融资和固定索取权后留下利润 → 普通股每股现金或资产增加
  payer_and_money_path: 用户、交易方或储备资产支付收益；必须按发行、分发、托管、交易和资本结构分别核算
  profit_control: 净储备收益、take rate、分发成本、单位贡献利润、债务与优先股顺位、完全摊薄股数
  favorable_fit: 收费池清晰且可重复，成本和优先索取后仍形成普通股现金
  counterpattern_and_falsifier: 主题增长但分发成本、负 EBITDA、债务、优先股或摊薄吞掉普通股收益
  applicable_asset_types: [operating_company, capital_structure_vehicle]
  linked_cases:
    - 04_CASE_GYM/RESEARCH_CASES/260724_bitgo_btgo_投资决策_legacy_source_case.md
    - 04_CASE_GYM/RESEARCH_CASES/260724_hashkey_hashkey_投资决策_legacy_source_case.md
  first_questions:
    - 收入来自哪一层收费池？
    - 直接成本和分成后单位利润是多少？
    - 普通股前面有哪些债务、优先股或摊薄？
  root_sources:
    - https://www.sec.gov/Archives/edgar/data/1876042/000187604226000150/crcl-20260331.htm
    - https://investors.bitgo.com/financials/quarterly-results/default.aspx
    - https://www.sec.gov/Archives/edgar/data/1050446/000119312526295586/mstr-20260706.htm
  reused_targets_or_settled_cases: [CRCL, BTGO, MSTR]
```

## 资产与 Case

- [[03_STATE/HYPOTHESIS_QUEUE/CURRENT/CRCL]]
- [[03_STATE/HYPOTHESIS_QUEUE/CURRENT/BTGO]]
- [[03_STATE/HYPOTHESIS_QUEUE/CURRENT/MSTR]]
- [[04_CASE_GYM/RESEARCH_CASES/260724_bitgo_btgo_投资决策_legacy_source_case]]
- [[04_CASE_GYM/RESEARCH_CASES/260724_hashkey_hashkey_投资决策_legacy_source_case]]
- dated synthesis：[[05_EVIDENCE_META/EVIDENCE/THEMES/260726稳定币与加密基础设施_CurrentThesis重置证据]]
