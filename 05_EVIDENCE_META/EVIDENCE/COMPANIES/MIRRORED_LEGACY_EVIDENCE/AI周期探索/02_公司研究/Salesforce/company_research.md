---
title: "company_research"
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
legacy_path: "AI周期探索/02_公司研究/Salesforce/company_research.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Salesforce (CRM) Company Research

## 一句话

Salesforce 正在执行从 CRM 座位许可软件公司到 AI 代理基础设施平台的深刻转型，Headless 360 + Agentforce + Slack AI 三位一体架构让公司直接回应了 SaaSpocalypse 生存问题。

## MCP 证据摘要

- **覆盖评估**: 优秀。TechCrunch（Q4/FY26 财报详细数据）、VentureBeat（3 篇深度产品报道）、FT（SaaSpocalypse 叙事）、IDC（2 篇分析报告）
- **覆盖充足**: 财报数据完整（收入/利润/RPO/指引）、产品路线图清晰（Headless 360/Agentforce/Slack AI）、竞争格局可见（Klaviyo/Writer/Dynamics）
- **核心证据**: 10 条，涵盖 media（TechCrunch/FT）、review（VentureBeat×3）、report（IDC×2）、official_press（VentureBeat）
- **证据级别**: 报告级（IDC）+ 媒体级（TechCrunch/FT/VentureBeat），足以支撑核心判断

## 结构性转变

**旧故事**：全球最大 CRM SaaS 公司，按座位收费，卖 Sales Cloud / Service Cloud / Marketing Cloud，依赖 AppExchange 生态锁定。

**新故事**：AI 代理基础设施平台。核心转变发生在三个层面：

1. **Headless 360（2026-04-16 TDX）**: 27 年历史上最大架构转型，将整个平台能力以 API、MCP 工具、CLI 暴露给 AI 代理，100+ 新工具（60+ MCP 工具 + 30+ 预配置编码技能），开源 Agent Script 和测试套件。公司原话："We made a decision two and a half years ago: Rebuild Salesforce for agents."
2. **Agentforce Operations（2026-05-01）**: 工作流执行控制平面，将企业后端流程拆解为确定性任务供代理执行，提供 Blueprints + 会话追踪 + 人工检查点。解决"工作流不是为代理设计的"这一核心问题。
3. **Slack AI（2026-03-31）**: 30+ 新 AI 功能，基于 Anthropic Claude，将 Slackbot 从聊天助手升级为企业代理——跨视频会议记录、MCP 第三方工具调用、轻量级 CRM。

**定价模式转变**: 从座位计费转向按消耗计费（Agentforce），引入 AWU（Agent Work Units）新指标衡量代理实际产出。

## 飞轮

```
企业 CRM 数据积累（最大安装基础）
  → 工作流上下文（Sales/Service/Marketing Cloud 流程）
  → AI 代理执行数据（Agentforce Operations）
  → 更精准的代理行为（Headless 360 开放架构）
  → 更多企业依赖 Salesforce 数据引力
  → 消耗计费放大收入
```

**飞轮验证状态**: 数据层飞轮已验证（$72B RPO）。代理层飞轮刚开始转动（Headless 360 2026-04 发布，Agentforce Operations 2026-05 发布）。

## What They Control

- **CRM 数据引力**: 全球最大企业客户数据集合，Informatica 收购（$8B）增强数据集成
- **企业工作流**: Sales/Service/Marketing Cloud 流程深入企业运营
- **协作层**: Slack 作为"工作中心"（IDC 确认定位），上下文工程 + Claude 集成
- **生态**: AppExchange + AgentExchange，第三方开发者锁定
- **$72B RPO**: 已签约未确认收入的合同，提供强大收入可见性

## Market's Old Eyes

市场以传统 SaaS P/S 估值 Salesforce，担心 SaaSpocalypse（AI 代理替代座位模式）。iShares 扩展科技软件 ETF 在 Salesforce 财报前下跌约 10%。

但可能忽略了：
1. Headless 360 不是防御，是进攻——主动把 CRM 变成 AI 代理的运行基础设施
2. 消耗计费模式如果成功，可能扩大 TAM（每个代理的 API 调用 > 每个人头的座位费）
3. $72B RPO 提供转型缓冲，不是在悬崖边上转型

## 失败条件

1. **座位收入下降速度快于消耗收入增长**: AI 代理减少 CRM 用户数，消耗收入不够弥补缺口
2. **消耗模式经济性差**: 代理执行任务的成本高于收入，利润率压缩
3. **竞争替代**: Klaviyo（Autonomous CRM + 首次盈利）、HubSpot、Microsoft Dynamics 从 SMB 向上侵蚀
4. **Informatica 整合失败**: $8B 收购整合风险
5. **OpenAI/Anthropic 直接切入**: 如果 AI 模型公司直接提供 CRM 能力，绕过 Salesforce

## 财务评估

| 指标 | 数据 | 备注 |
|---|---|---|
| Q4'26 收入 | $10.7B (+13% YoY) | 含 Informatica 贡献 |
| FY26 收入 | $41.5B (+10% YoY) | |
| 净利润 | $7.46B | 18% 净利率 |
| RPO | $72B+ | 强收入可见性 |
| FY27 指引 | $45.8-46.2B (+10-11%) | |
| 回购 | $50B | 增加股东回报 |
| Informatica 收购 | $8B（2025-05） | 数据管理增强 |
| AWU 指标 | 新推出 | 衡量代理产出，待验证 |

## 核心结论

Salesforce 的结构性转变是真实的、有资金支持的、有路线图的。与 Atlassian 不同，Salesforce 不是在裁员后声称转型，而是用 $41.5B 收入和 $72B RPO 在转型中保持增长。Headless 360 + Agentforce + Slack AI 三位一体架构直接回应了 SaaSpocalypse 的核心挑战：如果 AI 代理减少座位需求，那就让 Salesforce 成为代理运行的基础设施。

关键不确定性：消耗计费模式能否在座位收入下降前产生足够收入。这决定了转型是"升级"还是"收入缺口"。

## 分类：观察（上档）

- 转型方向正确，执行力度强，财务基础扎实
- 但需要 Q1'27（FY27 Q1）看到 AWU 和消耗收入的实际数据
- 如果 Agentforce 收入加速 + 消耗模式经济性验证 → 可升级为核心候选
- 当前仍是观察，因为座位→消耗的转型是 SaaS 行业最大赌注，无人有成功先例
