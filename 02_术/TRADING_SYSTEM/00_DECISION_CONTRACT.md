---
title: decision_contract
date: 2026-07-23
updated: 2026-07-23
layer: METHOD
primary_role: decision_contract
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: operational
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# 00 Decision Contract

## 先说人话

**今天发生了什么：**投资动作不再由长报告、评分表或 AI 共识直接推出，必须先通过同一份决策合同。

**为什么重要：**好故事、好公司、好价格和好情绪都可能只回答了一部分问题。增加风险前要知道自己到底在赚哪种钱，错了会损失什么。

**现在做什么：**任何结论只输出六档动作之一：`不投入 / 继续观察 / 建立验证仓 / 升级确认仓 / 不加仓 / 降级或退出`。

## 最小输入

- `business_horizon`：公司或行业变化的真实周期。
- `thesis_horizon`：这条 thesis 需要多久被验证。
- `execution_horizon`：本次动作打算承担多久的路径风险。
- `review_date`：下一次复查日期。
- `money_source`：赚基本面钱、流动性钱、风险偏好钱、认知差钱，还是事件跳变钱。
- `failure_condition`：什么事实说明我错了。

## 四票

| 票 | 中文名 | 问题 | 价格能否直接更新 | 权重 |
|---|---|---|---|---|
| `H_B` | **经营** | 公司是否真的更赚钱 | 不能 | 硬门 |
| `H_R` | **赔率** | 当前价格给的回报是否足够 | 可以 | 硬门 |
| `H_L` | **周期** | 持有期内（2 年/2 月/1 月）有哪些宏观微观风险 | 可以 | **软探测器（权重弱于其他三票）** |
| `H_C` | **仓位** | 错了是否能活下来 | 不能只靠价格 | 硬门 |

**硬门票**（经营 / 赔率 / 仓位）：任一失败或未知，默认不增加风险。

**周期票**（H_L）：是持有期内的宏观微观风险扫描器，起警示作用，权重弱于其他三票。失败时**不强制阻止动作**，但必须列出已知风险点、关键时间窗和复查日期；记录在案，由 Murphy 自行裁定是否行动。

## 决策输出模板

每次输出必须按这个顺序，不跳步：

```yaml
decision:
  action: 不投入 | 继续观察 | 建立验证仓 | 升级确认仓 | 不加仓 | 降级或退出
  money_source:
  business_horizon:
  thesis_horizon:
  execution_horizon:
  review_date:
  H_B:
  H_R:
  H_L:
  H_C:
  key_evidence:
  missing_evidence:
  failure_condition:
  do_not_do:
  write_to:
```

## 六档动作解释

| 动作 | 什么时候用 | 不代表什么 |
|---|---|---|
| `不投入` | 经营、赔率、周期或仓位有一项失败，或能力圈外无法复述 | 不代表标的一定差 |
| `继续观察` | 有研究价值，但关键证据缺失或 State 已过期 | 不代表可以无限拖延 |
| `建立验证仓` | 四票未失败，仍需小规模用真实反馈校准 | 不代表 thesis 已完全确认 |
| `升级确认仓` | 新增独立经营证据让经营票和赔率票同时改善 | 不代表可以忽略仓位票 |
| `不加仓` | 持有或关注中，但新增风险不合法 | 不代表必须卖出 |
| `降级或退出` | 失败条件、仓位超限、周期断裂或 thesis 被推翻 | 不代表事后一定不会卖飞 |

## 反方审查触发

出现这些词或状态，先走 [[02_术/SKILLS/BEHAVIOR_REVIEW]]：已经跌很多、错杀、回本、梭哈、怕错过、别人不懂、市场恐慌、卖 Put 降成本、AI 都同意、连续涨跌、大额浮盈亏、纪律触发。

## 吸收回执

新材料处理完必须留下三行：

- **新东西是什么：**
- **改变了什么：**
- **写到哪里：**

结果只能是 `METHOD_UPDATE / STATE_UPDATE / PHILOSOPHY_CANDIDATE / NO_INCREMENT`。
