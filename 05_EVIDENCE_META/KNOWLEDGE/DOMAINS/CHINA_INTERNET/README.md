---
knowledge:
  knowledge_id: DOMAIN-CHINA-INTERNET
  knowledge_type: domain_pattern_map
  domain_id: CHINA_INTERNET
  qualified_pattern_ids: [CI-P01]
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

# 中国互联网领域判断地图

## 60 秒入口

- 合格模式：`CI-P01`
- 首要反模式：把两只不同指数、不同包装的 ETF 当成同一产品比较折价或涨跌。
- 第一问题：产品究竟买到哪些平台、以什么权重和包装？

## 合格模式

### CI-P01｜先穿透产品，再判断行业

```yaml
qualified_pattern:
  pattern_id: CI-P01
  recognition_cues:
    - 同一主题存在多个 ETF 或包装层
    - 用户用折溢价、回撤或单一事件判断机会
  causal_chain: 平台经营改善 → 成分盈利与现金流形成广度 → 指数权重承接 → 费用、跟踪与折溢价后成为持有人回报
  payer_and_money_path: 消费者、商家和企业客户向平台付费，利润经回购或每股现金进入指数
  profit_control: 指数编制、权重集中、包装结构、加权盈利、费用与跟踪质量
  favorable_fit: 产品准确覆盖目标平台，前十大盈利与自由现金同步改善，包装与估值未吞噬收益
  counterpattern_and_falsifier: 指数或包装不匹配，盈利只集中于少数权重，折价只是 T-1 净值错位
  applicable_asset_types: [etf]
  linked_cases: []
  first_questions:
    - 跟踪什么指数，前十大是谁？
    - 加权盈利和自由现金是否有广度？
    - 是否存在 ETF-of-ETF、跟踪或折溢价尾部风险？
  root_sources:
    - https://www.efunds.com.cn/fund/513050.shtml
    - https://www.chinaamc.com/fund/513130/index.shtml
    - https://www.sse.com.cn/disclosure/fund/announcement/c/new/2026-04-22/513130_20260422_C8GF.pdf
  reused_targets_or_settled_cases: [513050, 513130]
```

## 资产与 State

- [[03_STATE/HYPOTHESIS_QUEUE/CURRENT/513050]]
- [[03_STATE/HYPOTHESIS_QUEUE/CURRENT/513130]]
- dated synthesis：[[05_EVIDENCE_META/EVIDENCE/THEMES/260726中国互联网平台_CurrentThesis重置证据]]

## 边界

本图只能回答“产品是否表达正确”；当前估值、资金和动作仍必须读取 Current。
