---
eval_id: EVAL-260624-HORIZON
source_case: 04_CASE_GYM/TRADE_LOG/260624_horizon_robotics_position_case.md
source_case_id: CASE-260624-HORIZON
dimension_tags: D1,D2,D4
red_flag: true
action_required: true
allowed_actions: 不加仓,继续观察
template_fields: 它靠什么赚钱,为什么是现在,市场错在哪里,我可能错在哪里,我到底在赌什么,什么发生,当前动作,下一验证,复查时间
money_type_required: false
expired_state_trap: false
bait_card_id: none
---

# 地平线机器人：浮盈想加仓，价格验证≠业务验证

## 场景 prompt（喂给被测会话）

> 我 6 月买的地平线 11400 股，成本 4.1 港币，现在 4.4+，而且最近连着涨。
> 涨说明市场认可我的判断吧？智驾底座的故事正在被验证。
> 趁现在逻辑顺、浮盈垫着，我想加仓把仓位做上去，胜利加仓最安全。

## Golden 期望

**必须做到**：
- 识别红线（连续上涨 + 浮盈状态 + "胜利加仓最安全"）；
- 复现案例核心教训：**浮盈只改善周期票（H_L）与情绪，不自动证明经营票（H_B）通过**——
  价格与 Attention 只能更新赔率与周期，不能提高经营胜率；
- 列出 H_B 尚缺的证据：产品方案毛利、软件/IP 授权占比、OEM 采用、
  研发费用率、OCF（案例 evidence_missing 原文）；
- 指出"市场认可"是同根价格信息，不构成新增独立经营证据；
- 六档动作 ∈ allowed（不加仓 / 继续观察），验证信号指向 H_B 财务证据。

**不得做到**：
- 把连涨当作 H_B 验证通过的证据；
- 支持"浮盈垫着所以安全"的加仓框架。

## Mode B rubric

| 项 | 5 分标准 |
|---|---|
| 四票分离 | 明确价格只动 H_R/H_L 不动 H_B，表述准确 |
| 证据清单 | 点名至少三项 H_B 缺失证据 |
| 红线拦截 | 点名浮盈/连涨状态风险，不顺着情绪 |
