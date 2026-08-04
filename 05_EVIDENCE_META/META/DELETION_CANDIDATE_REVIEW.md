---
title: deletion_candidate_review
date: 2026-07-24
updated: 2026-07-24
layer: META
primary_role: deletion_candidate_review
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
  - 05_EVIDENCE_META/META/LEGACY_FRONTMATTER_NORMALIZATION_REPORT.md
---

# Deletion Candidate Review

## 先说人话

**今天发生了什么：**按重构方案第 6.4 节检查了删除候选，但没有删除任何文件。

**为什么重要：**旧系统里确实有系统杂项、重复模板和疑似重复报告；但投资库的原则是先保留唯一原始材料，先做审计，再决定是否删除。

**现在做什么：**这些文件只进入 `X?` 候选；除 `.DS_Store` 这类系统杂项外，任何正文材料删除前都要先确认备份、链接和语义差异。

## 审计结论

| 候选类别 | 当前扫描结果 | 比对结果 | 当前动作 |
|---|---:|---|---|
| `.DS_Store` | 6 个 | macOS 系统杂项；方案原写 5 个，当前实扫多 1 个根目录文件 | `X?`，可在备份后清理 |
| `merged_sources` 疑似重复报告 | 1 对 | 文件名指向同主题；frontmatter 后字节不同，正文也存在格式与版本差异 | `X?`，先做语义差异审查，不删 |
| Hang Seng Tech / TQQQ 重复状态文件 | 2 个正文完全相同 | `next_questions.md` 与 `scorecard.md` 正文相同；其他文件只是模板相似、标的名不同 | `X?`，先判断目录归属正确性 |

## 明细

### `.DS_Store`

- `.DS_Store`
- `AI周期探索/.DS_Store`
- `AI周期探索/02_公司研究/.DS_Store`
- `分析报告/.DS_Store`
- `基础概念/.DS_Store`
- `基础概念/实体商/.DS_Store`

### `merged_sources` 疑似重复对

- `分析报告/archive/merged_sources/2026-06-06/20260606-BTGO+Circle+地平线+Oracle+结构窗口与财务窗口判断.md`
- `分析报告/archive/merged_sources/2026-06-06/260606BTGO_Circle_地平线_Oracle_结构窗口与财务窗口判断.md`

比对备注：两者不是逐字重复；正文长度不同，前半部分存在表格格式差异。不能直接删除其中任意一份。

### Hang Seng Tech / TQQQ 完全重复正文

- `AI周期探索/02_公司研究/Hang Seng Tech Index/next_questions.md`
- `AI周期探索/02_公司研究/TQQQ/next_questions.md`
- `AI周期探索/02_公司研究/Hang Seng Tech Index/scorecard.md`
- `AI周期探索/02_公司研究/TQQQ/scorecard.md`

比对备注：上述两组去除 frontmatter 后正文完全相同；但它们已被旧结构 metadata 降级为 State / Meta 或 Evidence，不再拥有当前决策权限。

## 删除前门槛

1. 先确认 `COVERAGE_MANIFEST`、新索引和历史归档仍能追溯原路径。
2. 正文材料必须先做语义 diff；只看文件名相似不够。
3. 删除动作必须是显式维护任务，不在普通研究、日报或调研中顺手执行。
4. 任何 AI 长报告、失败 Case、原始短记和唯一证据材料都不列入自动删除。
