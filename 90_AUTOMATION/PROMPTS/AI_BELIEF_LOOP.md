---
title: ai_belief_loop_input_contract
date: 2026-07-28
layer: AUTOMATION
primary_role: runner_prompt
status: active
decision_authority: none
---

# AI Belief Loop

## 一句话

把一份人工提供的材料拆成“来源候选、认知差分、原子 belief 更新建议”，
暂存在隔离区；不把它自动升级为事实或投资判断。

## 输入模板

```json
{
  "root_source_id": "SRC-YYYYMMDD-UNIQUE-ID",
  "as_of": "2026-07-28",
  "title": "材料标题",
  "source_locator": "原始 URL 或本地定位",
  "source_kind": "formal_disclosure | transcript | article | user_discussion",
  "target_claim_ids": ["ORCL-B02"],
  "excerpts": [
    {
      "excerpt_id": "EX-01",
      "text": "逐字摘录"
    }
  ],
  "moment_candidate": {
    "old_judgment": "原判断",
    "new_judgment": "材料可能带来的变化",
    "next_validation": "下一项验证",
    "counter_case": "最强替代解释"
  },
  "proposed_updates": [
    {
      "claim_id": "ORCL-B02",
      "direction": "support",
      "independence": "unknown",
      "diagnosticity": "medium",
      "evidence_channel": "customer_contract",
      "updates_dimension": "demand",
      "update_reason": "为什么可能更新",
      "counter_explanation": "还可能是什么",
      "old_state": "working",
      "proposed_state": "working"
    }
  ]
}
```

Runner 会忽略输入中的 authority / verification 身份并强制写成：

```yaml
verification_status: unverified_by_runner
promotion_authority: none
belief_update.authority: suggestion_only
belief_update.independence: unknown | same_root
```

## 运行

```bash
python3 90_AUTOMATION/PIPELINES/ai_belief_loop.py \
  --input /absolute/path/to/input.json \
  --mode dry-run
```

`dry-run` 零文件写入。确认计划后才可使用 `--mode stage`；stage 也只会
exclusive-create Staging 与脱敏 Run Log。

## 晋升

Staging 不是正式材料。要进入 Source 或 Moment，必须：

1. 回到原始定位核验 excerpt 与日期；
2. 判断是否同根重复或 `NO_INCREMENT`；
3. Murphy 明确要求写入；
4. Reviewer PASS；
5. Validator PASS。

Runner 永远不能写 Knowledge、Expectation、Current、Ledger、仓位或交易
动作。当前没有安装定时任务时，也不能描述为“已经自动监控”。
