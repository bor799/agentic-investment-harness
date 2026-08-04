---
description: Manually inspect or run one AI cycle v2 unit
argument-hint: [dry-run|next|object-id|finalize]
allowed-tools: Read, Glob, Grep, Edit, Write, WebSearch, WebFetch
model: sonnet
disable-model-invocation: true
layer: AUTOMATION
primary_role: legacy_claude_automation
status: active
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: operational
legacy_metadata_added: normalized
legacy_path: ".claude/commands/ai-cycle-cross-market-v2.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---


Operate the project’s `AI_CYCLE_CROSS_MARKET_V2` workflow in manual single-unit mode.

Read these files in full before acting:

- `AI周期探索/0_总览/LOOP_PROMPT_CROSS_MARKET_V2.md`
- `AI周期探索/0_总览/CROSS_MARKET_V2_RUN_BOUNDARIES.md`
- `AI周期探索/0_总览/cross_market_queue_v2.json`

User argument: `$ARGUMENTS`

Interpret it as follows:

- `dry-run` or empty: perform a read-only preflight. List all 18 objects in order, current status, attempts, research directories, options-enabled objects, total-loop defaults and the exact terminal command. Do not edit any file and do not start research.
- `next`: process only the first `pending` or `retry` object in queue order.
- an object id: process only that queue object if its status is `pending` or `retry`.
- `finalize`: proceed only if all 18 objects are `completed`.

For a research or finalize action, this manual command does not have Bash and must not call the host queue controller. The following manual claim transaction is the sole exception to the main prompt's “Claude does not edit the queue” rule; it permits edits only to the selected row or `final_report` and no other queue content:

1. Re-read the selected queue row immediately before editing.
2. Confirm `attempt_count < 3` and no other item is `running`. If either check fails, stop without editing.
3. Set only that row to `running`, increment `attempt_count`, set `last_attempt_at`, and create a unique manual `run_token`. For finalize, update only `final_report` in the same way.
4. Follow the v2 main prompt exactly, including source limits, four tickets, special tool tickets, holding-ledger rules, options completeness and write allowlist.
5. Write `AI周期探索/0_总览/v2_last_outcome.json`.
6. Self-check the outcome against the contract in the main prompt. Only after it passes, set the selected row to `completed` and copy `last_refresh`, `next_review`, `evidence_gaps` and `final_evidence_status` into the queue. Clear `run_token`.
7. On a technical failure, set the row to `retry` if fewer than three total attempts have occurred; otherwise set `failed_after_retries`. Record `last_error` and clear `run_token`. Do not claim another object in the same invocation.

Never expose Bash, delete or install anything, start another Agent, send messages, write outside the allowlist, modify the portfolio ledger, change capital parameters, place a trade or auto-continue to a second object.

For the full non-interactive loop, do not emulate it inside this slash command. In `dry-run`, show this manual terminal entrypoint:

```text
AI周期探索/0_总览/run_nightly_research_loop.sh --dry-run
```

The user must explicitly run the same script without `--dry-run` to incur API cost.
