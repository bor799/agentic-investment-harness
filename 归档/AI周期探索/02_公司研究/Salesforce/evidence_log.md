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
legacy_path: "AI周期探索/02_公司研究/Salesforce/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Salesforce Evidence Log

## MCP citation 规则

每条关键证据必须来自 Mindspace Source MCP，除非明确标注 fallback。

| source_name | source_tab | source_id | item_id | link | published_at | evidence_use | confidence | notes |
|---|---|---|---|---|---|---|---|---|
| AI News & Artificial Intelligence \| TechCrunch | media | 2b410a5f-04a2-465c-8e72-1e20335f89ac | 18f9bf90e2bceb101a3e2b9613d40258 | techcrunch.com/2026/02/25/salesforce-ceo-marc-benioff-this-isnt-our-first-saaspocalypse/ | 2026-02-25 | 核心证据：Q4'26 $10.7B(+13%)、FY26 $41.5B(+10%)、净利$7.46B、RPO $72B+、FY27指引$45.8-46.2B、$50B回购、AWU指标、Benioff回应SaaSpocalypse | 高 | 一手财报数据+管理层叙事 |
| VentureBeat | review | 5b991a01-d92a-4a21-92ad-5fd78179c27f | 45f875e9d09c0fe86f999fa90ff9c7d8 | venturebeat.com/technology/salesforce-launches-headless-360-to-turn-its-entire-platform-into-infrastructure-for-ai-agents | 2026-04-16 | 核心证据：Headless 360发布，100+新工具(60+ MCP/30+技能)，27年最大架构转型，API/MCP/CLI全暴露，消耗计费转型 | 高 | 产品深度报道，含官方声明和行业分析 |
| VentureBeat | review | 5b991a01-d92a-4a21-92ad-5fd78179c27f | 614f862f86e0e1e4acff5fe36968de8e | venturebeat.com/orchestration/salesforce-launches-agentforce-operations-to-fix-the-workflows-breaking-enterprise-ai | 2026-05-01 | 核心证据：Agentforce Operations发布，工作流执行控制平面，确定性任务拆解，Blueprints+会话追踪+人工检查点 | 高 | 含SVP Sanjna Parulekar采访 |
| VentureBeat | review | 5b991a01-d92a-4a21-92ad-5fd78179c27f | f4434bbdd313b1863e666e2e43a08b57 | venturebeat.com/orchestration/slack-adds-30-ai-features-to-slackbot-its-most-ambitious-update-since-the | 2026-03-31 | 核心证据：Slack AI 30+功能，Claude驱动，MCP集成，轻量CRM，会议记录，Business+/Enterprise+快速采用 | 中高 | 收购后最大更新 |
| UK homepage (FT) | media | 53698bdc-9fb2-4bc6-abd8-527597460708 | adeebc5dd631949bc3d48f9557ad5a19 | ft.com/content/b74b8227-d7cb-4976-ba95-a3a27b79cbdd | 2026-02-26 | 补充证据：Benioff否认SaaS-pocalypse，AI增强而非取代企业软件 | 中 | 管理层叙事 |
| rssitbuyer (IDC) | report | 8da847b0-f9d8-4f0d-9f38-579a5b295534 | 42a8c7f2e7ea76588d052cc4b68d3ad1 | my.idc.com/getdoc.jsp?containerId=lcUS54524026 | 2026-05-01 | 核心证据：IDC确认"platform inflection point"，Slack=工作中心，Headless 360=agentic使能层，不是产品发布而是平台拐点 | 高 | IDC分析师观点 |
| rsssoftware (IDC) | report | e0629e72-9660-439f-b6ce-354af657bfc4 | fa1a753ccf58c3f0e2612834402faed9 | my.idc.com/getdoc.jsp?containerId=lcUS54534126 | 2026-05-07 | 竞争证据：Klaviyo实现"Autonomous CRM"首个盈利季度，威胁Salesforce SMB段 | 中 | 竞争格局信号 |
| VentureBeat | review | 5b991a01-d92a-4a21-92ad-5fd78179c27f | c4e1fc60c0d1b293ef3f8797dfccc4ee | venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among | 2026-04-03 | 补充证据：Salesforce为Nvidia Agent Toolkit 17家采用者之一 | 低 | 合作信号 |
| VentureBeat | review | 5b991a01-d92a-4a21-92ad-5fd78179c27f | 61aea922191ecd28db0157696f1de319 | venturebeat.com/technology/writer-launches-ai-agents-that-can-act-without-prompts-taking-on-amazon-microsoft-and-salesforce | 2026-04-30 | 竞争证据：Writer推出事件触发代理，直接竞争Salesforce Agentforce | 中 | 竞争压力 |
| rssitbuyer (IDC) | report | 8da847b0-f9d8-4f0d-9f38-579a5b295534 | e980ab1133973501cf091448f6e26f95 | my.idc.com/getdoc.jsp?containerId=US53322726 | 2026-03-27 | 背景证据：Salesforce实施服务关键在人与治理，非纯技术 | 低 | 实施复杂性信号 |

## fallback 记录

| fallback_reason | search_query | link | used_for | notes |
|---|---|---|---|---|
| 无需fallback | N/A | N/A | N/A | MCP覆盖优秀，财报+产品+竞争+分析师全覆盖 |

## 覆盖评估

### 优势
- **财报数据完整**: Q4/FY26 收入、利润、RPO、指引均有
- **产品路线图清晰**: Headless 360、Agentforce Operations、Slack AI 三条线均有深度报道
- **分析师背书**: IDC 2 篇报告确认"平台拐点"判断
- **竞争可见**: Klaviyo、Writer、Dynamics 竞争信号

### 不足
- **估值数据缺失**: 无 P/E、P/S、EV/EBITDA 等（MCP 不覆盖金融数据）
- **消耗收入占比缺失**: AWU 指标刚推出，尚无具体数字
- **客户留存率缺失**: 无 Net Retention Rate 数据

## Agent-Reach Sources (PRO Update 2026-05-17)

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| **StockAnalysis (SEC filings)** | TTM: Revenue $41.53B(+9.6%), GM 77.68%, OM 20.06%, NI $7.46B(+20.3%), FCF $14.40B(34.68%) | 财务核心 | 极高 | |
| **StockAnalysis (forecast)** | FY2027E: Revenue $46.61B(+12.2%), EPS $13.32(+70.8%); FY2028E: $51.02B(+9.5%), EPS $14.98 | 预测 | 高 | EPS大幅跃升 |
| **StockAnalysis (analysts)** | Buy(35人), PT $278.40(+60.45%), Range $188-$405 | 分析师估值 | 高 | PT上行空间大 |

## PRO source coverage

- final evidence status: evidence_complete

## Evidence Assessment: PRO evidence_complete

覆盖4/4证据桶：
1. **财报/经营**: TTM Revenue $41.53B(+9.6%)/NI $7.46B/FCF $14.40B(34.68%)
2. **估值/市场预期**: Market Cap $141.94B/Forward P/E 13.16/Buy PT +60.45%/FY2027-2028E
3. **结构性变化**: Headless 360+Agentforce+座位→消耗转型
4. **失败条件**: 增速9.6%放缓+消耗计费不确定性+竞争(Dynamics/HubSpot)
