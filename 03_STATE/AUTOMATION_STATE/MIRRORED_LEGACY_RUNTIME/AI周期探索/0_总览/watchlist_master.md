---
title: "watchlist_master"
date: 2026-07-24
updated: 2026-07-24
layer: STATE
primary_role: legacy_automation_state
status: superseded
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
legacy_metadata_added: true
legacy_path: "AI周期探索/0_总览/watchlist_master.md"
migration_target: "90_AUTOMATION/RUNTIME + 03_STATE"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Watchlist Master

更新日期：2026-05-24

说明：这是第一版统一索引。评分和最终分类仍以 `company_score_table.md` 为准；本文件用于跨文件对齐公司、ticker、市场、canonical id、当前研究状态和刷新优先级。

## Canonical ID 规则

```text
INV-{市场}-{ticker_or_code}
```

市场代码：

- `US`：美股
- `HK`：港股
- `CN`：A股
- `DUAL`：双重或多市场上市
- `PRIVATE`：私有公司
- `INDEX`：指数或工具类标的

## P1 Refresh Watchlist

| canonical_id | 公司 | 代码 | 市场 | 当前层/主题 | 刷新优先级 | 核心下一证据 |
|---|---|---|---|---|---|---|
| INV-US-MDB | MongoDB | MDB | US | 数据与上下文 | P1 | Atlas 增速、GM、NRR、FY2027 盈利 |
| INV-US-NET | Cloudflare | NET | US | Agent runtime / 边缘网络 | P1 | Workers AI 收入、Dynamic Workers 采用、盈利路径 |
| INV-US-MRVL | Marvell Technology | MRVL | US | AI 网络/定制 ASIC | P1 | Q1 FY27、设计胜出、Google MPU/TPU |
| INV-CN-300390 | 天华新能 | 300390.SZ | CN | 锂电材料/氢氧化锂 | P1 | H股进展、CATL 占比、Q2 毛利率 |
| INV-CN-300476 | 胜宏科技 | 300476.SZ | CN | AI 服务器 PCB | P1 | AI PCB 收入占比、Rubin 订单 |
| INV-CN-002463 | 沪电股份 | 002463.SZ | CN | AI 服务器 PCB | P1 | AI PCB 收入占比、毛利率、大客户 |
| INV-CN-002916 | 深南电路 | 002916.SZ | CN | PCB + IC 载板 | P1 | FC-BGA 良率、无锡扩产 |
| INV-CN-688183 | 生益电子 | 688183.SH | CN | 高端 PCB / ASIC | P1 | ASIC 客户、Q1 数据、CCL 协同 |
| INV-DUAL-001389-01989 | 广合科技 | 001389.SZ / 01989.HK | DUAL | 算力服务器 PCB | P1 | PCIE6.0、AI PCB 占比、限售解禁 |
| INV-US-SNOW | Snowflake | SNOW | US | 数据与上下文 | P1 | Cortex AI 收入、consumption 趋势 |
| INV-US-ESTC | Elastic | ESTC | US | 混合搜索/企业搜索 | P1 | ELSER 收入、混合搜索采用 |
| INV-US-PLTR | Palantir | PLTR | US | 企业 Ontology | P1 | AIP 收入、商业客户增速 |
| INV-US-DDOG | Datadog | DDOG | US | AI 可观测性 | P1 | AI 功能收入、RPO 增速 |
| INV-US-MSFT | Microsoft | MSFT | US | Agent 控制面 | P1 | Agent 365、Copilot seat、Azure AI |
| INV-US-GTLB | GitLab | GTLB | US | DevSecOps | P1 | AI security 采纳、增速重加速 |
| INV-CN-301358 | 湖南裕能 | 301358.SZ | CN | LFP/LMFP | P1 | LFP 价格、客户集中度、Q2 毛利率 |

## Core Tracked Universe

### AI 企业效率 / 工作流 / 控制面

| canonical_id | 公司 | 代码 | 市场 |
|---|---|---|---|
| INV-US-MSFT | Microsoft | MSFT | US |
| INV-US-NOW | ServiceNow | NOW | US |
| INV-US-TEAM | Atlassian | TEAM | US |
| INV-US-CRM | Salesforce | CRM | US |
| INV-US-GTLB | GitLab | GTLB | US |
| INV-US-DDOG | Datadog | DDOG | US |
| INV-US-OKTA | Okta | OKTA | US |
| INV-US-CYBR | CyberArk | CYBR | US |
| INV-US-CRWD | CrowdStrike | CRWD | US |
| INV-US-FROG | JFrog | FROG | US |

### 数据与上下文

| canonical_id | 公司 | 代码 | 市场 |
|---|---|---|---|
| INV-US-MDB | MongoDB | MDB | US |
| INV-US-SNOW | Snowflake | SNOW | US |
| INV-US-ESTC | Elastic | ESTC | US |
| INV-US-PLTR | Palantir | PLTR | US |
| INV-US-ORCL | Oracle | ORCL | US |
| INV-US-GOOGL | Google | GOOGL | US |

### AI 基础设施 / 物理瓶颈

| canonical_id | 公司 | 代码 | 市场 |
|---|---|---|---|
| INV-US-NVDA | Nvidia | NVDA | US |
| INV-US-MU | Micron | MU | US |
| INV-US-MRVL | Marvell Technology | MRVL | US |
| INV-US-NET | Cloudflare | NET | US |
| INV-US-VST | Vistra | VST | US |
| INV-US-SMR | NuScale Power | SMR | US |
| INV-US-LITE | Lumentum | LITE | US |
| INV-US-CRWV | CoreWeave | CRWV | US |
| INV-US-CBRS | Cerebras | CBRS | US |

### 加密 / 金融科技 / 期权型

| canonical_id | 公司 | 代码 | 市场 |
|---|---|---|---|
| INV-US-CRCL | Circle | CRCL | US |
| INV-US-COIN | Coinbase | COIN | US |
| INV-US-BTGO | BitGo Holdings | BTGO | US |
| INV-HK-03887 | HashKey Holdings | 03887.HK | HK |
| INV-US-FIGR | Figure Technology | FIGR | US |

### 消费 / 平台 / 中国资产

| canonical_id | 公司 | 代码 | 市场 |
|---|---|---|---|
| INV-DUAL-BABA-09988 | Alibaba | BABA / 09988.HK | DUAL |
| INV-HK-00700 | Tencent | 00700.HK | HK |
| INV-US-PDD | PDD | PDD | US |
| INV-HK-03690 | Meituan | 03690.HK | HK |
| INV-HK-01810 | Xiaomi | 01810.HK | HK |
| INV-HK-09626 | Bilibili | 09626.HK | HK |
| INV-HK-09992 | Pop Mart | 09992.HK | HK |
| INV-HK-09896 | Miniso | 09896.HK | HK |
| INV-HK-02423 | Beike | 02423.HK | HK |
| INV-US-DUOL | Duolingo | DUOL | US |
| INV-US-LMND | Lemonade | LMND | US |
| INV-US-TSLA | Tesla | TSLA | US |
| INV-US-LI | Li Auto | LI | US |
| INV-HK-09660 | Horizon Robotics | 09660.HK | HK |

### A股 / 港股制造与周期

| canonical_id | 公司 | 代码 | 市场 |
|---|---|---|---|
| INV-CN-301358 | 湖南裕能 | 301358.SZ | CN |
| INV-CN-300390 | 天华新能 | 300390.SZ | CN |
| INV-CN-300476 | 胜宏科技 | 300476.SZ | CN |
| INV-CN-002463 | 沪电股份 | 002463.SZ | CN |
| INV-CN-688183 | 生益电子 | 688183.SH | CN |
| INV-CN-002916 | 深南电路 | 002916.SZ | CN |
| INV-DUAL-001389-01989 | 广合科技 | 001389.SZ / 01989.HK | DUAL |
| INV-HK-03606 | Fuyao Glass | 03606.HK | HK |
| INV-HK-01766 | CRRC | 01766.HK | HK |
| INV-HK-02580 | Aux Electric | 02580.HK | HK |
| INV-CN-002027 | 分众传媒 | 002027.SZ | CN |

### 工具 / 指数 / 基准

| canonical_id | 对象 | 代码 | 类型 |
|---|---|---|---|
| INV-US-BRKB | Berkshire Hathaway B | BRK.B | 传统资产/现金流基准 |
| INV-INDEX-TQQQ | TQQQ | TQQQ | 杠杆指数工具 |
| INV-INDEX-HKHSTECH | Hang Seng Tech Index | HKHSTECH | 港股科技指数 |

## 使用规则

- 新公司进入 `new_company_intake_queue.md` 时同步添加 canonical id。
- 公司改名或多地上市时 canonical id 不轻易更换，只在备注中增加别名。
- 投资池移动不在本文件直接判断，只同步当前索引。
- 若本文件与 `company_score_table.md` 冲突，以 `company_score_table.md` 为准。

