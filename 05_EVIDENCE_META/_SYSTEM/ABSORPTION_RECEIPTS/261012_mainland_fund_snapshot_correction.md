---
receipt_id: AR-261012-MAINLAND-FUND-SNAPSHOT
status: provisional_snapshot_recorded
created_at: 2026-10-12
write_authority: murphy_explicit
capital_authority: none
---

# 境内场内基金持仓更正吸收回执

## 新东西是什么

Murphy 本轮说「A 股已清仓」，并提供券商资产全景截图。截图「股票 / 普通」页显示 161226 13,700 份、588170 171,700 份、589070 24,800 份；三只可见基金市值合计 ¥195,803.30、持仓浮亏合计 ¥29,310.18，按反推成本 ¥225,113.48 计算为 -13.02%。券商页面提示系统清算中；截图没有拍摄日期和现金/账户总资产。

## 改变了什么

旧交易手册首页 2026-09-04 的「8 仓」与兴业银锡等旧持仓不再代表当前状态。按 Murphy 原话与截图兼容的解释登记为“A 股个股已清仓、三只场内基金仍显示持有”；这句话含解释，若 Murphy 澄清不同，应以澄清及券商成交回报修正。161226 在历史卖出与当前持有之间的交易链仍未知。未计算全部账户价值或累计总收益。

## 写到哪里

- 新建 `05_EVIDENCE_META/SOURCES/2026/261012组合_场内基金持仓截图与A股个股状态更正_Murphy来源.md`，保留本轮可见事实、口径差异及截图 SHA256。
- 归档旧手册 `归档/📈 个人交易手册.md` 此前已标为 `superseded`，且不属于 canonical 写入 sink；本轮未覆盖其历史正文。`03_STATE/PORTFOLIO_LEDGER.md` 是索引且持仓正文受保护，本轮未改。

## 审查与校验

- 独立只读 Reviewer：2026-10-12 对 Source 给出 PASS；弱点为截图无日期、清算中，Reviewer 工具未能直接显示图像像素，根图位于临时附件目录；最强反方是清算终值或 Murphy 所说“A 股”范围与当前解释不同。
- Source 写入前 Validator PASS（/tmp/261012_holdings_validator_result.json），exclusive-create 写入后 Validator PASS（/tmp/261012_holdings_post_result.json）；未修改既有文件，无备份需要。根截图在本轮主 Agent 环境中仍可读取，SHA256 为 `01d044ddf2b1c9f760c1a3c0e80af874fa924ed49ced0d7bcb628b73f8eaedc0`；Reviewer 的只读工具未能直接展示图像像素。
- 本回执只登记来源吸收，不授权交易或改变资本参数。

## 下一验证

清算完成后的持仓及总资产页、A 股个股卖出的券商回报，以及其他账户同一时点资产页。
