# agentic-investment-harness

> 人类保留最终权威、AI 只做研究与反证的投资操作系统。
>
> A human-authority-first investment agent harness that turns fragmented research into traceable evidence, expiring state, reviewable decisions, and safely evolving methods — without granting AI trading authority.

---

## 那一刻

你打开笔记库——几百篇 AI 报告、去年那份"强烈建议"还在原地。AI 现在又递来一份新的"强烈建议"。

你停下来，发现自己回答不了三个问题：

1. **旧的还作数吗？** 去年那份报告过期了没有？它的判断今天是否还成立？
2. **新的能信吗？** 这份新报告有没有独立证据？还是只是顺着最近的涨跌情绪在附和？
3. **如果按它做、亏了——能回溯吗？** 能不能找到具体是哪一步、哪个证据出了问题？

如果你在这一刻停下来，这个项目就是为你做的。

---

## 共同困境

当投资研究被 AI 接管后，四件事同时失控：

| 失控维度 | 症状 |
|---|---|
| **研究混乱** | 报告越攒越多，不知道哪份在指导当前决策 |
| **State 过期** | 去年的判断还在"有效"状态，但没有人复查 |
| **AI 越权** | AI 直接给出"建议加仓""目标价 XX"，没有人类确认 |
| **观点无法回溯** | 一个判断说"看好"，但不知道证据从哪来、什么时候成立的 |

核心问题不是"AI 写得对不对"，而是**你失去了对自己判断的追溯权和最终权威**。

---

## Before → After

```
材料、观点、旧报告和当前判断混在一起
                    ↓
Source → Knowledge → State → Decision → Case → Method Evolution
```

每条信息有根来源，每个判断有过期时间，每个写入经过审查，每个动作只用六档表达。

| 阶段 | 系统做什么 | 人类保留什么 |
|---|---|---|
| **Source** | 登记根来源、发布时间、数据口径 | 决定哪些来源值得登记 |
| **Knowledge** | 萃取散乱观点为可证伪的原子 belief | 确认哪些 belief 进入稳定层 |
| **State** | 给每个判断装上过期时间和复查日期 | 决定 State 是否升级或降级 |
| **Decision** | 四票 + 六档动作 + 独立 Reviewer | **唯一交易授权** |
| **Case** | 完成的交易进入案例库，失败的进入错误库 | 决定案例如何反哺方法 |
| **Method Evolution** | 从案例中提炼模式 → 提案 → 审查 → 合并 | 合并方法的最终裁决 |

---

## 它如何运作

### 最小加载

Agent 不全量加载所有文件。按问题分流，只读命中的路径：

```
AGENTS.md → PATHS.md → CONTENT_ROUTER.md → 命中的道/Skill → Current State → Evidence
```

### 四票：H_B / H_R / H_L / H_C

任何资本动作前，四张"门票"分开投：

| 票 | 判断什么 | 只靠什么更新 |
|---|---|---|
| **H_B** 经营胜率 | 这家公司能不能持续赚钱 | 经营证据（订单、利润、现金） |
| **H_R** 赔率 | 当前价格值不值 | 价格 vs 价值差距 |
| **H_L** 周期 | 现在是什么市场阶段 | 软探测器，只影响进入时点 |
| **H_C** 仓位 | 该投多少 | 总资本分母和风险预算 |

**铁律**：价格下跌只能改善赔率（H_R），不能提高经营胜率（H_B）。三张硬门票（经营 / 赔率 / 仓位）任一失败或未知，默认不增加风险。

### 独立 Reviewer

当写入触发硬条件时，独立只读 Reviewer（工具权限硬限制为 `Read` / `Grep` / `Glob`）必须先审查：

- `PASS` → 允许写入
- `BLOCK` → 退回补充
- `DISAGREE` → 保留双方判断，**不自动折中**

主 Agent 只能增加 Reviewer，不能取消。

### Validator（写入前机械校验）

写入前必须通过 `validate_investment_output.py`（42 项校验，fail-closed）：

- 写入路径属于 canonical sink
- 状态时间自洽（data_cutoff / expires_at / 当前日期）
- Reviewer `PASS` 且反方证据非空
- canonical 正文未被越权修改
- 修改前存在备份

---

## 项目不做什么

- **不荐股** — 不提供选股信号、目标价、仓位建议
- **不保证收益** — 没有"确定涨"的判断
- **不自动交易** — AI 没有交易授权、仓位修改权、自动成交权
- 公开的 `03_STATE/` 是作者的个人状态记录，**不是他人的买卖建议**

---

## 目录地图

```
00_HOME/           路径索引、任务分流
01_道/             宪法（Guardrail）、认知前台
02_术/             交易系统（四票、六档动作）、技能
03_STATE/          当前 thesis、预期、领域模型
04_CASE_GYM/       研究案例、错误库、交易日志
05_EVIDENCE_META/  来源、知识、证据层
90_AUTOMATION/     验证器、审查协议、测试
99_ARCHIVE/        历史 layout
归档/              旧分析报告与基础概念（兼容引用）
```

---

## 五分钟跑测试

```bash
git clone https://github.com/bor799/agentic-investment-harness.git
cd agentic-investment-harness

# Harness Validator 测试（169 项）
python3 -m unittest discover -s 90_AUTOMATION/TESTS -p 'test_*.py'

# 发布安全审计器
python3 90_AUTOMATION/PIPELINES/audit_publication.py .
```

全部绿色 = 写入校验和发布安全检查未被绕过。

---

## 怎么换成你自己的

1. **保留 `90_AUTOMATION/`** — 验证器和测试是通用骨架
2. **替换 `01_道/`** — 写你自己的宪法、认知、风险纪律
3. **改 `02_术/TRADING_SYSTEM/PARAMETERS.md`** — 设置你自己的总资本和风险预算
4. **清空 `03_STATE/` 和 `05_EVIDENCE_META/`** — 从你自己的研究开始积累
5. **读懂 `AGENTS.md` 再改** — 它定义 Agent 行为边界

---

## 自进化如何发生

```
Evidence / Case
    ↓
Method Proposal（对话中形成，不直接落盘）
    ↓
独立 Reviewer
    ↓
CI / Validator
    ↓
人类合并
```

AI 只能提方案，不能直接改道 / 术正文。每一次方法进化都经过：提案 → 反方审查 → 机械校验 → 人类合并。

---

## 许可证

| 层 | 许可证 | 范围 |
|---|---|---|
| **代码** | Apache-2.0 | `90_AUTOMATION/` 下的 `.py`、`.sh`、`.yml` |
| **内容** | CC BY 4.0 | 其他所有 markdown 和文档 |
| **第三方** | 见 `NOTICE` | 无明确再发布权的第三方内容只保留链接 |

详见 `LICENSE`、`LICENSE-CONTENT`、`NOTICE`。

---

## 贡献

AI Agent 的贡献走固定流程：

1. 在 `agent/*` 分支上工作
2. 创建 draft PR
3. PR 必须通过 CI + Validator + 发布审计
4. `main` 禁止强推和删除
5. 只有人类仓库所有者能合并

详见 `CONTRIBUTING.md`。

---

## 风险声明

本仓库是一个个人投资操作系统的**公开记录**，不是投资建议。

- `03_STATE/` 中的 thesis 和动作表达是作者的个人状态快照，**有过期时间**，不代表当前判断
- 任何人不应基于本仓库内容做出投资决策
- 投资有风险，决策需自行判断并承担后果
