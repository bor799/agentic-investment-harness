---
title: "MINDSPACE_SOURCE_MCP_SOP"
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
legacy_path: "AI周期探索/0_总览/MINDSPACE_SOURCE_MCP_SOP.md"
migration_target: "02_术/SKILLS + 90_AUTOMATION"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Mindspace Source MCP SOP

目标：所有公司研究先经过 Mindspace Source MCP 控制信源，再进入投资分析。禁止先自由 web search，禁止使用内置 `web_search`。

## Claude Code 工具识别规则

- Mindspace Source MCP 是工具型 MCP，不是资源型 MCP。
- 不要用 `listMcpResources` / “List MCP resources” 判断它是否可用；资源列表为空不代表 MCP 工具不可用。
- 在 Claude Code 中应直接调用 `mindspace-source` 暴露的工具：
  - `health_check`
  - `search_channels`
  - `list_channels`
  - `list_channel_sources`
  - `search_articles`
  - `get_article_detail`
  - `inspect_source_coverage`
- 如果工具选择器中出现完整工具名，优先使用 `mcp__mindspace-source__health_check` 这类 `mcp__{server}__{tool}` 工具名。
- 只有在实际调用 `health_check` 返回失败，或 Claude Code 当前会话确实没有任何 `mindspace-source` 工具可选时，才视为 MCP 不可用。

## 固定工具顺序

1. `health_check`
   - 必须先通过。
   - 如果失败，本轮公司研究停止，写入该公司 `evidence_log.md` 和 `0_总览/run_log.md`，公司状态保持 `pending`。

2. `search_channels(query, source_tabs, active_only=true, limit=50)`
   - 这是频道选择的主入口，不要先用 `list_channels` 翻频道。
   - `query` 必须包含公司名、ticker 和研究主题关键词，例如 `Microsoft MSFT AI enterprise software margin earnings`。
   - `source_tabs` 必须优先使用高质量信源类型：
     - `filing_feed`
     - `official_press`
     - `announcement`
     - `report`
     - `data aggregator`
     - `blog`
     - `newsletter`
     - `article`
     - `media`
     - `forum`
   - 默认不要把 `podcast` 放进频道发现阶段；podcast 只能作为后续补充证据。
   - MCP 服务端只返回置信度最高的 top 50 channel candidates，这是硬上限。
   - agent 只能在这 50 个候选中选择 1-3 个最相关 channel 继续查 MongoDB 文章。
   - 如果前 3 个候选没有找到可用文章，最多继续尝试到第 5 个候选；禁止把 50 个候选逐个全部打穿。
   - 如果 top 50 里没有合理候选，记录“频道匹配不足”，不要扩大到全库扫描。

3. `list_channels(active_only=true, limit=50, offset=0)`
   - 仅用于诊断或 `search_channels` 明显失效后的兜底。
   - 频道浏览必须分页，不能一次性拉全量频道。
   - 每次只允许请求 `limit=50`。
   - 最多只允许查看 6 页：`offset=0,50,100,150,200,250`，总浏览上限 300 个频道。
   - 禁止为了寻找更优 channel 扫描 500、1000、5000、40000 个频道；这会超出 agent 的上下文和判断上限。

4. `inspect_source_coverage(channel_id, days_back=90)`
   - 检查该 channel 的信源覆盖和近 90 天文章分布。
   - 如果覆盖很弱，仍继续尝试搜索，但在 `evidence_log.md` 记录“Mindspace 覆盖不足”。

5. `list_channel_sources(channel_id)`
   - 记录可用信源结构，尤其是 `source_tab_counts`。
   - 优先使用一手事实源和高质量结构判断源。

6. `search_articles(...)`
   - 只能对 `search_channels` 选出的少量 channel 执行。
   - 每家公司研究最多对 5 个候选 channel 执行 `search_articles`。
   - 每个 channel 每组关键词默认 `limit=10`，必要时最多 `limit=20`。
   - 结构性变化：`days_back=365`
   - 消息面 / 情绪 / 催化剂：`days_back=90`
   - 财报 / 近期验证信号：`days_back=180`

7. `get_article_detail(source_id, item_id)`
   - 对所有核心证据回源。
   - 不允许只用搜索结果摘要支撑核心结论。

## source_tab 优先级

一手事实源：
- `filing_feed`
- `official_press`
- `announcement`

结构判断源：
- `report`
- `data aggregator`
- `blog`
- `newsletter`

市场情绪源：
- `media`
- `forum`
- `podcast`

规则：
- `podcast` 只作补充，不单独支撑核心结论。
- 只有媒体、论坛、播客支撑时，结论必须降置信度。
- 核心判断至少需要 2 条高质量证据。

## 查询关键词

科技公司：
- `{company} {ticker} AI agent enterprise margin guidance earnings`
- `{company} {ticker} workflow context platform pricing retention`

基础设施公司：
- `{company} {ticker} capacity demand supply capex pricing power data center`
- `{company} {ticker} backlog utilization margin guidance`

消费品牌 / 广告公司：
- `{company} {ticker} revenue same store overseas IP advertising margin channel`
- `{company} {ticker} brand retail traffic pricing cash flow`

特别规则：
- MINISO、Pop Mart、分众传媒禁止只用 AI 查询。
- 这三类公司优先消费、渠道、广告、品牌、利润率关键词。

## fallback agent-reach 联网搜索

只有在 MCP 覆盖不足且问题关键时，才允许 fallback 联网搜索。

fallback 只能使用 `agent-reach` skill，禁止使用内置 `web_search`。

推荐 agent-reach 路径：
- 搜索：`mcporter call 'exa.web_search_exa(query: "query", numResults: 5)'`
- 网页阅读：`curl -s "https://r.jina.ai/URL"`
- 精确网页读取：`mcporter call 'web-reader.webReader(url: "https://example.com")'`

注意：这里的 `exa.web_search_exa` 是 `agent-reach` 的 Exa 搜索通道，不是内置 `web_search`。

fallback 必须写入 `evidence_log.md`：
- fallback 原因
- 搜索关键词
- 使用链接
- 为什么 MCP 结果不足

## evidence_log.md 字段

每条关键证据必须记录：

| 字段 | 要求 |
|---|---|
| source_name | MCP 返回的 source name |
| source_tab | MCP 返回的 source_tab |
| source_id | MCP source_id |
| item_id | MCP item_id |
| link | 原文链接 |
| published_at | 发布时间 |
| evidence_use | 支撑什么判断 |
| confidence | 高 / 中 / 低 |
| notes | 限制或冲突 |
