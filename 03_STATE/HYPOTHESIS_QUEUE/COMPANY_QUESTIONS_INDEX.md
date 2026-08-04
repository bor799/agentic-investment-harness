---
title: company_questions_index
date: 2026-07-23
updated: 2026-07-23
layer: STATE
primary_role: company_questions_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
data_cutoff: 2026-07-23
expires_at: 2026-08-23
---

# Company Questions Index

## 先说人话

**今天发生了什么：**旧公司目录里的 `research_task`、`next_questions` 和 `next_signals` 统一接入 State 队列。

**为什么重要：**这些文件是当前研究状态，不是长期公司结论；必须定期刷新，过期后不能继续当作当前问题。

**现在做什么：**做公司研究前先看这里，再决定哪些问题需要刷新。

| 公司 / 标的 | State 类型 | 旧文件 |
|---|---|---|
| `Alibaba` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Alibaba/next_questions]] |
| `Alibaba` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Alibaba/research_task]] |
| `Atlassian` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Atlassian/next_questions]] |
| `Atlassian` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Atlassian/research_task]] |
| `Aux Electric` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Aux Electric/next_questions]] |
| `Aux Electric` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Aux Electric/research_task]] |
| `Beike` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Beike/next_questions]] |
| `Beike` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Beike/research_task]] |
| `Berkshire Hathaway B` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Berkshire Hathaway B/next_questions]] |
| `Berkshire Hathaway B` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Berkshire Hathaway B/research_task]] |
| `Bilibili` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Bilibili/next_questions]] |
| `Bilibili` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Bilibili/research_task]] |
| `BitGo Holdings` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/BitGo Holdings/next_questions]] |
| `BitGo Holdings` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/BitGo Holdings/research_task]] |
| `CRRC` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/CRRC/next_questions]] |
| `CRRC` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/CRRC/research_task]] |
| `Circle` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Circle/next_questions]] |
| `Circle` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Circle/research_task]] |
| `Cloudflare` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Cloudflare/next_questions]] |
| `Cloudflare` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Cloudflare/research_task]] |
| `Coinbase` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Coinbase/next_questions]] |
| `Coinbase` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Coinbase/research_task]] |
| `Datadog` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Datadog/next_questions]] |
| `Datadog` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Datadog/research_task]] |
| `Duolingo` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Duolingo/next_questions]] |
| `Duolingo` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Duolingo/research_task]] |
| `Figure Technology` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Figure Technology/next_questions]] |
| `Figure Technology` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Figure Technology/research_task]] |
| `Fuyao Glass` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Fuyao Glass/next_questions]] |
| `Fuyao Glass` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Fuyao Glass/research_task]] |
| `GitLab` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/GitLab/next_questions]] |
| `GitLab` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/GitLab/research_task]] |
| `Google` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Google/next_questions]] |
| `Google` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Google/research_task]] |
| `Hang Seng Tech Index` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Hang Seng Tech Index/next_questions]] |
| `Hang Seng Tech Index` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Hang Seng Tech Index/research_task]] |
| `HashKey Holdings` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/HashKey Holdings/next_questions]] |
| `HashKey Holdings` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/HashKey Holdings/research_task]] |
| `Horizon Robotics` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Horizon Robotics/next_questions]] |
| `Horizon Robotics` | `state_next_signals` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Horizon Robotics/next_signals]] |
| `Horizon Robotics` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Horizon Robotics/research_task]] |
| `Lemonade` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Lemonade/next_questions]] |
| `Lemonade` | `state_next_signals` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Lemonade/next_signals]] |
| `Lemonade` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Lemonade/research_task]] |
| `Li Auto` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Li Auto/next_questions]] |
| `Li Auto` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Li Auto/research_task]] |
| `Lumentum` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Lumentum/next_questions]] |
| `Lumentum` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Lumentum/research_task]] |
| `Marvell Technology` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Marvell Technology/next_questions]] |
| `Marvell Technology` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Marvell Technology/research_task]] |
| `Meituan` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Meituan/next_questions]] |
| `Meituan` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Meituan/research_task]] |
| `Meta` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Meta/next_questions]] |
| `Meta` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Meta/research_task]] |
| `Micron` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Micron/next_questions]] |
| `Micron` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Micron/research_task]] |
| `Microsoft` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Microsoft/next_questions]] |
| `Microsoft` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Microsoft/research_task]] |
| `Miniso` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Miniso/next_questions]] |
| `Miniso` | `state_next_signals` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Miniso/next_signals]] |
| `Miniso` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Miniso/research_task]] |
| `MongoDB` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/MongoDB/next_questions]] |
| `MongoDB` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/MongoDB/research_task]] |
| `NuScale Power` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/NuScale Power/next_questions]] |
| `NuScale Power` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/NuScale Power/research_task]] |
| `Nvidia` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Nvidia/next_questions]] |
| `Nvidia` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Nvidia/research_task]] |
| `Oracle` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Oracle/next_questions]] |
| `Oracle` | `state_next_signals` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Oracle/next_signals]] |
| `Oracle` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Oracle/research_task]] |
| `PDD` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/PDD/next_questions]] |
| `PDD` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/PDD/research_task]] |
| `Palantir` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Palantir/next_questions]] |
| `Palantir` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Palantir/research_task]] |
| `Pop Mart` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Pop Mart/next_questions]] |
| `Pop Mart` | `state_next_signals` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Pop Mart/next_signals]] |
| `Pop Mart` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Pop Mart/research_task]] |
| `Rocket Lab` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Rocket Lab/next_questions]] |
| `Rocket Lab` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Rocket Lab/research_task]] |
| `Salesforce` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Salesforce/next_questions]] |
| `Salesforce` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Salesforce/research_task]] |
| `ServiceNow` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/ServiceNow/next_questions]] |
| `ServiceNow` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/ServiceNow/research_task]] |
| `TQQQ` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/TQQQ/next_questions]] |
| `TQQQ` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/TQQQ/research_task]] |
| `Tempus AI` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Tempus AI/next_questions]] |
| `Tempus AI` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Tempus AI/research_task]] |
| `Tencent` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Tencent/next_questions]] |
| `Tencent` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Tencent/research_task]] |
| `Tesla` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Tesla/next_questions]] |
| `Tesla` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Tesla/research_task]] |
| `Vistra` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Vistra/next_questions]] |
| `Vistra` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Vistra/research_task]] |
| `Xiaomi` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Xiaomi/next_questions]] |
| `Xiaomi` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/Xiaomi/research_task]] |
| `亨通光电` | `state_next_signals` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/亨通光电/next_signals]] |
| `分众传媒` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/分众传媒/next_questions]] |
| `分众传媒` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/分众传媒/research_task]] |
| `天华新能` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/天华新能/next_questions]] |
| `天华新能` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/天华新能/research_task]] |
| `广合科技` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/广合科技/next_questions]] |
| `广合科技` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/广合科技/research_task]] |
| `沪电股份` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/沪电股份/next_questions]] |
| `沪电股份` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/沪电股份/research_task]] |
| `深南电路` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/深南电路/next_questions]] |
| `深南电路` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/深南电路/research_task]] |
| `湖南裕能` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/湖南裕能/next_questions]] |
| `湖南裕能` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/湖南裕能/research_task]] |
| `湖南裕能` | `state_next_signals` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/湖南裕能/天赐材料/next_signals]] |
| `生益电子` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/生益电子/next_questions]] |
| `生益电子` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/生益电子/research_task]] |
| `紫金矿业` | `state_next_signals` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/紫金矿业/next_signals]] |
| `胜宏科技` | `state_next_questions` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/胜宏科技/next_questions]] |
| `胜宏科技` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/胜宏科技/research_task]] |
| `顺丰控股` | `state_next_signals` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/02_公司研究/顺丰控股/next_signals]] |
| `四方股份_601126` | `state_next_signals` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/标的研究/四方股份_601126/next_signals]] |
| `四方股份_601126` | `state_research_task` | [[兴趣领域/股票投资/03_STATE/HYPOTHESIS_QUEUE/MIRRORED_LEGACY_STATE/AI周期探索/标的研究/四方股份_601126/research_task]] |
