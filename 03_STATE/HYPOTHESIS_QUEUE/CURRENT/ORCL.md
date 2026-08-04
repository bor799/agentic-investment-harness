---
current_thesis_state:
  target_id: ORCL
  target_name: Oracle
  domain_ids: [AI]
  pattern_ids_relevant: [AI-P01]
  orientation_status: retrospectively_mapped
  data_cutoff: 2026-07-24
  expires_at: 2026-10-22
  review_date: 2026-08-24
  money_source: "基本面 + 认知差"
  H_B: "pass：IaaS、云收入与RPO均已形成独立经营增量"
  H_R: "pass：2026-07-24收盘114.99美元，约14.3倍FY27非GAAP EPS指引"
  H_L: "warn：AI资本开支、融资与客户合同兑现仍在高波动阶段"
  H_C: "unknown：当前Portfolio Ledger没有券商持仓、总资本和最大损失事实"
  odds_calibration: calibrated
  asset_conclusion: 可买
  key_evidence:
    - "FY26收入674亿美元，IaaS收入181亿美元、同比增长77%｜Oracle FY26结果"
    - "RPO为6380亿美元，其中750亿美元GPU相关合同由客户预付或供货｜Oracle FY26结果"
    - "FY26经营现金流320亿美元，但自由现金流为-237亿美元｜Oracle FY26结果"
  missing_evidence:
    - "FY27 Q1合同转收入、IaaS增速与自由现金流"
    - "当前个人账户H_C"
  failure_condition: "RPO转收入连续低于公司指引，同时新增融资后自由现金流继续恶化"
  refresh_trigger: "FY27 Q1披露的云/IaaS增长、RPO转收入与自由现金流"
  allowed_action: "若FY27 Q1兑现指引且H_C由当前账户事实判定为pass，则允许建立验证仓。"
  open_disagreement: none
  belief_refs:
    - AI-B01
    - AI-B02
    - AI-B04
    - ORCL-B01
    - ORCL-B02
    - ORCL-B03
  forecast_ref: "03_STATE/EXPECTATIONS/AI/ORCL_FY27Q1_v1.md"
  source_paths:
    - "05_EVIDENCE_META/EVIDENCE/THEMES/260726AI基础设施_CurrentThesis重置证据.md"
    - "https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/"
    - "https://www.nasdaq.com/market-activity/stocks/orcl/historical"
  last_reviewer: "PASS | independent_readonly | 2026-07-26"
---

# Oracle Current Decision Card

今天发生了什么：Oracle 已经把 AI 云需求变成收入和合同。为什么重要：一年回报取决于这些合同能否覆盖资本开支与融资成本。现在做什么：资产层可买，个人账户仍继续观察。

## 当前判断

- **结论：可买。当前六档动作：继续观察。**
- **核心赚钱路径：** AI 云合同转成 IaaS 收入，利用率提升后自由现金流转正。
- **十年方向：** 数据库、云和 AI 基础设施融合。
- **三年路径：** RPO 分批转收入，客户预付降低自有资本压力。
- **一年兑现：** FY27 收入与 EPS 指引落地，并证明 RPO、实际客户资金、经营现金与容量融资没有被混为一谈。
- **市场隐含预期：** 114.99 美元约对应 14.3 倍 FY27 非 GAAP EPS；市场相信增长，但仍给负自由现金流折价。

## 冻结预期与更新

- 领域 belief：[[05_EVIDENCE_META/KNOWLEDGE/DOMAINS/AI/README]]
- Oracle entity belief：[[05_EVIDENCE_META/KNOWLEDGE/ENTITIES/COMPANIES/ORCL]]
- 财报前冻结基线：[[03_STATE/EXPECTATIONS/AI/ORCL_FY27Q1_v1]]

本卡不再填写未校准主观胜率或 Bull/Base/Bear 涨跌区间。新材料只能提出定性 `belief_update`，不能机械加总或自动改变本卡。

## 纪律

- **最大反方证据：** RPO 可能更多反映客户预付和资本安排，而不是高回报现金流。
- **退出条件：** RPO 转收入连续低于指引，且新增融资后自由现金流继续恶化。
- **下一项验证：** FY27 Q1 的云/IaaS 增长、RPO 转收入与自由现金流。
- **授权边界：** H_C 未知；“可买”只是资产研究结论，不是 Murphy 的买入授权。
