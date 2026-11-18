# 本机部署与已知限制

本页描述在本机（macOS + Cindy ≥ 0.1.136）复现 Research Desk 的步骤与真实验证记录。**本机成功不等于任意机器零配置可用**：行情凭证与档案路径都是本机既有配置，换机需按下文调整。

## 前置条件

1. Cindy ≥ 0.1.136（mainView / wake+kv / BroadcastChannel 后台接口在此版本核实，commit `7227e83`）。
2. 本机既有 Alpaca 只读凭证：`.env` 含 `ALPACA_API_KEY` / `ALPACA_API_SECRET`，路径定义在 `node/market.cjs`。凭证只发送至 `data.alpaca.markets`，不进仓库、KV、日志或包。
3. 出网可达 `query1.finance.yahoo.com`（缺项兜底）。

## 安装与验证（本机记录，2026-11-14）

```
# 1. 安装（Forge 从源码目录装到 local 命名空间）
ghost_forge_install dir=/path/to/projects/research-desk
#    回执：installed, instanceId=_ns__local__murphy-research-desk, enabled=true

# 2. 确认插件与工具
ghost_info murphy-research-desk        # setup.state=ready, tools=get_snapshot/refresh_market

# 3. 真实刷新（经已安装插件的 node 进程与行情链路）
ghost_call murphy-research-desk refresh_market
#    回执：fetchedAt=2026-11-14T07:35:31Z, 21 标的, asOf=2026-11-13, 全部 available

# 4. 重开缓存（KV 持久化验证）
ghost_call murphy-research-desk get_snapshot
#    回执：与上步相同 fetchedAt 的完整快照

# 5. 单元测试
node tests/market.test.cjs && node tests/edge-cases.test.cjs
```

页面入口：Cindy 左侧 **Research Desk**。首次打开如无快照，点"刷新日线"；网络失败时目录与规则仍可完整浏览。

## 已知限制（如实，不淡化）

- **沙箱内 Alpaca 未生效**：同日对照测试中，`node/market.cjs` 独立运行可从 Alpaca 取回 19 ETF 日线（asOf 2026-11-13），但经插件沙箱内 node 进程请求失败（原因在沙箱环境，具体为文件或网络隔离），后台自动落到 Yahoo 兜底，数据完整但 `sourceUrl` 为 Yahoo。修复沙箱内主数据源是下一迭代事项。
- **Yahoo 公共接口不稳定**：批量请求可能 403/限流；失败保留旧值并标 stale，无缓存显示缺失（灰色，不是绿色）。
- **19 代理 ≠ 71 指标**：当前仅 A101/A102/A301/E101/G101/G102 有局部代理观测；信用利差、公司经营、宏观时钟、事件抓取未接入。
- **金银铜是新建专题**：GLD/SLV/CPER 日线代理，明确基金≠现货；用户记忆中的完整旧专题尚未定位。
- **JNK–SPY 未启用触发计算**：三版规则并列展示；−1.5 是旧版同钟点残差 Z（联合条件），不是 −1.5% 跌幅；需要同步日内数据，本页不提供。
- **历史监测卡固定 asOf 2026-10-23**：14 字段独立展示，不是实时读数。
- **KV ≤64KB**：快照超限时不持久化（页面提示），本次显示仍有效。
- 凭证与私人档案路径不出现在仓库：`data/catalog.json` 的 `sourcePath` 使用 `local://` 引用本机档案。

## 脱敏清单（发布前检查）

排除：`.env`、`.verification/`（日志与截图）、构建产物 `.cindy`、内部交接文档、绝对私人路径（已转 `local://`）、持仓与交易记录。保留：目录定义、代码、测试、验收与限制说明。

## 2026-11-18 · 2.0.1 同步

本目录源码已与本机在用版本 2.0.1 对齐（desk-core 契约层、消息看板四视图、日记草稿、运行健康、X 共识差可选接入）。上文的安装与验证步骤不变；`tests/` 以 `market / desk-core / main-harness` 三套为准（1.1.0 的 `edge-cases.test.cjs` 已并入 `market.test.cjs`）。
