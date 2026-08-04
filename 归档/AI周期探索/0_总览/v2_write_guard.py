#!/usr/bin/env python3
"""PreToolUse path guard for the v2 Claude agent.

Allow Edit/Write only for the single host-claimed object and the outcome handoff.
In finalize mode, allow only the dated cross-market report and the outcome handoff.
Any parsing, state or path ambiguity is denied with exit code 2.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[1]
DEFAULT_QUEUE = SCRIPT_DIR / "cross_market_queue_v2.json"
OUTCOME_FILE = (SCRIPT_DIR / "v2_last_outcome.json").resolve()
FINAL_DIR = (PROJECT_ROOT / "分析报告/archive").resolve()
REFRESH_PATTERN = re.compile(r"^\d{6}.+_证据状态刷新\.md$")
FINAL_PATTERN = re.compile(r"^\d{6}跨市场_AI周期证据与赔率循环\.md$")


def deny(reason: str) -> int:
    print(f"v2 write guard blocked the tool call: {reason}", file=sys.stderr)
    return 2


def load_payload() -> dict[str, Any]:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError) as exc:
        raise ValueError(f"invalid hook JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError("hook payload root is not an object")
    return payload


def resolve_target(raw_path: str, cwd: str) -> Path:
    candidate = Path(raw_path).expanduser()
    if not candidate.is_absolute():
        candidate = Path(cwd) / candidate
    return candidate.resolve(strict=False)


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def active_claim(queue: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    running = [item for item in queue.get("items", []) if item.get("status") == "running"]
    final = queue.get("final_report", {})
    final_running = final.get("status") == "running"
    if len(running) + int(final_running) != 1:
        raise ValueError("expected exactly one running object or final claim")
    if final_running:
        return "finalize", final
    return "object", running[0]


def object_path_allowed(target: Path, item: dict[str, Any]) -> bool:
    research_dir = (PROJECT_ROOT / str(item["research_dir"])).resolve(strict=False)
    if not is_relative_to(target, research_dir):
        return False
    relative = target.relative_to(research_dir)
    if len(relative.parts) != 1:
        return False
    return target.name in {"evidence_log.md", "next_signals.md"} or bool(REFRESH_PATTERN.fullmatch(target.name))


def final_path_allowed(target: Path) -> bool:
    return target.parent == FINAL_DIR and bool(FINAL_PATTERN.fullmatch(target.name))


def main() -> int:
    try:
        payload = load_payload()
        tool_name = payload.get("tool_name")
        if tool_name not in {"Edit", "Write"}:
            return 0
        tool_input = payload.get("tool_input")
        if not isinstance(tool_input, dict) or not isinstance(tool_input.get("file_path"), str):
            return deny("Edit/Write call has no file_path")
        cwd = payload.get("cwd")
        if not isinstance(cwd, str) or not cwd:
            return deny("hook payload has no cwd")
        target = resolve_target(tool_input["file_path"], cwd)
        queue_path = Path(os.environ.get("AI_CYCLE_V2_QUEUE_FILE", str(DEFAULT_QUEUE))).resolve()
        with queue_path.open("r", encoding="utf-8") as handle:
            queue = json.load(handle)
        mode, claim = active_claim(queue)
        if target == OUTCOME_FILE:
            return 0
        if mode == "object" and object_path_allowed(target, claim):
            return 0
        if mode == "finalize" and final_path_allowed(target):
            return 0
        return deny(f"path is outside the active {mode} allowlist: {target}")
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        return deny(str(exc))


if __name__ == "__main__":
    raise SystemExit(main())
