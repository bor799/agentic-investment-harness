# Legacy Automation Inventory (T0 盘点)

Investment Harness T0 阶段对 `90_AUTOMATION/` 与既有自动化入口的盘点结果。

本轮原则：
- 不调用；
- 不恢复；
- 不迁移；
- 不重写。

## 1. 已归档（移动到 `90_AUTOMATION/ARCHIVE/legacy_claude_config/`）

| 原路径 | frontmatter 状态 | 归档原因 |
|---|---|---|
| `.claude/agents/ai-cycle-cross-market-v2.md` | `legacy_claude_automation` | 服务旧 AI 周期 v2，非 Harness 职责，且 PreToolUse hook 引用旧目录脚本 |
| `.claude/commands/ai-cycle-cross-market-v2.md` | `legacy_claude_automation` | 同上 |
| `.claude/commands/ai-research-loop-pro.md` | `superseded` | 文件自述"历史命令，不再授权当前判断" |

## 2. 已失效但未迁移的入口（保留原位，T0 不动）

### 2.1 旧 AI 周期 prompt / command 队列

位置：`90_AUTOMATION/PROMPTS/REVIEW_QUEUE/`、`90_AUTOMATION/PROMPTS/CURRENT_CANDIDATES/`

子目录：

- `AI周期探索/`、`codeex 版本/`、`交易宪法/`、`基础概念/`、`ploymarket/`
- `CURRENT_CANDIDATES/.claude/agents|commands/`（旧 `.claude/` 副本）

失效原因：

- 引用的 `LOOP_PROMPT_PRO.md`、`cross_market_queue_v2.json`、`v2_write_guard.py` 等位于根目录 `AI周期探索/`，已不在新分层结构内；
- 评分、固定分数、AI 共识、未校准概率进入 EV 的规则已被 `02_术/TRADING_SYSTEM/00_DECISION_CONTRACT.md` 与 `02_术/SKILLS/BEHAVIOR_REVIEW.md` 废止；
- 工具可用性仅说明 2026-05-24 附近环境。

### 2.2 旧 phase2 迁移脚本

位置：`90_AUTOMATION/PIPELINES/phase2_*.py`（共 13 个）

包括：

```
phase2_build_migration_backlog.py
phase2_materialize_analysis_state_batch.py
phase2_materialize_evidence_batch.py
phase2_materialize_governance_automation_batch.py
phase2_materialize_indexes.py
phase2_materialize_legacy_layers.py
phase2_materialize_method_source_batch.py
phase2_materialize_physical_batches.py
phase2_materialize_special_legacy_batch.py
phase2_materialize_state_scorecard_batch.py
phase2_normalize_history_copies.py
phase2_normalize_legacy_frontmatter.py
phase2_patch_legacy_frontmatter.py
phase2_restructure_bootstrap.py
```

失效原因：用于第二阶段骨架物化，已执行完毕。再次运行可能覆盖当前结构。T0 阶段不调用、不修改、不删除。

### 2.3 旧运行态

位置：`90_AUTOMATION/RUNTIME/`

```
AI_CYCLE_RUNTIME_INDEX.md
PLOYMARKET_LEGACY_AUTOMATION_INDEX.md
README.md
```

失效原因：旧 nightly loop、跨市场队列、Polymarket 自动化的运行日志。Harness 不消费这些状态。

### 2.4 旧 PIPELINES 索引

位置：`90_AUTOMATION/PIPELINES/AI_CYCLE_PIPELINES_INDEX.md`

失效原因：旧 AI 周期 pipeline 入口，与 Harness validator 路径无重叠。

## 3. 待清洗的潜在入口（无法确认，留待 Murphy 决策）

以下文件不在 T0 处置范围，仅登记：

- 根目录 `AI周期探索/`（位于仓库根，被多处 legacy 入口引用，但已被 `02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/AI周期探索/` 镜像吸收）。
- 根目录 `归档/`（旧分析报告与基础概念仓库，已被 `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/` 与 `02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/` 镜像吸收）。
- `99_ARCHIVE/LEGACY_LAYOUT/`（旧 layout 历史，未被新分层引用）。

T0 不调整以上目录，仅记录。

## 4. 设计论证归档说明

本目录（`90_AUTOMATION/DESIGN_NOTES/`）只存放 Harness 设计论证，不会被 `AGENTS.md`、`CLAUDE.md` 或运行时 Prompt 引用。

后续所有 Harness 架构对比、方案选择、被否决的设计均写入此目录，不混入 PROMPTS 或 PIPELINES。
