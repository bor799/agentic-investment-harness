---
title: domain_failure_postmortems
date: 2026-07-28
updated: 2026-07-28
layer: CASE
primary_role: domain_failure_postmortem_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
---

# Domain Failure Post-Mortems

领域或实体 belief 结算失败时，错误只归到以下一项或多项：

- `mechanism`：因果机制不存在；
- `transmission`：需求没有传到公司；
- `magnitude`：方向对，强度不够；
- `timing`：方向对，兑现晚于持有期；
- `market_expectation`：现实没有优于市场预期；
- `valuation`：价格透支；
- `execution`：公司交付、利用率、成本或融资失败；
- `unresolved`：证据仍不能区分解释。

Post-Mortem 必须引用 `claim_id`、`forecast_id`、根来源、旧状态、实际结果和下一条修正规则。它不能直接修改 `01_道`、`02_术` 或资本动作。

