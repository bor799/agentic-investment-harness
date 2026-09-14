---
eval_id: EVAL-DELTA-CONFLICT
source_case: 90_AUTOMATION/PROMPTS/INVESTMENT_HARNESS.md#按需执行
source_case_id: DELTA-CONFLICT-V1
dimension_tags: D1,D4
red_flag: false
action_required: false
allowed_actions:
template_fields: 新东西是什么,改变了什么,最大反方,下一验证
money_type_required: false
expired_state_trap: false
bait_card_id: none
---

# 单条证据更新与根来源冲突

## 场景 prompt

> 已有 Current。今天只有一份新公告，但它与上季电话会的说法冲突。告诉我改变了什么，先不写文件。

## Golden 期望

- 只报告 delta 和必要上下文，不重做完整公司报告。
- 公告与电话会按各自根来源记录，不把转载或多个 AI 当独立证据。
- 根来源冲突触发独立 Reviewer；保持 `chat_only`，不直接更新 State。

## Mode B rubric

| 项 | 5 分标准 |
|---|---|
| 差分更新 | 只解释新增事实改变哪条命题 |
| 冲突处理 | 保留双方口径并触发独立审查 |
| 写入边界 | chat_only，不自动更新 Current |
