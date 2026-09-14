---
title: run_modes
date: 2026-08-05
updated: 2026-09-13
layer: METHOD
primary_role: run_modes
status: retired
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: historical_only
source_paths:
  - 90_AUTOMATION/PROMPTS/INVESTMENT_HARNESS.md
  - 02_术/TRADING_SYSTEM/01_RESEARCH_FLOW.md
  - 02_术/TRADING_SYSTEM/00_DECISION_CONTRACT.md
---

# 04 Run Modes

> **退役声明（2026-09-13）：**本文件保留为历史设计记录，不再参与当前加载、
> 路由、Reviewer 或 Validator 判断。当前按需执行、差分更新与停止条件唯一见
> `90_AUTOMATION/PROMPTS/INVESTMENT_HARNESS.md`；Reviewer 硬触发仍唯一见
> `AGENTS.md §4.1`。下文不再拥有当前操作权。

## 职责

定义三种运行模式，控制 [[01_RESEARCH_FLOW|方法论]] 的运行深度和
[[00_DECISION_CONTRACT|四票硬门]] 的 gating 时机。不替代它们。

## 模式选择原则

**运行模式由本次行为准备产生的副作用决定，不由研究主题、信息类型或文件名称决定。**

- "研究财报"本身不进入 PROMOTE；"用财报正式改变 H_B State"才进入 PROMOTE。
- "阅读外部材料"本身不进入 STAGE；"准备把外部材料转成候选 State 更新"才进入 STAGE。
- §4.1 触发 7（根来源冲突）和 8（无法说明市场可能正确）在 EXPLORE 中生效——
  但只表现为必须提示冲突或补反证，不强制升级模式或调用正式 Reviewer。

## 三种模式

| 模式 | 触发（副作用意图） | write_intent | 写入范围 | Reviewer | Validator |
|---|---|---|---|---|---|
| **EXPLORE** | 默认；未准备写入 | chat_only | 零 | 内部自检（见下） | 不调用 |
| **STAGE** | 准备生成候选卡 / shadow-test / 待审提案 | automation_stage | 仅 STAGING/ exclusive-create | 正式调用（若拟晋升） | 不要求完整 canonical Validator；若现有工具无法选择规则子集，保留为待实现能力 |
| **PROMOTE** | 准备写入 canonical / 资本动作 / 方法变更 | explicit_persist | canonical sink + 备份 + 回执 | 12 检查 MUST PASS | 全部 |

## EXPLORE 9 步协议

```text
1. 赚什么钱     从 6 类选主要 + 次要 + 明确不依赖（return_account 作为第一锚定）
2. 核心命题     一句话最强版本复述：市场可能错在哪个因果环节
3. 必要假设     拆 3-5 个缺一不可的假设（每个：是什么 / 为什么必要 / 失效条件）
4. 第一关键未知 指定唯一的、解决后能改变假设的那个问题
5. 最小搜索     只找能改变假设的根来源（财报 / 电话会 / 客户 / 监管 / 价格产能）
6. 集中反证     市场为什么可能正确 / 最强替代解释 / 最接近的失败类比
7. 更新而非重写 若已有 Current 或 Knowledge——只报告 delta
8. 自检         R-checks 内部执行（见下）
9. 输出         对话式；不生成卡片或文件
```

方法论 ([[01_RESEARCH_FLOW]]) 在 EXPLORE 中只取必要链环（赚什么钱 → 假设 → 未知 → 证据 → 反证），
不走完整宏观 → 产业 → 公司 → 估值全链。四票 ([[00_DECISION_CONTRACT]]) 作为思考框架（"大概什么状态"），
不作为硬门 gating。

## EXPLORE 自检（R-checks）

以下检查在内部执行。**只呈现未通过、不确定或决策相关的项；不逐项汇报。**

- 事实与推断分开了吗？
- 有至少一个替代解释吗？
- 能说出"市场为什么可能正确"吗？
- 来源可追溯到根来源吗？
- 因果链最脆弱的箭头在哪？
- 赔率校准诚实吗（calibrated / uncalibrated）？
- 第一关键未知解决后改变哪个假设？
- 产生了决策增量吗（还是同根重复）？

**自检 ≠ Reviewer 正式调用。** 不产生 verdict、不产生 `last_reviewer`、不写入任何文件。

## 停止条件

满足任一即停止搜索：

- 第一关键未知解决且不改变任何假设
- 新增来源只是重复同一根来源
- 新增内容只增加叙事丰富度，不增加决策信息
- 关键问题只能等待新财报 / 事件 / Murphy 信息

## §4.1 硬触发 → 模式映射

| §4.1 触发 | EXPLORE | STAGE | PROMOTE |
|---|---|---|---|
| 1. `explicit_persist` | — | — | ✅ |
| 2. 路径在 01_道 / 02_术 / 03_STATE | — | — | ✅ |
| 3. 资本动作 | — | — | ✅ |
| 4. 财报拟改变 H_B | — | — | ✅ |
| 5. 外部材料拟产生 State 更新 | — | ✅ | ✅ |
| 6. 哲学候选 / 方法提案 | — | ✅ | ✅ |
| 7. 根来源冲突 | ✅ | ✅ | ✅ |
| 8. 无法说明"市场可能正确" | ✅ | ✅ | ✅ |
| 9. 批量比较产生优先级 | — | ✅ | ✅ |

触发 7/8 在 EXPLORE 中以"提示冲突 / 补反证"形式生效，不升级模式。

## 与现有文件的关系

| 文件 | 在 RUN_MODES 下的角色 |
|---|---|
| [[01_RESEARCH_FLOW]] 方法论 | 所有模式使用；EXPLORE 只取必要链环 |
| [[00_DECISION_CONTRACT]] 四票 | EXPLORE = 思考框架；PROMOTE = 硬门 gating |
| [[90_AUTOMATION/PROMPTS/INVESTMENT_HARNESS\|Harness 17 步]] | PROMOTE 完整路径；EXPLORE 用 9 步替代 |
| [[90_AUTOMATION/PROMPTS/INVESTMENT_REVIEWER\|Reviewer 12 检查]] | EXPLORE 提取 R-checks 自检；PROMOTE 正式调用 |

## 不能证明什么 / 失败条件

- EXPLORE 输出不是正式判断、不是 Current 卡、不是交易授权。
- EXPLORE 自检不等于 Reviewer PASS。
- 选择 EXPLORE 不绕过 §4.1 任何硬触发。
- 不能用 EXPLORE 假装完成正式研究后直接写入。
