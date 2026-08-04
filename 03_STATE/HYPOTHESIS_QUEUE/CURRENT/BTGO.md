---
current_thesis_state:
  target_id: BTGO
  target_name: BitGo Holdings
  domain_ids: [STABLECOIN_CRYPTO_INFRA]
  pattern_ids_relevant: [SCI-P01]
  orientation_status: retrospectively_mapped
  data_cutoff: 2026-07-24
  expires_at: 2026-10-22
  review_date: 2026-08-24
  money_source: "基本面 + 风险偏好"
  H_B: "fail：26Q1调整后EBITDA为负，多个收入环节尚未证明可留下利润"
  H_R: "unknown：2026-07-24收盘4.82美元，但短上市历史和不稳定单位经济无法可靠反推"
  H_L: "warn：交易、质押和资产价格受加密周期驱动"
  H_C: "unknown：当前Portfolio Ledger没有券商持仓、总资本和最大损失事实"
  odds_calibration: bounded_unknown
  asset_conclusion: 等待
  key_evidence:
    - "26Q1收入37.74亿美元，但直接成本37.25亿美元｜BitGo Q1结果"
    - "调整后EBITDA为-170万美元，上年同期为正｜BitGo Q1结果"
    - "稳定币服务收入3820万美元、直接成本3530万美元｜BitGo Q1结果"
  missing_evidence:
    - "稳定币、交易与托管的可重复贡献利润"
    - "经营现金流与完全摊薄股数"
  failure_condition: "收入增长继续不能带来正调整后EBITDA和经营现金流"
  refresh_trigger: "下一季度调整后EBITDA与经营现金流同时转正"
  allowed_action: "若唯一触发得到验证且H_C完成校准，则允许继续观察。"
  open_disagreement: none
  source_paths:
    - "05_EVIDENCE_META/EVIDENCE/THEMES/260726稳定币与加密基础设施_CurrentThesis重置证据.md"
    - "https://investors.bitgo.com/financials/quarterly-results/default.aspx"
    - "https://www.nasdaq.com/market-activity/stocks/btgo/historical"
  last_reviewer: "PASS | independent_readonly | 2026-07-26"
---

# BitGo Current Decision Card

今天发生了什么：BitGo 收入很大，但大部分是低毛利资产销售，调整后 EBITDA 已转负。为什么重要：规模不等于收费权。现在做什么：等待，当前不投入。

## 当前判断

- **结论：等待。当前六档动作：不投入。**
- **核心赚钱路径：** 托管、交易、质押和稳定币服务形成可重复高毛利收入。
- **十年方向：** 机构数字资产托管与结算需求增长。
- **三年路径：** 从资产销售规模转向平台费率与客户留存。
- **一年兑现：** EBITDA 与经营现金流转正，才有讨论 30% 回报的基础。
- **市场隐含预期：** 4.82 美元、约 5.6 亿美元市值看似不贵，但盈利分母不稳定，赔率只能 bounded unknown。

## 胜率与赔率

- **主观胜率：30%–40%。** 上界依据是客户增长和多条业务线；下界依据是负 EBITDA、staking 下滑与很薄的稳定币贡献。
- **Bull：** 单位经济快速修复，约 +50% 至 +75%。
- **Base：** 收入增长但利润不明显，约 -10% 至 +10%。
- **Bear：** 加密活动下降，约 -60% 至 -45%。

区间不是统计频率，不进入 EV、仓位或交易授权。

## 纪律

- **最大反方证据：** 26Q1 近 37.7 亿美元收入只留下约 4900 万美元毛贡献，调整后 EBITDA 为负。
- **退出条件：** 收入增长继续不能带来正 EBITDA 和经营现金流。
- **下一项验证：** 下一季度调整后 EBITDA 与经营现金流同时转正。
- **授权边界：** H_B 未通过，价格再低也不能增加风险。

