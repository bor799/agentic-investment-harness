---
title: harness_dry_run_260725
date: 2026-07-25
updated: 2026-07-25
layer: AUTOMATION
primary_role: dry_run_log
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: operational
---

# Harness Dry Run 260725

四类真实样本试运行记录。全部 `write_intent: chat_only`，未修改任何正式投资文件。

样本来源：

- TARGET：`Coinbase`（dossier 存在）
- BATCH：`Coinbase / Cloudflare / Datadog`（dossier 均存在）
- CONTENT：仓库内 `归档/分析报告/260720投资框架_宏观流动性过滤器与认知退出纪律.md` 模拟外部内容输入
- CAPITAL：`Alibaba` 建仓假设（dossier 存在）

四类输入均预先确认：`03_STATE/HYPOTHESIS_QUEUE/CURRENT/` 目录不存在，因此所有标的 `state_status = legacy_only`。

---

## Dry Run 1：TARGET — Coinbase

### 用户输入

> Coinbase 当前值得继续观察还是已经可以建仓？

### 自动分诊结果

```yaml
harness_task:
  lane: JUDGE
  input_type: TARGET
  scope: single
  response_mode: concise
  process_depth: reviewed
  target_ids: [COIN]
  state_status: legacy_only
  write_intent: chat_only
  review_required: true
  loaded_skills: [COMPANY_FUNDAMENTALS, EXPECTATIONS_VALUATION, BEHAVIOR_REVIEW]
  reviewer_agent_mode: injected
```

`review_required: true` 触发依据：`AGENTS.md §4.1`"资本动作"——用户提到"建仓"。

### 用户实际看到的回答（concise）

```
一句话判断：Coinbase 当前 thesis 数据已过期，需要先刷新证据再讨论动作。
机会类型：流动性 + 风险偏好跳变 + 交易手续费（H_R 主导，H_B 不强）。
当前是否正在发生：未发生；只有 legacy_only dossier，无 CURRENT 卡。
最强支持证据：旧 dossier 显示交易手续费 + USDC 利息是核心收入来源，但字段已过期。
最大反方证据：监管不确定、稳定币竞争（Circle）、加密流动性依赖风险偏好。
关键 unknown：最新季度交易量、USDC 余额、Circle 份额、现货 ETF 资金流。
当前六档动作：继续观察（State 已过期，关键证据缺失）。
下一项验证信号：补齐最新季度交易量与 USDC 余额，刷新 data_cutoff。
```

### 是否触发 Reviewer

是。Reviewer 在 chat_only 下仍跑，但只输出 `review_result`，不写入。

### 期望行为

- 默认输出 ≤ 9 行；
- 不展示 dossier 加载过程；
- 不展示 Reviewer 全部检查；
- 不写文件。

### 实际偏差

- 偏差 D1-1：`AGENTS.md §4.1` 在 `chat_only + CAPITAL` 时仍然触发 Reviewer，但 Validator V-6 主要面向 `explicit_persist`。**chat_only 下 Reviewer 跑完后的 verdict 处理路径未明确**。需要 Validator 区分"写入门禁"和"判断门禁"。

### 需要加入 Validator 的检查

- V-11（新增提案）：当 `process_depth == reviewed` 且 `write_intent == chat_only` 时，Reviewer `verdict` 仅记录在对话中，不阻塞输出；只有 `explicit_persist` 才强制要求 `verdict == PASS` 才写入。

---

## Dry Run 2：BATCH — Coinbase / Cloudflare / Datadog

### 用户输入

> Coinbase、Cloudflare、Datadog 三个标的，从基本面和赔率看谁最值得继续研究？

### 自动分诊结果

```yaml
harness_task:
  lane: JUDGE
  input_type: BATCH
  scope: batch
  response_mode: concise
  process_depth: reviewed
  target_ids: [COIN, NET, DDOG]
  state_status: legacy_only   # 三个标的均为 legacy_only
  write_intent: chat_only
  review_required: true        # 批量比较产生投资优先级建议
  loaded_skills: [COMPANY_FUNDAMENTALS, EXPECTATIONS_VALUATION]
  reviewer_agent_mode: injected
```

### 用户实际看到的回答（concise）

```
三个标的都是 legacy_only 状态，下述排序只反映现有 dossier 的相对位置，不构成动作建议。

按继续研究优先级排序：

1. Cloudflare — 增长质量最稳，但估值最贵；H_R 票最弱。
2. Datadog — 平台化最清晰，但增长边际减速；H_B 边际下行风险。
3. Coinbase — 流动性依赖最强，监管不确定最大；H_L 软探测器警示。

关键催化：Cloudflare 待验证 R2 与 Workers 单价；Datadog 待验证 AI 工作负载占比；Coinbase 待验证 USDC 余额与 Circle 份额。

证据完整度：三者均缺失当前季度数据；都不允许直接形成 H_B 升级判断。

下一步研究优先级：先补 Cloudflare 与 Datadog 的最新季度财报证据；Coinbase 等待监管与流动性信号。
```

### 是否触发 Reviewer

是。批量比较直接产生优先级建议，硬触发。

### 期望行为

- 默认只展示 ≤ 5 个标的；
- 每个标的最多 2–3 行；
- 不为每个标的生成长报告。

### 实际偏差

- 偏差 D2-1：Harness Prompt 未规定"批量超过 5 个标的时如何截断"。**V-12（新增提案）：BATCH 输入超过 5 个标的时，Harness 必须按"当前确定性 + 证据完整度"过滤出前 5，其余以列表形式简短说明"暂不在主输出展开"。**
- 偏差 D2-2：所有标的 `state_status: legacy_only` 时，Harness 应输出极简回复（"全部需要先刷新 State，再讨论优先级"），不应展开三段比较。**V-13（新增提案）：当 BATCH 中 ≥ 50% 标的为 `missing` 或 `legacy_only` 时，Harness 必须先输出 State 缺失声明，再展开比较。**

### 需要加入 Validator 的检查

- V-12：BATCH 上限截断规则。
- V-13：BATCH 中 legacy_only / missing 比例阈值与对应输出约束。

---

## Dry Run 3：CONTENT — 流动性框架文章

### 用户输入

> 把 `归档/分析报告/260720投资框架_宏观流动性过滤器与认知退出纪律.md` 当作外部文章输入，看看有什么增量。

### 自动分诊结果

```yaml
harness_task:
  lane: REVIEW
  input_type: CONTENT
  scope: single
  response_mode: concise
  process_depth: reviewed
  target_ids: []
  state_status: legacy_only
  write_intent: chat_only
  review_required: true        # 拟产生 METHOD_UPDATE
  loaded_skills: [LIQUIDITY_TRANSMISSION, MACRO_REGIME]
  reviewer_agent_mode: injected
```

### 用户实际看到的回答（concise）

```
这份内容是否有增量：有。明确"四级水 + 四坐标"的认知退出框架。
哪些事实成立：本文是方法论文献，不陈述新事实；引用的政策/市场/板块/标的信号是模型分类。
哪些属于推断或叙事：四级水的逐级传导是经验模型，不能反推每次必然传导。
最重要的新机制：政策水 → 市场水 → 板块水 → 标的水，必须逐级验收。
改变了哪个判断：未改变具体标的判断；强化了"价格和 Attention 只更新 H_R/H_L，不能直接抬高 H_B"。
不能证明什么：四级水的有效性是经验规则；不能证明任何具体标的的下一段必然兑现。
下一步验证什么：在具体历史标的上回测"四级水都打通 → 标的水"的命中频率。

absorption: NEW_MECHANISM（拟形成 proposal；本轮不直接落盘，等 Murphy 决策）。
```

### 是否触发 Reviewer

是。拟产生方法更新，硬触发。

### 期望行为

- 不把内容直接写成方法正文；
- 不复制原文到 `02_术/SKILLS/`；
- 仅在对话形成 proposal。

### 实际偏差

- 偏差 D3-1：内容来源来自仓库内部（`归档/`），不是严格意义"外部"。**Harness 应明确：仓库内 legacy 报告作为内容输入时，source_traceability 应标记 `internal_legacy`，并避免把它当成"独立第三方来源"计入证据。V-14（新增提案）。**

### 需要加入 Validator 的检查

- V-14：内容来源分类（`external_publish` / `internal_legacy` / `user_thesis`）；同根信息只计一次。

---

## Dry Run 4：CAPITAL — Alibaba 建仓

### 用户输入

> 如果我现在想对 Alibaba 建仓 5%，应该走哪些验证步骤？

### 自动分诊结果

```yaml
harness_task:
  lane: JUDGE
  input_type: CAPITAL
  scope: single
  response_mode: concise
  process_depth: reviewed
  target_ids: [BABA]
  state_status: legacy_only
  write_intent: chat_only
  review_required: true        # 资本动作 + 用户给出仓位参数
  loaded_skills: [COMPANY_FUNDAMENTALS, EXPECTATIONS_VALUATION, BEHAVIOR_REVIEW]
  reviewer_agent_mode: injected
```

### 用户实际看到的回答（concise）

```
一句话判断：Alibaba 当前 thesis 数据已过期；想建仓必须先重建证据链，本轮不进入动作讨论。
机会类型：基本面反转 + 估值修复（H_B/H_R 主导）。
当前是否正在发生：legacy_only，无 CURRENT 卡；既有 dossier 字段已 superseded。
最强支持证据：旧 dossier 显示电商 + 云 + 蚂蚁三条腿，但字段已过期，不能直接用。
最大反方证据：电商竞争、监管不确定、云业务增速不确定、股东回报路径未明确。
关键 unknown：最新季度云业务增速、蚂蚁治理与 IPO 进度、电商市场份额、港股通资金流。
当前六档动作：不投入（证据不足 + State missing）。
下一项验证信号：刷新最近两个季度财报 → 重建 H_B → 再讨论 H_R 是否给到足够赔率。

行为纠偏：用户给出具体仓位（5%）属于新增风险意图，按 AGENTS.md §8 默认冻结新增风险 24 小时；本轮只输出验证清单，不讨论参数。
```

### 是否触发 Reviewer

是。资本动作 + 仓位参数，硬触发。

### 期望行为

- 不在 chat_only 下输出仓位建议；
- 触发 24 小时新增风险冻结（亏损后/想加仓语境）；
- 引导用户先刷新 State。

### 实际偏差

- 偏差 D4-1：用户给出具体仓位参数（"5%"），Harness 必须识别为"仓位参数意图"并触发 `BEHAVIOR_REVIEW`。**当前 Harness Prompt 未明确仓位参数识别规则。V-15（新增提案）：用户输入出现百分比仓位、金额、"梭哈"、"满仓"、"加 X 仓"等表达时，Harness 必须自动触发 BEHAVIOR_REVIEW 与 24 小时新增风险冻结提示。**
- 偏差 D4-2：chat_only 下 `六档动作 = 不投入`，但 Reviewer 在背景仍跑。**Reviewer 输出 `allowed_write_route` 应在 `chat_only` 时强制留空，避免被误解为"可写入路径"。**（与 D1-1 同源）

### 需要加入 Validator 的检查

- V-15：仓位参数识别 + 自动触发 BEHAVIOR_REVIEW 与新增风险冻结提示。
- V-11（同 D1-1）：chat_only 下 Reviewer `allowed_write_route` 必须留空。

---

## 总观察：偏差汇总

| ID | 偏差 | 加入 Validator |
|---|---|---|
| D1-1 | chat_only + CAPITAL 下 Reviewer 处理路径未明确 | V-11 |
| D2-1 | BATCH 超过 5 个标的时的截断规则未定义 | V-12 |
| D2-2 | BATCH 全 legacy_only / missing 时的极简回复规则未定义 | V-13 |
| D3-1 | 仓库内 legacy 报告作为内容输入的来源分类未定义 | V-14 |
| D4-1 | 用户仓位参数识别 + BEHAVIOR_REVIEW 自动触发未定义 | V-15 |

## 关键正反馈

- `state_status: legacy_only` 在四次试运行中都正确阻止了"直接复用旧报告作为当前判断"——Validator V-2 起作用。
- 四次首回答都控制在 9–13 行，符合 concise 原则。
- 没有出现"维持甚至加仓""谨慎乐观"等模糊动作表达——四票硬门起作用。
- 没有错误写入任何文件（chat_only 默认生效）。

## 未在本轮覆盖的真实样本

- "FILING" 单独类型（财报原文、招股书原文、监管公告原文）：本轮用 CONTENT 替代，因为仓库内已有的"外部文章"是方法报告，不是 FILING。如 Murphy 提供具体财报链接，可补一次 FILING dry-run。
- `write_intent: explicit_persist` 全流程：本轮全程 chat_only，Validator 写入门禁未走完闭环。建议下一轮由 Murphy 主动触发一次 explicit_persist 写入。

## 后续动作

- 把 V-11 到 V-15 写入 `90_AUTOMATION/PIPELINES/validate_investment_output.py`（T5）。
- 在 T6 README 中明确 `legacy_only` 与 `current` 的转换条件，避免"自动批量回填历史 dossier"。
