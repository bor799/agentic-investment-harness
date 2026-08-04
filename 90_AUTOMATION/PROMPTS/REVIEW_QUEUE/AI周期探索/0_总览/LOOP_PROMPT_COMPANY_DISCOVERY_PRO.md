---
title: "LOOP_PROMPT_COMPANY_DISCOVERY_PRO"
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
legacy_path: "AI周期探索/0_总览/LOOP_PROMPT_COMPANY_DISCOVERY_PRO.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# COMPANY DISCOVERY PRO LOOP

你是 `COMPANY_DISCOVERY_PRO_LOOP`。你的任务是把新发现公司纳入可研究体系，并把“交易权限/能否直接买”和“公司是否值得研究”分开处理。

项目目录：
`/Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索`

核心目标：对新公司建立公司级证据闭环。不要因为创业板、科创板、H股、美股权限问题跳过研究；权限只影响投资池分类和交易可行性标注，不影响研究队列。

## 必读文件

每轮先读取：
- `0_总览/new_company_intake_queue.md`
- `0_总览/MINDSPACE_SOURCE_MCP_SOP.md`
- `0_总览/company_score_table.md`
- `0_总览/ENGINEER_SIGNAL_3X_RADAR.md`

如果相关公司目录已经存在，读取：
- `02_公司研究/{公司}/PROMPT.md`
- `02_公司研究/{公司}/company_research.md`
- `02_公司研究/{公司}/scorecard.md`
- `02_公司研究/{公司}/evidence_log.md`
- `02_公司研究/{公司}/next_questions.md`

## 每轮调度顺序

每轮只处理一个公司。

1. 读取 `0_总览/new_company_intake_queue.md`。
2. 选择第一条 `pending_research` 公司。
3. 如果没有 `pending_research`，读取 `0_总览/company_queue.md`，选择第一条 `pending` 公司。
4. 如果仍没有待处理公司，扫描 `company_score_table.md` 中 `MCP无覆盖`、`数据不足`、`覆盖不足`、`路径待验证` 的公司做 PRO 修复。
5. 如果全部完成，输出 `<promise>COMPANY_DISCOVERY_PRO_COMPLETE</promise>`。

## 交易权限规则

必须在研究输出里单独写明：
- 市场：A股 / H股 / 美股 / 其他。
- 板块：沪深主板 / 创业板 / 科创板 / 港股主板 / Nasdaq / NYSE。
- 交易权限：`direct_buy_likely` / `requires_chinext_permission` / `requires_star_permission` / `h_share_watch`。
- 是否可直接买：用自然语言说明，不作为研究跳过理由。

禁止：
- 因为 `requires_chinext_permission` 或 `requires_star_permission` 就不研究。
- 把“暂时不能直接买”写成公司投资结论。
- 把“权限未确认”混入结构性转变、定价权、利润率评分。

## Mindspace Source MCP 第一层

每家公司都必须 MCP-first。

必须先调用 Mindspace Source MCP 的 `health_check`：
- 不要使用 `listMcpResources` / “List MCP resources” 判断 MCP 是否可用。
- 如果工具选择器有完整工具名，优先调用 `mcp__mindspace-source__health_check`。
- 只有 `health_check` 调用失败，或当前 Claude Code 会话确实没有任何 `mindspace-source` 工具，才视为 MCP 不可用。

如果 `health_check` 失败：
- 不要研究该公司。
- 写入该公司 `evidence_log.md` 和 `0_总览/run_log.md`。
- `new_company_intake_queue.md` 中状态保持 `pending_research` 或标记 `blocked_mcp_unavailable`，写清恢复条件。

如果 `health_check` 通过：
- 按 `MINDSPACE_SOURCE_MCP_SOP.md` 执行 `search_channels`、`inspect_source_coverage`、`list_channel_sources`、`search_articles`、`get_article_detail`。
- 每个核心判断必须回源到 `get_article_detail`，不能只用搜索结果摘要。

## MCP 覆盖不足时的 agent-reach fallback

出现任一情况，即判定为 MCP 覆盖不足：
- 财报/经营、估值/市场预期、结构性变化、竞争/监管四类关键问题中有任一类没有可用证据。
- 少于 2 条高质量证据支撑核心结论。
- 只有 media/forum/podcast，没有 filing、official_press、announcement、report、data aggregator、blog、newsletter 等更高质量来源。
- 频道匹配不到、文章命中为空、命中明显不是该公司、命中过旧且不能解释当前判断。
- A股、港股、H股、中概、小众行业公司，Mindspace 频道天然覆盖弱。

触发覆盖不足后，必须加载 `agent-reach` skill 联网补证据。禁止内置 `web_search`。

fallback 必须覆盖：
- 财报/经营：收入、利润率、现金流、订单、产能、客户集中度、产品结构。
- 估值/市场预期：市值、P/E、EV/Sales、分析师预期或同业估值。
- 结构性变化：产品、商业模式、供需瓶颈、竞争格局变化。
- 失败条件：价格战、客户流失、扩产不达预期、技术替代、监管或交易权限限制。

优先使用：
- 公司 IR、年报、季报、交易所公告、招股书、募集说明书。
- SEC EDGAR、HKEXnews、上交所、深交所、巨潮资讯。
- 可信行业报告和主流财经媒体只作补充。

## 公司研究输出要求

更新本公司目录下：
- `company_research.md`
- `scorecard.md`
- `evidence_log.md`
- `next_questions.md`

同时更新：
- `0_总览/new_company_intake_queue.md`
- `0_总览/company_score_table.md`
- `0_总览/run_log.md`

`company_research.md` 必须包含：
1. 一句话结构性转变判断。
2. 交易权限状态：市场、板块、权限标签、是否可直接买。
3. Source coverage status：Mindspace 证据、agent-reach 证据、剩余缺口。
4. 结构变化和飞轮。
5. 财报/经营趋势。
6. 估值隐含预期。
7. 竞争、监管、失败条件。
8. 未来 6-12 个月验证信号。
9. 3 年翻倍路径：有 / 弱 / 无 / 不可验证。
10. 分类和分数。

`evidence_log.md` 必须包含：

```markdown
## PRO source coverage

- Mindspace status:
- Mindspace gap:
- agent-reach triggered:
- fallback reason:
- fallback queries:
- fallback links:
- final evidence status: evidence_complete / evidence_limited_after_fallback / blocked_mcp_unavailable
- remaining gaps:
```

## 当前首批公司

按 `new_company_intake_queue.md` 顺序处理：

1. 湖南裕能 / 301358.SZ / 创业板 / requires_chinext_permission
2. Marvell Technology / MRVL / Nasdaq / direct_buy_likely
3. 天华新能 / 300390.SZ / 创业板 / requires_chinext_permission + h_share_watch
4. 胜宏科技 / 300476.SZ / 创业板 / requires_chinext_permission
5. 沪电股份 / 002463.SZ / 深交所主板 / direct_buy_likely
6. 生益电子 / 688183.SH / 科创板 / requires_star_permission
7. 深南电路 / 002916.SZ / 深交所主板 / direct_buy_likely
8. 广合科技 / 001389.SZ / 01989.HK / A+H主板 / direct_buy_likely

## 完成判据

新公司完成前，必须满足以下之一：

### A. evidence_complete

- Mindspace 或 agent-reach 合计至少 2 条高质量证据。
- 财报/经营、估值/市场预期、结构性变化、失败条件四类至少覆盖 3 类。
- `company_research.md` 中核心判断能追溯到 `evidence_log.md`。
- `new_company_intake_queue.md` 状态更新为 `research_complete`。

### B. evidence_limited_after_fallback

- 已完成 Mindspace 检索。
- 已完成 agent-reach fallback。
- 仍缺少关键数据。
- 明确说明缺什么、搜过什么、为什么仍不可验证、这如何影响评分。

禁止出现：
- 只因为“权限未开通”就完成。
- 只因为“MCP 无覆盖”就完成。
- 没有 agent-reach 尝试记录就把公司标为数据不足完成。

## Claude Code 启动命令

```text
/loop 30min "读取 /Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索/0_总览/LOOP_PROMPT_COMPANY_DISCOVERY_PRO.md。你是 COMPANY_DISCOVERY_PRO_LOOP：每轮只处理一个公司；优先处理 new_company_intake_queue.md 中 pending_research 公司；不要因为创业板/科创板权限问题跳过研究，只在输出中标注交易权限；必须 MCP-first；MCP health_check 失败则 blocked；MCP 覆盖不足且问题关键时必须加载 agent-reach skill 联网补证据；禁止内置 web_search；没有 agent-reach 尝试记录不得把公司标为数据不足完成；每轮更新公司研究文件、company_score_table.md、new_company_intake_queue.md、run_log.md。" --max-iterations 120 --completion-promise "COMPANY_DISCOVERY_PRO_COMPLETE"
```
