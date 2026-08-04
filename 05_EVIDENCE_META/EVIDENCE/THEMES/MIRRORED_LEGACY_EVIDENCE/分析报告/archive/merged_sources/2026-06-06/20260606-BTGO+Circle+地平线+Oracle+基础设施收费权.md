---
title: "20260606-BTGO+Circle+地平线+Oracle+基础设施收费权"
date: 2026-07-24
updated: 2026-07-24
layer: EVIDENCE
primary_role: legacy_analysis_evidence
status: archived
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
legacy_metadata_added: true
legacy_path: "分析报告/archive/merged_sources/2026-06-06/20260606-BTGO+Circle+地平线+Oracle+基础设施收费权.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/THEMES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# BTGO / Circle / 地平线 / Oracle：基础设施收费权与三年翻倍验证

更新日期：2026-06-06（北京时间）  
市场数据快照：美股为 2026-06-05 盘中/近收盘快照，港股为 2026-06-05 港股收盘后公开页面快照。  
核心资料：BitGo FY2025 10-K 与 Q1 2026 release、Circle FY2025 10-K 与 Q1 2026 10-Q、地平线 2025 年度业绩公告、Oracle FY2026 Q3 release。

## 1. 一页结论

结论先说硬的：四家公司都在“基础设施”叙事里，但收费权质量完全不同。

| 标的 | 需求是否真实增长 | 生态位 | 收费权是否成立 | 利润能否留存 | 三年翻倍是否被当前估值支持 | 投资池 |
|---|---|---|---|---|---|---|
| BTGO / BitGo | 混合。客户数和价格归一化 AoP 增长，但实际 AoP、staking revenue 受币价拖累明显。 | 机构 crypto custody + wallet + trading + staking + stablecoin infrastructure。OCC national trust bank 地位增强合规可信度。 | 部分成立。subscriptions/services、staking、trading margin 有收费权；stablecoin-as-a-service 有收入线但净留存极低；RWA 收入证据不足。 | 暂弱。FY2025 reported revenue 巨大，但主要来自低毛利 digital asset sales；Q1 2026 经济毛利约 1.3% of revenue。 | 高赔率但证据不足。市值很小，翻倍所需 EBITDA 不高，但必须证明非币价 beta 的经济毛利扩张。 | 证据不足池 |
| Circle / CRCL | 真实。Q1 2026 USDC 期末流通量 $77.0B，同比 +28%；平均流通量 +39%；链上交易量 +263%。 | USDC/EURC 发行方 + 链上美元结算网络 + CPN/Arc 生态。 | 成立，但本质是“美元稳定币 float + 分销网络”的收费权，不是单纯支付手续费。 | 中等。RLDC 留存明确，但 Coinbase/渠道分成与利率决定利润弹性。 | 有条件支持。若 USDC 平均流通量 3 年到 $150-180B 且利率不大幅下行，翻倍可解释；若利率降到 2% 附近，要求大幅提高。 | 核心候选池（价格纪律） |
| 地平线机器人 / 9660.HK | 真实。FY2025 收入 +57.7%；Journey 硬件出货 4.01M 套，NOA-capable 出货占比 45%，ASP +75%+。 | 不是纯平台，也不是普通零部件商；是“芯片 + 软件/IP + 工具链 + 生态伙伴交付”的混合平台。 | 正在形成。license/services 毛利率 94.5% 说明软件/IP 收费权强；但产品解决方案占比上升压低整体毛利率。 | 尚不能。gross profit 增长，但 R&D 费用率 137.1%，调整经营亏损扩大。 | 有条件支持但已预支不少。需要收入 3 年到 RMB10-14B、产品毛利率修复、R&D 费用率明显下降。 | 观察池 |
| Oracle / ORCL | 真实。Q3 FY2026 OCI revenue +84%，RPO $553B +325%。 | AI cloud + enterprise database + multicloud database 验证器。 | 成立。Oracle 证明关键企业工作负载仍愿意为数据库与云基础设施付费。 | 被 AI capex 暂时压低。TTM FCF 为 -$24.7B。 | 本报告不作为核心仓翻倍模型。Oracle 是趋势验证器，不是本轮高赔率标的。 | 剔除池（仅趋势验证） |

一句话组合判断：Circle 是确定性最强的收费权，地平线是产业趋势最真实但利润留存未验证，BTGO 是赔率最大但证据最薄的“便宜期权”，Oracle 只证明“数据库 + AI 云 + 企业关键工作负载”这条主线仍然有效。

## 2. BTGO 深度研究

### 2.1 资料与口径

主要来源：

- [BitGo FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1740604/000174060426000020/btgo-form10xk.htm)
- [BitGo Q1 2026 financial results PDF](https://s21.q4cdn.com/773293151/files/doc_news/BitGo-Announces-First-Quarter-2026-Financial-Results-2026.pdf)
- [BitGo IPO pricing announcement](https://investors.bitgo.com/news/news-details/2026/BitGo-Holdings-Announces-Pricing-of-Initial-Public-Offering/default.aspx)
- [BitGo OCC national trust bank approval announcement](https://investors.bitgo.com/news/news-details/2026/BitGo-Becomes-the-First-Public-Federally-Chartered-Digital-Asset-Infrastructure-Company/default.aspx)

关键口径：BitGo 的 reported revenue 不能直接当作 SaaS/平台收入看。digital asset sales 按 gross basis 记收入和成本，导致收入规模极大，但真实留存靠 margin / take rate / subscriptions / services / staking spread / stablecoin reserve economics。

### 2.2 核心财务与运营数据

| 指标 | FY2025 / Q1 2026 | 解释 |
|---|---:|---|
| FY2025 total revenue | $16.2B，+424.3% YoY | 主要由 digital asset sales gross basis 推动。 |
| FY2025 digital asset sales revenue | $15.6B，+512.6% YoY | 总额大，但 overall margin 仅 0.21%，低于 2024 的 0.47%。 |
| FY2025 staking revenue | $385.0M，-16.2% YoY | 受数字资产价格波动影响。 |
| FY2025 subscriptions & services | $121.5M，+56.9% YoY | 最像“基础设施 SaaS/服务”的收入线。 |
| FY2025 stablecoin-as-a-service | $66.7M 新收入线 | 但 stablecoin sponsor fees $64.0M，净贡献很小。 |
| FY2025 net income / adjusted EBITDA | net loss $(14.8)M；adjusted EBITDA $32.4M | 净利受 BTC treasury mark-to-market 等影响。 |
| Q1 2026 total revenue / direct costs | $3.774B / $3.725B | 经济毛利约 $49.0M。 |
| Q1 2026 clients | 5,569，+42.0% YoY | 客户扩张是真实积极信号。 |
| Q1 2026 assets on platform | $63.0B，-30.4% YoY | 价格归一化后 +29.4% YoY，说明币价扰动很大。 |
| Q1 2026 assets staked | $11.8B，-58.3% YoY | 价格归一化后 +20.8% YoY。 |
| Q1 2026 digital asset sales | revenue $3.659B，direct cost $3.648B，margin 32 bps | margin 较 Q1 2025 20 bps 和 Q4 2025 24 bps 改善。 |
| Q1 2026 stablecoin-as-a-service | revenue $38.2M，direct cost $35.3M，take rate 7.4% | gross revenue 成长，但净留存仍需验证。 |
| Q1 2026 derivatives | notional volume 约 $3B | derivatives net revenue 口径与 spot gross revenue 口径不同，reported revenue 可比性下降。 |

### 2.3 四条增长线验证

**1. RWA / tokenization 是否放大 custody assets：证据不足。**  
支持证据是 BitGo 已经具备 regulated custody、wallet、settlement、compliance、national trust bank 的合规基础，且 Q1 2026 normalized assets on platform +29.4% YoY。反证是公司未单独披露 RWA / tokenized assets revenue，也没有把 AoP 增长拆成净流入、币价上涨、RWA 资产贡献。当前只能说“位置有利”，不能说“RWA 已经放大收入”。

**2. stablecoin-as-a-service 是否成为新收入线：成为收入线，但尚未证明利润线。**  
FY2025 stablecoin-as-a-service revenue $66.7M，Q1 2026 $38.2M，说明产品有商业化。但 FY2025 sponsor fees $64.0M，Q1 2026 direct cost $35.3M，净留存很薄。结论：stablecoin SaaS 是真实业务，不是纯叙事；但“收费权”还不等于“利润留存权”。

**3. 机构交易、衍生品、prime brokerage 是否带来高 take rate：方向正确，证据仍早。**  
Q1 2026 digital asset sales margin 从 20 bps 提高到 32 bps，derivatives notional volume 约 $3B，说明高 margin mix 有改善。但 digital asset sales 本体仍是低毛利 gross-accounting 业务，reported revenue 不能当经营能力。要证明高 take rate，需要后续看到：digital asset sales net margin 持续 >30 bps、derivatives revenue 单独披露、subscriptions/services 同步增长。

**4. crypto 牛市是否只是平台 beta：很可能混有显著 beta。**  
FY2024/2025 的收入与净利润都受数字资产价格、交易活跃度、BTC treasury mark-to-market 影响。Q1 2026 实际 AoP -30.4% YoY，而 normalized AoP +29.4%，这说明单看 AoP 容易误判。未来必须用 normalized AoP、净流入、经济毛利、subscriptions/services、客户数来判断经营质量。

### 2.4 收费权判断

成立的部分：

- Custody/wallet/subscriptions/services：高价值机构基础设施，FY2025 +56.9%，更接近可持续收费权。
- Staking：有 take rate，但受 token price 与 staking balance 影响。
- Trading/derivatives：有交易型收费权，但 reported revenue 有会计放大，真实应看 margin。
- Stablecoin infrastructure：已商业化，但净利润留存尚弱。

未成立或证据不足的部分：

- RWA/tokenization：没有独立收入披露。
- Stablecoin-as-a-service 的净留存：gross revenue 增长不等于利润增长。
- 客户迁移壁垒：机构 custody 有合规和集成黏性，但 Coinbase、Fireblocks、Anchorage、银行托管、自建方案都可替代部分功能。

### 2.5 支持证据、反证、待验证信号

| 类型 | 内容 |
|---|---|
| 支持证据 | 客户数 +42.0%；normalized AoP +29.4%；subscriptions/services +56.9%；national trust bank approval；Q1 digital asset sales margin 改善到 32 bps。 |
| 反证 | FY2025 revenue 大部分来自低毛利 digital asset sales；stablecoin gross revenue 几乎被 sponsor fees 抵消；actual AoP 与 assets staked 下滑；净亏损受数字资产价格影响。 |
| 待验证信号 | RWA/tokenized assets revenue 单独披露；stablecoin net contribution >$20M annualized；subscriptions/services 连续 4 季度 >30% 增长；derivatives revenue 和 margin 单独披露；normalized AoP 增长与实际净流入一致。 |

### 2.6 BTGO 估值反推

市场快照：BTGO 约 $4.71，市值约 $0.46B。三年翻倍需要市值约 $0.93B。

reported revenue 对 BTGO 的估值意义有限，模型应看“经济毛利 / adjusted EBITDA / net income”。

| 反推项 | 需要达到的状态 |
|---|---|
| 三年后市值 | $0.9-1.0B |
| 需要的 revenue | reported revenue 不关键；需要 economic gross contribution 约 $280-350M。 |
| 需要的 EBITDA | adjusted EBITDA $75-90M，对应 10-12x EBITDA。 |
| 需要的 net income | $45-60M，对应 15-20x earnings。 |
| 路径是否现实 | 有赔率，但不是 base case。Q1 2026 年化经济毛利约 $196M，若 subscriptions/services、trading margin、stablecoin net contribution 同时改善，翻倍可解释。 |
| 最敏感变量 | crypto 交易活跃度、actual/normalized AoP 差异、digital asset sales margin、stablecoin net contribution、BTC treasury mark-to-market。 |

BTGO 的一句话：市值低到可以把它看成“机构 crypto 基础设施期权”，但它还没有证明 RWA/stablecoin 能变成高留存利润。

## 3. Circle vs BTGO 生态位比较

主要来源：

- [Circle Q1 2026 results](https://www.circle.com/pressroom/circle-reports-first-quarter-2026-results)
- [Circle Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1876042/000187604226000150/crcl-20260331.htm)
- [Circle FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1876042/000187604226000062/crcl-20251231.htm)
- [U.S. Treasury GENIUS Act proposed rule, 2026-04-08](https://home.treasury.gov/news/press-releases/sb0435)
- [White House: S.1582 / GENIUS Act signed, 2025-07-18](https://www.whitehouse.gov/briefings-statements/2025/07/the-president-signed-into-law-s-1582/)

### 3.1 Circle 核心数据

| 指标 | Q1 2026 |
|---|---:|
| USDC in circulation, end of period | $77.0B，+28% YoY |
| Average USDC in circulation | $75.2B，+39% YoY |
| Reserve return rate | 3.5%，同比 -66 bps |
| USDC on-chain transaction volume | $21.5T，+263% YoY |
| Total revenue and reserve income | $694M，+20% YoY |
| Reserve income | $653M，+17% YoY |
| Other revenue | $42M，+101.5% YoY |
| Distribution, transaction and other costs | $407M，+17% YoY |
| Revenue less distribution costs | 约 $287M |
| Net income | $55M，-15% YoY |
| Adjusted EBITDA | $151M，+24% YoY |

Circle 的收费权本质：USDC 作为链上美元结算资产，发行方拿到 reserve income；但为了分销和流动性，要把相当一部分收益分给 Coinbase、Binance 等渠道。FY2025 10-K 披露，distribution and transaction costs 增长主要来自 Coinbase、Binance 和其他战略分销伙伴成本增加。

### 3.2 RWA 价值链拆解

| RWA 价值链环节 | 谁吃价值 | Circle | BTGO |
|---|---|---|---|
| 资产发行方 | BlackRock、资产管理人、贷款/基金/债券发行方 | 不主导资产本体 | 不主导资产本体 |
| 法律结构 / SPV / fund admin | 律所、信托、基金管理人、transfer agent | 间接受益 | 间接受益 |
| tokenization platform | Securitize、Ondo、Figure、资产方自建等 | 不是主层 | 不是主层，但可提供 wallet/custody/infrastructure |
| custody | 托管人、银行、qualified custodian | 储备资产 custody 依赖 BNY/BlackRock 等；对客户资产 custody 不是核心 | 核心收入层之一：custody、wallet、qualified/regulatory infrastructure |
| wallet / permissioning / compliance | 基础设施平台 | 有 Circle Mint、CPN、compliance 基础 | 核心能力之一 |
| stablecoin settlement | 稳定币发行方 | 核心层。USDC 是 settlement money，吃 float/reserve economics | 参与 stablecoin infrastructure，但不是主要 dollar settlement network |
| trading liquidity | exchange、broker、OTC、prime broker | 间接受益于 USDC 流动性 | trading、derivatives、settlement 可吃交易 margin |
| reporting / compliance | transfer agent、custodian、platform | 部分应用层 | custody/compliance/reporting 可参与 |
| distribution | exchanges、wallets、banks、fintech | 关键但成本高；Circle 需要给渠道分成 | BitGo 有机构客户网络，但分销强度低于稳定币网络 |

### 3.3 必答问题

**1. RWA 爆发时 Circle 吃哪一层价值？**  
Circle 吃“链上美元结算层”和“稳定币 float 层”。RWA 交易、申购赎回、抵押融资、跨平台结算都需要稳定结算资产时，USDC 流通量和链上交易量受益，收入主要体现为 reserve income 与少量交易/服务收入。

**2. BTGO 吃哪一层价值？**  
BTGO 吃“机构 custody / wallet / compliance / settlement / trading access”层。如果 RWA 资产进入机构组合，BitGo 可托管 tokenized assets、提供权限钱包、结算、交易、合规报告。但它不是 RWA 资产发行方，也不是稳定币主网络。

**3. 谁确定性更强？**  
Circle 更强。原因是 USDC 流通量、交易量、reserve income、distribution cost、adjusted EBITDA 都已披露并形成闭环。BTGO 的 RWA 收入未单独披露，stablecoin-as-a-service 的 net contribution 还小。

**4. 谁赔率更大？**  
BTGO 赔率更大。约 $0.46B 市值下，只要经济毛利和 adjusted EBITDA 明显改善，股价弹性会很大。但这不是确定性，是“便宜 + 证据未完成”的赔率。

**5. 谁更受利率、监管、分销成本、竞争影响？**

- 利率：Circle 更敏感。reserve income 直接受短端利率影响。BTGO 也受利率影响，但主要利润驱动不是 reserve float。
- 监管：两者都敏感。Circle 受稳定币法规、PPSI、reserve、AML/sanctions 影响；BTGO 受 custody、trading、staking、bank/trust 监管影响。
- 分销成本：Circle 更敏感。渠道分成是利润留存关键变量。
- 竞争：Circle 面对 Tether、银行稳定币、交易所/支付公司稳定币；BTGO 面对 Coinbase、Fireblocks、Anchorage、银行托管、自建钱包。

**6. 三年翻倍角度，谁更可能？**  
概率角度 Circle 更可能，赔率角度 BTGO 更大。Circle 的翻倍路径需要 USDC float 扩大和 RLDC 扩张；BTGO 的翻倍路径需要市场重新相信它的经济毛利不是 crypto beta。若只能选一个“基础设施收费权”更清晰的公司，是 Circle。

## 4. 地平线深度研究

主要来源：

- [Horizon Robotics 2025 annual results announcement PDF](https://cdn.financialreports.eu/financialreports/media/filings/51126/2026/RNS/51126_rns_2026-03-19_1075f3cb-9531-4ffb-a1c7-93331d822bba.pdf)
- [Horizon Robotics investor relations](https://www.horizon.auto/investor-relations)
- [StockAnalysis: Horizon Robotics revenue and market cap](https://stockanalysis.com/quote/hkg/9660/revenue/)
- [StockAnalysis: Horizon Robotics financials](https://stockanalysis.com/quote/hkg/9660/financials/)

### 4.1 核心财务

| 指标 | FY2025 | FY2024 | 变化 |
|---|---:|---:|---:|
| Revenue | RMB3.758B | RMB2.384B | +57.7% |
| Gross profit | RMB2.426B | RMB1.841B | +31.7% |
| Gross margin | 64.5% | 77.3% | -12.8 pct |
| Operating loss | RMB(3.339)B | RMB(2.144)B | 亏损扩大 |
| Adjusted operating loss | RMB(2.372)B | RMB(1.495)B | 亏损扩大 |
| Adjusted net loss | RMB(2.812)B | RMB(1.681)B | 亏损扩大 |
| R&D expense | RMB5.154B | RMB3.156B | +63.3% |
| R&D as % revenue | 137.1% | 132.4% | 未下降 |
| S&M as % revenue | 16.8% | 17.2% | 小幅下降 |
| Admin as % revenue | 19.3% | 26.8% | 明显下降 |

### 4.2 收入结构与毛利结构

| 业务 | FY2025 revenue | 占比 | YoY | FY2025 gross profit | FY2025 GM |
|---|---:|---:|---:|---:|---:|
| Automotive product solutions | RMB1.622B | 43.2% | +144.2% | RMB560M | 34.5% |
| Automotive license and services | RMB1.935B | 51.4% | +17.4% | RMB1.829B | 94.5% |
| Automotive subtotal | RMB3.557B | 94.6% | +53.9% | RMB2.389B | 67.2% |
| Non-automotive solutions | RMB201M | 5.4% | +179.9% | RMB36M | 18.1% |

关键判断：地平线的“平台性”来自 license and services 的 94.5% 毛利率；但增量收入来自 product solutions 的放量，导致综合毛利率下降。2025 年产品毛利率从 46.4% 降到 34.5%，公司解释包括为部分客户供应域控制器等非核心集成硬件，剔除此影响后 adjusted product GM 约 42.5%。这意味着毛利率下滑不全是商品化，但价格竞争确实存在。

### 4.3 经营指标

| 指标 | FY2025 |
|---|---:|
| Journey 系列车规级处理硬件出货 | 4.01M 套，+38.8% |
| NOA-capable 硬件出货占比 | 45% |
| NOA-capable 出货量 | 约为 2024 的 4.8x |
| ASP / 单车价值量 | +75%+ |
| 生态伙伴交付占比 | >95% |
| 新增 design wins | 110+ |
| HSD design wins | 10 个 OEM 品牌、20+ 车型 |
| HSD 量产 | 2025 年 11 月进入量产，一个多月交付 22,000+ 套 |
| HSD 车型销量结构 | HSD 装配版本占相关车型销量 83% |
| HSD 用户 AD mileage rate | 2026 春节期间 41% |
| 出口车型定点 | 11 家车企、40+ 出口车型、生命周期 2M 套 |
| 海外市场定点 | 3 家全球车企，经 2 家国际 Tier-1，生命周期 10M 套 |

### 4.4 重点问题验证

**1. 地平线是平台，还是汽车零部件供应商？**  
是混合体。license/services 51.4% 收入、94.5% 毛利率、>95% 出货经生态伙伴交付，说明它不是普通零部件商；但 product solutions 已升至 43.2% 收入，且毛利率 34.5%，说明规模化收入越来越像汽车供应链交付。最准确说法：地平线是智能驾驶“计算平台 + IP/软件授权 + 生态伙伴交付”的平台型 Tier-2/Tier-1.5。

**2. 放量导致毛利率下降，是否能被规模抵消？**  
短期可以部分抵消：FY2025 gross profit +31.7%，说明放量没有把 gross profit 打没。但还不能抵消 R&D：R&D expense +63.3%，R&D/revenue 从 132.4% 升到 137.1%。真正的拐点不是 gross margin，而是 R&D 费用率能否随收入放大下降。

**3. 车厂自研是否会削弱地平线？**  
会，但不是一刀切。高端车型和具备软件组织的车企更倾向自研或深度自研；成本敏感的主流车型、合资品牌、出海车型更可能采用外采或混合方案。地平线在 RMB200,000 以下主流 NOA 市场 44.2% 份额，说明它目前吃到“智驾平权”的外采红利。风险是：若自研下沉到 100,000-200,000 元价位，地平线的 ASP 和产品毛利率会被压。

**4. 三年内真正贡献收入的是 L2/L2+/NOA，还是 L3/L4？**  
三年内是 L2/L2+/NOA。HSD、Journey 6、城市 NOA、主流车型下沉是收入主线。L3/L4/Robotaxi 是技术期权，公司计划 2026 Q3 与生态伙伴开展 Robotaxi 试运营，但不能作为三年财务模型的基线。

**5. 是否具备全球化能力？**  
具备早期证据，但未进入收入验证期。出口车型定点和全球车企经 Tier-1 定点说明能力存在；但生命周期定点不等于短期收入，仍需看海外 SOP、量产节奏、认证、售后与本地法规适配。

### 4.5 竞争格局

| 竞争方 | 对地平线的影响 |
|---|---|
| 华为车 BU | 在中国高阶智驾心智强，生态封闭但品牌强，是中高端最大压力源之一。 |
| Momenta / DJI 卓驭 | 算法与方案竞争，尤其在 NOA 普及阶段争 OEM 项目。 |
| 黑芝麻智能 | 国产智驾芯片竞品，压力在成本和国产替代口径。 |
| NVIDIA DRIVE | 高端算力与全球生态强，但成本和国产供应链环境给地平线留空间。 |
| Qualcomm | 舱驾融合和汽车 SoC 能力强，是地平线 Agentic CAR SoC 的关键对照。 |
| Mobileye | 全球 ADAS 传统强者，但中国本土 NOA 迭代速度给地平线窗口。 |
| 车厂自研 | 最大长期变量。自研成功会压外采 ASP；自研失败或成本过高则强化地平线生态位。 |

### 4.6 支持证据、反证、待验证信号

| 类型 | 内容 |
|---|---|
| 支持证据 | 收入 +57.7%；gross profit +31.7%；Journey 出货 4.01M；NOA-capable 占比 45%；ASP +75%+；license/services GM 94.5%；主流 NOA 市场 44.2% 份额。 |
| 反证 | 综合 GM 从 77.3% 降到 64.5%；product solutions GM 34.5%；R&D/revenue 137.1% 且未下降；adjusted operating loss 扩大；L3/L4 尚无财务贡献。 |
| 待验证信号 | HSD 2026 出货量与 ASP；product GM 是否回升至 40%+；license/services 是否维持 >35% 收入占比；R&D/revenue 是否降至 <90%、再降至 <60%；海外定点 SOP 与实际收入。 |

### 4.7 地平线估值反推

市场快照：9660.HK 约 HK$5.01，市值约 HK$73.3B。按粗略汇率换算约 RMB66-68B；三年翻倍约 HK$146.7B / RMB133B 左右。

| 反推项 | 需要达到的状态 |
|---|---|
| 三年后市值 | 约 HK$147B / RMB133B |
| 需要 revenue | RMB10-14B。若市场给 10-13x sales，需要 revenue 至少 RMB10-13B；若增长仍高且亏损收窄，可容忍更高 P/S。 |
| 需要 gross profit | RMB6-8B，假设 blended GM 58-62%。 |
| 需要 EBITDA / net income | 至少接近 adjusted operating breakeven；更好状态是 adjusted EBITDA 为正、adjusted net loss < RMB1B。 |
| 合理估值倍数 | 高增长硬科技平台可给 10-13x sales 或 18-22x gross profit；若 R&D 费用率不降，倍数应下修。 |
| 路径是否现实 | 有可能，但当前估值已定价高增长。需要 3 年 40-55% revenue CAGR，同时 R&D 费用率显著下降。 |
| 最敏感变量 | HSD 出货、NOA 渗透率、ASP、product GM、license/services 占比、R&D cloud/training cost、OEM 自研。 |

地平线的一句话：需求是真的，位置也好，但“平台收费权”还在和“汽车供应链价格压力”拔河；三年翻倍必须同时发生收入高增和费用率下降。

## 5. Oracle 轻记录验证器

主要来源：

- [Oracle FY2026 Q3 financial results](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Fiscal-Year-2026-Third-Quarter-Financial-Results/default.aspx)
- [Oracle Q3 FY2026 financial tables PDF](https://s23.q4cdn.com/440135859/files/doc_financials/2026/q3/Q326_Form8K_Exhibit99-1_Earnings_Release_Tables_FINAL-V1.pdf)

### 5.1 验证问题

| 问题 | 证据 | 判断 |
|---|---|---|
| OCI 增长是否真实 | Q3 FY2026 Cloud Infrastructure revenue $4.9B，+84% USD；total cloud revenue $8.9B，+44%。 | 真实。 |
| RPO 能否转化为收入 | RPO $553B，+325% YoY，+ $29B QoQ；公司 FY2027 revenue guidance 提高到 $90B。 | 转化有基础，但取决于 data center/GPU 交付。 |
| AI 合同是否压低 FCF | FY2026 Q3 TTM operating cash flow $23.5B，但 capex $48.25B，TTM FCF $(24.7)B；FY2026 capex 指引 $50B。 | 是，AI 云增长高度资本密集。 |
| Database / Autonomous / Multicloud 是否重新增长 | Q3 Oracle Cloud Database IaaS +35%；Multicloud Database +531%。 | 数据库在 multicloud/AI 场景下重新变成增长资产。 |
| 是否证明“数据库 + AI 云 + 企业关键工作负载”有长期价值 | 大额 RPO、OCI 增长、数据库 multicloud 增长同时出现。 | 是，但同时证明这个价值会吞噬现金流。 |

Oracle 对本报告的意义：它支持 Circle、BTGO、地平线共同的底层命题，即关键基础设施在 AI/数字资产/智能驾驶时代仍能收费；但它也提醒，基础设施扩张常伴随高 capex 或高 R&D，利润留存不能默认发生。

## 6. 三年翻倍反推模型

| 标的 | 当前市值 | 翻倍市值 | 需要的 revenue | 需要的 gross profit / EBITDA / net income | 合理估值倍数 | 路径现实性 | 最敏感变量 |
|---|---:|---:|---|---|---|---|---|
| BTGO | 约 $0.46B | 约 $0.93B | reported revenue 不关键；economic gross contribution $280-350M | adjusted EBITDA $75-90M，或 net income $45-60M | 10-12x EBITDA / 15-20x earnings | 有赔率，证据不足 | digital asset margin、normalized AoP、stablecoin net contribution、crypto beta |
| Circle | 约 $21.4B | 约 $42.8B | revenue/reserve income $5.5-6.5B；RLDC $2.3-2.8B | adjusted EBITDA $1.3-1.6B；net income $1.0-1.3B | 25-32x EBITDA / 30-40x earnings | 有条件现实 | USDC float、reserve yield、Coinbase/渠道分成、监管、USDC on-platform ratio |
| 地平线 | 约 HK$73.3B | 约 HK$146.7B | RMB10-14B | gross profit RMB6-8B；adjusted operating loss 接近 break-even | 10-13x sales / 18-22x gross profit | 有可能但不便宜 | HSD 出货、product GM、license/services 占比、R&D 费用率、OEM 自研 |

模型底线：如果只能靠收入讲故事，不靠 gross profit / EBITDA / net income，三年翻倍不成立。

## 7. 支持证据 / 反证 / 待验证信号表

| 标的 | 支持证据 | 反证 | 待验证信号 |
|---|---|---|---|
| BTGO | 客户数 +42%；normalized AoP +29.4%；subscriptions/services +56.9%；OCC national trust bank；Q1 margin 改善。 | reported revenue 被 gross accounting 放大；stablecoin sponsor fees 吃掉收入；actual AoP 下滑；net loss 受 BTC treasury 影响。 | RWA revenue、stablecoin net contribution、derivatives margin、subscriptions/services 连续高增、净流入披露。 |
| Circle | USDC flow 和 transaction volume 高增；Q1 adjusted EBITDA $151M；GENIUS Act 提供监管清晰度；other revenue 翻倍。 | reserve income 占比高；利率下行会压收入；Coinbase/渠道分成高；银行/交易所/支付公司可能进入。 | USDC avg float、reserve return rate、RLDC margin、on-platform ratio、CPN/Arc 真实收入、分销成本率。 |
| 地平线 | 收入 +57.7%；Journey 出货 4.01M；NOA 出货近 5 倍；license/services GM 94.5%；主流 NOA 份额高。 | product GM 下滑；R&D/revenue 137.1%；adjusted loss 扩大；L3/L4 仍是期权；车厂自研压价。 | HSD SOP 与出货、product GM >40%、R&D/revenue 下降、海外收入、license/services 占比。 |
| Oracle | OCI +84%；RPO $553B +325%；database cloud 和 multicloud database 高增；FY2027 revenue guide $90B。 | TTM FCF -$24.7B；capex $50B；RPO 需要数据中心和 GPU 交付；债务/融资压力上升。 | RPO revenue conversion、capex/OCF ratio、OCI gross margin、database cloud growth 是否持续。 |

## 8. 投资池结论

### 核心候选池

**Circle / CRCL**  
理由：收费权最清晰，需求和收入闭环最完整。它不是最便宜，但最像真正的基础设施收费资产。进入核心候选池的前提是价格纪律：若市值显著高于 $25-30B，而 USDC float 或 RLDC margin 没有同步上修，赔率会变差。

### 观察池

**地平线机器人 / 9660.HK**  
理由：需求真实，平台属性存在，NOA 放量强；但估值已经不低，利润留存尚未验证。观察的核心不是收入，而是 product GM 与 R&D 费用率。

### 证据不足池

**BTGO / BitGo**  
理由：便宜、有合规地位、有机构客户增长、有稳定币收入线，但 RWA 收入缺证据，stablecoin 净留存过薄，digital asset sales reported revenue 容易误导。它适合作为“高赔率跟踪对象”，还不适合作为高确信核心仓。

### 剔除池

**Oracle / ORCL（从本轮三年翻倍核心池剔除，仅保留趋势验证器）**  
理由：Oracle 基础设施收费权很强，但市值体量巨大、AI capex 正在显著压低 FCF，本报告不把它作为 BTGO/Circle/地平线同一赔率层级的候选。它的用途是验证：AI 云 + 数据库 + 企业关键工作负载仍然有长期价值。

