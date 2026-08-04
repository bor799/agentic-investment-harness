#!/usr/bin/env python3
"""
Investment Harness Validator 单元测试。

纯标准库（unittest）。每项 V-x 至少一通一败。
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = REPO_ROOT / "90_AUTOMATION/PIPELINES/validate_investment_output.py"

sys.path.insert(0, str(VALIDATOR.parent))

import validate_investment_output as v  # noqa: E402


def _write_temp(payload):
    fd, path = tempfile.mkstemp(suffix=".json")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
    return path


def _run_cli(payload):
    path = _write_temp(payload)
    try:
        proc = subprocess.run(
            [sys.executable, str(VALIDATOR), path],
            capture_output=True, text=True, check=False,
        )
        return proc.returncode, proc.stdout
    finally:
        os.unlink(path)


BASE_TASK = {
    "lane": "JUDGE",
    "input_type": "TARGET",
    "scope": "single",
    "response_mode": "concise",
    "process_depth": "quick",
    "target_ids": ["COIN"],
    "state_status": "missing",
    "write_intent": "chat_only",
    "review_required": False,
    "loaded_skills": [],
    "reviewer_agent_mode": "injected",
}


def _payload(**overrides):
    base = {
        "harness_task": dict(BASE_TASK),
        "today": "2026-07-25",
        "action": "继续观察",
        "H_R": "unknown",
        "odds_calibration": {
            "status": "uncalibrated",
            "market_implied_expectation": "当前资料不足，无法可靠反推",
            "basis_or_boundary": "",
            "missing_evidence": ["当前价格与估值分母"],
        },
        "state_expiry_scan": {
            "expired": [],
            "due_for_review": [],
            "missing_time_fields": [],
            "inconsistent": [],
        },
    }
    for k, val in overrides.items():
        if k == "harness_task":
            base["harness_task"].update(val)
        elif k == "state_expiry_scan":
            base["state_expiry_scan"].update(val)
        else:
            base[k] = val
    return base


def _current_write_payload(**overrides):
    target = "03_STATE/HYPOTHESIS_QUEUE/CURRENT/COIN.md"
    base = _payload(
        harness_task={
            "process_depth": "reviewed",
            "state_status": "current",
            "write_intent": "explicit_persist",
            "review_required": True,
        },
        write_target=target,
        thesis_state={
            "data_cutoff": "2026-07-25",
            "expires_at": "2026-10-23",
            "review_date": "2026-08-25",
            "open_disagreement": "none",
        },
        H_B="unknown：待验证现金流",
        H_R="unknown：估值未校准",
        research_trigger={
            "asset_type": "operating_company",
            "recovery_status": "recovered",
            "why_in_target_library": "用户明确关注其收费权",
            "original_materials": [
                {
                    "path": "/tmp/current-user-thesis.txt",
                    "source_role": "current_user_thesis",
                },
                {
                    "path": "legacy-ai-report.md",
                    "source_role": "ai_exploration",
                },
            ],
            "murphy_prior": [
                {
                    "claim": "收费权需要验证",
                    "basis": "user_explicit",
                    "source_path": "/tmp/current-user-thesis.txt",
                },
            ],
            "ai_extensions": ["历史 AI 推演"],
            "money_path": "收费转成每股现金流",
            "current_validation_question": "毛利是否转成经营现金流",
        },
        asset_validation={
            "route": "operating_company",
            "industry_change": "需求增长",
            "profit_capture": "毛利与现金流",
            "odds": "当前估值未校准",
            "account_fit": "最大损失未知",
        },
        user_facing_summary=(
            "当前继续观察。行业方向存在，但利润、赔率和账户承受力仍待验证。"
        ),
        unknown_resolution=[
            {
                "missing": "经营现金流",
                "why_it_matters": "判断利润是否真实",
                "how_to_verify": "读取下一季度现金流量表",
                "pass_condition": "现金流与利润同步改善",
                "fail_condition": "利润增长但现金流继续恶化",
            },
        ],
        review_result={
            "verdict": "PASS",
            "weakest_link": "现金流",
            "best_bear_case": "利润只是应收扩张",
            "allowed_write_route": target,
            "source_traceability": {
                "root_sources": [
                    {
                        "path_or_url": "/tmp/current-user-thesis.txt",
                        "published_at": "2026-07-25",
                        "data_caliber": "user_thesis",
                    },
                ],
            },
            "odds_calibration_check": {
                "status": "uncalibrated",
                "internally_consistent": True,
                "reason": "缺估值分母",
            },
            "murphy_ai_boundary_check": {
                "status": "pass",
                "reason": "用户判断与历史 AI 分账",
            },
            "asset_route_check": {
                "status": "pass",
                "asset_type": "operating_company",
                "reason": "经营公司路径完整",
            },
        },
    )
    for key, value in overrides.items():
        if key == "harness_task":
            base["harness_task"].update(value)
        elif key in {
            "research_trigger", "asset_validation",
            "review_result", "thesis_state",
        }:
            base[key].update(value)
        else:
            base[key] = value
    return base


class TestV1WritePath(unittest.TestCase):
    def test_pass_chat_only(self):
        r = v.v1_write_path(_payload(), None)
        self.assertEqual(r["status"], "OK")

    def test_pass_automation_stage_path(self):
        r = v.v1_write_path(_payload(
            harness_task={"write_intent": "automation_stage"},
            write_target=(
                "90_AUTOMATION/RUNTIME/STAGING/"
                "SRC-TEST-01--aaaaaaaaaaaa.json"
            ),
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_automation_stage_outside_sink(self):
        r = v.v1_write_path(_payload(
            harness_task={"write_intent": "automation_stage"},
            write_target="05_EVIDENCE_META/KNOWLEDGE/forbidden.json",
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_canonical_sink(self):
        r = v.v1_write_path(_payload(
            harness_task={"write_intent": "explicit_persist"},
            write_target="05_EVIDENCE_META/SOURCES/2026/test.md",
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_outside_sink(self):
        r = v.v1_write_path(_payload(
            harness_task={"write_intent": "explicit_persist"},
            write_target="分析报告/test.md",
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_protected_path(self):
        r = v.v1_write_path(_payload(
            harness_task={"write_intent": "explicit_persist"},
            write_target="01_道/CONSTITUTION.md",
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestV2StateTime(unittest.TestCase):
    def test_pass_missing(self):
        r = v.v2_state_time(_payload(harness_task={"state_status": "missing"}),
                            v.date(2026, 7, 25))
        self.assertEqual(r["status"], "OK")

    def test_pass_current(self):
        r = v.v2_state_time(_payload(
            harness_task={"state_status": "current"},
            thesis_state={
                "data_cutoff": "2026-06-30",
                "expires_at": "2026-08-30",
            },
        ), v.date(2026, 7, 25))
        self.assertEqual(r["status"], "OK")

    def test_fail_expired_marked_current(self):
        r = v.v2_state_time(_payload(
            harness_task={"state_status": "current"},
            thesis_state={
                "data_cutoff": "2026-05-01",
                "expires_at": "2026-06-01",
            },
        ), v.date(2026, 7, 25))
        self.assertEqual(r["status"], "FAIL")

    def test_fail_missing_dates(self):
        r = v.v2_state_time(_payload(
            harness_task={"state_status": "current"},
            thesis_state={},
        ), v.date(2026, 7, 25))
        self.assertEqual(r["status"], "FAIL")


class TestV3ReviewerDerived(unittest.TestCase):
    def test_pass_capital(self):
        r = v.v3_reviewer_derived(_payload(
            harness_task={"input_type": "CAPITAL", "review_required": True},
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_capital_without_reviewer(self):
        r = v.v3_reviewer_derived(_payload(
            harness_task={"input_type": "CAPITAL", "review_required": False},
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_explicit_persist_without_reviewer(self):
        r = v.v3_reviewer_derived(_payload(
            harness_task={"write_intent": "explicit_persist",
                          "review_required": False},
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_voluntary_reviewer(self):
        r = v.v3_reviewer_derived(_payload(
            harness_task={"input_type": "TARGET", "review_required": True},
        ), None)
        self.assertEqual(r["status"], "OK")


class TestV4Action(unittest.TestCase):
    def test_pass_six_tier(self):
        for a in ["不投入", "继续观察", "建立验证仓", "升级确认仓", "不加仓", "降级或退出"]:
            r = v.v4_action(_payload(action=a), None)
            self.assertEqual(r["status"], "OK", a)

    def test_fail_ambiguous(self):
        # 历史报告负例
        for a in ["维持甚至加仓", "降低权重", "谨慎乐观", "逢低吸纳", "波段操作"]:
            r = v.v4_action(_payload(action=a), None)
            self.assertEqual(r["status"], "FAIL", a)

    def test_fail_unknown_action(self):
        r = v.v4_action(_payload(action="稳步建仓"), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_review_lane_no_action(self):
        r = v.v4_action(_payload(harness_task={"lane": "REVIEW"}), None)
        self.assertEqual(r["status"], "OK")


class TestV5SourceFields(unittest.TestCase):
    def test_pass_reviewed_full(self):
        r = v.v5_source_fields(_payload(
            harness_task={"process_depth": "reviewed"},
            review_result={"source_traceability": {"root_sources": [
                {"path_or_url": "https://sec.gov/x",
                 "published_at": "2026-07-01",
                 "data_caliber": "10-Q"},
            ]}},
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_reviewed_no_sources(self):
        r = v.v5_source_fields(_payload(
            harness_task={"process_depth": "reviewed"},
            review_result={"source_traceability": {}},
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_quick_skipped(self):
        r = v.v5_source_fields(_payload(
            harness_task={"process_depth": "quick"},
        ), None)
        self.assertEqual(r["status"], "OK")


class TestV6ReviewerCompleteness(unittest.TestCase):
    def test_pass_full(self):
        r = v.v6_reviewer_completeness(_payload(
            harness_task={"process_depth": "reviewed"},
            review_result={
                "verdict": "PASS",
                "weakest_link": "客户集中度",
                "best_bear_case": "下季度增速转负",
            },
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_pass_without_weakest(self):
        r = v.v6_reviewer_completeness(_payload(
            harness_task={"process_depth": "reviewed"},
            review_result={
                "verdict": "PASS",
                "weakest_link": "none",
                "best_bear_case": "x",
            },
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_pass_without_best_bear(self):
        r = v.v6_reviewer_completeness(_payload(
            harness_task={"process_depth": "reviewed"},
            review_result={
                "verdict": "PASS",
                "weakest_link": "x",
                "best_bear_case": "",
            },
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_explicit_with_exact_route(self):
        r = v.v6_reviewer_completeness(_current_write_payload(), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_explicit_block(self):
        r = v.v6_reviewer_completeness(_current_write_payload(
            review_result={"verdict": "BLOCK"},
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_explicit_route_mismatch(self):
        r = v.v6_reviewer_completeness(_current_write_payload(
            review_result={
                "allowed_write_route":
                    "03_STATE/HYPOTHESIS_QUEUE/CURRENT/OTHER.md",
            },
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestV7CanonicalProtection(unittest.TestCase):
    def test_pass_no_target(self):
        r = v.v7_canonical_protection(_payload(), None)
        self.assertEqual(r["status"], "OK")

    def test_pass_philosophy_inbox(self):
        r = v.v7_canonical_protection(_payload(
            write_target="01_道/PHILOSOPHY_INBOX/c1.md",
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_constitution(self):
        r = v.v7_canonical_protection(_payload(
            write_target="01_道/CONSTITUTION.md",
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_portfolio_ledger(self):
        r = v.v7_canonical_protection(_payload(
            write_target="03_STATE/PORTFOLIO_LEDGER.md",
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestV8Backup(unittest.TestCase):
    def test_pass_new_file(self):
        r = v.v8_backup(_payload(
            write_target="05_EVIDENCE_META/EVIDENCE/COMPANIES/COIN/new.md",
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_pass_existing_with_backup(self):
        # AGENTS.md 存在；用 .harness_backup 内副本模拟
        backup_path = ".harness_backup/20260725-190233/AGENTS.md"
        r = v.v8_backup(_payload(
            write_target="AGENTS.md",
            backup_path=backup_path,
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_existing_without_backup(self):
        r = v.v8_backup(_payload(
            write_target="AGENTS.md",
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_postwrite_new_file(self):
        r = v.v8_backup(_payload(
            write_target="AGENTS.md",
            target_preexisted=False,
        ), None)
        self.assertEqual(r["status"], "OK")


class TestV9StateExpiryScan(unittest.TestCase):
    def test_pass_full(self):
        r = v.v9_state_expiry_scan(_payload(
            state_expiry_scan={
                "expired": [],
                "due_for_review": [],
                "missing_time_fields": [],
                "inconsistent": [],
            },
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_missing_field(self):
        # 直接构造 payload，绕过 _payload 的 merge 默认值
        payload = {
            "harness_task": dict(BASE_TASK),
            "today": "2026-07-25",
            "state_expiry_scan": {"expired": [], "due_for_review": []},
        }
        r = v.v9_state_expiry_scan(payload, None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_no_scan(self):
        payload = {
            "harness_task": dict(BASE_TASK),
            "today": "2026-07-25",
        }
        r = v.v9_state_expiry_scan(payload, None)
        self.assertEqual(r["status"], "FAIL")


class TestV10Disagree(unittest.TestCase):
    def test_pass_no_disagree(self):
        r = v.v10_disagree(_payload(
            review_result={"verdict": "PASS"},
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_disagree_with_write(self):
        r = v.v10_disagree(_payload(
            review_result={"verdict": "DISAGREE"},
            write_target="05_EVIDENCE_META/EVIDENCE/COMPANIES/COIN/x.md",
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_disagree_no_open_field(self):
        r = v.v10_disagree(_payload(
            review_result={"verdict": "DISAGREE"},
            thesis_state={"data_cutoff": "2026-07-01", "expires_at": "2026-09-01"},
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_disagree_with_open(self):
        r = v.v10_disagree(_payload(
            review_result={"verdict": "DISAGREE"},
            thesis_state={"data_cutoff": "2026-07-01", "expires_at": "2026-09-01",
                          "open_disagreement": "reviewer 看空客户集中度"},
        ), None)
        self.assertEqual(r["status"], "OK")


class TestV11ChatOnlyRoute(unittest.TestCase):
    def test_pass_chat_only_empty(self):
        r = v.v11_chat_only_route(_payload(
            harness_task={"write_intent": "chat_only"},
            review_result={"allowed_write_route": ""},
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_chat_only_with_route(self):
        r = v.v11_chat_only_route(_payload(
            harness_task={"write_intent": "chat_only"},
            review_result={"allowed_write_route": "05_EVIDENCE_META/EVIDENCE/COMPANIES/COIN/x.md"},
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestV12BatchCap(unittest.TestCase):
    def test_pass_under_5(self):
        r = v.v12_batch_cap(_payload(
            harness_task={"input_type": "BATCH",
                          "target_ids": ["A", "B", "C"]},
            batch_shown_targets=["A", "B", "C"],
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_pass_over_5_truncated(self):
        targets = [f"T{i}" for i in range(10)]
        r = v.v12_batch_cap(_payload(
            harness_task={"input_type": "BATCH", "target_ids": targets},
            batch_shown_targets=targets[:5],
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_over_5_not_truncated(self):
        targets = [f"T{i}" for i in range(10)]
        r = v.v12_batch_cap(_payload(
            harness_task={"input_type": "BATCH", "target_ids": targets},
            batch_shown_targets=targets[:6],
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestV13BatchLegacyMajority(unittest.TestCase):
    def test_pass_declared(self):
        r = v.v13_batch_legacy_majority(_payload(
            harness_task={"input_type": "BATCH",
                          "target_ids": ["A", "B", "C"],
                          "state_status": "legacy_only"},
            batch_state_gap_declared=True,
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_not_declared(self):
        r = v.v13_batch_legacy_majority(_payload(
            harness_task={"input_type": "BATCH",
                          "target_ids": ["A", "B", "C"],
                          "state_status": "legacy_only"},
            batch_state_gap_declared=False,
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestV14SourceClassification(unittest.TestCase):
    def test_pass_external(self):
        r = v.v14_source_classification(_payload(
            harness_task={"input_type": "CONTENT"},
            review_result={"source_traceability": {"root_sources": [
                {"source_class": "external_publish"},
            ]}},
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_unknown_class(self):
        r = v.v14_source_classification(_payload(
            harness_task={"input_type": "CONTENT"},
            review_result={"source_traceability": {"root_sources": [
                {"source_class": "third_party"},  # 不在允许集
            ]}},
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_missing_class(self):
        r = v.v14_source_classification(_payload(
            harness_task={"input_type": "CONTENT"},
            review_result={"source_traceability": {"root_sources": [{}]}},
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestV15PositionTrigger(unittest.TestCase):
    def test_pass_no_position(self):
        r = v.v15_position_trigger(_payload(
            user_input_raw="想讨论一下 Coinbase 是否值得继续研究",
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_pass_position_with_br_and_freeze(self):
        r = v.v15_position_trigger(_payload(
            user_input_raw="想加 5% 仓位",
            harness_task={"loaded_skills": ["BEHAVIOR_REVIEW"]},
            risk_freeze_acknowledged=True,
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_position_without_br(self):
        r = v.v15_position_trigger(_payload(
            user_input_raw="想加 5% 仓位",
            harness_task={"loaded_skills": ["COMPANY_FUNDAMENTALS"]},
            risk_freeze_acknowledged=True,
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_position_without_freeze(self):
        r = v.v15_position_trigger(_payload(
            user_input_raw="梭哈",
            harness_task={"loaded_skills": ["BEHAVIOR_REVIEW"]},
            risk_freeze_acknowledged=False,
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestV16OddsCalibration(unittest.TestCase):
    def test_pass_calibrated(self):
        r = v.v16_odds_calibration(_payload(
            H_R="pass",
            odds_calibration={
                "status": "calibrated",
                "market_implied_expectation": "当前价格隐含未来两年利润复合增长 20%",
                "basis_or_boundary": "2026-07-25 收盘价与一致口径远期 PE 反推",
                "missing_evidence": [],
            },
        ), None)
        self.assertEqual(r["status"], "OK")


class TestV17ResearchTriggerProvenance(unittest.TestCase):
    def test_pass_full_trigger(self):
        r = v.v17_research_trigger_provenance(
            _current_write_payload(), None,
        )
        self.assertEqual(r["status"], "OK")

    def test_fail_ai_masquerades_as_murphy(self):
        payload = _current_write_payload()
        payload["research_trigger"]["murphy_prior"][0]["basis"] = "ai_exploration"
        r = v.v17_research_trigger_provenance(payload, None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_unconfirmed_trigger_increases_risk(self):
        payload = _current_write_payload(action="建立验证仓")
        payload["research_trigger"]["recovery_status"] = "needs_murphy_confirmation"
        payload["research_trigger"]["murphy_prior"][0]["basis"] = "unknown"
        r = v.v17_research_trigger_provenance(payload, None)
        self.assertEqual(r["status"], "FAIL")


class TestV18AssetRoute(unittest.TestCase):
    def test_pass_operating_company(self):
        r = v.v18_asset_route(_current_write_payload(), None)
        self.assertEqual(r["status"], "OK")

    def test_pass_etf_route(self):
        payload = _current_write_payload()
        payload["research_trigger"]["asset_type"] = "etf"
        payload["asset_validation"] = {
            "route": "etf",
            "industry_policy": "产业催化",
            "funds_relative_strength": "资金趋势待确认",
            "valuation_crowding": "估值待校准",
            "product_fit": "指数权重已核对",
        }
        payload["review_result"]["asset_route_check"] = {
            "status": "pass",
            "asset_type": "etf",
            "reason": "ETF 四项路径完整",
        }
        r = v.v18_asset_route(payload, None)
        self.assertEqual(r["status"], "OK")

    def test_fail_etf_uses_company_route(self):
        payload = _current_write_payload()
        payload["research_trigger"]["asset_type"] = "etf"
        r = v.v18_asset_route(payload, None)
        self.assertEqual(r["status"], "FAIL")


class TestV19UserOutputAndUnknowns(unittest.TestCase):
    def test_pass_natural_language(self):
        r = v.v19_user_output_and_unknowns(
            _current_write_payload(), None,
        )
        self.assertEqual(r["status"], "OK")

    def test_fail_internal_code_leak(self):
        r = v.v19_user_output_and_unknowns(_current_write_payload(
            user_facing_summary="H_R 未校准，所以继续观察。",
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_unknown_without_resolution(self):
        r = v.v19_user_output_and_unknowns(_current_write_payload(
            unknown_resolution=[],
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_incomplete_resolution(self):
        r = v.v19_user_output_and_unknowns(_current_write_payload(
            unknown_resolution=[{"missing": "现金流"}],
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_bounded_unknown(self):
        r = v.v16_odds_calibration(_payload(
            H_R="mixed",
            odds_calibration={
                "status": "bounded_unknown",
                "market_implied_expectation": "只能确认价格隐含利润率高于当前水平",
                "basis_or_boundary": "上界按同业成熟利润率，下界按当前利润率",
                "missing_evidence": ["分部利润率"],
            },
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_missing_odds_block(self):
        r = v.v16_odds_calibration(_payload(
            odds_calibration={},
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_uncalibrated_marked_mixed(self):
        r = v.v16_odds_calibration(_payload(
            H_R="mixed",
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_reviewed_without_reviewer_check(self):
        r = v.v16_odds_calibration(_payload(
            harness_task={"process_depth": "reviewed"},
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_reviewed_with_matching_check(self):
        r = v.v16_odds_calibration(_payload(
            harness_task={"process_depth": "reviewed"},
            review_result={
                "odds_calibration_check": {
                    "status": "uncalibrated",
                    "internally_consistent": True,
                    "reason": "缺当前价格与估值分母，未声称赔率改善",
                },
            },
        ), None)
        self.assertEqual(r["status"], "OK")


class TestEndToEnd(unittest.TestCase):
    def test_clean_chat_only_target(self):
        payload = _payload()
        code, out = _run_cli(payload)
        self.assertEqual(code, 0, out)
        report = json.loads(out)
        self.assertEqual(report["overall"], "PASS")

    def test_blocked_constitution_write(self):
        payload = _payload(
            harness_task={"write_intent": "explicit_persist",
                          "review_required": True,
                          "input_type": "CAPITAL"},
            write_target="01_道/CONSTITUTION.md",
            review_result={"verdict": "PASS",
                           "weakest_link": "x",
                           "best_bear_case": "y"},
            state_expiry_scan={"expired": [], "due_for_review": [],
                               "missing_time_fields": [], "inconsistent": []},
        )
        code, out = _run_cli(payload)
        self.assertNotEqual(code, 0, out)
        report = json.loads(out)
        self.assertEqual(report["overall"], "FAIL")
        codes = [c["code"] for c in report["checks"] if c["status"] == "FAIL"]
        self.assertIn("V-7", codes)


# ---------------------------------------------------------------------------
# Domain Model 校验测试（D-1 ~ D-8）
# ---------------------------------------------------------------------------

def _domain_payload(**overrides):
    """生成一个最小合法的领域写入 payload。"""
    base = {
        "harness_task": {
            "lane": "JUDGE",
            "input_type": "TARGET",
            "scope": "domain",
            "response_mode": "concise",
            "process_depth": "reviewed",
            "write_intent": "explicit_persist",
            "review_required": True,
            "domain_ids": ["AI"],
        },
        "today": "2026-07-27",
        "write_target": "03_STATE/DOMAIN_MODELS/AI/THESES/AI_PHYSICAL_INFRASTRUCTURE.md",
        "thesis_state": {
            "thesis_id": "AI_PHYSICAL_INFRASTRUCTURE",
            "domain_id": "AI",
            "thesis_status": "working",
            "data_cutoff": "2026-07-27",
            "expires_at": "2027-01-23",
            "review_date": "2026-08-26",
        },
        "last_reviewer": "PASS | independent_readonly | 2026-07-27",
        "review_result": {
            "verdict": "PASS",
            "weakest_link": "瓶颈迁移而非消失，单点投资纯度下降",
            "best_bear_case": "大型云厂商同步缩减 capex",
            "allowed_write_route": "03_STATE/DOMAIN_MODELS/AI/THESES/AI_PHYSICAL_INFRASTRUCTURE.md",
        },
        "proposed_body": _DOMAIN_THESIS_BODY,
        "state_expiry_scan": {
            "expired": [], "due_for_review": [],
            "missing_time_fields": [], "inconsistent": [],
        },
    }
    for k, val in overrides.items():
        if k == "harness_task":
            base["harness_task"].update(val)
        else:
            base[k] = val
    return base


_DOMAIN_THESIS_BODY = """# AI 物理基础设施瓶颈

## 因果链

### Murphy confirmed
- AI 基础设施是互补系统

### Co-created working thesis
- 需求→资本开支→工程约束

### AI extension
- 旧报告历史排序

## 利润池

### Murphy confirmed
- 高端加速器

### Co-created working thesis
- 网络硅

### AI extension
- 历史推断

## 可投资点

### Murphy confirmed
- NVDA

### Co-created working thesis
- 电力公用事业候选

### AI extension
- 旧报告清单

## 绕开路径

### Murphy confirmed
- SDN

### Co-created working thesis
- 光模块下沉

### AI extension
- 历史叙事

## 失败条件

### Murphy confirmed
- 云厂商缩减 capex

### Co-created working thesis
- 瓶颈被绕开

### AI extension
- 历史失败条件
"""


class TestD1DomainPath(unittest.TestCase):
    def test_pass_ai_thesis_write(self):
        r = v.d1_domain_path(_domain_payload(), None)
        self.assertEqual(r["status"], "OK")

    def test_pass_skip_non_domain_write(self):
        r = v.d1_domain_path(_domain_payload(
            write_target="03_STATE/HYPOTHESIS_QUEUE/CURRENT/COIN.md",
        ), None)
        self.assertEqual(r["status"], "OK")  # 跳过

    def test_fail_undeclared_domain(self):
        r = v.d1_domain_path(_domain_payload(
            write_target="03_STATE/DOMAIN_MODELS/AI/unknown.md",
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestD2DomainRegistered(unittest.TestCase):
    def test_pass_ai(self):
        r = v.d2_domain_registered(_domain_payload(), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_crypto_not_registered(self):
        r = v.d2_domain_registered(_domain_payload(
            write_target="03_STATE/DOMAIN_MODELS/CRYPTO/README.md",
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_skip_non_domain(self):
        r = v.d2_domain_registered(_domain_payload(
            write_target="03_STATE/HYPOTHESIS_QUEUE/CURRENT/COIN.md",
        ), None)
        self.assertEqual(r["status"], "OK")


class TestD3ThesisStatusEnum(unittest.TestCase):
    def test_pass_working(self):
        r = v.d3_thesis_status_enum(_domain_payload(), None)
        self.assertEqual(r["status"], "OK")

    def test_pass_validated(self):
        r = v.d3_thesis_status_enum(_domain_payload(
            thesis_state={"thesis_status": "validated",
                           "data_cutoff": "2026-07-27",
                           "expires_at": "2027-01-23",
                           "review_date": "2026-08-26"},
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_invalid_status(self):
        r = v.d3_thesis_status_enum(_domain_payload(
            thesis_state={"thesis_status": "approved",
                           "data_cutoff": "2026-07-27",
                           "expires_at": "2027-01-23",
                           "review_date": "2026-08-26"},
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_skip_non_thesis(self):
        r = v.d3_thesis_status_enum(_domain_payload(
            write_target="03_STATE/DOMAIN_MODELS/AI/INVESTMENT_MAP.md",
        ), None)
        self.assertEqual(r["status"], "OK")


class TestD4TimeTriple(unittest.TestCase):
    def test_pass_valid_triple(self):
        r = v.d4_time_triple(_domain_payload(), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_missing_field(self):
        r = v.d4_time_triple(_domain_payload(
            thesis_state={"data_cutoff": "2026-07-27",
                          "expires_at": "2027-01-23"},  # 缺 review_date
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_thesis_over_180_days(self):
        r = v.d4_time_triple(_domain_payload(
            thesis_state={"data_cutoff": "2026-07-27",
                          "expires_at": "2027-02-15",  # > 180d
                          "review_date": "2026-08-26"},
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_map_over_90_days(self):
        r = v.d4_time_triple(_domain_payload(
            write_target="03_STATE/DOMAIN_MODELS/AI/INVESTMENT_MAP.md",
            investment_map_state={
                "data_cutoff": "2026-07-27",
                "expires_at": "2026-11-15",  # > 90d
                "review_date": "2026-08-26",
            },
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_review_too_far(self):
        r = v.d4_time_triple(_domain_payload(
            thesis_state={"data_cutoff": "2026-07-27",
                          "expires_at": "2027-01-23",
                          "review_date": "2026-10-27"},  # > 31d
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestD5NoCapitalAction(unittest.TestCase):
    def test_pass_clean(self):
        r = v.d5_no_capital_action(_domain_payload(), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_target_price_in_frontmatter(self):
        r = v.d5_no_capital_action(_domain_payload(
            thesis_state={"thesis_status": "working",
                          "target_price": 200,
                          "data_cutoff": "2026-07-27",
                          "expires_at": "2027-01-23",
                          "review_date": "2026-08-26"},
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_position_size_in_body(self):
        r = v.d5_no_capital_action(_domain_payload(
            proposed_body="## 可投资点\n建议 position_size: 5%\n",
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_weight_in_body(self):
        r = v.d5_no_capital_action(_domain_payload(
            proposed_body="## 可投资点\n- NVDA weight: 0.3\n",
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_skip_non_domain(self):
        r = v.d5_no_capital_action(_domain_payload(
            write_target="03_STATE/HYPOTHESIS_QUEUE/CURRENT/COIN.md",
            harness_task={"write_intent": "explicit_persist"},
        ), None)
        self.assertEqual(r["status"], "OK")


class TestD6MurphyAiSplit(unittest.TestCase):
    def test_pass_three_sections(self):
        r = v.d6_murphy_ai_split(_domain_payload(), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_missing_ai_extension(self):
        body = _DOMAIN_THESIS_BODY.replace("### AI extension", "### 历史")
        r = v.d6_murphy_ai_split(_domain_payload(proposed_body=body), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_missing_section(self):
        body = _DOMAIN_THESIS_BODY.replace("## 失败条件", "## 风险")
        r = v.d6_murphy_ai_split(_domain_payload(proposed_body=body), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_skip_non_thesis(self):
        r = v.d6_murphy_ai_split(_domain_payload(
            write_target="03_STATE/DOMAIN_MODELS/AI/README.md",
        ), None)
        self.assertEqual(r["status"], "OK")


class TestD7CanonicalSinkMatch(unittest.TestCase):
    def test_pass_registered_sink(self):
        r = v.d7_canonical_sink_match(_domain_payload(), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_random_path(self):
        # 一个不在 sink 列表里的 domain 路径
        r = v.d7_canonical_sink_match(_domain_payload(
            write_target="03_STATE/DOMAIN_MODELS/CRYPTO/README.md",
            harness_task={"write_intent": "explicit_persist"},
        ), None)
        # CRYPTO/README.md 命中 "03_STATE/DOMAIN_MODELS/" sink，所以 D-7 应 PASS
        # D-2 会拒；这里只确认 D-7 自己不拒
        self.assertEqual(r["status"], "OK")

    def test_pass_skip_non_domain(self):
        r = v.d7_canonical_sink_match(_domain_payload(
            write_target="05_EVIDENCE_META/EVIDENCE/THEMES/x.md",
            harness_task={"write_intent": "explicit_persist"},
        ), None)
        self.assertEqual(r["status"], "OK")


class TestD8ReviewerPass(unittest.TestCase):
    def test_pass_with_pass(self):
        r = v.d8_reviewer_pass(_domain_payload(), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_pending(self):
        r = v.d8_reviewer_pass(_domain_payload(
            last_reviewer="pending",
            thesis_state={"last_reviewer": "pending",
                          "data_cutoff": "2026-07-27",
                          "expires_at": "2027-01-23",
                          "review_date": "2026-08-26",
                          "thesis_status": "working"},
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_missing_timestamp(self):
        r = v.d8_reviewer_pass(_domain_payload(
            last_reviewer="PASS | independent_readonly",
            thesis_state={"last_reviewer": "PASS | independent_readonly",
                          "data_cutoff": "2026-07-27",
                          "expires_at": "2027-01-23",
                          "review_date": "2026-08-26",
                          "thesis_status": "working"},
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_disagree_silent_promote(self):
        r = v.d8_reviewer_pass(_domain_payload(
            last_reviewer="PASS | DISAGREE | 2026-07-27",
            thesis_state={"last_reviewer": "PASS | DISAGREE | 2026-07-27",
                          "data_cutoff": "2026-07-27",
                          "expires_at": "2027-01-23",
                          "review_date": "2026-08-26",
                          "thesis_status": "working"},
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_review_verdict_disagree(self):
        r = v.d8_reviewer_pass(_domain_payload(
            review_result={"verdict": "DISAGREE"},
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_skip_non_domain(self):
        r = v.d8_reviewer_pass(_domain_payload(
            write_target="03_STATE/HYPOTHESIS_QUEUE/CURRENT/COIN.md",
            harness_task={"write_intent": "explicit_persist"},
        ), None)
        self.assertEqual(r["status"], "OK")


def _belief(**overrides):
    item = {
        "claim_id": "AI-B01",
        "proposition": "生产 Agent 需要治理层",
        "origin": "murphy_explicit",
        "origin_ref": "05_EVIDENCE_META/SOURCES/2026/x.md#EX-01",
        "state": "working",
        "mechanism": "生产任务需要权限和回退",
        "supports_if": "企业付费部署",
        "weakens_if": "裸模型长期稳定承担关键任务",
        "cannot_prove": "第三方一定获利",
        "alternative_model": "云厂商免费打包",
        "source_refs": ["05_EVIDENCE_META/SOURCES/2026/x.md#EX-01"],
        "latest_moment": "MOM-1",
    }
    item.update(overrides)
    return item


def _belief_update(**overrides):
    item = {
        "claim_id": "AI-B01",
        "root_source_id": "SRC-1",
        "direction": "support",
        "independence": "independent",
        "diagnosticity": "medium",
        "evidence_channel": "operating",
        "updates_dimension": "demand",
        "update_reason": "新增企业合同",
        "counter_explanation": "可能是试点预算",
        "old_state": "working",
        "proposed_state": "supported",
        "authority": "suggestion_only",
    }
    item.update(overrides)
    return item


def _expectation(**overrides):
    item = {
        "forecast_id": "EXP-ORCL-1",
        "forecast_version": "v1",
        "claim_ids": ["ORCL-B02"],
        "scope": "ORCL",
        "as_of": "2026-07-28",
        "frozen_as_of": "2026-07-28",
        "state": "frozen",
        "settlement_date": "unknown",
        "settlement_date_status": "not_announced",
        "settlement_event": "next_official_results",
        "expected_window": {
            "start": "2026-09-01",
            "end": "2026-10-15",
        },
        "review_by": "2026-08-15",
        "own_range": {
            "stronger": "现金改善",
            "inline": "收入增长但现金弱",
            "weaker": "融资快于利用率",
        },
    }
    item.update(overrides)
    return item


class TestK1ContentTypePath(unittest.TestCase):
    def test_pass_domain_knowledge(self):
        r = v.k1_content_type_path(_payload(
            write_target="05_EVIDENCE_META/KNOWLEDGE/DOMAINS/AI/README.md",
            content_type="domain_knowledge",
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_type_path_mismatch(self):
        r = v.k1_content_type_path(_payload(
            write_target="05_EVIDENCE_META/SOURCES/2026/x.md",
            content_type="entity_knowledge",
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestK2BeliefContract(unittest.TestCase):
    def test_pass_atomic_belief(self):
        r = v.k2_belief_contract(_payload(
            content_type="domain_knowledge",
            beliefs=[_belief()],
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_murphy_without_excerpt(self):
        r = v.k2_belief_contract(_payload(
            content_type="domain_knowledge",
            beliefs=[_belief(
                origin_ref="summary.md",
                source_refs=["summary.md"],
            )],
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_subjective_probability(self):
        r = v.k2_belief_contract(_payload(
            content_type="domain_knowledge",
            beliefs=[_belief()],
            proposed_body="主观胜率：70%",
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestK3LjgBoundary(unittest.TestCase):
    def test_pass_readonly_projection(self):
        r = v.k3_ljg_projection_boundary(_payload(
            lens_output={"new_order": "企业任务控制平面", "flywheel": "使用到现金"},
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_capital_action(self):
        r = v.k3_ljg_projection_boundary(_payload(
            lens_output={"exchange": "建议投资并建立验证仓"},
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_old_path_or_authority(self):
        r = v.k3_ljg_projection_boundary(_payload(
            lens_output={"path": "分析报告/archive", "status": "murphy_confirmed"},
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestK4SingleCanonical(unittest.TestCase):
    def test_pass_one_active(self):
        r = v.k4_single_active_canonical(_payload(canonical_registry=[
            {"role": "claim_ledger", "path": "05/_SYSTEM/CLAIM.md", "status": "active"},
            {"role": "claim_ledger", "path": "05/META/CLAIM.md", "status": "superseded"},
        ]), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_two_active(self):
        r = v.k4_single_active_canonical(_payload(canonical_registry=[
            {"role": "claim_ledger", "path": "new.md", "status": "active"},
            {"role": "claim_ledger", "path": "old.md", "status": "active"},
        ]), None)
        self.assertEqual(r["status"], "FAIL")


class TestU1BeliefUpdate(unittest.TestCase):
    def test_pass_suggestion(self):
        r = v.u1_belief_update_contract(_payload(
            belief_update=_belief_update(),
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_applied_or_numeric(self):
        r = v.u1_belief_update_contract(_payload(
            belief_update=_belief_update(applied=True, posterior_probability=0.8),
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_authority(self):
        r = v.u1_belief_update_contract(_payload(
            belief_update=_belief_update(authority="auto_apply"),
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestU2RootDedupe(unittest.TestCase):
    def test_fail_duplicate_root(self):
        r = v.u2_root_source_dedupe(_payload(
            belief_updates=[_belief_update(), _belief_update()],
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_same_root_changes_state(self):
        r = v.u2_root_source_dedupe(_payload(
            belief_update=_belief_update(independence="same_root"),
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_same_root_no_change(self):
        r = v.u2_root_source_dedupe(_payload(
            belief_update=_belief_update(
                independence="same_root",
                direction="no_change",
                proposed_state="working",
            ),
        ), None)
        self.assertEqual(r["status"], "OK")


class TestU3ChannelBoundary(unittest.TestCase):
    def test_fail_price_updates_operating(self):
        r = v.u3_evidence_channel_boundary(_payload(
            belief_update=_belief_update(
                evidence_channel="market_price",
                updates_dimension="profit",
            ),
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_price_updates_expectation(self):
        r = v.u3_evidence_channel_boundary(_payload(
            belief_update=_belief_update(
                evidence_channel="market_flow",
                updates_dimension="market_expectation",
            ),
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_financing_updates_demand(self):
        r = v.u3_evidence_channel_boundary(_payload(
            belief_update=_belief_update(
                evidence_channel="formal_financing",
                updates_dimension="demand",
            ),
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestE1Expectation(unittest.TestCase):
    def test_pass_unknown_date_with_window(self):
        r = v.e1_expectation_contract(_payload(
            active_expectation=_expectation(),
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_unknown_date_without_window(self):
        r = v.e1_expectation_contract(_payload(
            active_expectation=_expectation(expected_window={}),
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_resolved_without_source(self):
        r = v.e1_expectation_contract(_payload(
            active_expectation=_expectation(
                state="resolved",
                settlement_date="2026-09-10",
                settlement_date_status="announced",
            ),
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestE2FundingLedger(unittest.TestCase):
    def test_pass_separate_buckets(self):
        r = v.e2_funding_ledger(_payload(funding_ledger=[
            {"metric": "RPO", "bucket": "customer_commitment"},
            {"metric": "customer_prepayment", "bucket": "customer_cash"},
            {"metric": "debt", "bucket": "formal_financing"},
        ]), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_rpo_as_cash(self):
        r = v.e2_funding_ledger(_payload(funding_ledger=[
            {"metric": "RPO", "bucket": "customer_cash"},
        ]), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_duplicate_metric(self):
        r = v.e2_funding_ledger(_payload(funding_ledger=[
            {"metric": "equity", "bucket": "formal_financing"},
            {"metric": "equity", "bucket": "customer_cash"},
        ]), None)
        self.assertEqual(r["status"], "FAIL")


class TestE3FrozenVersion(unittest.TestCase):
    def test_fail_overwrite(self):
        r = v.e3_frozen_version(_payload(
            active_expectation=_expectation(),
            overwrite_previous=True,
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_same_version_update(self):
        r = v.e3_frozen_version(_payload(
            active_expectation=_expectation(),
            is_update=True,
            previous_forecast_version="v1",
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_new_version(self):
        r = v.e3_frozen_version(_payload(
            active_expectation=_expectation(forecast_version="v2"),
            is_update=True,
            previous_forecast_version="v1",
        ), None)
        self.assertEqual(r["status"], "OK")


class TestA1AutomationAuthority(unittest.TestCase):
    def test_pass_isolated_staging(self):
        r = v.a1_automation_authority(_payload(
            actor="automation",
            write_target=(
                "90_AUTOMATION/RUNTIME/STAGING/"
                "SRC-TEST-01--aaaaaaaaaaaa.json"
            ),
            belief_update=_belief_update(),
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_source_write(self):
        r = v.a1_automation_authority(_payload(
            actor="automation",
            write_target="05_EVIDENCE_META/SOURCES/2026/260728_x.md",
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_moment_write(self):
        r = v.a1_automation_authority(_payload(
            actor="automation",
            write_target="05_EVIDENCE_META/MOMENTS/260728_x.md",
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_knowledge_write(self):
        r = v.a1_automation_authority(_payload(
            actor="automation",
            write_target="05_EVIDENCE_META/KNOWLEDGE/DOMAINS/AI/README.md",
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_current_write(self):
        r = v.a1_automation_authority(_payload(
            actor="automation",
            write_target="03_STATE/HYPOTHESIS_QUEUE/CURRENT/ORCL.md",
        ), None)
        self.assertEqual(r["status"], "FAIL")


def _staging_record(**overrides):
    digest = "a" * 64
    base = {
        "schema_version": "ai-belief-loop-staging-v1",
        "runner_version": "1.0.0",
        "created_at": "2026-07-28T00:00:00+00:00",
        "input_sha256": digest,
        "verification_status": "unverified_by_runner",
        "promotion_authority": "none",
        "root_source_id": "SRC-TEST-01",
        "target_claim_ids": ["AI-B01"],
        "belief_updates": [
            _belief_update(
                claim_id="AI-B01",
                root_source_id="SRC-TEST-01",
                independence="unknown",
            )
        ],
    }
    base.update(overrides)
    return base


def _run_log_record(**overrides):
    base = {
        "schema_version": "ai-belief-loop-staging-v1",
        "runner_version": "1.0.0",
        "created_at": "2026-07-28T00:00:00+00:00",
        "input_sha256": "a" * 64,
        "mode": "stage",
        "result": "STAGED_UNVERIFIED",
        "created_paths": [
            "90_AUTOMATION/RUNTIME/STAGING/SRC-TEST-01--aaaaaaaaaaaa.json",
            "90_AUTOMATION/RUN_LOG/SRC-TEST-01--aaaaaaaaaaaa.json",
        ],
        "error_code": None,
    }
    base.update(overrides)
    return base


class TestA2AutomationStagingContract(unittest.TestCase):
    def test_pass_staging(self):
        record = _staging_record()
        r = v.a2_automation_staging_contract(_payload(
            actor="automation",
            content_type="automation_staging",
            write_target=(
                "90_AUTOMATION/RUNTIME/STAGING/"
                "SRC-TEST-01--aaaaaaaaaaaa.json"
            ),
            staging_record=record,
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_readme_or_extension(self):
        r = v.a2_automation_staging_contract(_payload(
            actor="automation",
            content_type="automation_staging",
            write_target="90_AUTOMATION/RUNTIME/STAGING/README.md",
            staging_record=_staging_record(),
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_claims_independent(self):
        record = _staging_record()
        record["belief_updates"][0]["independence"] = "independent"
        r = v.a2_automation_staging_contract(_payload(
            actor="automation",
            content_type="automation_staging",
            write_target=(
                "90_AUTOMATION/RUNTIME/STAGING/"
                "SRC-TEST-01--aaaaaaaaaaaa.json"
            ),
            staging_record=record,
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_pass_run_log(self):
        r = v.a2_automation_staging_contract(_payload(
            actor="automation",
            content_type="automation_run_log",
            write_target=(
                "90_AUTOMATION/RUN_LOG/"
                "SRC-TEST-01--aaaaaaaaaaaa.json"
            ),
            run_log_record=_run_log_record(),
        ), None)
        self.assertEqual(r["status"], "OK")


class TestA3RunLogSanitization(unittest.TestCase):
    def test_pass_minimal_log(self):
        r = v.a3_run_log_sanitization(_payload(
            actor="automation",
            content_type="automation_run_log",
            run_log_record=_run_log_record(),
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_excerpt_leak(self):
        record = _run_log_record()
        record["excerpt"] = "sensitive source text"
        r = v.a3_run_log_sanitization(_payload(
            actor="automation",
            content_type="automation_run_log",
            run_log_record=record,
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestD6OutlookCompatibility(unittest.TestCase):
    def test_pass_outlook_without_belief(self):
        r = v.d6_murphy_ai_split(_domain_payload(
            primary_role="domain_outlook",
            domain_outlook={"outlook_status": "active"},
            proposed_body="# Outlook\n\n只保存验证窗口与 claim 反链。",
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_outlook_duplicates_belief(self):
        r = v.d6_murphy_ai_split(_domain_payload(
            primary_role="domain_outlook",
            domain_outlook={"outlook_status": "active"},
            proposed_body="proposition: 稳定命题",
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestV20StructuralPrior(unittest.TestCase):
    def test_pass_uncalibrated_prior(self):
        r = v.v20_structural_prior(_payload(
            structural_prior={
                "domain_ids": ["AI"],
                "structural_fit": "mixed",
                "evidence_status": "uncalibrated",
                "qualified_patterns": ["AI-P01"],
                "counter_pattern": "需求真实但资本回报不足",
                "analogue_case": "none_found",
                "failure_case": "none_found",
                "first_questions": ["合同能否转成每股现金流？"],
                "next_step": "proceed_to_verify",
            },
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_capital_language(self):
        r = v.v20_structural_prior(_payload(
            structural_prior={
                "domain_ids": ["AI"],
                "structural_fit": "favorable",
                "evidence_status": "uncalibrated",
                "qualified_patterns": [],
                "counter_pattern": "none",
                "analogue_case": "none_found",
                "failure_case": "none_found",
                "first_questions": [],
                "next_step": "建立验证仓",
            },
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestK5QualifiedPattern(unittest.TestCase):
    def _pattern(self):
        return {
            "pattern_id": "AI-P01",
            "recognition_cues": ["合同与资本开支同时上升"],
            "causal_chain": "需求→合同→收入→利润→现金",
            "payer_and_money_path": "企业客户付费",
            "profit_control": "利用率与融资纪律",
            "favorable_fit": "收入与现金同步改善",
            "counterpattern_and_falsifier": "融资快于现金改善",
            "applicable_asset_types": ["operating_company"],
            "linked_cases": [],
            "first_questions": ["合同转收入速度？"],
            "root_sources": ["oracle-results", "nebius-results"],
            "reused_targets_or_settled_cases": ["ORCL", "NBIS"],
        }

    def test_pass_two_roots_two_reuse(self):
        r = v.k5_qualified_pattern(_payload(
            qualified_patterns=[self._pattern()],
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_single_root(self):
        pattern = self._pattern()
        pattern["root_sources"] = ["oracle-results"]
        r = v.k5_qualified_pattern(_payload(
            qualified_patterns=[pattern],
        ), None)
        self.assertEqual(r["status"], "FAIL")


class TestK2PatternMapCompatibility(unittest.TestCase):
    def test_pass_pattern_map_without_atomic_beliefs(self):
        r = v.k2_belief_contract(_payload(
            content_type="domain_knowledge",
            knowledge_format="pattern_map",
            beliefs=[],
            qualified_patterns=[],
        ), None)
        self.assertEqual(r["status"], "OK")

    def test_fail_pattern_map_with_atomic_belief(self):
        r = v.k2_belief_contract(_payload(
            content_type="domain_knowledge",
            knowledge_format="pattern_map",
            beliefs=[{"claim_id": "SHOULD-NOT-EXIST"}],
            qualified_patterns=[],
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_fail_pattern_map_without_pattern_list(self):
        r = v.k2_belief_contract(_payload(
            content_type="domain_knowledge",
            knowledge_format="pattern_map",
            beliefs=[],
        ), None)
        self.assertEqual(r["status"], "FAIL")

    def test_domain_index_is_registered(self):
        r = v.k1_content_type_path(_payload(
            write_target="05_EVIDENCE_META/KNOWLEDGE/DOMAINS/README.md",
        ), None)
        self.assertEqual(r["status"], "OK")


if __name__ == "__main__":
    unittest.main()
