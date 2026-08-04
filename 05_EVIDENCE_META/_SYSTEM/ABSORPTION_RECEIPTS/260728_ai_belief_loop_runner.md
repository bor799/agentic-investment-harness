---
receipt_id: AR-260728-AI-BELIEF-LOOP-RUNNER
status: complete
created_at: 2026-07-28
write_authority: murphy_explicit
capital_authority: none
---

# AI Belief Loop Runner 吸收回执

## 交付结果

- 新增 [[90_AUTOMATION/PROMPTS/AI_BELIEF_LOOP|输入契约]]。
- 新增 `90_AUTOMATION/PIPELINES/ai_belief_loop.py`。
- 默认 `dry-run` 零文件写入。
- `stage` 只以 exclusive-create 写入未核验 Staging 与脱敏 Run Log。
- Runner 不联网、不回源，不写 Source、Moment、Knowledge、Expectation、
  Current、Ledger、仓位或交易动作。

## 强制边界

- `verification_status: unverified_by_runner`
- `promotion_authority: none`
- `belief_update.authority: suggestion_only`
- `belief_update.independence: unknown | same_root`
- Claim allowlist 只从
  [[05_EVIDENCE_META/_SYSTEM/CLAIM_LEDGER|canonical Claim Ledger]] 读取。
- 同一 `root_source_id + claim_id` 跨 Source、Moment 与 Staging 去重。
- runner 使用排他锁保护扫描与写入；不覆盖现有文件。
- 任一 staging / log 写入失败，只回滚本次进程创建的 staging 文件。
- Run Log 只保留哈希、模式、结果、创建路径与错误码。

## Reviewer

第一次审查为 `BLOCK`：直接创建 Source / Moment 会让未核验输入获得正式
证据外观。修订为只写隔离 Staging / Run Log 后，最终 verdict 为 `PASS`。

- weakest_link：跨目录去重依赖所有自动输入遵守同一 runner 入口。
- best_bear_case：结构化 Staging 仍可能被后续 Agent 误读成已核验证据。

因此 Staging 晋升必须重新回源，并经过 Murphy explicit、Reviewer PASS、
Validator PASS。

## 验收

- 第二批备份：`.harness_backup/20260728-012000-ai-belief-loop-runner/`
- 全量测试：`161/161 PASS`
- Validator：Staging `40/40 PASS`
- Validator：Run Log `40/40 PASS`
- Validator：本回执 `40/40 PASS`
- 试点内部链接：`127 checked / 0 unresolved`
- 真实旧材料 dry-run：`NO_INCREMENT`
- Staging / Run Log 未因 dry-run 新增业务文件。

## 未做

当前环境没有可调用的 `automation_update` 能力，因此没有安装或声称已经
安装 ORCL / NBIS 定时监控。现在交付的是可手动或由未来调度器调用的安全
runner；调度器也不能扩大它的写入权限。
