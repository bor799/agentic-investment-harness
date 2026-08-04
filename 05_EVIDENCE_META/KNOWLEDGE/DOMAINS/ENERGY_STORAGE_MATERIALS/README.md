---
knowledge:
  knowledge_id: DOMAIN-ENERGY-STORAGE-MATERIALS
  knowledge_type: domain_pattern_map
  domain_id: ENERGY_STORAGE_MATERIALS
  qualified_pattern_ids: []
  candidate_pattern_ids: [ESM-C01]
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

# 储能材料领域判断地图

## 60 秒入口

当前没有通过双根来源与跨标的复用门槛的合格模式。

```yaml
structural_fit: unknown
evidence_status: uncalibrated
qualified_patterns: []
counter_pattern: 终端需求和排产增长可能只形成低毛利扩量
first_questions:
  - 销量、价差、单吨利润和经营现金是否共同改善？
  - 认证、一体化或配方优势能否留下利润？
  - 供给扩张多久会反噬当前紧平衡？
next_step: proceed_to_verify
```

## 候选模式

### ESM-C01｜物理需求线性，利润兑现非线性

候选因果链：

```text
储能/动力需求
→ 材料出货与利用率
→ 售价减原料及制造成本的价差
→ 单吨利润
→ 应收、存货与经营现金
```

当前只在天赐材料及其历史研究中反复出现，尚未取得第二个独立标的或已结算
Case，因此不进入合格模式。

## 资产与 Case

- Current：[[03_STATE/HYPOTHESIS_QUEUE/CURRENT/002709]]
- Case：[[04_CASE_GYM/TRADE_LOG/260709_tinci_unfilled_order_case]]
- Murphy 基线：[[05_EVIDENCE_META/EVIDENCE/THEMES/260727系统_Murphy判断驱动Harness基线]]

## 反模式

- 满产不等于高单吨利润；
- 龙头份额不等于定价权；
- 利润增长但应收、存货和现金恶化，不构成闭环。
