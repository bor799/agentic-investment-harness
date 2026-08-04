---
title: "next_questions"
date: 2026-07-24
updated: 2026-07-24
layer: STATE
primary_role: legacy_company_question_state
status: superseded
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
legacy_metadata_added: true
legacy_path: "AI周期探索/02_公司研究/Datadog/next_questions.md"
migration_target: "03_STATE/HYPOTHESIS_QUEUE"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Datadog Next Questions

## 高优先级（影响分类）

### 1. AI 工作负载可观测性收入占比
- **问题**: AI 相关功能（GPU 监控、LLM 可观测性、AI agent 安全）贡献了多少收入？是独立品类还是功能附加？
- **验证方式**: Q2/Q3 FY26 财报电话会、投资者日
- **判断影响**: AI 可观测性收入 >15% 且独立披露 → 转型验证；未披露或 <5% → 只是功能延伸

### 2. Hyperscaler 竞争实际影响
- **问题**: AWS CloudWatch / Google Cloud Operations 对 Datadog 新客户获取和续约率的实际影响？
- **验证方式**: 财报中客户净留存率（NRR）、大型企业客户增长、churn 原因披露
- **判断影响**: NRR 从 130%+ 降至 120% 以下 → 竞争实质性侵蚀

### 3. Usage-based 定价韧性
- **问题**: 客户成本优化（FinOps）是否压缩 Datadog 单客户收入增速？usage-based 在降本周期中表现如何？
- **验证方式**: 季度 DBNER（dollar-based net expansion rate）、平均客户合同值变化
- **判断影响**: DBNER <115% → usage-based 模式在成本压力下弹性不足

## 中优先级（影响评分）

### 4. 估值与增长匹配
- **问题**: 当前 P/S 和 P/E 处于什么水平？30% 增速是否已充分定价？
- **验证方式**: 财报发布后估值计算，对比 Dynatrace/Splunk 估值倍数
- **判断影响**: P/S >20x 且增速降至 25% 以下 → 估值压缩风险

### 5. 企业级市场渗透深度
- **问题**: 大型企业（>$1B 收入）客户占比和增速？AI 工作负载是否推动更多企业级采购？
- **验证方式**: 财报中企业客户数量、ARR>$100K 客户数
- **判断影响**: 企业客户增速 > 营收增速 → 平台价值验证

### 6. 开源替代威胁
- **问题**: Grafana/Mimir/OpenTelemetry 在大型企业的采用率？自建趋势是否加速？
- **验证方式**: Grafana Labs 融资和营收、OpenTelemetry 社区活跃度
- **判断影响**: 大型企业自建比例 >20% → Datadog TAM 上限收窄
