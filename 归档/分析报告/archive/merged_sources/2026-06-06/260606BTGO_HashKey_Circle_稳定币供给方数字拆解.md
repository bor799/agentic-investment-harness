---
title: "260606BTGO_HashKey_Circle_稳定币供给方数字拆解"
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
legacy_path: "分析报告/archive/merged_sources/2026-06-06/260606BTGO_HashKey_Circle_稳定币供给方数字拆解.md"
migration_target: "05_EVIDENCE_META/EVIDENCE/THEMES"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# BTGO / HashKey / Circle：稳定币供给方数字拆解

更新日期：2026-06-06  
主题：收入来源、成本结构、财务质量、供给稀缺性、需求爆发条件  

## 0. 一句话结论

你的核心判断方向是对的：未来稳定币和链上结算需求大概率继续扩张，供给端的合规基础设施会变稀缺。但三家公司不是同一种供给。

| 公司                 | 最像什么                                  | 供给质量          | 数字结论                                                                              | 投资位置                |
| ------------------ | ------------------------------------- | ------------- | --------------------------------------------------------------------------------- | ------------------- |
| Circle / CRCL      | 链上美元发行方 + 储备收益权 + 结算网络                | 最高            | Q1 2026 收入 94% 来自储备收益；USDC 规模和链上交易已验证需求，但渠道分成和利率是硬约束                              | 核心候选，但必须看利率和价格      |
| BitGo / BTGO       | 机构数字资产托管、钱包、交易、staking、稳定币白标基础设施      | 中等，未证明定价权     | FY2025 $16.15B revenue 主要是交易总额会计口径；真正要看经济毛利、subscriptions/services、stablecoin 净留存 | 小仓位期权，不能当已验证好生意     |
| HashKey / 03887.HK | 香港合规交易、托管、资管、RWA/tokenisation、稳定币结算入口 | 区域政策稀缺，但未转成盈利 | FY2025 收入 HK$723M 基本零增长，净亏 HK$1.08B；稳定币交易占比是需求信号，不是收费权证据                          | 观察池，等 RWA/稳定币收入进入报表 |

更锋利一点说：**长期看 Circle，短中期看 BTGO 的弹性，这个框架可以成立；但 BTGO 只能用“证据改善”买，不能用“收入很大”买。HashKey 是香港政策期权，不是现在已经转起来的利润机器。**


## 1. 先把“收入”拆干净

### 1.1 Circle：核心收入是稳定币储备收益

Circle 的公式非常干净：

USDC/EURC 流通量 x 储备收益率 = reserve income  
reserve income - Coinbase/渠道分成/交易成本 = revenue less distribution costs  
再扣运营费用 = EBIT / 净利润

白话流程是：

```text
客户/机构把 1 美元打给 Circle
-> Circle 铸造 1 个 USDC
-> 这 1 美元进入隔离储备，主要放在银行现金和 Circle Reserve Fund
-> USDC 在交易所、钱包、支付、RWA、跨境结算里流通
-> USDC 本身不给持有人利息
-> 储备资产产生的利息先进入 Circle 的 reserve income
-> Circle 再把一大部分分给 Coinbase、Binance 等分销/生态渠道
-> 用户赎回时交回 USDC，Circle 销毁 USDC 并退回美元
```

所以你的理解基本对：**流通多少 USDC，背后就应该有多少等值美元或短期美元资产。** 但它不是“无限发行”，而是“需求驱动的弹性发行”：只有客户存入合格美元资产、通过合规流程，Circle 才能铸造；客户赎回时，USDC 数量会收缩。

关键数字：

| 指标                                        |    FY2025 |     Q1 2026 | 解释                                  |
| ----------------------------------------- | --------: | ----------: | ----------------------------------- |
| Total revenue and reserve income          |   $2.747B |       $694M | 主体是储备收益                             |
| Reserve income                            |   $2.637B | 约占总收入 94.0% | 公司自己披露 Q1 2026 仍高度依赖 reserve income |
| Other revenue                             |     $110M |     约占 6.0% | 支付、平台、服务等还很小                        |
| Distribution, transaction and other costs |   $1.664B |       $407M | 主要是渠道、分销、交易相关成本                     |
| Adjusted EBITDA                           |     $582M |     约 $151M | 经营质量比 GAAP 净利润更能看主业                 |
| USDC 期末流通量                                | 约 $75B 以上 |        $77B | Q1 2026 平均 USDC 流通量同比 +39%          |
| USDC 链上交易量                                |         - |      $21.5T | Q1 2026 同比 +263%，说明使用强度在上升          |

Circle 的好处是：需求已经进报表。坏处是：**这不是纯软件网络，收益率和渠道分成会把利润弹性吃掉。**

最重要的==利率敏感性==：最新 Q1 2026 10-Q 口径是，若利率从 2026 年 3 月平均 3.49% 变化 100 bps，未来 12 个月 reserve income 约变化 $773M，distribution and transaction costs 约变化 $384M。也就是说，**100 bps 的降息，对净留存大约是 $389M 年化逆风**。旧的 FY2025 10-K 口径是 2025 年 12 月平均 3.64%，对应 $756M / $369M / $387M；差异约 2%-4%，不改变结论。降息能不能利好 Circle，取决于 USDC 流通量能不能用更快增长抵消单位收益率下降。

这里要把非农和美联储说清楚：

| 宏观变量 | 对 Circle 的第一层影响 | 第二层影响 | 投资者怎么读 |
|---|---|---|---|
| 非农很强 | 市场会预期利率更高、更久 | 储备收益率更好，但风险偏好可能被压制 | 对 Circle 不一定单向利好，要看 USDC 流通量有没有被高利率吸走 |
| 非农转弱但不是衰退 | 降息预期上升，储备收益率下行 | crypto/RWA/跨境支付风险偏好可能回升 | 对 Circle 的关键是流通量增长能否抵消利率下降 |
| 非农很差、衰退风险上升 | 利率下行，交易和支付活动也可能变弱 | reserve income 和流通量可能一起受压 | 这是最差组合 |
| 美联储加息或高利率维持 | 单位 USDC 储备收益更高 | 持有人可能赎回 USDC，转去买货币基金、短债、存款吃利息 | 只有在 USDC 存量不被取走、渠道分成不恶化时，才是净利好 |

所以“加息对 Circle 有益”必须带前提：**USDC float 不流失，且 Coinbase/Binance 等渠道没有拿走更多分成。** Circle 不是简单利率股，它更像“美元储备收益率 x 稳定币流通量 x 渠道净留存率”的乘法。

Coinbase 和 Binance 的关系也要分清：Coinbase 不是 Circle 子公司，而是最核心的分销和生态合作方；Binance 是 Circle 披露的分销/生态参与方之一。Q1 2026 Circle 对 Coinbase 的 distribution costs 是 $330.6M，而当季全部 distribution, transaction and other costs 是 $407M，说明渠道确实拿走了很大一块经济利益。交易所会不会拿走主要收益？答案是：**会拿走很大一块，尤其 Coinbase；但不是全部。** Circle 真正能留下的是扣完渠道、链上交易成本、其他直接成本之后的 RLDC。

### 1.2 BitGo：表面收入巨大，但不能按 SaaS 看

BitGo 的收入表面很大，但会计口径有噪音。FY2025 total revenue $16.152B，其中绝大多数是 digital asset sales revenue 的总额确认。

更适合看的不是 reported revenue，而是经济贡献：

| FY2025 业务线               |        收入 |              直接成本/费用 |       粗略经济贡献 | 判断                        |
| ------------------------ | --------: | -------------------: | -----------: | ------------------------- |
| Digital asset sales      | 约 $15.58B |             $15.545B |     约 $32.9M | 规模很大，毛利率约 0.21%，更像过账/交易价差 |
| Staking                  |   $385.0M | $344.5M staking fees |       $40.5M | 有需求，但受资产价格和 staking 余额影响  |
| Subscriptions & services |   $121.5M |            未单独披露直接成本 | $121.5M 收入口径 | 最像高质量服务收入                 |
| Stablecoin-as-a-Service  |    $66.7M |  $64.0M sponsor fees |        $2.7M | 有战略位置，但当前净留存极薄            |
| Interest income          |     $1.5M |                    - |           很小 | 不是主线                      |

所以 BitGo 的真实问题是：**它到底是机构数字资产基础设施，还是交易活动的低毛利放大器？**

先把几个看不清的词翻译成人话：

| 词                          | 具体在做什么                                                      | 收入怎么来                             | 应该看哪个数字                                       |
| -------------------------- | ----------------------------------------------------------- | --------------------------------- | --------------------------------------------- |
| Subscriptions and services | 钱包、托管接口、机构账户、借贷相关利息/费用、Crypto-as-a-Service、WBTC mint/burn 等 | 平台访问费、钱包解决方案费、贷款利息和费用、WBTC 发行/赎回费 | 这条最像可重复服务收入，FY2025 $121.5M                    |
| Digital asset sales        | 帮客户买卖/交割数字资产，收入按交易总额 gross 进表                               | 交易额很大，但成本也几乎等额进表                  | 看 economic contribution，不要只看 reported revenue |
| Staking                    | 帮客户把 PoS 资产质押赚奖励                                            | 奖励收入减去分给客户/验证相关方的 staking fees    | 看 assets staked、staking fee 后的净留存             |
| Stablecoin-as-a-Service    | 帮机构发行和管理美元稳定币，包括 token issuance、智能合约、储备托管/管理、审计、赎回和交易处理     | 实施费、持续服务费、储备收益分成                  | 看 sponsor fees 占比和净贡献                         |
| Crypto-as-a-Service        | 给支付平台、金融科技、金融机构接入钱包、托管、交易、出入金、监管报告等模块                       | 平台访问费和使用量费用                       | 当前还早，10-K 披露 active clients 少于 10 个           |

这里容易误解的一点是：BitGo 的稳定币收入不是“链上 gas 费”。链上交易费通常是网络成本或客户成本，==真正能成为 BTGO 收入的是白标稳定币的实施费、储备管理费、交易处理费、平台接入费，以及可能的储备收益分成==。FY2025 它的 Stablecoin-as-a-Service revenue 是 $66.7M，但 sponsor fees 是 $64.0M；Q1 2026 这项收入增加 $38.2M，同时 sponsor fees 增加 $35.3M。也就是说，**业务位置有价值，但当下大部分储备收益被 sponsor/客户/合作方拿走，BitGo 留下来的很薄。**

客户数也不能直接理解成“银行客户”。Q1 2026 客户从 3,900 增至 5,500 是亮点，但这些客户可能是机构、金融科技、支付平台、交易机构、企业 treasury、开发者/平台、也可能有高净值或零售相关客户。它不等于“5,500 家银行准备发稳定币”。截至 FY2025 10-K 日期，BitGo 披露只有 1 个 active Stablecoin-as-a-Service client，Crypto-as-a-Service active clients 少于 10 个。所以客户增长是真需求信号，但稳定币发行客户还没有规模化。

BitGo 的主线也不是“只要存的 Bitcoin 越多，利润就一定越高”。托管资产越多，会提高潜在收费底盘和交叉销售机会，但报表没有把 custody fee 单独拆得很干净。当前真正要排序是：digital asset sales 最大但毛利很薄；subscriptions/services 最像高质量收费权；staking 有资产价格和收益率周期；Stablecoin-as-a-Service 战略位置好但净留存很薄。预测市场、tokenized equities、RWA、链上衍生品如果规模化，理论上会需要托管、钱包、清算、结算和交易接口，可能利好 BitGo；但在报表里还没有形成单独可验证收入线。

Q1 2026 的最新数字让判断更谨慎：

| 指标                 |  Q1 2025 |  Q1 2026 | 判断                       |
| ------------------ | -------: | -------: | ------------------------ |
| Total revenue      |  $1.775B |  $3.774B | 表面增长很强                   |
| Net loss           | $(25.7)M | $(60.7)M | 亏损扩大                     |
| Adjusted EBITDA    |    $3.9M |  $(1.7)M | 主业调整后也承压                 |
| Assets on Platform |   $90.5B |   $63.0B | 实际 AoP 同比 -30.4%，主要受币价影响 |
| Clients            |    3,900 |    5,500 | 客户增长是真亮点                 |
| AoP 中 Bitcoin 占比   |        - |    50.1% | BTGO 确实是 Bitcoin beta    |

这里要把 AoP 口径标清：$90.5B 是 Q1 2025 同比列，不是 FY2025 年末。BitGo FY2025 10-K 披露的 2025 年 AoP 是 $81.6B，2024 年是 $89.9B；Q1 2026 再降到 $63.0B。

BitGo 自身也披露：Q1 2026 时 Bitcoin 是 AoP 最大单一资产，约占 AoP 50.1%。另外公司 treasury 持有 Bitcoin，FY2025 末持有 1,673 BTC；50% 的 BTC 公允价值变化会对 FY2025 净利润造成约 $73.2M 影响，Q1 2026 口径约 $83.6M。  
这解释了你的直觉：**BTC 涨飞，BTGO 会跟；但这首先是 beta，不是护城河利润。**

BitGo 有没有自己的链？截至这份报告使用的披露，BitGo 更像“钱包、托管、交易、结算、白标发行基础设施”，不是靠一条公共 L1/L2 公链赚钱。它有 proprietary settlement network，也就是 Go Network，用于机构之间更快结算；它的 Stablecoin-as-a-Service 和 Crypto-as-a-Service 则是给机构提供发行、储备管理、钱包、托管、交易、出入金和监管报告模块。所以 BTGO 的激发点不是“公链 token 涨”，而是：

1. BTC/crypto 价格上涨带来 AoP、交易、staking 和 treasury 公允价值弹性。
2. 客户数增长转成多产品使用，而不是只开户。
3. Subscriptions/services 增长，说明托管/钱包/合规接口变成收费权。
4. Stablecoin-as-a-Service 的 sponsor fees 占比下降，说明白标稳定币不再只是过账。
5. RWA/tokenized assets 需要托管、钱包、结算、发行和二级交易，相关收入开始单独或间接进入 subscriptions/services、custody、transaction revenue。

### 1.3 HashKey：稳定币占比是信号，但收入还没兑现

HashKey 的供给位置在香港：合规交易所、托管、经纪、资管、on-chain services、RWA/tokenisation、HashKey Chain。这些位置有政策稀缺性，但 FY2025 报表还没有证明它能把位置变成高质量利润。

关键数字：

| 指标                   |    FY2024 |    FY2025 | 判断                       |
| -------------------- | --------: | --------: | ------------------------ |
| Revenue              | HK$720.7M | HK$723.1M | 几乎零增长                    |
| Cost of revenue      | HK$188.2M | HK$314.6M | +67.2%，展业/交易/链上服务等直接成本上升 |
| Gross profit         | HK$532.5M | HK$408.5M | -23.3%                   |
| Gross margin         |     73.9% |     56.5% | 直接变现效率下降，需要看是否换来渠道权和资产规模 |
| Net loss             | HK$1.190B | HK$1.084B | 仍大亏                      |
| Cash and equivalents |         - |  HK$2.81B | IPO 后现金改善                |

业务结构：

| FY2025 业务 | 收入 | 占比 | 判断 |
|---|---:|---:|---|
| Transaction facilitation services | HK$522.8M | 72.3% | 核心收入，但增长不强 |
| On-chain services | HK$83.2M | 11.5% | 受 staking yield 和资产规模影响 |
| Asset management services | 约 HK$117M | 16.2% | 比重提升，是更值得跟踪的线 |

校验备注：Transaction facilitation services 的 HK$522.8M 是 FY2025 正确披露数；FY2024 是 HK$517.8M。两年很接近不是错标，而是这条收入只增长 1.0%。

HashKey 最值得注意的是“稳定币交易量占比接近一半”这一类结构信号。它说明平台上的结算资产正在稳定币化，但注意：**交易量占比不是收入占比，更不是毛利占比。**  
如果稳定币只是低费率过账，它会制造交易量但不制造利润。HashKey 要证明的是：稳定币、RWA、tokenised funds 能不能带来托管费、发行费、交易费、资管费和结算费，而不只是漂亮的 volume。

给金融小白的 HashKey 白话版：它现在不是单纯“币圈交易所”，更像香港合规数字资产入口，业务分三块。

| 业务 | 像传统金融里的什么 | HashKey 做什么 | 怎么赚钱 | 现在的问题 |
|---|---|---|---|---|
| Transaction facilitation | 券商 + 交易所 + OTC 柜台 | 帮客户交易数字资产、撮合、结算、托管 | 交易费、价差、托管/结算相关收入 | FY2025 收入 72.3% 来自这里，但只增长 1.0% |
| On-chain services | 托管行 + 质押服务商 + 上链服务商 | staking、tokenisation、HashKey Chain、链上结算 | staking fee、tokenisation fee、链上服务费 | FY2025 收入下降 33.3%，主要还是 staking |
| Asset management | 基金管理公司 | VC fund、数字资产基金、多资产/RWA 产品 | 管理费、业绩费 | 占比提升，但还没证明能覆盖集团亏损 |

你说的东南亚扩展是存在的。HashKey 年报写得比较明确：它已经在日本、香港、新加坡、迪拜、百慕大等地取得数字资产业务牌照或布局，并计划通过 exchange alliance 与关键国家的持牌交易所合作，整合东南亚流动性、加强区域 footprint、建设 pan-Asian liquidity network。投资含义是：**HashKey 想做亚洲合规数字资产流动性的区域入口。**

但“虹吸东南亚资金”现在还只能算假设，不是已验证事实。FY2025 报表能证明的是：

| 已验证事实 | 数字 | 读法 |
|---|---:|---|
| 香港交易量上升 | HK$530.0B，FY2025 同比 +72.3% | 香港主场变强 |
| 机构交易量上升 | HK$431.0B，FY2025 vs FY2024 HK$273.7B | 机构需求更重要 |
| Omnibus 客户交易量上升 | HK$86.4B，FY2025 vs FY2024 HK$11.7B | 通过持牌金融机构/综合账户导流有效 |
| 稳定币占数字资产交易量 | 48.0% | 结算资产稳定币化 |
| 平台资产 | HK$18.4B，峰值超过 HK$20.0B | 客户资产池扩大 |
| RWA value | HK$2.0B，11 个 tokenised products | RWA 在跑，但规模仍小 |

中国资金是不是主力？这里要分清两个概念：

1. **中国资产出海/RWA 化**：这是更可验证的方向。2026-02-06 中国证监会发布《境内资产境外发行资产支持证券代币的监管指引》，依据银发〔2026〕42 号等规定，给“境内资产或相关现金流在境外发行代币化权益凭证”设了备案和监管路径。这说明政策从“完全灰区”变成“极窄合规通道”，对 HashKey 这种香港合规入口是需求催化。
2. **境内个人或企业资金自由借 HashKey 流入流出**：这个不能这么写成结论。42 号文和证监会指引强调的是严监管、备案、跨境投资、外汇、数据安全、网络安全等要求，不是放开境内资金绕道炒币。

所以更稳的投资表述是：**HashKey 可能受益于“中国资产 RWA + 香港合规发行/交易/托管 + 亚洲流动性分发”，但不是已经证明“中国资金自由进出 HashKey”。** 需求方向可能被政策验证了，规模化收费权还没被报表验证。

## 2. 谁的供给真的少？

稳定币供给不是一个层次，而是四层：

1. 发行牌照和储备管理：Circle 最强，银行和 Tether 也会竞争。
2. 分销和流动性：Coinbase、Binance、钱包、支付公司、银行渠道最关键。
3. 托管、钱包、结算、白标发行基础设施：BitGo、Fireblocks、Anchorage、Coinbase、银行自建都会争。
4. 区域合规入口和 RWA 分发：HashKey 在香港有位置，但区域依赖强。

| 层次             | 稀缺性 | 最受益者            | 备注                                 |
| -------------- | --- | --------------- | ---------------------------------- |
| 合规美元稳定币发行      | 高   | Circle          | 但 Tether、银行、PayPal、Stripe 体系会压估值上限 |
| 白标稳定币发行基础设施    | 中   | BitGo           | 小银行/机构可能外包，但服务费是否厚要验证              |
| 香港合规稳定币/RWA 入口 | 中高  | HashKey         | 牌照和政策窗口有价值，收入兑现还早                  |
| 交易/托管/钱包技术     | 中   | BitGo / HashKey | 功能可替代，客户集成和监管资质增加黏性                |

结论：**供给少成立，但不是所有供给都同样值钱。发行权最值钱；分销权很值钱；后台基础设施要靠规模和净留存证明；区域牌照要靠政策和成交闭环证明。**

## 3. 稳定币需求什么时候爆发？

截至 2026-06-06 读取 DefiLlama 口径，全球稳定币供给约 $314.8B，其中 USDT 约 $187.0B，占 59.4%；USDC 约 $75.6B，占 24.0%。这个规模已经不小，但相对全球支付、跨境贸易、短债、银行存款和货币市场基金仍很早。

真正的爆发不是“大家突然想买稳定币”，而是以下几件事同时发生：

### 3.1 监管从“不确定”变成“可申请、可审计、可经营”

美国 GENIUS Act 已经建立 payment stablecoin 监管框架，OCC 和 FDIC 在 2026 年推进具体规则。核心含义是：不是谁都能发，未来美国市场只有 permitted payment stablecoin issuer 能合法发行支付稳定币。  
香港方面，HKMA 稳定币发行人监管制度于 2025-08-01 生效，并在 2026 年开始出现首批牌照。这对 HashKey 这类香港入口是政策窗口。

监管清晰会同时产生两种效果：

- 利好头部合规供给：Circle、持牌银行、合规基础设施商。
- 稀释“发行稀缺性”：更多银行、支付公司、非银机构能申请，单纯发行可能红海化。

所以监管不是无脑利好。监管的真正利好对象是：**有分销、有流动性、有品牌、有合规运营能力的供给方。**

### 3.2 银行什么时候会发稳定币？

银行会在以下条件同时满足时发：

| 条件 | 触发点 | 对谁有利 |
|---|---|---|
| 合法性 | 许可路径、储备规则、审计披露、赎回责任明确 | Circle、银行、BitGo、HashKey |
| 防御需求 | 存款/客户结算关系被 Circle、Tether、PayPal、Stripe 抢走 | 银行自发或找 BitGo 白标 |
| 真实支付场景 | 跨境 B2B、24/7 settlement、交易所出入金、RWA 结算、AI agent 微支付 | Circle、支付网络、链上基础设施 |
| 成本收益 | 储备收益、客户留存、手续费、结算成本节约能覆盖合规成本 | 大银行自建，小银行外包 |
| 技术和风控 | 钱包、KYC/AML、制裁筛查、私钥安全、赎回流动性成熟 | BitGo / Fireblocks / Anchorage / HashKey |

小银行最可能找 BitGo 这类基础设施商，不是因为它们不想自己发，而是自己发的固定成本太高：牌照、储备、审计、AML、技术、保险、私钥、安全、链上监控都很重。  
但这并不自动等于 BTGO 高利润。FY2025 BitGo 的 Stablecoin-as-a-Service revenue $66.7M，sponsor fees $64.0M，净留存只有 $2.7M。它必须证明白标稳定币从“帮客户过账”变成“自己能留住服务费”。

RWA 对 BitGo 和 HashKey 的收入路径也不一样：

```text
资产上链/RWA 发行
-> 需要托管底层资产或数字凭证
-> 需要钱包、私钥、安全、合规、KYC/AML
-> 需要稳定币或法币出入金做结算
-> 需要二级市场交易和做市
-> 公司才能收托管费、发行服务费、平台接入费、交易费、结算费、资管费
```

所以 RWA 的收入不是凭空来的。对 BitGo，更可能落在托管、钱包、Crypto-as-a-Service、Stablecoin-as-a-Service、settlement rails；对 HashKey，更可能落在 tokenisation service、HashKey Chain、交易/OTC、资产管理和托管。**只有 RWA value 上升但没有收入分项增长，就还只是需求线索，不是利润线索。**

### 3.3 降息到底是利好还是利空？

分公司看：

| 情景                          | Circle                              | BitGo                           | HashKey         |
| --------------------------- | ----------------------------------- | ------------------------------- | --------------- |
| 降息但风险偏好不升                   | 利空，reserve yield 下行                 | 中性/偏弱                           | 中性/偏弱           |
| 降息 + crypto 牛市              | reserve yield 下行，但 USDC 流通量/交易量可能上升 | 明显利好，BTC beta、交易、AoP、staking 活跃 | 利好，交易/RWA 活跃    |
| 降息 + RWA/跨境支付爆发             | 中长期利好，USDC float 扩张可能抵消利率           | 利好白标发行和托管结算                     | 利好香港 RWA 与稳定币入口 |
| 高利率维持 + stablecoin float 增长 | 最利好 Circle                          | 对 BTGO 中性偏好                     | 中性              |

最关键的判断式：

**Circle：USDC 流通量增速 x 净留存率 > reserve yield 下滑幅度。**  
如果按 Q1 2026 口径，100 bps 降息带来约 $389M 年化净逆风，那么 USDC 要增长很多、且 distribution cost 不能恶化，Circle 才能把降息变成净利好。

**BTGO：BTC/crypto beta + 客户数增长 + economic gross contribution 扩大。**  
BTC 涨会让 AoP、交易活跃度、treasury 公允价值都变好，但要升级成好公司，必须看到 subscriptions/services 和 stablecoin net contribution 上台阶。

**HashKey：香港政策 + 稳定币交易 + RWA 发行/二级市场成交进入收入表。**  
只要还是 volume 好看、收入不长、毛利下滑，就只能叫政策期权。

## 4. 三家公司的质量排序

### 4.1 商业模式质量

Circle > BitGo > HashKey

Circle 已经有稳定币网络和储备收益闭环；BitGo 有机构基础设施位置但收费权未证明；HashKey 有区域牌照和 RWA 叙事但盈利路径更远。

### 4.2 短期弹性

BitGo > HashKey > Circle

BTGO 市值小、Bitcoin beta 强、预期低，只要几个指标改善，股价弹性可能最大。HashKey 受政策和港股流动性影响，弹性也有，但流动性和解禁/牌照风险更复杂。Circle 是更好生意，但市场已经更充分认识它。

### 4.3 数字可信度

Circle > BitGo > HashKey

Circle 的核心指标 USDC circulation、reserve income、RLDC、distribution costs 都能直接跟踪。BitGo 要把 gross revenue 改成 economic contribution 来看。HashKey 很多关键叙事，比如 RWA、稳定币交易、tokenisation，还需要收入分项进一步拆开。

## 5. 下一步只盯这些数字

### Circle 必盯

| 指标 | 好信号 | 坏信号 |
|---|---|---|
| Average USDC in circulation | 连续高双位数增长，突破 $100B 后不回落 | 两个季度停滞或被 USDT/银行币抢走增量 |
| Reserve return rate | 下降慢于预期，或被流通量增长抵消 | 降息导致 reserve income 明显下滑 |
| RLDC margin | 稳定或改善 | 渠道分成继续吃掉大部分收入 |
| Other revenue 占比 | 超过 10%，说明支付/平台收入长出来 | 长期停留在 5%-6%，仍是利率代理 |
| Coinbase 相关成本 | 占比下降或效率提升 | 继续成为利润天花板 |

### BitGo 必盯

| 指标 | 好信号 | 坏信号 |
|---|---|---|
| Subscriptions/services revenue | 连续 30%+ 增长 | 跌到 20% 以下 |
| Stablecoin-as-a-Service 净贡献 | sponsor fees 占比下降，净留存明显扩大 | revenue 增长但 sponsor fees 几乎全吃掉 |
| Economic gross contribution | 增长快于 reported revenue | reported revenue 高增但经济贡献不动 |
| Actual AoP vs normalized AoP | 同向增长，说明真实净流入 | actual AoP 只跟币价走 |
| Clients | 高增长且大客户多产品使用 | 客户增长放缓 |
| BTC treasury 敏感性 | 上涨带来资产负债表弹性 | 下跌吞掉净利润 |

### HashKey 必盯

| 指标 | 好信号 | 坏信号 |
|---|---|---|
| Revenue growth | 从零增长恢复到 30%+ | 继续零增长 |
| Gross margin | 回到 60%+ | 继续下滑 |
| Stablecoin 相关收入 | 单独披露并增长 | 只有交易占比，没有收入 |
| RWA/tokenised products 收入 | 发行、托管、二级交易产生可见 fee | 只有公告和叙事 |
| Asset management revenue | 占比提升且利润率好 | 规模增长但亏损扩大 |
| Cash burn | 亏损收窄，现金消耗下降 | IPO 现金被持续亏损快速消耗 |

## 6. 决策结论

1. Circle 是这组三家公司里最像“新时代 Visa/PayPal/银行混合体”的标的，但它还没有完全摆脱利率股属性。长期看它没问题，买点要看价格、USDC 流通量和 RLDC margin。
2. BTGO 是短中期最有弹性的标的，但现在还不是高质量基础设施资产。它确实会跟 Bitcoin 和 crypto 活跃度走，但这只是 beta。只有当 subscriptions/services、stablecoin 净留存、economic gross contribution 改善，才能说它从周期交易商变成收费权资产。
3. HashKey 是香港合规数字资产和中国资产 RWA 的政策期权。位置对，但数字没证明。稳定币交易占比是好信号，收入零增长和毛利下滑是坏信号。
4. “机构什么时候发稳定币”的答案不是单纯降息，而是监管许可、分销需求、防御压力、真实支付/RWA 场景、技术外包成本同时成熟。降息会提高风险偏好，但会压 reserve yield；所以要看总量增长能否跑赢单位收益下降。

我的当前排序：

| 用途          | 首选              |
| ----------- | --------------- |
| 好生意核心候选     | Circle          |
| 小仓位赔率期权     | BitGo           |
| 政策/RWA 观察期权 | HashKey         |
| 当前最需要数字验证   | BitGo 和 HashKey |

## 7. 来源

- BitGo FY2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/1740604/000174060426000020/btgo-form10xk.htm
- BitGo Q1 2026 Form 10-Q: https://www.sec.gov/Archives/edgar/data/1740604/000174060426000031/btgo-20260331.htm
- Circle FY2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/1876042/000187604226000062/crcl-20251231.htm
- Circle Q1 2026 Form 10-Q: https://www.sec.gov/Archives/edgar/data/1876042/000187604226000150/crcl-20260331.htm
- HashKey FY2025 annual results announcement: https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0327/2026032701352.pdf
- HashKey FY2025 annual report: https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0429/2026042902783.pdf
- HashKey financials cross-check: https://stockanalysis.com/quote/hkg/3887/financials/
- HKMA stablecoin issuer regime implementation: https://www.hkma.gov.hk/eng/news-and-media/press-releases/2025/07/20250729-4/
- CSRC 境内资产境外发行资产支持证券代币监管指引（2026-02-06）: https://www.csrc.gov.cn/csrc/c101954/c7614288/content.shtml
- OCC GENIUS Act proposed rule: https://www.occ.treas.gov/news-issuances/bulletins/2026/bulletin-2026-3.html
- FDIC GENIUS Act proposed rule: https://www.fdic.gov/news/financial-institution-letters/2026/notice-proposed-rulemaking-establish-genius-act
- DeFiLlama stablecoin supply data, accessed 2026-06-06: https://defillama.com/stablecoins


# 附录

## 0.4 AoP 是什么

AoP 是 Assets on Platform，直译是“平台资产”。对 BitGo 来说，它不是收入，也不是利润，而是客户在 BitGo 平台上的资产规模。BitGo 的定义是：统计期内每日平台资产余额的中位数，按当天市场价格计量，资产可以包括客户托管或非托管账户里的数字资产和少量法币。

投资上可以这么读：

```text
AoP = 未来可能收费的资产底盘
托管费/平台费 = AoP x take rate
交易收入 = AoP x 活跃度 x 交易费率/价差
staking 收入 = staked assets x staking yield x 分成
```

但 AoP 有一个大坑：它会被币价强烈影响。客户没有新增存入，只要 BTC 涨，AoP 也会涨；客户没有大规模赎回，只要 BTC 跌，AoP 也会跌。所以看 BTGO 时要同时拆两个问题：

| 问题 | 看什么 | 含义 |
|---|---|---|
| 是币价涨出来的，还是客户真流入？ | actual AoP vs normalized AoP | 只有 normalized AoP 同向增长，才更像真实净流入 |
| 是被动托管，还是变成收入？ | AoP、交易量、staking assets、subscriptions/services | 资产多但不交易、不质押、不买服务，收费权就弱 |
| BTC beta 有多大？ | AoP 中 Bitcoin 占比、公司自有 BTC 敏感性 | BTGO 会跟 BTC 走，但这不等于护城河 |

Q1 2026 的例子很典型：BitGo AoP 从 Q1 2025 的 $90.5B 降到 Q1 2026 的 $63.0B，同比 -30.4%，公司解释主要受数字资产价格下跌影响；同时 Q1 2026 AoP 中 Bitcoin 占 50.1%。所以这家公司确实有 Bitcoin beta，但投资者要继续追问：**币价上涨之外，它有没有把客户资产变成稳定收费权？**

HashKey 也有类似“平台资产”概念，但口径不完全等同于 BTGO 的 AoP。HashKey FY2025 平台资产 HK$18.4B、峰值超过 HK$20.0B，可以说明客户资产池变大；但同样不能直接等于收入和利润。它最终要落到交易费、托管费、tokenisation fee、资管费、稳定币/RWA 结算费。

## 0.5 投资者读财务的路径

看供给端公司，财务不是为了挑毛病，而是为了判断：==**这家公司有没有把行业需求转成自己能留住的钱。**==

基本路径：

```text
收入
-> 扣直接成本
-> 毛利 / 类毛利
-> 扣经营费用
-> 经营利润
-> 扣利息、税、投资/资产公允价值波动
-> 净利润
-> 再看现金流和估值
```

每一层回答的问题不同：

| 层级                                          | 看什么                | 回答什么问题       | 对投资判断的含义                                 |
| ------------------------------------------- | ------------------ | ------------ | ---------------------------------------- |
| Revenue / reported revenue                  | 表面收入               | 业务有没有规模      | 只能证明有流量/交易/资产，不等于赚钱                      |
| Gross profit / RLDC / economic contribution | 收入扣直接成本后留下多少       | 单位业务有没有变现效率  | 毛利率下降不一定坏，关键看是否换来渠道权、客户资产、流动性或更大收入池      |
| Operating expenses                          | 人工、研发、销售、管理、合规、技术等 | 公司为了扩张花多少钱   | 扩张期费用上升可以接受，但要看费用率和亏损是否逐步改善              |
| Operating income / adjusted EBITDA          | 主业经营结果             | 主业是否能自我造血    | 比净利润更能看经营质量，但要警惕调整项                      |
| Net income                                  | 最终会计利润             | 扣完所有项目后是否赚钱  | 受税、利息、股权激励、公允价值波动影响，尤其 BTGO 受 BTC 波动影响很大 |
| Cash flow                                   | 现金进出               | 利润是否变成现金     | 亏损公司尤其要看现金消耗速度                           |
| PE / P/S / EV/EBITDA                        | 估值                 | 价格是否已经提前反映终局 | 最后才看，不能先用低 P/S 证明便宜                      |

所以这里的判断规则是：

```text
毛利率下降 + 收入增长 + 毛利绝对额增长 + 客户/渠道权增强 + 经营费用率改善 = 可以接受的扩张成本

毛利率下降 + 收入不增长 + 毛利绝对额下降 + 费用率不改善 + 现金流恶化 = 需求没有转成收费权
```

这也是为什么 HashKey 的毛利率下降不能机械判死刑，但也不能直接忽略；要问它有没有用这部分成本换来稳定币渠道权、RWA 资产、机构客户和未来可留存收入。

## 数据校验摘要（2026-06-06 复核）

这次复核后的结论：Circle 和 BitGo 的核心数字高度可靠，主要问题是口径标注；HashKey 原先的 HKEX 来源链接指向了错误公司，已改为 HashKey 正确的 2026-03-27 年度业绩公告和 2026-04-29 年报，FY2025 关键数字可以验证。

| 公司      | 复核结果                                                 | 需要修正或标注的地方                                                                              |
| ------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Circle  | 财务主表、RLDC、USDC、Adjusted EBITDA 均可核对                  | 利率敏感性用最新 Q1 2026 10-Q 口径；FY2025 10-K 口径保留为旧口径对照                                         |
| BitGo   | 收入、成本、stablecoin sponsor fees、AoP、客户数均可核对            | $90.5B 是 Q1 2025 同比口径，不是 FY2025 年末；FY2025 年末 AoP 是 $81.6B                               |
| HashKey | FY2025 收入、毛利、费用、业务分项、RWA value、稳定币交易占比均已用 HKEX 原公告核对 | 经营费用需要拆开看，不能只用一个模糊的 total operating expenses；交易促成收入 HK$522.8M 是 FY2025 正确数，不是 FY2024 错标 |

| 原校验问题                   | 复核后处理                                                                                          |
| ----------------------- | ---------------------------------------------------------------------------------------------- |
| Circle 1 项利率敏感性有差异      | 改用 Q1 2026 10-Q 的 $773M / $384M / $389M；保留 FY2025 10-K 的 $756M / $369M / $387M 作为旧口径           |
| BitGo AoP $90.5B 容易被误读  | 标注为 Q1 2025 同比口径，并补充 FY2025 年末 AoP $81.6B                                                      |
| HashKey FY2025 15 项无法验证 | 找到正确 HKEX 年度业绩公告 `2026032701352.pdf` 和年报 `2026042902783.pdf` 后，FY2025 核心项目已可验证                 |
| HashKey 交易促成收入疑似错标      | 已确认 HK$522.8M 是 FY2025，FY2024 是 HK$517.8M；不是错标，而是只增长 1.0%                                      |
| HashKey 经营费用/经营亏损口径有差异  | 已把经营费用拆成 R&D、sales and marketing、G&A、other losses/gains，并修正 loss from operations 为 HK$(908.2)M |

### 新上市数据完整性限制

这三家公司都有一个共同问题：**上市后可观察的公开季度样本太短**，所以现在不能把所有指标都当成“稳定长期规律”。

| 公司 | 上市时间 | 数据完整性怎么读 |
|---|---|---|
| Circle / CRCL | 2025-06-05 在 NYSE 开始交易 | 已有上市前审计历史和上市后 10-Q，但公开市场下的连续季度还不够长；Q1 2026 只能说明当前经营质量，不足以证明降息周期下的完整弹性 |
| BitGo / BTGO | 2026-01-22 在 NYSE 开始交易 | 10-K 有 2023-2025 审计历史，但上市后只有很短季度样本；reported revenue、AoP、BTC beta 和新业务稳定性都需要继续看 2026 后续季度 |
| HashKey / 03887.HK | 2025-12-17 在 HKEX 主板上市 | 有 FY2025 年度业绩和年报，但作为上市公司可连续跟踪的季报/半年报样本仍少；RWA、稳定币、机构交易是否转成收入还需要至少 2-4 个报告期验证 |

所以这份报告的使用方式应该是：**用已有财报判断“当前质量”，用后续季度验证“趋势是否成立”。** 当前能下的结论是供给位置和收入质量判断，不是长期财务模型已经完全跑通。

## 0.6 三家公司财务路径补充

### Circle：毛利口径要看 RLDC

Circle 不像制造业那样披露传统 gross profit。最接近“类毛利”的指标是 RLDC，也就是 total revenue and reserve income 扣掉 distribution, transaction and other costs 后剩下的钱。

| 指标                                        |  FY2024 |  FY2025 | Q1 2025 | Q1 2026 | 读法                      |
| ----------------------------------------- | ------: | ------: | ------: | ------: | ----------------------- |
| Total revenue and reserve income          | $1.676B | $2.747B |   $579M |   $694M | USDC 储备收益和其他收入总盘子       |
| Distribution, transaction and other costs | $1.017B | $1.664B |   $348M |   $407M | Coinbase/渠道、交易、分销等直接成本  |
| Revenue less distribution costs / RLDC    |   $659M | $1.083B |   $231M |   $287M | 类毛利，最该跟踪                |
| RLDC margin                               |     39% |     39% |     40% |     41% | Q1 2026 小幅改善，不是直接恶化     |
| Total operating expenses                  |   $492M | $1.179B |   $138M |   $242M | FY2025 受 IPO 相关股权激励显著拉高 |
| Operating income                          |   $167M |  $(96)M |    $93M |    $45M | 会计经营利润受费用扩张影响           |
| Net income                                |   $157M |  $(70)M |    $65M |    $55M | FY2025 受股权激励等影响；Q1 仍盈利  |
| Adjusted EBITDA                           |   $285M |   $582M |   $122M |   $151M | 更能看主业现金经营质量             |

判断：Circle 的直接变现效率没有坏，RLDC margin 基本稳定；真正要盯的是降息后 reserve income 被压缩时，USDC 流通量和非利息收入能不能补上。

### BitGo：毛利要改成 economic contribution

BitGo 的 reported revenue 被 digital asset sales 总额确认放大。它更像“交易额入收入表”，所以不能直接按 SaaS P/S 看。

| 指标                                  |  FY2024 |   FY2025 | Q1 2025 | Q1 2026 | 读法                         |
| ----------------------------------- | ------: | -------: | ------: | ------: | -------------------------- |
| Total revenue                       | $3.081B | $16.152B | $1.775B | $3.774B | 表面收入很大，但多数是数字资产交易总额        |
| Digital asset sales cost            | $2.531B | $15.545B | $1.602B | $3.648B | 买入/交割数字资产的直接成本             |
| Staking fees                        |   $419M |    $345M |   $128M |    $41M | 支付给客户/验证相关方的 staking 分成    |
| Stablecoin sponsor fees             |       - |     $64M |       - |    $35M | 稳定币服务里付给 sponsor/发行支持方的费用  |
| 直接贡献，扣 DAS/staking/sponsor/interest | 约 $128M |  约 $188M |  约 $43M |  约 $43M | 比 reported revenue 更接近真实留存 |
| Compensation and benefits           |    $80M |    $104M |    $24M |    $41M | 人工和股权激励等                   |
| General and administrative          |    $53M |     $76M |    $16M |    $20M | 法务、专业服务、保险、技术、营销等          |
| Operating income                    |   约 $7M |    约 $4M |     $2M |  $(20)M | 主业经营层面 Q1 2026 转弱          |
| Net income / loss                   |   $157M |   $(15)M |  $(26)M |  $(61)M | 受 BTC/数字资产公允价值影响很大         |
| Adjusted EBITDA                     |     $3M |     $32M |     $4M |   $(2)M | FY2025 改善，Q1 2026 又承压      |

判断：BTGO 不是没有业务质量，而是还没证明“交易规模 -> 可留存收费权”。如果它为了获取白标稳定币客户、银行渠道、结算网络而牺牲短期毛利，可以接受；但必须看到 stablecoin sponsor fees 占比下降、subscriptions/services 增长、economic contribution 增长。

### HashKey：毛利率下降可以接受，但要换来收费权

HashKey 的报表更像扩张期平台：收入刚起来，合规、研发、销售、管理成本很重。FY2025 的好处是经营费用下降、亏损收窄；坏处是收入几乎不增长、毛利绝对额下降、自由现金流恶化。

| 指标 | FY2024 | FY2025 | 变化 | 读法 |
|---|---:|---:|---:|---|
| Revenue | HK$720.7M | HK$723.1M | +0.3% | 收入没有放量 |
| Cost of revenue | HK$188.2M | HK$314.6M | +67.2% | 展业、交易、链上服务、渠道和直接履约成本上升 |
| Gross profit | HK$532.5M | HK$408.5M | -23.3% | 毛利绝对额下降，这是需要解释的地方 |
| Gross margin | 73.9% | 56.5% | -17.4pct | 直接变现效率下降，但不等于公司一定坏 |
| R&D | HK$556.7M | HK$503.9M | -9.5% | 研发费用下降 |
| Sales and marketing | HK$390.1M | HK$374.8M | -3.9% | 销售营销费用小幅压降 |
| General and administrative | HK$633.0M | HK$376.6M | -40.5% | 管理费用下降明显，部分来自 FY2024 股权激励高基数 |
| Operating expenses, R&D + S&M + G&A | HK$1.580B | HK$1.255B | -20.6% | 经营费用纪律有改善 |
| Other losses/gains, net | HK$39.9M gain | HK$(61.3)M loss | 转弱 | 数字资产和汇兑等公允价值扰动 |
| Loss from operations | HK$(1.007)B | HK$(908.2)M | 收窄 9.8% | 主业经营亏损收窄，但仍很重 |
| Loss for the year | HK$(1.190)B | HK$(1.084)B | 收窄 8.8% | 仍大亏，但不是继续恶化 |
| Net operating cash flow | HK$(183.3)M | HK$(692.3)M | 恶化 | 现金消耗需要继续跟踪 |
| Estimated FCF, OCF - capex | HK$(188.9)M | HK$(695.8)M | 恶化 | 非公司披露指标，只作为现金消耗参考 |

判断：HashKey 的财务不是简单“公司有问题”，而是“位置对，收费权还没兑现”。如果毛利率下降是在换取稳定币交易入口、RWA 资产部署、机构渠道和未来二级交易流动性，可以接受；但下一阶段必须看到收入增长、毛利绝对额修复和经营现金流改善。这里要特别注意：费用表面压降是真实的，但经营现金流恶化也是真实的。
