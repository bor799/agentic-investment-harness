---
knowledge:
  knowledge_id: DOMAIN-RESOURCES-POWER-GRID
  knowledge_type: domain_pattern_map
  domain_id: RESOURCES_POWER_GRID
  qualified_pattern_ids: [RPG-P01]
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

# 资源、电力与电网领域判断地图

## 60 秒入口

- 合格模式：`RPG-P01`
- 首要反模式：用“电力需求增长”同时给矿企、发电公司和设备 ETF 加分。
- 第一问题：需求通过价格、产量、电价、利用小时还是设备订单进入利润？

## 合格模式

### RPG-P01｜相同需求必须按资产钱路拆开

```yaml
qualified_pattern:
  pattern_id: RPG-P01
  recognition_cues:
    - 多类资产共享资源、电力或电网叙事
    - 政策、需求或资本开支被直接等同于公司利润
  causal_chain: 宏观需求或投资 → 各资产专属经营变量 → 单位利润与回款 → 经营现金 → 每股价值
  payer_and_money_path: 矿企由资源价格与低成本产量支付；公用事业由电价与利用小时支付；设备公司由订单、毛利和回款支付；ETF 由成分盈利与资金共同支付
  profit_control: 周期正常化成本、单位利润、电价、利用小时、资本开支、订单质量、应收回款和产品映射
  favorable_fit: 专属经营变量与现金共同改善，资本开支没有吞掉每股价值
  counterpattern_and_falsifier: 商品高价制造峰值低 PE，需求增长被电价或检修截断，订单增长只形成应收，ETF 没买到目标环节
  applicable_asset_types: [resource_cycle_company, utility, operating_company, etf]
  linked_cases: []
  first_questions:
    - 这个资产的直接付款人是谁？
    - 单位利润和经营现金由哪个变量决定？
    - 当前盈利是否只是周期峰值或项目确认节奏？
  root_sources:
    - https://www.zijinmining.com/upload/file/2026/07/09/06b57b716de246f782abca6f4597a310.pdf
    - https://static.cninfo.com.cn/finalpage/2026-04-30/1225257689.PDF
    - https://www.gffunds.com.cn/funds/?fundcode=159611
    - https://www.chinaamc.com/fund/159326/index.shtml
  reused_targets_or_settled_cases: [601899, 601985, 159611, 159326]
```

## 资产映射

- 资源公司：[[03_STATE/HYPOTHESIS_QUEUE/CURRENT/601899]]
- 公用事业：[[03_STATE/HYPOTHESIS_QUEUE/CURRENT/601985]]
- ETF：[[03_STATE/HYPOTHESIS_QUEUE/CURRENT/159611]]、[[03_STATE/HYPOTHESIS_QUEUE/CURRENT/159326]]
- 跨领域经营公司：[[03_STATE/HYPOTHESIS_QUEUE/CURRENT/600487]]
- dated synthesis：[[05_EVIDENCE_META/EVIDENCE/THEMES/260726资源电力与电网_CurrentThesis重置证据]]
