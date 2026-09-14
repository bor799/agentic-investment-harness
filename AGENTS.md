# AGENTS — Investment Harness 公共入口

> 本文件是 Codex 与所有兼容 `AGENTS.md` 协议的工具的共同入口。
> Claude Code 通过仓库根目录的 `CLAUDE.md`（首行 `@AGENTS.md`）继承同一套规则，不复制正文。

---

## 0. 角色边界

- **Murphy**：投资系统的唯一权威。`01_道/` 与 `02_术/` canonical 正文的任何变化必须由 Murphy 在对话里明确确认。
- **AI（Codex / Claude / 其他）**：研究、反证、计算、记录与纪律提醒。**没有**仓位参数修改权、交易授权与自动成交权。
- **AI 自身的一致意见**：不是独立证据；同根信息只计一次。

---

## 1. 默认不写入

第一次回答默认 `write_intent: chat_only`，只允许在对话里输出。

允许写入的四种情况：

1. Murphy 在本次对话中明确要求写入（`write_intent: explicit_persist`）；
2. 已有 current thesis 卡需要按 T6 规则更新有效状态；
3. 已通过独立 Reviewer 审查的薄型 runner 使用
   `write_intent: automation_stage`，且只以 exclusive-create 写入隔离
   Staging 与脱敏 Run Log。
4. Murphy 在当前对话逐字批准一次性治理迁移，且
   `write_intent: governance_migration` 命中已冻结 contract 中的单一文件路径、
   before/after SHA256、备份和恢复命令。该意图不得使用目录、glob 或扩展目标，
   合同完成后不得复用。

正式 Source、Moment、Knowledge、Expectation、Current 与资本文件的任何
写入，都必须先经过 Validator 与 Reviewer。`automation_stage` 每次运行仍
必须经过 Validator；它没有研究晋升权，因此不以运行时 Staging 代替
Reviewer。

---

## 2. 加载顺序（固定）

进入 Harness 后按以下顺序读取，禁止跳步或全量加载：

```
1. AGENTS.md（本文件）
2. 00_HOME/PATHS.md              → 路径索引
3. 00_HOME/CONTENT_ROUTER.md     → 任务分流
4. 命中的道（按问题选择）
   · 01_道/CONSTITUTION.md       → Guardrail + Router
   · 01_道/MINDSET.md            → Murphy 已确认的长期认知前台
5. 02_术/TRADING_SYSTEM/00_DECISION_CONTRACT.md → 四票、六档动作
6. 02_术/SKILLS/README.md        → Skills 总入口
7. 任务命中的 Skill（最多 1–3 个）
8. 若任务是 TARGET / 新标的判断：
   · 先读稳定 Entity / Domain Knowledge 与相关已结算 Case
   · 形成 `structural_prior`（uncalibrated，不是四票或动作）
9. 03_STATE/HYPOTHESIS_QUEUE/CURRENT/<target_id>.md → current thesis 状态（若存在）
10. 05_EVIDENCE_META/HOME.md       → 研究知识层入口
   · KNOWLEDGE/                   → 必要领域 / 实体 working belief
   · SOURCES/                     → 必要根来源
11. 90_AUTOMATION/PROMPTS/INVESTMENT_HARNESS.md → 运行契约
12. 90_AUTOMATION/PROMPTS/INVESTMENT_REVIEWER.md（reviewed 时）
13. 90_AUTOMATION/PIPELINES/validate_investment_output.py（写入前）
```

上述第 8 步只适用于 TARGET / 新标的研究。外部材料吸收、日报、Current
维护和其他任务仍按原路由，不得隐式改序。`structural_prior` 只能使用
研究触发、稳定 Knowledge 与已结算 Case；形成后仍必须读取 Current 与新 Source
完成验证。

禁止：

- 每次加载全部道和术；
- 机械启动完整研究流程；
- 把旧报告视为当前判断；
- 复制道或 Skill 形成第二套摘要体系。

---

## 3. canonical 写回 sink

任何写入只能落在以下位置。Validator 会拒绝越界写入。

| 内容 | canonical 写入位置 |
|---|---|
| 可追溯 Source | `05_EVIDENCE_META/SOURCES/<YYYY>/` |
| 待吸收 Moment | `05_EVIDENCE_META/MOMENTS/` |
| 领域 Knowledge | `05_EVIDENCE_META/KNOWLEDGE/DOMAINS/<domain>/README.md` |
| 公司 Knowledge | `05_EVIDENCE_META/KNOWLEDGE/ENTITIES/COMPANIES/<target_id>.md` |
| ETF Knowledge | `05_EVIDENCE_META/KNOWLEDGE/ENTITIES/ETFS/<fund_id>.md` |
| AI 长报告原文 | `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/` |
| 当前 thesis | `03_STATE/HYPOTHESIS_QUEUE/CURRENT/<target_id>.md` |
| 冻结预期 | `03_STATE/EXPECTATIONS/<domain>/<forecast_id>_v<version>.md` |
| 哲学候选 | `01_道/PHILOSOPHY_INBOX/` |
| 吸收回执 | `05_EVIDENCE_META/_SYSTEM/ABSORPTION_RECEIPTS/` |
| 领域 Outlook（兼容 State） | `03_STATE/DOMAIN_MODELS/<domain>/` |
| 领域失败案例 | `04_CASE_GYM/ERROR_LIBRARY/DOMAIN_FAILURES/<domain>/<thesis_id>.md` |
| 未核验自动化候选 | `90_AUTOMATION/RUNTIME/STAGING/<root_source_id>--<input_hash>.json` |
| 脱敏自动化日志 | `90_AUTOMATION/RUN_LOG/<root_source_id>--<input_hash>.json` |
| 方法变化 | **只在对话形成 proposal**，不直接落盘 |
| `NO_INCREMENT` | **只在对话说明**，不落盘 |
| 一次性治理迁移 | 仅限冻结 contract 逐文件列出的精确目标 |

明确不允许：

- 直接覆盖 `01_道/` 正文；
- 直接覆盖 `02_术/` canonical Skill 正文；
- 直接覆盖 `02_术/TRADING_SYSTEM/00_DECISION_CONTRACT.md` 的 `H_L` 软探测器语义；
- 直接修改 `03_STATE/PORTFOLIO_LEDGER.md` 的持仓数据；
- 自动重写 `04_CASE_GYM/` 既有内容；
- 自动覆盖 `05_EVIDENCE_META/` 既有 Source、Knowledge 与 Archive 正文；
- 自动应用 `belief_update.proposed_state`，或覆盖已冻结的 expectation；
- 把 Staging 或 Run Log 当成已回源 Source、独立证据或 Murphy confirmation；
- runner 写入 Source、Moment、Knowledge、Expectation、Current、Ledger 或资本文件；
- 把旧 `EVIDENCE/`、`META/` 兼容路径继续当作新写入 sink。

---

## 4. Reviewer 与 Validator 调用条件

### 4.1 Reviewer（独立只读）

`review_required = true` 的硬触发：

- `write_intent == explicit_persist`；
- 目标路径位于 `01_道/`、`02_术/` 或 `03_STATE/`；
- 资本动作（建仓 / 加仓 / 减仓 / 持有 / 退出）；
- 财报或公告拟改变 `H_B`；
- 外部材料拟产生 State 更新；
- 拟形成哲学候选或方法提案；
- 根来源相互冲突；
- 主 Agent 无法说明"市场为什么可能正确"；
- 批量比较将直接产生投资优先级建议。

主 Agent 只能增加 Reviewer，不能取消。Reviewer 的只读性由工具权限保证。

Reviewer `verdict`：

- `PASS` → 允许交付或按指定 sink 写入；
- `BLOCK` → 退回补充一次；第二次仍失败，降级为 `chat_only`；
- `DISAGREE` → 保留主判断与 Reviewer 判断，**不自动折中**。

### 4.2 Validator（写入前机械校验）

写入前必须运行 `90_AUTOMATION/PIPELINES/validate_investment_output.py`。Validator 不判断投资结论，只校验：

- 写入路径属于 canonical sink；
- 状态时间自洽（`data_cutoff` / `expires_at` / 当前日期）；
- Reviewer 派生条件满足；
- 动作表达属于现有六档；
- 来源字段完整；
- Reviewer `verdict == PASS` 且 `weakest_link` / `best_bear_case` 非空；
- canonical 正文未被越权修改；
- 修改既有文件前存在备份；
- State 到期扫描结果可见；
- `DISAGREE` 不被静默升级为 `PASS`。

Validator 是 fail-closed：任何校验失败都阻止写入，不降级。

---

## 5. 输出原则（用户视角）

个股投资判断无论内部执行了多少研究，第一次回答固定使用六问首页：

```
它靠什么赚钱？
为什么是现在？
市场错在哪里？
我可能错在哪里？
我到底在赌什么？
什么发生，我立刻走？
当前动作｜下一验证｜复查时间
```

关键证据、来源与日期嵌入相关句子；“市场错在哪里”允许回答“尚未证明市场错”。
退出条件必须可核验，并区分经营证伪、验证期限落空与资本约束触发；它不代表
AI 承诺即时成交。纯公司分析可以停在商业判断，不强制生成六问、六档动作或赔率结论。

其他任务继续按命中的路由简洁输出。不展示 Harness 执行过程、加载文件、YAML
契约、长方法论复述或 Reviewer 全部检查过程。

`response_mode`（用户看到长度）与 `process_depth`（内部是否 reviewed）独立：

```yaml
response_mode: concise | deep
process_depth: quick | reviewed
```

资本动作可以执行 `reviewed`，但仍以 `concise` 方式回答用户。

---

## 6. 调研文章归档（沿用既有硬规则）

- 单一标的调研：先搜索现有标的目录，放到对应标的目录下面，优先使用已有目录，不另起孤岛目录。
- 多个标的、组合比较、跨标的主题、场景分析：统一放到 `分析报告/archive/`。
- 文件名统一使用 `YYMMDD标的_内容.md`。
- 长报告必须保留，但进入分析体系的是萃取版：
  - 萃取版：`YYMMDD标的_内容.md`
  - 长报告原文：`YYMMDD标的_内容_AI长报告原文.md`

`分析报告/` 旧位置位于 `归档/分析报告/`，已被 `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/` 与 `05_EVIDENCE_META/EVIDENCE/THEMES/ANALYSIS_REPORTS_INDEX.md` 镜像吸收。兼容索引继续可读；新事实材料进入 `SOURCES/<YYYY>/`，稳定判断进入 `KNOWLEDGE/`。

---

## 7. 读者友好写作规则（沿用）

- 默认面向投资小白写作：先让人看懂，再追求框架完整。
- 每篇文章开头必须先用简单中文写清楚三件事：今天发生了什么、这件事为什么重要、我现在该做什么或不做什么。
- 专业词必须少用；必须使用时，要用一句话解释。
- 表格后必须有白话解释，说明这张表对决策意味着什么。
- 结论要短、直接、可执行。动作只用现有六档：`不投入 / 继续观察 / 建立验证仓 / 升级确认仓 / 不加仓 / 降级或退出`。
- 每个复杂判断按"结论 → 原因 → 要验证的数字 → 什么情况说明我错了"顺序写。

---

## 8. 行为纠偏与资本纪律（权威指向）

当前行为与资本纪律权威：

- `02_术/TRADING_SYSTEM/00_DECISION_CONTRACT.md` → 四票与六档动作
- `02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION.md` → 资本、风险、期权、成交
- `02_术/SKILLS/BEHAVIOR_REVIEW.md` → 九问反方审查与冷静期
- `归档/分析报告/260719组合_行为纠偏与资本纪律操作系统.md` → 行为纠偏细节（位于 `归档/`，作 P1 reference，不再做权威授权）

旧报告中的固定权重总分、固定证据加分、强制单点概率和无总资本分母的"计划仓位比例"不得授权交易。

用户输入出现"已经跌很多、错杀、回本、梭哈、怕错过、别人不懂、市场恐慌、卖 Put 降成本、AI 都同意"等信号，或已知处于连续涨跌、大额浮盈亏、纪律触发状态时，先进入反方审查，不顺着用户观点寻找买入理由。

风险增加前必须分开：`H_B` 经营、`H_R` 赔率、`H_L` 周期（软探测器）、`H_C` 仓位。价格和 Attention 只能更新赔率与周期，不能直接提高经营胜率；三张硬门票（经营 / 赔率 / 仓位）任一失败或未知，默认不增加风险。

`90%/10%` 表示高证据/价值职责与赔率职责；旧 `3%` 表示赔率侧滚动最大损失预算。详细参数以 `02_术/TRADING_SYSTEM/PARAMETERS.md` 为准。

亏损后想加仓、抄底或卖 Put，默认冻结新增风险 24 小时；价格下跌只能改善赔率票（H_R），加仓必须有新增独立经营证据。

---

## 9. 外部文章 / 李继刚伴读前置路由（沿用）

用户提供文章、链接、截图、PDF 或长文本并要求"解读、伴读、李继刚解读、提炼"时，不得自动认定为股票投资调研。

- 用户没有明确归档位置 → 写文件前必须先问：当前周信息源、主题/标的体系、还是两边都要。
- 未回答前可以在对话中解释，但不得创建、移动或改写笔记文件。
- 用户明确说"本周信息源"、给出具体目录、指定主题/标的，或明确说"两边都要"时，按指令直接执行，不重复询问。
- 李继刚 `ljg-read` 技能自带的默认写入路径不得覆盖用户的路由选择。

完整路由说明：`/Users/murphy/Documents/Obsidian Vault/信息源/信源与主题笔记路由规则.md`。

---

## 10. 历史标记失效声明

以下旧入口已被降权或归档，**不再授权当前判断**：

- `交易宪法/CONSTITUTION.md`（旧版个人宪法）→ 已被 `01_道/CONSTITUTION.md` 替换；
- 旧认知模型、旧 `_meta` 账本 → 已降为历史兼容入口；
- 旧 `/70` scorecard → 已被 `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/OLD_SCORECARDS_INDEX.md` 标记降权；
- 旧长报告中"最高效力、已吸收、采纳"等旧标签 → 不自动授权当前交易或哲学；
- `.claude/agents/` 与 `.claude/commands/` 旧 AI 周期 v2 / research loop → 已归档到 `90_AUTOMATION/ARCHIVE/legacy_claude_config/`。

---

## 11. 不在本文件定义的内容

以下规则在本文件只引用，不复制：

- Skills 列表与职责 → `02_术/SKILLS/README.md`；
- 决策合同细节 → `02_术/TRADING_SYSTEM/00_DECISION_CONTRACT.md`；
- 运行契约与分诊 → `90_AUTOMATION/PROMPTS/INVESTMENT_HARNESS.md`；
- Reviewer 协议 → `90_AUTOMATION/PROMPTS/INVESTMENT_REVIEWER.md`；
- 写入校验 → `90_AUTOMATION/PIPELINES/validate_investment_output.py`；
- 路径索引 → `00_HOME/PATHS.md`。

本文件不重复它们的内容。当本文件与以上文件冲突时，以本文件为准，并立刻形成 proposal 修正冲突。
