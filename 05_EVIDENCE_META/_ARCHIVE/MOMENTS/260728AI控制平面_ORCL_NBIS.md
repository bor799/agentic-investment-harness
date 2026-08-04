---
moment:
  moment_id: MOM-260728-AI-CTRL-01
  state: absorbed
  trigger_source_ids:
    - SRC-260728-MURPHY-AI-CTRL-01
  affected_claim_ids:
    - AI-B01
    - AI-B02
    - AI-B03
    - AI-B04
    - ORCL-B01
    - ORCL-B02
    - ORCL-B03
    - NBIS-B01
    - NBIS-B02
    - NBIS-B03
  absorbed_to:
    - 05_EVIDENCE_META/KNOWLEDGE/DOMAINS/AI/README.md
    - 05_EVIDENCE_META/KNOWLEDGE/ENTITIES/COMPANIES/ORCL.md
    - 05_EVIDENCE_META/KNOWLEDGE/ENTITIES/COMPANIES/NBIS.md
    - 03_STATE/EXPECTATIONS/AI/
layer: MOMENT
primary_role: cognitive_diff
status: archived
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
---

# AI 控制平面 → Oracle / Nebius

## 触发材料

- [[05_EVIDENCE_META/SOURCES/2026/260728AI控制平面_Murphy讨论来源]]
- [[05_EVIDENCE_META/EVIDENCE/THEMES/260726AI基础设施_CurrentThesis重置证据]]
- [[05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/MIRRORED_SOURCES/分析报告/archive/260617AI算力连接与材料瓶颈_挖掘端框架_AI长报告原文]]

## 旧判断

领域认识、公司事实和带时效 thesis 混在 `03_STATE/DOMAIN_MODELS`；系统能记录“发生了什么”，但不能冻结“我们预期什么、为何更新、何时算错”。

## 新判断

稳定的领域/实体 working belief 进入 Knowledge；每次认知变化用唯一 `belief_update` 接口；带时间的预期进入 State 并冻结版本；结算后按错误类型进入 Case。

## 下一项验证

分别结算 Oracle 与 Nebius 的客户资金、容量利用率、利润/现金和融资来源；不能把 RPO、ARR、预付款、债务、股权或市场价格混成同一种“资金进入”。

## 吸收结果

`absorbed`。本 Moment 已进入 AI / ORCL / NBIS Knowledge 与两张 v1 Active Expectation，不留在前台。

