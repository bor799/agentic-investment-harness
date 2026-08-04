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
legacy_path: "AI周期探索/02_公司研究/Xiaomi/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Xiaomi Evidence Log (Refreshed 2026-05-16)

## 数据源

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| Xiaomi IR / HKEX | FY2025 Annual Results Announcement (2026-03-24), PwC 审计 | 核心财务: Revenue RMB457.3B, Net Income RMB41.6B, GP 22.3% | 极高 | 官方 HKEX 公告，替换 Wikipedia |
| Xiaomi IR | FY2025 Annual Report (2026-04-28) | 年度详细报告 | 极高 | 官方 PDF |
| Xiaomi IR | Q4'25 Results Presentation (2026-03-24) | 业务亮点、战略、分部数据 | 极高 | 官方演示文稿 |
| Xiaomi IR | Q1-Q3'25 Quarterly Announcements | 季度趋势 | 极高 | 官方季度公告 |
| Google Finance | Price ~HK$31.72, 81% Strong Buy, Target HK$50.66 | 估值 | 高 | 实时行情 |
| Google Finance | EV 550K target, IoT 35%+ gross profit forecast, consensus revision | 市场预期 | 高 | 分析师汇总 |
| Wikipedia (background only) | XRING O1 3nm, MiMo AI, Fortune 500 #338 | 技术转型背景 | 高 | 仅作背景，已由官方 IR 确认 |

## CN refresh source coverage

- refresh date: 2026-05-16
- cutoff date: 2026-05-16
- source route: Xiaomi IR (ir.mi.com) + HKEX + Google Finance
- preflight cache used: yes (Mindspace OK, Jina OK, Exa unavailable_not_blocking)
- agent-reach availability: Jina Reader primary, MCP web-reader limit exhausted
- official links:
  - FY2025 Annual Results: https://ir.mi.com/system/files-encrypted/nasdaq_kms/assets/2026/03/24/5-35-03/25Q4%20EN%20AC%20Xiaomi.pdf
  - FY2025 Annual Report: https://ir.mi.com/system/files-encrypted/nasdaq_kms/assets/2026/04/28/5-29-08/Xiaomi%202025%20AR_EN.pdf
  - Q4'25 Presentation: https://ir.mi.com/system/files-encrypted/nasdaq_kms/assets/2026/03/24/6-20-53/Xiaomi%20Corp_25Q4_ER_ENG%20vF.pdf
  - IR Quarterly Results: https://ir.mi.com/financial-information/quarterly-results
  - IR Annual Reports: https://ir.mi.com/financial-information/annual-interim-reports
- fallback links: Google Finance (https://www.google.com/finance/quote/1810:HKG)
- replaced stale evidence: Wikipedia 作为 FY2024 核心财务源 → 替换为 HKEX 官方 FY2025 公告; Google Finance-only 估值 → 保留但补充官方 IR 交叉验证
- evidence buckets covered: 财报/经营(官方完整), 估值/市场预期(Google Finance+共识), 结构性变化(EV盈利+芯片+AI), 失败条件(组件成本+地缘+竞争)
- ljg-invest conclusion: 非秩序创造机器 — 硬件生态飞轮在转动(RMB 457B营收+1B+IoT设备+411K EV)，但本质是规模经济而非稀缺瓶颈；XRING O1 3nm+MiMo AI是技术突破但尚未形成不可替代的控制点；权力来源是硬件规模+供应链效率+渠道覆盖(18,000门店)，失败条件是EV价格战+组件成本+地缘政治+AI投资无法变现
- comprehensive-analysis conclusion: 财报质量优秀(营收+25%/净利+76%/净利率6.4%→9.1%)，估值不贵(PE~18.5x/+25%增速)但共识下修(EPS -28%)暗示市场对持续性存疑；催化剂是Q1'26手机GP恢复+EV 550K目标+SU7新订单；情绪偏弱(股价-36.7% YoY)但81% Strong Buy显示机构看好；3年翻倍路径有但需EV规模+利润率持续+AI变现
- final evidence status: evidence_complete
- remaining gaps: Q1'26 季度数据尚未发布（预计 2026 年 5-6 月发布）

## PRO source coverage

- Mindspace status: ⚠️ 弱（发现4个小米专属channel，含67 sources，但全部为通用RSS feeds：Bloomberg/Reuters/Yahoo Finance/TradingView等，零小米特定文章可检索；earnings channels也无Xiaomi命中）
- Mindspace gap: 4 channel × search_articles均返回 items:[] — channel 有 sources 但无 matching articles
- agent-reach triggered: no（CN refresh 2026-05-16 已通过 Jina Reader + Google Finance 获取完整证据，官方 IR 数据齐全：HKEX FY2025 年报+季度公告+业绩演示文稿）
- final evidence status: evidence_complete（PRO 确认 MCP 覆盖弱但已有充分 agent-reach fallback 数据）
- remaining gaps: Q1'26 季度数据（预计 2026 年 5-6 月发布）

## 关键证据详细记录

| source_name | source_type | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|
| Xiaomi IR Annual Results | exchange_announcement | https://ir.mi.com/system/files-encrypted/nasdaq_kms/assets/2026/03/24/5-35-03/25Q4%20EN%20AC%20Xiaomi.pdf | 2026-03-24 | FY2025完整财务数据 | 极高 | PwC审计，HKEX备案 |
| Xiaomi IR Annual Report | annual_report | https://ir.mi.com/system/files-encrypted/nasdaq_kms/assets/2026/04/28/5-29-08/Xiaomi%202025%20AR_EN.pdf | 2026-04-28 | FY2025年度报告 | 极高 | 完整年报 |
| Xiaomi IR Presentation | regulator_filing | https://ir.mi.com/system/files-encrypted/nasdaq_kms/assets/2026/03/24/6-20-53/Xiaomi%20Corp_25Q4_ER_ENG%20vF.pdf | 2026-03-24 | 业务亮点+战略 | 极高 | 业绩演示文稿 |
| Google Finance | data_aggregator_crosscheck | https://www.google.com/finance/quote/1810:HKG | 2026-05-15 | 实时股价+分析师 | 高 | 聚合源 |
