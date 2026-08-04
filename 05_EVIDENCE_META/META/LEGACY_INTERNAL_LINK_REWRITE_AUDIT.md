---
title: legacy_internal_link_rewrite_audit
date: 2026-07-24
updated: 2026-07-24
layer: META
primary_role: legacy_internal_link_rewrite_audit
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
  - 05_EVIDENCE_META/META/PHYSICAL_MIGRATION_BACKLOG.md
  - 05_EVIDENCE_META/META/PHASE2_VALIDATION_REPORT.md
---

# Legacy Internal Link Rewrite Audit

## 先说人话

**今天发生了什么：**已审计旧结构内部 Wikilink，确认旧原文里仍有 102 个文件、419 个旧式内部链接。

**为什么重要：**这些链接存在于历史原文、公司研究、每日简报和 AI 长报告中。它们现在是 Evidence / State / Case / Archive 来源层，不是当前前台。如果直接批量替换，可能破坏原文语境和审计链。

**现在做什么：**当前 canonical 范围链接已经通过校验；旧原文链接暂不直接重写，改由新索引、镜像、回执和本审计报告接管导航。

## 审计结果

| 指标 | 数量 |
|---|---:|
| 旧结构含 Wikilink 文件 | 102 |
| 旧结构 Wikilink 总数 | 419 |
| 当前 canonical 范围 missing links | 0 |
| 当前 canonical 范围 frontmatter 缺失 | 0 |
| 当前 canonical 范围必需权限字段缺失 | 0 |

## 不直接批量改旧原文的原因

1. 旧原文已被降权为来源层，链接本身属于历史上下文。
2. 同名旧文件很多，简单替换容易指向错误新文件。
3. AI 长报告和 Case 来源必须保留原始语境，不能为了导航好看改写证据。
4. 新结构已经通过索引和镜像提供可解析入口，当前工作不依赖旧原文链接。

## 当前导航策略

| 旧链接类型 | 当前处理 |
|---|---|
| 旧方法来源 | 通过 [[02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE_INDEX]] 与 [[02_术/SKILLS/METHOD_SOURCE_MERGE_STATUS]] 导航 |
| 旧公司/标的研究 | 通过 [[05_EVIDENCE_META/EVIDENCE/COMPANIES/COMPANY_DOSSIER_INDEX]] 导航 |
| 旧主题 Evidence | 通过 [[05_EVIDENCE_META/EVIDENCE/THEMES/ANALYSIS_REPORTS_INDEX]] 导航 |
| 旧 State / scorecard | 通过 [[05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/OLD_SCORECARDS_INDEX]] 导航 |
| 旧 Case 来源 | 通过 [[04_CASE_GYM/RESEARCH_CASES/MIGRATED_LEGACY_SOURCE_CASES_INDEX]] 导航 |
| AI 长报告 | 通过 [[05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/AI_LONG_REPORTS_INDEX]] 导航 |

## 后续重写门槛

只有满足三项才允许改写旧原文链接：

1. 有一对一映射表，且每个旧链接能唯一解析到新结构文件。
2. 改写不会改变引用语境、证据顺序或旧版本审计。
3. 改写前后都跑 canonical 范围和 legacy 范围链接检查，并保留 diff 报告。

在此之前，旧文件内链状态记为 `audited_frozen`，不是当前前台断链。
