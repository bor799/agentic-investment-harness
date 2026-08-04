---
title: "cn_consumer_refresh_queue"
date: 2026-07-24
updated: 2026-07-24
layer: STATE
primary_role: legacy_automation_state
status: superseded
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
legacy_metadata_added: true
legacy_path: "AI周期探索/0_总览/cn_consumer_refresh_queue.md"
migration_target: "90_AUTOMATION/RUNTIME + 03_STATE"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# CN Consumer Refresh Queue

用途：`AI_CN_CONSUMER_REFRESH_LOOP` 专用队列，只刷新 11 家中国消费/品牌/制造相关公司。不要改动主队列 `company_queue.md`。

## Preflight cache

| item | status | notes |
|---|---|---|
| Run started at | 2026-05-17 (R2: analytical overlay) CST | AI_CN_CONSUMER_REFRESH_LOOP Round 2 |
| Mindspace MCP | OK | SQL + Mongo both healthy |
| agent-reach doctor | available | Jina Reader + mcp tools as primary paths |
| Jina Reader | OK | HTTP 200 |
| Exa via mcporter | unavailable_not_blocking | mcporter only has douyin(online)+linkedin(offline), no Exa |

## Queue

| status | 公司 | 代码 | source route | current weak evidence to replace |
|---|---|---|---|---|
| completed | Xiaomi | 01810.HK | HKEXnews + Xiaomi IR + official annual/interim results | ✅ 已替换为 HKEX 官方 FY2025 年报 + IR presentation |
| completed | Pop Mart | 09992.HK | HKEXnews + Pop Mart IR + official annual/interim results | ✅ 已替换为 HKEX 官方 FY2025 年报 + 44位分析师覆盖 + 完整财务数据 |
| completed | Meituan | 03690.HK | Meituan IR + Google Finance + SeekingAlpha + Jina Reader | ✅ 已替换为 Q1 2026 季度数据+官方IR链接+监管催化+Moonshot AI+Keeta亏损收窄 |
| completed | PDD | PDD | SEC 10-K (StockAnalysis) + Google Finance + SeekingAlpha + Bloomberg | ✅ 已替换为 SEC 10-K 完整年报 + 季度趋势 + de minimis/Amazon Haul/$14.5B供应链新进展 |
| completed | Beike | BEKE / 02423.HK | StockAnalysis (SEC 10-K) + Google Finance + Reuters + Investing.com | ✅ 已替换为季度趋势(Q4 PM 0.40%)+回购148M+GS/UBS升级+家装/租房+18%+Q1预期-20% |
| completed | Bilibili | BILI / 09626.HK | StockAnalysis (SEC 10-K) + Bilibili IR (SEC+HKEX filings) | ✅ 已替换为 FY2025完整年报(首次盈利+GM 36.62%+FCF 21.86%)+5年趋势+IR可追溯 |
| completed | Miniso | MNSO / 09896.HK | StockAnalysis (SEC FY2024年报+TTM) | ✅ 已替换为 FY2025 TTM数据(EPS -53%+股息+6.16%)+Miniso IR 404已记录，FY2025年报待提交 |
| completed | CRRC | 01766.HK / 601766.SH | SSE+SEHK+东方财富 (PRO已有完整数据) | ✅ PRO数据已含FY2025年报+Q1 2026+氢能源/迪拜地铁，外部源配额耗尽，数据保留 |
| completed | Fuyao Glass | 03606.HK / 600660.SH | Google Finance (TTM Q1 2026) + CNBC + Fuyao IR (fuyaogroup.com) | ✅ 已替换为 TTM 4季度数据+官方IR可追溯+Q1 2026外汇损失分析+Vitro竞争新闻 |
| completed | Aux Electric | 02580.HK | SEHK+GuruFocus (PRO已有完整数据) | ✅ PRO数据已含FY2025年报+42分析师+PE 5.89x+股息11.93%，外部源配额耗尽，数据保留 |
| completed | 分众传媒 | 002027.SZ | SZSE+东方财富 (PRO已有完整数据) | ✅ PRO数据已含FY2025年报+Q1 2026反弹+GM 68.74%+新潮收购，外部源配额耗尽，数据保留 |
