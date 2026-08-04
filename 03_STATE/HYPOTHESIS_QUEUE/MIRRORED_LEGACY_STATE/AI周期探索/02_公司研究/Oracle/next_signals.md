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
legacy_path: "AI周期探索/02_公司研究/Oracle/next_signals.md"
migration_target: "03_STATE/HYPOTHESIS_QUEUE"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Oracle Next Signals（v2 跨市场循环）

> 由 `next_questions.md` 迁入并扩展。旧文件保留为历史线索，不删除。

## 当前四票状态（截至 2026-07-22）

| 票 | 状态 | 方向 | 关键依据 |
|---|---|---|---|
| `H_B` 经营票 | pass | unchanged | 云 +39%、IaaS +77-93%、RPO $638B、GPU 利用率 97.5% |
| `H_R` 赔率票 | unknown | unchanged | 前瞻 PE ~18 倍看似合理，但 FY26 FCF -$23.7B，净赔率无法确证 |
| `H_L` 周期票 | unknown | unchanged | 大市值流动性深；但 $129.5B 总债务与 FY27 $40B 融资计划带来再融资和稀释风险 |
| `H_C` 仓位票 | unknown | unchanged | 非持仓、非强制读账对象；资本桶和风险簇剩余额度未知 |

## 已验证信号

| 信号 | 数据点 | 来源 | 数据日 |
|---|---|---|---|
| FY26 总收入 | $67.4B，+17% | Oracle IR FY4Q26 公告 | 2026-06 |
| FY26 云收入 | $34.0B，+39% | Oracle IR FY4Q26 公告 | 2026-06 |
| FY26 IaaS | $18.1B，+77%（Q4 +93%） | Oracle IR FY4Q26 公告 | 2026-06 |
| RPO | $638B，+363% | Oracle IR FY4Q26 公告 / 10-K | 2026-06 |
| GPU 利用率 | 97.5% | CEO Q4 电话会 | 2026-06 |
| FY27 收入指引 | $90B，+34% | Oracle IR FY4Q26 公告 | 2026-06 |
| FY27 非 GAAP EPS 指引 | $8.05，+18% | Oracle IR FY4Q26 公告 | 2026-06 |
| FY26 OCF | $32.0B | 10-K | 2026-06 |
| FY26 CapEx | $55.7B | 10-K | 2026-06 |
| FY26 FCF | -$23.7B | 10-K | 2026-06 |
| 总债务 / 近似净债务 | $129.5B / $97.6B | 10-K | 2026-06 |
| FY27 融资计划 | 约 $40B，含 $20B ATM | 管理层指引 | 2026-06 |
| 客户预付（BYOH） | 约 $75B | 管理层披露 | 2026-06 |

## 仍待验证（claim.evidence_gaps）

| 编号 | 信号 | 为什么重要 | 验证方式 | 预期数据日 |
|---|---|---|---|---|
| G1 | RPO $638B 中 12 个月内确认比例 | 判断"合同可见性"能否快速变收入，以及 OpenAI 集中度 | FY27 Q1/Q2 财报附注、管理层电话会 | 2026-09 / 2026-12 |
| G2 | OpenAI/Stargate 合同占 RPO 比例 | 客户集中风险，影响 H_B 单客户依赖判断 | 管理层披露、合同公开备案 | 2026-09+ |
| G3 | FY27 CapEx 节奏（维持/加速/回落） | 判断 FCF 何时转正，以及债务是否继续膨胀 | FY27 各季度现金流量表 | 2026-09+ |
| G4 | $20B ATM 实际发行量与稀释节奏 | 直接影响每股价值，是 H_R 的关键变量 | 10-Q 附注、后续 8-K | 2026-09+ |
| G5 | 客户预付款对 FCF 的真实冲抵 | 判断"不增加负现金流"表述是否成立 | FY27 各季度 OCF 和客户预付负债变化 | 2026-09+ |
| G6 | Moody's / S&P 评级动作 | 融资成本和再融资路径（H_L） | 评级机构公告 | 持续 |
| G7 | OCI SLA 达成率与大客户留存 | OCI 可靠性反证（H_B） | 独立研报、客户反馈、中断事件 | 持续 |
| G8 | Multicloud AI Database 收入基数 | "战略拐点"能否变收入 | 管理层披露 | 2026-09+ |

## 下一硬复查日

- **FY2027 Q1 财报**：预期 2026 年 9 月中旬。同时检查 G1-G5、G7。
- **web 配额恢复后补查**（reset 2026-07-26）：2026-07-01 至今是否有 8-K、IR 新闻稿、Stargate 进展、评级更新。

## 事件触发完整重评

沿用 `260719组合_行为纠偏与资本纪律操作系统` 第七节：财报/指引、客户取消、融资/增发、审计治理异常、周期价差跳变、承诺节点逾期。ORCL 特有触发：
- OpenAI/Stargate 合同变更或取消；
- 评级下调；
- OCI 连续大型中断；
- FY27 指引下修；
- GPU 利用率跌破 90%。
