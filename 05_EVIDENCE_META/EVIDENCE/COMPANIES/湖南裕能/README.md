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

# 湖南裕能

## 先说人话

**今天发生了什么：**本 dossier 把旧公司研究目录接入新 Evidence 前台，但不移动旧文件。

**为什么重要：**公司研究中的 Prompt、Evidence、State、旧评分和长报告现在分账显示；旧 scorecard 和 AI 长报告不再拥有当前决策权限。

**现在做什么：**读公司证据时先看 `evidence_log` 与 `company_research`；看当前问题去 State 队列；不要用旧 `/70` scorecard 授权交易。

## 文件分账

| 角色 | 数量 | 旧文件 |
|---|---:|---|
| `ai_long_report_original` | 2 | [[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260706天赐材料_暴跌后的买点与双层结构判断_AI长报告原文]]<br>[[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260709天赐材料_雪球电解液之王逻辑链与证据更新_AI长报告原文]] |
| `automation_prompt` | 1 | [[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/PROMPT]] |
| `evidence_company_research` | 1 | [[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/company_research]] |
| `evidence_log` | 2 | [[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/evidence_log]]<br>[[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/evidence_log]] |
| `evidence_or_state_report` | 15 | [[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260616天赐材料_产业结构秩序创造机器判断]]<br>[[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260616天赐材料_价格信号与赚钱概率判断]]<br>[[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260616天赐材料_旧框架复盘与投资假设萃取]]<br>[[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260622天赐材料_涨跌叙事事实审计与1至3年判断]]<br>[[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260704天赐材料_产能重配经营验证增量]]<br>[[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260706天赐材料_暴跌后的买点与双层结构判断]]<br>[[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260709天赐材料_6F定价权与缺货窗口校验]]<br>[[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260709天赐材料_储能假设交叉验证与贝叶斯交易结论]]<br>[[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260709天赐材料_定价权与难攻破节点判断]]<br>[[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260709天赐材料_挂单价格与PE安全边界]]<br>[[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260709天赐材料_新型储能趋势与高端材料瓶颈调研提纲]]<br>[[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260709天赐材料_财报穿透与公募挤兑假设校验]]<br>[[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260709天赐材料_雪球电解液之王逻辑链与证据更新]]<br>[[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260717天赐材料_资金承接与最佳赔率监控]]<br>[[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/260722天赐材料_证据状态刷新]] |
| `state_next_questions` | 1 | [[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/next_questions]] |
| `state_next_signals` | 1 | [[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/天赐材料/next_signals]] |
| `state_research_task` | 1 | [[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/research_task]] |
| `superseded_scorecard` | 1 | [[兴趣领域/股票投资/归档/AI周期探索/02_公司研究/湖南裕能/scorecard]] |

## 权限边界

- Evidence 可以更新研究问题，不能直接生成 `murphy_status: confirmed`。
- `scorecard.md` 属于历史 State / 旧评分，统一 `decision_authority: none`。
- `PROMPT.md` 属于 Automation 模板，不是公司事实。
- `next_questions.md`、`next_signals.md` 和 `research_task.md` 属于会过期的 State。

## 数量快照

```yaml
file_count: 25
role_counts: {'automation_prompt': 1, 'evidence_company_research': 1, 'evidence_log': 2, 'state_next_questions': 1, 'state_research_task': 1, 'superseded_scorecard': 1, 'evidence_or_state_report': 15, 'ai_long_report_original': 2, 'state_next_signals': 1}
```
