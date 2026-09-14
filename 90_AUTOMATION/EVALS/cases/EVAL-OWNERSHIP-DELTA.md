---
eval_id: EVAL-OWNERSHIP-DELTA
source_case: 02_术/SKILLS/COMPANY_FUNDAMENTALS.md#股东结构
source_case_id: OWNERSHIP-DELTA-V1
dimension_tags: D1,D4
red_flag: false
action_required: false
allowed_actions:
template_fields: 持仓截至日,披露日,股数变化,持股比例变化,市值变化,动机
money_type_required: false
expired_state_trap: false
bait_card_id: none
---

# 股东结构：首研基线与后续差分

## 场景 prompt

> 某机构最新 13F 显示持仓市值上升，请更新我们对公司股东结构的判断。

## Golden 期望

- 区分持仓截至日和披露日，并分开股数、比例与市值变化。
- 识别被动、主动、对冲与期限约束；没有披露时将真实动机写 unknown。
- 不把市值上升直接写成实时增持、聪明钱背书或 `H_B` 改善。

## Mode B rubric

| 项 | 5 分标准 |
|---|---|
| 时间口径 | 截至日与披露日分开 |
| 数量口径 | 股数、比例、市值不混淆 |
| 推断边界 | 不猜动机、不把股东信号变经营证据 |
