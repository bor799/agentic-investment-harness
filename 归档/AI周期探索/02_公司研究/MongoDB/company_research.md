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
legacy_path: "AI周期探索/02_公司研究/MongoDB/company_research.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# MongoDB Company Research (PRO Updated 2026-05-17)

## 0. 覆盖声明

MCP 覆盖中等偏弱：SA 2篇 + MongoDB Blog 3篇 + 行业报道 3篇。PRO agent-reach 补充：StockAnalysis SEC 完整年报 + 分析师预测 + 估值数据。证据状态：evidence_complete。

## 1. 一句话结构性转变判断

MongoDB 从开源文档数据库转型为 Atlas 消费型云数据平台（72%营收），FY2026 FCF 爆发至 $500M(20.30% margin)验证盈利路径，但 GM 下滑(74.8%→71.8%) + Forward P/E 53x 昂贵 + pgvector 免费替代构成持续压力。

## 2. Source Coverage Status

- **MCP 证据**: SA 2篇(Atlas深度+Alger基金) + Blog 3篇(Agent Skills/MCP Server/扩缩容) + InfoQ/VentureBeat行业
- **agent-reach 证据**: StockAnalysis SEC FY2026年报 + 42位分析师预测 + 估值/市值数据
- **剩余缺口**: Atlas vs Non-Atlas收入拆分、>$100K ARR客户数、NRR具体数值、季度趋势

## 3. 结构变化和飞轮

### 结构变化（进行中，增速趋稳）
Atlas 72% 营收占比证实消费平台转型。FY2026 收入 +22.80% 比 FY2025 的 +19.22% 有所回升，但远低于 FY2024 的 +31%。增速从"高增长"过渡到"稳健增长"阶段。

### 飞轮（运行中，面临侵蚀）
```
开发者采纳文档模型
  → Atlas 云消费增长（72%营收）
  → 向量搜索/AI功能增强粘性
  → MCP Server/Agent Skills拥抱AI代理
  → 更多开发者采纳？
```

侵蚀压力：PostgreSQL + pgvector 从开发者生态侧 + Qdrant/Pinecone 从 AI 向量搜索侧两面夹击。

## 4. 财报/经营趋势

| 指标 | FY2024 | FY2025 | FY2026 | 趋势 |
|---|---|---|---|---|
| Revenue | $1,683M | $2,006M | $2,464M | +22.80% 回升 |
| Revenue Growth | +31.07% | +19.22% | +22.80% | V型企稳 |
| Gross Margin | 74.78% | 73.32% | 71.75% | 连续下滑⚠️ |
| Operating Margin | -13.89% | -10.77% | -5.56% | 大幅改善 |
| Net Income | -$176.6M | -$129.1M | -$71.15M | 亏损收窄 |
| FCF | $115.4M | $120.6M | $500.2M | 爆发增长 |
| FCF Margin | 6.86% | 6.01% | 20.30% | 3x提升 |
| Shares Outstanding | 72.7M | 80.5M | 80.5M | 稀释放缓 |

**关键矛盾**: FCF 爆发(20.30%) vs GM 下滑(71.75%)。FCF 改善来自运营效率提升，但定价权可能正在被侵蚀。

## 5. 估值隐含预期

| 指标 | 数值 | 备注 |
|---|---|---|
| Market Cap | $25.09B | +79.5% |
| Forward P/E | 53.44x | FY2027E EPS $5.89 |
| P/S (TTM) | ~10.2x | $25.09B / $2.46B |
| 52-Week Range | $182.43 - $444.72 | |
| Analyst Target | $370.79 (+18.78%) | 42位分析师 |
| Analyst Consensus | Buy | Mizuho看多"新阶段" |

Forward P/E 53x 对应 FY2027 收入增长 18.68% — PEG ~2.85，估值偏贵。市场定价了 Atlas 继续主导开发者数据库 + AI 工作负载增长的预期。

## 6. 竞争、监管、失败条件

- **PostgreSQL/pgvector**: 免费替代，开发者生态最大威胁，功能差距持续缩小
- **专用向量数据库**: Qdrant($50M B轮)/Pinecone 在 AI 场景专门化
- **Hyperscaler**: AWS DocumentDB/Azure Cosmos 直接竞争
- **新CRO**: Ryan Mac Ban 2026年4月上任，销售执行力待验证

**失败条件**:
1. pgvector 功能追平 Atlas Vector Search（正在发生）
2. Atlas 消费增速持续放缓
3. GM 继续下滑至 70% 以下
4. FY2027 盈利预测未能兑现

## 7. 未来 6-12 个月验证信号

1. **FY2027 Q1-Q2 财报**（May/Aug 2026）— 盈利进度
2. **Atlas 消费增速** — 是否维持 20%+
3. **GM 趋势** — 71.75% 是否触底
4. **NRR 数据** — 客户留存是否健康
5. **新CRO执行力** — 企业销售加速？

## 8. 三年翻倍路径：弱

Market Cap $25.09B → $50B 需 P/E 维持 50x+ + EPS 从 $5.89 增长到 ~$10+。
- 条件：Atlas 保持 20%+ 增速 + GM 止跌 + AI 工作负载爆发
- 风险：pgvector 侵蚀 + Forward P/E 53x 压缩 + 增速继续放缓
- PEG 2.85 暗示增长已大部分被定价

## 9. 分类与分数

**分类：观察(下档)→观察**（PRO 修复 +6）

理由：Atlas 转型真实 + FCF 20.30%验证盈利能力 + FY2027 预测首次盈利。但 GM 下滑 + pgvector 竞争 + Forward P/E 53x 限制升级空间。从"下档"升级为标准"观察"。

**总分：35/70**（PRO 修复更新 2026-05-17）
