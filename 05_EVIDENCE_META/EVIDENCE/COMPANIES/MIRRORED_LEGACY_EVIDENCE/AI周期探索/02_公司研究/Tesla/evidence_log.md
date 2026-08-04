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
legacy_path: "AI周期探索/02_公司研究/Tesla/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Tesla Evidence Log (PRO Updated 2026-05-16)

## MCP搜索记录

### PRO修复搜索（2026-05-16）
1. health_check → 通过
2. search_articles(X信源 b0e8adcc, "Tesla TSLA earnings revenue FSD autonomy") → 10条，含Musk推文、unusual_whales财报汇总、indigo X Q1财报总结
3. search_articles(ai market trends f6760f0f, "Tesla FSD robot autonomy Optimus robotaxi") → 10条直接文章（The Verge×5、TechCrunch×2、Forbes×2、indigo×1）

**结论**: MCP 对 Tesla 覆盖极丰富，10+ 条高质量直接文章，涵盖 Q1 财报、FSD、Robotaxi、Optimus、竞争对比。

## MCP Direct Evidence

| source_name | source_tab | evidence_use | confidence |
|---|---|---|---|
| The Verge | media | Q1 2026: 营收$22.4B(+16%), 净利$477M(+17%), Optimus产线筹备 | 高 |
| The Verge | media | HW3(400万辆)无法支持无人监督FSD，内存带宽仅HW4的1/8 | 高 |
| TechCrunch | media | Robotaxi扩展Dallas/Houston，各仅1辆登记，Austin 14起碰撞 | 高 |
| The Verge | media | FSD累计100亿英里达"安全无人监督"门槛，但未切换客户模式 | 高 |
| The Verge | media | Cybercab在Austin量产，Musk罕见谨慎强调验证 | 高 |
| Forbes | media | XPENG VLA 2.0已在中国领先Tesla自动驾驶 | 高 |
| Forbes | media | Rivian LiDAR+多传感器 vs Tesla纯视觉路线对比 | 高 |
| Indigo X | official_press | Q1财报总结: 汽车毛利率19.2%(+1.3pp), CapEx高, Optimus量产难 | 高 |
| TechCrunch (today) | media | Tesla披露2起Robotaxi远程操作员碰撞事故 | 高 |

## Agent-Reach Fallback 证据

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| StockAnalysis.com | 市值$1.59T(+74.5%), 价格$422.24 | 估值基准 | 高 | 万亿级 |
| StockAnalysis.com | TTM营收$97.88B(+2.3%) | 核心财务 | 高 | 几乎零增长 |
| StockAnalysis.com | FY2025营收$94.83B(-2.93%) | 营收下降 | 高 | 负增长！ |
| StockAnalysis.com | TTM净利$3.86B(-36.8%) | 利润下降 | 高 | 腰斩 |
| StockAnalysis.com | FY2025净利$3.79B(-46.79%) | 利润大幅下降 | 高 | |
| StockAnalysis.com | P/E 431.10, Forward P/E 206.09 | 极端估值 | 高 | |
| StockAnalysis.com | 32位分析师Buy, 目标$405.47(-3.97%) | 高估信号 | 高 | 目标低于现价 |

## PRO source coverage

- Mindspace status: ✅ 通过（10+条直接文章，覆盖极丰富）
- Mindspace gap: 无 — MCP 已覆盖财报、产品、竞争、安全、战略
- agent-reach triggered: yes（补充精确财务数据）
- fallback queries: stockanalysis.com/stocks/tsla/
- fallback links: stockanalysis.com/stocks/tsla/
- final evidence status: evidence_complete
- remaining gaps: 能源存储业务具体数据、中国市场份额趋势
