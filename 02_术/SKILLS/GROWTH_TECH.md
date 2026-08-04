---
title: growth_tech
date: 2026-07-23
updated: 2026-07-24
layer: METHOD
primary_role: growth_tech
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: operational
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260713AI_Token需求增长与稀缺性迁移投资框架.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/稳定币与财务指标概念路径.md
  - 02_术/SKILLS/METHOD_SOURCE_REVIEW_QUEUE/基础概念/交易策略组合/260624电解液_物理需求线性与利润估值非线性.md
---

# GROWTH_TECH

## 职责

处理高增长、未盈利或资本强度高的科技资产。

## 输入

TAM、RPO、ARR、订单、容量、利用率、毛利、SBC、CapEx、完全稀释股数。

## 输出

兑现阶梯、稀释风险、资本强度和单位经济。

## 不能证明什么

TAM、签约容量和调整后指标不能证明每股 FCF。

## 失败条件

需求热但交付、毛利、费用和现金流不能兑现。

## 兑现阶梯

高增长、未盈利或资本强度高的资产，按下面链路验收：

```text
需求或使用量
→ 付费客户和留存
→ 订单 / RPO / ARR / 交易量 / AUM / 托管资产
→ 收入确认
→ 毛利或 take rate
→ 经营费用和 SBC
→ 经营利润或亏损收窄
→ 经营现金流
→ 自由现金流
→ 完全稀释后每股价值
```

任何一步缺失，都不能用 TAM、用户热度、交易量、tokenised value、签约容量或调整后 EBITDA 直接证明每股 FCF。

## AI Token 资产检查

不要从“我用了更多 Token”直接跳到“所有 AI、半导体、机器人和储能都受益”。先看四组数字：

1. **用量：**付费 Token、AI 收入、客户留存，而不是赠送额度。
2. **效率：**每元、每度电、每张卡能生成多少 Token。
3. **供给和利润：**订单、利用率、售价、毛利率、库存和账期。
4. **终端 ROI：**企业用 AI 增加的收入或节约的成本能否覆盖 AI 账单。

只有使用量增速大于单位效率增速，且继续传导到供应商收入、毛利和现金流，才能提高经营票（H_B）。

## 稳定币 / RWA / 数字资产检查

稳定币和 RWA 先按业务路径拆：

```text
客户/机构发行或使用稳定币
→ 储备资产托管和管理
→ 交易所、钱包、支付、RWA 场景
→ 流通量、交易量和托管资产
→ 发行费、储备收益、托管费、交易费、结算费、服务费
→ 毛利 / sponsor fee / 运营费用
→ 净利润和现金流
```

白标稳定币和 Stablecoin-as-a-Service 有战略价值，但不天然高毛利。sponsor fee 越高，越像后台代工或通道商；sponsor fee 占比下降，才可能说明定价权增强。

RWA “在跑”不等于公司“在赚钱”。如果只有 tokenised value、资产展示或交易热度，没有单独收入、take rate、毛利和现金流，就仍是叙事。

## 输出格式

```yaml
growth_tech:
  demand_or_usage:
  payer_and_roi:
  revenue_bridge:
  gross_margin_or_take_rate:
  operating_cost_and_sbc:
  cash_conversion:
  dilution:
  supply_or_efficiency_offset:
  valuation_language:
  H_B: pass | mixed | fail | unknown
  next_number:
  failure_condition:
```

## 旧基础概念方法源吸收记录

已吸收 `260713AI_Token需求增长与稀缺性迁移投资框架.md`、`稳定币与财务指标概念路径.md` 和电解液利润非线性框架中的成长资产传导规则。保留 Token 到硬件/电力/利润的闸门、稳定币/RWA 收费权路径和每股现金流验证；不把使用量、资产规模、tokenised value 或 AI 叙事直接写成业务过票。
