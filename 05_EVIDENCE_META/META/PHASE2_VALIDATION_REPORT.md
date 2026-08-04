---
title: phase2_validation_report
date: 2026-07-24
updated: 2026-07-24
layer: META
primary_role: validation_report
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
  - 05_EVIDENCE_META/META/PHASE2_ACCEPTANCE_CHECKLIST.md
---

# Phase 2 Validation Report

## 先说人话

**今天发生了什么：**对第二阶段重构产物跑了脚本编译、旧结构 metadata 覆盖和当前 canonical 范围 Wikilink/frontmatter 检查，并复核本次旧根框架方法源合并。

**为什么重要：**这一步确认新系统不是只有目录看起来正确，而是能被脚本复跑、能被链接导航、能把旧材料权限降下来。

**现在做什么：**继续使用 `00_HOME/HOME.md` 作为入口；可逆物理接入、旧方法合并、Case 阶段性结算、代表性吸收回执和旧原文链接审计均已收口。

## 验证结果

| 检查 | 结果 | 备注 |
|---|---:|---|
| Pipeline 编译 | pass | 14 支 Phase 2 脚本均通过 `py_compile` |
| 旧结构 Markdown | 612 | 包含 `AGENTS.md` 特殊规则文件 |
| 已检查 frontmatter | 611 | `AGENTS.md` 保持原样 |
| 缺 `layer` | 0 | 当前权限字段已覆盖 |
| 缺 `primary_role` | 0 | 当前权限字段已覆盖 |
| 缺 `status` | 0 | 当前权限字段已覆盖 |
| 缺 `decision_authority` | 0 | 当前权限字段已覆盖 |
| 当前 canonical 范围 Wikilink 检查文件 | 186 | 新前台、治理层、自动化入口；排除历史副本、镜像和 Review Queue |
| 当前范围 missing links | 0 | 目录、CSV、脚本、JSON 按真实文件存在判断 |
| 历史原文/镜像副本保留旧外链 | not_rechecked | `_HISTORY`、旧日报、镜像副本、Review Queue 和旧源正文中的旧链接，不作为当前断链 |
| 新结构非队列 Markdown frontmatter | 186 | 必需权限字段缺失 `0` |
| 旧 Markdown 可逆物理接入 | 611 | backlog 611/611 均有新结构接入点 |
| AI 长报告镜像副本 | 14 | 第一批可逆物理迁移完成 |
| 旧来源 Case 卡 | 8 | 已补齐结算规则、期限和阶段性结算状态 |
| 旧个人交易手册全文镜像 | 1 | 第七批可逆物理迁移完成 |
| 旧每日投资观察镜像 | 1 | 第七批可逆物理迁移完成 |
| Hypothesis Queue 镜像 | 117 | 第二批可逆物理迁移完成 |
| Watchlists 镜像 | 8 | 第二批可逆物理迁移完成 |
| Automation State 镜像 | 6 | 第二批可逆物理迁移完成 |
| Scorecards 镜像 | 54 | 第二批可逆物理迁移完成 |
| Analysis State 镜像 | 41 | 第六批可逆物理迁移完成 |
| 旧方法源合并进度 | 44/44 | 已新增根框架方法源吸收；Review Queue 方法源已全部合并 |
| 吸收回执 | 13 | 新增 `root_framework_absorption_receipt` |
| 旧原文内链审计 | 102 文件 / 419 链接 | 旧原文链接状态 `audited_frozen`；当前前台不依赖旧链接 |
| 公司/标的 Evidence 镜像 | 191 | 第三批可逆物理迁移完成 |
| 主题 Evidence 镜像 | 45 | 第三批可逆物理迁移完成 |
| 治理历史镜像 | 7 | 第四批可逆物理迁移完成 |
| 自动化 Review Queue | 72 | 第四批可逆物理迁移完成，未晋升 canonical |
| 当前自动化候选 | 2 | 第四批可逆物理迁移完成，仍需核验 |
| Method Source Review Queue | 44 | 第五批可逆物理迁移完成，44 个来源已合并入 canonical 体系 |
| 旧方法来源合并 | 44 / 44 | 期权方法、旧 Constitution skills、分析报告方法源、基础概念普通方法源、旧 AI 周期方法源与根框架已合并；详见 [[02_术/SKILLS/METHOD_SOURCE_MERGE_STATUS]] |

## 本次增量验证

- 旧 Constitution skills 7 个来源已写入 [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/constitution_skills_absorption_receipt]]。
- 7 个来源已分流进入 `Research Flow / Capital And Execution / Feedback Loop / Supply Demand / Liquidity / Behavior / Meta`，旧路径只保留来源权限。
- 分析报告方法源 5 个来源已写入 [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/analysis_method_sources_absorption_receipt]]。
- 5 个来源已分流进入 `Structural Change / Company Fundamentals / Capital / Behavior / Feedback / Liquidity / Supply Demand / Automation`，旧报告中的个案判断和旧参数不恢复授权。
- 基础概念普通方法源 15 个来源已写入 [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/basic_concepts_method_sources_absorption_receipt]]。
- 15 个来源已分流进入 `Research Flow / Capital / Structural Change / Supply Demand / Valuation / Growth Tech / Company Fundamentals / Liquidity`，旧概率、评分、Kelly 和固定仓位不恢复授权。
- 旧 AI 周期方法源 12 个来源已写入 [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/ai_cycle_method_sources_absorption_receipt]]。
- 12 个来源已分流进入 `Structural Change / Feedback Loop / Watchlists / Provenance / Automation`，旧公司清单、工具状态、三倍标签、得分和命令示例不恢复授权。
- 根框架 1 个来源已写入 [[05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/root_framework_absorption_receipt]]。
- 1 个来源已分流进入 `Research Flow / Philosophy Inbox / Evidence`，旧配置比例、ETF 代码、地产个案和公司计划不恢复授权。
- 当前 canonical 范围 Wikilink：`checked_current_scope_md = 186`，`missing_links_current_scope = 0`。
- 当前 canonical 范围 frontmatter：`missing_frontmatter = 0`，`missing_required_fields = 0`。

## 已验证脚本

- `90_AUTOMATION/PIPELINES/phase2_restructure_bootstrap.py`
- `90_AUTOMATION/PIPELINES/phase2_materialize_indexes.py`
- `90_AUTOMATION/PIPELINES/phase2_materialize_legacy_layers.py`
- `90_AUTOMATION/PIPELINES/phase2_patch_legacy_frontmatter.py`
- `90_AUTOMATION/PIPELINES/phase2_normalize_legacy_frontmatter.py`
- `90_AUTOMATION/PIPELINES/phase2_build_migration_backlog.py`
- `90_AUTOMATION/PIPELINES/phase2_materialize_physical_batches.py`
- `90_AUTOMATION/PIPELINES/phase2_materialize_state_scorecard_batch.py`
- `90_AUTOMATION/PIPELINES/phase2_normalize_history_copies.py`
- `90_AUTOMATION/PIPELINES/phase2_materialize_evidence_batch.py`
- `90_AUTOMATION/PIPELINES/phase2_materialize_governance_automation_batch.py`
- `90_AUTOMATION/PIPELINES/phase2_materialize_method_source_batch.py`
- `90_AUTOMATION/PIPELINES/phase2_materialize_analysis_state_batch.py`
- `90_AUTOMATION/PIPELINES/phase2_materialize_special_legacy_batch.py`

## 收口边界

- 当前 canonical 范围链接已全部可解析；旧原文内部链接已审计并冻结直接批量重写。
- 抽查的重要材料和代表性材料族已有吸收回执；普通历史材料后续按需补齐。
- 旧方法正文 44/44 已逐段并入 canonical Skill / Trading System / State / Meta / Automation / Philosophy Inbox / Evidence。
- 新迁入 8 张 Case 来源卡已逐张补齐结算规则、期限和阶段性结算状态；`rule_defined_unsettled` 与 `partially_settled_price_path` 后续仍需按复核日回源。
