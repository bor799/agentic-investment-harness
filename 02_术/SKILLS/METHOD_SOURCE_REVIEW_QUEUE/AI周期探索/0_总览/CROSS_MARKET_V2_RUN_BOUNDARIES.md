---
title: "CROSS_MARKET_V2_RUN_BOUNDARIES"
date: 2026-07-24
updated: 2026-07-24
layer: METHOD
primary_role: legacy_ai_cycle_method
status: superseded
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
legacy_metadata_added: true
legacy_path: "AI周期探索/0_总览/CROSS_MARKET_V2_RUN_BOUNDARIES.md"
migration_target: "02_术/SKILLS + 90_AUTOMATION"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# 跨市场证据与赔率循环 v2：运行边界

> [!important] 当前状态：仅生成，尚未启动
> 截至 2026-07-21，本 v2 只完成文件、队列、Agent、命令和验证工具。本次没有调用 Claude，没有产生 API 费用，也没有生成任何对象刷新报告。

## 手动入口

在股票投资库根目录执行：

```bash
# 只检查计划；不调用 Claude、不写文件
AI周期探索/0_总览/run_nightly_research_loop.sh --dry-run

# 按默认 10 小时、22 轮、35 美元总上限运行
AI周期探索/0_总览/run_nightly_research_loop.sh

# 显式绕过 Claude 权限确认；工具和写入边界不会扩大
AI周期探索/0_总览/run_nightly_research_loop.sh --bypass-permissions
```

接口：

```text
run_nightly_research_loop.sh [--dry-run] [--hours 10] [--max-iterations 22] [--budget-usd 35] [--bypass-permissions]
```

默认模型为 Claude Sonnet，推理强度为 `high`，运行方式为非交互 `--print`。总预算按每轮 Claude 返回的实际费用累加；若调用后无法确认费用，循环保守停止，避免未知超支。

## 工具硬边界

Claude 只获得：

```text
Read, Glob, Grep, Edit, Write, WebSearch, WebFetch
```

明确不提供：

- Bash 或任意 shell；
- 删除、安装、包管理、系统修改；
- Task/子 Agent、消息发送、邮件、日历或外部写入；
- 券商、交易、下单、撤单、持仓或订单修改；
- MCP 写工具及其他未列出的工具。

`--bypass-permissions` 只把 Claude Code 的权限模式改为 `bypassPermissions`，不会添加工具、目录或动作权限。

项目 Agent 还挂载 `PreToolUse` 写路径守卫：每次 `Edit/Write` 执行前读取持久化队列，只允许当前唯一 `running` 对象的当日刷新、`evidence_log.md`、`next_signals.md` 和 outcome；汇总轮只允许最终报告和 outcome。守卫解析失败、没有唯一 claim 或路径越界时一律退出码 2 拒绝，因此在 `acceptEdits` 和显式 bypass 下都生效。

## 写入白名单

对象轮只允许：

1. 当前 claim 的 `research_dir`；
2. `AI周期探索/0_总览/v2_last_outcome.json`。

宿主脚本另可原子更新：

1. `AI周期探索/0_总览/cross_market_queue_v2.json`；
2. `AI周期探索/0_总览/v2_run_log.jsonl`。

项目 slash command 的手动单轮模式没有 Bash，因此允许它按命令文件定义的事务步骤直接更新当前一个队列行；这是唯一例外，不能连续认领第二个对象。完整非交互循环仍由宿主控制器独占队列写入。

汇总轮只允许额外写入：

`分析报告/archive/YYMMDD跨市场_AI周期证据与赔率循环.md`

Claude 启动参数不使用 `--add-dir`。运行工作目录固定为股票投资库根目录。绕过权限时上述白名单不变。

## 状态机与失败恢复

```text
pending → running → completed
              └→ retry（最多两次）
                     └→ failed_after_retries
```

- 初次尝试加两次重试，总尝试上限为 3。
- 宿主在调用 Claude 前原子认领一个对象并写入唯一 `run_token`。
- Claude 只写 outcome，不直接改队列；宿主验证 token、对象、来源、四票、工具票和文件字段后才提交完成状态。
- 上次进程崩溃留下的 `running` 会在下次真实运行开始时转成 `retry`；`--dry-run` 不做恢复写入。
- `failed_after_retries` 不等于研究完成。存在失败对象时不生成跨市场汇总，后续需人工检查并显式重置。
- 达到时间、轮次或预算上限时安全停止，保留队列状态；下次从持久化队列继续。

## 18 个对象与轮次解释

LMND 同时属于现有持仓与美股赔率组，但在队列中只出现一次，排在现有持仓组。之后赔率段只处理 CRCL、NBIS、MSTR、BTGO。因此首轮是 18 个唯一对象；第 19 个成功轮次才是跨市场汇总。默认 22 轮为全量对象、汇总和少量技术重试预留空间。

## 不授权事项

- 旧 PRO 固定评分循环保留为历史记录，不授权 v2 判断。
- 概率未校准时保持 `uncalibrated`，未知不填 50%。
- 新闻不能单独提高 `H_B`；价格和 Attention 不能变成业务证据。
- 不进行 AI 共识计票，不给固定证据分，不用区间中点计算 EV。
- 期权只研究买方或借方价差；字段缺失时 `contract_status: incomplete` 且不得指定合约。
- 本循环永远不自动成交，也不修改组合主账。

## 验证入口

```bash
bash -n AI周期探索/0_总览/run_nightly_research_loop.sh
python3 AI周期探索/0_总览/validate_cross_market_v2.py
python3 -m unittest AI周期探索/0_总览/tests/test_cross_market_v2.py
```
