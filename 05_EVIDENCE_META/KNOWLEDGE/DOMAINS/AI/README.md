---
knowledge:
  knowledge_id: DOMAIN-AI
  knowledge_type: domain_pattern_map
  domain_id: AI
  qualified_pattern_ids: [AI-P01]
  candidate_pattern_ids: [AI-C01, AI-C02, AI-C03, AI-C04, AI-C05]
  murphy_confirmed_candidate_ids: [AI-C01, AI-C02]
  decision_authority: none
  research_authority: structural_prior_only
layer: KNOWLEDGE
primary_role: domain_knowledge
status: active
authored_by: human_ai
source_type: P3
human_reviewed: false
last_reviewer: "PASS | independent_readonly | 2026-07-30"
---

# AI 领域判断地图

## 60 秒入口

- 先问：AI 需求是否已经从使用或合同穿透到利润、现金和单位资本回报？
- 合格模式：`AI-P01`
- 首要反模式：需求和合同真实，但资本开支、融资、闲置或价格竞争吞掉股东现金。
- 第一问题：客户使用和合同，能否在未来一年转成每股现金流？

结构先验固定 `uncalibrated`，不能生成价格、四票或动作。

## 合格模式

### AI-P01｜需求必须穿透到利润与现金

```yaml
qualified_pattern:
  pattern_id: AI-P01
  recognition_cues:
    - 使用量、ARR、RPO 或订单高速增长
    - 资本开支、融资或摊薄同步上升
  causal_chain: 使用或订单增长 → 合同转收入 → 利用率与毛利改善 → 经营现金覆盖资本开支与融资 → 每股现金增加
  payer_and_money_path: 企业客户为云容量、软件任务或交付结果付费，收入扣除算力、建设和融资成本后归属普通股
  profit_control: 客户预付、容量利用率、单位资本产出、融资纪律和每股现金流
  favorable_fit: 合同按期转收入，毛利与经营现金同步改善，新增融资慢于每股价值增长
  counterpattern_and_falsifier: ARR/RPO 增长但收入、利润或自由现金长期落后，容量闲置或摊薄快于现金改善
  applicable_asset_types: [operating_company, etf]
  linked_cases:
    - 04_CASE_GYM/TRADE_LOG/260624_horizon_robotics_position_case.md
  first_questions:
    - 合同或使用量转收入需要多久？
    - 经营现金能否覆盖资本开支？
    - 完全摊薄后的每股价值是否改善？
  root_sources:
    - https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/
    - https://assets.nebius.com/assets/6fc0ea6c-0884-4a1f-bed8-1f797eb9628f/Financial%20results_Q1%202026.pdf
  reused_targets_or_settled_cases: [ORCL, NBIS]
```

## 候选模式｜暂不进入 60 秒前台

| ID | 候选 | 未过门槛原因 |
|---|---|---|
| `AI-C01` | 瓶颈会从 GPU 迁移到网络、电力、冷却、存储和运行层 | Murphy 已确认研究先验；仍缺两组独立世界事实根来源与跨标的结算 |
| `AI-C02` | Token 总需求增长可能快于单位效率提升 | Murphy 已确认研究先验；仍缺同口径需求、效率、能耗和利润数据 |
| `AI-C03` | 企业控制平面和私有上下文可能获得独立预算 | 现有依据以 Murphy 讨论和 AI 综合为主 |
| `AI-C04` | Physical AI 可能形成真实世界数据闭环 | 只有地平线等少量映射，兑现窗口不足 |
| `AI-C05` | 泡沫收缩可能把资源从训练迁向真实应用 | 尚无可结算跨周期样本 |

## Murphy 已确认候选先验｜不进入 structural_prior

下文是 AI 对 Murphy 原话的结构化映射，不是 Murphy 逐字原话。逐字来源：[[05_EVIDENCE_META/SOURCES/2026/260730AI工程化第二轮硬件需求_Murphy判断来源#EX-01]]

```yaml
candidate_prior:
  pattern_ids: [AI-C01, AI-C02]
  status: candidate
  structural_prior_eligible: false
  evidence_status: uncalibrated
  decision_authority: none
  murphy_prior_source:
    source_id: SRC-260730-MURPHY-AI-HW2-01
    excerpt_id: EX-01
```

### 条件链

- 模型能力商品化、推理成本下降和 CSP 工程工具补齐，可能推动企业工作负载由试验进入生产。
- 只有当场景数、调用频率、上下文长度与 Agent 步骤增长合计快于单位 Token 成本和算力效率改善时，总计算需求才会扩张。
- 需求瓶颈可能由单一 GPU 扩散至存储、光互连、网络、电力、冷却及半导体设备材料，但各环节兑现节奏不可预设。
- 研究次序先验证资本开支、订单、收入、利润和现金，再观察利润是否向 CSP、中间平台和应用迁移。
- 这是一项阶段性研究假设，不构成任何硬件资产的永久持有承诺。

### 不能证明

- 不能证明 AI 硬件近期必然反弹。
- 不能证明政策支持会自动转为订单、利润、现金或股价。
- 不能证明所有供应链环节同步受益，也不能用行业需求替代具体资产的收益路径。
- 不能生成价格结论、四票、仓位或六档动作。

### 晋级条件

- 至少两组相互独立的世界事实根来源，分别覆盖需求扩张与供给瓶颈。
- 至少一个跨标的或已结算 Case，证明需求能够穿透到收入、利润、经营现金及每股价值。
- 同口径跟踪总 Token/推理量、单位效率、能耗与单位资本产出，验证总量增长是否快于效率改善。
- 同时观察 CSP 资本开支与利用率，以及通信、半导体设备材料、电力基础设施的订单、毛利和经营现金。

### 削弱或失败条件

- 总使用量增长长期慢于单位成本与效率改善，实际算力或能耗需求不增反降。
- 需求集中于少数 CSP，利用率提升和现有库存吸收了新增工作负载，没有形成新订单周期。
- 订单增长但价格竞争、资本开支、融资或摊薄使利润和股东现金持续落后。
- 出口限制、供给过剩或客户自研改变利润池，使行业需求无法穿透到候选资产。

## 资产映射

- 公司：[[03_STATE/HYPOTHESIS_QUEUE/CURRENT/ORCL]]、[[03_STATE/HYPOTHESIS_QUEUE/CURRENT/NBIS]]、[[03_STATE/HYPOTHESIS_QUEUE/CURRENT/09660]]、[[03_STATE/HYPOTHESIS_QUEUE/CURRENT/600487]]
- ETF：[[03_STATE/HYPOTHESIS_QUEUE/CURRENT/515880]]、[[03_STATE/HYPOTHESIS_QUEUE/CURRENT/562500]]、[[03_STATE/HYPOTHESIS_QUEUE/CURRENT/588000]]
- 当前领域状态：[[03_STATE/DOMAIN_MODELS/AI/README]]

## Claim 反链

以下 working beliefs 的唯一完整正文位于 Claim Ledger；它们不自动成为合格模式：

- [[05_EVIDENCE_META/_SYSTEM/CLAIM_LEDGER#AI-B01｜生产级 Agent 需要模型之外的系统]]
- [[05_EVIDENCE_META/_SYSTEM/CLAIM_LEDGER#AI-B02｜企业会为治理与私有部署持续付费]]
- [[05_EVIDENCE_META/_SYSTEM/CLAIM_LEDGER#AI-B03｜普通智能商品化会迁移利润池]]
- [[05_EVIDENCE_META/_SYSTEM/CLAIM_LEDGER#AI-B04｜只有“使用—合同—利润—现金”闭环才是新秩序飞轮]]

原始版本：[[05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/260728AI领域知识_控制平面原子版_AI长报告原文]]。

本次母稿：[[05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/260728AI领域知识母稿_投资之道到Physical_AI_AI长报告原文]]。

Claim 状态和唯一正文见 [[05_EVIDENCE_META/_SYSTEM/CLAIM_LEDGER]]。

## 来源边界

- AI 母稿只提供候选连接，不把其中 `P0` 或 `AI_SYNTHESIS` 当 Murphy 确认。
- 当前对话只确认 `AI-C01`、`AI-C02` 为 Murphy 候选研究先验；“近期必定反弹”仍是 dated forecast，不进入稳定 Knowledge。
- dated synthesis：[[05_EVIDENCE_META/EVIDENCE/THEMES/260726AI基础设施_CurrentThesis重置证据]]
- Murphy 基线：[[05_EVIDENCE_META/EVIDENCE/THEMES/260727系统_Murphy判断驱动Harness基线]]
