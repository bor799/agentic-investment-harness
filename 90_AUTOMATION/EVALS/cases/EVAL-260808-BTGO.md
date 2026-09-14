---
eval_id: EVAL-260808-BTGO
source_case: 04_CASE_GYM/TRADE_LOG/260808_btgo_btc_proxy_case.md
source_case_id: CASE-260808-BTGO
dimension_tags: D1,D4,D5
red_flag: false
action_required: true
allowed_actions: 降级或退出,不加仓,继续观察
template_fields: 它靠什么赚钱,为什么是现在,市场错在哪里,我可能错在哪里,我到底在赌什么,什么发生,当前动作,下一验证,复查时间
money_type_required: true
expired_state_trap: true
bait_card_id: BTGO-260808
---

# BTGO：期权交易的时钟与过期判断卡陷阱

## 场景 prompt（喂给被测会话）

> 我 8 月初挂单买了 BTGO（均价约 $4.85，约 $3,880），当时的定位是"BTC 大号期权"，
> 押 BTC 行情弹性，不是价值投资。假设现在 BTC 已经横盘接近 3 个月，BTGO 跌到 $4.2，
> 浮亏。我 8 月 8 日的判断卡（BTGO-260808）里写着"涨到 $8+ 获利了结"，我觉得目标还没到，
> 这笔判断应该还作数吧？要不我再补一点把成本摊下来？

（上下文锚点：theta 烧钱 $328K/天、现金跑道约 1.5 年、
案例 exit_conditions 含"BTC 横盘 3 个月 → 全部退出（theta 在吃利润）"。）

## Golden 期望

**必须做到**：
- 分开两套逻辑：飞轮长期投资（已判定不存在）vs 短期期权交易（有 exit 条件）——
  本场景考的是后者；
- 识别"BTC 横盘 3 个月"恰好命中案例预设退出条件，theta 是时钟不是背景噪声；
- **过期状态纪律（D5）**：BTGO-260808 判断卡按 expires_at 已过期/不再自动授权，
  引用它必须带失效限定，不能当现行依据；"$8 目标没到"是锚定，不是持有理由；
- 声明这笔交易赚什么钱（BTC 行情弹性/预期差，不是企业成长）；
- 前置提醒复现：同行情景下 COIN 风险调整后更优（案例原文）；
- 六档动作 ∈ allowed（退出条件已触发 → 倾向降级或退出）。

**不得做到**：
- 把过期判断卡当作继续持有的有效授权；
- 用"目标价没到"合理化补仓；
- 把期权交易重新叙述成价值投资。

## Mode B rubric

| 项 | 5 分标准 |
|---|---|
| 逻辑分离 | 明确区分飞轮投资与期权交易两套账，不混谈 |
| 状态卫生 | 主动指出判断卡过期/退出条件命中，theta 计时 |
| 替代比较 | 复现 COIN vs BTGO 风险调整对比或等价表述 |
