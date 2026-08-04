---
current_thesis_state:
  target_id: MSTR
  target_name: Strategy
  domain_ids: [STABLECOIN_CRYPTO_INFRA]
  pattern_ids_relevant: [SCI-P01]
  orientation_status: retrospectively_mapped
  data_cutoff: 2026-07-24
  expires_at: 2026-10-22
  review_date: 2026-08-24
  money_source: "流动性 + 风险偏好"
  H_B: "fail：软件经营现金流不足以独立覆盖优先股、债务和BTC资本结构"
  H_R: "unknown：2026-07-24收盘92.93美元，BTC资产、优先索取权与潜在摊薄使普通股赔率不稳定"
  H_L: "warn：BTC价格、融资窗口与风险偏好共同驱动"
  H_C: "unknown：当前Portfolio Ledger没有券商持仓、总资本和最大损失事实"
  odds_calibration: bounded_unknown
  asset_conclusion: 等待
  key_evidence:
    - "2026-07-05持有843775枚BTC，成本约636.9亿美元｜Strategy 8-K"
    - "美元储备25.5亿美元，用于优先股分配与债务利息｜Strategy 8-K"
    - "公司已建立最高12.5亿美元BTC变现容量补充美元储备｜Strategy 8-K"
  missing_evidence:
    - "完全摊薄普通股、优先股和债务的实时索取权"
    - "非稀释性现金流覆盖固定支付的能力"
  failure_condition: "公司持续出售BTC或发行普通股覆盖优先股分配与利息"
  refresh_trigger: "不再需要出售BTC支付优先股分配，且美元储备可由非稀释性现金流覆盖"
  allowed_action: "若唯一触发得到验证且H_C完成校准，则允许继续观察。"
  open_disagreement: none
  source_paths:
    - "05_EVIDENCE_META/EVIDENCE/THEMES/260726稳定币与加密基础设施_CurrentThesis重置证据.md"
    - "https://www.sec.gov/Archives/edgar/data/1050446/000119312526295586/mstr-20260706.htm"
    - "https://www.nasdaq.com/market-activity/stocks/mstr/historical"
  last_reviewer: "PASS | independent_readonly | 2026-07-26"
---

# Strategy Current Decision Card

今天发生了什么：Strategy 持有大量 BTC，也需要美元储备覆盖优先股与债务。为什么重要：普通股不是对 BTC 的简单一比一索取权。现在做什么：等待，当前不投入。

## 当前判断

- **结论：等待。当前六档动作：不投入。**
- **核心赚钱路径：** BTC 上涨与融资溢价使每股 BTC 增加，且不被优先权和摊薄吃掉。
- **十年方向：** BTC 稀缺资产与资本市场包装。
- **三年路径：** 在融资窗口开放时持续滚动资本结构。
- **一年兑现：** BTC 大涨且普通股融资仍具溢价，才可能超过 30%。
- **市场隐含预期：** 92.93 美元附近的普通股价值必须分层扣除债务、优先股和潜在摊薄，不能只看 BTC 市值。

## 胜率与赔率

- **主观胜率：35%–45%。** 上界依据是 BTC 弹性和资产规模；下界依据是优先索取权、摊薄与资产变现。
- **Bull：** BTC 与融资溢价共振，约 +50% 至 +80%。
- **Base：** BTC 横盘、融资继续，约 -10% 至 +10%。
- **Bear：** BTC 下跌且融资窗口关闭，约 -65% 至 -45%。

区间不是统计频率，不进入 EV、仓位或交易授权。

## 纪律

- **最大反方证据：** 公司允许出售 BTC 补充支付优先股分配和利息的美元储备。
- **退出条件：** 持续出售 BTC 或发行普通股覆盖固定支付。
- **下一项验证：** 不再需要出售 BTC 支付优先股分配，且美元储备可由非稀释性现金流覆盖。
- **授权边界：** 这是 BTC 杠杆与资本结构载体，不是稳定币经营公司。

