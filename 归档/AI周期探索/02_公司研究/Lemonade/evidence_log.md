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
legacy_path: "AI周期探索/02_公司研究/Lemonade/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Lemonade Evidence Log (PRO Updated 2026-05-16)

## MCP搜索记录

### PRO修复搜索（2026-05-16）
1. health_check → 通过
2. search_articles(X信源 b0e8adcc, "Lemonade LMND insurance AI") → 0 LMND 直接相关（通用AI/保险文章）
3. search_articles(ai market trends f6760f0f, "Lemonade AI insurance LMND") → 0 LMND 直接相关（行业文章含"insurance"和"AI"但不涉及Lemonade公司）

**结论**: MCP 零 LMND（Lemonade 保险）直接覆盖。

## Agent-Reach Fallback 证据

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| StockAnalysis.com | 市值$3.94B(+90%), 价格$51.34 | 估值基准 | 高 | |
| StockAnalysis.com | TTM营收$844.70M(+51.22%) | 核心财务验证 | 高 | 强增速 |
| StockAnalysis.com | FY2025营收$737.90M(+40.15%) | 年度验证 | 高 | |
| StockAnalysis.com | 5年营收$128.4M→$844.7M | 长期增长 | 高 | 46% CAGR |
| StockAnalysis.com | TTM净亏损-$138.90M | 盈利状态 | 高 | 持续收窄 |
| StockAnalysis.com | 损失率97%(FY22)→61.3%(TTM) | AI风控验证 | 高 | 关键改善 |
| StockAnalysis.com | 营业利润率-182%→-15.88%(TTM) | 运营效率 | 高 | 接近盈亏平衡 |
| StockAnalysis.com | TTM FCF +$19.5M（首次转正） | 现金流拐点 | 高 | |
| StockAnalysis.com | 净保费$644.6M(76.3%收入) | 收入构成 | 高 | |
| StockAnalysis.com | 9位分析师Buy, 目标$67.78(+32%) | 市场预期 | 高 | |
| StockAnalysis.com | Beta 1.85 | 波动性 | 高 | 高于市场 |
| StockAnalysis.com | 员工1,282 | 公司规模 | 高 | |

## PRO source coverage

- Mindspace status: ✅ 通过（零 LMND 覆盖）
- Mindspace gap: 完全无 Lemonade 保险相关文章
- agent-reach triggered: yes
- fallback reason: MCP 完全零覆盖
- fallback queries: stockanalysis.com/stocks/lmnd/ + financials
- fallback links: stockanalysis.com/stocks/lmnd/, stockanalysis.com/stocks/lmnd/financials/
- final evidence status: evidence_complete
- remaining gaps: 州覆盖率、车险产品详情、竞争对比数据

---

## v2 跨市场循环 — 2026-07-22 刷新

**本轮增量**：自 2026-04-30 Q1 2026 财报会分析以来新增 5 项事实；Q2 2026 财报未发布（定档 2026-07-29）。

| 时间 | 事实 | 根来源 | 来源类型 | 独立根? | 更新哪张票 |
|---|---|---|---|---|---|
| 2026-06-22 签署 / 2026-06-24 8-K 备案 | Lemonade 与 Hannover Re (Ireland) DAC 签署 Growth Financing Agreement：2027-01-01 至 2028-12-31；最高未偿金额 2027 年 $150M、2028 年 $250M；月初按当月计划 Growth Spend 的 80% 提取，单 cohort 不超过 $20M；还款来自受益 cohort 保费的固定比例；利率 = max(0%, 3Y UST) + 5.8%；含 customary covenants 和双方终止权；完整协议文本将随 Q2 2026 10-Q 备案 | Lemonade IR Filings 页（https://www.lemonade.com/investor/filings）+ Minichart 8-K 摘要（https://www.minichart.com.sg/2026/06/24/lemonade-inc-files-8-k-for-material-definitive-agreement-and-new-financial-obligation-june-2026/） | filing + news（news 仅作 8-K 内容索引，根来源为 8-K 本身） | 是（8-K 为独立根；Minichart 为同根二次解读，不另计） | H_B 间接（前瞻性 cohort 融资假设，非已成立承保利润）、H_L（非稀释路径）、H_C（新增财务义务） |
| 2026-07-14 | Renters 险种扩展至 Maine（$5/月起） | https://www.lemonade.com/investor/news/lemonade-expands-renters-insurance-to-maine | company_ir | 是 | H_B 边际（运营扩张，非承保质量证据） |
| 2026-07-01 生效 | Renters 险种扩展至 Mississippi | BusinessWire 2026-06-29（经 Lemonade IR 索引） | company_ir | 同根（Lemonade 公司公告） | H_B 边际 |
| 2026-06-10 | Renters 险种扩展至 North Dakota | Fintech Global 2026-06-10（经 Lemonade IR 索引） | company_ir | 同根 | H_B 边际 |
| 2026-07（连续） | 股价 ~$67.45，4 月以来 +30%，相对成本 $52.50 +29%；52 周区间 $35.70-$99.90 | Yahoo Finance / 多行情源聚合 | exchange（行情数据） | 是（但行情不能单独更新 H_B） | H_R（fail, down）、H_L（unchanged） |
| 2026-07-29 定档 | Q2 2026 财报发布日（本轮时尚未发布） | https://www.lemonade.com/investor/news/lemonade-to-announce-second-quarter-2026-financial-results | company_ir | 是 | 催化剂待验证 |
| 2026-11-17 定档 | 2026 Investor Day（NYC） | https://www.lemonade.com/investor | company_ir | 是 | 事件待验证 |

**四票变化**（vs 2026-04-30 Q1 分析后状态）：

| 票 | 上次 | 本次 | 变化原因 |
|---|---|---|---|
| H_B | unknown | unknown（unchanged） | Hannover Re 协议是专业第三方正面信号，但属前瞻性融资假设；GLR 可持续性核心缺口未关闭 |
| H_R | fail（$51 已高于 $38-45 核心买入区） | fail, down（$67+ 进一步压缩安全边际） | 价格 +30%，安全边际下降 |
| H_L | pass | pass（unchanged） | NYSE 流动性充足；非稀释融资协议改善路径；具体 covenants 待 Q2 10-Q 全文 |
| H_C | pass | pass（unchanged） | 持仓 1 股 ¥459 / 总资产 0.16%，所有资本约束合法 |

**冲突与未解决项**：
- Q1 2026 GLR 62% 是季节性 CAT（5%）+ 一次性 vs 结构性恶化——Q2 数据未出，无法定论；按来源冲突规则保持 unknown。
- Hannover Re 协议的 cohort 定义和 covenants 未公开——待 Q2 10-Q 全文。
- Cohort-level GLR 与公司整体 GLR 差异未披露——待 Q2 电话会议或 10-Q。
- Probability status 保持 `uncalibrated`：无固定参考类、期限、结算规则和历史校准。

**新增根来源链接（本轮）**：
1. Lemonade IR Filings 页：https://www.lemonade.com/investor/filings（确认 6/24/2026 8-K 存在、Q1 10-Q 已备案 4/30/2026）
2. Lemonade IR Q2 2026 业绩公告：https://www.lemonade.com/investor/news/lemonade-to-announce-second-quarter-2026-financial-results
3. Lemonade IR Maine 扩张公告：https://www.lemonade.com/investor/news/lemonade-expands-renters-insurance-to-maine
4. Minichart 8-K 内容摘要（非独立根，作为 8-K 内容索引）：https://www.minichart.com.sg/2026/06/24/lemonade-inc-files-8-k-for-material-definitive-agreement-and-new-financial-obligation-june-2026/
5. Yahoo Finance LMND 行情：https://finance.yahoo.com/quote/LMND/（仅用于 H_R/H_L，不更新 H_B）

**下复查**：2026-07-29 Q2 2026 财报发布后立即刷新；关键监控数字已迁入 next_signals.md。

---

## v2 跨市场循环 — 2026-07-22 同日重试（attempt 2，run_token 25c5d60f）

**本轮增量**：同日重试；attempt 1 完成后无新增独立根证据。**判断未变**。

| 复核项 | 结果 |
|---|---|
| Q2 2026 财报是否已发布 | 否，仍定档 2026-07-29 8:00 AM ET |
| 是否有新 8-K 或 10-Q | 否；EDGAR 与 Lemonade IR 最新相关 8-K 仍是 2026-06-24 Hannover Re 协议 |
| 股价是否发生足以改变 H_R 的变化 | 否；~$67.5 与 attempt 1 抓取的 ~$67.45 一致（噪音范围） |
| 主账是否变化 | 否；数据日 2026-07-15，1 股 @ $52.50 不变 |
| attempt 1 四票是否需要修正 | 否；H_B=unknown/unchanged、H_R=fail/down、H_L=pass/unchanged、H_C=pass/unchanged |

**本轮检查过的根来源**（不重复 attempt 1 已计入的来源，只列本轮为确认"无新事实"而重新核查的入口）：

1. Lemonade IR Filings 页（确认无新 8-K）：https://www.lemonade.com/investor/filings
2. Lemonade IR 主页（确认 Q2 2026 仍定档 7/29）：https://www.lemonade.com/investor
3. SEC EDGAR Lemonade（CIK 0001691421）：未列出 attempt 1 之后的新 8-K 或 10-Q
4. Yahoo Finance Q2 2026 公告（确认日期未变）：https://finance.yahoo.com/markets/stocks/articles/lemonade-announce-second-quarter-2026-003400201.html

**四票状态**：与 attempt 1 完全一致（H_B unknown / H_R fail, down / H_L pass / H_C pass）。

**新增事实**：无。**判断变化**：无。**动作**：`不加仓`。

**下复查**：2026-07-29 Q2 2026 财报后；在此之前不再做同日复核。

---

## v2 跨市场循环 — 2026-07-22 attempt 3（run_token 220b54a6）

**本轮增量**：同日第 3 次执行（初次 + 两次重试的上限）；attempt 2 完成后仍无新增独立根证据。**判断未变**。

| 复核项 | 结果 |
|---|---|
| Q2 2026 财报是否已发布 | 否，仍定档 2026-07-29 8:00 AM ET |
| 是否有新 8-K / 10-Q（attempt 2 之后） | 否；SEC EDGAR (CIK 0001691421) 与 Lemonade IR Filings 页最新相关 8-K 仍是 2026-06-24 Hannover Re 协议 |
| 股价是否发生足以改变 H_R 的变化 | 否；attempt 2 抓取 ~$67.54，本轮 ~$67.45（+0.27, +0.40%），噪音范围 |
| 主账是否变化 | 否；数据日 2026-07-15，1 股 @ $52.50 不变 |
| attempt 2 四票是否需要修正 | 否；H_B=unknown/unchanged、H_R=fail/down、H_L=pass/unchanged、H_C=pass/unchanged |

**边际信息（不改变判断）**：

| 时间 | 事实 | 根来源 | 是否新独立根? | 更新哪张票 |
|---|---|---|---|---|
| 2026-07-07 生效 | Renters 险种扩展至 Vermont（$5/月起） | [ADVFN 引用 Lemonade 公司公告](https://ca.advfn.com/stock-market/NYSE/LMND/stock-news/98878740) | 同根（Lemonade 公司公告，与 attempt 1 已记录的 Maine/Mississippi/North Dakota/Nebraska 同一扩张节奏） | H_B 边际，不变 |
| 2026-07-01 生效 | 再保 cede rate 从 ~20% 降至 ~18% | StockStory / StocksToTrade 引用公司披露（attempt 1 已记录 Q1 电话会议的 cede rate 从 55% 峰值降至约 30%；此为同一再保策略的延续披露） | 同根 | H_B 边际，不变 |
| 2026-07-06 前后 | 股价曾因再保协议与产品发布上行至约 $77.73，后回落至 ~$67.5 | 多行情源聚合 | 行情数据（不能单独更新 H_B） | H_R（仍 fail, down vs 4 月基线） |

**四票状态**：与 attempt 1 / attempt 2 完全一致（H_B unknown / H_R fail, down / H_L pass / H_C pass）。

**本轮检查过的根来源**：

1. SEC EDGAR Lemonade（CIK 0001691421）：未列出 attempt 2 之后的新 8-K 或 10-Q。https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001691421&type=8-K&dateb=&owner=include&count=40
2. Lemonade IR Filings 页：https://www.lemonade.com/investor/filings
3. Lemonade IR 主页（Q2 2026 仍定档 7/29）：https://www.lemonade.com/investor
4. Stock Titan / Barchart Q2 2026 公告索引（仅作交叉核对，非独立根）
5. ADVFN Vermont 扩展新闻（仅确认同一扩张节奏延续）

**新增事实**：无。**判断变化**：无。**动作**：`不加仓`。

**下复查**：2026-07-29 Q2 2026 财报后立即刷新；本对象在 attempt 3 完成后进入 `completed`，等待硬触发刷新或下一轮 v2 循环认领。
