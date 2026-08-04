@AGENTS.md

# Claude Code 专属补充

本文件**只**包含 Claude Code 的适配说明。所有投资规则、加载顺序、写入 sink、Reviewer 与 Validator 条件都在 `AGENTS.md` 内，本文件不复制。

## 1. 加载入口

读取本文件时第一行 `@AGENTS.md` 已自动注入 Codex 公共入口规则。Claude Code 在本仓库的任何投资任务都遵守 `AGENTS.md`。

## 2. 只读 Reviewer 调用

Claude Code 端的 Reviewer 配置位于：

```
.claude/agents/investment-reviewer.md
```

该子 agent 工具集硬限制为 `Read`、`Grep`、`Glob`，禁止 `Edit` / `Write` / `NotebookEdit`。Reviewer 只读性由工具权限保证，不靠 Prompt 自我约束。

调用条件按 `AGENTS.md §4.1` 触发；Claude Code 不得跳过。

## 3. Claude Code 工具权限限制

- Claude Code 没有 native 写入权限层的 hook 强制力，写入 canonical 文件前必须运行 Validator；
- Claude Code 不能直接执行 Codex 专属队列脚本；
- Claude Code 不应当作自动交易入口，仅作研究、反证、记录与纪律提醒；
- 任何来自 Claude Code 的写入都必须先备份到 `.harness_backup/<YYYYMMDD-HHMMSS>/`。

## 4. 当前施工任务

本仓库已完成 Investment Harness 最小施工（T0–T7）。Claude Code 在新增规则、修改既有 canonical 文件、扩展 Skills 前必须先读取 `90_AUTOMATION/DESIGN_NOTES/` 与最近一次 `05_EVIDENCE_META/META/ABSORPTION_RECEIPTS/` 回执。

施工单原本位于会话上下文，已不在仓库内复述；如需重建任何施工阶段，以 `AGENTS.md` + `00_HOME/PATHS.md` + 上述回执为准。
