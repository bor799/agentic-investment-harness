---
title: "refresh_targets_2026-05-24"
date: 2026-07-24
updated: 2026-07-24
layer: METHOD
primary_role: legacy_ai_cycle_method
status: superseded
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
legacy_metadata_added: true
legacy_path: "AI周期探索/0_总览/refresh_targets_2026-05-24.md"
migration_target: "02_术/SKILLS + 90_AUTOMATION"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Refresh Targets

日期：2026-05-24

## 本轮目标

先做证据刷新和趋势整理，不直接输出买入/卖出建议。所有更新必须回到 `evidence_log.md`，并同步 `company_score_table.md` 和 `run_log.md`。

## P0：索引和数据结构

| target | output | 状态 |
|---|---|---|
| watchlist master | `0_总览/watchlist_master.md` | 已建立初版 |
| source health | `0_总览/source_health_2026-05-24.md` | 已建立初版 |
| refresh targets | `0_总览/refresh_targets_2026-05-24.md` | 当前文件 |

## P1：公司级刷新

### 数据与上下文层

| 公司 | 代码 | 关键问题 | 优先证据 |
|---|---|---|---|
| MongoDB | MDB | Atlas 消费增速、GM 是否触底、NRR、>$100K ARR 客户 | FY2027 Q1/Q2 财报、10-Q、IR、StockAnalysis、Mindspace 文章 |
| Snowflake | SNOW | Cortex AI 是否贡献增量收入，consumption 是否恢复 | 财报电话会、IR、Mindspace report/blog |
| Elastic | ESTC | ELSER / 混合搜索是否转化为收入 | 财报、产品采用、客户案例 |
| Palantir | PLTR | AIP/Ontology 商业客户增速，SAP 合作产出 | 财报、合同公告、SAP/Accenture 合作进展 |

### Agent runtime / 控制面

| 公司 | 代码 | 关键问题 | 优先证据 |
|---|---|---|---|
| Cloudflare | NET | Workers AI 收入、Dynamic Workers 客户采用、盈利路径、RPO 组成 | Q2'26 财报、10-Q、Cloudflare Radar、客户案例 |
| Datadog | DDOG | AI 可观测性是否成为独立品类，RPO 是否维持高增 | 财报、产品收入披露、客户采用 |
| Microsoft | MSFT | Agent 365 企业采纳、Copilot seat 渗透率、Azure AI 增速 | 财报、M365/Copilot 披露、官方案例 |
| GitLab | GTLB | AI DevSecOps 功能采用率、增速是否重加速 | 财报、产品指标、客户案例 |

### AI 物理瓶颈

| 公司 | 代码 | 关键问题 | 优先证据 |
|---|---|---|---|
| Marvell | MRVL | Q1 FY27 财报、定制硅设计胜出、Google MPU/TPU 合作 | 2026-05-27 财报、IR、客户公告 |
| Micron | MU | HBM 供给缺口、毛利率峰值风险、客户满足率 | 财报、HBM 合同、供应链报告 |
| Nvidia | NVDA | 推理收入占比、Blackwell/Rubin 供给、毛利率压力 | 财报、供应链、客户 capex |
| Lumentum | LITE | InP 产能锁定、OCS 订单、估值消化 | 财报、订单、行业供需 |
| Vistra | VST | PPA 新签约、电价和 ERCOT 风险、FCF 稳定性 | 财报、PPA 公告、电力市场数据 |

### A股 PCB 组

| 公司 | 代码 | 关键问题 | 优先证据 |
|---|---|---|---|
| 胜宏科技 | 300476.SZ | AI PCB 收入占比、Rubin 订单、海外大客户 | 公司公告、调研纪要、东方财富/同花顺 |
| 沪电股份 | 002463.SZ | AI PCB 收入占比、毛利率趋势、大客户验证 | 财报、机构调研、行业对比 |
| 深南电路 | 002916.SZ | FC-BGA 良率、无锡扩产、载板盈利时间表 | 财报、扩产公告、研报 |
| 生益电子 | 688183.SH | ASIC 客户、Q1 数据、母公司 CCL 协同 | 财报、调研纪要、公告 |
| 广合科技 | 001389.SZ / 01989.HK | PCIE6.0 量产、AI 算力 PCB 占比、限售解禁 | 财报、A/H 公告、客户认证 |

### 周期材料

| 公司 | 代码 | 关键问题 | 优先证据 |
|---|---|---|---|
| 天华新能 | 300390.SZ | H股进展、CATL 占比、Q2 毛利率持续性、锂价中枢 | 巨潮/深交所、东方财富、SMM 价格、HKEX |
| 湖南裕能 | 301358.SZ | LFP 价格、客户集中度、LMFP 差异化、Q2 毛利率 | 财报、价格数据、客户公告 |

## P2：主题级趋势刷新

| 主题 | 关键词 | 输出 |
|---|---|---|
| Agent 控制面 | `AI agent runtime enterprise adoption`, `Agent 365 governance`, `agent identity audit` | Agent 控制面趋势 |
| MCP 治理 | `MCP governance security enterprise`, `shadow MCP`, `tool poisoning` | MCP 治理趋势 |
| 数据上下文 | `enterprise RAG context engineering`, `hybrid search`, `vector search revenue` | 数据与上下文趋势 |
| 电力瓶颈 | `AI data center power bottleneck`, `PPA AI data center`, `ERCOT data center load` | AI 电力趋势 |
| HBM/网络 | `HBM supply pricing`, `AI optical interconnect`, `Nvidia Rubin supply chain` | AI 物理瓶颈趋势 |
| PCB | `AI PCB Nvidia Rubin`, `HDI server PCB`, `FC-BGA substrate China` | AI PCB 横向比较 |
| 锂电材料 | `lithium hydroxide price rebound`, `LFP price 2026`, `LMFP capacity` | 周期材料趋势 |
| 中国消费平台 | `China consumer platform earnings 2026`, `Pop Mart overseas revenue`, `Meituan subsidy war` | 中国平台与消费趋势 |

## 执行批次建议

第一批只处理 5 个：

1. MongoDB
2. Cloudflare
3. Marvell
4. 天华新能
5. PCB 横向组（先做横向表，不急着改五家公司评分）

原因：这五个覆盖了数据层、agent runtime、物理瓶颈、周期材料和 A股产业链，能快速验证整条流程是否顺。

