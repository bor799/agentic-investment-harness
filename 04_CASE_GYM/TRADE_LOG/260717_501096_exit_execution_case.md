---
title: 260717_501096_exit_execution_case
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
  - 📈 个人交易手册.md#0.7 501096 操作复盘 — 2026-07-17
---

# 501096 退出执行未闭环 Case

```yaml
case_id: CASE-260717-501096
case_type: trade
source: "📈 个人交易手册.md#0.7 501096 操作复盘 — 2026-07-17"
date_opened: 2026-07-17
date_closed:
pre_decision_context: "连续急跌后持有 23,800 份，成本约 1.85 元，收盘 1.585 元。"
thesis_before_action: "可能反弹，但买入前缺独立理由、企稳证据和失败条件。"
action_or_non_action: "尝试在约 1.75 / 1.70 / 1.65 / 1.60 卖出，但成交状态未确认。"
expected_result: "降低风险或等待更好反弹价。"
actual_result: "主账暂按未卖出，必须核对券商委托、成交、撤单、废单。"
method_version: "旧个人交易手册 + 当前行为/资本纪律"
evidence_used: "腾讯行情、基金公告、本人委托口述。"
evidence_missing: "券商成交回报、每笔委托时间、数量、状态、均价。"
emotion_or_state: "成本锚、回本愿望、连续急跌后的风险压力。"
what_changed: "退出意图与委托方式必须分开；主账只认券商回报。"
what_would_have_proved_wrong: "若买入前已有企稳、承接、折溢价和成交量恢复记录，左侧乱接刀判断需重审。"
lesson_type: temporary_firewall
write_to: "02_术/SKILLS/BEHAVIOR_REVIEW.md; 02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION.md"
```

## 结论

这不是长期人格证明，而是一个流程漏洞样本：买入前独立陈述不足，触发风险线后，执行退出单和等待反弹单混在一起。

## 可立即改的术

- 下单前必须写买入理由、三个验证数字、失败条件、仓位角色和为什么是现在。
- 执行退出单必须检查 `已报 / 部成 / 已成 / 已撤 / 废单`。
- AI 只能提供证据、反证、情景和风险线，不能给交易授权。

## 不得改的道

单个 501096 Case 不得自动新增 MINDSET 原则，也不得把“亏损后纪律弱”写成 Murphy 稳定人格。
