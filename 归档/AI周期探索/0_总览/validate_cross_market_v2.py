#!/usr/bin/env python3
"""Static and dry-run validation for AI cycle cross-market v2.

This validator never invokes Claude. It places a sentinel `claude` executable at
the front of PATH and verifies that the loop's --dry-run path does not touch it.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

from v2_queue import EXPECTED_IDS, OPTION_IDS, QueueError, load_json, validate_queue


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[1]
QUEUE = SCRIPT_DIR / "cross_market_queue_v2.json"
PROMPT = SCRIPT_DIR / "LOOP_PROMPT_CROSS_MARKET_V2.md"
BOUNDARIES = SCRIPT_DIR / "CROSS_MARKET_V2_RUN_BOUNDARIES.md"
RUNNER = SCRIPT_DIR / "run_nightly_research_loop.sh"
QUEUE_TOOL = SCRIPT_DIR / "v2_queue.py"
WRITE_GUARD = SCRIPT_DIR / "v2_write_guard.py"
OUTCOME = SCRIPT_DIR / "v2_last_outcome.json"
AGENT = PROJECT_ROOT / ".claude/agents/ai-cycle-cross-market-v2.md"
COMMAND = PROJECT_ROOT / ".claude/commands/ai-cycle-cross-market-v2.md"
README = SCRIPT_DIR / "README.md"
HISTORICAL_FILES = [
    SCRIPT_DIR / "LOOP_PROMPT_PRO.md",
    SCRIPT_DIR / "CLAUDE_CODE_RUN_COMMAND_PRO.md",
    PROJECT_ROOT / ".claude/commands/ai-research-loop-pro.md",
]


class ValidationFailure(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationFailure(message)


def sha256(path: Path) -> str | None:
    if not path.exists():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValidationFailure(f"cannot read {path}: {exc}") from exc


def validate_files_exist() -> None:
    required = [QUEUE, PROMPT, BOUNDARIES, RUNNER, QUEUE_TOOL, WRITE_GUARD, OUTCOME, AGENT, COMMAND, README]
    missing = [str(path) for path in required if not path.is_file()]
    require(not missing, f"missing v2 files: {missing}")


def validate_queue_file() -> dict:
    queue = load_json(QUEUE)
    try:
        validate_queue(queue)
    except QueueError as exc:
        raise ValidationFailure(str(exc)) from exc
    require([item["id"] for item in queue["items"]] == EXPECTED_IDS, "18-object order changed")
    require(sum(item["id"] == "lmnd" for item in queue["items"]) == 1, "LMND must appear once")
    require(
        {item["id"] for item in queue["items"] if item["options_enabled"]} == OPTION_IDS,
        "options set changed",
    )
    require(queue["max_attempts_per_object"] == 3, "retry policy must be initial attempt + two retries")
    for item in queue["items"]:
        directory = PROJECT_ROOT / item["research_dir"]
        require(directory.is_dir(), f"missing research directory for {item['id']}: {directory}")
    return queue


def frontmatter(text: str) -> str:
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    require(match is not None, "missing YAML frontmatter")
    return match.group(1)


def validate_agent_and_command() -> None:
    agent_text = read(AGENT)
    agent_meta = frontmatter(agent_text)
    require("name: ai-cycle-cross-market-v2" in agent_meta, "agent name invalid")
    require("model: sonnet" in agent_meta, "agent must default to Sonnet")
    require(agent_meta.count("<example>") >= 2, "agent description needs triggering examples")
    tools_match = re.search(r"tools:\s*\[(.*?)\]", agent_meta)
    require(tools_match is not None, "agent tools missing")
    tool_text = tools_match.group(1)
    for forbidden in ("Bash", "Task", "SendMessage", "NotebookEdit"):
        require(forbidden not in tool_text, f"agent exposes forbidden tool {forbidden}")
    for required in ("Read", "Glob", "Grep", "Edit", "Write", "WebSearch", "WebFetch"):
        require(required in tool_text, f"agent missing required tool {required}")
    require('matcher: "Edit|Write"' in agent_meta, "agent is missing the Edit/Write PreToolUse guard")
    require(str(WRITE_GUARD) in agent_meta, "agent hook does not reference the v2 write guard")

    command_text = read(COMMAND)
    command_meta = frontmatter(command_text)
    require("disable-model-invocation: true" in command_meta, "manual command must disable model invocation")
    require("model: sonnet" in command_meta, "manual command must default to Sonnet")
    allowed_line = next((line for line in command_meta.splitlines() if line.startswith("allowed-tools:")), "")
    require("Bash" not in allowed_line and "Task" not in allowed_line, "manual command exposes Bash or Task")


def validate_prompt_semantics() -> None:
    prompt = read(PROMPT)
    boundaries = read(BOUNDARIES)
    required_prompt_phrases = [
        "H_B",
        "H_R",
        "H_L",
        "H_C",
        "probability_status: uncalibrated",
        "contract_status: incomplete",
        "designated_contract: false",
        "上交所、深交所、巨潮资讯",
        "SEC 原始 filing",
        "HKEX",
        "指数公司、基金公司、交易所",
        "新闻只负责发现叙事",
        "政策水 → 市场水 → 板块水 → 标的水",
        "不操作",
        "不得改写 `cross_market_queue_v2.json`",
        "只研究买方期权或借方价差",
    ]
    for phrase in required_prompt_phrases:
        require(phrase in prompt, f"main prompt missing requirement: {phrase}")
    require("70 分" not in prompt and "70分" not in prompt, "active prompt must not use the historical fixed score")
    require(not re.search(r"H_[BRLC].{0,20}[+＋]\s*\d+", prompt), "active prompt contains fixed ticket points")
    require(not re.search(r"probability_status[\"'`:\s]+(?:50%|0\.5)", prompt), "unknown probability defaults to 50%")
    require("允许裸卖" not in prompt and "允许无限损失" not in prompt, "unsafe options structure authorized")
    require("自动成交" in prompt and "不得自动成交" in prompt, "automatic execution must be explicitly forbidden")
    require("当前状态：仅生成，尚未启动" in boundaries, "generated-only status is missing")
    require("bypassPermissions" in boundaries and "不会添加工具" in boundaries, "bypass boundary is unclear")


def validate_runner_static() -> None:
    result = subprocess.run(["bash", "-n", str(RUNNER)], capture_output=True, text=True)
    require(result.returncode == 0, f"bash -n failed: {result.stderr}")
    runner = read(RUNNER)
    require('HOURS="10"' in runner, "default hours must be 10")
    require('MAX_ITERATIONS="22"' in runner, "default max iterations must be 22")
    require('BUDGET_USD="35"' in runner, "default budget must be 35 USD")
    tools_line = next((line for line in runner.splitlines() if line.startswith("CLAUDE_TOOLS=")), "")
    require("Bash" not in tools_line and "Task" not in tools_line, "runner grants Claude a forbidden tool")
    require("--permission-mode acceptEdits" in runner, "default acceptEdits mode missing")
    require("--max-budget-usd" in runner and "DEADLINE_EPOCH" in runner, "budget or time guard missing")
    require("--add-dir" not in runner, "runner may not expand Claude directory access")


def run_guard(queue: dict, target: Path, permission_mode: str = "acceptEdits") -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory(prefix="ai-cycle-v2-guard-") as temp_dir:
        temp_queue = Path(temp_dir) / "queue.json"
        temp_queue.write_text(json.dumps(queue, ensure_ascii=False), encoding="utf-8")
        env = os.environ.copy()
        env["AI_CYCLE_V2_QUEUE_FILE"] = str(temp_queue)
        payload = {
            "cwd": str(PROJECT_ROOT),
            "permission_mode": permission_mode,
            "tool_name": "Write",
            "tool_input": {"file_path": str(target), "content": "test"},
        }
        return subprocess.run(
            [sys.executable, str(WRITE_GUARD)],
            input=json.dumps(payload),
            env=env,
            capture_output=True,
            text=True,
        )


def validate_write_guard(queue: dict) -> None:
    guarded = json.loads(json.dumps(queue))
    item = next(item for item in guarded["items"] if item["id"] == "meta")
    item["status"] = "running"
    item["run_token"] = "static-guard-test"
    allowed_refresh = PROJECT_ROOT / item["research_dir"] / "260721Meta_证据状态刷新.md"
    allowed_outcome = OUTCOME
    forbidden_queue = QUEUE
    require(run_guard(guarded, allowed_refresh).returncode == 0, "write guard rejected the claimed refresh file")
    require(
        run_guard(guarded, allowed_outcome, permission_mode="bypassPermissions").returncode == 0,
        "write guard rejected outcome under bypass",
    )
    denied = run_guard(guarded, forbidden_queue, permission_mode="bypassPermissions")
    require(denied.returncode == 2, "write guard allowed a queue write under bypass")
    require("outside" in denied.stderr, "write guard denial reason missing")


def validate_dry_run(queue: dict) -> None:
    watched = [QUEUE, OUTCOME, SCRIPT_DIR / "v2_run_log.jsonl"]
    before = {path: sha256(path) for path in watched}
    with tempfile.TemporaryDirectory(prefix="ai-cycle-v2-validator-") as temp_dir:
        temp = Path(temp_dir)
        sentinel = temp / "claude-called"
        fake_claude = temp / "claude"
        fake_claude.write_text(f"#!/bin/sh\ntouch '{sentinel}'\nexit 99\n", encoding="utf-8")
        fake_claude.chmod(fake_claude.stat().st_mode | stat.S_IXUSR)
        env = os.environ.copy()
        env["PATH"] = f"{temp}{os.pathsep}{env.get('PATH', '')}"
        result = subprocess.run(
            [str(RUNNER), "--dry-run", "--hours", "10", "--max-iterations", "22", "--budget-usd", "35"],
            cwd=PROJECT_ROOT,
            env=env,
            capture_output=True,
            text=True,
        )
        require(result.returncode == 0, f"dry-run failed: {result.stderr}")
        require(not sentinel.exists(), "dry-run invoked Claude")
        require("Claude will not be called" in result.stdout, "dry-run safety message missing")
        for item in queue["items"]:
            require(item["id"] in result.stdout, f"dry-run omitted {item['id']}")
        require("__final__" in result.stdout, "dry-run omitted the final synthesis round")
    after = {path: sha256(path) for path in watched}
    require(before == after, "dry-run modified queue, outcome or run log")


def validate_historical_markers() -> None:
    for path in HISTORICAL_FILES:
        require(path.is_file(), f"missing historical PRO file: {path}")
        text = read(path)
        require("历史" in text and "不再授权" in text, f"historical PRO file lacks no-authority marker: {path}")


def main() -> int:
    checks = [
        ("files", validate_files_exist),
        ("agent-command", validate_agent_and_command),
        ("prompt-semantics", validate_prompt_semantics),
        ("runner-static", validate_runner_static),
        ("historical-markers", validate_historical_markers),
    ]
    try:
        for name, check in checks:
            check()
            print(f"PASS {name}")
        queue = validate_queue_file()
        print("PASS queue")
        validate_write_guard(queue)
        print("PASS write-guard-acceptEdits-and-bypass")
        validate_dry_run(queue)
        print("PASS dry-run-no-Claude-no-write")
    except (ValidationFailure, QueueError) as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1
    print("PASS all v2 static checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
