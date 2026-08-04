---
title: automation_index
date: 2026-07-23
updated: 2026-07-24
layer: AUTOMATION
primary_role: automation_index
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: operational
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/分析报告/archive/260630财报季_经营验证与定时任务体系.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/CROSS_MARKET_V2_RUN_BOUNDARIES.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/MINDSPACE_SOURCE_MCP_SOP.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/README.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/refresh_targets_2026-05-24.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/source_health_2026-05-24.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/信息重整与趋势刷新计划_2026-05-24.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/0_总览/研究对象清单.md
---

# Automation

Prompts、脚本、测试和运行态统一在这里管理。自动化最多运行到 Philosophy Inbox，不能写 MINDSET/CONSTITUTION。

当前 `AI_BELIEF_LOOP` 是隔离候选编译器：默认 dry-run；stage 只创建
`RUNTIME/STAGING/` 与脱敏 `RUN_LOG/`。它不联网、不回源，也不写正式研究
知识或投资状态。

## 运行边界

自动化可以做三类事：

- **每日哨兵：**检查正式披露、公司 IR、交易所/监管公告、业绩预告、已发布财报和任务是否到期。
- **每周准备会：**滚动列出未来 30 天验证窗口、缺失基线和最值得补证据的标的。
- **月度复盘会：**汇总经营质量、瓶颈控制、利润池、竞争结构、估值赔率和下一月验证数字。

自动化不能做三类事：

- 不能自动写入 MINDSET / CONSTITUTION；
- 不能自动修改 `R`、仓位、参数、价格线或主账；
- 不能把“任务触发、新闻热度、AI 共识、财报超预期”直接改写成风险增加授权。

任何自动化输出若涉及投资动作，只能交给 [[02_术/TRADING_SYSTEM/01_RESEARCH_FLOW]]、[[02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION]] 和 [[02_术/TRADING_SYSTEM/03_FEEDBACK_LOOP]] 复核。

## 旧 AI 周期自动化边界

旧 AI 周期里的命令、队列、source health 和 refresh target 都是历史运行设计，不是当前可直接执行的命令清单。重新启用前必须先确认当前工具、路径、脚本、权限和 dry-run 结果。

可保留的自动化规则：

- 每轮先做只读基线：本地索引、watchlist、source health、refresh targets。
- 公司刷新先读本地四件套，再取一手来源；搜索摘要不能直接下结论。
- 核心证据必须回源，并写入证据日志。
- fallback 只能在主信源覆盖不足、超时或关键桶缺失时使用，且必须记录原因。
- 公司级刷新和主题级刷新分开；主题热度不能直接改公司四票。
- 失败、超时、工具不可用、证据不足都必须留下状态，而不是静默跳过。

重新启用旧跨市场 v2 队列时，必须满足：

```yaml
automation_run_boundary:
  mode: dry_run_first
  tool_whitelist: required
  write_whitelist: required
  run_token: unique_per_object
  claim_rule: host_claims_one_object_atomically
  model_write_scope: outcome_only
  host_validation:
    - run_token
    - object_id
    - source_fields
    - H_B_H_R_H_L_H_C
    - tool_evidence
    - file_paths
  failed_after_retries_counts_as_complete: false
  summary_allowed_when_failed_objects_exist: false
```

废止或降权：

- 旧命令示例不等于当前指令。
- 旧工具可用性只说明 2026-05-24 附近的环境，不说明现在可用。
- 旧评分、固定分数、AI 共识、区间中点、未校准概率不能进入 EV 或仓位。
- 自动化不得修改主账、交易权限、仓位参数、ledger 或券商事实。
- Staging 必须标记 `unverified_by_runner`；正式 Source / Moment 晋升回到完整 Harness 门禁。
- 期权自动化只能做资料准备；字段不全时不得给卖 Put、roll、杠杆或仓位建议。

## 入口

| 入口 | 用途 |
|---|---|
| [[90_AUTOMATION/PROMPTS/AI_CYCLE_PROMPTS_INDEX]] | 旧 AI 周期 prompt / command |
| [[90_AUTOMATION/PROMPTS/AUTOMATION_REVIEW_QUEUE_INDEX]] | 待复核旧 prompt、旧命令和历史自动化设计 |
| [[90_AUTOMATION/PROMPTS/CURRENT_CANDIDATES_INDEX]] | 当前 Claude 自动化候选副本 |
| [[90_AUTOMATION/PIPELINES/AI_CYCLE_PIPELINES_INDEX]] | 旧脚本与测试 |
| [[90_AUTOMATION/RUNTIME/AI_CYCLE_RUNTIME_INDEX]] | 旧队列、日志和运行态 |
| [[90_AUTOMATION/PIPELINES/phase2_restructure_bootstrap.py]] | 第二阶段骨架生成脚本 |
| [[90_AUTOMATION/PIPELINES/phase2_materialize_indexes.py]] | 第二阶段索引物化脚本 |
| [[90_AUTOMATION/PIPELINES/phase2_materialize_legacy_layers.py]] | 第二阶段旧报告/基础概念/Case 分层脚本 |
| [[90_AUTOMATION/PIPELINES/phase2_materialize_evidence_batch.py]] | 第三批 Evidence 镜像脚本 |
| [[90_AUTOMATION/PIPELINES/phase2_materialize_governance_automation_batch.py]] | 第四批治理/自动化镜像脚本 |
| [[90_AUTOMATION/PROMPTS/AI_BELIEF_LOOP]] | AI 原子 belief 候选输入契约 |
| [[90_AUTOMATION/PIPELINES/ai_belief_loop.py]] | dry-run / 隔离 stage runner |
| [[90_AUTOMATION/RUNTIME/STAGING/README]] | 未核验候选隔离区 |
| [[90_AUTOMATION/RUN_LOG/README]] | 脱敏运行日志 |
