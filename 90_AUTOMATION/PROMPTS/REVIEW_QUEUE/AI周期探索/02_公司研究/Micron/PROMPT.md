---
title: "PROMPT"
date: 2026-07-24
updated: 2026-07-24
layer: AUTOMATION
primary_role: legacy_company_prompt
status: superseded
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: operational
legacy_metadata_added: true
legacy_path: "AI周期探索/02_公司研究/Micron/PROMPT.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Micron 调研执行 Prompt

你现在只研究这一家公司，不要顺手研究其他公司。

公司：Micron
代码：MU
初始分组：AI内存/HBM瓶颈

核心问题：
> Micron 是否正在发生结构性转变？这种变化能不能带来定价权、利润率改善、竞争位置变化或估值中枢变化？

## 固定 SOP：Mindspace MCP + 双 Skill 流转

### 1. 先跑 Mindspace Source MCP
目的：控制信息源输入，先从本地 mindspace 高质量信源找证据；禁止先自由 web search，禁止使用内置 `web_search`。

必须按顺序执行：
- 读取 `../../0_总览/MINDSPACE_SOURCE_MCP_SOP.md`。
- 调用 `mindspace-source.health_check`。
- 如果 `health_check` 失败：停止本公司研究，写入 `evidence_log.md` 和 `../../0_总览/run_log.md`，不要改 `company_queue.md` 为 completed。
- 调用 `mindspace-source.list_channels(active_only=true, limit=50)`。
- 选择名称/描述最匹配投资、股票、AI、科技、消费、品牌、基础设施的 channel。
- 调用 `mindspace-source.inspect_source_coverage(channel_id, days_back=90)`。
- 调用 `mindspace-source.list_channel_sources(channel_id)`。
- 用 `mindspace-source.search_articles(...)` 搜索结构变化、财报/验证信号、消息面/情绪。
- 对支撑核心判断的文章，必须调用 `mindspace-source.get_article_detail(source_id, item_id)` 回源。

默认搜索窗口：
- 结构性变化：`days_back=365`
- 消息面 / 情绪 / 催化剂：`days_back=90`
- 财报 / 近期验证信号：`days_back=180`

source_tab 优先级：
- 一手事实：`filing_feed`、`official_press`、`announcement`
- 结构判断：`report`、`data aggregator`、`blog`、`newsletter`
- 市场情绪：`media`、`forum`、`podcast`

证据规则：
- `podcast` 只作补充，不单独支撑核心结论。
- 核心判断至少需要 2 条高质量证据。
- 只有媒体、论坛、播客时，结论必须降置信度。
- MCP 覆盖不足时允许换关键词重试 3 轮；仍不足再标注“Mindspace 覆盖不足”。
- fallback 联网搜索只能在 MCP 覆盖不足且问题关键时使用；禁止内置 `web_search`，只能使用 `agent-reach`，并必须写明原因、关键词和链接。

### 2. 再跑 ljg-invest
目的：判断结构性变化，不看短期股价。

必须提炼：
- 这家公司是不是秩序创造机器？
- 它的飞轮是什么？飞轮是否已经转起来？
- 它控制了什么别人拿不走的东西？
- 市场正在用什么旧眼睛看它？
- 它的结构性变化失败条件是什么？

### 3. 再跑 comprehensive-analysis
目的：判断二级市场当下状态。

必须提炼：
- 近期财报和经营趋势。
- 近期消息面和催化剂。
- 当前估值隐含了什么预期。
- 市场情绪是过热、合理还是低估。
- 未来 6-12 个月最重要的验证信号。

注意：不要照搬买入 / 卖出建议，只把结果转成研究判断。

### 4. 最后融合
把 MCP 证据、结构性变化判断、二级市场状态合成一份研究结论，写入本目录文件。

## 本公司专用框架

- 是否处在 AI 需求外溢后的真实瓶颈？
- 供给是否慢于需求？
- 紧缺时能否涨价？
- 涨价后利润是否留在公司？
- 周期反转时最大风险是什么？


## 输出文件

更新本公司目录下：
- `company_research.md`
- `scorecard.md`
- `evidence_log.md`
- `next_questions.md`

同时更新：
- `../../0_总览/company_score_table.md`
- `../../0_总览/company_queue.md`
- `../../0_总览/run_log.md`

## company_research.md 写作结构

1. 一句话结构性转变判断
2. Mindspace MCP 证据摘要：关键来源 / source_tab / 核心证据 / 覆盖不足
3. ljg-invest 结论：结构变化 / 飞轮 / 权力来源 / 失败条件
4. comprehensive-analysis 结论：财报趋势 / 消息面 / 估值预期 / 情绪 / 催化剂
5. 融合判断：真瓶颈、定价权、利润率变化
6. 未来 6-12 个月验证信号
7. 3 年翻倍路径：有 / 弱 / 无，以及原因
8. 分类：核心候选 / 观察 / 期权 / 中国消费与品牌 / 暂不研究
9. 下一步最需要验证的问题

## 硬约束

- 不要写泛泛公司介绍。
- 不要把“有 AI 功能”当作 AI 受益。
- 不要输出直接买卖建议。
- 不要编造资料；资料不足写入 `evidence_log.md`。
- 不允许先自由 web search；禁止使用内置 `web_search`；必须先完成 Mindspace MCP 检索。
- MCP 不可用时，本轮研究 blocked，状态保持 pending。
- MCP 覆盖不足且问题关键时，fallback 只能使用 `agent-reach` skill 联网搜索。
- 消费 / 品牌 / 广告公司不要硬套科技 AI 框架。
