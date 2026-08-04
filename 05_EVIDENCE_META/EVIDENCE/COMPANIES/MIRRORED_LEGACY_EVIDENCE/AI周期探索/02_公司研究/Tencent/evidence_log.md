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
legacy_path: "AI周期探索/02_公司研究/Tencent/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Tencent Evidence Log (PRO Updated 2026-05-16)

## MCP搜索记录

### PRO修复搜索（2026-05-16）
1. health_check → 通过
2. search_articles(X信源 b0e8adcc, "Tencent 腾讯 WeChat AI revenue earnings profit 2025 2026") → WeChat官方推文+unusual_whales财报汇总（间接）
3. search_articles(ai market trends f6760f0f, "Tencent AI WeChat mini program cloud gaming revenue earnings") → 云游戏/Xbox/Oracle等背景，0 Tencent直接
4. search_articles(NVDA频道 5931c9a3, "Tencent 00700 revenue profit market cap analyst valuation") → ✅ CNBC腾讯Q1 2026财报（2026-05-13）

## MCP Direct Evidence

| source_name | source_tab | evidence_use | confidence |
|---|---|---|---|
| CNBC (Earnings) | media | Q1 2026: 营收¥196.5B(+9%), 低于预期¥199B; 游戏¥45.4B(+6%); WorkBuddy中国最受欢迎代理; 云+20%; AI广告模型推广告+20% | 高 |
| Morningstar (via CNBC) | media | Ivan Su分析师: AI投入已产生回报，广告推荐模型驱动增长 | 高 |

## Agent-Reach Fallback 证据

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| Wikipedia | 2024营收¥660.26B, 营业利润¥208.10B, 净利¥196.47B | 年度财务基准 | 高 | |
| Wikipedia | 总资产¥1.781T, 净资产¥1.053T | 资产规模 | 高 | |
| Wikipedia | 员工105,417, WeChat 1B+ MAU | 公司规模 | 高 | |
| Wikipedia | Naspers/Prosus持股25.65%, 600+投资 | 股东结构 | 高 | |
| Google Finance | 股价HK$454.90, 200日均线HK$580.5 | 技术面偏弱 | 高 | 下行趋势 |
| Google Finance | TradingView目标HK$717.92 (55%上行) | 分析师预期 | 中 | |

## PRO source coverage

- Mindspace status: ✅ 良好（CNBC Q1财报详细报道+Morningstar分析师评论）
- Mindspace gap: 无 — MCP已覆盖财报、AI产品、竞争、分析师观点
- agent-reach triggered: yes（补充年度财务+股价）
- fallback queries: Wikipedia Tencent + Google Finance 0700:HKG
- fallback links: en.wikipedia.org/wiki/Tencent, google.com/finance/quote/0700:HKG
- final evidence status: evidence_complete（4/4类别覆盖）
- remaining gaps: 海外游戏具体收入数据、AI CapEx精确金额
