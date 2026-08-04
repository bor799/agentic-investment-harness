---
title: "LOOP_PROMPT_CN_CONSUMER_REFRESH"
date: 2026-07-24
updated: 2026-07-24
layer: AUTOMATION
primary_role: legacy_prompt_or_command
status: superseded
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: operational
legacy_metadata_added: true
legacy_path: "AI周期探索/0_总览/LOOP_PROMPT_CN_CONSUMER_REFRESH.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 中国消费与品牌公司 Agent-Reach 刷新循环

你是 `AI_CN_CONSUMER_REFRESH_LOOP` 循环调度器，不是泛化公司研究员。

项目目录：
`/Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索`

核心目标：只刷新 11 家中国消费/品牌/制造相关公司的证据质量，用 agent-reach 优先补齐官方财报、交易所公告、IR、中文/英文关键词证据，替换 Wikipedia 旧数据、Google Finance 单点数据和异常财务值。

重要：补证据只是第一步。每家公司刷新后，必须继续使用本地投资分析 skills 重新判定：
- `ljg-invest`：判断它是不是一台“秩序创造机器”，飞轮是否转起来，权力来源和失败条件是什么。
- `comprehensive-analysis`：判断财报质量、估值、消息面/催化剂、市场情绪和流动性环境。

截止日期：只使用 `2026-05-16` 及以前已发布的数据。不要使用晚于该日期的事实、财报、新闻或市场数据。

禁止事项：
- 不要改动 `0_总览/company_queue.md`。
- 不要使用内置 `web_search`。
- 不要把 Wikipedia 作为核心财务来源。
- 不要把 Google Finance 单独作为估值或投资结论来源。
- 不要因为 Exa 未配置就停止；Exa 不是本循环的硬前置。

## 自动执行约束

- 使用当前工作环境执行，不进入额外 sandbox。
- 全自动执行；常规 MCP、agent-reach、Jina、curl、文件读写和检索步骤不需要向用户确认。
- 不要因为需要调用 MCP 工具、读取网页、更新公司文件或同步池文件而打断用户。
- 自行选择并调用当前会话可用的 MCP 工具；如果某个 MCP 不可用，按本协议记录并使用 fallback。
- 只有遇到真实阻塞（认证缺失、网页完全不可读、目标公司路径不存在、数据晚于 cutoff 且无法替代）才写入 `blocked_source_unavailable` 或 `evidence_limited_after_fallback`。

## 目标公司

只处理以下 11 家公司：

| 公司 | 代码 | source route |
|---|---|---|
| Xiaomi | 01810.HK | HKEXnews + Xiaomi IR + official annual/interim results |
| Pop Mart | 09992.HK | HKEXnews + Pop Mart IR + official annual/interim results |
| Meituan | 03690.HK | HKEXnews + Meituan IR + official annual/interim results |
| PDD | PDD | SEC EDGAR + PDD IR + 20-F/6-K + StockAnalysis cross-check |
| Beike | BEKE / 02423.HK | SEC EDGAR + KE Holdings IR + HKEXnews + StockAnalysis cross-check |
| Bilibili | BILI / 09626.HK | SEC EDGAR + Bilibili IR + HKEXnews + StockAnalysis cross-check |
| Miniso | MNSO / 09896.HK | SEC EDGAR + Miniso IR + HKEXnews + StockAnalysis cross-check |
| CRRC | 01766.HK / 601766.SH | HKEXnews + SSE + CRRC IR + official annual results |
| Fuyao Glass | 03606.HK / 600660.SH | HKEXnews + SSE + Fuyao IR + official annual/interim results |
| Aux Electric | 02580.HK | HKEXnews + prospectus + Aux Electric IR/announcements |
| 分众传媒 | 002027.SZ | CNINFO + SZSE + Focus Media official announcements |

## 状态文件

使用独立队列：
`0_总览/cn_consumer_refresh_queue.md`

规则：
1. 每轮只处理 `Queue` 表里第一个 `pending` 公司。
2. 公司完成后，把状态改为 `completed`。
3. 如果官方源和 fallback 都已尝试但仍缺关键数据，把状态改为 `limited`，并在 `evidence_log.md` 写清楚缺口。
4. 如果遇到临时网络、站点或工具问题，最多重试 2 次；仍失败则标为 `blocked_source_unavailable`，并记录可恢复条件。
5. 不要把主项目队列 `company_queue.md` 作为本循环状态。

如果 `cn_consumer_refresh_queue.md` 不存在，按本 prompt 的 11 家目标公司创建它，全部设为 `pending`。

## 启动预检

每次 Ralph loop 启动后先检查 `cn_consumer_refresh_queue.md` 的 `Preflight cache`。如果 `Run started at` 为空、为 `unchecked`，或明显不是本次启动时间，执行一次预检，并写入该文件与 `0_总览/run_log.md`。

预检项目：
0. Run started at：写入当前本地时间和本轮 loop 名称 `AI_CN_CONSUMER_REFRESH_LOOP`。
1. Mindspace MCP：如果当前 Claude Code 会话暴露 `mindspace-source` 工具，调用 `health_check`；失败也不阻断。
2. agent-reach：运行或等价检查 `agent-reach doctor`，记录 Jina、Exa、雪球/财经、RSS、网页等可用 channel。
3. Jina Reader：用 `curl -s "https://r.jina.ai/https://example.com"` 或等价轻量 URL 验证网页读取可用。
4. Exa via mcporter：用 `mcporter list` 或轻量 Exa 调用检查是否配置。若 Exa 未配置，记录 `unavailable_not_blocking`。

预检后本轮后续公司复用该结果，不要每家公司重复 health_check 或 doctor。

## agent-reach 使用规则

必须加载并遵守 `agent-reach` skill。

推荐工具路径：
- Exa 搜索（如果已配置）：`mcporter call 'exa.web_search_exa(query: "...", numResults: 5)'`
- 通用网页直读：`curl -s "https://r.jina.ai/URL"`
- 精确网页读取（如果已配置）：`mcporter call 'web-reader.webReader(url: "https://example.com")'`

Exa 未配置时：
- 直接访问官方 IR、HKEXnews、SEC EDGAR、SSE、SZSE、CNINFO 页面。
- 使用 Jina Reader 读取已知官方 URL。
- 允许使用可信聚合源（StockAnalysis、交易所行情页、主流财经媒体）做 cross-check，但不能替代官方财报/公告。

## 每家公司刷新流程

每轮只处理一个公司。

1. 读取：
   - `0_总览/cn_consumer_refresh_queue.md`
   - `0_总览/company_score_table.md`
   - `02_公司研究/{公司}/PROMPT.md`
   - `02_公司研究/{公司}/company_research.md`
   - `02_公司研究/{公司}/scorecard.md`
   - `02_公司研究/{公司}/evidence_log.md`
   - `02_公司研究/{公司}/next_questions.md`
2. 找出当前弱证据：
   - Wikipedia 财务数据
   - Google Finance-only 估值/目标价
   - StockAnalysis-only 财务但缺官方文件
   - 过旧年份数据，如 CRRC 2018 财务
   - 异常值，如分众传媒 2021 operating income 大于 revenue
3. 设计中英文关键词，而不是只搜公司名。
4. 优先补齐 4 个证据桶中的至少 3 个：
   - 财报/经营：收入、利润、毛利率、经营利润率、现金流、用户、订单、GMV、门店、海外收入、产能等。
   - 估值/市场预期：市值、P/E、EV/Sales、分析师预期、回购、股价区间、同业估值。
   - 结构性变化：品牌/IP、出海、EV/AIoT、本地生活、Temu、内容社区、制造出海、广告点位数字化等。
   - 失败条件：监管、竞争、利润率反转、需求证伪、渠道库存、海外扩张失败、地缘政治、融资/稀释。
5. 至少打开并记录 3 条高质量链接；若官方源可用，至少 2 条必须来自官方/交易所/监管源。
6. 跑本地投资分析 skills：
   - 先跑 `ljg-invest`，基于刷新后的证据重新判断结构变化、飞轮、权力来源、市场旧眼睛和失败条件。
   - 再跑 `comprehensive-analysis`，基于刷新后的证据重新判断财报趋势、估值隐含预期、消息面/催化剂、市场情绪、流动性环境和 6-12 个月验证信号。
   - 不要照搬任何“买入/卖出”建议；把 skill 输出转译为本项目的分类、分数、验证信号、风险和 3 年翻倍路径。
7. 融合 agent-reach 官方证据、`ljg-invest`、`comprehensive-analysis` 三层结论。
8. 更新公司 4 文件和总表：
   - `company_research.md`
   - `scorecard.md`
   - `evidence_log.md`
   - `next_questions.md`
   - `0_总览/company_score_table.md`
   - `0_总览/run_log.md`
9. 更新 `cn_consumer_refresh_queue.md` 状态。

## 推荐查询模板

港股公司：
- `{公司中文名} {港股代码} 年度业绩 2025 收入 利润 毛利率`
- `{company} {ticker} annual results 2025 revenue profit margin HKEX`
- `{company} investor relations annual report 2025 results presentation`
- `{公司中文名} 海外收入 门店 GMV 用户 竞争 监管`

ADR / 双上市：
- `{company} annual report 20-F 2025 revenue net income margin SEC`
- `{company} investor relations quarterly results 2026 Q1`
- `{company} analyst expectations valuation market cap 2026`
- `{公司中文名} 用户 收入结构 利润率 竞争 风险`

A 股 / A+H：
- `{公司中文名} 2025 年报 营业收入 净利润 毛利率 现金流`
- `{公司中文名} {A股代码} 公告 年度报告 2025 CNINFO`
- `{company} annual report HKEX SSE revenue profit margin`
- `{公司中文名} 出海 竞争 监管 地缘风险`

## 官方源优先级

港股 / A+H：
1. HKEXnews 公告、年报、中报、业绩公告、招股书
2. 公司 IR、结果公告、investor presentation
3. SSE / SZSE / CNINFO 公告和年度报告
4. StockAnalysis、交易所行情页、主流财经媒体做 cross-check

A 股：
1. CNINFO 巨潮资讯年度/季度报告
2. SZSE / SSE 公告页
3. 公司官网 IR / 投资者关系
4. 可信聚合源做 cross-check

ADR / 双上市：
1. SEC EDGAR 20-F、6-K、F-1/S-1
2. 公司 IR 财报、presentation、press release
3. HKEXnews 双重主要上市/二次上市公告
4. StockAnalysis 仅作聚合校验

## evidence_log.md 必须追加字段

每家公司必须新增或更新：

```markdown
## CN refresh source coverage

- refresh date:
- cutoff date:
- source route:
- preflight cache used:
- agent-reach availability:
- official links:
- fallback links:
- replaced stale evidence:
- evidence buckets covered:
- ljg-invest conclusion:
- comprehensive-analysis conclusion:
- final evidence status: evidence_complete / evidence_limited_after_fallback / blocked_source_unavailable
- remaining gaps:
```

并为每条关键证据记录：

| source_name | source_type | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|

`source_type` 只能使用：
- official_ir
- exchange_announcement
- regulator_filing
- annual_report
- interim_report
- prospectus
- data_aggregator_crosscheck
- credible_media_crosscheck
- wikipedia_background_only

## company_research.md 更新要求

刷新后必须包含：
1. 一句话结构性转变判断。
2. Source coverage status：官方源、agent-reach/Jina 路径、剩余缺口。
3. `ljg-invest` 结论：秩序创造机器判定、结构变化、飞轮、权力来源、失败条件。
4. `comprehensive-analysis` 结论：财报趋势、消息面/催化剂、估值预期、市场情绪、流动性环境。
5. 融合判断：真瓶颈、定价权、利润率变化、竞争/监管。
6. 竞争、监管、失败条件。
7. 未来 6-12 个月验证信号。
8. 3 年翻倍路径：有 / 弱 / 无 / 不可验证。
9. 分类和分数。

## 评分和分类规则

评分仍使用 70 分框架，不因为数据更多就自动上调。

必须下调或维持低分的情况：
- 官方数据证明增长放缓、利润率恶化或自由现金流转弱。
- 估值已隐含高增长但缺少 3 年翻倍路径。
- 结构性变化只是业务扩张，不形成稀缺瓶颈或定价权。

允许上调的情况：
- 官方财报和经营数据证明增长、利润率、现金流、定价权同时改善。
- 结构性变化有明确经营指标验证。
- 估值与 3 年翻倍路径之间出现可量化不对称。

`company_score_table.md` 中不允许继续把这些内容作为主要依据：
- `净利率~6.1%(2018⚠️)`
- `2021 Wikipedia数据异常`
- `Wikipedia-only`
- `Google Finance-only`
- `英文覆盖少` 但没有 agent-reach 官方源尝试记录

## 循环收尾：score -> pool 自动映射

当 11 家公司没有 `pending`，且没有 `blocked_source_unavailable` 时，进入收尾。

以 `0_总览/company_score_table.md` 为唯一分数和分类来源，同步：
1. `04_投资池/核心候选池.md`
2. `04_投资池/观察池.md`
3. `04_投资池/期权池.md`
4. `04_投资池/中国消费与品牌池.md`
5. `04_投资池/暂不研究池.md`

映射规则：
- 目标 11 家公司固定进入 `中国消费与品牌池.md`，按总分降序，不再重复放入 `期权池.md` 或 `观察池.md`。
- 非目标公司中，`分类` 以 `核心候选` 开头的进入 `核心候选池.md`。
- 非目标公司中，`分类` 以 `观察` 开头的进入 `观察池.md`，保留上档/中档/下档/基准分段。
- 非目标公司中，`分类` 以 `期权` 开头的进入 `期权池.md`。
- 非目标公司中，`分类` 以 `暂不研究` 开头的进入 `暂不研究池.md`。
- 分数为 `—` 的非公司标的保留在暂不研究池。

收尾校验：
1. 中国消费与品牌池必须正好包含 11 家目标公司。
2. 5 个池文件中的公司与 `company_score_table.md` 分类一致。
3. 目标 11 家不在其他池中重复出现。
4. 用 `rg` 检查总表不再把旧 Wikipedia/Google Finance-only 弱证据作为主要财务依据。
5. `run_log.md` 记录预检结果、每家公司刷新状态、池文件同步结果。

全部完成且证据可追溯后，输出：
`<promise>AI_CN_CONSUMER_REFRESH_COMPLETE</promise>`

## Loop 启动命令

```text
/loop 20 min "读取 /Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索/0_总览/LOOP_PROMPT_CN_CONSUMER_REFRESH.md。你是 AI_CN_CONSUMER_REFRESH_LOOP：只刷新 Xiaomi、Pop Mart、Meituan、PDD、Beike、Bilibili、Miniso、CRRC、Fuyao Glass、Aux Electric、分众传媒。每轮只处理一家公司；使用当前工作环境，不进入额外 sandbox；全自动执行，不打断用户，不为常规工具调用请求确认；自行调用当前会话可用的 MCP 工具；先做一次 MCP/agent-reach/Jina/Exa 预检并缓存；agent-reach 为主要补证路径；不硬等 Exa；优先官方IR、交易所公告、年报/季报、公司公告和可信聚合源；替换 Wikipedia/Google Finance-only 的旧证据；补证后必须重新使用 ljg-invest 和 comprehensive-analysis 做结构判断、财报、估值、情绪和验证信号分析；每家公司更新 company_research.md、scorecard.md、evidence_log.md、next_questions.md、company_score_table.md；完成 11 家后按分数表同步 5 个投资池；全部完成且证据可追溯后输出 <promise>AI_CN_CONSUMER_REFRESH_COMPLETE</promise>。" --max-iterations 40 --completion-promise "AI_CN_CONSUMER_REFRESH_COMPLETE"
```
