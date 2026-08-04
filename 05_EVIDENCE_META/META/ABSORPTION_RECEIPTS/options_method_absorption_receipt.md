---
title: options_method_absorption_receipt
date: 2026-07-24
updated: 2026-07-24
layer: META
primary_role: absorption_receipt
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/期权基础.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/期权策略与认知演进总结.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/期权卖方统计学与Roll策略实战.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/波动率收割与期权量化策略体系.md
---

# Options Method Absorption Receipt

```yaml
new_information: 旧期权基础、卖方统计/Roll、波动率收割和认知演进四份方法源
change: revise
affected_item: 02_术/SKILLS/OPTIONS.md
result: METHOD_UPDATE
write_to: 02_术/SKILLS/OPTIONS.md
source:
  - 期权基础
  - 期权策略与认知演进总结
  - 期权卖方统计学与Roll策略实战
  - 波动率收割与期权量化策略体系
```

## 前台摘要

- **新东西是什么：**把 4 份旧期权方法全文纳入当前 `OPTIONS` Skill 的吸收范围。
- **改变了什么：**保留合约基础、Long option 正凸性、卖方负凸性、IV/Delta/DTE/Roll 诊断；退役“卖 Put 反脆弱”“Roll 走就好”“白赚权利金/咋都不亏”“固定 90/9/1 或 50 手授权”等表达。
- **写到哪里：**[[02_术/SKILLS/OPTIONS]]

## 边界

- 本回执不授权任何期权交易。
- 旧期权文档仍保留在 Review Queue 作为来源，但不再拥有当前方法权限。
- Roll 只作为事后补救或重新承保，不作为事前安全条件。
