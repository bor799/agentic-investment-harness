---
title: etf_lof_fund
date: 2026-07-23
updated: 2026-07-23
layer: METHOD
primary_role: etf_lof_fund
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: operational
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# ETF_LOF_FUND

## 职责

处理 ETF、LOF、基金和包装层路径。

## 输入

成分权重、目标 ETF、申赎规则、折溢价、证券借贷、经理口径、NAV。

## 输出

底层业务、包装层资金和交易路径的分账。

## 不能证明什么

分散不等于低风险，折价不等于底层便宜。

## 失败条件

无法验收持仓、申赎、券商路径、费用和退出深度。
