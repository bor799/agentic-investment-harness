#!/usr/bin/env python3

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[2]
PIPELINES = REPO_ROOT / "90_AUTOMATION/PIPELINES"
sys.path.insert(0, str(PIPELINES))

import ai_belief_loop as runner  # noqa: E402


class TestAiBeliefLoop(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name) / "repo"
        for relative in (
            "05_EVIDENCE_META/_SYSTEM",
            "05_EVIDENCE_META/SOURCES",
            "05_EVIDENCE_META/MOMENTS",
            "05_EVIDENCE_META/_ARCHIVE/MOMENTS",
            "90_AUTOMATION/PIPELINES",
            "90_AUTOMATION/RUNTIME/STAGING",
            "90_AUTOMATION/RUN_LOG",
        ):
            (self.repo / relative).mkdir(parents=True, exist_ok=True)
        (self.repo / "05_EVIDENCE_META/_SYSTEM/CLAIM_LEDGER.md").write_text(
            "| Claim | 当前状态 | 唯一正文 |\n"
            "|---|---|---|\n"
            "| `AI-B01` | working | x |\n"
            "| `ORCL-B02` | working | x |\n",
            encoding="utf-8",
        )
        shutil.copy2(
            PIPELINES / "validate_investment_output.py",
            self.repo / "90_AUTOMATION/PIPELINES/validate_investment_output.py",
        )

    def tearDown(self):
        self.temp.cleanup()

    def _payload(self, **overrides):
        payload = {
            "root_source_id": "SRC-TEST-01",
            "as_of": "2026-07-28",
            "title": "Oracle contract signal",
            "source_locator": "https://example.test/source",
            "source_kind": "formal_disclosure",
            "target_claim_ids": ["ORCL-B02"],
            "verification_status": "verified_by_input",
            "excerpts": [
                {
                    "excerpt_id": "EX-01",
                    "text": "A candidate excerpt that the runner does not verify.",
                }
            ],
            "moment_candidate": {
                "old_judgment": "Demand was unverified.",
                "new_judgment": "The contract may support demand.",
                "next_validation": "Check revenue and customer cash.",
                "counter_case": "The contract may not convert to cash.",
            },
            "proposed_updates": [
                {
                    "claim_id": "ORCL-B02",
                    "direction": "support",
                    "independence": "independent",
                    "diagnosticity": "medium",
                    "evidence_channel": "customer_contract",
                    "updates_dimension": "demand",
                    "update_reason": "Contracted demand may have increased.",
                    "counter_explanation": "It may be cancellable or delayed.",
                    "old_state": "working",
                    "proposed_state": "working",
                    "authority": "auto_apply",
                }
            ],
        }
        payload.update(overrides)
        return payload

    def _input(self, payload=None, name="input.json"):
        path = Path(self.temp.name) / name
        path.write_text(
            json.dumps(payload or self._payload(), ensure_ascii=False),
            encoding="utf-8",
        )
        return path

    def test_default_cli_is_zero_write(self):
        input_path = self._input()
        proc = subprocess.run(
            [
                sys.executable,
                str(PIPELINES / "ai_belief_loop.py"),
                "--input",
                str(input_path),
                "--repo-root",
                str(self.repo),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout)
        self.assertEqual(
            list((self.repo / "90_AUTOMATION/RUNTIME/STAGING").glob("*.json")),
            [],
        )
        self.assertEqual(
            list((self.repo / "90_AUTOMATION/RUN_LOG").glob("*.json")),
            [],
        )

    def test_stage_forces_unverified_suggestion_unknown(self):
        result = runner.run_bundle(self.repo, self._input(), "stage")
        self.assertEqual(result["result"], "STAGED_UNVERIFIED")
        stage_path = self.repo / result["created_paths"][0]
        record = json.loads(stage_path.read_text(encoding="utf-8"))
        self.assertEqual(record["verification_status"], "unverified_by_runner")
        self.assertEqual(record["promotion_authority"], "none")
        self.assertEqual(record["belief_updates"][0]["authority"], "suggestion_only")
        self.assertEqual(record["belief_updates"][0]["independence"], "unknown")
        self.assertFalse(any((self.repo / p).is_file() for p in (
            "05_EVIDENCE_META/SOURCES/new.md",
            "05_EVIDENCE_META/MOMENTS/new.md",
            "05_EVIDENCE_META/KNOWLEDGE/new.md",
            "03_STATE/EXPECTATIONS/new.md",
            "03_STATE/HYPOTHESIS_QUEUE/CURRENT/new.md",
        )))

    def test_root_source_path_traversal_is_rejected(self):
        with self.assertRaises(runner.RunnerError) as context:
            runner.run_bundle(
                self.repo,
                self._input(self._payload(root_source_id="../escape")),
                "dry-run",
            )
        self.assertEqual(context.exception.code, "ROOT_SOURCE_ID_INVALID")

    def test_input_symlink_is_rejected(self):
        real = self._input(name="real.json")
        link = Path(self.temp.name) / "link.json"
        link.symlink_to(real)
        with self.assertRaises(runner.RunnerError) as context:
            runner.run_bundle(self.repo, link, "dry-run")
        self.assertEqual(context.exception.code, "INPUT_SYMLINK")

    def test_output_directory_symlink_is_rejected(self):
        stage = self.repo / "90_AUTOMATION/RUNTIME/STAGING"
        stage.rmdir()
        stage.symlink_to(Path(self.temp.name))
        with self.assertRaises(runner.RunnerError) as context:
            runner.run_bundle(self.repo, self._input(), "dry-run")
        self.assertEqual(context.exception.code, "OUTPUT_SYMLINK")

    def test_existing_target_is_never_overwritten(self):
        input_path = self._input()
        digest = hashlib.sha256(input_path.read_bytes()).hexdigest()
        target = (
            self.repo
            / "90_AUTOMATION/RUNTIME/STAGING"
            / f"SRC-TEST-01--{digest[:12]}.json"
        )
        target.write_text("{}", encoding="utf-8")
        with self.assertRaises(runner.RunnerError) as context:
            runner.run_bundle(self.repo, input_path, "stage")
        self.assertEqual(context.exception.code, "TARGET_EXISTS")
        self.assertEqual(target.read_text(encoding="utf-8"), "{}")

    def test_cross_run_root_claim_duplicate_is_no_increment(self):
        first = runner.run_bundle(self.repo, self._input(), "stage")
        self.assertEqual(first["result"], "STAGED_UNVERIFIED")
        changed = self._payload(title="Same root and claim, different hash")
        second = runner.run_bundle(
            self.repo, self._input(changed, "changed.json"), "stage"
        )
        self.assertEqual(second["result"], "NO_INCREMENT")
        self.assertEqual(len(list(
            (self.repo / "90_AUTOMATION/RUNTIME/STAGING").glob("*.json")
        )), 1)

    def test_unknown_claim_is_rejected(self):
        payload = self._payload(
            target_claim_ids=["UNKNOWN-B01"],
            proposed_updates=[{
                **self._payload()["proposed_updates"][0],
                "claim_id": "UNKNOWN-B01",
            }],
        )
        with self.assertRaises(runner.RunnerError) as context:
            runner.run_bundle(self.repo, self._input(payload), "dry-run")
        self.assertEqual(context.exception.code, "UNKNOWN_CLAIM")

    def test_probability_field_is_rejected(self):
        payload = self._payload()
        payload["proposed_updates"][0]["posterior_probability"] = 0.8
        with self.assertRaises(runner.RunnerError) as context:
            runner.run_bundle(self.repo, self._input(payload), "dry-run")
        self.assertEqual(context.exception.code, "FORBIDDEN_FIELD")

    def test_same_root_state_change_is_rejected(self):
        payload = self._payload()
        payload["proposed_updates"][0]["independence"] = "same_root"
        payload["proposed_updates"][0]["proposed_state"] = "supported"
        with self.assertRaises(runner.RunnerError) as context:
            runner.run_bundle(self.repo, self._input(payload), "dry-run")
        self.assertEqual(context.exception.code, "ILLEGAL_STATE_CHANGE")

    def test_oversized_input_is_rejected(self):
        path = Path(self.temp.name) / "large.json"
        path.write_bytes(b"{" + b"x" * runner.MAX_INPUT_BYTES + b"}")
        with self.assertRaises(runner.RunnerError) as context:
            runner.run_bundle(self.repo, path, "dry-run")
        self.assertEqual(context.exception.code, "INPUT_TOO_LARGE")

    def test_log_is_minimal_and_does_not_copy_excerpt(self):
        result = runner.run_bundle(self.repo, self._input(), "stage")
        log = json.loads(
            (self.repo / result["created_paths"][1]).read_text(encoding="utf-8")
        )
        self.assertEqual(set(log), runner.LOG_KEYS)
        serialized = json.dumps(log, ensure_ascii=False)
        self.assertNotIn("candidate excerpt", serialized.lower())
        self.assertNotIn("source_locator", serialized)

    def test_log_failure_rolls_back_only_this_staging(self):
        original = runner._exclusive_json
        calls = []

        def fail_second(path, data):
            calls.append(path)
            if len(calls) == 2:
                raise runner.RunnerError("WRITE_FAILED", "simulated log failure")
            return original(path, data)

        with mock.patch.object(runner, "_exclusive_json", side_effect=fail_second):
            with self.assertRaises(runner.RunnerError):
                runner.run_bundle(self.repo, self._input(), "stage")
        self.assertEqual(
            list((self.repo / "90_AUTOMATION/RUNTIME/STAGING").glob("*.json")),
            [],
        )
        self.assertEqual(
            list((self.repo / "90_AUTOMATION/RUN_LOG").glob("*.json")),
            [],
        )


if __name__ == "__main__":
    unittest.main()
