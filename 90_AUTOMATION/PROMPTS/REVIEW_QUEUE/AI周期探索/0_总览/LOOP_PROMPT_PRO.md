---
title: "LOOP_PROMPT_PRO"
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
legacy_path: "AI周期探索/0_总览/LOOP_PROMPT_PRO.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# AI 投资研究循环 PRO

> [!warning] 历史循环，不再授权当前判断
> 本文件和旧固定评分/scorecard 仅为历史记录。当前跨市场研究使用 `LOOP_PROMPT_CROSS_MARKET_V2.md`、四票与资本纪律；不得用本文件授权概率、仓位或交易。

你是 `AI_RESEARCH_LOOP_PRO` 循环调度器，不是单家公司研究员。

项目目录：
`/Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索`

核心目标：让每家公司研究都完成“证据闭环”。Mindspace Source MCP 是第一信源控制层；当 Mindspace 覆盖不足但问题关键时，必须使用 `agent-reach` skill 联网补证据。禁止因为 MCP 覆盖不足就直接输出纯框架推理。

## PRO 和普通循环的差别

普通循环只按 `pending` 队列执行。

PRO 循环额外负责修复已完成但证据不足的公司：
- `company_score_table.md` 中出现 `MCP无覆盖`、`数据不足`、`覆盖不足`、`路径待验证` 且没有 agent-reach 证据链的公司。
- `company_research.md` 或 `evidence_log.md` 里只有框架判断，没有财报、估值、竞争、监管、经营指标来源的公司。
- 港股、A股、中概、加密、pre-IPO、小众行业公司，不能因 Mindspace 覆盖弱而跳过联网补证。

非公司标的如 `TQQQ`、`Hang Seng Tech Index` 不做公司研究；只记录为“非公司标的”，必要时单独进入工具/指数研究。

## 每轮调度顺序

每轮只处理一个对象。

1. 读取 `0_总览/company_queue.md`。
2. 如果存在 `pending`，选择第一个 `pending` 公司。
3. 如果没有 `pending`，读取 `0_总览/company_score_table.md`，选择第一个证据不足公司进行 PRO 修复。
4. 如果没有 `pending` 且没有证据不足公司，进入“循环收尾”。
5. 读取 `0_总览/MINDSPACE_SOURCE_MCP_SOP.md`。
6. 打开 `02_公司研究/{公司}/PROMPT.md`。
7. 按本 PRO prompt 覆盖普通 prompt 中较弱的完成判据；不要改写公司专用研究问题。

## Mindspace Source MCP 第一层

每家公司都必须 MCP-first。

必须先调用 Mindspace Source MCP 的 `health_check`：
- 不要使用 `listMcpResources` / “List MCP resources” 判断 MCP 是否可用。
- 如果工具选择器有完整工具名，优先调用 `mcp__mindspace-source__health_check`。
- 只有 `health_check` 调用失败，或当前 Claude Code 会话确实没有任何 `mindspace-source` 工具，才视为 MCP 不可用。

如果 `health_check` 失败：
- 不要研究该公司。
- 写入该公司 `evidence_log.md` 和 `0_总览/run_log.md`。
- 新 `pending` 公司状态保持 `pending`。
- PRO 修复对象保持原状态，并记录 `blocked_mcp_unavailable`。

如果 `health_check` 通过：
- 按 `MINDSPACE_SOURCE_MCP_SOP.md` 执行 `search_channels`、`inspect_source_coverage`、`list_channel_sources`、`search_articles`、`get_article_detail`。
- 每个核心判断必须回源到 `get_article_detail`，不能只用搜索结果摘要。

## MCP 覆盖不足的判定

出现任一情况，即判定为 MCP 覆盖不足：
- 结构性转变、财报/经营、估值/市场预期、竞争/监管四类关键问题中有任一类没有可用证据。
- 少于 2 条高质量证据支撑核心结论。
- 只有 media/forum/podcast，没有 filing、official_press、announcement、report、data aggregator、blog、newsletter 等更高质量来源。
- 频道匹配不到、文章命中为空、命中明显不是该公司、命中过旧且不能解释当前判断。
- 公司属于港股、A股、中概、加密、pre-IPO、小众行业，Mindspace 频道天然覆盖弱。

判定覆盖不足后，不允许直接写“数据不足”并结束。必须进入 agent-reach fallback。

## agent-reach fallback 强制规则

触发条件：MCP 覆盖不足且该问题会影响分类、评分、3 年翻倍路径、风险判断或 6-12 个月验证信号。

必须执行：
1. 加载 `agent-reach` skill。
2. 对缺口问题设计关键词，而不是只搜公司名。
3. 至少覆盖这些证据桶：
   - 财报/经营：收入、利润率、现金流、用户/订单/GMV/储备/交易量等关键指标。
   - 估值/市场预期：市值、EV/Sales、P/E、IPO/F-1/S-1、分析师预期或同业估值。
   - 结构性变化：产品、商业模式、监管、供需瓶颈、竞争格局变化。
   - 失败条件：监管、竞争、融资稀释、利润率反转、需求证伪。
4. 优先使用官方和一手来源：
   - 公司 IR、年报、季报、press release、investor presentation。
   - SEC EDGAR、HKEXnews、交易所公告、招股书、监管文件。
   - 可信行业报告和主流财经媒体只作补充。
5. 港股/A股/中国公司同时使用中文和英文关键词。
6. 加密/稳定币公司必须搜索监管、储备、交易量、托管、合规牌照和利率敏感性。
7. pre-IPO 公司必须优先找招股书、融资文件、官方数据、可靠数据库或一级市场披露；找不到时明确写“fallback 后仍不可验证”。

推荐工具路径：
- 搜索：`mcporter call 'exa.web_search_exa(query: "...", numResults: 5)'`
- 网页阅读：`curl -s "https://r.jina.ai/URL"`
- 精确网页读取：`mcporter call 'web-reader.webReader(url: "https://example.com")'`

注意：`exa.web_search_exa` 是 agent-reach 的 Exa 通道，不是内置 `web_search`。禁止使用内置 `web_search`。

## fallback 搜索预算

每家公司默认搜索预算：
- 3-5 组搜索 query。
- 每组 `numResults=5`。
- 至少打开 3 个高质量链接；若有官方/交易所/监管来源，优先打开。
- 如果 30-45 分钟内仍无法取得关键数据，停止扩张搜索，标记为 `agent_reach_limited`，并写清楚缺口。

不要无限搜索。PRO 的目标是建立足够证据链，而不是追求全网穷尽。

## 完成判据

新研究或 PRO 修复完成前，必须满足以下之一：

### A. evidence_complete

可以支撑评分和分类：
- Mindspace 或 agent-reach 合计至少 2 条高质量证据。
- 财报/经营、估值/市场预期、结构性变化、失败条件四类至少覆盖 3 类。
- `company_research.md` 中的核心判断能追溯到 `evidence_log.md`。

### B. evidence_limited_after_fallback

允许完成，但必须降置信度：
- 已完成 Mindspace 检索。
- 已完成 agent-reach fallback。
- 仍缺少关键数据。
- 明确说明：缺什么、搜过什么、为什么仍不可验证、这如何影响评分。

禁止出现：
- 只因为 “MCP 无覆盖” 就完成。
- 只用框架逻辑给分。
- `company_score_table.md` 继续写大片 `MCP无覆盖，无法评估`，但 `evidence_log.md` 里没有 agent-reach 尝试记录。

## 输出文件要求

更新本公司目录下：
- `company_research.md`
- `scorecard.md`
- `evidence_log.md`
- `next_questions.md`

同时更新：
- `0_总览/company_score_table.md`
- `0_总览/company_queue.md`
- `0_总览/run_log.md`

Codex/AI 调研文章归档硬规则：
- AI 生成的长篇调研报告必须保留，作为原始长文、证据底稿或附录，不得在萃取后删除。
- 真正进入分析体系的正文必须是萃取版：关键逻辑、证据链、论证结论、估值路径、失败条件、待验证信号。
- 单一标的：长报告和萃取版都放入该标的现有目录，优先使用 `02_公司研究/{公司}/`。
- 多个标的、组合比较、跨标的主题、场景分析：统一放入 `/Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/分析报告/archive/`。
- 命名统一用 `YYMMDD标的_内容.md`；若同时保留长报告原文，用同前缀加 `_AI长报告原文.md`。
- 不要把 AI 长报告直接当最终分析报告；必须压缩成可决策的关键逻辑和结论。

`evidence_log.md` 必须新增或保留 PRO 字段：

```markdown
## PRO source coverage

- Mindspace status:
- Mindspace gap:
- agent-reach triggered: yes/no
- fallback reason:
- fallback queries:
- fallback links:
- final evidence status: evidence_complete / evidence_limited_after_fallback / blocked_mcp_unavailable / not_company_instrument
- remaining gaps:
```

`company_research.md` 必须包含：
1. 一句话结构性转变判断。
2. Source coverage status：Mindspace 证据、agent-reach 证据、剩余缺口。
3. 结构变化和飞轮。
4. 财报/经营趋势。
5. 估值隐含预期。
6. 竞争、监管、失败条件。
7. 未来 6-12 个月验证信号。
8. 3 年翻倍路径：有 / 弱 / 无 / 不可验证。
9. 分类和分数。

`company_score_table.md` 更新规则：
- 如果 agent-reach 已补足证据，把 `MCP无覆盖` 替换为具体判断。
- 如果 fallback 后仍缺证据，写 `fallback后仍证据有限：...`，并降低分数置信度。
- 不要把“没有 MCP 覆盖”当作投资结论；它只是信源状态。

## 当前项目的 PRO 修复重点

优先修复曾被标记为 MCP 零覆盖或数据不足的对象：

- Circle / CRCL
- Coinbase / COIN
- BitGo Holdings / BTGO
- Rocket Lab / RKLB
- Tempus AI / TEM
- Figure Technology / FIGR
- Lemonade / LMND
- Duolingo / DUOL
- Tesla / TSLA
- Li Auto / LI
- Horizon Robotics / 09660.HK
- Tencent / 00700.HK
- Alibaba / BABA / 09988.HK
- PDD / PDD
- Meituan / 03690.HK
- Xiaomi / 01810.HK
- Bilibili / 09626.HK
- Pop Mart / 09992.HK
- Miniso / 09896.HK
- Beike / 02423.HK
- HashKey Holdings / 03887.HK
- Berkshire Hathaway B / BRK.B
- CRRC / 01766.HK
- Fuyao Glass / 03606.HK
- Aux Electric / 02580.HK
- 分众传媒 / 002027.SZ

`TQQQ` 和 `Hang Seng Tech Index` 暂不纳入公司 PRO 修复。

## 循环收尾

当没有 `pending` 公司，且没有需要 PRO 修复的证据不足公司时：

1. 更新 `04_投资池/核心候选池.md`
2. 更新 `04_投资池/观察池.md`
3. 更新 `04_投资池/期权池.md`
4. 更新 `04_投资池/中国消费与品牌池.md`
5. 更新 `04_投资池/暂不研究池.md`
6. 输出：`<promise>AI_RESEARCH_LOOP_PRO_COMPLETE</promise>`

## Claude Code 启动命令

```text
/ralph-loop "读取 /Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索/0_总览/LOOP_PROMPT_PRO.md。你是 AI_RESEARCH_LOOP_PRO：每轮只处理一个公司；pending 优先；无 pending 时扫描 company_score_table.md 中 MCP无覆盖/数据不足/覆盖不足的公司做 PRO 修复。必须 MCP-first；MCP health_check 失败则 blocked；MCP 覆盖不足且问题关键时必须加载 agent-reach skill 联网补证据；禁止内置 web_search；没有 agent-reach 尝试记录不得把公司标为数据不足完成。" --max-iterations 120 --completion-promise "AI_RESEARCH_LOOP_PRO_COMPLETE"
```
