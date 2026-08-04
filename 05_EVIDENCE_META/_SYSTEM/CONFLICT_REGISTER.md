---
title: conflict_register
date: 2026-07-23
updated: 2026-07-28
layer: META
primary_role: conflict_register
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
supersedes:
  - 05_EVIDENCE_META/META/CONFLICT_REGISTER.md
---

# Conflict Register

## 现存治理冲突

| 冲突 | 当前处理 | 是否暂停 |
|---|---|---|
| 旧“已吸收/最高效力”与新状态冲突 | 旧标签只作 `legacy_status`，不映射 belief state | 否 |
| 旧 Constitution 混入权限和方法 | 原文归档，新 Constitution 只保留 Guardrail + Router | 否 |
| AI 推断与 Murphy 原话混同 | P0 必须逐字 excerpt；AI 摘要 `authority:none` | 否 |
| 单次 Case 生成长期规则 | Case 可形成方法候选，不能直接改道 | 否 |
| 纯 AI 探索更新人格、四票、概率或仓位 | PX 只能保留线索或拒绝 | 否 |
| 混合文件整篇按 P0 | 按段落定权 | 否 |
| P3/PX 转述一手链接后直接升级 | 必须重新打开原文并复算 | 否 |
| 数值口径冲突或时点不一致 | 写 `unknown`，等待统一口径 | 否 |
| ETF 折溢价被写成无风险套利 | 同时核验时点、价差、深度、申赎、费用和到账 | 否 |
| ETF 流入被写成成分公司盈利上修 | 价格/资金只更新 `H_R/H_L` | 否 |
| 新版规则静默覆盖旧版 | 必须写 supersedes、原因、边界和回滚 | 否 |

## 本轮新增冲突

| 冲突 | 当前处理 | 是否暂停 |
|---|---|---|
| 稳定领域 belief 放在会过期的 State | 唯一正文移到 `05/KNOWLEDGE`；`03_STATE/DOMAIN_MODELS` 仅 Outlook | 否 |
| 新旧 Claim/Schema 同时 active | 新 `_SYSTEM` 唯一 active；旧 `META` 只作 superseded 指针 | 否 |
| 漂亮叙事冒充贝叶斯更新 | `ljg-invest` 只生成 read-only projection；更新必须走 `belief_update` | 否 |
| RPO/ARR 被当成现金 | 合同、客户现金、收入、经营现金与融资分账 | 否 |
| Oracle “资金进入”来源含混 | 分开客户承诺、实际客户资金、债务、股权、租赁、供应商融资和市场流 | 否 |
| Nebius 高增长遮蔽建设风险 | 在利用率前单独监控闲置、融资与每股摊薄 | 否 |
| 价格上涨被当经营验证 | 只能更新市场预期、`H_R/H_L` | 否 |
| 正式融资被当客户需求 | 只能更新融资能力和资本成本 | 否 |

## AI 权限

AI 可以读取、关联、反证、计算、记录、提出 `belief_update` 和维护来源审计。AI 不得自行定义 Murphy 的稳定哲学、确认 `murphy_confirmed`、应用 `proposed_state`、修改资本参数或在券商回报缺失时改变成交/持仓主账。

