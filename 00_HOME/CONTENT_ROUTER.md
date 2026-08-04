---
title: content_router
date: 2026-07-23
updated: 2026-07-25
layer: META
primary_role: content_router
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: operational
source_paths:
  - 90_AUTOMATION/DESIGN_NOTES/LEGACY_AUTOMATION_INVENTORY.md
---

# 内容路由

> 本文件决定外部材料进入 Harness 后产生哪种合法影响。
> 输入识别、任务分诊与运行契约见 [[90_AUTOMATION/PROMPTS/INVESTMENT_HARNESS]]。

## 新材料吸收

任何文章、研报、财报、截图、PDF、播客或长文本进入后，不以摘要完成为标准，而是回答：

- **新东西是什么：**
- **改变了什么：**
- **写到哪里：**

## 五种唯一判断

| 判断 | 使用条件 | canonical 写入位置 | 权限 |
|---|---|---|---|
| `SOURCE_CAPTURE` | 新的原文、事实或数据 | `05_EVIDENCE_META/SOURCES/<YYYY>/` | 不能自动改变 belief |
| `MOMENT_CAPTURE` | 我们的判断发生了尚待吸收的变化 | `05_EVIDENCE_META/MOMENTS/` | `authority: suggestion_only` |
| `KNOWLEDGE_UPDATE` | 稳定领域/实体 working belief 改变 | `05_EVIDENCE_META/KNOWLEDGE/` | Murphy + Reviewer + Validator |
| `STATE_UPDATE` | 带时效预期、市场或标的 thesis 改变 | `03_STATE/EXPECTATIONS/` 或 `03_STATE/HYPOTHESIS_QUEUE/CURRENT/` | 冻结/TTL + Reviewer + Validator |
| `NO_INCREMENT` | 同根重复、无认知差或无法影响判断 | 只在对话说明 | 不落盘 |

方法 proposal 与哲学候选仍按原权限分别进入对话 proposal 与 `01_道/PHILOSOPHY_INBOX/`，但它们不是普通文章的默认结果。

任何写入必须满足 `AGENTS.md §3` canonical sink 与 `AGENTS.md §4` Reviewer/Validator 触发条件。

## Knowledge 只更新既有判断结构

`KNOWLEDGE_UPDATE` 必须先指向一个领域和一个模式，并且只允许：

```yaml
knowledge_effect:
  domain_id:
  pattern_id:
  effect: strengthen | weaken | revise_chain | add_counterpattern | add_qualified_pattern
  independent_root_sources: []
  reused_targets_or_settled_cases: []
  failure_condition:
```

`add_qualified_pattern` 还必须同时满足：至少两个独立根来源、至少两个标的
或已结算 Case 可复用、因果链与失败条件明确。未过门槛的候选只进入 Moment
或 Open，不创建原子知识文件，也不进入 60 秒前台。

单篇材料默认只能成为 Source、Moment 或 State。重复同根观点、没有改变模式
或当前验证问题的摘要，输出 `NO_INCREMENT`。

## 自动化候选不是第六种判断

`AI_BELIEF_LOOP` runner 只把人工提供的输入包暂存为
`unverified_by_runner` 候选。Staging 不属于 Source、Moment、Knowledge
或 State，也不能被下游当作事实。只有回源核验后，Harness 才能按上面的
五种唯一判断晋升；晋升仍需 Murphy 明确写入、Reviewer PASS 与 Validator
PASS。

## 外部信源前置路由

用户直接提供文章、链接、截图、PDF 或长文本并要求解读、伴读、提炼时，如果没有明确归档位置，写文件前先问：进入当前周信息源、进入某个主题或标的体系，还是两边都要。未回答前可以在对话里解释，但不得创建、移动或改写笔记文件。

完整路由说明：`/Users/murphy/Documents/Obsidian Vault/信息源/信源与主题笔记路由规则.md`。

## Source / Knowledge 分账

- 新原文、事实、数据 → `05_EVIDENCE_META/SOURCES/<YYYY>/`
- 稳定领域判断 → `05_EVIDENCE_META/KNOWLEDGE/DOMAINS/<domain>/README.md`
- 稳定公司/ETF 结构 → `05_EVIDENCE_META/KNOWLEDGE/ENTITIES/`
- 仍在变化的预期 → `03_STATE/EXPECTATIONS/`
- AI 长报告原文（必须保留）→ `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/`
- 旧 `EVIDENCE/` 索引继续可读，但不再接收新材料。

`归档/分析报告/` 旧位置已被 `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/` 与 `05_EVIDENCE_META/EVIDENCE/THEMES/ANALYSIS_REPORTS_INDEX.md` 镜像吸收；兼容索引保留，新写入走上表。

## 不允许

- 不允许把摘要直接当 Evidence 写入；
- 不允许用同一 Source 同时生成多个独立证据权重；
- 不允许覆盖 frozen expectation；只允许新版本或结算；
- 不允许自动应用 `belief_update.proposed_state`；
- 不允许在 `01_道/`、`02_术/` canonical 正文、`03_STATE/PORTFOLIO_LEDGER.md` 持仓数据上直接覆盖；
- 不允许跳过 Reviewer 与 Validator 写入；
- 不允许把 `90_AUTOMATION/RUNTIME/STAGING/` 的候选直接当作 Source 或 Evidence；
- 不允许把旧 `/70` scorecard、旧 `交易宪法/CONSTITUTION.md`、旧长报告标签当作当前权威。
- 不允许把 `structural_prior`、合格模式数量或历史 Case 直接写成四票、六档动作或资本授权。
