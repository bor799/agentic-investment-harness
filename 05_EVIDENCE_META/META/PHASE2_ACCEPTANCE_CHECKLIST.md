---
title: phase2_acceptance_checklist
date: 2026-07-23
updated: 2026-07-24
layer: META
primary_role: acceptance_checklist
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# Phase 2 Acceptance Checklist

## 先说人话

**今天发生了什么：**本轮完成了第二阶段的权限接管、前台重建、兼容入口降权、逐文件迁移 manifest，并把旧公司研究、公司问题队列、投资池、AI 周期自动化、分析报告、基础概念和个人交易 Case 接入新结构；旧结构 Markdown 也已补齐 legacy metadata。

**为什么重要：**旧核心页不再因为文件名拥有最高效力；新系统能先按道、术、State、Case、Evidence、Automation 分层工作。

**现在做什么：**用新前台继续工作；下一步重点不再是简单镜像，而是旧方法全文合并、Case 结算、吸收回执和旧内链重写。

## A. 权限验收

- [x] 重要新文件都有 `primary_role`。
- [x] Constitution 与 AGENTS 已分离。
- [x] 旧 Constitution、旧认知模型、旧命题账本、旧来源和旧覆盖文件已降为兼容入口。
- [x] AI 推断进入 `INFERRED_PATTERNS`，不使用 Murphy 第一人称。
- [x] 历史 AI 长报告未删除，迁移权限在 manifest 中统一降权；14 份 AI 长报告已镜像入 [[05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/MIRRORED_AI_LONG_REPORTS_INDEX]]。
- [x] 旧结构 Markdown 除 `AGENTS.md` 特殊规则文件外，均已补齐或规范化 frontmatter。
- [x] `_HISTORY` 与 `LEGACY_LAYOUT` 历史副本已补齐降权 metadata；详见 [[05_EVIDENCE_META/META/HISTORY_COPY_FRONTMATTER_REPORT]]。

## B. Constitution / MINDSET 验收

- [x] Constitution 只含 Guardrail + Router。
- [x] 七条 Guardrail 没有混入参数、Case、公司名、持仓和实时判断。
- [x] Router 指向的新前台链接已抽查，可解析。
- [x] MINDSET 前台不展示数据库式候选清单。
- [x] MINDSET 不含 State、公司判断和 AI 推断人格。
- [x] `INFERRED_PATTERNS` 明确标注为待验证。

## C. “术”的验收

- [x] 已建立 Trading System 和 11 个 canonical Skill。
- [x] 每个 Skill 写清输入、输出、不能证明什么和失败条件。
- [x] 旧 `/70`、固定 LR、未校准单点概率和旧仓位参数已在 `PARAMETERS.md` 降权。
- [x] 已建立 [[02_术/SKILLS/METHOD_ABSORPTION_MAP]]，旧方法到 canonical Skill 有接管映射。
- [x] 已补强核心决策合同、公司基本面、流动性、估值、供需、瓶颈和行为审查 Skill。
- [x] 旧方法正文 44/44 已逐段合并入 canonical Skill / Trading System / State / Meta / Automation / Philosophy Inbox / Evidence；详见 [[02_术/SKILLS/METHOD_SOURCE_MERGE_STATUS]]。
- [x] 个人交易手册 6 个核心样本已标准化进入 [[04_CASE_GYM/CASE_FRONTSTAGE_INDEX]]。
- [x] Backlog 中 9 个 Case 来源已接入 Case Gym：个人交易手册由 6 个标准 Case 覆盖，其余 8 个旧实体商/IP 来源已抽成 [[04_CASE_GYM/RESEARCH_CASES/MIGRATED_LEGACY_SOURCE_CASES_INDEX]]。
- [x] 新迁入 8 张 Case 来源卡已逐张补齐结算规则、期限和阶段性事实结算；当前状态为 `partially_settled_price_path / settled_process_lesson / rule_defined_unsettled / not_executed_plan`。

## D. 新材料吸收验收

- [x] 已建立四类吸收结果：`METHOD_UPDATE / STATE_UPDATE / PHILOSOPHY_CANDIDATE / NO_INCREMENT`。
- [x] 已建立极简吸收回执模板。
- [x] Philosophy Inbox 候选没有自动进入 MINDSET。
- [x] 已为 13 个代表性材料/材料族建立 [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS_INDEX]]。
- [x] 抽查的重要材料和代表性材料族已有吸收回执，覆盖 `METHOD_UPDATE / STATE_UPDATE / PHILOSOPHY_CANDIDATE / NO_INCREMENT` 四类结果；普通历史材料后续按需补齐。

## E. 全局迁移验收

- [x] 当前本地旧结构扫描到 `633` 个文件，均有 manifest 迁移记录。
- [x] 旧 `AI周期探索/02_公司研究` 和 `AI周期探索/标的研究` 已生成 62 个公司/标的 dossier。
- [x] 旧公司 `research_task/next_questions/next_signals` 已接入 [[03_STATE/HYPOTHESIS_QUEUE/COMPANY_QUESTIONS_INDEX]]。
- [x] 旧 `AI周期探索/04_投资池` 已接入 [[03_STATE/WATCHLISTS/AI_CYCLE_WATCHLISTS_INDEX]]。
- [x] 旧 AI 周期 prompt、pipeline、runtime 已分别接入 `90_AUTOMATION` 索引。
- [x] 旧 `/70` scorecard 已接入 [[05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/OLD_SCORECARDS_INDEX]]。
- [x] `分析报告/` 已接入 [[05_EVIDENCE_META/EVIDENCE/THEMES/ANALYSIS_REPORTS_INDEX]]、[[05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/ANALYSIS_STATE_ARCHIVE_INDEX]] 和 [[05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/AI_LONG_REPORTS_INDEX]]。
- [x] `基础概念/交易策略组合` 已接入 [[02_术/SKILLS/BASIC_CONCEPTS_METHOD_SOURCE_INDEX]]。
- [x] `基础概念/实体商` 已接入 [[05_EVIDENCE_META/EVIDENCE/COMPANIES/BASIC_CONCEPTS_COMPANY_EVIDENCE_INDEX]]。
- [x] 个人交易手册 Case 已接入 [[04_CASE_GYM/TRADE_LOG/LEGACY_TRADE_CASES_INDEX]]。
- [x] Case 捕捉模板和方法测试模板已建立。
- [x] 501096、天赐、名创、地平线、LMND、泡泡玛特未买入对照已转成标准 Case。
- [x] 代表性材料吸收回执已覆盖 `METHOD_UPDATE / STATE_UPDATE / PHILOSOPHY_CANDIDATE / NO_INCREMENT` 四类结果。
- [x] 旧路径已有关键重定向或兼容入口。
- [x] 旧结构 Markdown frontmatter 权限字段校验：`layer / primary_role / status / decision_authority` 缺失均为 `0`；详见 [[05_EVIDENCE_META/META/LEGACY_FRONTMATTER_PATCH_REPORT]] 与 [[05_EVIDENCE_META/META/LEGACY_FRONTMATTER_NORMALIZATION_REPORT]]。
- [x] 删除候选已登记为 `X?`，本轮未删除唯一材料；详见 [[05_EVIDENCE_META/META/DELETION_CANDIDATE_REVIEW]]。
- [x] 旧结构物理迁移 backlog 已建立，611 个旧 Markdown 入队；详见 [[05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG]]。
- [x] 第一批可逆物理迁移已完成：14 份 AI 长报告镜像、8 张旧来源 Case 卡；详见 [[05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BATCH1_REPORT]]。
- [x] 第二批可逆物理迁移已完成：117 个旧问题队列、8 个旧观察池、6 个旧自动化 State、54 个旧 scorecard 镜像；详见 [[05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BATCH2_REPORT]]。
- [x] 第三批可逆物理迁移已完成：191 个旧公司/标的 Evidence、45 个旧主题 Evidence 镜像；详见 [[05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BATCH3_REPORT]]。
- [x] 第四批可逆物理迁移已完成：7 个治理历史镜像、72 个自动化 Review Queue、2 个当前自动化候选副本；详见 [[05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BATCH4_REPORT]]。
- [x] 第五批可逆物理迁移已完成：44 个旧方法来源镜像入 [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE_INDEX]]；详见 [[05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BATCH5_REPORT]]。
- [x] 第六批可逆物理迁移已完成：41 个旧分析 State 镜像入 [[05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/MIRRORED_LEGACY_ANALYSIS_STATE_INDEX]]；详见 [[05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BATCH6_REPORT]]。
- [x] 第七批可逆物理迁移已完成：旧个人交易手册全文和旧每日投资观察全文镜像；详见 [[05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BATCH7_REPORT]]。
- [x] 物理迁移 backlog 中 611 个旧 Markdown 均已有新结构接入点或镜像/队列位置；方法来源仍需逐段合并。
- [x] 新前台与兼容入口 Wikilink 检查结果：`missing_links_current_scope = 0`；新结构非镜像 Markdown 权限字段缺失为 `0`；详见 [[05_EVIDENCE_META/META/PHASE2_VALIDATION_REPORT]]。
- [x] 未不可恢复删除唯一原始材料。
- [x] 旧文件已完成可逆物理接入；未进行不可恢复移动或删除。
- [x] 当前 canonical 范围链接已全部可解析；旧原文内部链接已完成审计并冻结直接批量重写，详见 [[05_EVIDENCE_META/META/LEGACY_INTERNAL_LINK_REWRITE_AUDIT]]。

## F. 五个样例测试

| 测试输入 | 当前路由结果 | 状态 |
|---|---|---|
| 外部文章提出新方法 | Evidence 指针 + `METHOD_UPDATE` + Skill changelog | pass by router |
| 一次真实亏损交易 | Case + 临时防火墙或实验性 Skill 更新 | pass by router |
| 改变当前行业判断的新闻 | `STATE_UPDATE` + data cutoff / TTL | pass by router |
| AI 发现 Murphy 隐性模式 | `INFERRED_PATTERNS` + `murphy_status: unreviewed` | pass |
| 同一新闻多篇转述 | 一个根 Evidence + `NO_INCREMENT` | pass by router |

## 收口边界

本轮已完成 611 个旧 Markdown 的可逆物理接入和权限接管，并把 44/44 个旧方法来源合并进 canonical Skill / Trading System / State / Meta / Automation / Philosophy Inbox / Evidence，8 张新迁入 Case 来源卡也已补齐结算规则和阶段性结算状态；当前 canonical 范围链接为 0 断链，旧原文内链已审计并冻结直接批量重写。后续普通历史材料仍可按需补吸收回执。
