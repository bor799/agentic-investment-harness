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
legacy_path: "AI周期探索/02_公司研究/PDD/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# PDD Evidence Log (CN Refresh 2026-05-17)

## CN Refresh 数据源

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| **Google Finance** | Q1-Q4 2025季度: 营收95.67-123.91B, 净利14.74-30.75B, 利润率15.41-29.57% | 季度趋势 | 极高 | 4季度完整数据 |
| **Google Finance** | Q1 2026 EPS预期$2.13-2.23(+43%YoY), 营收CN¥15.94-16.02B | 前瞻预期 | 高 | 5/19发布 |
| **Google Finance 新闻** | De minimis终结+$14.5B供应链投资+Amazon Haul+EU监管 | 战略+竞争 | 极高 | 6条新闻交叉验证 |
| **SeekingAlpha** | "A Cash-Rich Compounder Trading Like A Broken Business" | 分析师观点 | 高 | |
| **Bloomberg** | "Temu-Owner PDD Quickens Growth After US Business Steadies" | 分析师观点 | 高 | |
| **WSJ** | "Temu Owner PDD Posts Surprise Profit Drop" | 新闻 | 极高 | Q4 miss |
| **BNN Bloomberg** | "Temu-owner PDD misses quarterly revenue estimates" | 新闻 | 极高 | |

## PRO 更新数据源 (2026-05-16, 保留)

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| StockAnalysis.com | FY2025完整10-K年报 | 财务核心 | 极高 | SEC filing |
| StockAnalysis.com | GM 56.28%(↓), OM 21.56%(↓), PM 22.63%, FCF 24.50% | 利润率 | 极高 | |
| Wikipedia | 公司背景+创始人 | 背景 | 高 | |

## PRO source coverage

- Mindspace status: ⚠️ 极弱（3个channel搜索，仅1条CNBC相关文章+3条Zacks股票追踪但全部反bot拦截不可读）
- Mindspace gap: 无PDD直接财报/分析师/战略分析，仅间接行业背景
- agent-reach triggered: yes
- fallback reason: MCP覆盖极弱，Exa MCP离线(DNS失败)，回退Jina Reader
- fallback queries: StockAnalysis PDD overview + forecast + CNBC quotes
- fallback links:
  - stockanalysis.com/stocks/pdd/ (实时财务+分析师+新闻)
  - stockanalysis.com/stocks/pdd/forecast/ (详细分析师预测+估值)
  - www.cnbc.com/quotes/PDD (实时报价)
- MCP回源证据:
  - CNBC Supreme Court tariff ruling (2026-02-20): source_id=2a2b77c4, item_id=513c776446255aa34759488b63f17276, media质量
- final evidence status: evidence_complete
- remaining gaps: Q1 2026财报(5/19发布)后需更新、Temu精确收入拆分、中国vs海外收入占比

## PRO 新增证据 (agent-reach fallback, 2026-05-17)

### 1. 实时估值与财务 (StockAnalysis, 2026-05-15)
| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| StockAnalysis | 价格$95.83, 市值$136.4B, PE 10.16, Forward PE 7.95 | 估值 | 极高 | 实时数据 |
| StockAnalysis | TTM营收$61.74B(+9.7%), 净利$13.99B(-13.0%), EPS $9.44(-13.2%) | 财务趋势 | 极高 | |
| StockAnalysis | FY2025营收CNY 431.85B(+9.65%), 盈利CNY 97.84B(-12.98%) | 年度财务 | 极高 | 与10-K一致 |

### 2. 分析师预测 (StockAnalysis Forecast)
| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| StockAnalysis | 8分析师, Consensus Buy, PT $136(+41.92%), 范围$105-$170 | 估值预期 | 高 | |
| StockAnalysis | FY2026E 营收CNY 496.9B(+15.1%), EPS CNY 82.80(+25.5%) | 前瞻预测 | 高 | 35位分析师 |
| StockAnalysis | FY2027E 营收CNY 558.4B(+12.4%), EPS CNY 96.89(+17.0%) | 前瞻预测 | 高 | 34位分析师 |
| StockAnalysis | Forward PE FY2026 7.88, FY2027 6.74 | 估值 | 高 | |
| StockAnalysis | Strong Buy 3, Buy 1, Hold 4 (May 2026) | 分析师情绪 | 高 | 较12月12人减少至8人 |
| TheFly | Arete升级至Buy, PT $121 (2026-04) | 分析师变化 | 高 | 改善盈利前景 |
| TheFly | Morgan Stanley开设Research Tactical Idea | 分析师变化 | 中 | 短期看好 |

### 3. 关键结构性事件 (MCP回源)
| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| CNBC (MCP回源) | SCOTUS 6-3裁定IEEPA关税违宪(2026-02-20), PDD+2% | **重大政策转向** | 极高 | de minimis法律基础动摇 |
| CNBC (MCP回源) | Temu曾暂停中国直邮→已建立美国本地seller+物流 | 战略应对 | 高 | 供应链已转型 |
| StockAnalysis News | SHEIN vs Temu版权案伦敦高法院 | 竞争风险 | 高 | 法律不确定 |
| StockAnalysis News | Trump-Xi峰会有限突破 | 地缘政治 | 中 | 短期正面 |

### 4. 关键判断更新: SCOTUS关税裁决影响
- **原判断**: "de minimis终结"是PDD四重压制之一
- **SCOTUS裁决(2026-02-20)**: 最高法院6-3裁定IEEPA不授权关税→de minimis移除的法律基础动摇
- **新判断**: de minimis风险部分缓解但未完全消除；IEEPA被否决不等于de minimis豁免自动恢复，需后续行政/法律程序
- **对PDD影响**: Temu已提前转型local-to-local模型，IEEPA被否决反使Temu已投入的$14.5B供应链投资获得额外回报(成本优势恢复)
- **估值影响**: Forward PE 7.95(FY2026)已定价最差情景，SCOTUS裁决+Arete升级构成上行催化

- **ljg-invest conclusion**: 非秩序创造机器 — 低价电商飞轮(低价→规模→更低价)被de minimis终结打断，788M用户+Temu全球网络是规模但非稀缺，$14.5B供应链本地化是防御非进攻性壁垒，失败条件是Amazon Haul直竞争+关税成本+增长崩至10%
- **comprehensive-analysis conclusion**: 财报恶化(净利-12.98%/GM连续3年下滑75.9%→60.9%→56.3%)但PE~10极便宜，Q1 2026财报5/19是关键催化剂，分析师+45%上行vs基本面下行，估值已反映最坏但增长10%不足支撑翻倍

## Evidence Status: evidence_complete (PRO Repair)
- 4/4类别覆盖: 财务(SEC年报+TTM+季度趋势)+估值(实时+8分析师+FY2026/27预测)+战略(SCOTUS裁决+供应链转型)+竞争(Amazon Haul+SHEIN诉讼+EU监管)
- 关键增量: SCOTUS IEEPA裁决(2026-02-20)部分缓解de minimis风险，这是CN Refresh未捕捉的重大变化
- Q1 2026财报(5/19)发布后将需要再次更新
- PDD IR网站不可用，依赖SEC filings+聚合源+MCP回源
