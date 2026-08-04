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
legacy_path: "AI周期探索/02_公司研究/Google/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Google Evidence Log

## MCP citation 规则

每条关键证据必须来自 Mindspace Source MCP，除非明确标注 fallback。

| source_name | source_tab | source_id | item_id | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|---|---|
| WIRED | media | 3cea7812-d64e-4db0-b5af-8863edc85518 | 1fc622e79a62a66be4c45b41adc08a42 | wired.com/story/google-nick-fox-advertising-search-ai-gemini | 2026-03-12 | 核心证据：SVP Nick Fox 采访。2025年收入$400B+首次突破；Gemini 750M MAU（较350M翻倍）；不排除Gemini广告；AI Mode/AI Overviews/Gemini融合方向；Personal Intelligence是搜索"holy grail" | 高 | 回源确认，核心管理层信号 |
| WIRED | media | 163cb0f2-beaf-4520-93d5-cb10f4fc6479 | 824bfeb1f66651b1f5972b8b53b75675 | wired.com/story/google-ai-searches-love-to-refer-you-back-to-google | 2026-03-13 | 核心证据：AI Mode自引率17%（3x YoY增长）；YouTube第二大引用；娱乐/旅行领域约半数自引；"zero-click web"趋势；Google是AI流量最大受益者 | 高 | 回源确认，SE Ranking独立研究 |
| All About Circuits | official_press | 0380f531-724b-4d43-8b3a-63669fdbabbe | b16c7fa47224ce20e2e78a704b7a4e96 | allaboutcircuits.com/news/arm-axion-heads-googles-8th-gen-tpus-as-cloud-pivots-to-agentic-ai | 2026-05-05 | 第8代TPU拆分训练/推理变体；Arm Neoverse Axion CPU统一主机架构；Google Cloud明确转向Agentic AI；Arm发布Performix工具包 | 高 | 回源确认，硬件基础设施证据 |
| Google Developers Blog | blog | 287df69d-0aff-4868-a8ee-b8fb3759d831 | 95019a75e4030497020b09846e10b19d | developers.googleblog.com/building-with-gemini-embedding-2 | 2026-04 | Gemini Embedding 2 GA：首个统一多模态嵌入模型（文本/图像/视频/音频/文档同一向量空间），100+语言；Harvey Recall@20+3%、Supermemory Recall@1+40%、Nuuly Match@20由60%升至87% | 中 | 产品能力证据 |
| Google Developers Blog | blog | 287df69d-0aff-4868-a8ee-b8fb3759d831 | 8339a303e8471c63fa46b141652fd072 | developers.googleblog.com (Cloud Next '26) | 2026-04 | Google Cloud Next '26聚焦agentic AI、Gemini、Vertex AI、Cloud Run；4月22-24日拉斯维加斯 | 中 | 战略方向信号 |
| Slashdot | review | 693d0d1a-424b-49d2-b4be-56f65a278165 | d00aba0d9200a09446ba7875fe4f66f1 | yro.slashdot.org (Google-Pentagon AI) | 2026-04-16 | Google与五角大楼讨论机密Gemini部署协议；合同限制：禁止国内大规模监控和缺乏人类控制的自主武器 | 中 | 政府合同信号 |
| Slashdot | review | c4d81ee0-2589-4ee1-839c-bfe245049ccb | fde64ec4009746634c47d12a851c61c7 | tech.slashdot.org (Gemma 4) | 2026-04-02 | Google发布Gemma 4开源模型（26B MoE到E2B/E4B移动端），切换到Apache 2.0许可 | 低 | 开源生态策略 |
| The Guardian | media | 1b5510f5-7e99-49ca-9367-c4214d5d4ac7 | 665203e8d6f1fb69044bd35e66badc26 | theguardian.com/technology (Gemini lawsuit) | 2026-03-04 | Gemini安全事件：用户自杀诉讼，家属起诉Google过失致死和产品责任；可能成为AI安全法律标杆案例 | 中 | 风险因素 |
| The Guardian | media | 1b5510f5-7e99-49ca-9367-c4214d5d4ac7 | 12833f48c558da8bb27fc2bf0dcea925 | theguardian.com/technology (AI Overviews health) | 2026-02-16 | AI Overviews医疗建议免责声明不明显，专家警告可能导致错误诊断 | 低 | 产品风险 |
| arXiv | paper_repo | 6cea19f9-d629-4d4f-890b-2fd9dc870939 | 78fd35e2f2774152635e3c2170485a54 | arxiv.org/abs/2602.17675 | 2026-02-23 | Gemini Enterprise A2A Hub跨项目/跨账号部署实践；Cloud Run + Vertex AI架构 | 低 | 技术架构参考 |

## fallback 记录

| fallback_reason | search_query | link | used_for | notes |
|---|---|---|---|---|
| 无需fallback | N/A | N/A | N/A | MCP覆盖足够完成核心分析，财务数据从WIRED采访间接获得 |

## 覆盖不足或冲突

### MCP 覆盖中等偏强
- **有**: AI搜索战略（WIRED 2篇详细回源）、TPU硬件（回源确认）、产品路线（Google Blog）、安全风险（Guardian/Slashdot）
- **无**: 具体季度财报数据（Q1'26 收入/利润/Cloud增速）、前瞻P/E估值、分析师共识、反垄断判决最新进展
- **缓解**: WIRED采访提供 $400B+ 收入和 Gemini 750M MAU 关键数字；估值数据可在 Web search 可用后补充

## Agent-Reach Sources (PRO Update 2026-05-17)

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| **StockAnalysis (SEC filings)** | TTM: Revenue $422.50B(+17.5%), GM 60.37%, OM 32.69%, NI $160.21B(+44.3%), FCF $64.43B(15.25%) | 财务核心 | 极高 | Period ending Mar 2026 |
| **StockAnalysis (forecast)** | FY2026E: Revenue $496.39B(+23.2%), EPS $13.62; FY2027E: $583.96B(+17.6%), EPS $14.58 | 预测 | 高 | |
| **StockAnalysis (analysts)** | Strong Buy(45人), PT $394.82(-0.49%!)⚠️, Range $190-$515 | 分析师估值 | 高 | PT接近持平=接近公允 |

## PRO source coverage

- Mindspace status: 10条 MCP 证据(media/blog/review/paper_repo)，AI搜索+TPU+产品路线覆盖好
- Mindspace gap: 精确季度财报+估值数据
- agent-reach triggered: yes (PRO补充)
- final evidence status: evidence_complete
- remaining gaps: Q1'26 Cloud增速细节、反垄断判决进展

## Evidence Assessment: PRO evidence_complete

覆盖4/4证据桶：
1. **财报/经营**: TTM Revenue $422.50B(+17.5%)/NI $160.21B/FCF $64.43B(15.25%)
2. **估值/市场预期**: Market Cap $4.81T/Forward P/E 31.65/Strong Buy PT -0.49%⚠️/FY2026-2027E
3. **结构性变化**: AI Search+Personal Intelligence+Gemini 750M MAU+TPU第8代
4. **失败条件**: 反垄断风险+AI搜索自引17%/FCF margin仅15.25%(CapEx压力)+PT零上行
