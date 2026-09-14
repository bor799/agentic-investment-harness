---
title: company_fundamentals
date: 2026-07-23
updated: 2026-07-24
layer: METHOD
primary_role: company_fundamentals
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: operational
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260630财报季_经营验证与定时任务体系.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/稳定币与财务指标概念路径.md
---

# COMPANY_FUNDAMENTALS

## 职责

公司怎么真正赚钱。`ljg-invest` 在本 Skill 内只作为 Business Engine 镜头：
解释客户为何付钱、赚钱机制、竞争优势、再投资和机器失效条件，再用财务事实验证
利润、现金与每股价值。它不判断市场是否错定价，不给资本动作或金额建议。

## 输入

客户付费、赚钱机制、收入、直接成本、毛利、经营费用、经营利润、净利润、现金流、
股数、资本配置、主要持有人与管理层历史承诺。

## 输出

商业机器判断、关键命题证据表、证据缺口和反证。只有进入个股投资判断时，才把这些
输出交给决策合同形成 `H_B`；完成公司研究不自动代表 `H_B: pass`。

## 不能证明什么

高收入、高增长、好创始人、飞轮叙事或知名持有人都不能替代股东现金，也不能直接
证明当前价格有赔率。

## 失败条件

客户付费不能穿透为利润和现金，竞争或资本投入使机器反向旋转，或每股价值被稀释。

## Business Engine

先用一句话说清“谁为什么付钱，公司怎样留下钱”，再检查：

- 赚钱机制是否已经运行，还是只有结构想象；
- 竞争优势如何形成，冲击后变强还是变弱；
- 利润再投资能否转成新收入、效率或壁垒；
- 哪个变量会让机器停转或反向旋转。

飞轮是可选机制，不是所有公司的硬门。资源周期公司、公用事业和资本结构载体按真实
收益结构验证，不能因“没有飞轮”直接判定失败。

## 股东结构

首次研究经营公司时检查主要持有人、创始人或产业资本、控制权、融资与稀释；后续只在
新披露或相关风险变化时做差分更新。每条变化必须同时记录：

```yaml
ownership_change:
  position_as_of:
  disclosed_at:
  shares_change:
  ownership_percentage_change:
  market_value_change:
  capital_type:
  inferred_motive: unknown
```

股数、持股比例和市值变化必须分开。被动配置、主动策略、组合对冲和期限约束不得混为
同一种资本；公开披露不能证明实时资金流或持有人真实动机。资本性质可以生成控制权、
融资或拥挤问题，但不能直接提高 `H_B`。

## 管理层核验

财报和公告中的经营事实应尽早读取；先形成独立的 Business Engine 与毁损变量判断，
再核对管理层对未来的解释。只检查三件事：增长来自哪里、承认了什么风险、过去承诺
兑现了多少。管理层叙事是待验证解释，不是根证据的替代品。

风险、管理层和多空材料共用一张证据表，不重复写三套报告：

| 关键命题 | 支持事实 | 最强反证或替代解释 | 下一判定事件 |
|---|---|---|---|

只保留能改变结论的命题，致命问题最多三个且不凑数；同一根来源只计一次。

## 执行步骤

1. **收入：**谁付款，为什么现在付款，收入是一次性、周期性、总额法还是净额法。
2. **直接成本：**这笔收入最先被什么成本吃掉，成本随规模上升还是下降。
3. **毛利 / 类毛利：**收入扩大后，毛利率是否改善，还是只是在做低留存流水。
4. **经营费用：**销售、研发、管理和股份支付是否吞掉毛利。
5. **经营利润：**增长是否已经穿透到经营利润，而不是只停在调整后指标。
6. **净利润：**净利润是否来自主业，还是来自公允价值、一次性收益、汇率或会计处理。
7. **经营现金流：**经营现金流，也就是公司日常生意真正流进来的现金，是否跟利润同向。
8. **自由现金流：**资本开支后是否还剩现金；高增长是否需要持续融资。
9. **每股价值：**股数、SBC、可转债、权证和融资是否稀释股东。
10. **估值接口：**把上述结果交给 [[02_术/SKILLS/EXPECTATIONS_VALUATION]]。

## 财报季经营验证

财报不是开奖，而是经营假设的定期验收。财报前 7 到 14 天先冻结验证基线，不猜单季数字，不因“可能超预期”提前扩大风险。

财报前必须写清：

```yaml
earnings_baseline:
  business_focus_last_1_to_2_years:
  next_customer_bottleneck:
  bottleneck_control:
  profit_pool_quality:
  competition_or_new_order:
  validation_conditions:
  neutral_conditions:
  failure_conditions:
  do_not_chase_condition:
```

财报发布后 24 小时内，只做差分，不重写故事。实际结果逐项对照财报前基线，检查：

| 层级 | 验证数字 |
|---|---|
| 收入 | 总收入、分部收入、订单、ARR、GMV、ASP、出货、使用量 |
| 直接成本 | 原材料、产能利用率、云/算力、履约、渠道、项目交付成本 |
| 毛利 | 毛利率、take rate、价差、单位经济 |
| 经营费用 | 销售、研发、管理、补贴、SBC |
| 经营利润 | GAAP/IFRS 经营利润、调整后口径差异 |
| 现金流 | 经营现金流、自由现金流、应收、库存、合同负债、资本开支 |

财报后只允许四种经营结论：

1. **经营验证增强：**方向、瓶颈控制和利润留存同时改善。
2. **经营验证维持：**核心方向未坏，但报表仍处投入或转化期。
3. **经营验证转弱：**收入或订单尚可，但毛利、费用、现金流或竞争结构恶化。
4. **经营假设失败：**失败条件被触发，原逻辑不能再靠“长期”解释。

资本动作必须同时满足经营证据、价格赔率、周期和资本纪律。财报超预期不等于可以追，财报后下跌也不等于可以抄底。

## 财报季研究任务接口

每日哨兵只检查正式财报日期、交易所/监管披露、公司 IR、业绩预告和已发布财报；不能用新闻热度替代公告。

每周未来 30 天验证准备会，回答哪些标的即将进入财报窗口、哪些基线不完整、哪些瓶颈有高毛利潜力但尚未进报表、哪三个标的最值得补证据、哪些标的即使财报很好也不应追价。

月度经营方向与资本配置会只形成研究优先级和六档动作候选，不更新仓位。每一次资本投入都必须写明验证条件、失败条件和下一检查时间。

## 输出格式

```yaml
company_fundamentals:
  business_engine:
    payer_and_reason:
    money_mechanism:
    competitive_advantage:
    reinvestment_conversion:
    break_condition:
  ownership:
    baseline_or_delta:
    position_as_of:
    disclosed_at:
    capital_type:
    control_financing_dilution_effect:
    inferred_motive: unknown
  management_check:
    claimed_growth_source:
    admitted_risks:
    promise_delivery_record:
  revenue_quality:
  direct_cost_pressure:
  gross_margin_or_take_rate:
  operating_leverage:
  net_income_quality:
  operating_cash_flow:
  capex_and_free_cash_flow:
  dilution:
  disputed_claims: []
  H_B: pass | mixed | fail | unknown
  next_number:
  what_would_prove_wrong:
```

## 典型伪证据

| 伪证据 | 为什么不够 |
|---|---|
| 收入高增长 | 可能没有毛利，或费用更快增长 |
| TAM 很大 | 不证明公司能收费，也不证明股东能留下钱 |
| 调整后 EBITDA | 可能排除了真实成本、SBC 或资本开支 |
| 客户预付款 | 可能是融资路径，不是成熟经营造血 |
| 回购授权 | 授权不等于已经执行，也不等于业务改善 |
| 裁员 | 可能是主动提效，也可能是增长压力 |
| 创始人可信 | 只能生成持续性假设，必须由数字验证 |

## 概念到财务路径

解释任何行业词或财务词时，必须回答：

```text
这个词是什么
→ 在商业流程哪个环节
→ 影响收入、毛利、经营费用、净利润、现金流还是估值
→ 对应哪家公司或哪类业务
→ 投资者应该看哪个验证数字
```

例如 `net revenue` 是净收入，不是净利润；`Adjusted EBITDA` 是经营质量辅助指标，不代表自由现金流；`digital asset sales` 可能是交易过账收入，收入巨大但真实留存很薄。所有概念都要落回收入、成本、费用、利润和现金流。

## 与其他 Skill 的接口

- 供需和付款人不清楚时，先回 [[02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND]]。
- 高增长、未盈利、重 CapEx 或严重稀释时，加跑 [[02_术/SKILLS/GROWTH_TECH]]。
- 公司事实过票后，才能进入 [[02_术/SKILLS/EXPECTATIONS_VALUATION]]。

## 旧分析报告方法源吸收记录

已吸收 `260630财报季_经营验证与定时任务体系.md` 的财报前基线、财报后差分、四种经营结论和三类财报季研究任务。旧文中的资本动作表统一改写为当前六档动作和四票承保，不授权自动交易。

## 旧基础概念方法源吸收记录

已吸收 `稳定币与财务指标概念路径.md` 的概念到财务路径规则。后续解释行业词和财务词，不只写百科定义，必须说明它如何变成收入、如何被成本吃掉、最后能不能留下利润和现金。
