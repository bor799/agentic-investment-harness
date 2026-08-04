---
title: constitution_skills_absorption_receipt
date: 2026-07-24
updated: 2026-07-24
layer: META
primary_role: absorption_receipt
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/01_投资主框架.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/02_泊松供需闭环.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/03_流动性过滤器.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/04_行为纠偏系统.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/05_资本纪律.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/06_认知训练协议.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/交易宪法/skills/07_认知模型维护协议.md
---

# Constitution Skills Absorption Receipt

```yaml
new_information: 旧交易宪法 7 个 skill 的方法正文
change: revise
affected_item:
  - 02_术/TRADING_SYSTEM/01_RESEARCH_FLOW.md
  - 02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION.md
  - 02_术/TRADING_SYSTEM/03_FEEDBACK_LOOP.md
  - 02_术/TRADING_SYSTEM/PARAMETERS.md
  - 02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND.md
  - 02_术/SKILLS/LIQUIDITY_TRANSMISSION.md
  - 02_术/SKILLS/BEHAVIOR_REVIEW.md
  - 05_EVIDENCE_META/META/PROVENANCE_SCHEMA.md
  - 05_EVIDENCE_META/META/CLAIM_LEDGER.md
  - 05_EVIDENCE_META/META/CONFLICT_REGISTER.md
result: METHOD_UPDATE
write_to:
  - Trading System
  - Skills
  - Evidence Meta
```

## 前台摘要

- **新东西是什么：**把旧 Constitution 下 7 个 skill 从旧路径移交给新 canonical 体系。
- **为什么重要：**旧 Constitution 同时承担“道、术、治理、参数、AI 权限”，会让制度入口混杂；新体系要求 Constitution 只做 Guardrail + Router，具体方法进入 Trading System / Skills / Meta。
- **现在做什么：**以后调用当前方法时，以新 canonical 文件为准；旧 skill 保留在 Review Queue 作为来源，不再直接授权决策。

## 吸收映射

| 旧来源 | 写入 | 吸收内容 |
|---|---|---|
| `01_投资主框架.md` | `02_术/TRADING_SYSTEM/01_RESEARCH_FLOW.md` | 主分析链、三层股价、估值语法、四票、收益来源、工具匹配 |
| `02_泊松供需闭环.md` | `02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND.md` | 产业需求漏斗、供给锁死、财务变现、周期/存储闭环、事件时钟 |
| `03_流动性过滤器.md` | `02_术/SKILLS/LIQUIDITY_TRANSMISSION.md` | 四级水、四坐标、顺风/分化/逆风、蓄水池、约束转移、退出纪律 |
| `04_行为纠偏系统.md` | `02_术/SKILLS/BEHAVIOR_REVIEW.md` | 触发词、九问反方审查、24 小时冷静期、暴跌后流程、悬置容器、AI 防火墙 |
| `05_资本纪律.md` | `02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION.md`、`02_术/TRADING_SYSTEM/PARAMETERS.md` | 生活资金隔离、职责桶、四票承保、压力损失、工具边界、唯一主账、参数权限 |
| `06_认知训练协议.md` | `02_术/TRADING_SYSTEM/03_FEEDBACK_LOOP.md` | 日报写作、信息分层、决策冻结、三类反馈、卖飞复盘、模型更新接口 |
| `07_认知模型维护协议.md` | `05_EVIDENCE_META/META/PROVENANCE_SCHEMA.md`、`CLAIM_LEDGER.md`、`CONFLICT_REGISTER.md` | 来源身份、段落级定权、回源 P2、认知差分、AI 权限、静默覆盖禁令 |

## 明确降权或废止

- 政策、降息、ETF 流入、板块热度和价格变化不能更新 `H_B`。
- 未固定参考类、期限、结算规则和历史校准时，概率状态必须是 `uncalibrated`；固定 LR、固定加分、区间中点、主观单点概率不得进入 EV 或仓位。
- 旧仓位比例、旧金额桶、旧评分、旧固定升级计数和无 `R` 分母的计划仓位不授权新风险。
- 15 到 30 分钟观察、1.5% 到 2% 回升等盘面条件只允许重启研究，不能覆盖四票、冷静期和资本门。
- “降息等于股票增量”“热门板块等于业务强”“卖飞等于卖错”“Roll 走就好”“卖 Put 降成本”都被明确退役。
- 单次 Case、单篇文章、一天行情、一次盈亏和纯 AI 新框架不能修改 MINDSET 或 Murphy 人格。

## 边界

- 本回执不授权任何交易、仓位或参数修改。
- 旧 skill 仍作为来源保留；如未来发现遗漏，应追加到对应 canonical 文件并更新本回执。
- `merged` 只表示方法正文已经进入当前体系，不表示 Murphy 把全部内容确认为稳定哲学。
