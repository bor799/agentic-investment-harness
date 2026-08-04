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
legacy_path: "AI周期探索/02_公司研究/CRRC/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# CRRC Evidence Log (CN Refresh 2026-05-17)

## CN Refresh 数据源尝试 (2026-05-17)

| source | result | notes |
|---|---|---|
| Jina Reader (StockAnalysis) | ❌ 429限额用尽 | 2026-05-26 21:31:58 UTC 重置 |
| Jina Reader (东方财富) | ❌ 429限额用尽 | 同上 |
| Web Search | ❌ 429限额用尽 | 同上 |

**结论**: CN Refresh 无新增数据。A/H股标的英文数据源有限(StockAnalysis不覆盖HK/A股)，中文数据源(Jina+WebSearch)配额已耗尽。PRO数据(2026-05-16)已为最新。

## 数据源 (PRO Updated 2026-05-16)

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| Google Finance | 股价HK$5.32, 市值HK$190.55B(~US$24.5B), PE 9.81(H), PB 0.98 | 估值 | 极高 | 2026-05-15 |
| 东方财富(East Money) | Q1 2026: 营收CN¥53.82B(+10.57%), 净利CN¥3.38B(+10.66%), GM 23.81% | 最新季度 | 极高 | |
| 东方财富 | FY2025: 营收~CN¥246B(+5%), 净利CN¥13.18B(+6.4%) | 年度财务 | 极高 | |
| 东方财富 | 净利趋势: FY2021 103→2022 116.5→2023 117.1→2024 123.9→2025 131.8 (CN¥B) | 5年趋势 | 极高 | 稳定5-6%增长 |
| Google Finance | 员工152,000, AH溢价22.3%(H股折让), 负债率60.26% | 公司结构 | 高 | |
| Exa搜索 | 迪拜地铁蓝线(首次GCC突破), 雅万高铁990万乘客, 匈塞铁路 | 海外合同 | 高 | |
| Exa搜索 | 氢能源ALK电解槽交付(全球首个液态阳光项目), CR450动车, 600km/h磁浮 | 新技术 | 高 | |

## Agent-Reach 更新 (2026-05-16)

- **数据质量飞跃**: 从仅2018 Wikipedia数据→完整FY2021-2025+Q1 2026东方财富数据
- 来源: Google Finance (H+A股) + 东方财富 F10 + Exa搜索新闻
- 新发现: 氢能源业务是意外增长点，CR450动车组+600km/h磁浮是技术前沿

## 投资结论

- **ljg-invest conclusion**: 非秩序创造机器 — 传统轨交制造央企，全球最大规模不可复制但国有体制限制效率和创新，氢能源/风电/磁浮新业务是增量非转型，权力来源是政府订单+制造规模，失败条件是海外政治风险(美国制裁+欧盟调查)+国内增长天花板5-6%
- **comprehensive-analysis conclusion**: 财报稳健(FY2025净利+6.4%+GM 23.81%改善+Q1 2026营收+10.57%加速)，PB 0.98<1+PE H股9.81x极度便宜是深度价值信号，迪拜地铁/CR450是出海催化剂，但国有体制限制估值扩张

## Evidence Status: evidence_complete
- 4/4类别覆盖: 财务(5年+Q1 2026)+估值(实时双市场)+新业务(Exa)+海外合同
- Data quality: 极高 (东方财富+Google Finance primary)
- CN Refresh 2026-05-17: 无新数据可获取，下次重试 2026-05-26+

## PRO source coverage

- Mindspace status: ⚠️ 零覆盖（无中车/CRRC专属channel，earnings channels零命中）
- Mindspace gap: 无CRRC相关文章
- agent-reach triggered: no（PRO 2026-05-16已有Google Finance+东方财富+Exa搜索完整数据）
- final evidence status: evidence_complete（PRO确认MCP零覆盖但已有充分agent-reach fallback数据）
- remaining gaps: 无重大缺口
