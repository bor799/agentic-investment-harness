#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd -- "$SCRIPT_DIR/../.." && pwd)"
QUEUE_FILE="$SCRIPT_DIR/cross_market_queue_v2.json"
QUEUE_TOOL="$SCRIPT_DIR/v2_queue.py"
MAIN_PROMPT="$SCRIPT_DIR/LOOP_PROMPT_CROSS_MARKET_V2.md"
BOUNDARIES="$SCRIPT_DIR/CROSS_MARKET_V2_RUN_BOUNDARIES.md"
OUTCOME_FILE="$SCRIPT_DIR/v2_last_outcome.json"
RUN_LOG="$SCRIPT_DIR/v2_run_log.jsonl"

DRY_RUN=false
HOURS="10"
MAX_ITERATIONS="22"
BUDGET_USD="35"
BYPASS_PERMISSIONS=false
CLAUDE_TOOLS="Read,Glob,Grep,Edit,Write,WebSearch,WebFetch"

usage() {
  printf '%s\n' \
    'Usage: run_nightly_research_loop.sh [--dry-run] [--hours 10] [--max-iterations 22] [--budget-usd 35] [--bypass-permissions]'
}

die() {
  printf 'error: %s\n' "$1" >&2
  exit 2
}

while (($# > 0)); do
  case "$1" in
    --dry-run)
      DRY_RUN=true
      shift
      ;;
    --hours)
      (($# >= 2)) || die '--hours requires a value'
      HOURS="$2"
      shift 2
      ;;
    --max-iterations)
      (($# >= 2)) || die '--max-iterations requires a value'
      MAX_ITERATIONS="$2"
      shift 2
      ;;
    --budget-usd)
      (($# >= 2)) || die '--budget-usd requires a value'
      BUDGET_USD="$2"
      shift 2
      ;;
    --bypass-permissions)
      BYPASS_PERMISSIONS=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      usage >&2
      die "unknown argument: $1"
      ;;
  esac
done

command -v python3 >/dev/null 2>&1 || die 'python3 is required'

python3 - "$HOURS" "$MAX_ITERATIONS" "$BUDGET_USD" <<'PY' || exit 2
import sys

try:
    hours = float(sys.argv[1])
    iterations_text = sys.argv[2]
    budget = float(sys.argv[3])
    if not iterations_text.isdigit():
        raise ValueError
    iterations = int(iterations_text)
    if hours <= 0 or iterations <= 0 or budget <= 0:
        raise ValueError
except ValueError:
    print("error: --hours and --budget-usd must be positive numbers; --max-iterations must be a positive integer", file=sys.stderr)
    raise SystemExit(1)
PY

for required_file in "$QUEUE_FILE" "$QUEUE_TOOL" "$MAIN_PROMPT" "$BOUNDARIES"; do
  [[ -f "$required_file" ]] || die "missing required file: $required_file"
done

if [[ "$DRY_RUN" == true ]]; then
  printf 'AI cycle v2 dry run (Claude will not be called; no files will be modified)\n'
  printf 'model: sonnet\n'
  printf 'effort: high\n'
  printf 'hours: %s\n' "$HOURS"
  printf 'max_iterations: %s (18 objects + 1 final report + retry capacity)\n' "$MAX_ITERATIONS"
  printf 'total_budget_usd: %s\n' "$BUDGET_USD"
  printf 'permission_mode: %s\n' "$([[ "$BYPASS_PERMISSIONS" == true ]] && printf bypassPermissions || printf acceptEdits)"
  printf 'tools: %s\n' "$CLAUDE_TOOLS"
  printf 'queue: %s\n' "$QUEUE_FILE"
  printf 'final_report_dir: %s\n' "$PROJECT_ROOT/分析报告/archive"
  printf 'planned rounds:\n'
  python3 "$QUEUE_TOOL" show --queue "$QUEUE_FILE"
  printf '19\t__final__\t-\tpending-after-18-complete\t0\t分析报告/archive\n'
  exit 0
fi

command -v claude >/dev/null 2>&1 || die 'Claude Code CLI is required for a real run'

python3 "$QUEUE_TOOL" recover --queue "$QUEUE_FILE"

RUN_TMP_DIR="$(mktemp -d "${TMPDIR:-/tmp}/ai-cycle-v2.XXXXXX")"
cleanup() {
  if [[ -n "${RUN_TMP_DIR:-}" && -d "$RUN_TMP_DIR" && "$RUN_TMP_DIR" == "${TMPDIR:-/tmp}/ai-cycle-v2."* ]]; then
    rm -rf -- "$RUN_TMP_DIR"
  fi
}
trap cleanup EXIT

START_EPOCH="$(date +%s)"
DURATION_SECONDS="$(python3 - "$HOURS" <<'PY'
import sys
print(int(float(sys.argv[1]) * 3600))
PY
)"
DEADLINE_EPOCH=$((START_EPOCH + DURATION_SECONDS))
ITERATION=0
SPENT_USD="0"

while ((ITERATION < MAX_ITERATIONS)); do
  NOW_EPOCH="$(date +%s)"
  if ((NOW_EPOCH >= DEADLINE_EPOCH)); then
    printf 'time limit reached after %s iterations\n' "$ITERATION"
    break
  fi

  if ! python3 - "$SPENT_USD" "$BUDGET_USD" <<'PY'
import sys
raise SystemExit(0 if float(sys.argv[1]) < float(sys.argv[2]) else 1)
PY
  then
    printf 'budget limit reached: spent_usd=%s budget_usd=%s\n' "$SPENT_USD" "$BUDGET_USD"
    break
  fi

  CLAIM_ERR="$RUN_TMP_DIR/claim.err"
  set +e
  CLAIM_JSON="$(python3 "$QUEUE_TOOL" claim --queue "$QUEUE_FILE" 2>"$CLAIM_ERR")"
  CLAIM_RC=$?
  set -e
  if ((CLAIM_RC != 0)); then
    printf 'loop stopped: %s\n' "$(tr '\n' ' ' <"$CLAIM_ERR")"
    break
  fi

  ITERATION=$((ITERATION + 1))
  CLAIM_ID="$(python3 -c 'import json,sys; print(json.load(sys.stdin)["id"])' <<<"$CLAIM_JSON")"
  CLAIM_MODE="$(python3 -c 'import json,sys; print(json.load(sys.stdin)["mode"])' <<<"$CLAIM_JSON")"
  RUN_TOKEN="$(python3 -c 'import json,sys; print(json.load(sys.stdin)["run_token"])' <<<"$CLAIM_JSON")"
  REMAINING_BUDGET="$(python3 - "$BUDGET_USD" "$SPENT_USD" <<'PY'
import sys
print(f"{max(0.0, float(sys.argv[1]) - float(sys.argv[2])):.6f}")
PY
)"

  ITERATION_PROMPT="$(printf '%s\n\n%s\n%s\n\n%s\n%s\n\n%s\n' \
    'Read and obey the v2 main prompt and run boundaries.' \
    "Main prompt: $MAIN_PROMPT" \
    "Run boundaries: $BOUNDARIES" \
    'The host atomically claimed exactly one unit of work. Treat this JSON as immutable:' \
    "$CLAIM_JSON" \
    "Write the required validated outcome to: $OUTCOME_FILE")"

  STDOUT_FILE="$RUN_TMP_DIR/claude-${ITERATION}.json"
  STDERR_FILE="$RUN_TMP_DIR/claude-${ITERATION}.err"
  APPLY_ERR="$RUN_TMP_DIR/apply-${ITERATION}.err"
  CLAUDE_ARGS=(
    --print
    --agent ai-cycle-cross-market-v2
    --model sonnet
    --effort high
    --tools "$CLAUDE_TOOLS"
    --allowed-tools "$CLAUDE_TOOLS"
    --max-budget-usd "$REMAINING_BUDGET"
    --output-format json
    --no-session-persistence
    --name "ai-cycle-v2-${ITERATION}-${CLAIM_ID}"
  )
  if [[ "$BYPASS_PERMISSIONS" == true ]]; then
    CLAUDE_ARGS+=(--permission-mode bypassPermissions --dangerously-skip-permissions)
  else
    CLAUDE_ARGS+=(--permission-mode acceptEdits)
  fi

  printf 'iteration %s/%s: %s (%s), remaining_budget_usd=%s\n' \
    "$ITERATION" "$MAX_ITERATIONS" "$CLAIM_ID" "$CLAIM_MODE" "$REMAINING_BUDGET"

  set +e
  (
    cd -- "$PROJECT_ROOT"
    claude "${CLAUDE_ARGS[@]}" "$ITERATION_PROMPT"
  ) >"$STDOUT_FILE" 2>"$STDERR_FILE" &
  CLAUDE_PID=$!
  TIMED_OUT=false
  while kill -0 "$CLAUDE_PID" 2>/dev/null; do
    NOW_EPOCH="$(date +%s)"
    if ((NOW_EPOCH >= DEADLINE_EPOCH)); then
      TIMED_OUT=true
      kill -TERM "$CLAUDE_PID" 2>/dev/null
      for _ in 1 2 3 4 5; do
        kill -0 "$CLAUDE_PID" 2>/dev/null || break
        sleep 1
      done
      kill -KILL "$CLAUDE_PID" 2>/dev/null || true
      break
    fi
    sleep 5
  done
  wait "$CLAUDE_PID"
  CLAUDE_RC=$?
  set -e

  COST_USD="$(python3 - "$STDOUT_FILE" <<'PY'
import json
import sys

try:
    with open(sys.argv[1], "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    value = payload.get("total_cost_usd")
    if value is None:
        raise ValueError
    print(float(value))
except (OSError, ValueError, TypeError, json.JSONDecodeError):
    raise SystemExit(1)
PY
)" || COST_USD="unknown"

  if [[ "$COST_USD" != unknown ]]; then
    SPENT_USD="$(python3 - "$SPENT_USD" "$COST_USD" <<'PY'
import sys
print(f"{float(sys.argv[1]) + float(sys.argv[2]):.6f}")
PY
)"
  fi

  if [[ "$TIMED_OUT" == true ]]; then
    python3 "$QUEUE_TOOL" fail --queue "$QUEUE_FILE" --id "$CLAIM_ID" --run-token "$RUN_TOKEN" \
      --error "host_time_limit_reached" --run-log "$RUN_LOG"
    printf 'time limit interrupted %s; queue preserved for recovery\n' "$CLAIM_ID"
    break
  fi

  if ((CLAUDE_RC != 0)); then
    ERROR_TEXT="claude_exit_${CLAUDE_RC}: $(tail -c 1200 "$STDERR_FILE" | tr '\n' ' ')"
    python3 "$QUEUE_TOOL" fail --queue "$QUEUE_FILE" --id "$CLAIM_ID" --run-token "$RUN_TOKEN" \
      --error "$ERROR_TEXT" --run-log "$RUN_LOG"
    if [[ "$COST_USD" == unknown ]]; then
      printf 'Claude failed and cost is unknown; stopping conservatively\n'
      break
    fi
    continue
  fi

  if [[ "$COST_USD" == unknown ]]; then
    python3 "$QUEUE_TOOL" fail --queue "$QUEUE_FILE" --id "$CLAIM_ID" --run-token "$RUN_TOKEN" \
      --error "successful_cli_exit_but_cost_unknown" --run-log "$RUN_LOG"
    printf 'cost could not be confirmed; stopping conservatively\n'
    break
  fi

  set +e
  APPLY_OUTPUT="$(python3 "$QUEUE_TOOL" apply --queue "$QUEUE_FILE" --outcome "$OUTCOME_FILE" \
    --run-log "$RUN_LOG" 2>"$APPLY_ERR")"
  APPLY_RC=$?
  set -e
  if ((APPLY_RC != 0)); then
    ERROR_TEXT="invalid_outcome: $(tail -c 1500 "$APPLY_ERR" | tr '\n' ' ')"
    python3 "$QUEUE_TOOL" fail --queue "$QUEUE_FILE" --id "$CLAIM_ID" --run-token "$RUN_TOKEN" \
      --error "$ERROR_TEXT" --run-log "$RUN_LOG"
    printf 'outcome rejected for %s; scheduled according to retry policy\n' "$CLAIM_ID"
    continue
  fi

  printf '%s; spent_usd=%s\n' "$APPLY_OUTPUT" "$SPENT_USD"
  if [[ "$CLAIM_ID" == "__final__" ]]; then
    printf 'AI cycle v2 complete\n'
    break
  fi
done

python3 "$QUEUE_TOOL" status --queue "$QUEUE_FILE"
printf 'run finished: iterations=%s spent_usd=%s\n' "$ITERATION" "$SPENT_USD"
