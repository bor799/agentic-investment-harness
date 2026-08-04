---
title: "source_health_2026-05-24"
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
legacy_path: "AI周期探索/0_总览/source_health_2026-05-24.md"
migration_target: "02_术/SKILLS + 90_AUTOMATION"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# Source Health

日期：2026-05-24

## 结论

当前可以启动第一阶段索引和 MCP-first 公司刷新。Mindspace Source MCP 的 SQL 和 MongoDB 均可用；agent-reach 可作为 fallback，但 Exa、Twitter/X、Reddit 当前不可作为第一轮主信源。

## Mindspace Source MCP

调用入口：

```bash
python /Users/murphy/Desktop/mindspace/mindspace_ml_backend/script/mcp_call.py health_check
```

检查结果：

```json
{
  "success": true,
  "server": "mindspace-source",
  "sql_ok": true,
  "mongo_ok": true,
  "errors": []
}
```

可用策略：

- 继续使用 `mcp_call.py` bridge，不依赖 Claude Code 工具选择器是否直接暴露 MCP 工具。
- 每轮先 `health_check`。
- 核心证据必须通过 `get_article_detail` 回源。
- 遇到 channel 轮换或 MongoDB 超时时，写入 `evidence_log.md`，再进入 fallback。

## agent-reach

命令：

```bash
agent-reach doctor
```

当前可用渠道：

| 渠道 | 状态 | 用途 |
|---|---|---|
| GitHub | 可用 | 开源项目、工程师信号、issue/PR 活跃度 |
| Jina Reader | 可用 | 通用网页读取、公司 IR、交易所公告、新闻正文 |
| V2EX | 可用 | 中文开发者社区信号 |
| RSS/Atom | 可用 | 订阅源读取 |
| 雪球 | 可用 | 股票行情、中文市场社区动态 |
| B站 | 部分可用 | 视频和字幕读取 |
| 抖音 | 可用 | 短视频解析，暂不作为投资主证据 |
| LinkedIn | 可用 | 公司、岗位、组织扩张信号 |

当前不可用或未配置：

| 渠道 | 状态 | 影响 |
|---|---|---|
| Exa | 未配置 | 全网语义搜索能力不足，不能作为 fallback 主搜索 |
| Twitter/X CLI | 未安装 | 社交情绪和工程师实时信号覆盖不足 |
| Reddit CLI | 未安装 | 英文社区讨论覆盖不足 |
| YouTube JS runtime | 未配置完整 | 视频字幕读取可用性需修复 |

## 第一轮可执行边界

可以做：

- 本地索引整理。
- Mindspace MCP 查询。
- Jina Reader 读取公开网页。
- 雪球中文行情和社区补充。
- 公司 IR、SEC/HKEX/交易所公告的网页读取。

暂缓做：

- 依赖 Exa 的全网趋势扫描。
- 依赖 Twitter/X 的实时 KOL 情绪。
- 依赖 Reddit 的英文散户社区情绪。

## 建议修复项

优先级从高到低：

1. 配置 Exa：恢复全网语义搜索能力。
2. 安装 Twitter/X CLI：恢复工程师和 KOL 实时信号。
3. 安装 Reddit CLI：补充英文社区情绪。
4. 配置 yt-dlp JS runtime：改善视频/播客信源。

