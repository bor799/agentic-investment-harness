# 运行入口

| 入口 | 何时读取 |
|---|---|
| [INVESTMENT_HARNESS](INVESTMENT_HARNESS.md) | 企业、行业、市场与材料判断；默认简洁输出 |
| [INVESTMENT_REVIEWER](INVESTMENT_REVIEWER.md) | 命中 AGENTS 的审查条件时，交给独立只读 Reviewer |
| [AI_BELIEF_LOOP](AI_BELIEF_LOOP.md) | 隔离候选 runner；不代替研究核验 |

加载顺序与权限以 [AGENTS](../../AGENTS.md) 为准；不另建模型专用提示词副本。

历史检索按需打开：[旧周期索引](AI_CYCLE_PROMPTS_INDEX.md)、
[待复核队列](AUTOMATION_REVIEW_QUEUE_INDEX.md)、[未核验候选](CURRENT_CANDIDATES_INDEX.md)。
这些索引不是当前运行入口，也不自动授权写入。
