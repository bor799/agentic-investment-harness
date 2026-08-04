---
title: investment_harness_receipt_260725
date: 2026-07-25
updated: 2026-07-25
layer: META
primary_role: absorption_receipt
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: operational
source_paths:
  - 90_AUTOMATION/RUN_LOG/260725_harness_dry_run.md
  - 90_AUTOMATION/DESIGN_NOTES/LEGACY_AUTOMATION_INVENTORY.md
data_cutoff: 2026-07-25
expires_at: 2026-10-25
---

# Investment Harness 施工交付回执（T0–T7）

本轮完成 Investment Harness 最小施工。本回执记录新建/修改文件、SHA-256、试运行结果、测试结果、Reviewer 验证与未决事项。

---

## 1. 新建文件（11）

| 路径 | 用途 | SHA-256 |
|---|---|---|
| `.harness_backup/README.md` | 备份目录说明 | `11475eb8a1829f7c1bc782c9ce8f65e2ede010caf23f3ae8c141765f0e0ac72a` |
| `CLAUDE.md` | Claude Code 入口（首行 `@AGENTS.md`） | `aeab6cf668c9482259b7caa874a7a6ed6492b4bf7ad0d44fc88cd1e52e079931` |
| `00_HOME/PATHS.md` | 仓库相对路径索引 | `4346629dc6b7c6a5b1669a88abd868b364cb10486e77e167cabc8fbf5c43dc40` |
| `90_AUTOMATION/DESIGN_NOTES/LEGACY_AUTOMATION_INVENTORY.md` | 失效入口盘点 | `4872cd922a29a7583d04e5dee42b2975ebc7ab920b3f5cf1068b7f12b6d27118` |
| `90_AUTOMATION/ARCHIVE/legacy_claude_config/README.md` | 归档目录说明 | `848267f054237bafbc37dd53ab353b65ac51450ad6bbe0d42ff73fa10454e111` |
| `90_AUTOMATION/PROMPTS/INVESTMENT_HARNESS.md` | Harness 运行契约 | `43096c29215563171c712c13b21038883b219fe185b017bd794b1fa6d7e8fa2b` |
| `90_AUTOMATION/PROMPTS/INVESTMENT_REVIEWER.md` | Reviewer 协议 | `a2aaa38aeab4767a83b36697d0c1fff4ff8679f3a805f321bde75d19e8162e2c` |
| `.claude/agents/investment-reviewer.md` | Claude 只读 Reviewer 子 agent | `3d5ca96dfe1a92ea7dc58646cd9914648abd250cefaa7ea7ce72c2ff426615b4` |
| `90_AUTOMATION/RUN_LOG/260725_harness_dry_run.md` | 四类试运行记录 | `5bc6bf23721b112450503a31ce245dd4db3caf44d59a406c750d58d3bd35fc0d` |
| `90_AUTOMATION/PIPELINES/validate_investment_output.py` | 机械校验器（V-1~V-15） | `29d463fca750d1fbc161e614bf88ab0204576eb8430d6fecc8676622813b8a1c` |
| `90_AUTOMATION/TESTS/test_investment_output.py` | 单元测试（52 用例） | `3cebf59aadc9c6e20200070131436ab555f498f4495d65304fb702933f56808e` |

新建空目录：

- `03_STATE/HYPOTHESIS_QUEUE/CURRENT/`（T6 创建，等待按需创建状态卡）
- `90_AUTOMATION/ARCHIVE/legacy_claude_config/agents/` 与 `commands/`（保留归档结构）

---

## 2. 修改文件（4）

| 路径 | 修改前 SHA-256（备份） | 修改后 SHA-256 |
|---|---|---|
| `AGENTS.md` | `fa8ab7d4eee45ad175bda60fdedc5d7b3f07fd2a8cbc15e2593baa039faa8487` | `932712043791d133c5f8bdb4b7822cd8ec9ebf328fc6f32b8c6aa2d231cce930` |
| `00_HOME/HOME.md` | `2d3f35368fa6d7dea6950c68821033faca5485b63b54314ea2137db9390a1b68` | `47cc027da6b3c421dcd7c56b020912af8c1af2ef9539eef5316e4a75d264c607` |
| `00_HOME/CONTENT_ROUTER.md` | `e65978ed0fde1ebe2a0599cfc2b74c014b455335b54e2b20ad28aa6a69da19b9` | `9564c56d479a7490f202f36812a8bf0160e9c7558bbce6ba3832ebe7d943e2cd` |
| `03_STATE/HYPOTHESIS_QUEUE/README.md` | `59654fd4e4e548481989b74f58d9c302ff5988cfc98d5fa2464caa864581ed32` | `432bf6cbefb158d2cc50c0852043fefb86b8ed8b14e937b8f2d6bd4cb0306701` |

修改要点：

- `AGENTS.md`：重写为 Harness 公共入口；加载顺序、canonical sink、Reviewer/Validator 触发条件、历史标记失效声明、外部文章前置路由、行为纠偏权威指向。
- `00_HOME/HOME.md`：Skills 入口改为 `02_术/SKILLS/README.md`；新增 Investment Harness 入口；source_paths 改为 LEGACY_AUTOMATION_INVENTORY。
- `00_HOME/CONTENT_ROUTER.md`：METHOD_UPDATE 改为"对话 proposal"；新增 canonical sink 表与不允许项；source_paths 改为 LEGACY_AUTOMATION_INVENTORY。
- `03_STATE/HYPOTHESIS_QUEUE/README.md`：新增 §CURRENT 状态卡规则（T6）。

---

## 3. 备份位置

```
.harness_backup/20260725-190113/.claude/{agents,commands}/  → T0 归档前的旧 .claude/ 三份
.harness_backup/20260725-190233/{AGENTS.md, HOME.md, CONTENT_ROUTER.md}  → T1 修改前
.harness_backup/20260725-224656/03_STATE/HYPOTHESIS_QUEUE/README.md  → T6 修改前
```

`.harness_backup/README.md` 已声明：本目录不用于运行时加载；不做 Git 初始化；只保留仓库相对路径副本。

---

## 4. 已归档（移动，不修改）

`.claude/agents/ai-cycle-cross-market-v2.md`、`.claude/commands/ai-cycle-cross-market-v2.md`、`.claude/commands/ai-research-loop-pro.md` 已移动到 `90_AUTOMATION/ARCHIVE/legacy_claude_config/`。原相对路径与 SHA 已在 `90_AUTOMATION/ARCHIVE/legacy_claude_config/README.md` 与 `.harness_backup/20260725-190113/` 双重保留。

---

## 5. 四次试运行结果

详细记录见 `90_AUTOMATION/RUN_LOG/260725_harness_dry_run.md`。

| Dry Run | input_type | 标的 | state_status | review_required | write_intent | 文件改动 |
|---|---|---|---|---|---|---|
| 1 | TARGET | Coinbase | legacy_only | true（含"建仓"） | chat_only | 0 |
| 2 | BATCH | COIN/NET/DDOG | legacy_only | true（批量优先级） | chat_only | 0 |
| 3 | CONTENT | 仓库内流动性框架文章 | legacy_only | true（拟 METHOD_UPDATE） | chat_only | 0 |
| 4 | CAPITAL | Alibaba 建仓 5% | legacy_only | true（资本动作） | chat_only | 0 |

四次均：

- 输出 ≤ 13 行的 concise 回答；
- 自动识别正确 `input_type` 与 `lane`；
- 未启动过度研究；
- 未引用 legacy 旧报告作为 current 判断；
- 未出现"维持甚至加仓""谨慎乐观"等模糊动作；
- 未写入任何正式文件。

dry-run 共暴露 5 条偏差，均已写入新 Validator 检查项 V-11~V-15：

| 偏差 | Validator |
|---|---|
| chat_only + CAPITAL 下 Reviewer `allowed_write_route` 处理 | V-11 |
| BATCH 超过 5 个标的时的截断规则 | V-12 |
| BATCH 全 legacy_only/missing 时的极简回复规则 | V-13 |
| 仓库内 legacy 报告作为内容输入的来源分类 | V-14 |
| 仓位参数识别 + BEHAVIOR_REVIEW 自动触发 | V-15 |

未覆盖的真实样本：

- **FILING** 单独类型（财报原文 / 招股书原文 / 监管公告原文）：本轮以 CONTENT 替代，仓库内现成 FILING 样本不足。如 Murphy 提供具体财报链接，可补一次 FILING dry-run。
- **`write_intent: explicit_persist` 全流程**：本轮全程 chat_only，Validator 写入门禁未走完闭环。建议下一轮由 Murphy 主动触发一次 explicit_persist 写入（例如明确要求"写入 X 的 current thesis"）。

---

## 6. Validator 测试结果

```
$ python3 -m unittest 90_AUTOMATION.TESTS.test_investment_output
----------------------------------------------------------------------
Ran 52 tests in 0.062s

OK
```

覆盖：

- V-1 ~ V-15 各项至少一通一败；
- 历史报告中"维持甚至加仓""降低权重""谨慎乐观""逢低吸纳""波段操作"作为 V-4 负例；
- End-to-end：clean chat_only 全通；constitution 写入被 V-7 拒绝。

Validator 特性已生效：

- fail-closed（任何 FAIL → overall FAIL，exit 1）；
- 纯标准库（json/os/re/sys/datetime/pathlib/tempfile/subprocess/unittest）；
- 不联网；
- 不判断投资结论；
- `_strip_dot_slash` 正确处理 `.harness_backup/` 等点开头相对路径（修复了一个 `lstrip("./")` 误剥前导点的 bug）。

---

## 7. Claude Reviewer 权限验证

`.claude/agents/investment-reviewer.md` frontmatter：

```yaml
tools: ["Read", "Grep", "Glob"]
```

明确未授权：`Edit`、`Write`、`NotebookEdit`、`Bash`、`WebSearch`、`WebFetch`。

Reviewer 文档正文重申：

> Your tools are hard-restricted to: Read / Grep / Glob. You **must not** request or use Edit, Write, NotebookEdit, or any web/shell tool. This restriction is enforced by the harness; do not attempt to bypass it.

权限验证：通过。

---

## 8. Codex Reviewer 模式

Codex 当前版本未在本仓库内提供稳定的 native 自定义 subagent 配置入口。本轮采用 `agent_mode: injected`：

- Codex 读取 `AGENTS.md §4.1`，识别 Reviewer 硬触发；
- Codex 进入只读模式（禁用 `apply_patch` / `write_file` 等写入工具）；
- 注入 `90_AUTOMATION/PROMPTS/INVESTMENT_REVIEWER.md` 作为审查 Prompt；
- 输出 `review_result` YAML，标注 `agent_mode: injected`；
- 不允许静默退回主 Agent 自审。

如未来 Codex 升级支持 stable native subagent，可切换到 `agent_mode: native`，本回执与 Reviewer Prompt 不需修改。

---

## 9. 未处理的冲突

| ID | 冲突 | 当前处置 |
|---|---|---|
| C1 | `分析报告/archive/` 作为 `source_paths` 大量出现在旧文件 frontmatter，但 `分析报告/` 旧位置已迁移到 `归档/分析报告/`，新位置由 `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/` 镜像吸收 | 本轮只在三个修改文件（HOME/CONTENT_ROUTER/HYPOTHESIS README）中改为新引用；其他文件的 `source_paths: 分析报告/archive/...` 字段未批量改动，留给后续 neat-freak |
| C2 | 旧 `分析报告/archive/260719组合_行为纠偏与资本纪律操作系统.md` 在 `AGENTS.md §8` 中作为 P1 reference，但其 canonical 权威已被 `02_术/TRADING_SYSTEM/` 接管 | 已在 `AGENTS.md §8` 显式声明"位于 `归档/`，作 P1 reference，不再做权威授权" |
| C3 | `01_道/PHILOSOPHY_INBOX/` 已存在候选命题，但本轮 Harness 未定义从 REVIEW 内容到 PHILOSOPHY_INBOX 候选的写入模板 | Reviewer 可声明 `incremental_value: NEW_PERSPECTIVE` + `allowed_write_route: 01_道/PHILOSOPHY_INBOX/`；具体候选文件 schema 留给 Murphy 下次明确要求时形成 proposal |

---

## 10. 明确未建设的内容

按施工单"本轮不建设"清单：

- 新的投资哲学；
- 新的 Evidence Schema；
- 数据库；
- Portfolio YAML；
- CLI；
- nightly loop；
- 定时队列；
- 全量历史迁移；
- 独立 Researcher Agent；
- 多 Reviewer 投委会；
- 全盲审；
- Git 初始化；
- 自动交易能力。

也未建设：

- Codex 端 native subagent 配置文件（Codex 当前版本不支持稳定入口）；
- Validator 的 cron / pre-commit hook；
- `PROVENANCE_SCHEMA` 与 `CLAIM_LEDGER` 实体文件（仅在 PATHS.md 声明，未在本轮创建）；
- FILING 类型 dry-run（仓库缺真实样本）；
- `explicit_persist` 全流程闭环 dry-run（本轮全程 chat_only）。

---

## 11. 总验收对照

| # | 验收项 | 状态 | 证据 |
|---|---|---|---|
| 1 | Codex 只读 `AGENTS.md` 即可运行完整 Harness | ✅ | `AGENTS.md` 已含加载顺序、canonical sink、Reviewer/Validator 条件 |
| 2 | Claude Code 通过 `CLAUDE.md` 导入同一套规则，无规则复制 | ✅ | `CLAUDE.md` 首行 `@AGENTS.md`，其余仅 Claude 专属说明 |
| 3 | 用户输入股票代码/清单/外部内容/资本问题无需手工指定流程 | ✅ | INVESTMENT_HARNESS.md §1 输入识别 + §2 任务分诊 |
| 4 | 第一次回答先给简洁结论 | ✅ | Dry-run 1–4 均 ≤ 13 行 |
| 5 | 用户要求深入时可继续展开而不重新启动 | ✅ | INVESTMENT_HARNESS.md §9 deep 模式 |
| 6 | 内部 reviewed 与外部 concise 可同时成立 | ✅ | Dry-run 1、4（reviewed + concise） |
| 7 | legacy 报告不会被当作 current State | ✅ | V-2 + Dry-run 全部 state_status=legacy_only |
| 8 | 资本动作和正式写入必定触发 Reviewer | ✅ | V-3 + INVESTMENT_HARNESS.md §4.1 |
| 9 | Reviewer 的只读性由权限层保证 | ✅ | `.claude/agents/investment-reviewer.md` tools: [Read/Grep/Glob] |
| 10 | BLOCK 或 DISAGREE 不会被主 Agent 自动变成 PASS | ✅ | V-6 + V-10 |
| 11 | validator 能拒绝模糊动作、越权写入和过期状态 | ✅ | V-4 / V-7 / V-2 单测均通过 |
| 12 | validator 每次运行都会暴露到期与待复查状态 | ✅ | V-9 + V-2 |
| 13 | 所有既有文件修改前均有备份 | ✅ | `.harness_backup/` 三时间戳 |
| 14 | 全部 Python 测试通过 | ✅ | 52/52 OK |
| 15 | 实际文件变化与交付回执完全一致 | ✅ | §1 / §2 / §3 SHA-256 列表 |
| 16 | `01_道/`、canonical Skills 和 Portfolio 持仓数据零改动 | ✅ | 本轮无对这些路径的 write_target；V-7 / V-1 单测验证拒绝路径 |

---

## 12. 给 Murphy 的提案

| 提案 | 触发原因 | 建议 |
|---|---|---|
| P-1 | `分析报告/archive/` 旧 source_paths 引用广泛 | 下次 neat-freak 阶段统一替换为 `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/` 路径，或在 `分析报告/` 下保留软重定向 README |
| P-2 | FILING dry-run 缺真实样本 | Murphy 提供一份具体财报链接（如 10-Q、港交所公告），补一次 FILING dry-run 与 V-5 字段细化 |
| P-3 | `explicit_persist` 闭环未跑 | Murphy 在下一轮主动触发一次"写入 X current thesis"指令，验证 Reviewer + Validator + 备份 + 写入完整链路 |
| P-4 | PHILOSOPHY_INBOX 候选 schema 未定义 | 当 REVIEW 内容标 `NEW_PERSPECTIVE` 时，候选文件的 YAML frontmatter 与正文 schema 需要单独形成 proposal |
| P-5 | Codex native subagent 配置 | 等 Codex 稳定支持后，在 Codex 全局配置（`~/AGENTS.md` 或 `~/.codex/`）中建立独立 Reviewer subagent，将 `agent_mode` 切换为 `native` |

---

## 13. 收尾声明

本轮 Harness 最小施工已闭合 T0–T7。Harness 不代替 Murphy 形成投资判断；它只保证：

- 默认不写入；
- 写入前必经 Reviewer 与 Validator；
- canonical sink 之外不写入；
- legacy 旧报告不冒充 current；
- 模糊动作被拒绝；
- State 会过期；
- 一切写入可回滚（备份 + SHA-256）。

如需扩展（新增 Skill、新增 Validator 检查、新增 State 字段、新增 Evidence 类型），按 `AGENTS.md §11` 引用的 canonical 路径追加；不绕过 Reviewer、不复制道/术正文、不在 canonical sink 之外写入。
