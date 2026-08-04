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
legacy_path: "AI周期探索/02_公司研究/Aux Electric/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Aux Electric Evidence Log (CN Refresh 2026-05-17)

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
| GuruFocus | FY2022-2025完整4年: Revenue HK$21.8B→33.2B, NI HK$1.6B→2.5B, GM 21.25%→18.84% | 核心财务 | 极高 | |
| GuruFocus | PE 5.89(TTM)/4.76(Fwd), PB 1.45, EV/EBITDA 2.07, Dividend 11.93% | 估值 | 极高 | |
| GuruFocus | FY2026E Revenue HK$40.5B(+22%), EPS HK$2.11; FY2027E EPS HK$2.38 | 前瞻预测 | 高 | |
| Google Finance | Price HK$10.07(+1.51%), Market Cap HK$15.99B(~US$2.04B), IPO HK$13.38 | 估值+IPO | 极高 | 2026-05-15 |
| GuruFocus | GF Score 19/100, 42分析师Outperform, 负债率0.16, 员工22,408 | 综合评估 | 高 | |

## Agent-Reach 更新 (2026-05-16)

- **数据质量飞跃**: 从仅Wikipedia母公司2022数据→完整FY2022-2025+GuruFocus+Google Finance
- 关键发现: PE 5.89x+股息11.93%+EV/EBITDA 2.07是深度价值区间
- 警告: FY2025 GM下滑2pp(20.97%→18.84%)+净利-20.6%，基本面恶化中
- IPO后股价-25%(HK$13.38→10.07)

## 投资结论

- **ljg-invest conclusion**: 非秩序创造机器 — 传统家电制造，无结构性变化，空调中国前四但格力/美的/海尔主导，GM下滑2pp至18.84%证明定价权弱，权力来源是成本控制+渠道覆盖，失败条件是价格战持续+利润恶化+需求放缓
- **comprehensive-analysis conclusion**: 财报恶化(FY2025净利-20.6%+GM↓2pp)但PE 5.89x极度便宜+股息率11.93%+EV/EBITDA 2.07是纯深度价值+高股息特征，42分析师覆盖+FY2026E指引+22%，需利润触底反弹确认

## Evidence Status: evidence_complete
- 4/4类别覆盖: 财务(FY2022-2025)+估值(实时)+前瞻(GuruFocus)+IPO数据
- CN Refresh 2026-05-17: 无新数据可获取，下次重试 2026-05-26+

## PRO source coverage

- Mindspace status: ⚠️ 零覆盖（无奥克斯/Aux专属channel，earnings channels零命中）
- Mindspace gap: 无Aux Electric相关文章
- agent-reach triggered: no（PRO 2026-05-16已有GuruFocus+Google Finance完整数据）
- final evidence status: evidence_complete（PRO确认MCP零覆盖但已有充分agent-reach fallback数据）
- remaining gaps: 无重大缺口
