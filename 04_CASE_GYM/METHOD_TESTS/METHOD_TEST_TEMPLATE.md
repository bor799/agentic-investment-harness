---
title: method_test_template
date: 2026-07-23
updated: 2026-07-23
layer: CASE
primary_role: method_test_template
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# Method Test Template

```yaml
method:
version:
reference_class:
sample:
prediction_or_rule:
time_horizon:
settlement_rule:
result:
false_positive:
false_negative:
changed_method:
rollback_needed:
```

没有参考类、期限和结算规则时，只能写 `uncalibrated`，不得输出单点概率。
