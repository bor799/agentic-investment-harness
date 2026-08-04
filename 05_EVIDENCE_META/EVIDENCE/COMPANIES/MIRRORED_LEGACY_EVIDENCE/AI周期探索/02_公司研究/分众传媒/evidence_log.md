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
legacy_path: "AI周期探索/02_公司研究/分众传媒/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 分众传媒 Evidence Log (CN Refresh 2026-05-17)

## CN Refresh 数据源尝试 (2026-05-17)

| source | result | notes |
|---|---|---|
| Jina Reader (东方财富) | ❌ 429限额用尽 | 2026-05-26 21:31:58 UTC 重置 |
| Web Search | ❌ 429限额用尽 | 同上 |

**结论**: CN Refresh 无新增数据。A股标的中文数据源(Jina+WebSearch)配额已耗尽。PRO数据(2026-05-16)已为最新。

## 数据源 (PRO Updated 2026-05-16)

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| 东方财富 F10 | FY2025年报: 归母净利润CN¥29.46亿(-42.85%), 主因剥离数禾科技减值 | 年度财务 | 极高 | 2026-04-29发布 |
| 东方财富 F10 | Q1 2026: 营收CN¥29.15亿(+2.01%), 归母净利润CN¥17.90亿(+57.65%), GM 68.74% | 最新季度 | 极高 | |
| 东方财富 F10 | 分析师预测: 2026E EPS 0.42, 2027E 0.44, 2028E 0.47 | 前瞻估值 | 极高 | |
| 雪球 | 股价CN¥5.92, 市值CN¥854.98亿, TTM PE 23.74x, 股息率5.74% | 实时估值 | 极高 | 2026-05-15 |
| CLS(财联社) | 收购新潮传媒90.02%(CN¥77.94亿)审核中, 海外FMOIL III融资$63M | 战略动态 | 极高 | |
| 东方财富 | 累计回购CN¥153亿(注销CN¥148亿), 2026中期分红上限100%净利 | 股东回报 | 极高 | |

## 关键发现

1. **FY2025净利-42.85%非经营性**: 剥离数禾科技导致资产减值，核心广告业务仍健康
2. **Q1 2026强劲反弹**: 净利+57.65%+GM+4.03pp验证核心广告业务盈利能力
3. **新潮传媒收购**: 合并中国两大电梯广告网络，实质性增强护城河
4. **海外9国布局**: FMOIL III平台获$63M新融资，验证海外扩张加速
5. **Wikipedia数据异常已解决**: 2021年数据(营业利润>营收)被2025年报+Q1 2026东方财富数据替代

## 投资结论

- **ljg-invest conclusion**: 非秩序创造机器 — 电梯广告垄断有物理稀缺性(优质屏幕位置)但非技术瓶颈，GM 68.74%验证强定价权，AI精准投放"千楼千面"是效率提升非飞轮重构，收购新潮传媒巩固垄断地位，权力来源是物理屏幕网络+优质楼宇合同，失败条件是消费下行+广告主预算缩减+新媒体替代
- **comprehensive-analysis conclusion**: 财报改善(Q1 2026净利+57.65%+GM 68.74%极强+Forward PE 14x+股息5.74%深度价值)，新潮传媒收购90.02%巩固地位+海外9国扩张，但FY2025净利-42.85%(含减值)和消费周期依赖是主要风险

## Evidence Status: evidence_complete
- 4/4类别覆盖: 财务(FY2025+Q1 2026)+估值(实时)+战略(收购+海外)+分红(5.74%)
- Data quality: 极高 (东方财富 F10 primary source)
- CN Refresh 2026-05-17: 无新数据可获取，下次重试 2026-05-26+

## PRO source coverage

- Mindspace status: ⚠️ 零覆盖（无分众传媒专属channel，earnings channels零命中）
- Mindspace gap: 无分众传媒相关文章
- agent-reach triggered: no（PRO 2026-05-16已有东方财富F10+雪球+CLS完整数据）
- final evidence status: evidence_complete（PRO确认MCP零覆盖但已有充分agent-reach fallback数据）
- remaining gaps: 无重大缺口
