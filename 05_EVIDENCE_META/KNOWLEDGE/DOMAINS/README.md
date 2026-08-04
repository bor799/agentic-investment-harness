---
title: 领域判断地图
date: 2026-07-28
updated: 2026-07-28
layer: KNOWLEDGE
primary_role: domain_map_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
research_authority: structural_prior_only
---

# 领域判断地图

这里不是报告目录，而是新标的到来时调用的长期语义记忆。

| 领域 | 60 秒先识别什么 | 当前合格模式 |
|---|---|---:|
| [[05_EVIDENCE_META/KNOWLEDGE/DOMAINS/AI/README\|AI]] | 需求能否穿透合同、利润、现金与资本回报 | 1 |
| [[05_EVIDENCE_META/KNOWLEDGE/DOMAINS/ENERGY_STORAGE_MATERIALS/README\|储能材料]] | 量、价、单吨利润和现金是否共同改善 | 0 |
| [[05_EVIDENCE_META/KNOWLEDGE/DOMAINS/CHINA_INTERNET/README\|中国互联网]] | 产品是否买对，以及平台盈利是否有广度 | 1 |
| [[05_EVIDENCE_META/KNOWLEDGE/DOMAINS/CONSUMER_IP/README\|消费与 IP]] | 热度和扩张能否变成周转、利润与自由现金 | 1 |
| [[05_EVIDENCE_META/KNOWLEDGE/DOMAINS/INNOVATIVE_DRUGS/README\|创新药]] | 合同 headline 能否变成现金与管线价值 | 0 |
| [[05_EVIDENCE_META/KNOWLEDGE/DOMAINS/STABLECOIN_CRYPTO_INFRA/README\|稳定币与加密基础设施]] | 先分清收费池、利率敏感性和普通股索取权 | 1 |
| [[05_EVIDENCE_META/KNOWLEDGE/DOMAINS/RESOURCES_POWER_GRID/README\|资源、电力与电网]] | 同一宏观需求如何进入不同资产的钱路 | 1 |

`0` 表示证据不足，不是领域没有价值。没有合格模式时，结构先验必须返回
`unknown`，继续读取 Current 与新 Source。

领域地图没有四票、价格、仓位或交易权限。
