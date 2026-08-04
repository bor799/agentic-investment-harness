#!/usr/bin/env python3
"""Persistent queue controller for the cross-market v2 research loop.

The host script owns queue mutations. Claude receives one immutable claim and
writes a validated outcome file; this controller commits the outcome atomically.
Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import copy
import json
import os
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


LOOP_ID = "ai-cycle-cross-market-v2"
EXPECTED_IDS = [
    "lmnd",
    "horizon",
    "miniso",
    "zijin",
    "tianci",
    "hengtong",
    "sf",
    "star50-etf",
    "optical-etf",
    "battery-etf",
    "meta",
    "google",
    "oracle",
    "crcl",
    "nbis",
    "mstr",
    "btgo",
    "pop-mart",
]
OPTION_IDS = {"crcl", "nbis", "mstr", "btgo"}
HOLDING_IDS = {"lmnd", "horizon", "miniso"}
ETF_IDS = {"star50-etf", "optical-etf", "battery-etf"}
ALLOWED_ACTIONS = {
    "不投入",
    "继续观察",
    "建立验证仓",
    "升级确认仓",
    "不加仓",
    "降级或退出",
}
ALLOWED_EVIDENCE_STATUS = {
    "evidence_complete",
    "evidence_limited",
    "evidence_conflict",
    "no_new_facts",
}
ALLOWED_TICKET_STATE = {"pass", "fail", "unknown"}
ALLOWED_DIRECTION = {"up", "down", "unchanged", "unknown"}
ROOT_SOURCE_TYPES = {
    "filing",
    "exchange",
    "company_ir",
    "regulator",
    "index_provider",
    "fund_company",
}
FORBIDDEN_OUTCOME_KEYS = {
    "subjective_probability",
    "probability_percent",
    "likelihood_ratio",
    "evidence_score",
    "total_score",
    "expected_value",
    "ev",
    "ai_vote_count",
}
LEDGER_PATH = "/Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/📈 个人交易手册.md"
PROJECT_ROOT = Path(__file__).resolve().parents[2]


class QueueError(RuntimeError):
    """Raised for invalid queue transitions or outcome payloads."""


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise QueueError(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise QueueError(f"JSON root must be an object: {path}")
    return data


def atomic_write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def append_log(path: Path | None, event: dict[str, Any]) -> None:
    if path is None:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {"logged_at": utc_now(), **event}
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def validate_queue(queue: dict[str, Any]) -> None:
    if queue.get("schema_version") != 2 or queue.get("loop_id") != LOOP_ID:
        raise QueueError("queue schema_version or loop_id is invalid")
    items = queue.get("items")
    if not isinstance(items, list) or len(items) != 18:
        raise QueueError("queue must contain exactly 18 objects")
    ids = [item.get("id") for item in items]
    if ids != EXPECTED_IDS:
        raise QueueError(f"queue order mismatch: {ids}")
    if [item.get("order") for item in items] != list(range(1, 19)):
        raise QueueError("queue order fields must be 1..18")
    required = {
        "display_name",
        "ticker",
        "market",
        "asset_kind",
        "role",
        "status",
        "attempt_count",
        "last_refresh",
        "next_review",
        "research_dir",
        "evidence_gaps",
        "final_evidence_status",
        "options_enabled",
        "holding",
        "special_tool_ticket",
    }
    for item in items:
        missing = sorted(required - set(item))
        if missing:
            raise QueueError(f"{item.get('id')} missing queue fields: {missing}")
        if not isinstance(item["attempt_count"], int) or item["attempt_count"] < 0:
            raise QueueError(f"{item['id']} has invalid attempt_count")
        if item["status"] not in {
            "pending",
            "running",
            "retry",
            "completed",
            "failed_after_retries",
        }:
            raise QueueError(f"{item['id']} has invalid status {item['status']}")
    if {item["id"] for item in items if item["options_enabled"]} != OPTION_IDS:
        raise QueueError("options must be enabled only for CRCL, NBIS, MSTR and BTGO")
    if {item["id"] for item in items if item["holding"]} != HOLDING_IDS:
        raise QueueError("holding flags must identify only LMND, Horizon and Miniso")
    if {item["id"] for item in items if item["special_tool_ticket"] == "etf"} != ETF_IDS:
        raise QueueError("ETF tool-ticket set is invalid")
    mstr = next(item for item in items if item["id"] == "mstr")
    if mstr["special_tool_ticket"] != "mstr" or mstr["asset_kind"] != "special_asset":
        raise QueueError("MSTR must be a special asset with an MSTR tool ticket")
    final_report = queue.get("final_report")
    if not isinstance(final_report, dict) or final_report.get("status") not in {
        "pending",
        "running",
        "retry",
        "completed",
        "failed_after_retries",
    }:
        raise QueueError("final_report state is invalid")


def find_item(queue: dict[str, Any], object_id: str) -> dict[str, Any]:
    for item in queue["items"]:
        if item["id"] == object_id:
            return item
    raise QueueError(f"unknown object id: {object_id}")


def queue_summary(queue: dict[str, Any]) -> dict[str, Any]:
    counts: dict[str, int] = {}
    for item in queue["items"]:
        counts[item["status"]] = counts.get(item["status"], 0) + 1
    return {
        "loop_id": LOOP_ID,
        "objects": len(queue["items"]),
        "counts": counts,
        "final_report_status": queue["final_report"]["status"],
        "all_objects_completed": all(item["status"] == "completed" for item in queue["items"]),
    }


def show_queue(queue: dict[str, Any]) -> None:
    print("ord\tid\tticker\tstatus\tattempts\tresearch_dir")
    for item in queue["items"]:
        print(
            f"{item['order']}\t{item['id']}\t{item['ticker']}\t{item['status']}\t"
            f"{item['attempt_count']}\t{item['research_dir']}"
        )


def recover_running(queue: dict[str, Any]) -> list[str]:
    max_attempts = int(queue.get("max_attempts_per_object", 3))
    recovered: list[str] = []
    for item in queue["items"]:
        if item["status"] != "running":
            continue
        item["status"] = "retry" if item["attempt_count"] < max_attempts else "failed_after_retries"
        item["last_error"] = "recovered_after_interrupted_run"
        item["run_token"] = None
        recovered.append(item["id"])
    final_report = queue["final_report"]
    if final_report["status"] == "running":
        final_report["status"] = (
            "retry" if final_report.get("attempt_count", 0) < max_attempts else "failed_after_retries"
        )
        final_report["last_error"] = "recovered_after_interrupted_run"
        final_report["run_token"] = None
        recovered.append("__final__")
    if recovered:
        queue["updated_at"] = utc_now()
    return recovered


def make_claim(queue: dict[str, Any], requested_id: str | None = None) -> dict[str, Any]:
    max_attempts = int(queue.get("max_attempts_per_object", 3))
    if requested_id == "__final__":
        if not all(item["status"] == "completed" for item in queue["items"]):
            raise QueueError("finalize is unavailable until all 18 objects are completed")
        final_report = queue["final_report"]
        if final_report["status"] not in {"pending", "retry"}:
            raise QueueError(f"final report is not claimable: {final_report['status']}")
        if final_report.get("attempt_count", 0) >= max_attempts:
            raise QueueError("final report retry limit reached")
        token = str(uuid.uuid4())
        final_report["status"] = "running"
        final_report["attempt_count"] = final_report.get("attempt_count", 0) + 1
        final_report["run_token"] = token
        final_report["last_error"] = None
        queue["updated_at"] = utc_now()
        return {
            "mode": "finalize",
            "id": "__final__",
            "display_name": "跨市场汇总",
            "run_token": token,
            "attempt_count": final_report["attempt_count"],
            "report_path_template": final_report["path_template"],
        }

    if requested_id:
        candidate = find_item(queue, requested_id)
        candidates = [candidate]
    else:
        candidates = queue["items"]

    for item in candidates:
        if item["status"] not in {"pending", "retry"}:
            continue
        if item["attempt_count"] >= max_attempts:
            item["status"] = "failed_after_retries"
            continue
        token = str(uuid.uuid4())
        item["status"] = "running"
        item["attempt_count"] += 1
        item["run_token"] = token
        item["last_attempt_at"] = utc_now()
        item["last_error"] = None
        queue["updated_at"] = utc_now()
        claim = copy.deepcopy(item)
        claim["mode"] = "object"
        return claim

    if requested_id:
        raise QueueError(f"object is not claimable: {requested_id}")
    if all(item["status"] == "completed" for item in queue["items"]):
        if queue["final_report"]["status"] in {"pending", "retry"}:
            return make_claim(queue, "__final__")
        raise QueueError(f"all objects complete; final report status={queue['final_report']['status']}")
    exhausted = [item["id"] for item in queue["items"] if item["status"] == "failed_after_retries"]
    if exhausted:
        raise QueueError(f"no claimable work; exhausted objects: {', '.join(exhausted)}")
    raise QueueError("no claimable work")


def forbidden_keys(value: Any, path: str = "$") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key in FORBIDDEN_OUTCOME_KEYS:
                found.append(f"{path}.{key}")
            found.extend(forbidden_keys(child, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(forbidden_keys(child, f"{path}[{index}]"))
    return found


def require_fields(mapping: dict[str, Any], fields: set[str], label: str) -> None:
    missing = sorted(field for field in fields if field not in mapping)
    if missing:
        raise QueueError(f"{label} missing fields: {missing}")


def validate_object_outcome(
    outcome: dict[str, Any], item: dict[str, Any], check_files: bool = False
) -> None:
    if outcome.get("probability_status") != "uncalibrated":
        raise QueueError("probability_status must remain uncalibrated")
    bad_keys = forbidden_keys(outcome)
    if bad_keys:
        raise QueueError(f"forbidden probability/score/EV fields: {bad_keys}")
    if outcome.get("final_evidence_status") not in ALLOWED_EVIDENCE_STATUS:
        raise QueueError("invalid final_evidence_status")
    if outcome.get("decision_action") not in ALLOWED_ACTIONS:
        raise QueueError("decision_action is not one of the six authorized research actions")
    sources = outcome.get("sources")
    if not isinstance(sources, list) or not 2 <= len(sources) <= 5:
        raise QueueError("a completed round must record 2-5 new root sources")
    domains = {source.get("root_domain") for source in sources if source.get("root_domain")}
    if len(domains) < 2:
        raise QueueError("sources must contain at least two independent root domains")
    root_sources = [source for source in sources if source.get("source_type") in ROOT_SOURCE_TYPES]
    if len({source.get("root_domain") for source in root_sources}) < 2:
        raise QueueError("at least two independent filing/official root sources are required")
    for source in sources:
        require_fields(source, {"url", "root_domain", "source_type", "published_at"}, "source")

    tickets = outcome.get("tickets")
    if not isinstance(tickets, dict) or set(tickets) != {"H_B", "H_R", "H_L", "H_C"}:
        raise QueueError("tickets must contain exactly H_B/H_R/H_L/H_C")
    for name, ticket in tickets.items():
        require_fields(ticket, {"state", "direction", "basis"}, name)
        if ticket["state"] not in ALLOWED_TICKET_STATE or ticket["direction"] not in ALLOWED_DIRECTION:
            raise QueueError(f"{name} has an invalid state or direction")
    if tickets["H_B"]["direction"] in {"up", "down"} and not root_sources:
        raise QueueError("news alone cannot change H_B")

    if outcome.get("new_facts") is False:
        if outcome.get("judgement_changed") is not False or "判断未变" not in outcome.get("refresh_note", ""):
            raise QueueError("no-new-facts outcome must explicitly record 判断未变")
    conflicts = outcome.get("conflicts", [])
    if outcome["final_evidence_status"] == "evidence_conflict":
        if not conflicts or tickets["H_B"]["direction"] not in {"unchanged", "unknown"}:
            raise QueueError("source conflict must be recorded without changing H_B")

    capital = outcome.get("capital_ticket")
    if not isinstance(capital, dict):
        raise QueueError("capital_ticket is required")
    require_fields(capital, {"ledger_read", "ledger_path", "ledger_modified"}, "capital_ticket")
    if capital["ledger_modified"] is not False:
        raise QueueError("the portfolio ledger may never be modified")
    if item["holding"]:
        if capital["ledger_read"] is not True or capital["ledger_path"] != LEDGER_PATH:
            raise QueueError("existing holdings must read the portfolio ledger")

    tool_ticket = outcome.get("tool_ticket")
    if item["special_tool_ticket"] == "etf":
        if not isinstance(tool_ticket, dict) or tool_ticket.get("type") != "etf":
            raise QueueError("ETF outcome requires an ETF tool_ticket")
        require_fields(
            tool_ticket,
            {
                "type",
                "underlying_purity",
                "concentration",
                "valuation",
                "fees",
                "fund_size",
                "trading_depth",
                "tracking_error",
                "premium_discount",
                "creation_redemption",
            },
            "ETF tool_ticket",
        )
    elif item["special_tool_ticket"] == "mstr":
        if not isinstance(tool_ticket, dict) or tool_ticket.get("type") != "mstr":
            raise QueueError("MSTR outcome requires an MSTR tool_ticket")
        require_fields(
            tool_ticket,
            {
                "type",
                "btc_inventory",
                "btc_per_share",
                "debt",
                "convertibles",
                "preferred_or_other_financing",
                "dilution",
                "nav_premium",
                "financing_loop",
                "btc_downside_stress",
                "refinancing_path",
            },
            "MSTR tool_ticket",
        )
    elif tool_ticket is not None:
        raise QueueError("ordinary companies must not invent a special tool_ticket")

    options = outcome.get("options")
    if not isinstance(options, dict):
        raise QueueError("options object is required")
    if item["options_enabled"]:
        if options.get("enabled") is not True:
            raise QueueError("options module must be enabled for this object")
        if options.get("contract_status") not in {"complete", "incomplete"}:
            raise QueueError("options contract_status must be complete or incomplete")
        option_fields = {
            "data_time",
            "underlying_price",
            "expiry",
            "strike",
            "bid",
            "ask",
            "midpoint",
            "spread_ratio",
            "iv",
            "iv_percentile",
            "iv_percentile_source",
            "delta",
            "theta",
            "vega",
            "open_interest",
            "volume",
            "exit_depth",
            "catalyst",
            "catalyst_date",
            "max_loss",
            "breakeven",
            "comparison_to_stock",
            "comparison_to_no_action",
            "structure_type",
        }
        missing = sorted(field for field in option_fields if options.get(field) in {None, ""})
        if options["contract_status"] == "complete" and missing:
            raise QueueError(f"complete options record is missing key fields: {missing}")
        if options["contract_status"] == "incomplete" and options.get("designated_contract") is not False:
            raise QueueError("incomplete options data may not designate a contract")
        if options.get("structure_type") not in {None, "", "long_option", "debit_spread"}:
            raise QueueError("only long options or debit spreads may be researched")
    else:
        if options.get("enabled") is not False or options.get("contract_status") != "not_applicable":
            raise QueueError("options must be not_applicable for this object")
        if options.get("designated_contract") is not False:
            raise QueueError("non-options objects cannot designate a contract")

    if outcome.get("evidence_log_updated") is not True or outcome.get("next_signals_updated") is not True:
        raise QueueError("evidence_log.md and next_signals.md must be incrementally updated")
    refresh_file = outcome.get("refresh_file")
    if not isinstance(refresh_file, str) or not refresh_file.startswith(item["research_dir"] + "/"):
        raise QueueError("refresh_file must stay inside the claimed research_dir")
    if not refresh_file.endswith("_证据状态刷新.md"):
        raise QueueError("refresh_file must use the YYMMDD标的_证据状态刷新.md convention")
    if check_files:
        required_paths = [
            PROJECT_ROOT / refresh_file,
            PROJECT_ROOT / item["research_dir"] / "evidence_log.md",
            PROJECT_ROOT / item["research_dir"] / "next_signals.md",
        ]
        missing_paths = [str(path) for path in required_paths if not path.is_file()]
        if missing_paths:
            raise QueueError(f"declared research files do not exist: {missing_paths}")


def validate_finalize_outcome(
    outcome: dict[str, Any], queue: dict[str, Any], check_files: bool = False
) -> None:
    if not all(item["status"] == "completed" for item in queue["items"]):
        raise QueueError("cannot finalize before all 18 objects are completed")
    if outcome.get("source_object_ids") != EXPECTED_IDS:
        raise QueueError("final report must include all 18 object ids in queue order")
    if outcome.get("no_global_score") is not True or outcome.get("no_action_assessed") is not True:
        raise QueueError("final report must reject a global score and assess no-action")
    report_file = outcome.get("report_file")
    if not isinstance(report_file, str) or not report_file.startswith("分析报告/archive/"):
        raise QueueError("final report must be written to 分析报告/archive/")
    if not report_file.endswith("跨市场_AI周期证据与赔率循环.md"):
        raise QueueError("final report filename does not match the required convention")
    if check_files and not (PROJECT_ROOT / report_file).is_file():
        raise QueueError(f"declared final report does not exist: {report_file}")


def validate_outcome(
    outcome: dict[str, Any], queue: dict[str, Any], check_files: bool = False
) -> dict[str, Any] | None:
    if outcome.get("schema_version") != 2 or outcome.get("loop_id") != LOOP_ID:
        raise QueueError("outcome schema_version or loop_id is invalid")
    object_id = outcome.get("object_id")
    if object_id == "__final__":
        final_report = queue["final_report"]
        if outcome.get("mode") != "finalize" or final_report["status"] != "running":
            raise QueueError("finalize outcome does not match a running final claim")
        if outcome.get("run_token") != final_report.get("run_token"):
            raise QueueError("finalize run_token mismatch")
        if outcome.get("result") == "completed":
            validate_finalize_outcome(outcome, queue, check_files)
        elif outcome.get("result") != "retryable_failure":
            raise QueueError("invalid finalize result")
        return None

    item = find_item(queue, str(object_id))
    if outcome.get("mode") != "object" or item["status"] != "running":
        raise QueueError("object outcome does not match a running claim")
    if outcome.get("run_token") != item.get("run_token"):
        raise QueueError("object run_token mismatch")
    if outcome.get("result") == "completed":
        validate_object_outcome(outcome, item, check_files)
    elif outcome.get("result") != "retryable_failure":
        raise QueueError("invalid object result")
    return item


def mark_failure(
    queue: dict[str, Any], object_id: str, run_token: str, error: str
) -> str:
    max_attempts = int(queue.get("max_attempts_per_object", 3))
    if object_id == "__final__":
        target = queue["final_report"]
    else:
        target = find_item(queue, object_id)
    if target.get("status") != "running" or target.get("run_token") != run_token:
        raise QueueError("failure does not match the active claim")
    target["status"] = "retry" if target.get("attempt_count", 0) < max_attempts else "failed_after_retries"
    target["last_error"] = error[:2000]
    target["run_token"] = None
    queue["updated_at"] = utc_now()
    return target["status"]


def apply_outcome(queue: dict[str, Any], outcome: dict[str, Any], check_files: bool = True) -> str:
    item = validate_outcome(outcome, queue, check_files)
    object_id = outcome["object_id"]
    if outcome["result"] == "retryable_failure":
        return mark_failure(
            queue,
            object_id,
            outcome["run_token"],
            str(outcome.get("error", "Claude reported retryable_failure")),
        )
    if object_id == "__final__":
        final_report = queue["final_report"]
        final_report["status"] = "completed"
        final_report["actual_path"] = outcome["report_file"]
        final_report["last_error"] = None
        final_report["run_token"] = None
        queue["updated_at"] = utc_now()
        return "completed"
    assert item is not None
    item["status"] = "completed"
    item["last_refresh"] = outcome["last_refresh"]
    item["next_review"] = outcome["next_review"]
    item["evidence_gaps"] = outcome["evidence_gaps"]
    item["final_evidence_status"] = outcome["final_evidence_status"]
    item["last_error"] = None
    item["run_token"] = None
    queue["updated_at"] = utc_now()
    return "completed"


def command_claim(args: argparse.Namespace) -> int:
    queue_path = Path(args.queue)
    queue = load_json(queue_path)
    validate_queue(queue)
    claim = make_claim(queue, args.id)
    atomic_write_json(queue_path, queue)
    print(json.dumps(claim, ensure_ascii=False))
    return 0


def command_recover(args: argparse.Namespace) -> int:
    queue_path = Path(args.queue)
    queue = load_json(queue_path)
    validate_queue(queue)
    recovered = recover_running(queue)
    if recovered:
        atomic_write_json(queue_path, queue)
    print(json.dumps({"recovered": recovered}, ensure_ascii=False))
    return 0


def command_apply(args: argparse.Namespace) -> int:
    queue_path = Path(args.queue)
    outcome_path = Path(args.outcome)
    queue = load_json(queue_path)
    validate_queue(queue)
    outcome = load_json(outcome_path)
    status = apply_outcome(queue, outcome, check_files=not args.skip_file_check)
    atomic_write_json(queue_path, queue)
    append_log(
        Path(args.run_log) if args.run_log else None,
        {"event": "outcome_applied", "object_id": outcome.get("object_id"), "status": status},
    )
    print(json.dumps({"object_id": outcome.get("object_id"), "status": status}, ensure_ascii=False))
    return 0


def command_fail(args: argparse.Namespace) -> int:
    queue_path = Path(args.queue)
    queue = load_json(queue_path)
    validate_queue(queue)
    status = mark_failure(queue, args.id, args.run_token, args.error)
    atomic_write_json(queue_path, queue)
    append_log(
        Path(args.run_log) if args.run_log else None,
        {"event": "claim_failed", "object_id": args.id, "status": status, "error": args.error},
    )
    print(json.dumps({"object_id": args.id, "status": status}, ensure_ascii=False))
    return 0


def command_show(args: argparse.Namespace) -> int:
    queue = load_json(Path(args.queue))
    validate_queue(queue)
    show_queue(queue)
    return 0


def command_status(args: argparse.Namespace) -> int:
    queue = load_json(Path(args.queue))
    validate_queue(queue)
    print(json.dumps(queue_summary(queue), ensure_ascii=False))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ("show", "status", "recover"):
        sub = subparsers.add_parser(name)
        sub.add_argument("--queue", required=True)
        sub.set_defaults(func=globals()[f"command_{name}"])
    claim = subparsers.add_parser("claim")
    claim.add_argument("--queue", required=True)
    claim.add_argument("--id")
    claim.set_defaults(func=command_claim)
    apply_parser = subparsers.add_parser("apply")
    apply_parser.add_argument("--queue", required=True)
    apply_parser.add_argument("--outcome", required=True)
    apply_parser.add_argument("--run-log")
    apply_parser.add_argument("--skip-file-check", action="store_true")
    apply_parser.set_defaults(func=command_apply)
    fail = subparsers.add_parser("fail")
    fail.add_argument("--queue", required=True)
    fail.add_argument("--id", required=True)
    fail.add_argument("--run-token", required=True)
    fail.add_argument("--error", required=True)
    fail.add_argument("--run-log")
    fail.set_defaults(func=command_fail)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return int(args.func(args))
    except QueueError as exc:
        print(f"queue error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
