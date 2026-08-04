---
title: judgment_driven_harness_receipt_260727
date: 2026-07-27
updated: 2026-07-27
layer: META
primary_role: absorption_receipt
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: operational
data_cutoff: 2026-07-27
expires_at: 2026-10-25
source_paths:
  - 05_EVIDENCE_META/EVIDENCE/THEMES/260727系统_Murphy判断驱动Harness基线.md
---

# Murphy 判断驱动 Harness 交付回执

## 吸收三行

- **新东西是什么：**研究必须从“为什么研究”开始，分开 Murphy 判断与 AI 探索，并按资产类型选择最小证据路径。
- **改变了什么：**Harness、Reviewer 和 Validator 增加研究触发链、资产分型、用户正文去内部代码、unknown 可解决性和精确写入路由门禁。
- **写到哪里：**Automation 精确工程文件、主题 Evidence 基线，以及第一组六张 Current 卡。

## 完成内容

### 工程

- `90_AUTOMATION/PROMPTS/INVESTMENT_HARNESS.md`
- `90_AUTOMATION/PROMPTS/INVESTMENT_REVIEWER.md`
- `90_AUTOMATION/PIPELINES/validate_investment_output.py`
- `90_AUTOMATION/TESTS/test_investment_output.py`

新增机械门禁：

1. 正式写入必须 Reviewer `PASS`，且允许路径与目标路径精确一致；
2. Current 卡必须有研究触发链与 Murphy / AI 分账；
3. 资产类型必须匹配公司、资源、公用事业、资本结构载体或 ETF 路径；
4. 用户正文不得泄露内部票据代码；
5. 每个 unknown 必须包含缺口、重要性、验证办法、通过条件和失败条件；
6. 本轮新建文件可在写后复核中声明 `target_preexisted: false`，不会被误判为缺备份。

### 判断基线

- `05_EVIDENCE_META/EVIDENCE/THEMES/260727系统_Murphy判断驱动Harness基线.md`

只把本轮附件和 Murphy 当前消息列为 current user thesis。260630、260725 等历史报告继续标为 AI exploration，无当前决策权限。

### 第一组 Current

- `002709.md`：天赐材料，经营公司；唯一信号是销量、单吨利润与经营现金流共同改善。
- `600487.md`：亨通光电，经营公司；研究触发仍待 Murphy 确认，当前只继续观察。
- `601985.md`：中国核电，公用事业；长期方向与一年期重估分开。
- `159611.md`：电力 ETF；改走行业政策、资金、估值拥挤和产品映射路径。
- `515880.md`：通信 ETF；明确主要光模块暴露，不等同亨通式光纤光缆。
- `159326.md`：电网设备 ETF；资本开支方向不再直接推出一年上涨。

## 验收

| 检查 | 结果 |
|---|---|
| 独立只读 Reviewer | PASS |
| Validator 单元测试 | 72 / 72 PASS |
| Python 编译 | PASS |
| 新基线与六张 Current frontmatter | 7 / 7 PASS |
| 六张用户正文内部代码扫描 | 6 / 6 PASS |
| Current 到期扫描 | expired 0 / due 0 / missing 0 / inconsistent 0 |
| 六张 Current 写前与写后 Validator | 6 / 6 PASS |
| `MINDSET` 与决策合同改动 | 0 |

## 边界

- 没有重做全部标的研究；
- 没有刷新 2026-07-24 之后的行情、资金或估值；
- 没有计算概率、EV、仓位或授权交易；
- 没有修改历史 AI 报告；
- 没有把“整体胜率乘以赔率”直接提升为 `MINDSET` 正文；
- 亨通的主产业表达等待 Murphy 回答后再做唯一一次最小刷新。

## 回滚

本轮修改前副本位于：

` .harness_backup/20260727-005354/ `

四张旧 Current 与四个 Automation 工程文件均可从该目录恢复。
