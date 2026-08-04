---
title: "美股AI投资日报自动化计划_codeex版本"
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
legacy_path: "codeex 版本/美股AI投资日报自动化计划_codeex版本.md"
migration_target: "90_AUTOMATION + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 美股 AI 投资日报自动化计划（codeex 版本）

## Summary

- 在当前股票投资项目中建立“全库一起扫”的每日投资信号系统：美股 AI 为日报核心，同时扫描现有港股、A股、加密/期权、指数工具，只有出现异常信号时进入重点观察。
- 采用轻集成：不重写 V3，只给 V3 增加信源和边界提示；Codex Automation 每天北京时间 08:00 调度、汇总、写入日报。
- 信号门槛采用保守验证：积极行动标签必须依赖财报、订单、指引、capex、毛利率、FCF、backlog、监管文件或公司一手披露；软信号只能进“待验证/明日观察”。

## Key Changes

- 创建或增量更新当前项目文件：
  - `AGENTS.md`：写入日报研究员角色、证据优先级、禁止 FOMO、禁止直接买卖建议、交易纪律。
  - `WATCHLIST.yml`：合并用户给定美股 AI 股票池与现有 `AI周期探索/0_总览/watchlist_master.md`，增加 `canonical_id`、市场、分类、状态、优先级、下一验证信号。
  - `SIGNALS.md`、`DAILY_SIGNAL_LOG.md`、`DECISION_NOTES.md`：分别记录已验证/待验证/噪音信号、每日主线状态、真正改变投资框架的变化。
  - `DAILY_REPORT_TEMPLATE.md`：按用户给出的 15 节结构生成模板，但将“全库一起扫”压缩为“核心日报 + 异常信号附录”。
  - `RUNBOOK_DAILY_REPORT.md`：说明数据源顺序、交易日/非交易日处理、冲突数据处理、失败降级。
  - `reports/YYYY-MM-DD_us_market_daily.md`：生成首版占位模板；实现时若当天非美股常规交易日，写周末/节假日复盘结构。

- 安装并接入 AI HOT：
  - 安装到 `~/.codex/skills/aihot`，安装后需要重启 Codex 才会出现在新会话技能列表。
  - 同时把 `https://aihot.virxact.com/feed.xml` 加入 V3 RSS 信源，作为 AI 行业动态输入，不作为投资结论源。
  - AI HOT API 使用时必须带浏览器 User-Agent；只把它当“AI 行业事实/产品/模型/工程师信号”的候选源，结论需回到公司 IR、SEC、CME、FRED、交易所、财报等硬证据。

- V3 轻集成：
  - 在 V3 的 `config/sources.yaml` 或外部 `sources_files` 增量加入 AI HOT、公司 IR、SEC/Nasdaq/Fed/CME/FRED/EIA 等可 RSS 或稳定抓取的源。
  - 不新增日报生成 runner；V3 继续负责抓取、萃取、信号过滤，Codex Automation 负责每日汇总与写报告。
  - 保持 Mindspace Source MCP-first；agent-reach/Jina/RSS 只在 MCP 覆盖不足时补证据。

- 创建 Codex Automation：
  - 名称：`Generate US AI Market Daily`
  - 类型：standalone automation
  - 频率：每天北京时间 08:00
  - 工作目录：当前股票投资项目
  - 输出：`reports/YYYY-MM-DD_us_market_daily.md`
  - 自动化提示词要求：读取 `AGENTS.md`、`WATCHLIST.yml`、V3 输出、现有 AI 周期探索文件；生成日报并更新 `SIGNALS.md`、`DAILY_SIGNAL_LOG.md`、`DECISION_NOTES.md`。

## Interfaces And Rules

- `WATCHLIST.yml` 状态只允许：`core_compound_pool`、`three_bagger_candidate`、`bottleneck_watchlist`、`insufficient_evidence`、`exclude`。
- 个股行动标签只允许使用用户给定列表；不得输出“买入/卖出”。
- 每条关键结论必须标为：`已验证信号`、`待验证信号`、`噪音信号`、`需要后续追踪`。
- 数据冲突时优先级：公司 IR/SEC/交易所/CME/FRED/美国财政部/EIA > Reuters/Bloomberg/CNBC/WSJ > Yahoo/MarketWatch/Investing/Barchart > AI HOT/社区/分析师/KOL。
- 报告必须包含“今日不应该做什么”，用来约束追高、听朋友推荐、无止损补仓等历史风险。

## Test Plan

- 验证文件：确认目标文件存在；已有文件只增量修改，不覆盖用户内容。
- 验证 V3：运行配置加载检查、RSS 源发现检查、V3 doctor；确认新增信源不会破坏现有 7x24H 流程。
- 验证 AI HOT：确认 skill 文件安装成功；确认 RSS 可被 V3 解析；API 访问带 User-Agent。
- 验证日报：手动跑一次 automation prompt 的等价流程，检查报告包含三层结构、15 个模块、全库异常附录、来源链接、信号分类和行动纪律。
- 验证 automation：创建后查看任务状态，并确认下一次运行时间为北京时间下一次 08:00。

## Assumptions

- 用户选择“全库一起扫”：日报主轴仍是 AI 投资框架，但港股/A股/加密/期权/指数工具出现强信号时进入观察。
- 用户选择“轻集成”：不重写 V3，不复制 V3 的抓取和萃取能力。
- 用户选择“保守验证”：软信号不触发积极行动标签。
- 已参考本地 V3、`AI周期探索`、V2 legacy prompts，以及 AI HOT 文档：[Agent 接入](https://aihot.virxact.com/agent)、[更新日志](https://aihot.virxact.com/changelog)、[RSS Feed](https://aihot.virxact.com/feed.xml)。

## Implementation Boundary

- 本文件只是保存“codeex 版本”的计划文档。
- 本次不创建日报系统的实际运行文件。
- 本次不安装 AI HOT Skill。
- 本次不创建 Codex Automation。
