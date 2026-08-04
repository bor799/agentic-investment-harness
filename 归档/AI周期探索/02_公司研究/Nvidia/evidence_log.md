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
legacy_path: "AI周期探索/02_公司研究/Nvidia/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Nvidia Evidence Log

## MCP citation 规则

每条关键证据必须来自 Mindspace Source MCP，除非明确标注 fallback。

| source_name | source_tab | source_id | item_id | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|---|---|
| U.S. News (CNBC) | media | 2a2b77c4 | 9d3a0a309ff7e8c06f7d9b5cf5aa3c7c | cnbc.com/2026/02/25/nvidia-nvda-earnings-report-q4-2026.html | 2026-02-26 | 核心证据：FY26 Q4财报，营收$68.13B(+73%), 数据中心$62.3B(+75%), 净利润$43B, 指引$78B, Vera Rubin首批样机已交付 | 高 | 含完整财务数据+产品路线图+供应链多元化, get_article_detail已回源 |
| Earnings (CNBC) | media | 0a85b9dd | d296c06dca7cf93c8617a632edb58893 | cnbc.com/2026/02/25/nvidia-keeps-the-ai-party-alive-with-a-booming-quarter-and-even-better-outlook.html | 2026-02-26 | 核心证据：分析师解读，Hopper/Ampere旧芯片仍售罄，供给承诺延伸至2027，$500B Blackwell+Rubin收入机会 | 高 | 含管理层引言+竞争分析+估值讨论, get_article_detail已回源 |
| U.S. News (CNBC) | media | 2a2b77c4 | 32d4cf40fe600ac14625d023e348f448 | cnbc.com/2026/02/24/nvidia-earnings-collide-with-wall-street-skepticism-over-ai-spending.html | 2026-02-24 | 核心证据：华尔街AI支出怀疑论，hyperscaler capex $700B预期+见顶担忧，Groq $20B收购+Vera Rubin期待 | 高 | 含竞争格局+估值风险+分析师观点, get_article_detail已回源 |
| U.S. News (CNBC) | media | 2a2b77c4 | a5e45a82381ae9edb5de25f7e4d65f28 | cnbc.com/2026/02/27/nvidia-wraps-tough-week-as-investors-focus-on-competition-over-growth.html | 2026-02-27 | 核心证据：竞争加剧信号，OpenAI→AWS Trainium/Meta→AMD+TPU，客户分散化削弱Nvidia定价杠杆 | 中高 | 竞争风险验证 |
| Earnings (CNBC) | media | 0a85b9dd | 692ef17ebd37ea91ea0c5037f06003cf | cnbc.com/2026/05/08/wall-street-ai-chip-love-moves-from-nvidia-to-intel-amd-and-micron.html | 2026-05-08 | 补充证据：AI投资轮动从Nvidia→更广泛硬件(Intel/AMD/Micron)，"换岗"叙事 | 中 | 市场情绪转变信号 |
| Earnings (CNBC) | media | 0a85b9dd | ca2fabc856015001f71b9f12429530cb | cnbc.com/2026/02/25/nvidia-forecast-points-to-accelerating-growth-vera-rubin-hits-market.html | 2026-02-26 | 核心证据：营收增速加速至77%，Vera Rubin样机交付，每瓦性能10x | 高 | 产品路线图验证 |
| SemiAnalysis | review | f850db7e | ccd19a146709f2d5a1c4dec50aca9173 | newsletter.semianalysis.com/p/dissecting-nvidia-blackwell-tensor | 2026-03-31 | 补充证据：Blackwell架构深度分析，PTX/SASS级微基准，技术护城河验证 | 中高 | review级别技术分析 |
| SemiAnalysis | review | f850db7e | fd928028b4756584b1e3376e6485f234 | newsletter.semianalysis.com/p/ai-value-capture-the-shift-to-model | 2026-05-01 | 核心证据：AI价值捕获转移，Nvidia有再定价空间，SOCAMM+Vera Rubin内存定价 | 中高 | 产业链价值分配分析 |
| Seeking Alpha (Long Ideas) | official_press | 21dc2b4b | 2874bede7722a3753a86ca9a32d568c2 | seekingalpha.com/article/4879889-nvidia-the-market-is-wrong | 2026-03-08 | 补充证据：前瞻P/E 22.66x，EV/Sales 12.01x，中国市场恢复可额外增加$200-300B | 中 | 估值参考 |
| Mad Money (CNBC) | media | 5be8df74 | 87e366665bce1b53a6779e871fe57a80 | cnbc.com/2026/05/07/nvidia-ceo-ai-partnership-corning-revitalize-american-manufacturing.html | 2026-05-07 | 补充证据：Nvidia-Corning硅光子合作，康宁扩产10x，3000+岗位 | 中 | 供应链扩展信号 |

## fallback 记录

| fallback_reason | search_query | link | used_for | notes |
|---|---|---|---|---|
| 无需fallback | N/A | N/A | N/A | MCP NVDA专用频道(5931c9a3)覆盖优秀，103 sources含filing_feed/media/report/review |

## 覆盖不足或冲突

### 优势
- **财务数据完整**: FY26 Q4完整财报数据（营收/利润/指引/分部收入）
- **多维度证据**: 财报+竞争分析+技术深度+估值讨论+地缘政治
- **高质量信源**: CNBC(media) + SemiAnalysis(review) + Seeking Alpha(official_press)
- **竞争格局清晰**: AMD/custom ASIC/hyperscaler自研均有证据

### 不足
- **无filing_feed级别财报**: 主要依赖CNBC媒体解读，无SEC filing直接引用
- **Q1 FY27实际结果**: FY27 Q1（4月季度）实际财报可能已发布但MCP中未找到
- **OpenAI合作关系**: $100B协议尚未最终确定，具体状态不明
- **中国收入**: 管理层称指引未包含中国数据中心收入，具体影响不确定

### 冲突
- **管理层乐观（供给承诺至2027+$500B收入机会）vs 华尔街怀疑（capex见顶+竞争侵蚀）**: 两种叙事均有证据支撑，当前无法判断哪个更接近现实
- **旧代产品售罄（需求强劲）vs 投资轮动（Nvidia→更广泛硬件）**: 短期需求vs长期竞争格局的矛盾

## Agent-Reach Sources (PRO Update 2026-05-17)

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| **StockAnalysis (SEC filings)** | FY2026(Jan): Revenue $215.94B(+65.47%), GM 71.07%, OM 60.38%, NI $120.07B(+64.75%), FCF $96.68B(44.77%) | 财务核心 | 极高 | Period ending Jan 25, 2026 |
| **StockAnalysis (forecast)** | FY2027E: Revenue $375.73B(+74%), EPS $8.47; FY2028E: $498.55B(+33%), EPS $11.57 | 预测 | 高 | |
| **StockAnalysis (analysts)** | Strong Buy(37人), PT $273.62(+21.44%), Range $195-$360 | 分析师估值 | 高 | |

## PRO source coverage

- Mindspace status: 10条 MCP 证据(media/review/official_press)，财报+竞争+技术+供应链覆盖极好
- agent-reach triggered: yes (PRO补充估值/预测)
- final evidence status: evidence_complete
- remaining gaps: FY27 Q1实际结果、OpenAI $100B协议最终状态

## Evidence Assessment: PRO evidence_complete

覆盖4/4证据桶：
1. **财报/经营**: FY2026 Revenue $215.94B(+65.47%)/NI $120.07B/FCF $96.68B(44.77%)
2. **估值/市场预期**: Market Cap $5.46T/Forward P/E 26.88/Strong Buy PT +21.44%/FY2027-2028E
3. **结构性变化**: CUDA+系统+网络全栈/Vera Rubin交付/Blackwell售罄至2027
4. **失败条件**: hyperscaler自研(OpenAI→AWS Trainium/Meta→AMD)/CapEx见顶担忧/Groq $20B竞争
