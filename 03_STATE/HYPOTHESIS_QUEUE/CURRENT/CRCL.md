---
current_thesis_state:
  target_id: CRCL
  target_name: Circle Internet Group
  domain_ids: [STABLECOIN_CRYPTO_INFRA]
  pattern_ids_relevant: [SCI-P01]
  orientation_status: retrospectively_mapped
  data_cutoff: 2026-07-24
  expires_at: 2026-10-22
  review_date: 2026-08-24
  money_source: "基本面 + 流动性"
  H_B: "pass：USDC规模、储备收益与非利息收入均有可验证经营基础"
  H_R: "fail：2026-07-24收盘62.36美元，约155亿美元市值，约为26Q1净利润年化的70倍"
  H_L: "warn：利率、加密周期与监管会显著改变储备收益"
  H_C: "unknown：当前Portfolio Ledger没有券商持仓、总资本和最大损失事实"
  odds_calibration: calibrated
  asset_conclusion: 等待
  key_evidence:
    - "26Q1收入与储备收益6.94亿美元，其中94%来自储备收益｜SEC 10-Q"
    - "USDC期末流通量770亿美元，季度平均增长39.1%｜SEC 10-Q"
    - "分发与交易成本4.07亿美元，Coinbase分成是主要成本｜SEC 10-Q"
  missing_evidence:
    - "降息情景下RLDC与净利润弹性"
    - "非利息收入能否形成更高占比"
  failure_condition: "USDC平均余额和非利息收入不能抵消利率下行与分发成本增长"
  refresh_trigger: "Q2平均USDC、RLDC和非利息收入共同显示降息下利润韧性"
  allowed_action: "若唯一触发得到验证且H_C判定为pass，则允许建立验证仓。"
  open_disagreement: none
  source_paths:
    - "05_EVIDENCE_META/EVIDENCE/THEMES/260726稳定币与加密基础设施_CurrentThesis重置证据.md"
    - "https://www.sec.gov/Archives/edgar/data/1876042/000187604226000150/crcl-20260331.htm"
    - "https://www.circle.com/transparency"
    - "https://www.nasdaq.com/market-activity/stocks/crcl/historical"
  last_reviewer: "PASS | independent_readonly | 2026-07-26"
---

# Circle Current Decision Card

今天发生了什么：USDC 规模仍高，但 Circle 的利润高度依赖利率和分发协议。为什么重要：稳定币增长不等于普通股利润同比例增长。现在做什么：等待。

## 当前判断

- **结论：等待。当前六档动作：继续观察。**
- **核心赚钱路径：** USDC 平均余额增长，净储备收益与非利息收入增长快于分发成本。
- **十年方向：** 合规稳定币成为支付与链上结算基础设施。
- **三年路径：** 收入从储备利差扩展到网络、支付和服务费。
- **一年兑现：** USDC 增长抵消降息，RLDC 和非利息收入提升。
- **市场隐含预期：** 62.36 美元约为 Q1 净利润年化的 70 倍，已要求规模增长和收入多元化。

## 胜率与赔率

- **主观胜率：45%–55%。** 上界依据是 USDC 规模与其他收入翻倍；下界依据是利率敏感、Coinbase 分成和高估值。
- **Bull：** 网络效应扩大，约 +35% 至 +50%。
- **Base：** USDC 增长抵消降息，约 0% 至 +15%。
- **Bear：** 利率与流通量同时下降，约 -45% 至 -30%。

区间不是统计频率，不进入 EV、仓位或交易授权。

## 纪律

- **最大反方证据：** 26Q1 仍有 94% 收入来自储备收益，分发成本吃掉大部分增量。
- **退出条件：** USDC 平均余额和非利息收入不能抵消利率下行与分发成本。
- **下一项验证：** Q2 平均 USDC、RLDC 和非利息收入共同显示降息下利润韧性。
- **授权边界：** 单日 USDC 余额只作时点事实，不能替代季度平均利润；H_C 未知。

