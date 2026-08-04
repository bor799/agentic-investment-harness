---
title: 260709_tinci_unfilled_order_case
date: 2026-07-23
updated: 2026-07-23
layer: CASE
primary_role: trade_behavior_case
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 📈 个人交易手册.md#1. 天赐材料 002709.SZ — 2026-07-09 挂单（未成交）
---

# 天赐材料未追价 Case

```yaml
case_id: CASE-260709-TINCI
case_type: trade
source: "📈 个人交易手册.md#1. 天赐材料 002709.SZ — 2026-07-09 挂单（未成交）"
date_opened: 2026-07-09
date_closed: 2026-07-12
pre_decision_context: "左侧交易预案，限价 39.2 元，1,000 股，截至 2026-07-12 未成交。"
thesis_before_action: "事件跳变 + 周期利润修复，储能需求和电解液利润可能穿透。"
action_or_non_action: "按 39.2 元挂单，未因怕错过而抬价。"
expected_result: "若市场给到纪律价，获得观察权和事件窗口。"
actual_result: "未成交，市场没有给左侧机会。"
method_version: "旧储能/电解液交易框架"
evidence_used: "CNESA 招标、H1 利润预告、估值锚、承接规则。"
evidence_missing: "H1 正式毛利率、经营现金流、应收和存货、Q3 排产。"
emotion_or_state: "未持仓状态下能接受错过。"
what_changed: "未成交本身是信息；预案不等于持仓。"
what_would_have_proved_wrong: "若上调挂单价后仍有更好赔率和现金流证据，未追价可能过保守。"
lesson_type: observation
write_to: "04_CASE_GYM/METHOD_TESTS; 02_术/SKILLS/BEHAVIOR_REVIEW.md"
```

## 结论

这是一个正向过程样本：未持仓时，能让价格纪律阻止 FOMO。

## 边界

这只证明当次没有追价，不证明 `39.2` 元锚正确，也不恢复旧计划仓位。
