---
title: hypothesis_queue
date: 2026-07-23
updated: 2026-07-25
layer: STATE
primary_role: hypothesis_queue
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 90_AUTOMATION/DESIGN_NOTES/LEGACY_AUTOMATION_INVENTORY.md
data_cutoff:
expires_at:
---

# Hypothesis Queue

保存公司问题、下一信号、待研究假设。问题队列会过期，不能冒充公司长期结论。

## 入口

| 入口 | 用途 |
|---|---|
| [[03_STATE/HYPOTHESIS_QUEUE/COMPANY_QUESTIONS_INDEX]] | 公司 `research_task`、`next_questions`、`next_signals` |
| [[03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE_INDEX]] | 已镜像入新结构的旧问题队列原文 |
| [[03_STATE/HYPOTHESIS_QUEUE/CURRENT]] | current thesis 状态卡（按需创建） |

所有条目必须有 `data_cutoff`、`expires_at` 或明确 `refresh_trigger`。过期后只能作为历史 State，不能继续当当前证据。

---

## CURRENT 状态卡规则（T6）

current thesis 状态卡仅在以下情况下按需创建：

1. Murphy 在对话中**明确要求**持续跟踪某标的；
2. Murphy **明确要求**写入投资系统（`write_intent: explicit_persist`）；
3. `reviewed` 任务通过且 `verdict == PASS`，主 Agent 与 Reviewer 一致；
4. 已存在 current 卡，需要更新有效状态（例如新季度财报刷新 `data_cutoff`、`H_B`、`H_R`、`key_evidence`）。

### 禁止

- **禁止**批量回填历史 dossier 为 current 卡；
- **禁止**自动把旧报告 / `MIRRORED_LEGACY_STATE` / `归档/分析报告/` 内容转换为 current；
- **禁止**因一次普通问答创建状态卡（普通问答默认 `write_intent: chat_only`，不落盘）；
- **禁止**在 `state_status: legacy_only` 或 `missing` 时跳过 Reviewer 直接写 current 卡。

### 路径

```
03_STATE/HYPOTHESIS_QUEUE/CURRENT/<target_id>.md
```

`<target_id>` 使用统一规范：

- 美股 ticker：大写（如 `COIN.md`、`BABA.md`、`NVDA.md`）；
- 港股代码：5 位数字（如 `09988.md`）；
- A 股代码：6 位数字（如 `600519.md`）；
- 私募 / 未上市：公司英文名小写下划线（如 `figure_technology.md`）。

文件名只承担 ID；公司名、行业、币种等放在正文。

### 状态卡契约

```yaml
current_thesis_state:
  target_id:               # 与文件名一致
  data_cutoff:             # YYYY-MM-DD，证据最新截止
  expires_at:              # YYYY-MM-DD，本卡失效日（一般 data_cutoff + 90 天，季报后刷新）
  review_date:             # YYYY-MM-DD，下次复查日（一般 data_cutoff + 30 天）
  money_source:            # 基本面 | 流动性 | 风险偏好 | 认知差 | 事件跳变
  H_B:                     # 经营票：pass | fail | unknown + 一句话原因
  H_R:                     # 赔率票：pass | fail | unknown + 一句话原因
  H_L:                     # 周期票（软探测器）：pass | fail | warn + 关键风险点
  H_C:                     # 仓位票：pass | fail | unknown + 已定义最大损失说明
  key_evidence:            # 3–7 条；每条带根来源路径
  missing_evidence:        # 关键 unknown；下一段必须补的证据
  failure_condition:       # 什么事实说明 thesis 错了
  allowed_action:          # 条件式（见下方规则）
  open_disagreement:       # Reviewer DISAGREE 时保留；否则 none
  source_paths:            # 本卡写入时调用的根来源
  last_reviewer:           # 最近一次 Reviewer verdict + agent_mode + 时间
```

### `allowed_action` 必须写成条件式

合法形式：

```
若 <X 信号> 得到验证且 <Y 风险> 未恶化，则允许 <六档动作之一>。
```

举例：

```
若 26Q2 总交易量重回 $300B+ 且 Circle 份额未突破 30%，则允许建立验证仓。
若 26Q3 云业务增速重回 20%+ 且蚂蚁 IPO 完成，则允许升级确认仓。
```

非法形式（Validator V-4 会拒绝）：

```
可以买入
继续持有
适当加仓
逢低吸纳
```

### 与 Validator 的关系

`90_AUTOMATION/PIPELINES/validate_investment_output.py` 在每次写入前都会：

- V-2：根据 `data_cutoff` / `expires_at` / `today` 重新计算 `state_status`，声明与计算不一致即拒绝；
- V-9：扫描 `CURRENT/*.md`，输出 `expired` / `due_for_review` / `missing_time_fields` / `inconsistent`；
- V-6：写入时要求 Reviewer `verdict == PASS` 且 `weakest_link` / `best_bear_case` 非空；
- V-7：拒绝通过 current 卡路径间接覆盖 canonical 正文。

### 状态转换

```
missing → current       仅在四条创建条件满足时
current → expired       today > expires_at 或 today > review_date（保守取早）
expired → current       reviewed 任务通过且刷新了 data_cutoff/expires_at
current → legacy_only   thesis 被推翻，或长期不再追踪（需 Murphy 明确）
```

`legacy_only` 不自动发生——必须有 Murphy 明确声明"不再追踪"或 thesis `failure_condition` 触发。

### 不允许的转换

- `missing → current` 但未经 Reviewer；
- `legacy_only → current` 自动批量回填；
- `expired → current` 仅修改日期而不刷新证据；
- `current → current` 覆盖时未保留 `open_disagreement`。

