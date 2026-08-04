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
legacy_path: "AI周期探索/02_公司研究/Meituan/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Meituan Evidence Log (CN Refresh 2026-05-17)

## CN Refresh 数据源

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| **Meituan IR** (about.meituan.com) | Q3 2025最新季度+FY2024年度+Q1-Q3 2025全部链接 | 官方文件可追溯 | 极高 | PDFs被Cloudflare阻止无法读取内容 |
| **Google Finance** | Q1 2026营收CN¥31.67B(miss)+净利CN¥12.44B+利润率39.27% | 最新季度财务 | 极高 | 4季度趋势数据完整 |
| **Google Finance** | 股价HK$82.70, YTD -20%, 52周HK$73.6-149.8, 市值~US$27.5B | 估值 | 极高 | |
| **Google Finance** | FY2025净亏损CN¥24.3B, FY2026 EPS预期-CN¥1.73 | 年度财务 | 极高 | 补贴战争+Keeta亏损 |
| **Google Finance 新闻** | 监管干预补贴战+Moonshot AI $2B+Keeta巴西扩张+Fitch负面 | 战略催化 | 高 | 多来源交叉验证 |
| **SeekingAlpha** | "A Messy Quarter, But Underlying Trends Are Positive" | 分析师观点 | 高 | Q1 2026分析 |
| **Jina Reader** | Meituan IR完整页面抓取，确认Q1-Q3 2025+FY2024报告 | IR可追溯性 | 极高 | 英文版链接已确认 |

## PRO 更新数据源 (2026-05-16, 保留参考)

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| 雪球 | TTM EPS -HK$4.43, PB 2.96 | 财务+估值 | 高 | 与Google市值有差异 |
| Google Finance | 收购叮咚买菜US$717M, Keeta沙特扩张, 35+分析师 | 战略+覆盖 | 极高 | |

## PRO source coverage

- Mindspace status: ⚠️ 极弱（发现"美团股价"专属channel但MongoDB连续超时，earnings/X channels无Meituan内容）
- Mindspace gap: 零可用MCP文章（专属channel MongoDB连接失败，通用频道无Meituan命中）
- agent-reach triggered: yes
- fallback reason: MCP覆盖为零（MongoDB超时+无Meituan命中），Exa MCP离线(DNS失败)
- fallback queries: Google Finance Meituan 3690 + CNBC 3690-HK quote
- fallback links:
  - www.google.com/finance/quote/3690:HKG (实时+AI分析+分析师共识+多空观点)
  - www.cnbc.com/quotes/3690-HK (实时报价)
- final evidence status: evidence_complete
- remaining gaps: FY2025年报PDF内容(Cloudflare阻止)、Keeta各市场具体GMV/市占率、Moonshot AI估值变化

## PRO 新增证据 (agent-reach fallback, 2026-05-17)

### 1. Google Finance AI 分析 (2026-05-15)
| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| Google Finance | 36分析师Strong Buy共识, PT HK$110.90-128.88 (+34%+) | 分析师情绪 | 极高 | |
| Google Finance | FY2026E EPS损失从CN¥1.56扩大至CN¥1.73/share | 盈利预期恶化 | 极高 | |
| Google Finance | 股价HK$82.70(-3.50%), 市值HK$214.5B, EPS -HK$4.43 | 实时估值 | 极高 | |
| Google Finance | 外卖竞争从价格战转向理性竞争，监管压制非理性补贴 | **结构性变化** | 高 | 关键正面催化 |
| Google Finance | 管理层预期Q1 2026外卖每单亏损显著环比改善 | 盈利趋势 | 高 | |
| Google Finance | 收购叮咚买菜大陆业务$717M+AI"小赚"助手 | 战略 | 高 | |
| Google Finance | 骑手社保试点+减少配送时间压力→运营成本上升 | **新风险** | 高 | 原评估未覆盖 |
| Google Finance | Fitch负面展望，正FCF延迟至2027 | 信用风险 | 高 | |

### 2. 关键判断更新
- **补贴战争缓解**: Google Finance分析确认"regulatory guidance against irrational subsidies"正在生效，管理层从低价值订单转向质量增长
- **EPS恶化超预期**: FY2026E损失从-CN¥1.56扩大至-CN¥1.73，市场近期下调预期导致股价9%下跌
- **新风险-骑手成本**: 社保试点+配送时间限制是新发现的利润率压制因素
- **AI战略**: "小赚"AI助手用于服务发现，属于运营效率提升而非结构转型

## Evidence Status: evidence_complete (PRO Repair)
- 4/4类别覆盖: 财务(Q1 2026季度+FY2025年度+EPS恶化)+估值(实时+36分析师Strong Buy)+战略(监管干预+AI助手+叮咚收购)+竞争(补贴理性化+骑手成本+Douyin/JD)
- **关键增量**: (1)补贴战从"持续"修正为"正在理性化"，管理层确认Q1 2026亏损改善；(2)EPS恶化超预期(-CN¥1.73)；(3)新发现骑手成本风险
- 仍缺: FY2025年报PDF详情(2026-05-26后web-reader恢复补)
