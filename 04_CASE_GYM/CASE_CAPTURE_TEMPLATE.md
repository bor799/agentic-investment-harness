---
title: case_capture_template
date: 2026-07-23
updated: 2026-07-23
layer: CASE
primary_role: case_capture_template
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# Case Capture Template

```yaml
case_id:
case_type: trade | research | behavior | missed_opportunity | method_test
source:
date_opened:
date_closed:
pre_decision_context:
thesis_before_action:
action_or_non_action:
expected_result:
actual_result:
method_version:
evidence_used:
evidence_missing:
emotion_or_state:
what_changed:
what_would_have_proved_wrong:
lesson_type: observation | temporary_firewall | method_update | philosophy_candidate | no_increment
write_to:
```

## 规则

单个 Case 可以进入临时防火墙、研究问题或实验性 Skill 更新；不能直接写入 MINDSET / Constitution。
