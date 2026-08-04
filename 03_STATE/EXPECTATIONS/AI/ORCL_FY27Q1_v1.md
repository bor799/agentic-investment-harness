---
active_expectation:
  forecast_id: EXP-ORCL-260728-01
  forecast_version: v1
  claim_ids: [AI-B01, AI-B02, AI-B04, ORCL-B01, ORCL-B02, ORCL-B03]
  scope: ORCL
  as_of: 2026-07-28
  frozen_as_of: 2026-07-28
  state: frozen
  settlement_date: unknown
  settlement_date_status: not_announced
  settlement_event: next_official_FY27_Q1_results
  expected_window:
    start: 2026-09-01
    end: 2026-10-15
    basis: historical_reporting_cadence_not_official
  review_by: 2026-08-15
  external_consensus: unknown_not_collected
  market_implied_expectation: "截至 2026-07-24 的旧 Current 快照反映增长预期，同时对负自由现金流与融资风险折价；本轮未刷新。"
  decision_authority: none
layer: STATE
primary_role: active_expectation
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
last_reviewer: "PASS | injected | 2026-07-28"
---

# Oracle FY27 Q1 预期 v1

## 结算指标

```yaml
metrics:
  customer_commitment:
    - RPO 与新增合同
    - RPO 转收入节奏
  customer_cash:
    - 可定位的实际客户预付款
    - 可定位的客户供货或客户承担建设成本
  operating:
    - IaaS 与云收入
    - 云利润或可复核的利润留存
    - 经营现金与自由现金
  capacity_financing:
    - debt
    - equity
    - leases
    - supplier_finance
  market_money:
    - 机构持仓与成交
    - 分析师预期修订
    - 估值与相对强弱
```

RPO 只属于 `customer_commitment`，不得计入 `customer_cash`。债务、股权、租赁和供应商融资分别记录，不相互抵消或重复。

## 我们冻结的方向区间

```yaml
own_range:
  stronger: RPO 按披露节奏转为 IaaS/云收入，实际客户资金可定位，经营现金改善快于容量融资成本。
  inline: 收入与合同继续增长，但自由现金仍弱；融资来源可辨认且没有明显恶化每股索取权。
  weaker: RPO 转收入慢于预期，实际客户资金不足，建设更多依赖债务/股权/租赁且现金恶化。
```

## 结算规则

- `stronger`：只支持 ORCL-B02/03 的 proposed update；不自动升级。
- `inline`：保持状态，记录哪一段因果链尚未验证。
- `weaker`：提出 weaken；若只是股价变化，只更新市场预期/赔率。
- 结算根来源只能是 Oracle 正式披露、监管文件或可核验电话会原文。

## 不能证明什么

本预期不证明 Oracle 当前便宜，不提供概率、目标价、仓位或交易授权。

