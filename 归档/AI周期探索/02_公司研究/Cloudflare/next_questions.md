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
legacy_path: "AI周期探索/02_公司研究/Cloudflare/next_questions.md"
migration_target: "03_STATE/HYPOTHESIS_QUEUE"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Cloudflare Next Questions

## 高优先级（影响分类）

### 1. Workers AI 收入独立披露
- **问题**：Workers 平台收入占总收入比例？AI 相关收入是否独立披露？
- **验证方式**：Q2'26 财报电话会、10-Q 文件
- **判断影响**：Workers AI 收入占比 >20% → 结构性转变被财务验证

### 2. 盈利路径时间表
- **问题**：管理层是否给出盈利时间表？自由现金流趋势如何？
- **验证方式**：财报电话会指引
- **判断影响**：明确的盈利路径 + FCF 改善 → 可升级为核心候选

### 3. Dynamic Workers 客户采用
- **问题**：Dynamic Workers 有多少付费客户？主要用例是什么？
- **验证方式**：产品公告、客户案例、开发者社区活跃度
- **判断影响**：大量企业客户采用 → AI 代理运行时定位验证

## 中优先级（影响评分）

### 4. AI 代理流量占比
- **问题**：总流量中 AI 代理/bot 流量占比？趋势如何？
- **验证方式**：Cloudflare Radar 数据、年度安全报告
- **判断影响**：AI 流量快速增长 → 安全+流量管理从成本项变增长项

### 5. 与 AWS/Azure 边缘竞争格局
- **问题**：Cloudflare Workers vs Lambda@Edge vs Azure Functions 在 AI 代理场景的功能和性能对比？
- **验证方式**：开发者基准测试、行业报告
- **判断影响**：Workers 技术优势明显 → 护城河确认

### 6. RPO 质量和组成
- **问题**：$2.5B RPO 中多少来自 Workers/平台 vs 传统 CDN/安全？平均合同期限？
- **验证方式**：财报披露
- **判断影响**：Workers RPO 占比提升 → 平台转型加速
