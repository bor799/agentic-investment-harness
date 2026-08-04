---
title: "company_queue"
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
legacy_path: "AI周期探索/0_总览/company_queue.md"
migration_target: "90_AUTOMATION/RUNTIME + 03_STATE"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Company Queue

规则：Claude Code 每轮只取第一个 `pending` 公司，执行该公司 `02_公司研究/{company}/PROMPT.md`。

| status | 公司 | 代码 | 初始分组 |
|---|---|---|---|
| completed | Microsoft | MSFT | AI企业效率/上下文入口 |
| completed | ServiceNow | NOW | 企业流程编排 |
| completed | Oracle | ORCL | AI基础设施/企业数据 |
| completed | MongoDB | MDB | 企业数据/开发者基础设施 |
| completed | Cloudflare | NET | AI基础设施/边缘网络 |
| completed | Google | GOOGL | AI平台/企业上下文 |
| completed | Atlassian | TEAM | 软件工程效率/协作上下文 |
| completed | Salesforce | CRM | CRM流程入口 |
| completed | Palantir | PLTR | 企业数据/决策执行 |
| completed | Datadog | DDOG | DevOps可观测性 |
| completed | GitLab | GTLB | 软件工程效率/DevSecOps |
| completed | Nvidia | NVDA | AI算力基础设施 |
| completed | Micron | MU | AI内存/HBM瓶颈 |
| completed | Vistra | VST | AI电力瓶颈 |
| completed | NuScale Power | SMR | 核能期权/电力瓶颈 |
| completed | Lumentum | LITE | 光通信/数据中心瓶颈 |
| completed | Meta | META | AI应用/广告平台 |
| completed | Circle | CRCL | 稳定币/Agent支付期权 |
| completed | Coinbase | COIN | 加密金融基础设施 |
| completed | BitGo Holdings | BTGO | 数字资产托管基础设施 |
| completed | Rocket Lab | RKLB | 商业航天期权 |
| completed | Tempus AI | TEM | AI医疗数据期权 |
| completed | Figure Technology | FIGR | 金融科技期权 |
| completed | Lemonade | LMND | AI保险期权 |
| completed | Duolingo | DUOL | AI教育/消费订阅 |
| completed | Tesla | TSLA | 自动驾驶/机器人期权 |
| completed | Li Auto | LI | 智能汽车/中国消费科技 |
| completed | Horizon Robotics | 09660.HK | 智能驾驶/NOA平台 |
| completed | Tencent | 00700.HK | 中国平台/AI应用 |
| completed | Alibaba | BABA / 09988.HK | 中国平台/云与电商 |
| completed | PDD | PDD | 中国消费平台 |
| completed | Meituan | 03690.HK | 本地生活平台 |
| completed | Xiaomi | 01810.HK | 消费电子/汽车平台 |
| completed | Bilibili | 09626.HK | 内容社区平台 |
| completed | Pop Mart | 09992.HK | 消费品牌/IP平台 |
| completed | Miniso | 09896.HK | 消费品牌/全球化零售 |
| completed | Beike | 02423.HK | 居住服务平台 |
| completed | HashKey Holdings | 03887.HK | 港股数字资产期权 |
| completed | Berkshire Hathaway B | BRK.B | 传统资产/现金流基准 |
| completed | CRRC | 01766.HK | 传统制造/出海观察 |
| completed | Fuyao Glass | 03606.HK | 制造出海/汽车玻璃 |
| completed | Aux Electric | 02580.HK | 家电/制造观察 |
| completed | TQQQ | TQQQ | 指数杠杆工具 |
| completed | Hang Seng Tech Index | HKHSTECH | 港股科技指数 |
| completed | 分众传媒 | 002027.SZ | 消费广告现金流 |
