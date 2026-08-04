---
title: "evidence_log"
date: 2026-07-24
updated: 2026-07-24
layer: EVIDENCE
primary_role: legacy_company_evidence
status: archived
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
legacy_metadata_added: true
legacy_path: "AI周期探索/02_公司研究/HashKey Holdings/evidence_log.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/COMPANIES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# HashKey Holdings Evidence Log (Updated 2026-05-19)

## MCP 搜索记录
1. health_check → **失败**（MongoDB SSL 握手超时，SQL 正常）
2. search_channels → 成功（返回 20 个候选 channel）
3. search_articles → **全部失败**（MongoDB 不可用）
4. MCP fallback → agent-reach + Twitter MCP + 已有双轨报告

## 证据分级

### 一级证据（一手来源/高置信度）

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| HashKey 2025 年报（HKEX） | FY2025 营收 HKD 7.23 亿（+0.33%），净亏损 HKD 10.87 亿 | 财报趋势 | 高 | 一手 HKEX 披露 |
| HashKey 2025 年报 | 平台资产 HKD 184 亿（+60.5%），交易量 HKD 5,300 亿（+72.3%） | 飞轮分析 | 高 | 一手数据 |
| HashKey 2025 年报 | 稳定币交易量占比 48%，Omnibus 交易量 +640% | 结构性变化信号 | 高 | 年报披露 |
| HashKey 2025 年报 | 资产管理收入 HKD 1.2 亿（+49.8%） | 收入增长亮点 | 高 | 唯一显著增长分部 |
| HKEX IPO 文件 | IPO 发行价 HKD 6.68（2025.12.17），超购 395 倍 | 市场情绪 | 高 | HKEX 公告 |
| WuBlockchain (Twitter) | OKX/Binance/Bybit/Gate/HTX 于 2024.06 撤回香港 VATP 申请 | 竞争格局重构 | 高 | SFC 要求承诺全球不服务大陆用户 |
| HKMA 公告 | 2026 年 4 月发放首批 2 张稳定币牌照 | 监管趋势 | 高 | 官方公告 |
| SFC 新框架 | 2026.04/05 允许持牌平台进行代币化产品二次交易 | HashKey 直接受益 | 高 | 官方监管框架 |
| Japan FSA | 2026.06.01 起承认外国稳定币为合法支付方式 | 亚洲稳定币趋势 | 高 | 日本官方公告 |

### 二级证据（行业数据/中置信度）

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| Coin Bureau (Twitter, 1.1M followers) | 亚洲占全球稳定币支付量 2/3 | 市场规模验证 | 中 | 110K views |
| HashKey Group Twitter (@HashKeyGroup) | 越南 CAEX 战略合作，HashKey 提供交易所基础设施技术许可 | 商业模式扩展 | 中 | 公司官方推文 |
| HashKey Group Twitter | RWA 代币化解决方案，合作博时/广发证券/信达国际 | 新业务线 | 中 | 公司推文 |
| ALTF4 (Twitter, 57K followers) | HashKey Capital $250M 基金 | 资本实力 | 中 | 加密 VC 行业推文 |
| HashKey Chain Twitter (190K followers) | HSK White Paper 2.0，定位为 RWA + AI Agents 链上金融基础设施 | 叙事方向 | 中 | 公司推文 |
| CoinMarketCap (7.1M followers) | HashKey Research 分析 CLARITY Act 对稳定币影响 | 研究影响力 | 中 | 394 likes, 43K views |
| 分析师覆盖 | 3 位分析师给出 Strong Buy，平均目标价 HKD 7.17 | 市场预期 | 中 | TipRanks 数据 |

### 三级证据（市场数据/需持续验证）

| source | data_point | evidence_use | confidence | notes |
|---|---|---|---|---|
| 双轨报告（2026.05.06 更新） | 当前股价 HKD 4.55，P/S 8.77x，P/B 4.21x | 估值 | 中 | 需刷新实时数据 |
| 双轨报告 | 日均换手率 ~0.1%，流动性极差 | 交易风险 | 中 | 需刷新 |
| CoinGecko API（实时） | BTC $76.4K，ETH $2.1K，总市值 $2.63T | 加密市场环境 | 高 | 实时 API 数据 |
| Alternative.me API（实时） | Fear & Greed Index 25（极度恐惧） | 市场情绪 | 高 | 实时 API 数据 |
| Coinbase 10-K | 非盈利年 P/S 2.5-7x（2022-2023） | 估值对标 | 高 | SEC 公开文件 |
| Twitter 用户 | HSK 代币价格 ~$0.15，表现承压 | 代币生态 | 低 | 社区数据 |
| RWA.xyz/BCG | 链上 RWA 资产 $15-20B+，BCG 预测 2030 年 $16T | RWA 市场规模 | 中 | 行业报告 |

## 关键新发现（vs 旧分析）

1. **OKX 已撤回香港 VATP 申请（2024.06）**— 旧分析最大风险假设"OKX 获牌 = 死亡"被大幅削弱。SFC 要求申请人承诺全球不服务大陆用户，导致 OKX/Binance/Bybit/Gate/HTX 全部退出。
2. **越南 CAEX 合作**— HashKey 开始输出交易所基础设施技术（技术许可模式），这是新的收入来源类型。
3. **RWA 代币化解决方案**— 与博时、广发证券、信达国际合作，SFC 已开放代币化产品二次交易。
4. **HashKey Chain 定位升级**— 从通用 L2 转向 RWA + AI Agents 链上金融基础设施。
5. **亚洲稳定币支付占全球 2/3**— HashKey 的稳定币业务（48% 占比）可能不是噪音，而是结构性趋势。

## 覆盖不足

- Mindspace MCP MongoDB 完全不可用（SSL 握手失败）
- Web search / web-reader MCP 配额耗尽（2026.05.26 重置）
- 无法获取实时股价/行情数据
- HashKey 2026Q1 财报尚未发布
- OKX 是否已重新申请香港牌照需持续监控

## ⚠️ 数据差异待验证（2026-05-19 标注）

研究完成后的一个后台 agent 报告了与本研究所用数据不一致的数字。**web-reader 配额耗尽，无法现场验证。**

| 指标 | 本研究使用（双轨报告） | 后台 agent 报告 | 差异原因猜测 |
|---|---|---|---|
| 当前股价 | HKD 4.55 | HKD 3.67 | 股价可能在研究期间下跌，或数据时点不同 |
| 市值 | ~HKD 126 亿 | ~HKD 101.5 亿 | 与股价差异一致（4.55→3.67 ≈ -19%） |
| FY2025 营收 | HKD 7.23 亿 | HKD 2.196 亿 | ⚠️ 最大差异——可能为单季度 vs 全年，或货币单位错误 |
| P/S | 8.77x | 46.2x | 随营收差异放大 |
| 分析师覆盖 | 3 位 Strong Buy | 0 位 | 需验证数据源 |

**处理方案**：2026-05-26 web-reader 配额重置后，优先验证：
1. 从 HKEX/AAStocks 获取实时股价和市值
2. 从 HKEX 年报确认 FY2025 全年营收
3. 如营收确实是 HKD 2.196 亿（非 7.23 亿），P/S 46.2x 将使"偏贵"判断升级为"极度昂贵"，scorecard 需重新评估
