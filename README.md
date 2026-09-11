# 投资 Agent Harness

输入公司、行业、观点或材料，先回答：**赚什么钱、证据是否正在兑现、什么情况说明错了。**
模型负责研究和反证，Murphy 保留投资方法确认、风险预算与最终资本决策权。

## 直接开始

在仓库中使用 Codex 或 Claude Code，从 [AGENTS.md](AGENTS.md) 进入。无需复制长提示词，也无需为不同模型维护一套副本。

| 输入示例 | 首屏得到什么 |
|---|---|
| “研究这家公司，看到半年后” | 付款人 → 订单 → 利润 → 每股现金流；窗口内验证事件与最大反证 |
| “这个行业本周有什么值得关注” | 相对原预期的新证据、验证日程、尚未成立的传导 |
| “现在这个价格意味着什么” | 带时间的价格与隐含预期、缺失的赔率或执行条件 |
| “比较这几家公司” | 简短比较与最值得继续核验的少数对象，经独立审查；不逐家堆长报告 |
| “读这份材料” | 新增事实、推断、改变了哪个判断、下一验证；未指定归档位置时先在对话回答 |

半年、本周、当下共用一条赚钱逻辑，分别看利润兑现、事件验证、价格与执行条件。
历史研究需刷新才可回答“现在”；没有足够证据时明确保留未知。

默认七项短答：一句话判断、赚什么钱、是否正在发生、关键支持、最大反方、六档动作、下一项验证。
概念解释与文件定位不强套投资模板。内部检查字段不逐项搬到用户面前。

## 内容放在哪里

| 路径 | 职责 |
|---|---|
| [00_HOME](00_HOME/PATHS.md) | 路径和内容路由 |
| [01_道](01_道/CONSTITUTION.md) | Murphy 的原则与边界 |
| [02_术](02_术/SKILLS/README.md) | 按任务选择的研究方法与决策合同 |
| [Knowledge](05_EVIDENCE_META/KNOWLEDGE/DOMAINS/README.md) | 稳定但可被证伪的领域、公司模型 |
| [Source](05_EVIDENCE_META/SOURCES/README.md) | 原文、事实和来源 |
| [Current](03_STATE/HYPOTHESIS_QUEUE/README.md) | 带资料截止日、到期日的当前判断 |
| [Case Gym](04_CASE_GYM/RESEARCH_CASES/README.md) | 事前判断、结果、失败与复盘 |
| [运行提示词](90_AUTOMATION/PROMPTS/README.md) | 主研究、独立审查、隔离候选 runner |

按 [AGENTS §2](AGENTS.md#2-加载顺序固定) 加载必要内容，不扫描全库。一个任务中未变化的规则不重复读取。
旧报告与历史索引继续可检索，不自动成为当前判断，也不在每次研究时全量载入。

## 研究与资本分开

- 公司经营、当前赔率、周期和仓位分别判断；周期是软探测器。
- 价格下降不能证明公司变好；订单、ARR、RPO 不等于现金流或普通股回报。
- 没有校准依据就不编概率、目标价与收益率；AI 共识不算独立证据。
- 正式写入和资本动作按 [AGENTS §4](AGENTS.md#4-reviewer-与-validator-调用条件) 经独立 Reviewer 与 Validator。
- AI 不下单，不修改仓位或资本参数。工程改动的合并按用户授权执行，不能据此授权投资动作。

证据 → 判断 → 反证审查 → 人的决策 → 结算案例，是反馈链；候选 runner 只做隔离暂存。

## 本地与 GitHub 怎么协作

本地保存研究证据与工作状态。GitHub issue 保存待解决问题和已授权公开的交易日志；PR 保存经过检查的工程变更。
公开仓库只同步明确选择并经审计的文件，不整库上传本地新增材料。

| Issue | 处理原则 |
|---|---|
| [#1 JNK → SPX/SPY 监控器](https://github.com/bor799/agentic-investment-harness/issues/1) | 历史评论报告信号未优于对照；先验证增量，不以该规则建设实时监控器。详见 [路线图](ROADMAP.md) |
| [#2 META / SPY / SLV / 161226](https://github.com/bor799/agentic-investment-harness/issues/2) | 交易日志；券商事实、退出结果与复盘补齐才结算 |
| [#3 有色集中调仓](https://github.com/bor799/agentic-investment-harness/issues/3) | 交易日志；调仓计划、成交和剩余暴露分别核对 |

研究框架已存在，但“更快”“更准”与投资超额收益仍须分别验证，不能用测试通过代替。
历史长说明和提案可从 [精简前版本](https://github.com/bor799/agentic-investment-harness/tree/a4af366e2ec9e78441f28f3f571324e5df7c4c70) 查回。

## 验证

只用 Python 标准库：

```bash
python3 -m unittest discover -s 90_AUTOMATION/TESTS -p 'test_*.py' -v
python3 90_AUTOMATION/PIPELINES/audit_publication.py .
```

测试检查路径、权限、时间、来源与契约；publication audit 检查选定发布内容。
它们不能证明提示词遵循率、市场预测能力或收益。改动加载/输出时，还需用相同问题比较输出质量、读取量与耗时。

更多：[ROADMAP](ROADMAP.md) · [贡献规则](CONTRIBUTING.md) · [安全](SECURITY.md) · [代码许可](LICENSE) · [内容许可](LICENSE-CONTENT)
