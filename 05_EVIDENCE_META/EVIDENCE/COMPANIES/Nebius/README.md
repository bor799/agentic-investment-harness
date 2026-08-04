---
title: company_dossier
date: 2026-07-23
updated: 2026-07-23
layer: EVIDENCE
primary_role: company_dossier
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# Nebius

## 先说人话

**今天发生了什么：**本 dossier 把旧公司研究目录接入新 Evidence 前台，但不移动旧文件。

**为什么重要：**公司研究中的 Prompt、Evidence、State、旧评分和长报告现在分账显示；旧 scorecard 和 AI 长报告不再拥有当前决策权限。

**现在做什么：**读公司证据时先看 `evidence_log` 与 `company_research`；看当前问题去 State 队列；不要用旧 `/70` scorecard 授权交易。

## 文件分账

| 角色 | 数量 | 旧文件 |
|---|---:|---|
| `legacy_router` | 1 | [[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/Nebius/README]] |

## 权限边界

- Evidence 可以更新研究问题，不能直接生成 `murphy_status: confirmed`。
- `scorecard.md` 属于历史 State / 旧评分，统一 `decision_authority: none`。
- `PROMPT.md` 属于 Automation 模板，不是公司事实。
- `next_questions.md`、`next_signals.md` 和 `research_task.md` 属于会过期的 State。

## 数量快照

```yaml
file_count: 1
role_counts: {'legacy_router': 1}
```
