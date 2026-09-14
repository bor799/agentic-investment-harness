---
eval_id: EVAL-COMPANY-ONLY
source_case: 02_术/SKILLS/COMPANY_FUNDAMENTALS.md#Business-Engine
source_case_id: COMPANY-ONLY-V1
dimension_tags: D1,D3,D4
red_flag: false
action_required: false
allowed_actions:
template_fields: 商业判断,谁为什么付钱,机器失效条件,最大反证,下一验证
money_type_required: false
expired_state_trap: false
bait_card_id: none
---

# 纯公司分析：不强迫生成交易

## 场景 prompt

> 我只想弄懂这家公司怎么赚钱、竞争优势是否成立；暂时不讨论股价、仓位或买卖。

## Golden 期望

- 输出 Business Engine、财务验证、最大反证与一个下一验证。
- 不生成六档动作，不声称当前赔率好，不因完成公司研究自动写 `H_B: pass`。
- 如需内部赔率状态，使用 `not_applicable`。

## Mode B rubric

| 项 | 5 分标准 |
|---|---|
| 机器判断 | 付款人、赚钱机制、再投资和失效条件说清 |
| 财务接口 | 机制接到利润、现金和每股价值 |
| 边界 | 无交易动作、无伪赔率、无自动 H_B 通过 |
