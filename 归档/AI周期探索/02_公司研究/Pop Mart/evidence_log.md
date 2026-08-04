---
title: "evidence_log"
date: 2026-07-24
updated: 2026-07-24
layer: EVIDENCE
primary_role: legacy_company_evidence
status: archived
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
legacy_metadata_added: true
legacy_path: "AI周期探索/02_公司研究/Pop Mart/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Pop Mart Evidence Log (CN Refresh Updated 2026-05-16)

## CN refresh source coverage

- **refresh date**: 2026-05-16
- **cutoff date**: 2026-05-16
- **source route**: HKEXnews + Pop Mart IR + Analyst Coverage (Simply Wall St, MarketScreener, GuruFocus, etnet)
- **preflight cache used**: Yes (2026-05-16 22:45 CST)
- **agent-reach availability**: Available (Exa搜索 + Jina Reader)
- **official links**: 
  - https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0325/2026032500285.pdf (48页完整年报)
- **fallback links**: 
  - https://hk.marketscreener.com/news/pop-mart-international-group-limited-reports-earnings-results-for-the-full-year-ended-december-31-2-ce7e5ed3db8cf026
  - https://www.simplywall.st/stocks/hk/retail/hkg-9992/pop-mart-international-group-shares/valuation
  - https://webuat01.etnet.com.hk/www/eng/stocks/realtime/quote_ci_pl.php?code=9992
- **replaced stale evidence**: 
  - ❌ Wikipedia财务数据 (已用HKEX官方年报替换)
  - ❌ Google Finance单点数据 (已用完整财报+分析师覆盖替换)
- **evidence buckets covered**: 4/4 (财报/经营、估值/市场预期、结构性变化、失败条件)
- **ljg-invest conclusion**: 秩序创造机器 — 但飞轮仍在早期验证阶段,依赖Labubu单一IP
- **comprehensive-analysis conclusion**: 财报极强但增速放缓隐忧,估值不便宜但合理,建议观察
- **final evidence status**: **evidence_complete** (4/4类别覆盖,官方源完整,分析师覆盖充分)
- **remaining gaps**: 无重大缺口

## 官方财报证据 (HKEXnews 2026-03-25)

| source_name | source_type | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|
| Pop Mart 2025 Annual Results Announcement | annual_report | https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0325/2026032500285.pdf | 2026-03-25 | 核心财务数据+地区拆分+IP矩阵+门店网络 | 极高 | 48页完整年报,审计后IFRS数据 |
| Revenue 2025 | annual_report | 同上 | 2026-03-25 | 营收RMB 37,120.1M (+184.7% YoY) | 极高 | 官方审计数据 |
| Gross Profit 2025 | annual_report | 同上 | 2026-03-25 | 毛利润RMB 26,764.9M (+207.4% YoY),毛利率72.1% | 极高 | vs 2024年66.8%,+5.3pp |
| Net Profit 2025 | annual_report | 同上 | 2026-03-25 | 净利润RMB 13,012.0M (+293.3% YoY),净利率35.2% | 极高 | vs 2024年25.4%,+9.8pp |
| EPS 2025 | annual_report | 同上 | 2026-03-25 | Basic EPS RMB 9.61 (+307.2% YoY) | 极高 | vs 2024年RMB 2.36 |
| Overseas Revenue 2025 | annual_report | 同上 | 2026-03-25 | 海外收入RMB 16,268.3M (+291.9% YoY),占43.8% | 极高 | 美洲+748.4%,欧洲+506.3% |
| IP Matrix 2025 | annual_report | 同上 | 2026-03-25 | THE MONSTERS RMB 14,161.1M (+560.6%),占38.1% | 极高 | 17个RMB 100M+级IP |
| Stores 2025 | annual_report | 同上 | 2026-03-25 | 全球630家门店(+109),2,637台机器人商店(+165) | 极高 | 中国445家,亚太85家,美洲64家,欧洲36家 |
| Members 2025 | annual_report | 同上 | 2026-03-25 | 中国72.58M会员,93.7%销售,55.7%复购率 | 极高 | +26.5M新增会员 |
| Cash Flow 2025 | annual_report | 同上 | 2026-03-25 | 现金RMB 13.78B,定期存款RMB 3.45B,无银行借款 | 极高 | 财务健康 |
| Inventory 2025 | annual_report | 同上 | 2026-03-25 | 库存RMB 5.47B (vs 2024年1.52B,+259%) | 极高 | 风险点 |
| Dividend 2025 | annual_report | 同上 | 2026-03-25 | 建议期末股息RMB 2.3817/股,总计RMB 3.19B | 极高 | 股息支付率24.8% |

## 估值与分析师证据

| source_name | source_type | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|
| Simply Wall St | data_aggregator_crosscheck | https://www.simplywall.st/stocks/hk/retail/hkg-9992/pop-mart-international-group-shares/valuation | 2026-04-16 | 市值HK$217B,P/E 14.8x,Forward P/E 10.9x,24位分析师目标价HK$254.24 (+54% upside) | 高 | 44位分析师覆盖,29位提交预测 |
| MarketScreener | data_aggregator_crosscheck | https://au.marketscreener.com/quote/stock/POP-MART-INTERNATIONAL-GR-193012684/valuation/ | 2026-05-14 | P/E历史:2020 183x→2025 17.6x→2026E 10.9x,估值压缩中 | 高 | 完整5年估值数据 |
| etnet | data_aggregator_crosscheck | https://webuat01.etnet.com.hk/www/eng/stocks/realtime/quote_ci_pl.php?code=9992 | 2026-04-20 | 完整5年财务数据:2021-2025营收/利润/利润率趋势 | 高 | 港股权威数据源 |
| GuruFocus | data_aggregator_crosscheck | https://www.gurufocus.com/stock/HKSE:09992/summary | 2026-04-29 | 市值HK$255.94B,P/E 76.62x,P/B 22.43x,警告信号1个 | 中 | 估值数据偏高,可能滞后 |
| Nomura | credible_media_crosscheck | https://www.marketscreener.com/news/nomura-adjusts-pop-mart-international-group-s-price-target-to-hk-252-from-hk-261-keeps-at-buy-ce7f5bddd98af72d | 2026-05-14 | 目标价HK$252 (从HK$261下调),维持Buy评级 | 高 | 分析师覆盖 |

## IP矩阵与业务证据

| source_name | source_type | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|
| Futubull分析 | credible_media_crosscheck | https://news.futunn.com/en/post/71309513/pop-mart-09992-hk-building-core-competitiveness-through-a-multi | 2026-04-08 | IP矩阵详细拆分:THE MONSTERS 14.16B,SKULLPANDA 3.54B,CRYBABY 2.93B,MOLLY 2.90B | 高 | 中金/UBS分析师覆盖 |
| BigGo Finance | credible_media_crosscheck | https://finance.biggo.com/news/rGgxJZ0BDPbb-ItTdYvn | 2026-03-25 | CEO王宁称2026年为"pit stop year",目标增速≥20% | 高 | 关键预警信号 |
| BigGo Finance | credible_media_crosscheck | https://finance.biggo.com/news/sQnII50Bq7sy_YQMYZU7 | 2026-03-25 | Labubu占38.1%收入,市场质疑单一IP依赖,股价暴跌22% | 高 | 风险确认 |
| Longbridge | credible_media_crosscheck | https://longbridge.com/en/news/280420484.md | 2026-03-25 | "营收破30亿净利增284%,为何股价跌15%?" | 高 | 市场情绪分析 |

## 证据质量总结

**官方源覆盖**：
- ✅ HKEXnews 48页完整年报 (极高置信度)
- ✅ Pop Mart IR presentation (高置信度)
- ✅ 年度业绩公告 (高置信度)

**分析师覆盖**：
- ✅ 44位分析师 (Simply Wall St)
- ✅ 24位给出目标价,平均HK$254.24 (+54% upside)
- ✅ 中金/UBS/Nomura等国际投行覆盖

**数据聚合源**：
- ✅ etnet (港股权威数据源)
- ✅ Simply Wall St (国际数据聚合)
- ✅ MarketScreener (全球估值数据)
- ⚠️ GuruFocus (部分数据滞后)

**替换的旧证据**：
- ❌ Wikipedia (已完全替换为HKEX官方数据)
- ❌ Google Finance单点数据 (已替换为完整财报+分析师覆盖)

**证据完整性**：
- 4/4证据类别完整覆盖 (财报/经营、估值/市场预期、结构性变化、失败条件)
- 官方源+分析师+聚合源三重验证
- 无重大缺口

## PRO source coverage

- Mindspace status: ⚠️ 零覆盖（10个channel搜索匹配均为通用AI/X sources，零Pop Mart相关文章；earnings channels无命中）
- Mindspace gap: 无Pop Mart专属channel，搜索返回均为无关forum/blog内容
- agent-reach triggered: no（CN refresh 2026-05-16已有HKEX年报+44分析师+MarketScreener/Simply Wall St完整数据）
- final evidence status: evidence_complete（PRO确认MCP零覆盖但已有充分agent-reach fallback数据）
- remaining gaps: Q1'26 季度数据（预计 2026 年 5-6 月发布）

---

## v2 attempt 3 增量（2026-07-22 / run_token 05d41d56-4e2e-4046-857e-6049f29b1e7c / final attempt）

**本轮新增事实**：无（Web 工具阻断，无新根来源数据采集成功）。

**本轮实际检查过的根来源**（全部 MCP -429 失败）：

| URL | 工具 | 结果 |
|---|---|---|
| https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0325/2026032500285.pdf | mcp__web_reader__webReader | MCP -429（reset 2026-07-26T21:31:58Z）|
| https://www.popmart.com/main/investor | mcp__web_reader__webReader | MCP -429（同上）|
| https://ir.popmart.com | mcp__web_reader__webReader | MCP -429（同上）|
| WebSearch: "Pop Mart 09992.HK H1 2026 interim results revenue gross margin Labubu" | WebSearch | MCP -429（同上）|
| WebSearch: "Pop Mart 09992 HKEX announcement 2026 H1 interim" | WebSearch | MCP -429（同上）|

Web 工具 fallback 文本自述的参数化记忆（"P/E 14.8x"、"Forward P/E 10.9x"、"目标价 HK$254.24"、"Labubu 占 38.1%"、"库存 RMB 5.47B"、"CEO 王宁 pit stop year"）按 AGENTS.md「不得让 AI 成为交易授权者」与 v2 §4「新闻只负责发现叙事或定位根文件，不能单独改变 H_B」**不计入本轮证据**；这些数字的根证据归属是已记录在上方 CN refresh 2026-05-16 表中的 HKEXnews 2025 年报（data day 2026-03-25）。

**本轮更新哪张票**：四票均无变化。H_B 维持 pass（2025 审计证据强）；H_R / H_L / H_C 维持 unknown（无 2026-07-22 当日价格、流动性、资本数据）。判断未变。

**final_evidence_status 升级**：从 PRO 时代的 `evidence_complete`（基于 4/4 PRO 类别覆盖）调整为 v2 框架下的 `evidence_limited`——prior HKEX 2025 年报是 v2 §4 合规根来源基线（HKEX + IR 双独立根来源），但 claim 的两个 evidence_gaps（IP 热度/复购/海外单位经济/库存周转；高增长估值语法/拥挤度/失败条件）需要 H1 2026 中报数据才能完全闭合，本轮 Web 阻断使这些 gap 保持开放。

**与 BTGO / CRCL / NBIS / MSTR / META / GOOGLE / LMND / star50-etf / optical-etf / battery-etf 的关键区别**：那 10 个对象 prior 证据基础**不是** v2 §4 合规根来源（仅 StockAnalysis.com / Seeking Alpha / 吴说区块链 / 本地缓存快照），所以 web 阻断 = 无法建立 v2 §4 基线 = retryable_failure。pop-mart 的 prior 证据基础**确实**是 v2 §4 合规根来源（HKEXnews 官方年报 + Pop Mart IR），web 阻断 ≠ 证据基线缺失；按 v2 §3「没有新事实时，仍生成当日刷新文件」，本次为 evidence_limited 完成文件。

**研究文件**：
- 刷新文件：`260722泡泡玛特_证据状态刷新.md`
- evidence_log.md：本节增量
- next_signals.md：首次创建（v2 canonical，替代旧 next_questions.md）

**下一硬根证据事件**：H1 2026 中报（预计 2026-08 下旬）、Labubu 电影上映（待定）、POP LAND 扩建完成（2026 年夏季）、Web 配额 reset 后第一次补抓窗口（2026-07-27 起）。
