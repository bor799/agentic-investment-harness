---
knowledge:
  knowledge_id: DOMAIN-INNOVATIVE-DRUGS
  knowledge_type: domain_pattern_map
  domain_id: INNOVATIVE_DRUGS
  qualified_pattern_ids: []
  candidate_pattern_ids: [ID-C01]
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

# 创新药领域判断地图

## 60 秒入口

当前没有合格模式，必须返回 `unknown` 并继续验证：

```yaml
structural_fit: unknown
evidence_status: uncalibrated
qualified_patterns: []
counter_pattern: 许可合同总额是上限，不是已确认收入或现金
first_questions:
  - 首付款、里程碑和销售现金何时确认？
  - 管线失败与融资会如何影响成分公司？
  - ETF 是否真正覆盖目标管线并控制集中度？
next_step: proceed_to_verify
```

## 候选模式

### ID-C01｜许可 headline 必须转成现金与管线价值

目前只有一只 Current ETF，缺第二个可复用标的或已结算 Case，因此不进入
60 秒前台。

候选链条：

```text
临床与许可
→ 首付款和里程碑
→ 商业销售与毛利
→ 研发现金消耗下降
→ 每股价值改善
```

## 资产与来源

- [[03_STATE/HYPOTHESIS_QUEUE/CURRENT/513120]]
- dated synthesis：[[05_EVIDENCE_META/EVIDENCE/THEMES/260726创新药_CurrentThesis重置证据]]
- 基金入口：https://www.gffunds.com.cn/funds/?fundcode=513120
- 政策入口：https://www.nhsa.gov.cn/
