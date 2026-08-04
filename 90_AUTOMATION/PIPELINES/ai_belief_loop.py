#!/usr/bin/env python3
"""
AI belief loop v1

把人工提供的证据包编译成隔离的候选 Staging。它不联网、不回源、不更新
Source、Moment、Knowledge、Expectation、Current 或任何资本文件。
"""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import importlib.util
import json
import os
import re
import sys
from contextlib import contextmanager
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any


RUNNER_VERSION = "1.0.0"
SCHEMA_VERSION = "ai-belief-loop-staging-v1"
MAX_INPUT_BYTES = 256 * 1024
MAX_CLAIMS = 20
MAX_LIST_ITEMS = 20
MAX_FIELD_CHARS = 12_000
ROOT_SOURCE_ID_RE = re.compile(
    r"^(?=.{1,80}$)[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?$"
)
CLAIM_ID_RE = re.compile(r"^[A-Z][A-Z0-9]*-B\d{2}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
FORBIDDEN_KEYS = {
    "posterior_probability",
    "probability",
    "weight",
    "weight_delta",
    "score",
    "score_delta",
    "target_price",
    "position_size",
    "buy_authorization",
    "capital_action",
    "trade_action",
    "portfolio_weight",
    "murphy_confirmed",
    "applied",
    "force",
}
TOP_LEVEL_KEYS = {
    "root_source_id",
    "as_of",
    "title",
    "source_locator",
    "source_kind",
    "target_claim_ids",
    "excerpts",
    "moment_candidate",
    "proposed_updates",
    "verification_status",
}
UPDATE_KEYS = {
    "claim_id",
    "direction",
    "independence",
    "diagnosticity",
    "evidence_channel",
    "updates_dimension",
    "update_reason",
    "counter_explanation",
    "old_state",
    "proposed_state",
    "authority",
}
LOG_KEYS = {
    "schema_version",
    "runner_version",
    "created_at",
    "input_sha256",
    "mode",
    "result",
    "created_paths",
    "error_code",
}


class RunnerError(Exception):
    """可安全输出的、无原始输入内容的错误。"""

    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code
        self.safe_message = message


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _load_json_bytes(path: Path) -> tuple[bytes, dict[str, Any]]:
    if path.is_symlink():
        raise RunnerError("INPUT_SYMLINK", "input file cannot be a symlink")
    try:
        size = path.stat().st_size
    except OSError as exc:
        raise RunnerError("INPUT_READ_FAILED", "input file is not readable") from exc
    if size > MAX_INPUT_BYTES:
        raise RunnerError("INPUT_TOO_LARGE", "input exceeds 256 KiB")
    try:
        raw = path.read_bytes()
        data = json.loads(raw)
    except (OSError, json.JSONDecodeError) as exc:
        raise RunnerError("INPUT_INVALID", "input must be valid UTF-8 JSON") from exc
    if not isinstance(data, dict):
        raise RunnerError("INPUT_INVALID", "input root must be an object")
    return raw, data


def _walk_limits(value: Any, path: str = "input") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if not isinstance(key, str):
                raise RunnerError("SCHEMA_INVALID", f"{path} contains a non-string key")
            if key.casefold() in FORBIDDEN_KEYS:
                raise RunnerError("FORBIDDEN_FIELD", f"forbidden field: {key}")
            _walk_limits(child, f"{path}.{key}")
    elif isinstance(value, list):
        if len(value) > MAX_LIST_ITEMS:
            raise RunnerError("TOO_MANY_ITEMS", f"{path} exceeds {MAX_LIST_ITEMS} items")
        for index, child in enumerate(value):
            _walk_limits(child, f"{path}[{index}]")
    elif isinstance(value, str) and len(value) > MAX_FIELD_CHARS:
        raise RunnerError("FIELD_TOO_LONG", f"{path} exceeds {MAX_FIELD_CHARS} characters")


def _load_claim_states(repo_root: Path) -> dict[str, str]:
    ledger = repo_root / "05_EVIDENCE_META/_SYSTEM/CLAIM_LEDGER.md"
    if ledger.is_symlink() or not ledger.is_file():
        raise RunnerError("CLAIM_LEDGER_MISSING", "canonical Claim Ledger is missing")
    states: dict[str, str] = {}
    pattern = re.compile(
        r"^\|\s*`(?P<claim>[A-Z][A-Z0-9]*-B\d{2})`\s*"
        r"\|\s*(?P<state>candidate|working|supported|weakened|rejected)\s*\|"
    )
    for line in ledger.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            states[match.group("claim")] = match.group("state")
    if not states:
        raise RunnerError("CLAIM_LEDGER_EMPTY", "canonical Claim Ledger has no active claims")
    return states


def _required_text(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise RunnerError("SCHEMA_INVALID", f"{key} must be non-empty text")
    return value.strip()


def _normalize_updates(
    raw_updates: Any,
    root_source_id: str,
    target_claim_ids: list[str],
    claim_states: dict[str, str],
) -> list[dict[str, str]]:
    if not isinstance(raw_updates, list) or not raw_updates:
        raise RunnerError("SCHEMA_INVALID", "proposed_updates must be a non-empty list")
    if len(raw_updates) > MAX_CLAIMS:
        raise RunnerError("TOO_MANY_CLAIMS", f"proposed_updates exceeds {MAX_CLAIMS}")
    normalized = []
    seen = set()
    for item in raw_updates:
        if not isinstance(item, dict):
            raise RunnerError("SCHEMA_INVALID", "each proposed_update must be an object")
        unknown = set(item) - UPDATE_KEYS
        if unknown:
            raise RunnerError("SCHEMA_INVALID", f"unknown update fields: {sorted(unknown)}")
        claim_id = _required_text(item, "claim_id")
        if claim_id not in claim_states or claim_id not in target_claim_ids:
            raise RunnerError("UNKNOWN_CLAIM", f"claim is not active in canonical ledger: {claim_id}")
        if claim_id in seen:
            raise RunnerError("DUPLICATE_CLAIM", f"duplicate claim in input: {claim_id}")
        seen.add(claim_id)
        old_state = _required_text(item, "old_state")
        if old_state != claim_states[claim_id]:
            raise RunnerError("STALE_CLAIM_STATE", f"old_state is stale for {claim_id}")
        proposed_state = _required_text(item, "proposed_state")
        independence = "same_root" if item.get("independence") == "same_root" else "unknown"
        if independence == "same_root" and proposed_state != old_state:
            raise RunnerError(
                "ILLEGAL_STATE_CHANGE",
                f"same_root update cannot change state for {claim_id}",
            )
        update = {
            "claim_id": claim_id,
            "root_source_id": root_source_id,
            "direction": _required_text(item, "direction"),
            "independence": independence,
            "diagnosticity": _required_text(item, "diagnosticity"),
            "evidence_channel": _required_text(item, "evidence_channel"),
            "updates_dimension": _required_text(item, "updates_dimension"),
            "update_reason": _required_text(item, "update_reason"),
            "counter_explanation": _required_text(item, "counter_explanation"),
            "old_state": old_state,
            "proposed_state": proposed_state,
            "authority": "suggestion_only",
        }
        normalized.append(update)
    if set(target_claim_ids) != seen:
        raise RunnerError(
            "CLAIM_SET_MISMATCH",
            "target_claim_ids must exactly match proposed_updates",
        )
    return normalized


def _normalize_input(
    data: dict[str, Any],
    input_sha256: str,
    repo_root: Path,
) -> dict[str, Any]:
    unknown = set(data) - TOP_LEVEL_KEYS
    if unknown:
        raise RunnerError("SCHEMA_INVALID", f"unknown top-level fields: {sorted(unknown)}")
    _walk_limits(data)
    root_source_id = _required_text(data, "root_source_id")
    if not ROOT_SOURCE_ID_RE.fullmatch(root_source_id):
        raise RunnerError("ROOT_SOURCE_ID_INVALID", "root_source_id format is invalid")
    as_of = _required_text(data, "as_of")
    try:
        date.fromisoformat(as_of)
    except ValueError as exc:
        raise RunnerError("DATE_INVALID", "as_of must use YYYY-MM-DD") from exc
    target_claim_ids = data.get("target_claim_ids")
    if not isinstance(target_claim_ids, list) or not target_claim_ids:
        raise RunnerError("SCHEMA_INVALID", "target_claim_ids must be a non-empty list")
    if len(target_claim_ids) > MAX_CLAIMS:
        raise RunnerError("TOO_MANY_CLAIMS", f"target_claim_ids exceeds {MAX_CLAIMS}")
    if any(not isinstance(x, str) or not CLAIM_ID_RE.fullmatch(x) for x in target_claim_ids):
        raise RunnerError("CLAIM_ID_INVALID", "target_claim_ids contains an invalid claim")
    if len(set(target_claim_ids)) != len(target_claim_ids):
        raise RunnerError("DUPLICATE_CLAIM", "target_claim_ids contains duplicates")
    claim_states = _load_claim_states(repo_root)
    unknown_claims = sorted(set(target_claim_ids) - set(claim_states))
    if unknown_claims:
        raise RunnerError("UNKNOWN_CLAIM", f"claims not in canonical ledger: {unknown_claims}")
    excerpts = data.get("excerpts")
    if not isinstance(excerpts, list) or not excerpts:
        raise RunnerError("SCHEMA_INVALID", "excerpts must be a non-empty list")
    for excerpt in excerpts:
        if not isinstance(excerpt, dict) or set(excerpt) != {"excerpt_id", "text"}:
            raise RunnerError(
                "SCHEMA_INVALID",
                "each excerpt must contain only excerpt_id and text",
            )
        _required_text(excerpt, "excerpt_id")
        _required_text(excerpt, "text")
    moment = data.get("moment_candidate")
    if not isinstance(moment, dict):
        raise RunnerError("SCHEMA_INVALID", "moment_candidate must be an object")
    moment_keys = {
        "old_judgment",
        "new_judgment",
        "next_validation",
        "counter_case",
    }
    if set(moment) != moment_keys:
        raise RunnerError(
            "SCHEMA_INVALID",
            f"moment_candidate must contain exactly {sorted(moment_keys)}",
        )
    for key in moment_keys:
        _required_text(moment, key)
    updates = _normalize_updates(
        data.get("proposed_updates"),
        root_source_id,
        target_claim_ids,
        claim_states,
    )
    return {
        "schema_version": SCHEMA_VERSION,
        "runner_version": RUNNER_VERSION,
        "created_at": _utc_now(),
        "input_sha256": input_sha256,
        "verification_status": "unverified_by_runner",
        "promotion_authority": "none",
        "root_source_id": root_source_id,
        "as_of": as_of,
        "title": _required_text(data, "title"),
        "source_locator": _required_text(data, "source_locator"),
        "source_kind": _required_text(data, "source_kind"),
        "target_claim_ids": target_claim_ids,
        "excerpts": excerpts,
        "moment_candidate": moment,
        "belief_updates": updates,
        "promotion_gate": [
            "Murphy explicit persist",
            "source verification",
            "Reviewer PASS",
            "Validator PASS",
        ],
    }


def _safe_repo_root(repo_root: Path) -> Path:
    root = repo_root.resolve()
    required = root / "05_EVIDENCE_META/_SYSTEM/CLAIM_LEDGER.md"
    if not required.is_file():
        raise RunnerError("REPO_ROOT_INVALID", "repo_root is not an Investment Harness")
    return root


def _assert_safe_output_dir(repo_root: Path, relative: str) -> Path:
    path = repo_root / relative
    current = repo_root
    for part in Path(relative).parts:
        current = current / part
        if current.is_symlink():
            raise RunnerError("OUTPUT_SYMLINK", f"output path contains a symlink: {relative}")
    if not path.is_dir():
        raise RunnerError("OUTPUT_DIR_MISSING", f"output directory is missing: {relative}")
    try:
        path.resolve().relative_to(repo_root)
    except ValueError as exc:
        raise RunnerError("PATH_ESCAPE", "output directory escapes repo_root") from exc
    return path


def _extract_pairs_from_markdown(path: Path) -> set[tuple[str, str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return set()
    roots = set(
        re.findall(
            r"^\s*(?:root_source_id|source_id):\s*[`\"']?([A-Za-z0-9._-]+)",
            text,
            re.MULTILINE,
        )
    )
    claims = set(re.findall(r"\b[A-Z][A-Z0-9]*-B\d{2}\b", text))
    return {(root, claim) for root in roots for claim in claims}


def _historical_pairs(repo_root: Path) -> set[tuple[str, str]]:
    pairs: set[tuple[str, str]] = set()
    for relative in (
        "05_EVIDENCE_META/SOURCES",
        "05_EVIDENCE_META/MOMENTS",
        "05_EVIDENCE_META/_ARCHIVE/MOMENTS",
    ):
        directory = repo_root / relative
        if directory.is_dir():
            for path in directory.rglob("*.md"):
                if not path.is_symlink():
                    pairs.update(_extract_pairs_from_markdown(path))
    staging = repo_root / "90_AUTOMATION/RUNTIME/STAGING"
    if staging.is_dir() and not staging.is_symlink():
        for path in staging.glob("*.json"):
            if path.is_symlink():
                continue
            try:
                record = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, UnicodeError, json.JSONDecodeError):
                continue
            root = record.get("root_source_id")
            claims = record.get("target_claim_ids") or []
            if isinstance(root, str) and isinstance(claims, list):
                pairs.update(
                    (root, claim)
                    for claim in claims
                    if isinstance(claim, str)
                )
    return pairs


def _duplicate_pairs(repo_root: Path, record: dict[str, Any]) -> list[tuple[str, str]]:
    existing = _historical_pairs(repo_root)
    proposed = {
        (record["root_source_id"], claim)
        for claim in record["target_claim_ids"]
    }
    return sorted(existing & proposed)


def _load_validator(repo_root: Path):
    path = repo_root / "90_AUTOMATION/PIPELINES/validate_investment_output.py"
    spec = importlib.util.spec_from_file_location("investment_validator", path)
    if spec is None or spec.loader is None:
        raise RunnerError("VALIDATOR_MISSING", "Validator cannot be loaded")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.run


def _validator_base(as_of: str, write_target: str, content_type: str) -> dict[str, Any]:
    return {
        "harness_task": {
            "lane": "REVIEW",
            "input_type": "AUTOMATION_STAGE",
            "scope": "single",
            "response_mode": "concise",
            "process_depth": "quick",
            "target_ids": [],
            "state_status": "missing",
            "write_intent": "automation_stage",
            "review_required": False,
            "loaded_skills": [],
            "reviewer_agent_mode": "not_required_for_isolated_staging",
        },
        "today": as_of,
        "actor": "automation",
        "write_target": write_target,
        "content_type": content_type,
        "target_preexisted": False,
        "state_expiry_scan": {
            "expired": [],
            "due_for_review": [],
            "missing_time_fields": [],
            "inconsistent": [],
        },
    }


def _preflight_validator(
    repo_root: Path,
    record: dict[str, Any],
    stage_relative: str,
    log_relative: str,
    log_record: dict[str, Any],
) -> None:
    validate = _load_validator(repo_root)
    stage_payload = _validator_base(
        record["as_of"], stage_relative, "automation_staging"
    )
    stage_payload["staging_record"] = record
    stage_payload["belief_updates"] = record["belief_updates"]
    stage_result = validate(stage_payload)
    log_payload = _validator_base(
        record["as_of"], log_relative, "automation_run_log"
    )
    log_payload["run_log_record"] = log_record
    log_result = validate(log_payload)
    if stage_result.get("overall") != "PASS" or log_result.get("overall") != "PASS":
        raise RunnerError("VALIDATOR_BLOCK", "Validator blocked isolated staging")


@contextmanager
def _runner_lock(stage_dir: Path):
    descriptor = os.open(stage_dir, os.O_RDONLY)
    try:
        fcntl.flock(descriptor, fcntl.LOCK_EX)
        yield
    finally:
        fcntl.flock(descriptor, fcntl.LOCK_UN)
        os.close(descriptor)


def _exclusive_json(path: Path, data: dict[str, Any]) -> None:
    encoded = (
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    descriptor = None
    created = False
    try:
        descriptor = os.open(
            path,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL,
            0o600,
        )
        created = True
        with os.fdopen(descriptor, "wb") as handle:
            descriptor = None
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError as exc:
        raise RunnerError("TARGET_EXISTS", "exclusive output target already exists") from exc
    except OSError as exc:
        if created:
            try:
                path.unlink()
            except OSError:
                pass
        raise RunnerError("WRITE_FAILED", "exclusive output write failed") from exc
    finally:
        if descriptor is not None:
            os.close(descriptor)


def _output_paths(
    repo_root: Path,
    root_source_id: str,
    input_sha256: str,
) -> tuple[Path, Path, str, str]:
    basename = f"{root_source_id}--{input_sha256[:12]}.json"
    if not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?--[0-9a-f]{12}\.json", basename):
        raise RunnerError("OUTPUT_NAME_INVALID", "derived output filename is invalid")
    stage_relative = f"90_AUTOMATION/RUNTIME/STAGING/{basename}"
    log_relative = f"90_AUTOMATION/RUN_LOG/{basename}"
    return (
        repo_root / stage_relative,
        repo_root / log_relative,
        stage_relative,
        log_relative,
    )


def run_bundle(repo_root: Path, input_path: Path, mode: str) -> dict[str, Any]:
    if mode not in {"dry-run", "stage"}:
        raise RunnerError("MODE_INVALID", "mode must be dry-run or stage")
    repo_root = _safe_repo_root(repo_root)
    raw, data = _load_json_bytes(input_path)
    input_sha256 = hashlib.sha256(raw).hexdigest()
    if not SHA256_RE.fullmatch(input_sha256):
        raise RunnerError("HASH_INVALID", "input hash generation failed")
    record = _normalize_input(data, input_sha256, repo_root)
    stage_dir = _assert_safe_output_dir(
        repo_root, "90_AUTOMATION/RUNTIME/STAGING"
    )
    _assert_safe_output_dir(repo_root, "90_AUTOMATION/RUN_LOG")
    (
        stage_path,
        log_path,
        stage_relative,
        log_relative,
    ) = _output_paths(repo_root, record["root_source_id"], input_sha256)
    plan = {
        "schema_version": SCHEMA_VERSION,
        "runner_version": RUNNER_VERSION,
        "mode": mode,
        "result": "PLAN_ONLY" if mode == "dry-run" else "PENDING",
        "input_sha256": input_sha256,
        "verification_status": "unverified_by_runner",
        "promotion_authority": "none",
        "planned_paths": [stage_relative, log_relative],
    }
    if mode == "dry-run":
        duplicates = _duplicate_pairs(repo_root, record)
        if duplicates:
            plan["result"] = "NO_INCREMENT"
            plan["duplicate_count"] = len(duplicates)
        return plan

    with _runner_lock(stage_dir):
        duplicates = _duplicate_pairs(repo_root, record)
        if duplicates:
            return {
                **plan,
                "result": "NO_INCREMENT",
                "duplicate_count": len(duplicates),
                "created_paths": [],
            }
        if stage_path.exists() or log_path.exists():
            raise RunnerError("TARGET_EXISTS", "exclusive output target already exists")
        created_at = record["created_at"]
        log_record = {
            "schema_version": SCHEMA_VERSION,
            "runner_version": RUNNER_VERSION,
            "created_at": created_at,
            "input_sha256": input_sha256,
            "mode": "stage",
            "result": "STAGED_UNVERIFIED",
            "created_paths": [stage_relative, log_relative],
            "error_code": None,
        }
        if set(log_record) != LOG_KEYS:
            raise RunnerError("LOG_SCHEMA_INVALID", "run log schema is not minimal")
        _preflight_validator(
            repo_root,
            record,
            stage_relative,
            log_relative,
            log_record,
        )
        created_paths: list[Path] = []
        try:
            _exclusive_json(stage_path, record)
            created_paths.append(stage_path)
            _exclusive_json(log_path, log_record)
            created_paths.append(log_path)
        except RunnerError:
            for created in reversed(created_paths):
                try:
                    created.unlink()
                except OSError:
                    pass
            raise
    return {
        **plan,
        "result": "STAGED_UNVERIFIED",
        "created_paths": [stage_relative, log_relative],
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Stage unverified AI belief updates")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--mode", choices=("dry-run", "stage"), default="dry-run")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help=argparse.SUPPRESS,
    )
    args = parser.parse_args(argv)
    try:
        result = run_bundle(args.repo_root, args.input, args.mode)
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except RunnerError as exc:
        print(
            json.dumps(
                {
                    "schema_version": SCHEMA_VERSION,
                    "runner_version": RUNNER_VERSION,
                    "result": "BLOCKED",
                    "error_code": exc.code,
                    "message": exc.safe_message,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
        )
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
