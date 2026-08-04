---
title: "美股AI投资日报自动化计划_cc"
date: 2026-07-24
updated: 2026-07-24
layer: AUTOMATION
primary_role: legacy_codex_automation_design
status: archived
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
legacy_metadata_added: true
legacy_path: "codeex 版本/美股AI投资日报自动化计划_cc.md"
migration_target: "90_AUTOMATION + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 美股 AI 投资日报自动化系统

## Context

用户已有完整的 AI 投资研究体系（Bottleneck 3X Framework、V3 100X 知识萃取、Mindspace MCP 信源、agent-reach 联网能力），但缺少一个**每日自动运行的投资信号报告系统**。当前痛点：信息分散在多个系统中，无法每天系统性验证 AI 投资主线（token 需求 → GPU/HBM/网络瓶颈 → capex → 收入 → 利润 → 赔率），容易陷入新闻播报而非信号判断。

目标：在现有基础设施上新增一层自动化编排，每天北京时间 08:00 生成三层结构（5 分钟结论 / AI 主线验证面板 / 数据证据），输出投资信号而非新闻摘要。

## 核心原则

- **不重建**：V3 已处理 fetch/score/extract，Mindspace MCP 已控制信源，日报系统是编排层
- **MCP-first**：遵循 `MINDSPACE_SOURCE_MCP_SOP.md`，agent-reach 仅作 fallback
- **信号导向**：每个数据点必须映射到瓶颈链条的一个环节，否则丢弃
- **六项测试**：Need / Constraint / Control / Pricing / Capture / Duration

## 文件结构

```
AI周期探索/05_日报系统/
├── DAILY_LOOP_PROMPT.md        # 每日 CronCreate 读取的主 prompt
├── WATCHLIST.yml               # 80+ 股票，9 个分类，扩展自 watchlist_master.md
├── SIGNAL_DEFINITIONS.md       # 信号分类标准：已验证/待验证/噪音
├── REPORT_TEMPLATE.md          # 三层输出模板（结构骨架）
├── DATA_SOURCES.yaml           # 新增金融数据 RSS + web 源配置
├── DAILY_SIGNAL_LOG.md         # 累加式信号历史（每日追加一行）
├── DECISION_NOTES.md           # 影响投资框架的变化记录
└── reports/
    └── YYYY-MM-DD_us_market_daily.md  # 每日报告输出
```

## 实施步骤

### Phase 1：创建基础文件（05_日报系统/ 目录）

**Step 1.1 — 创建 `WATCHLIST.yml`**
- 路径：`05_日报系统/WATCHLIST.yml`
- 从 `0_总览/watchlist_master.md` 的 48 条现有条目导入，使用 canonical_id 对齐
- 扩展到用户指定的 9 个分类 80+ 只股票：
  - core_ai_platform: NVDA, MSFT, GOOGL, META, AMZN, ORCL
  - gpu_and_compute: NVDA, AMD, AVGO, MRVL, ARM, TSM, ASML, INTC, QCOM
  - hbm_and_memory: MU, WDC, STX
  - networking_and_interconnect: ANET, AVGO, MRVL, CRDO, ALAB, CIEN, NOK
  - optical_and_photonics: LITE, COHR, AAOI, TSEM, SIVE
  - servers_and_datacenter: SMCI, DELL, HPE, VRT, ETN, PWR, GEV
  - ai_power_and_energy: VST, CEG, NRG, OKLO, SMR, NEE, SO, DUK, FLNC
  - ai_infrastructure_software: DDOG, NET, MDB, SNOW, PLTR, NOW, CRM, PANW, CRWD, TEAM, WDAY, INTU, SHOP
  - consumer_or_edge_ai: AAPL, TSLA, QCOM, ARM
  - speculative_ai_infra: APLD, IREN, CORZ, BE
- 每条包含：canonical_id, company, ticker, market, category, bottleneck_layer(L1-L5), key_metrics, action_tag

**Step 2 — 创建 `SIGNAL_DEFINITIONS.md`**
- 路径：`05_日报系统/SIGNAL_DEFINITIONS.md`
- 定义三类信号分类标准（映射到 V2 legacy 的信号评估框架）：
  - **已验证信号**：source_tab 为 filing_feed/official_press/announcement + 有具体数据（收入/毛利率/FCF/capex/backlog/指引）
  - **待验证信号**：source_tab 为 report/data_aggregator/blog/newsletter + 有逻辑链条但缺直接数据
  - **噪音信号**：source_tab 为 forum/social + 无数据支撑的观点/情绪
- 定义核心公式检查链：AI usage → token → GPU/HBM/网络 → capex → revenue → margins/FCF/EPS → repricing → odds
- 定义行动标签词汇表（用户指定的 16 种标签）
- 定义风险等级：低/中/中高/高
- 引用 V2 legacy 的信号 vs 噪声框架（找相同 vs 找不同、穿越时间 vs 此刻刺激、反复出现 vs 只发生一次）

**Step 3 — 创建 `REPORT_TEMPLATE.md`**
- 路径：`05_日报系统/REPORT_TEMPLATE.md`
- 三层结构骨架：
  - Layer 1：5 分钟结论（市场状态一句话、AI 主线状态、操作倾向、风险级别）
  - Layer 2：AI 主线验证面板（5 大信号块：需求/瓶颈/利润/拥挤/轮动）
  - Layer 3：数据与证据（15 个模块：大盘、走势、宏观、板块、主题、宽度、技术面、个股、财报、机构、轮动、重点股、明日清单、风险提示、最终结论）
- 每个模块定义必需字段和判断要点

**Step 4 — 创建 `DATA_SOURCES.yaml`**
- 路径：`05_日报系统/DATA_SOURCES.yaml`
- 两类数据源：
  - RSS feeds（可加入 V3 调度器）：Seeking Alpha, Yahoo Finance, Semianalysis, Counterpoint, TrendForce
  - Web 源（agent-reach 抓取）：Finviz, Fear & Greed, Sector SPDR, CME FedWatch
- 数据源与报告模块的映射关系

**Step 5 — 创建 `DAILY_SIGNAL_LOG.md` 和 `DECISION_NOTES.md`**
- DAILY_SIGNAL_LOG.md：表头行（日期/主线状态/最强板块/最弱板块/已验证信号/待验证信号/最大风险/明日观察）
- DECISION_NOTES.md：空文件，只记录影响投资框架的变化

### Phase 2：创建主 Prompt

**Step 6 — 创建 `DAILY_LOOP_PROMPT.md`**
- 路径：`05_日报系统/DAILY_LOOP_PROMPT.md`
- 核心指令：
  1. 读取 WATCHLIST.yml + REPORT_TEMPLATE.md + SIGNAL_DEFINITIONS.md + BOTTLENECK_3X_FRAMEWORK.md
  2. 读取 watchlist_master.md 和 company_score_table.md 获取当前分类和分数
  3. 数据获取（MCP-first）：
     - health_check → search_channels（按 9 个分类批量查）→ search_articles → get_article_detail
     - Fallback: agent-reach（Exa 搜索、Jina Reader、web-reader MCP）
  4. 信号提取：对每条证据分类为 已验证/待验证/噪音
  5. 报告生成：按三层模板填充
  6. 输出文件：reports/YYYY-MM-DD_us_market_daily.md + 更新 DAILY_SIGNAL_LOG.md + 更新 DECISION_NOTES.md（如有）
- 硬约束：
  - 不是新闻摘要，每个数据点必须映射到瓶颈链条
  - 禁止输出买入/卖出建议，只用条件表达
  - 必须输出"今日不应该做什么"
  - 必须输出信号分类统计

### Phase 3：安装 AIHot Skill + V3 增强

**Step 7 — 安装 AIHot skill**
- 从 https://aihot.virxact.com/aihot-skill/ 安装
- 在 DAILY_LOOP_PROMPT.md 中添加 AIHot 作为补充中文 AI 新闻数据源
- AIHot 覆盖：AI 模型、产品、产业、论文、技巧

**Step 8 — 添加金融数据 RSS 到 V3（可选）**
- 修改 V3 config/config.local.yaml 添加 DATA_SOURCES.yaml 中的 RSS feeds
- 使 V3 调度器自动发现和抓取金融内容
- 日报系统从 Mindspace MCP 获取 V3 已处理的内容，避免重复抓取

### Phase 4：设置定时任务

**Step 9 — 创建 CronCreate 定时任务**
- 北京时间 08:00（UTC 00:03，避开整点）
- cron: `3 0 * * *`
- prompt: 读取 DAILY_LOOP_PROMPT.md 并执行
- durable: true
- recurring: true
- 自动 7 天过期，需定期刷新

**Step 10 — 手动运行一次验证**
- 触发首次运行，检查输出质量
- 验证：reports/ 目录是否生成、信号分类是否合理、数据源是否覆盖

## 关键复用文件

| 文件 | 用途 | 路径 |
|---|---|---|
| BOTTLENECK_3X_FRAMEWORK.md | 六项测试 + 五层蛋糕 + 三年三倍 | `0_总览/` |
| MINDSPACE_SOURCE_MCP_SOP.md | MCP-first 数据获取协议 | `0_总览/` |
| watchlist_master.md | 48 条现有 canonical_id | `0_总览/` |
| company_score_table.md | 当前分数和分类（只读） | `0_总览/` |
| v2_legacy/extraction.md | 信号 vs 噪声标准 | V3 prompts/versions/ |
| investment-data-routing | 数据源路由 skill | ~/.config/skillshare/skills/ |
| agent-reach | 联网 fallback skill | ~/.config/skillshare/skills/ |

## 验证方法

1. **文件完整性**：05_日报系统/ 下所有 6 个文件 + reports/ 目录已创建
2. **数据源连通性**：Mindspace MCP health_check 通过，agent-reach Exa 搜索返回结果
3. **首次运行**：手动执行 DAILY_LOOP_PROMPT.md，生成完整三层报告
4. **信号质量**：报告中已验证信号有 source_tab 引用，噪音信号正确过滤
5. **定时执行**：CronCreate 任务在北京时间 08:03 自动触发
6. **AIHot 集成**：安装后能在日报中引用中文 AI 新闻作为补充视角

## 风险与应对

- **MCP 覆盖不足**：金融数据（股价、板块表现、市场宽度）可能 MCP 无结果 → 重度依赖 agent-reach fallback
- **Token 消耗**：80+ 股票全量扫描消耗大 → 按 9 个分类批量查，每类 limit=5
- **信号漂移**：报告退化为新闻摘要 → DAILY_LOOP_PROMPT.md 硬约束每条证据必须映射到瓶颈链条
- **美股休市日**：检测交易日历，非交易日输出周末/节假日复盘 + 未来一周观察清单
