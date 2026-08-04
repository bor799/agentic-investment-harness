---
title: "scorecard"
date: 2026-07-24
updated: 2026-07-24
layer: META
primary_role: legacy_scorecard
status: superseded
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
legacy_metadata_added: true
legacy_path: "AI周期探索/02_公司研究/Cloudflare/scorecard.md"
migration_target: "05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Scorecard — Cloudflare (NET)

| 维度 | 分数 | 理由 |
|---|---:|---|
| 结构性转变 | 7 | CDN/边缘安全 → AI代理运行时是真实结构性转变。Dynamic Workers + Code Mode MCP Server 从边缘安全延伸到AI代理执行层，20M+网站网络效应提供基础。但转变仍在早期，收入结构尚未反映。 |
| 真瓶颈 | 7 | AI代理安全执行是新兴瓶颈。Cloudflare的isolate沙箱（比容器快~100x）解决AI代理代码执行的隔离和延迟问题。边缘位置+身份层+安全策略的组合形成结构性壁垒。但AWS/Azure也有边缘计算能力。 |
| 定价权 | 6 | Workers平台有一定定价权（开发者生态粘性），但CDN/WAF层商品化严重。AI代理运行时定价模式未确立。企业客户Zero Trust产品有切换成本但非独占。 |
| 利润率变化 | 4 | Q1'26净亏损$62M且扩大，尚未证明盈利路径。34%增速虽强但1,100人裁员暗示成本压力。AI代理运行时毛利率尚不确定。 |
| 6-12个月验证性 | 7 | Workers AI收入独立披露、Dynamic Workers采用率、AI代理流量占比、亏损收窄趋势均可季度追踪。RPO $2.5B提供短期收入可见性。 |
| 3年翻倍路径 | 5 | 可能但需多个条件同时成立：AI代理运行时市场爆发、Workers收入占比显著提升、实现盈利。当前亏损状态使路径依赖外部市场验证。 |
| 能力圈匹配 | 7 | 边缘网络+安全+开发者平台的组合独特。330+城市部署、20M+网站、Workers运行时形成难以复制的物理+软件护城河。但与AWS/Azure/GCP的全面竞争中规模劣势明显。 |

**总分：43/70**

**分类：观察**

核心判断：结构性转变方向正确，但财务验证不足。需看到Workers AI收入贡献和盈利趋势后再评估是否升级。
