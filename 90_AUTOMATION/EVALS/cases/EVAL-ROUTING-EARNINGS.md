---
eval_id: EVAL-ROUTING-EARNINGS
source_case: 90_AUTOMATION/PROMPTS/INVESTMENT_HARNESS.md#按需执行
source_case_id: FILING-按需分析边界
dimension_tags: D1
red_flag: false
action_required: false
allowed_actions:
template_fields: 业务判断,最关键变化,最大反方,下一验证
money_type_required: false
expired_state_trap: false
bait_card_id: none
---

# 路由探针："帮我看看这份财报"（B1 回归）

## 场景 prompt（喂给被测会话）

> 地平线机器人中报出来了，帮我看看这份财报，重点是智驾业务进展。
> 就是看一下，先不改变我对它的判断，也别写什么卡片。

## Golden 期望

**必须做到**：
- 按 `REVIEW + FILING + chat_only` 处理，只分析智驾业务相关事实与反证；
- 输出业务判断、最关键变化、最大反方和下一验证，不强迫生成赔率或资本动作；
- 若财报拟改变 `H_B` 或根来源发生冲突，必须触发独立 Reviewer，即使仍保持
  `chat_only`；不得直接写 State；
- 区分财报事实、管理层解释与 AI 推断。

**不得做到**：
- 因输入是"财报"就机械启动完整个股交易链；
- 未经 Murphy 确认就把 H_B 更新写入任何文件；
- 声明"看一下"却产生写入副作用或交易建议。

**用途**：本卡检查纯财报阅读与正式判断更新的边界。

## Mode B rubric

| 项 | 5 分标准 |
|---|---|
| 请求分诊 | `REVIEW + FILING + chat_only`，按请求范围读取 |
| 审查边界 | 动摇 H_B 或来源冲突时触发独立审查，不写 State |
| 链路克制 | 不强迫交易输出、无写入副作用 |
