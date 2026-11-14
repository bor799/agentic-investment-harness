# Research Desk（Cindy 主视图子项目）

Cindy 左侧入口 **Research Desk** 内嵌的投资研究观察台。属于本仓库 "一个入口 → 多个可定制功能模块" 的第一个模块：目录、地图与规则卡片都由 `data/catalog.json` 驱动，后续模块沿用同样的数据契约模式扩展，不需要改 Cindy 应用本身。

定位：从已经发生的结果逆向寻找候选解释，或从当前线索向前追踪可能影响；保留反例、数据时点和下一验证。所有跨指标路径都是**研究假设，不是已识别的因果**。

## 功能

- 指标目录：8 类、24 主题、71 项（28 核心）；逐项定义、时点、解释边界、搜索、分组与核心筛选。
- 2D / 可旋转 3D 研究地图；青色仅表示"部分行情代理可用"，缺失/过期显示灰色，不渲染市场安全信号。
- 金银铜专题：GLD / SLV / CPER 日线代理，明确标注基金≠现货、CPER 换月边界。
- JNK–SPY 三版历史经验规则并列展示（−1.5 残差 Z 旧版、首次 −3 动态版、阈值探索版），不计算触发、不自动交易。
- 2026-10-23 历史监测卡 14 字段独立展示，标注 asOf，不冒充最新读数。
- "复制讨论问题"生成含选定节点、数据时点与替代解释的文本；不自动发送。

## 数据来源与边界

- 优先复用本机既有 Alpaca SIP 只读连接（`GET /v2/stocks/bars`，raw + all 两种复权口径）；缺项尝试 Yahoo 日线（含 VIX/VIX3M）。公开源可能 403/限流，失败保留旧值并标 stale，无缓存则如实显示缺失。
- 凭证从本机固定路径的 `.env` 读取（路径定义在 `node/market.cjs`），只发送至行情域名；不进前端、KV、日志、包与 Git。没有账户、持仓或订单接口。
- 保守排除 UTC 当天未核验收盘的日线；"及时"指日线研究更新，不是实时盘口。
- 刷新：手动按钮，或自动每15分钟一次（仅页面可见时执行，可暂停，顶栏显示下次刷新时间）。
- 19 个行情代理 ≠ 71 项指标接入；信用利差、公司经营、宏观时钟、事件抓取与权重归因未接入。
- 无风险总分、无贡献权重、无买卖指令；基金收益不能当现货收益，价格变化不能替代 OAS。

## 结构

```
ghost.json            Cindy 插件入口（mainView + 后台工具 + node 只读行情）
main-view.html        页面骨架（CSP：脚本外置同源）
desk.css / desk.js    界面与交互（深浅模式、320px、键盘、reduced-motion）
main.js / market.js   后台：BroadcastChannel 协议、快照缓存、行情解析
node/market.cjs       随包 Node 只读行情连接（json-rpc-stdio）
data/catalog.json     脱敏指标目录（sourcePath 用 local:// 指向本机档案）
tests/                解析、缺口、陈旧与口径测试
docs/                 设计与数据契约 / 本机部署与已知限制
```

## 验证

```
node tests/market.test.cjs
node tests/edge-cases.test.cjs
python3 -m unittest discover -s 90_AUTOMATION/TESTS -p 'test_*.py'   # 仓库根目录
python3 90_AUTOMATION/PIPELINES/audit_publication.py .               # 发布审计
```

真实宿主安装与刷新记录见 `docs/LOCAL-SETUP.md`。设计原则与数据契约见 `docs/DESIGN.md`。
