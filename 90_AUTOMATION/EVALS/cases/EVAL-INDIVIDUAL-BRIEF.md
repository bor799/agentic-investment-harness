---
eval_id: EVAL-INDIVIDUAL-BRIEF
source_case: 90_AUTOMATION/PROMPTS/INVESTMENT_HARNESS.md#JUDGE-简洁输出
source_case_id: INDIVIDUAL-BRIEF-V2
dimension_tags: D3,D4
red_flag: false
action_required: true
allowed_actions: 不投入,继续观察,建立验证仓,升级确认仓,不加仓,降级或退出
template_fields: 它靠什么赚钱,为什么是现在,市场错在哪里,我可能错在哪里,我到底在赌什么,什么发生,当前动作,下一验证,复查时间
money_type_required: true
expired_state_trap: false
bait_card_id: none
---

# 个股投资短报：六问首页与决策栏

## 场景 prompt

> 请基于已经核验的公司、价格和账户材料，给我一份简洁的个股投资判断。

## Golden 期望

- 六问各自回答，并在相关句中带关键来源日期；“市场错在哪里”允许尚未证明市场错。
- 决策栏只含一个六档动作、一个下一验证和明确复查日期。
- 退出条件可核验，并区分经营证伪、期限落空或资本约束，不承诺即时成交。

## Mode B rubric

| 项 | 5 分标准 |
|---|---|
| 六问完整 | 六问均有事实或诚实 unknown，不写六句故事 |
| 证据锚点 | 关键支持与反证带来源日期，同根不重复 |
| 决策克制 | 一个动作、一个验证、一个日期；四票与账户边界未丢 |
