---
title: "LMND交易方案 legacy source case"
date: 2026-07-24
updated: 2026-07-24
layer: CASE
primary_role: migrated_legacy_source_case
status: active
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
case_type: research_or_decision_source
settlement_status: not_executed_plan
settlement_rule: execution_required_before_pnl_settlement
review_date: 2027-01-16
legacy_path: "基础概念/实体商/LMND/LMND交易方案.md"
source_paths:
  - 基础概念/实体商/LMND/LMND交易方案.md
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# LMND交易方案 Legacy Source Case

## 先说人话

**今天发生了什么：**旧文件 `基础概念/实体商/LMND/LMND交易方案.md` 已抽成 Case Gym 来源卡，原文继续保留在旧路径。

**为什么重要：**这类材料往往混有公司判断、交易方案、情绪反应和方法观察。进入 Case Gym 后，它只能训练方法，不能直接升级成 MINDSET、Constitution 或交易授权。

**现在做什么：**原文交易记录为待执行，不能伪装成真实持仓或真实期权盈亏；只保留为期权方法测试样本。

## Source

| 字段 | 内容 |
|---|---|
| 原始文件 | [[LMND交易方案]] |
| 原始标题 | LMND交易方案 |
| 来源角色 | `legacy_company_case_source` |
| 旧层级 | `CASE` |
| 原权限 | `none` |

## Case Capture

| 项目 | 当前状态 |
|---|---|
| 事前判断 | 待从原文萃取 |
| 当时价格 / 估值语法 | 待从原文萃取 |
| 核心证据链 | 待从原文萃取 |
| 行为信号 | 待复盘 |
| 验证期限 | 如果真实执行 Jan 2027 Put，则到 2027-01-16 附近结算；未执行则不结算 PnL |
| 结算结果 | 未执行计划：原文交易记录写“待执行”；因此不能计算收益、胜率或方法有效性 |
| 可写入位置 | `04_CASE_GYM / 02_术 / METHOD_TESTS` |
| 不可写入位置 | `01_道/MINDSET / 01_道/CONSTITUTION / 当前交易授权` |

## Settlement Snapshot

| 项目 | 内容 |
|---|---|
| 事前日期 | 2026-03-02 / 2026-03-06 |
| 事前价格 | 约 $52 |
| 核心方案 | 正股 + 卖 Put，含 Jan 2027 $45 Put 等示例 |
| 执行事实 | 原文交易记录为 `待执行` |
| 后验价格事实 | 2026-07 中下旬 LMND 约 $67，若仅看价格，$45 Put 暂未进入价内；但没有成交事实，不能算收益 |
| 方法结论 | 旧文中“卖方统计优势”“重仓”“roll”等表述不得恢复授权；期权必须先有最大损失、现金担保、真实成交和退出规则 |

## Review Gate

1. 先确认这是实际交易、未成交、研究判断、错过机会还是情绪短记。
2. 再补 `business_horizon / thesis_horizon / execution_horizon / review_date`。
3. 只有形成跨案例稳定反例或方法修正，才允许进入 Skill 更新。
4. 即使形成候选哲学，也只能进入 Philosophy Inbox，不能自动进入 MINDSET。
