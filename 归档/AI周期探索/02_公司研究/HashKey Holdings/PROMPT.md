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
legacy_path: "AI周期探索/02_公司研究/HashKey Holdings/PROMPT.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# HashKey Holdings 调研执行 Prompt

你现在只研究这一家公司，不要顺手研究其他公司。

公司：HashKey Holdings
代码：03887.HK
IPO：2025年12月17日，发行价 HKD 6.68
当前股价：~HKD 4.55（截至2026年5月）
市值：~HKD 126亿
初始分组：港股数字资产期权

核心问题：
> HashKey 是否从"香港持牌加密交易所"变成"亚洲合规数字资产基础设施平台"？

研究意图：旧分析结论是"HashKey = 牌照仓库，不是秩序创造机器"。这次用 Skill 方法论重新审视，目标是用更严谨的框架寻找被忽略的结构性变化信号，可能推翻旧结论。

## 固定 SOP：Mindspace MCP + 双 Skill 流转

### 1. 先跑 Mindspace Source MCP
目的：控制信息源输入，先从本地 mindspace 高质量信源找证据；禁止先自由 web search，禁止使用内置 `web_search`。

必须按顺序执行：
- 读取 `../../0_总览/MINDSPACE_SOURCE_MCP_SOP.md`。
- 调用 `mindspace-source.health_check`。
- 如果 `health_check` 失败：停止本公司研究，写入 `evidence_log.md` 和 `../../0_总览/run_log.md`，不要改 `company_queue.md` 为 completed。
- 调用 `mindspace-source.list_channels(active_only=true, limit=50)`。
- 选择名称/描述最匹配投资、股票、加密、数字资产、Web3、区块链的 channel。
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
- MCP 覆盖不足时允许换关键词重试 3 轮；仍不足再标注"Mindspace 覆盖不足"。
- fallback 联网搜索只能在 MCP 覆盖不足且问题关键时使用；禁止内置 `web_search`，只能使用 `agent-reach`，并必须写明原因、关键词和链接。

### 2. 再跑 ljg-invest
目的：判断结构性变化，不看短期股价。

必须提炼：
- 这家公司是不是秩序创造机器？旧分析说不是——要刻意挑战这个结论。
- 它的飞轮是什么？飞轮是否已经转起来？旧分析说"交易量+72% 但收入+0.33% 证明飞轮不转"——Omnibus 模式的机构关系是否有长期战略价值？
- 它控制了什么别人拿不走的东西？牌照？资金流？机构信任？数字资产服务标准？
- 市场正在用什么旧眼睛看它？如果不用"交易所"估值框架，应该用什么？
- 亏损是否在建立护城河（像 Coinbase 早期），还是纯消耗？
- 稳定币 48% 占比是噪音还是法币↔数字资产桥梁的信号？
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

### 核心命题
HashKey 是否从"香港持牌加密交易所"变成"亚洲合规数字资产基础设施平台"？

### 旧分析盲区（重点突破）
旧双轨报告结论是"牌照仓库，不是秩序创造机器"。以下 6 个判断可能存在盲区，刻意挑战：

1. **"飞轮不转"** — 交易量+72% 但收入+0.33%。但 Omnibus 模式的机构关系是否比短期手续费更有长期价值？
2. **"合规成本 > 收入"** — 亏损被解读为纯消耗。但早期基础设施公司（Coinbase 早期也巨额亏损）的亏损是否在建立护城河？
3. **"香港市场天花板低"** — 700 万人口是散户天花板。但 HashKey 的目标可能是机构入口，不是散户交易所。全球合规布局（百慕大/爱尔兰/迪拜）是否在搭建网络？
4. **"OKX 获牌 = 死亡"** — 竞争被简单化为零和博弈。但合规市场可能是多玩家共存的市场。
5. **"稳定币 48% 被轻视"** — 如果稳定币是 RWA/代币化的前哨站，HashKey 可能正在成为法币↔数字资产的桥梁。
6. **"P/S 8.77x 太贵"** — 和 Coinbase 比确实贵。但如果叙事是"合规基础设施"而非"交易所"，估值框架是否应该不同？

### Key Research Spine

**核心变量**：
- 香港 SFC 零售 VATP 牌照（首批仅 2 张：HashKey + OSL）
- FY2025 营收 HKD 7.23 亿，YoY +0.33%；平台资产 HKD 184 亿（+60.5%）
- 交易量 HKD 5,300 亿（+72.3%），Omnibus 过账模式驱动
- 稳定币交易量占比 48%
- 4 年累计亏损超 HKD 28 亿
- OKX 香港牌照申请为最大竞争威胁

**二级市场变量**：
- 股价 HKD 4.55（IPO 至今 -31.9%），52 周区间 HKD 3.88-7.98
- P/S 8.77x（从 15.2x 回落），P/B 4.21x
- 日均换手率 ~0.1%，流动性极差
- 3 位分析师覆盖，平均目标价 HKD 7.17（+68%）
- 2026 年 6 月基石解禁（UBS、Fidelity、鼎晖），12 月控股股东解禁
- BTC 处于调整期

### 信息源层
- HKEX 公告：https://www1.hkexnews.hk/search/titlesearch.xhtml（搜索 03887.HK）
- HKEX 个股页：https://www.hkex.com.hk/Market-Data/Securities-Prices/Equities/Equities-Quote?sym=3887&sc_lang=en
- HashKey 2025 年报（HKEX 披露）
- 行业数据：CoinGecko（BTC/ETH 价格、Fear & Greed）、Coinbase 财报
- 竞品：OSL/BC Technology (0863.HK)、OKX 牌照进展、Coinbase (COIN)
- 市场行情：腾讯财经 API、新浪财经、东方财富
- Mindspace MCP 检索（按现有 SOP 执行）

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

1. **一句话判断**：用 ljg-invest 风格回答"牌照仓库还是合规基础设施平台"
2. **证据底座**：HKEX 公告、年报、行业数据、竞品、市场行情五类来源
3. **秩序创造机器**（刻意挑战旧结论）：
   - 飞轮：合规牌照→机构信任→资金流入→交易量增长→收入增加。旧分析说飞轮不转，验证 Omnibus 机构关系是否有长期价值
   - 冲击后是否变强：加密熊市/OKX 获牌/监管收紧，HashKey 能否变强？还是直接被淘汰？
   - 资源是否自己来：用户/资金是冲着 HashKey 来，还是冲着香港牌照来？
   - 权力来源：牌照稀缺性 vs 网络效应 vs 资金流控制 vs 标准制定权
   - 失败条件：OKX 获牌、加密长期熊市、香港政策转向、Omnibus 收入永远不转化
   - **重点验证**：稳定币 48% 占比是否指向更大的结构性机会（RWA/代币化/法币桥）
4. **二级市场状态**：
   - 财报趋势：营收停滞、亏损持续、稳定币亮点
   - 估值隐含预期：P/S 8.77x 隐含什么增长预期
   - 情绪/资金面：解禁压力、分析师覆盖、加密市场情绪
   - 未来 6-12 个月催化剂：6 月解禁、OKX 牌照、2026Q2 财报、稳定币立法
5. **融合判断**（旧结论是"牌照仓库"，这次要给出新证据）：
   - 真瓶颈：合规成本 > 收入是旧判断，需验证是否有新信号
   - 定价权：旧判断为零（用户无转换成本），重新审视机构端是否有粘性
   - 利润率：旧判断为负（持续亏损无盈利路径），看 Coinbase 路径是否可比
   - 三年翻倍路径：旧判断为无，找到具体变量
   - 分类与 scorecard 重算：如果推翻旧结论，分数应显著从 17/70 上调
6. 分类：核心候选 / 观察 / 期权 / 中国消费与品牌 / 暂不研究
7. 下一步最需要验证的问题

## 硬约束

- 不要写泛泛公司介绍。
- 不要把"有 AI 功能"当作 AI 受益。
- 不要输出直接买卖建议。
- 不要编造资料；资料不足写入 `evidence_log.md`。
- 不允许先自由 web search；禁止使用内置 `web_search`；必须先完成 Mindspace MCP 检索。
- MCP 不可用时，本轮研究 blocked，状态保持 pending。
- MCP 覆盖不足且问题关键时，fallback 只能使用 `agent-reach` skill 联网搜索。
- 每个核心判断至少 2 条证据，至少 1 条一手来源（HKEX 公告/年报）。
- 明确区分 Omnibus 过账交易量和真实手续费收入。
- 区分平台资产规模和资产管理收入。
- 不用 Wikipedia 支撑核心判断。
- 情绪面必须有市场数据和公告支撑，不能只写"加密热"。
- 不是消费 / 品牌 / 广告公司，不要硬套消费框架。
