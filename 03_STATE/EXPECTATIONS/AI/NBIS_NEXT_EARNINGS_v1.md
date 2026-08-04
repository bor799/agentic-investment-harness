---
active_expectation:
  forecast_id: EXP-NBIS-260728-01
  forecast_version: v1
  claim_ids: [AI-B04, NBIS-B01, NBIS-B02, NBIS-B03]
  scope: NBIS
  as_of: 2026-07-28
  frozen_as_of: 2026-07-28
  state: frozen
  settlement_date: unknown
  settlement_date_status: not_announced
  settlement_event: next_official_quarterly_results
  expected_window:
    start: 2026-08-01
    end: 2026-09-30
    basis: historical_reporting_cadence_not_official
  review_by: 2026-08-15
  external_consensus: unknown_not_collected
  market_implied_expectation: "截至 2026-07-24 的旧 Current 快照已包含高速增长预期；本轮未刷新价格、共识或估值分母。"
  decision_authority: none
layer: STATE
primary_role: active_expectation
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
last_reviewer: "PASS | injected | 2026-07-28"
---

# Nebius 下一次财报预期 v1

## 结算指标

```yaml
metrics:
  customer_commitment:
    - 锚定客户合同
    - ARR
  customer_cash:
    - 可定位的实际客户付款
  operating:
    - ARR 转收入
    - 已交付容量与利用率
    - AI 云毛利/经营利润
    - 经营现金
  capacity_financing:
    - existing_cash
    - debt_or_project_finance
    - equity_and_dilution
    - leases
  market_money:
    - 机构持仓与成交
    - 分析师预期修订
    - 估值与相对强弱
```

ARR 与锚定客户承诺不是客户现金。存量现金、债务/项目融资、股权和租赁分别记录。

## 我们冻结的方向区间

```yaml
own_range:
  stronger: ARR 持续转收入，锚定客户与容量利用率同步提高，AI 云利润改善且后续摊薄受控。
  inline: 收入延续增长，但利用率或利润仍缺披露；建设主要由存量现金承担，未出现新的结构性恶化。
  weaker: 容量上线快于客户使用，ARR 转收入/利润弱，建设继续依赖大额融资或摊薄。
```

## 结算规则

- `stronger`：分别判断需求、利用率、利润和融资，不能“一次财报全部升级”。
- `inline`：保持状态，列下一项可解决 unknown。
- `weaker`：提出对应 claim 的 weaken；市场价格只更新市场预期/赔率。
- 结算根来源只能是 Nebius 正式披露、监管文件或可核验电话会原文。

## 不能证明什么

本预期不证明 Nebius 当前估值有吸引力，不提供概率、目标价、仓位或交易授权。

