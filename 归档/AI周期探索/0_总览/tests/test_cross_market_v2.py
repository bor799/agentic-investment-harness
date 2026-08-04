#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = SCRIPT_DIR.parents[1]
sys.path.insert(0, str(SCRIPT_DIR))

from v2_queue import (  # noqa: E402
    EXPECTED_IDS,
    LEDGER_PATH,
    QueueError,
    load_json,
    make_claim,
    mark_failure,
    recover_running,
    validate_object_outcome,
    validate_queue,
)


BASE_QUEUE = SCRIPT_DIR / "cross_market_queue_v2.json"
RUNNER = SCRIPT_DIR / "run_nightly_research_loop.sh"
WRITE_GUARD = SCRIPT_DIR / "v2_write_guard.py"
OUTCOME = SCRIPT_DIR / "v2_last_outcome.json"


class CrossMarketV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = copy.deepcopy(load_json(BASE_QUEUE))
        for item in self.queue["items"]:
            item["status"] = "pending"
            item["attempt_count"] = 0
            item["run_token"] = None
            item["last_error"] = None
        self.queue["final_report"].update(
            {"status": "pending", "attempt_count": 0, "run_token": None, "last_error": None}
        )
        validate_queue(self.queue)

    def claim(self, object_id: str) -> dict:
        return make_claim(self.queue, object_id)

    def base_outcome(self, claim: dict) -> dict:
        item = next(item for item in self.queue["items"] if item["id"] == claim["id"])
        capital = {"ledger_read": False, "ledger_path": None, "ledger_modified": False}
        if item["holding"]:
            capital = {"ledger_read": True, "ledger_path": LEDGER_PATH, "ledger_modified": False}
        options = {"enabled": False, "contract_status": "not_applicable", "designated_contract": False}
        if item["options_enabled"]:
            options = {"enabled": True, "contract_status": "incomplete", "designated_contract": False}
        tool_ticket = None
        if item["special_tool_ticket"] == "etf":
            tool_ticket = {
                "type": "etf",
                "underlying_purity": "checked",
                "concentration": "checked",
                "valuation": "checked",
                "fees": "checked",
                "fund_size": "checked",
                "trading_depth": "checked",
                "tracking_error": "checked",
                "premium_discount": "checked",
                "creation_redemption": "checked",
            }
        elif item["special_tool_ticket"] == "mstr":
            tool_ticket = {
                "type": "mstr",
                "btc_inventory": "checked",
                "btc_per_share": "checked",
                "debt": "checked",
                "convertibles": "checked",
                "preferred_or_other_financing": "checked",
                "dilution": "checked",
                "nav_premium": "checked",
                "financing_loop": "checked",
                "btc_downside_stress": "checked",
                "refinancing_path": "checked",
            }
        return {
            "schema_version": 2,
            "loop_id": "ai-cycle-cross-market-v2",
            "mode": "object",
            "run_token": claim["run_token"],
            "object_id": claim["id"],
            "result": "completed",
            "last_refresh": "2026-07-21T12:00:00+08:00",
            "next_review": "2026-08-01",
            "evidence_gaps": ["next filing"],
            "final_evidence_status": "evidence_complete",
            "probability_status": "uncalibrated",
            "new_facts": True,
            "judgement_changed": False,
            "refresh_note": "新增根证据但判断方向不变",
            "sources": [
                {
                    "url": "https://ir.example.com/filing",
                    "root_domain": "ir.example.com",
                    "source_type": "company_ir",
                    "published_at": "2026-07-20",
                },
                {
                    "url": "https://exchange.example.org/filing",
                    "root_domain": "exchange.example.org",
                    "source_type": "exchange",
                    "published_at": "2026-07-20",
                },
            ],
            "tickets": {
                name: {"state": "unknown", "direction": "unchanged", "basis": "root evidence"}
                for name in ("H_B", "H_R", "H_L", "H_C")
            },
            "tool_ticket": tool_ticket,
            "options": options,
            "capital_ticket": capital,
            "conflicts": [],
            "refresh_file": f"{item['research_dir']}/260721测试_证据状态刷新.md",
            "evidence_log_updated": True,
            "next_signals_updated": True,
            "decision_action": "继续观察",
        }

    def validate(self, object_id: str, mutate=None) -> dict:
        claim = self.claim(object_id)
        item = next(item for item in self.queue["items"] if item["id"] == object_id)
        outcome = self.base_outcome(claim)
        if mutate:
            mutate(outcome)
        validate_object_outcome(outcome, item, check_files=False)
        return outcome

    def test_queue_has_18_unique_objects_in_required_order(self) -> None:
        self.assertEqual([item["id"] for item in self.queue["items"]], EXPECTED_IDS)
        self.assertEqual(len(set(EXPECTED_IDS)), 18)
        self.assertEqual(EXPECTED_IDS.count("lmnd"), 1)

    def test_ordinary_company_outcome(self) -> None:
        outcome = self.validate("meta")
        self.assertIsNone(outcome["tool_ticket"])

    def test_etf_requires_complete_tool_ticket(self) -> None:
        self.validate("star50-etf")
        with self.assertRaises(QueueError):
            self.validate("optical-etf", lambda out: out["tool_ticket"].pop("tracking_error"))

    def test_mstr_uses_special_asset_fields(self) -> None:
        outcome = self.validate("mstr")
        self.assertEqual(outcome["tool_ticket"]["type"], "mstr")
        self.assertIn("btc_per_share", outcome["tool_ticket"])

    def test_existing_holding_must_read_but_not_modify_ledger(self) -> None:
        self.validate("lmnd")
        with self.assertRaises(QueueError):
            self.validate("horizon", lambda out: out["capital_ticket"].update(ledger_read=False))
        with self.assertRaises(QueueError):
            self.validate("miniso", lambda out: out["capital_ticket"].update(ledger_modified=True))

    def test_options_missing_fields_are_incomplete_and_no_contract(self) -> None:
        outcome = self.validate("crcl")
        self.assertEqual(outcome["options"]["contract_status"], "incomplete")
        self.assertFalse(outcome["options"]["designated_contract"])

    def test_options_cannot_claim_complete_with_missing_fields(self) -> None:
        with self.assertRaises(QueueError):
            self.validate("nbis", lambda out: out["options"].update(contract_status="complete"))

    def test_source_conflict_keeps_business_ticket_unchanged(self) -> None:
        def conflict(out: dict) -> None:
            out["final_evidence_status"] = "evidence_conflict"
            out["conflicts"] = [{"field": "revenue", "reason": "different reporting perimeter"}]
            out["tickets"]["H_B"]["direction"] = "unchanged"

        self.validate("oracle", conflict)
        with self.assertRaises(QueueError):
            self.validate("google", lambda out: (conflict(out), out["tickets"]["H_B"].update(direction="up")))

    def test_no_new_evidence_records_judgement_unchanged(self) -> None:
        def no_new(out: dict) -> None:
            out["new_facts"] = False
            out["judgement_changed"] = False
            out["final_evidence_status"] = "no_new_facts"
            out["refresh_note"] = "判断未变；已复查两条根来源"

        self.validate("sf", no_new)
        with self.assertRaises(QueueError):
            self.validate("tianci", lambda out: out.update(new_facts=False, refresh_note="nothing new"))

    def test_news_cannot_directly_raise_business_ticket(self) -> None:
        def news_only(out: dict) -> None:
            out["tickets"]["H_B"]["direction"] = "up"
            for source in out["sources"]:
                source["source_type"] = "news"

        with self.assertRaises(QueueError):
            self.validate("zijin", news_only)

    def test_continuous_failure_exhausts_after_initial_plus_two_retries(self) -> None:
        for expected_status in ("retry", "retry", "failed_after_retries"):
            claim = self.claim("hengtong")
            status = mark_failure(self.queue, "hengtong", claim["run_token"], "synthetic failure")
            self.assertEqual(status, expected_status)
        item = next(item for item in self.queue["items"] if item["id"] == "hengtong")
        self.assertEqual(item["attempt_count"], 3)
        with self.assertRaises(QueueError):
            self.claim("hengtong")

    def test_crash_recovery_returns_running_claim_to_retry(self) -> None:
        self.claim("btgo")
        recovered = recover_running(self.queue)
        self.assertEqual(recovered, ["btgo"])
        item = next(item for item in self.queue["items"] if item["id"] == "btgo")
        self.assertEqual(item["status"], "retry")
        self.assertIsNone(item["run_token"])

    def test_finalize_is_gated_on_all_objects(self) -> None:
        with self.assertRaises(QueueError):
            make_claim(self.queue, "__final__")
        for item in self.queue["items"]:
            item["status"] = "completed"
        claim = make_claim(self.queue, "__final__")
        self.assertEqual(claim["mode"], "finalize")

    def test_dry_run_respects_time_iteration_budget_without_queue_writes(self) -> None:
        before = BASE_QUEUE.read_bytes()
        result = subprocess.run(
            [str(RUNNER), "--dry-run", "--hours", "1.5", "--max-iterations", "19", "--budget-usd", "9.5"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("hours: 1.5", result.stdout)
        self.assertIn("max_iterations: 19", result.stdout)
        self.assertIn("total_budget_usd: 9.5", result.stdout)
        self.assertEqual(before, BASE_QUEUE.read_bytes())
        invalid = subprocess.run(
            [str(RUNNER), "--dry-run", "--hours", "0"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(invalid.returncode, 0)

    def invoke_guard(self, target: Path, permission_mode: str = "acceptEdits") -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory(prefix="v2-guard-test-") as temp_dir:
            queue_path = Path(temp_dir) / "queue.json"
            queue_path.write_text(json.dumps(self.queue, ensure_ascii=False), encoding="utf-8")
            env = os.environ.copy()
            env["AI_CYCLE_V2_QUEUE_FILE"] = str(queue_path)
            payload = {
                "cwd": str(PROJECT_ROOT),
                "permission_mode": permission_mode,
                "tool_name": "Edit",
                "tool_input": {"file_path": str(target), "old_string": "a", "new_string": "b"},
            }
            return subprocess.run(
                [sys.executable, str(WRITE_GUARD)],
                input=json.dumps(payload),
                env=env,
                capture_output=True,
                text=True,
            )

    def test_write_guard_enforces_object_paths_even_in_bypass(self) -> None:
        claim = self.claim("meta")
        research_dir = PROJECT_ROOT / claim["research_dir"]
        self.assertEqual(
            self.invoke_guard(research_dir / "260721Meta_证据状态刷新.md", "bypassPermissions").returncode,
            0,
        )
        self.assertEqual(self.invoke_guard(research_dir / "evidence_log.md").returncode, 0)
        self.assertEqual(self.invoke_guard(OUTCOME, "bypassPermissions").returncode, 0)
        self.assertEqual(self.invoke_guard(BASE_QUEUE, "bypassPermissions").returncode, 2)
        self.assertEqual(self.invoke_guard(PROJECT_ROOT / "outside.md").returncode, 2)

    def test_write_guard_allows_only_final_report_in_archive(self) -> None:
        for item in self.queue["items"]:
            item["status"] = "completed"
        make_claim(self.queue, "__final__")
        allowed = PROJECT_ROOT / "分析报告/archive/260721跨市场_AI周期证据与赔率循环.md"
        denied = PROJECT_ROOT / "分析报告/archive/260721任意报告.md"
        self.assertEqual(self.invoke_guard(allowed).returncode, 0)
        self.assertEqual(self.invoke_guard(denied).returncode, 2)


if __name__ == "__main__":
    unittest.main()
