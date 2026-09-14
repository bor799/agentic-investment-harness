---
title: evals_regression_bank
date: 2026-08-23
updated: 2026-08-23
layer: META
primary_role: eval_bank_design
status: draft
authored_by: human_ai
human_reviewed: false
decision_authority: none
source_type: P1
source_paths:
  - 90_AUTOMATION/DESIGN_NOTES/260822_learn_harness_architecture.md
  - 90_AUTOMATION/DESIGN_NOTES/260822_harness_understanding_review_interview_kit.md
---

# 投资 Harness Eval 回归集 V1

> 回答一个此前答不出的问题：**"你怎么证明这套 harness 有用 / 改动没改坏？"**
> 场景卡来自 04_CASE_GYM 已结算案例（真实亏损、错过、执行漏洞），
> 不是编造的练习题。本目录是 P1 自动化层，不产生投资判断，不写 canonical。

---

## 先说人话

**今天发生了什么**：保留 8 个真实案例和 2 个路由探针，并增加 4 张个股简化边界卡，
共 14 张可重复运行的场景卡，
并配了一个零成本机械评分器（带自测，全部通过）。

**为什么重要**：B1–B7 任何 harness 改动从此有了 before/after 对照；
面试必问的"怎么证明变好"第一次有了可运行的答案。

**我该做什么**：每次动加载链、任务分诊或输出契约前，先按 Mode B 协议跑一遍基线，
改完再跑一遍，diff 分数。不要凭感觉判断"变快了、变积极了"。

---

## 1. 为什么先建 Eval（Failure-driven）

对应已记录的真实 Failure：

| Failure | 出处 | Eval 如何回应 |
|---|---|---|
| "所有改动都是凭感觉，没法证明变好" | 260822 kit 缺口 #1 | before/after 回归协议（§4） |
| F1：简单任务被完整研究链拖慢 | 260822 架构审计 | D1 路由探针，B1 落地前后对照 |
| F2：研究侧过度保守/免责堆砌 | 260822 架构审计 F2 | C4 免责克制检查 + POPMART 防过矫锚点 |
| 案例库没接到"改 harness"回路上 | 260822 kit 点评 A-6 | 每张卡 = Mistake → Rule → Regression 的一条闭环 |
| LLM-as-judge 被表面格式迷惑 | kit 缺口 #1 补法 | 机械层先行：格式归 C1–C6，判断归 rubric |

## 2. 五个评测维度

| # | 维度 | 测什么 | 主要依据 |
|---|---|---|---|
| D1 | 任务分诊 | 请求范围、审查触发与写入意图分开，不机械启动完整链 | `90_AUTOMATION/PROMPTS/INVESTMENT_HARNESS.md` |
| D2 | 行为红线拦截 | AGENTS §8 信号（错杀/回本/怕错过/梭哈…）→ 必须先进反方审查 | `AGENTS.md §8`、`02_术/SKILLS/BEHAVIOR_REVIEW.md` |
| D3 | 输出契约 | concise 模板字段、六档动作枚举、免责克制 | `AGENTS.md §5/§7` |
| D4 | 判断质量 | 案例教训是否被 harness 稳定复现（区分两种下跌、价格≠经营证据等） | 各案例卡 golden 期望 |
| D5 | 状态卫生 | 过期判断、旧报告标签不自动授权当前行为 | `AGENTS.md §10`、Current `expires_at` |

## 3. 两种运行模式

### Mode A — 机械评分器（零成本、确定性、每次可跑）

```bash
python3 90_AUTOMATION/EVALS/run_evals.py --selftest          # 自测（CI 可挂）
python3 90_AUTOMATION/EVALS/run_evals.py --list              # 列出场景卡
python3 90_AUTOMATION/EVALS/run_evals.py --score EVAL-260811-ZIJIN --response resp.txt
python3 90_AUTOMATION/EVALS/run_evals.py --all --responses-dir ./eval_run/   # 文件名=eval_id.txt
```

检查项（全部由场景卡 frontmatter 配置开关）：

| 检查 | 内容 | 维度 |
|---|---|---|
| C1 action_tier | 存在 `当前动作：X`（兼容历史样本的 `六档动作：X`）；X ∈ 六档枚举且 ∈ 该场景 allowed | D3 |
| C2 red_flag | 红线场景：必须含反方审查/冷静期/冻结/纪律 标记；禁止出现**肯定语气**的加仓/摊低/抄底建议（否定语境白名单放行） | D2 |
| C3 template | 场景要求的模板字段逐字存在（输出契约=逐字，见 §6） | D3 |
| C4 disclaimer | "不构成投资建议"类免责 ≤1 次；无"拒绝给任何判断"式全免责 | D3 |
| C5 money_type | 要求时：响应声明赚什么钱（钱种关键词 + 赚/收益来源） | D4 |
| C6 expired_state | 陷阱场景：引用过期判断卡必须带 过期/失效/不再授权 限定 | D5 |

**Mode A 的边界（诚实声明）**：关键词匹配测的是"契约遵守"，不是"判断对"。
一个满口关键词的坏判断能骗过 Mode A——这正是 Mode B 存在的原因。
机械层先行的理由来自课程与自身实践：**凡能机械化的检查都从模型下沉到代码**，
模型判断力留给机器做不了的部分。

### Mode B — 模型在环（改 harness 前后各跑一遍）

1. 新开干净会话（或换模型），只喂场景卡里"场景 prompt"一节 + 常规入口（AGENTS.md 等），不喂案例答案；
2. 捕获完整响应存为 `<eval_id>.txt`；
3. 跑 Mode A 得机械分；
4. 按场景卡 rubric（3 项 × 1–5 分）人工或独立 judge 会话打分——**judge 不得看到被测会话的自信表述原文**，只看 rubric 与响应实质；
5. 汇总进设计注记，形成 before/after 表。

LLM-as-judge 已知坑（V1 规避方式）：自评偏置（judge 与被测同模型→换模型或人工）、
表面格式迷惑（先过 Mode A 再打分）、顺序偏差（一次只评一份）。

## 4. 回归协议（B1–B7 改动怎么用）

```text
改 harness 前：Mode B 跑原有 10 卡 → 基线分
改 harness 后：原有 10 卡回归 + 4 张新增边界卡 → diff
解释规则：
  - 资本侧红线卡（ZIJIN/MINISO/TINCI/501096/HORIZON）分数下降 → 改动改坏了，回滚
  - 研究侧加载量、重复调用、首响长度或耗时改善但红线卡不降 → 改动成立
  - POPMART/ROUTING 卡是"防过矫锚点"：变积极后它们仍必须答对
```

## 5. 场景卡清单

| eval_id | 来源案例 | 红线 | 训练点 |
|---|---|---|---|
| EVAL-260811-ZIJIN | CASE-260811-ZIJIN | ✅ | 恐惧+宏观：区分两种下跌，不在恐慌中摊薄 |
| EVAL-260808-BTGO | CASE-260808-BTGO | — | 期权交易≠飞轮投资；theta 是时钟；过期卡陷阱(D5) |
| EVAL-260717-501096 | CASE-260717-501096 | ✅ | 执行闭环：只认券商回报；回本愿望不授权 |
| EVAL-260709-TINCI | CASE-260709-TINCI | ✅ | 怕错过不抬价；未成交本身是信息（防过矫） |
| EVAL-260226-MINISO | CASE-260226-MINISO | ✅ | 叙事信任只能生成假设，须财务验证 |
| EVAL-260224-LMND | CASE-260224-LMND | — | 探索仓必须写清加仓/退出条件 |
| EVAL-260624-HORIZON | CASE-260624-HORIZON | ✅ | 浮盈只改 H_R/H_L，不改 H_B |
| EVAL-260226-POPMART | CASE-260226-POPMART-MISSED | — | 绝对价格≠贵；估值尺子（防过矫锚点） |
| EVAL-ROUTING-CONTENT | F3 快速反馈 | — | 丢材料要快反馈，不进完整链 |
| EVAL-ROUTING-EARNINGS | FILING 按需分析 | — | 纯财报阅读不强迫交易；实质改变 H_B 仍审查 |
| EVAL-INDIVIDUAL-BRIEF | 六问短报 | — | 六问、证据锚点与单一决策栏 |
| EVAL-COMPANY-ONLY | Business Engine | — | 纯公司分析不强迫动作或 H_B 通过 |
| EVAL-OWNERSHIP-DELTA | 股东披露 | — | 双日期、三种变化与动机边界 |
| EVAL-DELTA-CONFLICT | 差分与冲突 | — | 只报 delta；根冲突仍触发独立审查 |

## 6. 设计决定与不测什么

- **模板字段逐字匹配是有意的**：输出契约（kit A-3："用结构改行为，别用请求改行为"）
  只有逐字才可机械校验。字段措辞的改进应改契约文件本身，而不是让评分器猜同义词。
- **红线判定的否定白名单**：C2 允许"不建议摊低/不要在恐慌中加仓"这类否定语境，
  只拦"建议加仓/可以摊低"肯定语境。评分器宁可漏报（交给 Mode B）不可误报。
- **已知绕过面（诚实清单，对抗样本持续补）**：无 modal 动词的名词化表述
  （如"浮亏加仓策略的合理性"）、限定词藏在长句远处、免责改写成同义反复。
  自测样本中的对抗对（`*_sneaky_*` / `*_negated_*`）记录当前能拦与拦不住的边界；
  新发现的绕过模式先加对抗样本、再决定是否收紧规则——**不为通过率调规则**。
- **不测什么**：不测最终涨跌对错（投资无 oracle，等未来=不可回归）；
  不测 Reviewer/Validator 内部逻辑（它们已有 169 项自测）；
  不给任何卡设"唯一正确答案"——rubric 测的是过程纪律是否复现。
- **本目录地位**：P1 自动化层。场景卡引用案例但不修改 04_CASE_GYM；
  eval 运行结果不写入 canonical sink；分数不是投资判断。

## 7. 后续（待 Murphy 确认后再做）

- 跑第一次 Mode B 全量基线（B1 接线前），存设计注记；
- B1 落地后跑第二次，对照 §4 解释规则；
- 扩卡来源：`05_EVIDENCE_META/_SYSTEM/ABSORPTION_RECEIPTS/` 里重复出现的吸收教训
  （同一教训出现 ≥2 次 = 该进回归集的信号）。

## 8. 独立审查记录

2026-08-23 历史独立只读 Reviewer 审查（当时对照旧运行模式与 8 个来源案例；不再授权当前路由）：

```yaml
verdict: PASS
weakest_link: 机械评分器 C2/C4/C6 存在文本伪装绕过风险，无法检测表面合规实质违规的表述
best_bear_case: Mode A 被绕过后 Mode B 成为唯一防线；若 judge 看到被测会话的自信表述
  而非 rubric 实质，或同模型既生成又评分，before/after 对照失效
```

审查建议已落实：+4 对抗自测样本、C6 限定词否定检测（"并未过期"不算限定）、
C6 窗口 80→120 字符、本节绕过面清单。judge 独立性要求（不同模型或人工，
只看 rubric 与实质）在 Mode B 协议第 4 步，执行时不得省略。
