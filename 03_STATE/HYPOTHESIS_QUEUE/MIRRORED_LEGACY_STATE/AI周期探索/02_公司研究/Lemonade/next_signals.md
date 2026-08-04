---
title: "next_signals"
date: 2026-07-24
updated: 2026-07-24
layer: STATE
primary_role: legacy_company_question_state
status: superseded
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
legacy_metadata_added: true
legacy_path: "AI周期探索/02_公司研究/Lemonade/next_signals.md"
migration_target: "03_STATE/HYPOTHESIS_QUEUE"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Lemonade Next Signals (v2 cross-market loop, refreshed 2026-07-22)

> 本文件取代旧 `next_questions.md` 作为 v2 循环的 canonical signal tracker。旧文件保留为历史索引。
>
> **2026-07-22 attempt 2（run_token 25c5d60f）同日重试结果**：未发现新增独立根证据，所有已验证/仍待验证/失败条件/升级条件均与 attempt 1 一致；下复查日仍为 2026-07-29（Q2 2026 财报后）。本文件其他内容未经改动。
>
> **2026-07-22 attempt 3（run_token 220b54a6）同日重试结果（初次 + 两次重试上限）**：仍未发现新增独立根证据；Q2 2026 财报仍定档 7/29，SEC EDGAR / Lemonade IR 无新 8-K 或 10-Q，股价 ~$67.45 在 attempt 2 抓取值噪音范围内。边际信息（Vermont 州 renters 扩展 2026-07-07、再保 cede rate ~18%）属 attempt 1 已记录扩张节奏与 Q1 电话会议已披露再保策略的延续，不构成新独立根，不改变任何票。四票状态与 attempt 1/2 完全一致：H_B unknown / H_R fail, down / H_L pass / H_C pass。**判断未变，动作仍为 `不加仓`**。对象进入 `completed`，等待 2026-07-29 Q2 2026 财报硬触发或下一轮 v2 循环认领。本文件其他内容未经改动。

## 已验证（截至 2026-07-22）

| 信号 | 状态 | 数据日 | 来源 |
|---|---|---|---|
| Q1 2026 GLR 62% (+10pp vs Q4 52%) | 已确认（核心担忧） | 2026-05-06 10-Q | Q1 2026 10-Q + 财报会 |
| Q1 2026 CAT impact 5% | 已确认 | 2026-05-06 10-Q | Q1 2026 财报会 |
| Q1 2026 prior period development 3% (vs Q4 9%) | 已确认 | 2026-05-06 10-Q | Q1 2026 财报会 |
| Q1 2026 Adj EBITDA -$17M（同比改善 64%） | 已确认 | 2026-05-06 10-Q | Q1 2026 10-Q |
| Q1 2026 IFP $1.33B（+32% YoY） | 已确认 | 2026-05-06 10-Q | Q1 2026 10-Q |
| Q1 2026 Revenue $258M（+71% YoY，受再保过渡放大） | 已确认 | 2026-05-06 10-Q | Q1 2026 10-Q |
| FCF 连续四季为正（截至 Q1 2026） | 已确认 | 2026-05-06 10-Q | Q1 2026 财报会 |
| 宠物险 IFP $500M 里程碑 | 已确认 | 2026-05-06 | Q1 2026 财报会 |
| Hannover Re $250M Growth Financing Agreement 签署 | 已确认（6/22 签，6/24 8-K 披露） | 2026-06-22 / 2026-06-24 | 8-K + Lemonade IR Filings |
| 再保 cede rate 从 55% 峰值降至约 30% | 已确认（截至 Q1 2026 电话会议） | 2026-05-06 | Q1 2026 财报会 |

## 仍待验证（核心证据缺口，按优先级）

| # | 待验证信号 | 为什么关键 | 验证窗口 | 验证来源 |
|---|---|---|---|---|
| 1 | Q2 2026 GLR 是否回到 < 60%（剥离 CAT 后 run-rate） | 决定 H_B 能否从 unknown 升级；决定 AI 定价→承保利润传导是否成立 | 2026-07-29 Q2 财报 | Q2 10-Q + 电话会议 |
| 2 | Q2 2026 FCF 是否维持为正 | 决定盈利路径是否仍按轨道 | 2026-07-29 | Q2 10-Q 现金流量表 |
| 3 | Q2 2026 调整 EBITDA 与全年指引 | 是否再次上调决定管理层信心 | 2026-07-29 | Q2 财报会 |
| 4 | Hannover Re 协议完整文本（covenants / termination triggers / cohort 定义） | 决定 H_L 是否有隐藏约束；决定 cohort-level 数据可用性 | Q2 10-Q 备案时（~2026-08） | Q2 10-Q Exhibit |
| 5 | Cohort-level GLR（被 Hannover Re 选中的 cohort vs 存量） | 决定协议是"专业第三方正面背书"还是"高利率下接受高风险敞口" | Q2 电话会议或后续披露 | 电话会议 / 10-Q |
| 6 | 车险 IFP 增长与车险 GLR 分项 | 决定增长是否以承保质量恶化为代价 | Q2 10-Q | 10-Q 分项数据 |
| 7 | 综合成本率从 138% 的改善路径 | 决定何时接近承保利润 | Q2 / 后续季度 | 10-Q |
| 8 | 宠物险 $500M IFP 后的盈利能力 | 决定新增长引擎是否真盈利 | 后续季度披露 | 财报会 |
| 9 | 股权激励 $95M 全年指引对稀释率的影响 | 决定 H_R 的潜在稀释压力 | Q2 / Q3 | 10-Q |
| 10 | 车险州扩展节奏 | 决定最大市场的增长斜率 | 持续监控 | 公司公告 |

## 失败条件（任一触发 → 降级或退出）

- Q2 2026 GLR 维持 65%+（连续两季高位，确认结构性恶化）
- Q2 2026 FCF 转负
- Q2 2026 调整 EBITDA 转正目标被推迟
- 车险 IFP 高增长但车险 GLR 显著恶化（产品线污染）
- Hannover Re 协议在 2027 提款前被终止或大幅削减
- 重大监管行动或巨灾导致 solvency 受威胁
- 出现重大审计或治理异常

## 升级条件（任一触发 → 重新评估升级）

- Q2 2026 GLR 回到 60% 以下，且剥离 CAT 后 run-rate GLR 趋势性下行
- Q2 2026 FCF 继续为正且环比改善
- Cohort-level GLR 数据显示 Hannover Re 选中的新 cohort 显著优于存量
- 车险产品线扩展至更多州且车险 GLR 改善
- 调整 EBITDA 转正时间表提前

## 下一复查日

- **硬触发**：2026-07-29（Q2 2026 财报发布后立即刷新）
- **次硬触发**：2026-08（Q2 10-Q 完整备案后，特别检查 Hannover Re 协议 Exhibit）
- **软触发**：2026-11-17 Investor Day 前后
- **常规刷新**：每季度财报后

## 本轮已检查的根来源清单

1. Lemonade IR / Filings 页（https://www.lemonade.com/investor/filings）
2. Lemonade IR Q2 2026 业绩公告（https://www.lemonade.com/investor/news/lemonade-to-announce-second-quarter-2026-financial-results）
3. Lemonade IR Maine 扩张公告（https://www.lemonade.com/investor/news/lemonade-expands-renters-insurance-to-maine）
4. Minichart 8-K 摘要（仅作 8-K 内容索引，非独立根）
5. Yahoo Finance LMND 行情（仅用于 H_R/H_L）
