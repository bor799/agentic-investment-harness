# Legacy Claude Config Archive

本目录存放已被 frontmatter 自标为 `legacy_claude_automation` 或 `superseded` 的旧 `.claude/agents/` 与 `.claude/commands/` 文件。

## 归档依据

每个文件的 frontmatter 已声明：

| 文件 | 状态 | 迁移目标 |
|---|---|---|
| `agents/ai-cycle-cross-market-v2.md` | `legacy_claude_automation` | `90_AUTOMATION/PROMPTS` |
| `commands/ai-cycle-cross-market-v2.md` | `legacy_claude_automation` | `90_AUTOMATION/PROMPTS` |
| `commands/ai-research-loop-pro.md` | `superseded` | `90_AUTOMATION/PROMPTS` |

这些入口与 Investment Harness 无关：
- 不被 `AGENTS.md` / `CLAUDE.md` 引用；
- 不被 `00_HOME/HOME.md` 或 `00_HOME/CONTENT_ROUTER.md` 当作权威；
- 其 PreToolUse hook 与 `$ARGUMENTS` 命令仅服务旧 AI 周期 v2 工作流。

## 备份位置

修改前已备份至：

```
.harness_backup/20260725-190113/.claude/{agents,commands}/
```

SHA-256：

- `agents/ai-cycle-cross-market-v2.md`: `1ae8f30a400e58e3cbe1a43370fccca547961ed8aa54d89d05308725407cf306`
- `commands/ai-cycle-cross-market-v2.md`: `4ce5be53f6ea77fa053f8c48e4e3bf4c35b46e1505824c1e486cbdd3d90d6a48`
- `commands/ai-research-loop-pro.md`: `8cc2232397fb0d9ac0b21220587c1462638a3e69a873dbe5767f44bf162a3945`

## 不在此目录的内容

- 旧 prompt 全文与跨市场 v2 队列 → 已在 `90_AUTOMATION/PROMPTS/REVIEW_QUEUE/`，本轮不再迁移。
- 旧 phase2 脚本 → 仍在 `90_AUTOMATION/PIPELINES/`，本轮不调用、不恢复。
- 旧运行态 → 仍在 `90_AUTOMATION/RUNTIME/`，本轮不调用。
