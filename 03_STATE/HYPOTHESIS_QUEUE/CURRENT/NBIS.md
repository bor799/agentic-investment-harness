---
current_thesis_state:
  target_id: NBIS
  target_name: Nebius
  domain_ids: [AI]
  pattern_ids_relevant: [AI-P01]
  orientation_status: retrospectively_mapped
  data_cutoff: 2026-07-24
  expires_at: 2026-10-22
  review_date: 2026-08-24
  money_source: "基本面 + 风险偏好"
  H_B: "unknown：收入与ARR高速增长，但重资本回报和自由现金流尚未证明"
  H_R: "fail：2026-07-24收盘187.77美元，约477亿美元市值，相当于约14–16倍FY26收入指引"
  H_L: "warn：AI基础设施融资、客户集中与供给扩张处于高波动阶段"
  H_C: "unknown：当前Portfolio Ledger没有券商持仓、总资本和最大损失事实"
  odds_calibration: calibrated
  asset_conclusion: 等待
  key_evidence:
    - "26Q1 AI云收入3.897亿美元，同比增长841%｜Nebius Q1报告"
    - "ARR为19.2亿美元，FY26收入指引30–34亿美元｜Nebius Q1报告"
    - "期后现金约93亿美元，但扩张仍需大额资本开支｜Nebius Q1报告"
  missing_evidence:
    - "ARR向收入和现金流的转化"
    - "完全摊薄后每股价值与后续融资"
  failure_condition: "ARR增长未转成收入和AI云利润，且资本开支继续依赖大额股权融资"
  refresh_trigger: "下一期ARR转收入、AI云EBITDA与资本开支融资同时证明增长不依赖继续摊薄"
  allowed_action: "若唯一触发得到验证且H_C判定为pass，则允许建立验证仓。"
  open_disagreement: none
  belief_refs:
    - AI-B04
    - NBIS-B01
    - NBIS-B02
    - NBIS-B03
  forecast_ref: "03_STATE/EXPECTATIONS/AI/NBIS_NEXT_EARNINGS_v1.md"
  source_paths:
    - "05_EVIDENCE_META/EVIDENCE/THEMES/260726AI基础设施_CurrentThesis重置证据.md"
    - "https://assets.nebius.com/assets/6fc0ea6c-0884-4a1f-bed8-1f797eb9628f/Financial%20results_Q1%202026.pdf"
    - "https://www.nasdaq.com/market-activity/stocks/nbis/historical"
  last_reviewer: "PASS | independent_readonly | 2026-07-26"
---

# Nebius Current Decision Card

今天发生了什么：Nebius 的 AI 云收入与 ARR 高速增长。为什么重要：当前市值已经要求它快速把合同变成收入和现金流。现在做什么：等待。

## 当前判断

- **结论：等待。当前六档动作：继续观察。**
- **核心赚钱路径：** 新增算力被客户快速使用，ARR 转收入，规模效应覆盖资本开支。
- **十年方向：** AI 原生云基础设施需求增长。
- **三年路径：** 数据中心与电力扩张，形成较高利用率和可重复利润。
- **一年兑现：** FY26 收入与 ARR 向已交付容量、利用率、AI 云利润和每股现金穿透。
- **市场隐含预期：** 187.77 美元、约 477 亿美元市值，对应约 14–16 倍 FY26 收入指引，市场已计入高速兑现。

## 冻结预期与更新

- 领域 belief：[[05_EVIDENCE_META/KNOWLEDGE/DOMAINS/AI/README]]
- Nebius entity belief：[[05_EVIDENCE_META/KNOWLEDGE/ENTITIES/COMPANIES/NBIS]]
- 财报前冻结基线：[[03_STATE/EXPECTATIONS/AI/NBIS_NEXT_EARNINGS_v1]]

本卡不再填写未校准主观胜率或 Bull/Base/Bear 涨跌区间。需求、利用率、利润和融资必须分开更新，不能一次财报整体加权。

## 纪律

- **最大反方证据：** 公司仍是重资本模式，当前估值已提前买入 2026–2027 年增长。
- **退出条件：** ARR 不再转收入，且资本开支继续依赖大额摊薄。
- **下一项验证：** 下一期 ARR 转收入、AI 云 EBITDA 与资本开支融资同时证明增长不依赖继续摊薄。
- **授权边界：** H_C 未知，不增加风险。
