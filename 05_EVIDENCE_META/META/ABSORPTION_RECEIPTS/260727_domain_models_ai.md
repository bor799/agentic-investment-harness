---
title: domain_models_ai_receipt_260727
date: 2026-07-27
updated: 2026-07-27
layer: META
primary_role: absorption_receipt
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: operational
data_cutoff: 2026-07-27
expires_at: 2026-10-25
source_paths:
  - 03_STATE/DOMAIN_MODELS/README.md
  - 03_STATE/DOMAIN_MODELS/AI/README.md
  - 03_STATE/DOMAIN_MODELS/AI/THESES/AI_PHYSICAL_INFRASTRUCTURE.md
  - 03_STATE/DOMAIN_MODELS/AI/THESES/ENTERPRISE_AI_CONTROL_PLANE.md
  - 03_STATE/DOMAIN_MODELS/AI/INVESTMENT_MAP.md
---

# DOMAIN_MODELS / AI 试点实施回执

## 吸收三行

- **新东西是什么：** 道与标的级 thesis 之间的中间层"领域世界模型"；产出研究优先级、候选公司、验证顺序、共同反方，不产出仓位/目标价/买入授权。
- **改变了什么：** 新增 `03_STATE/DOMAIN_MODELS/{README.md, AI/}` 目录骨架；Validator 扩展 D-1~D-8 八项独立编号校验；Reviewer 增加领域专属检查与 Post-Mortem 协议。
- **写到哪里：** 6 个新文件（5 个 DOMAIN_MODELS + 本回执），6 个修改文件（Validator / Tests / Reviewer / PATHS / AGENTS / PROVENANCE_SCHEMA）。

## 新增文件清单

| 文件 | 角色 |
|---|---|
| `03_STATE/DOMAIN_MODELS/README.md` | 领域模型顶层规则 + EVOLUTION_PROTOCOL |
| `03_STATE/DOMAIN_MODELS/AI/README.md` | AI 领域主页 + couplings + common_antagonist |
| `03_STATE/DOMAIN_MODELS/AI/THESES/AI_PHYSICAL_INFRASTRUCTURE.md` | 物理基础设施主题卡 |
| `03_STATE/DOMAIN_MODELS/AI/THESES/ENTERPRISE_AI_CONTROL_PLANE.md` | 控制平面主题卡 |
| `03_STATE/DOMAIN_MODELS/AI/INVESTMENT_MAP.md` | 10 个候选公司/ETF 映射 |
| `05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/260727_domain_models_ai.md` | 本回执 |

## 修改文件清单

| 文件 | 变更 |
|---|---|
| `90_AUTOMATION/PIPELINES/validate_investment_output.py` | +8 D-X 函数 +4 canonical sinks + 配套常量 |
| `90_AUTOMATION/TESTS/test_investment_output.py` | +8 TestCase（33 个新测试） |
| `90_AUTOMATION/PROMPTS/INVESTMENT_REVIEWER.md` | +§4.5 领域检查 + §7 Post-Mortem |
| `00_HOME/PATHS.md` | +State 子类「领域模型」4 条目 |
| `AGENTS.md` | §3 canonical sink 表 +4 行 |
| `05_EVIDENCE_META/META/PROVENANCE_SCHEMA.md` | +`research_authority` 字段 |

## D-X 编号登记表

| 编号 | 函数 | 检查 |
|---|---|---|
| D-1 | `d1_domain_path` | 路径形态合法 |
| D-2 | `d2_domain_registered` | 领域已登记（首轮只有 AI） |
| D-3 | `d3_thesis_status_enum` | thesis_status 枚举 |
| D-4 | `d4_time_triple` | 时间三件套 + 不超期（180/90/30） |
| D-5 | `d5_no_capital_action` | 无资本字段 |
| D-6 | `d6_murphy_ai_split` | 每段判断 Murphy/AI 三档标题齐全 |
| D-7 | `d7_canonical_sink_match` | 命中已登记 sink |
| D-8 | `d8_reviewer_pass` | last_reviewer 含 PASS + 时间戳 |

## 验收

| 检查 | 结果 |
|---|---|
| 独立只读 Reviewer | PASS |
| Validator 单元测试 | 105 / 105 PASS（V-1~V-19：72；D-1~D-8：33） |
| Python 编译 | PASS |
| D-X 反向测试（未登记领域） | D-2 FAIL ✓ |
| D-X 反向测试（target_price） | D-5 FAIL ✓ |
| D-X 反向测试（缺 AI extension） | D-6 FAIL ✓ |
| D-X 反向测试（last_reviewer=pending） | D-8 FAIL ✓ |
| 端到端合法 thesis 写入 D-1~D-8 | 8 / 8 PASS |
| 旧 canonical 文件 SHA-256 哈希校验 | 97 / 97 一致（01_道 / 02_术 / CURRENT/ / PORTFOLIO_LEDGER） |

## SHA-256 指纹

### 新建文件

```
1de86071078940b9048f5b2a3f1e85419e5fb10563eb4e65d4d4c5e989d37dd6  03_STATE/DOMAIN_MODELS/README.md
4458e273996de45ade6211af93027476a3834f0e8cb19cc28a975944d3648bc2  03_STATE/DOMAIN_MODELS/AI/README.md
950ed301d23b6350cff85e0a07decb454359489fdd9ae5c3fc5d721a88b14884  03_STATE/DOMAIN_MODELS/AI/THESES/AI_PHYSICAL_INFRASTRUCTURE.md
36cd16df92c3c90c6330eee3f46cebd40c6eee7084668e5cffc485cc146fa006  03_STATE/DOMAIN_MODELS/AI/THESES/ENTERPRISE_AI_CONTROL_PLANE.md
c97342417833535cb5d9ff67d4e72deea463a0f16558891033e48f6e87162ef2  03_STATE/DOMAIN_MODELS/AI/INVESTMENT_MAP.md
```

### 修改文件（写后）

```
5bd01e133b313d7b89a2f6695586532216fb02380c55abcd5dd31caca63029a5  90_AUTOMATION/PIPELINES/validate_investment_output.py
05d6414532e71b1fb7dc1f87c54a4a912145426bda0ca331097a6aafeb4964e2  90_AUTOMATION/TESTS/test_investment_output.py
8693885d92c62e66cccf2985f21dc8b77d867224aa04f5dcf84a0d650c93cfa3  90_AUTOMATION/PROMPTS/INVESTMENT_REVIEWER.md
11ac59a8a9914b556b73665c2b1c242d664addafc7715722265c6470a3258053  00_HOME/PATHS.md
bed0f1121ba9fa851e4a410e3f82b5ac99c75af4a1422563a75a575533583372  AGENTS.md
6d843b6437a7585f320fd7f8e02d2bc08d963ff72d1056985277947eba122e54  05_EVIDENCE_META/META/PROVENANCE_SCHEMA.md
```

## 边界

- 没有创建 AI 以外的领域目录（Crypto / 生物科技等留待后续）；
- 没有刷新 2026-07-27 之后的行情、资金或估值；
- 没有计算概率、EV、仓位或授权交易；
- 没有修改 01_道 / 02_术 / CURRENT/ / PORTFOLIO_LEDGER 正文；
- 没有批量迁移旧 AI 周期报告内容到 DOMAIN_MODELS（仅引用）；
- 没有实现 experience-curator sub-agent（下一阶段任务）。

## 回滚

本轮修改前副本位于：

` .harness_backup/20260727-215235-domain-models-ai/ `

包含 `00_HOME/`、`01_道/`、`02_术/`、`03_STATE/`、`04_CASE_GYM/`、`05_EVIDENCE_META/`、`90_AUTOMATION/`、`AGENTS.md`、`CLAUDE.md` 完整副本，可整体回滚到本轮施工前。
