# Research Desk 设计与数据契约

## 为什么做

投资研究的主要成本不在取数，而在"看到异常 → 找到候选解释 → 保留反例与数据时点 → 形成下一验证"这条链路的管理。Research Desk 把这条链路放进 Cindy 主视图：一个入口承载多个可定制功能模块，减少应用切换，优先训练判断而不是替代判断。

## 模块架构

```
Cindy 主视图（唯一入口）
  └─ Research Desk 模块
       ├─ data/catalog.json     静态目录：指标、分组、专题、规则版本、历史卡
       ├─ 页面（desk.js）        只读目录 + 地图 + 专题 + 规则卡
       ├─ main.js 后台           快照缓存（/kv ≤64KB）+ BroadcastChannel 协议
       └─ node/market.cjs        本机只读行情连接（Alpaca 优先，缺项 Yahoo）
```

后续模块（新的专题、新的规则族）= 新的 catalog 数据 + 可选的新数据源，不新增入口。模块之间不共享运行时状态，只共享目录结构与讨论流程（"复制讨论问题"）。

## 数据契约

### catalog.json（随包静态）

```jsonc
{
  "generatedAt": "...", "sourcePath": "local://...",   // 脱敏档案引用，非机器路径
  "groups":   [{ "id": "A", "name": "..." }],
  "metrics":  [{ "id","core","groupId","subgroupId","name","fields","definition",
                 "unit","frequency","availability","meaning","boundary",
                 "evidenceStatus","role" }],           // 除 core 外均为字符串
  "history":  { "asOf": "2026-10-23", "items": [ /* 14 字段观测卡 */ ] },
  "rules":    [ /* JNK–SPY 各版本，threshold 未核实时为 null */ ],
  "topics":   [ /* 金银铜代理与边界 */ ]
}
```

### 行情快照（运行时）

- 页面先 `fetch('/wake')`，再经 BroadcastChannel `murphy-research-desk-v1` 请求 `{type:'desk-request',id,action:'snapshot'|'refresh'}`，回 `{type:'desk-response',id,ok,snapshot|error}`。
- `snapshot = { fetchedAt, quotes:[{symbol,label,kind,currency,asOf,observedAt,close,change1d,return5d,return21d,return63d,ma50Distance,drawdown63,volatility20,missingBars,basis,sourceUrl,status,error?}], errors:[] }`。
- 回报与距离为百分数（非小数）；series 用复权收盘可用时标注于 `basis`；缺失为 null，不伪造。
- 超时：refresh 100s、snapshot 15s；先 wake 并以同 id 重发直至回应，超时清理 timer。网络失败时目录仍可完整浏览。

### 展示诚实性规则

- 颜色只表达数据可用性（available / stale / missing），不表达市场安全或风险方向。
- 不生成风险总分、不显示贡献权重（除非真实可计算）、不产生买卖指令。
- `关联 ≠ 因果`：地图连线是研究假设组织，双向 hypothesisEdges 用于"从事件往下查 / 从线索往上追"两种路径。
- 历史监测卡固定 asOf 展示，规则卡 threshold 未核实即为 null 并显示"未启用"。

## 验收记录（2026-11-14，本机 Cindy 0.1.136）

| 项 | 结果 | 证据 |
|---|---|---|
| 语法/单测 | PASS | `node tests/market.test.cjs`、`edge-cases.test.cjs`；仓库 197 项 unittest PASS |
| 视觉/交互 | PASS | 桌面/320px/深色/reduced-motion、71 节点、3D、搜索、28 核心筛选，无页面错误 |
| 宿主安装 | PASS | Forge 安装回执 `installed`，local 命名空间，启用 |
| 宿主真实刷新 | PASS | `refresh_market` 经已安装插件返回 21 标的、asOf 2026-11-13 |
| 重开缓存 | PASS | `get_snapshot` 返回相同 fetchedAt 的 KV 快照 |
| 来源失败态 | 已验证 | 见 LOCAL-SETUP「已知限制」 |
| 900px 双栏常驻 | PASS | 地图+详情同排，详情 sticky；`node .verification/visual-mid.cjs` |
| 自动刷新可见化 | PASS | 倒计时+暂停开关（localStorage 记忆）；同上脚本 |

## 迭代方向（未承诺）

- 日内同步数据接入后，JNK–SPY 规则卡从"三版并列"升级为可计算触发（仍不自动交易）。
- 更多指标的真实数据源接入；信用利差（OAS）优先于价格代理。
- 模块化拆分：目录驱动的第二个专题模块落地时，抽取公共目录渲染层。
