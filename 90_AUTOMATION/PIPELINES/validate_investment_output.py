#!/usr/bin/env python3
"""
Investment Harness Validator

机械校验 Investment Harness 输出与写入意图。
- 只使用 Python 标准库
- 不联网
- fail-closed
- 不判断投资结论是否正确

校验项 V-1 ~ V-19。每项单独返回 OK/FAIL，整体聚合为 exit code（0/1）。

输入：JSON 文件路径（argv[1]）或 stdin
输出：JSON 校验报告 + 人类可读摘要

输入 schema 见 90_AUTOMATION/PIPELINES/validate_input_schema.json
（或参考 90_AUTOMATION/TESTS/test_investment_output.py 的样例）
"""

import hashlib
import json
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path


REPO_ROOT = Path(
    os.environ.get(
        "INVESTMENT_REPO_ROOT",
        str(Path(__file__).resolve().parents[2]),
    )
).resolve()

GOVERNANCE_CONTRACT_PATH = (
    REPO_ROOT
    / "05_EVIDENCE_META/_SYSTEM/ABSORPTION_RECEIPTS/"
      "260728_memory_palace_governance_contract.json"
)

CANONICAL_SINK_PREFIXES = [
    "05_EVIDENCE_META/SOURCES/",
    "05_EVIDENCE_META/MOMENTS/",
    "05_EVIDENCE_META/KNOWLEDGE/DOMAINS/",
    "05_EVIDENCE_META/KNOWLEDGE/ENTITIES/COMPANIES/",
    "05_EVIDENCE_META/KNOWLEDGE/ENTITIES/ETFS/",
    "05_EVIDENCE_META/_ARCHIVE/MOMENTS/",
    "05_EVIDENCE_META/_SYSTEM/ABSORPTION_RECEIPTS/",
    "05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/",
    "03_STATE/HYPOTHESIS_QUEUE/CURRENT/",
    "03_STATE/EXPECTATIONS/",
    "01_道/PHILOSOPHY_INBOX/",
    "90_AUTOMATION/RUNTIME/STAGING/",
    "90_AUTOMATION/RUN_LOG/",
    # Domain models (D-X series)
    "03_STATE/DOMAIN_MODELS/",                # 顶层 README
    "03_STATE/DOMAIN_MODELS/AI/",             # 领域主页 + INVESTMENT_MAP.md
    "03_STATE/DOMAIN_MODELS/AI/THESES/",      # 主题卡
    # 注：未登记领域（如 DOMAIN_MODELS/CRYPTO/）由 D-2 拒绝
]

CANONICAL_SINK_EXACT = {
    "05_EVIDENCE_META/HOME.md",
    "05_EVIDENCE_META/MOMENTS/README.md",
    "05_EVIDENCE_META/SOURCES/README.md",
    "05_EVIDENCE_META/_SYSTEM/README.md",
    "05_EVIDENCE_META/_SYSTEM/PROVENANCE_SCHEMA.md",
    "05_EVIDENCE_META/_SYSTEM/CLAIM_LEDGER.md",
    "05_EVIDENCE_META/_SYSTEM/CONFLICT_REGISTER.md",
    "05_EVIDENCE_META/_ARCHIVE/README.md",
    "05_EVIDENCE_META/_ARCHIVE/MOMENTS/README.md",
    "03_STATE/EXPECTATIONS/AI/README.md",
    "04_CASE_GYM/ERROR_LIBRARY/DOMAIN_FAILURES/README.md",
}

# 已登记领域 id 列表；本组由 Murphy 于 2026-07-28 明确批准。
REGISTERED_DOMAIN_IDS = {
    "AI",
    "ENERGY_STORAGE_MATERIALS",
    "CHINA_INTERNET",
    "CONSUMER_IP",
    "INNOVATIVE_DRUGS",
    "STABLECOIN_CRYPTO_INFRA",
    "RESOURCES_POWER_GRID",
}

ALLOWED_STRUCTURAL_FITS = {"favorable", "unfavorable", "mixed", "unknown"}
ALLOWED_STRUCTURAL_NEXT_STEPS = {
    "proceed_to_verify",
    "ask_identity",
    "out_of_scope",
}
ALLOWED_KNOWLEDGE_EFFECTS = {
    "strengthen",
    "weaken",
    "revise_chain",
    "add_counterpattern",
    "add_qualified_pattern",
}

# 允许的 thesis_status 枚举
ALLOWED_THESIS_STATUSES = {
    "working",
    "partially_validated",
    "validated",
    "failed",
    "expired",
}

# 资本动作字段禁止出现在领域模型
CAPITAL_ACTION_FIELDS = {
    "target_price",
    "position_size",
    "buy_authorization",
    "weight",
}

# 领域模型判断段落的三个 Murphy/AI 分账档
MURPHY_AI_SPLIT_HEADINGS = (
    "### Murphy confirmed",
    "### Co-created working thesis",
    "### AI extension",
)

# 领域模型判断段落主标题（每段都必须包含三档）
DOMAIN_JUDGMENT_SECTIONS = (
    "## 因果链",
    "## 利润池",
    "## 可投资点",
    "## 绕开路径",
    "## 失败条件",
)

CANONICAL_PROTECTED_PATHS = [
    "01_道/CONSTITUTION.md",
    "01_道/MINDSET.md",
    "02_术/TRADING_SYSTEM/00_DECISION_CONTRACT.md",
    "02_术/TRADING_SYSTEM/01_RESEARCH_FLOW.md",
    "02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION.md",
    "02_术/TRADING_SYSTEM/03_FEEDBACK_LOOP.md",
    "02_术/TRADING_SYSTEM/PARAMETERS.md",
    "03_STATE/PORTFOLIO_LEDGER.md",
]

CANONICAL_PROTECTED_PREFIXES = [
    "01_道/",     # 整个道正文（PHILOSOPHY_INBOX 子目录例外）
    "02_术/",     # 整个术 canonical
]

ALLOWED_ACTIONS = {
    "不投入",
    "继续观察",
    "建立验证仓",
    "升级确认仓",
    "不加仓",
    "降级或退出",
}

AMBIGUOUS_ACTION_PATTERNS = re.compile(
    r"(维持甚至加仓|逢低吸纳|谨慎乐观|适当参与|波段操作|降低权重|长期持有|逢高减仓"
    r"|稳健配置|适度配置|逢反弹|择机|视情况)",
    re.UNICODE,
)

ALLOWED_ABSORPTIONS = {
    "SOURCE_CAPTURE",
    "MOMENT_CAPTURE",
    "KNOWLEDGE_UPDATE",
    "STATE_UPDATE",
    "NEW_FACT",
    "NEW_MECHANISM",
    "NEW_PERSPECTIVE",
    "NEW_COUNTEREVIDENCE",
    "NO_INCREMENT",
}

ALLOWED_BELIEF_STATES = {
    "candidate",
    "working",
    "supported",
    "weakened",
    "rejected",
}

ALLOWED_BELIEF_ORIGINS = {
    "murphy_explicit",
    "co_created",
    "ai_narrative",
    "external_consensus",
}

ALLOWED_UPDATE_DIRECTIONS = {
    "strong_support",
    "support",
    "no_change",
    "weaken",
    "strong_weaken",
}

ALLOWED_INDEPENDENCE = {"independent", "same_root", "unknown"}
ALLOWED_DIAGNOSTICITY = {"high", "medium", "low"}
ALLOWED_UPDATE_CHANNELS = {
    "operating",
    "customer_contract",
    "customer_cash",
    "formal_financing",
    "market_price",
    "market_flow",
    "narrative",
}

ALLOWED_UPDATE_DIMENSIONS = {
    "domain_model",
    "demand",
    "utilization",
    "profit",
    "cash",
    "financing_capacity",
    "capital_cost",
    "market_expectation",
    "H_R",
    "H_L",
}

ALLOWED_CONTENT_TYPES = {
    "domain_knowledge",
    "entity_knowledge",
    "moment",
    "source",
    "active_expectation",
    "automation_staging",
    "automation_run_log",
}

LJG_FORBIDDEN_PATTERN = re.compile(
    r"(建议投资|建议金额|目标价|target_price|position_size|buy_authorization"
    r"|建立验证仓|升级确认仓|加仓|减仓|退出|murphy_confirmed"
    r"|分析报告/archive|AI周期探索/02_公司研究|基础概念/实体商)",
    re.IGNORECASE | re.UNICODE,
)

SUBJECTIVE_PRECISION_PATTERN = re.compile(
    r"(主观胜率|Bull\s*:|Base\s*:|Bear\s*:|posterior_probability"
    r"|weight_delta|score_delta|固定加分|机械加总)",
    re.IGNORECASE | re.UNICODE,
)

_CONTENT_PATH_RULES = {
    "domain_knowledge": re.compile(
        r"^05_EVIDENCE_META/KNOWLEDGE/DOMAINS/[^/]+/README\.md$"
    ),
    "entity_knowledge": re.compile(
        r"^05_EVIDENCE_META/KNOWLEDGE/ENTITIES/(?:COMPANIES|ETFS)/(?:README|[^/]+)\.md$"
    ),
    "moment": re.compile(
        r"^05_EVIDENCE_META/(?:MOMENTS|_ARCHIVE/MOMENTS)/[^/]+\.md$"
    ),
    "source": re.compile(
        r"^05_EVIDENCE_META/SOURCES/\d{4}/[^/]+\.md$"
    ),
    "active_expectation": re.compile(
        r"^03_STATE/EXPECTATIONS/[^/]+/[^/]+\.md$"
    ),
    "automation_staging": re.compile(
        r"^90_AUTOMATION/RUNTIME/STAGING/"
        r"[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?--[0-9a-f]{12}\.json$"
    ),
    "automation_run_log": re.compile(
        r"^90_AUTOMATION/RUN_LOG/"
        r"[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?--[0-9a-f]{12}\.json$"
    ),
}

_NEW_INDEX_PATHS = {
    "05_EVIDENCE_META/HOME.md",
    "05_EVIDENCE_META/KNOWLEDGE/DOMAINS/README.md",
    "05_EVIDENCE_META/MOMENTS/README.md",
    "05_EVIDENCE_META/SOURCES/README.md",
    "05_EVIDENCE_META/_SYSTEM/README.md",
    "05_EVIDENCE_META/_ARCHIVE/README.md",
    "05_EVIDENCE_META/_ARCHIVE/MOMENTS/README.md",
    "03_STATE/EXPECTATIONS/AI/README.md",
}

ALLOWED_STATES = {"current", "expired", "legacy_only", "missing"}

ALLOWED_ODDS_CALIBRATION_STATES = {
    "calibrated",
    "bounded_unknown",
    "uncalibrated",
    "not_applicable",
}

ALLOWED_ASSET_TYPES = {
    "operating_company",
    "resource_cycle_company",
    "utility",
    "capital_structure_vehicle",
    "etf",
}

ASSET_ROUTE_REQUIREMENTS = {
    "operating_company": {
        "industry_change", "profit_capture", "odds", "account_fit",
    },
    "resource_cycle_company": {
        "supply_demand", "normalized_profit", "capex_cashflow", "odds", "account_fit",
    },
    "utility": {
        "demand_policy", "unit_economics", "capex_cashflow", "account_role", "odds",
    },
    "capital_structure_vehicle": {
        "underlying_view", "per_share_exposure", "liability_dilution",
        "claims_seniority", "odds",
    },
    "etf": {
        "industry_policy", "funds_relative_strength",
        "valuation_crowding", "product_fit",
    },
}

INTERNAL_USER_OUTPUT_PATTERN = re.compile(
    r"(H_B|H_R|H_L|H_C|state_status|process_depth|review_required"
    r"|loaded_skills|write_intent|harness_task)",
    re.UNICODE,
)

# repository_publish 允许的发布脚手架路径（只写发布文件，不碰投资内容）
PUBLICATION_ALLOWED_ROOT_FILES = {
    "README.md",
    ".gitignore",
    "LICENSE",
    "LICENSE-CONTENT",
    "NOTICE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "ROADMAP.md",
    "CODEOWNERS",
    "PUBLICATION_MANIFEST.json",
}

PUBLICATION_ALLOWED_PREFIXES = [
    ".github/",
]

PUBLICATION_ALLOWED_EXACT = {
    "90_AUTOMATION/PIPELINES/audit_publication.py",
    "90_AUTOMATION/TESTS/test_audit_publication.py",
}


def _ok(code, message, evidence=None):
    return {"code": code, "status": "OK", "message": message, "evidence": evidence or {}}


def _fail(code, message, evidence=None):
    return {"code": code, "status": "FAIL", "message": message, "evidence": evidence or {}}


def _read_input(argv):
    if len(argv) >= 2 and argv[1] != "-":
        with open(argv[1], "r", encoding="utf-8") as f:
            return json.load(f)
    raw = sys.stdin.read()
    if not raw.strip():
        raise SystemExit("no input provided (file or stdin)")
    return json.loads(raw)


def _today(payload):
    t = payload.get("today")
    if t:
        try:
            return datetime.strptime(t, "%Y-%m-%d").date()
        except ValueError:
            return None
    return date.today()


def _strip_dot_slash(path):
    """只剥 './' 前缀，保留 '.harness_backup' 等点开头的相对路径。"""
    if not path:
        return path
    while path.startswith("./"):
        path = path[2:]
    return path


def _is_canonical_sink(path):
    if not path:
        return False
    norm = _strip_dot_slash(path)
    if norm in CANONICAL_SINK_EXACT:
        return True
    for prefix in CANONICAL_SINK_PREFIXES:
        if norm.startswith(prefix):
            return True
    return False


def _is_publication_path(path):
    """路径是否属于 repository_publish 允许的发布脚手架。"""
    if not path:
        return False
    norm = _strip_dot_slash(path)
    # 拒绝含双斜杠或尾部斜杠的异常路径
    if "//" in norm or norm.endswith("/"):
        return False
    if norm in PUBLICATION_ALLOWED_ROOT_FILES:
        return True
    if norm in PUBLICATION_ALLOWED_EXACT:
        return True
    for prefix in PUBLICATION_ALLOWED_PREFIXES:
        if norm.startswith(prefix):
            return True
    return False


def _is_protected(path):
    if not path:
        return False
    norm = _strip_dot_slash(path)
    if norm in CANONICAL_PROTECTED_PATHS:
        return True
    # 例外：01_道/PHILOSOPHY_INBOX/ 允许写入（候选）
    if norm.startswith("01_道/PHILOSOPHY_INBOX/"):
        return False
    for prefix in CANONICAL_PROTECTED_PREFIXES:
        if norm.startswith(prefix):
            return True
    if norm.startswith("03_STATE/PORTFOLIO_LEDGER"):
        return True
    return False


def _sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _governance_contract():
    if not GOVERNANCE_CONTRACT_PATH.exists():
        return None
    try:
        with open(GOVERNANCE_CONTRACT_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return None


def _governance_entry(payload):
    task = payload.get("harness_task", {})
    if task.get("write_intent") != "governance_migration":
        return None
    contract = _governance_contract()
    if not contract:
        return None
    if payload.get("governance_contract_id") != contract.get("contract_id"):
        return None
    target = _strip_dot_slash(payload.get("write_target") or "")
    for entry in contract.get("control_targets", []):
        if entry.get("write_target") == target:
            return entry
    return None


def v1_write_path(payload, today):
    """V-1 写入路径必须属于 canonical sink。"""
    write_intent = payload.get("harness_task", {}).get("write_intent")
    target = payload.get("write_target")
    if write_intent == "governance_migration":
        if not target or not _governance_entry(payload):
            return _fail("V-1", "governance_migration 未命中冻结 contract 精确目标")
        return _ok(
            "V-1",
            "governance_migration 命中冻结 contract",
            {"write_target": target},
        )
    if write_intent == "repository_publish":
        if not target:
            return _fail("V-1", "repository_publish 缺少 write_target")
        if _is_protected(target):
            return _fail("V-1", f"repository_publish 命中 canonical 保护：{target}")
        if not _is_publication_path(target):
            return _fail("V-1", f"repository_publish 路径不在发布允许列表：{target}")
        return _ok("V-1", "repository_publish 路径合法", {"write_target": target})
    if write_intent not in {"explicit_persist", "automation_stage"}:
        return _ok("V-1", "当前 write_intent 无文件写入；路径校验跳过",
                   {"write_intent": write_intent})
    if not target:
        return _fail("V-1", f"{write_intent} 缺少 write_target")
    if _is_protected(target):
        return _fail("V-1", f"write_target 命中 canonical 保护：{target}")
    if not _is_canonical_sink(target):
        return _fail("V-1", f"write_target 不在 canonical sink：{target}")
    return _ok("V-1", "write_target 属于 canonical sink", {"write_target": target})


def v2_state_time(payload, today):
    """V-2 状态时间自洽。"""
    task = payload.get("harness_task", {})
    state_status = task.get("state_status")
    thesis = payload.get("thesis_state") or {}
    if state_status not in ALLOWED_STATES:
        return _fail("V-2", f"state_status 不合法：{state_status}")

    if state_status == "missing":
        if thesis:
            return _fail("V-2", "state_status=missing 但 thesis_state 非空")
        return _ok("V-2", "missing 与空 thesis_state 一致")

    data_cutoff = thesis.get("data_cutoff")
    expires_at = thesis.get("expires_at")
    review_date = thesis.get("review_date")

    if not data_cutoff or not expires_at:
        return _fail("V-2", "thesis 缺少 data_cutoff 或 expires_at")

    try:
        cutoff_d = datetime.strptime(data_cutoff, "%Y-%m-%d").date()
        expires_d = datetime.strptime(expires_at, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return _fail("V-2", "data_cutoff/expires_at 日期格式不合法")

    if today is None:
        return _fail("V-2", "today 缺失或格式不合法")

    if cutoff_d > expires_d:
        return _fail("V-2", "data_cutoff > expires_at")

    actual_current = cutoff_d <= today <= expires_d
    if state_status == "current" and not actual_current:
        return _fail("V-2",
                     f"state_status=current 但 today={today} 不在 [{cutoff_d}, {expires_d}]")
    if state_status == "expired" and today < expires_d:
        return _fail("V-2",
                     f"state_status=expired 但 today={today} 早于 expires_at={expires_d}")

    if review_date:
        try:
            review_d = datetime.strptime(review_date, "%Y-%m-%d").date()
            if today > review_d and state_status == "current":
                return _fail("V-2",
                             f"today={today} 已过 review_date={review_d}，应进入 expired")
        except ValueError:
            return _fail("V-2", "review_date 格式不合法")

    return _ok("V-2", "状态时间自洽",
               {"state_status": state_status, "today": str(today),
                "data_cutoff": data_cutoff, "expires_at": expires_at})


def v3_reviewer_derived(payload, today):
    """V-3 Reviewer 派生条件：硬触发必须 review_required=true。"""
    task = payload.get("harness_task", {})
    review_required = task.get("review_required")
    target = payload.get("write_target")
    write_intent = task.get("write_intent")
    input_type = task.get("input_type")
    loaded_skills = task.get("loaded_skills", []) or []

    triggers = []
    if write_intent in {"explicit_persist", "governance_migration",
                        "repository_publish"}:
        triggers.append(write_intent)
    if target:
        norm = _strip_dot_slash(target)
        if (norm.startswith("01_道/") or norm.startswith("02_术/")
                or norm.startswith("03_STATE/")):
            triggers.append(f"protected_path:{norm}")
    if input_type == "CAPITAL":
        triggers.append("capital_action")
    if "BEHAVIOR_REVIEW" in loaded_skills:
        triggers.append("behavior_review_loaded")

    if triggers and not review_required:
        return _fail("V-3",
                     f"硬触发存在但 review_required=false：{triggers}")
    if not triggers and review_required:
        # 主 Agent 主动增加 Reviewer 是允许的
        return _ok("V-3", "无硬触发但主 Agent 主动增加 Reviewer（允许）")
    return _ok("V-3", "Reviewer 派生条件一致", {"triggers": triggers})


def v4_action(payload, today):
    """V-4 动作表达属于六档。"""
    action = payload.get("action")
    if action is None:
        # REVIEW lane 不输出 action
        task = payload.get("harness_task", {})
        if task.get("lane") == "REVIEW":
            return _ok("V-4", "REVIEW lane 无 action，跳过")
        return _fail("V-4", "JUDGE lane 缺少 action 字段")
    if action not in ALLOWED_ACTIONS:
        return _fail("V-4", f"action 不在六档内：{action}")
    if AMBIGUOUS_ACTION_PATTERNS.search(action):
        return _fail("V-4", f"action 含模糊表达：{action}")
    return _ok("V-4", f"action 合法：{action}")


def v5_source_fields(payload, today):
    """V-5 reviewed 输出包含来源字段。"""
    task = payload.get("harness_task", {})
    review = payload.get("review_result", {}) or {}
    sources = review.get("source_traceability", {}) or {}
    root_sources = sources.get("root_sources") or []

    if task.get("process_depth") != "reviewed":
        return _ok("V-5", "process_depth != reviewed，跳过")

    if not root_sources:
        return _fail("V-5", "reviewed 输出缺少 root_sources")

    missing = []
    for s in root_sources:
        if not s.get("path_or_url"):
            missing.append("root_source.path_or_url 缺失")
        if not s.get("published_at"):
            missing.append("root_source.published_at 缺失")
        if not s.get("data_caliber"):
            missing.append("root_source.data_caliber 缺失")
    if missing:
        return _fail("V-5", f"root_sources 字段不全：{missing[:3]}")

    return _ok("V-5", f"root_sources 完整（{len(root_sources)} 条）")


def v6_reviewer_completeness(payload, today):
    """V-6 Reviewer 完整；正式写入必须 PASS 且路由精确匹配。"""
    task = payload.get("harness_task", {})
    review = payload.get("review_result", {}) or {}
    verdict = review.get("verdict")
    weakest = (review.get("weakest_link") or "").strip()
    best_bear = (review.get("best_bear_case") or "").strip()

    if task.get("process_depth") != "reviewed":
        return _ok("V-6", "process_depth != reviewed，跳过")

    if verdict not in {"PASS", "BLOCK", "DISAGREE"}:
        return _fail("V-6", f"verdict 不合法：{verdict}")

    if verdict == "PASS":
        if not weakest or weakest.lower() == "none":
            return _fail("V-6", "PASS 缺少 weakest_link")
        if not best_bear or best_bear.lower() == "none":
            return _fail("V-6", "PASS 缺少 best_bear_case")
    if task.get("write_intent") in {"explicit_persist", "governance_migration",
                                     "repository_publish"}:
        if verdict != "PASS":
            return _fail("V-6", f"正式写入必须 Reviewer PASS：{verdict}")
        route = review.get("allowed_write_route")
        target = payload.get("write_target")
        if not isinstance(route, str) or route != target:
            return _fail(
                "V-6",
                f"allowed_write_route 与 write_target 不精确一致：{route!r} != {target!r}",
            )
    return _ok("V-6", "Reviewer 输出完整", {"verdict": verdict})


def v7_canonical_protection(payload, today):
    """V-7 canonical 保护：拒绝直接修改道/术/Portfolio 正文。"""
    target = payload.get("write_target")
    if not target:
        return _ok("V-7", "无 write_target，跳过")
    if payload.get("harness_task", {}).get("write_intent") == "governance_migration":
        if _governance_entry(payload):
            return _ok("V-7", "一次性治理 contract 精确授权 canonical 修改")
        return _fail("V-7", "治理迁移未命中 contract")
    if _is_protected(target):
        return _fail("V-7", f"write_target 命中 canonical 保护：{target}")
    return _ok("V-7", "write_target 不在 canonical 保护范围")


def v8_backup(payload, today):
    """V-8 修改既有文件前必须存在备份。"""
    target = payload.get("write_target")
    backup_path = payload.get("backup_path")
    if not target:
        return _ok("V-8", "无 write_target，跳过")
    target_abs = REPO_ROOT / target
    if not target_abs.exists():
        return _ok("V-8", "write_target 是新文件，无需备份")
    if payload.get("target_preexisted") is False:
        return _ok("V-8", "write_target 本轮新建，写后复核无需历史备份")
    if not backup_path:
        return _fail("V-8", "修改既有文件但未提供 backup_path")
    backup_abs = REPO_ROOT / _strip_dot_slash(backup_path)
    if not backup_abs.exists():
        return _fail("V-8", f"backup_path 不存在：{backup_path}")
    return _ok("V-8", "备份存在", {"backup_path": backup_path})


def v9_state_expiry_scan(payload, today):
    """V-9 State 到期扫描。"""
    scan = payload.get("state_expiry_scan") or {}
    if not scan:
        return _fail("V-9", "缺少 state_expiry_scan 字段")
    required_keys = {"expired", "due_for_review", "missing_time_fields", "inconsistent"}
    missing = required_keys - set(scan.keys())
    if missing:
        return _fail("V-9", f"state_expiry_scan 缺字段：{sorted(missing)}")
    return _ok("V-9", "state_expiry_scan 完整",
               {k: len(v) if isinstance(v, list) else v for k, v in scan.items()})


def v10_disagree(payload, today):
    """V-10 DISAGREE 不被静默升级为 PASS。"""
    review = payload.get("review_result", {}) or {}
    verdict = review.get("verdict")
    open_dis = payload.get("thesis_state", {}).get("open_disagreement")

    if verdict == "DISAGREE":
        if payload.get("write_target"):
            return _fail("V-10", "DISAGREE 时不应触发写入")
        if payload.get("thesis_state") and open_dis is None:
            return _fail("V-10", "DISAGREE 时 current thesis 缺少 open_disagreement 字段")
    return _ok("V-10", "DISAGREE 处理一致", {"verdict": verdict})


def v11_chat_only_route(payload, today):
    """V-11 chat_only 时 allowed_write_route 必须留空。"""
    task = payload.get("harness_task", {})
    review = payload.get("review_result", {}) or {}
    route = review.get("allowed_write_route")
    if task.get("write_intent") == "chat_only":
        if route:
            return _fail("V-11",
                         f"chat_only 下 allowed_write_route 不应非空：{route}")
    return _ok("V-11", "chat_only 与 allowed_write_route 一致",
               {"write_intent": task.get("write_intent"),
                "allowed_write_route": route or ""})


def v12_batch_cap(payload, today):
    """V-12 BATCH 超过 5 个标的时主输出截断。"""
    task = payload.get("harness_task", {})
    if task.get("input_type") != "BATCH":
        return _ok("V-12", "非 BATCH，跳过")
    target_ids = task.get("target_ids") or []
    shown = payload.get("batch_shown_targets") or []
    if len(target_ids) <= 5:
        return _ok("V-12", f"BATCH 标的数 {len(target_ids)} ≤ 5")
    if len(shown) > 5:
        return _fail("V-12",
                     f"BATCH 主输出展示 {len(shown)} 个，超过 5 个上限")
    if len(shown) < 1:
        return _fail("V-12", "BATCH 主输出为空")
    return _ok("V-12", f"BATCH 主输出展示 {len(shown)} 个（总数 {len(target_ids)}）")


def v13_batch_legacy_majority(payload, today):
    """V-13 BATCH 中 legacy_only/missing 占多数时先声明 State 缺失。"""
    task = payload.get("harness_task", {})
    if task.get("input_type") != "BATCH":
        return _ok("V-13", "非 BATCH，跳过")
    target_ids = task.get("target_ids") or []
    state_status = task.get("state_status")
    state_declared = payload.get("batch_state_gap_declared", False)

    # 简化：当 harness_task.state_status 为 legacy_only/missing 时，
    # 视为整体声明（粗粒度聚合）
    if state_status in {"legacy_only", "missing"} and len(target_ids) >= 2:
        if not state_declared:
            return _fail("V-13",
                         "BATCH 多数标的 legacy_only/missing 但未声明 State 缺失")
    return _ok("V-13", "BATCH State 缺失声明一致",
               {"state_status": state_status, "declared": state_declared})


def v14_source_classification(payload, today):
    """V-14 内容来源分类。"""
    task = payload.get("harness_task", {})
    if task.get("input_type") not in {"CONTENT", "FILING"}:
        return _ok("V-14", "非 CONTENT/FILING，跳过")
    sources = (payload.get("review_result", {}) or {}).get("source_traceability", {}) or {}
    classifications = []
    for s in sources.get("root_sources") or []:
        classifications.append(s.get("source_class"))
    if not classifications:
        return _fail("V-14", "CONTENT/FILING 缺少 root_sources 或 source_class")
    allowed = {"external_publish", "internal_legacy", "user_thesis"}
    bad = [c for c in classifications if c not in allowed]
    if bad:
        return _fail("V-14", f"source_class 不合法：{bad}")
    return _ok("V-14", f"source_class 合法：{classifications}")


POSITION_PATTERN = re.compile(
    r"(\d+\.?\d*\s*%|满仓|梭哈|加\s*\d+\s*%|清仓|全仓|半仓)",
    re.UNICODE,
)


def v15_position_trigger(payload, today):
    """V-15 仓位参数识别 + BEHAVIOR_REVIEW 自动触发。"""
    task = payload.get("harness_task", {})
    raw_input = payload.get("user_input_raw") or ""
    if POSITION_PATTERN.search(raw_input):
        loaded = task.get("loaded_skills", []) or []
        if "BEHAVIOR_REVIEW" not in loaded:
            return _fail("V-15",
                         "输入含仓位参数但未加载 BEHAVIOR_REVIEW")
        if not payload.get("risk_freeze_acknowledged", False):
            return _fail("V-15",
                         "输入含仓位参数但未声明 24h 新增风险冻结提示")
    return _ok("V-15", "仓位参数识别一致")


def v16_odds_calibration(payload, today):
    """V-16 JUDGE 输出必须诚实声明赔率校准状态。"""
    task = payload.get("harness_task", {})
    if task.get("lane") != "JUDGE":
        return _ok("V-16", "非 JUDGE，跳过")

    odds = payload.get("odds_calibration") or {}
    status = odds.get("status")
    implied = str(odds.get("market_implied_expectation") or "").strip()
    basis = str(odds.get("basis_or_boundary") or "").strip()
    missing = odds.get("missing_evidence")

    if status not in ALLOWED_ODDS_CALIBRATION_STATES:
        return _fail("V-16", f"赔率校准状态缺失或不合法：{status}")

    if status == "not_applicable":
        if not basis:
            return _fail("V-16", "not_applicable 缺少原因")
    else:
        if not implied:
            return _fail("V-16", f"{status} 缺少 market_implied_expectation")
        if status in {"calibrated", "bounded_unknown"} and not basis:
            return _fail("V-16", f"{status} 缺少 basis_or_boundary")
        if status in {"bounded_unknown", "uncalibrated"} and not missing:
            return _fail("V-16", f"{status} 缺少 missing_evidence")

    h_r = str(payload.get("H_R") or "").strip().lower()
    if status == "uncalibrated" and not (
            h_r.startswith("unknown") or h_r.startswith("uncalibrated")):
        return _fail("V-16",
                     f"uncalibrated 时 H_R 必须保持 unknown/uncalibrated：{h_r or '<空>'}")
    if status == "bounded_unknown" and h_r.startswith("pass"):
        return _fail("V-16", "bounded_unknown 不能把 H_R 标为 pass")

    if task.get("process_depth") == "reviewed":
        review = payload.get("review_result", {}) or {}
        check = review.get("odds_calibration_check") or {}
        if check.get("status") != status:
            return _fail("V-16", "Reviewer 赔率状态与主 Agent 不一致")
        if check.get("internally_consistent") is not True:
            return _fail("V-16", "Reviewer 未确认赔率校准内部一致")
        if not str(check.get("reason") or "").strip():
            return _fail("V-16", "Reviewer 赔率校准检查缺少 reason")

    return _ok("V-16", "赔率校准状态与证据缺口表达一致",
               {"status": status})


def v17_research_trigger_provenance(payload, today):
    """V-17 正式 Current 写入必须恢复触发链并分开 Murphy 与 AI。"""
    task = payload.get("harness_task", {})
    target = _strip_dot_slash(payload.get("write_target") or "")
    if task.get("write_intent") != "explicit_persist" or not target.startswith(
            "03_STATE/HYPOTHESIS_QUEUE/CURRENT/"):
        return _ok("V-17", "非正式 Current 写入，跳过")

    trigger = payload.get("research_trigger") or {}
    required = {
        "asset_type",
        "recovery_status",
        "why_in_target_library",
        "original_materials",
        "murphy_prior",
        "ai_extensions",
        "money_path",
        "current_validation_question",
    }
    missing_keys = required - set(trigger.keys())
    if missing_keys:
        return _fail("V-17", f"research_trigger 缺字段：{sorted(missing_keys)}")

    asset_type = trigger.get("asset_type")
    if asset_type not in ALLOWED_ASSET_TYPES:
        return _fail("V-17", f"asset_type 不合法：{asset_type}")
    if trigger.get("recovery_status") not in {
            "recovered", "needs_murphy_confirmation"}:
        return _fail("V-17", "recovery_status 不合法")
    for key in {"why_in_target_library", "money_path", "current_validation_question"}:
        if not str(trigger.get(key) or "").strip():
            return _fail("V-17", f"research_trigger.{key} 不能为空")

    originals = trigger.get("original_materials") or []
    if not originals:
        return _fail("V-17", "research_trigger.original_materials 不能为空")
    allowed_roles = {"current_user_thesis", "original_material", "ai_exploration"}
    for item in originals:
        if not str(item.get("path") or "").strip():
            return _fail("V-17", "original_material 缺 path")
        if item.get("source_role") not in allowed_roles:
            return _fail("V-17", "original_material.source_role 不合法")

    priors = trigger.get("murphy_prior") or []
    if not priors:
        return _fail("V-17", "murphy_prior 不能为空；未知也要显式记录")
    for item in priors:
        if not str(item.get("claim") or "").strip():
            return _fail("V-17", "murphy_prior.claim 不能为空")
        if item.get("basis") not in {"user_explicit", "user_confirmed", "unknown"}:
            return _fail("V-17", "murphy_prior.basis 不合法")
        if not str(item.get("source_path") or "").strip():
            return _fail("V-17", "murphy_prior.source_path 不能为空")

    if trigger.get("recovery_status") == "needs_murphy_confirmation":
        if payload.get("action") in {"建立验证仓", "升级确认仓"}:
            return _fail("V-17", "触发原因待 Murphy 确认时不得增加风险")

    review = payload.get("review_result", {}) or {}
    check = review.get("murphy_ai_boundary_check") or {}
    if check.get("status") != "pass" or not str(check.get("reason") or "").strip():
        return _fail("V-17", "Reviewer 未确认 Murphy / AI 边界")
    return _ok("V-17", "研究触发链与 Murphy / AI 分账完整")


def v18_asset_route(payload, today):
    """V-18 正式 Current 写入必须匹配资产类型验证路径。"""
    task = payload.get("harness_task", {})
    target = _strip_dot_slash(payload.get("write_target") or "")
    if task.get("write_intent") != "explicit_persist" or not target.startswith(
            "03_STATE/HYPOTHESIS_QUEUE/CURRENT/"):
        return _ok("V-18", "非正式 Current 写入，跳过")

    trigger = payload.get("research_trigger") or {}
    asset_type = trigger.get("asset_type")
    route = payload.get("asset_validation") or {}
    if route.get("route") != asset_type:
        return _fail("V-18", "asset_validation.route 与 asset_type 不一致")
    required = ASSET_ROUTE_REQUIREMENTS.get(asset_type)
    if not required:
        return _fail("V-18", f"缺少 asset_type 路由定义：{asset_type}")
    missing = [
        key for key in sorted(required)
        if not str(route.get(key) or "").strip()
    ]
    if missing:
        return _fail("V-18", f"{asset_type} 验证路径缺字段：{missing}")

    review = payload.get("review_result", {}) or {}
    check = review.get("asset_route_check") or {}
    if check.get("status") != "pass":
        return _fail("V-18", "Reviewer 未确认资产路由")
    if check.get("asset_type") != asset_type:
        return _fail("V-18", "Reviewer asset_type 与主 Agent 不一致")
    if not str(check.get("reason") or "").strip():
        return _fail("V-18", "Reviewer 资产路由检查缺 reason")
    return _ok("V-18", f"资产类型与验证路径一致：{asset_type}")


def v19_user_output_and_unknowns(payload, today):
    """V-19 用户正文不泄露内部代码；unknown 必须可验证。"""
    task = payload.get("harness_task", {})
    target = _strip_dot_slash(payload.get("write_target") or "")
    if task.get("write_intent") != "explicit_persist" or not target.startswith(
            "03_STATE/HYPOTHESIS_QUEUE/CURRENT/"):
        return _ok("V-19", "非正式 Current 写入，跳过")

    summary = str(payload.get("user_facing_summary") or "").strip()
    if not summary:
        return _fail("V-19", "缺少 user_facing_summary")
    hit = INTERNAL_USER_OUTPUT_PATTERN.search(summary)
    if hit:
        return _fail("V-19", f"用户正文泄露内部代码：{hit.group(0)}")

    internal_states = [
        str(payload.get(k) or "").lower()
        for k in ("H_B", "H_R", "H_L", "H_C")
    ]
    has_unknown = any(
        "unknown" in value or "uncalibrated" in value
        for value in internal_states
    )
    resolutions = payload.get("unknown_resolution") or []
    if has_unknown and not resolutions:
        return _fail("V-19", "存在 unknown 但缺少 unknown_resolution")
    required = {
        "missing", "why_it_matters", "how_to_verify",
        "pass_condition", "fail_condition",
    }
    for item in resolutions:
        empty = [
            key for key in sorted(required)
            if not str(item.get(key) or "").strip()
        ]
        if empty:
            return _fail("V-19", f"unknown_resolution 缺字段：{empty}")
    return _ok("V-19", "用户输出与 unknown 表达完整")


# ---------------------------------------------------------------------------
# Domain Model 校验（D-1 ~ D-8）
# 与 V-X 平行独立编号，仅在写入 03_STATE/DOMAIN_MODELS/ 时激活。
# ---------------------------------------------------------------------------

_DOMAIN_PATH_RE = re.compile(
    r"^03_STATE/DOMAIN_MODELS/(?P<domain>[^/]+)/(?:README\.md|THESES/(?P<thesis>[^/]+)\.md|INVESTMENT_MAP\.md)$"
)


def _is_domain_models_write(target, write_intent):
    if write_intent != "explicit_persist":
        return False
    norm = _strip_dot_slash(target or "")
    return norm.startswith("03_STATE/DOMAIN_MODELS/")


def d1_domain_path(payload, today):
    """D-1 写入路径属于合法 DOMAIN_MODELS 形态。"""
    task = payload.get("harness_task", {})
    target = _strip_dot_slash(payload.get("write_target") or "")
    if not _is_domain_models_write(target, task.get("write_intent")):
        return _ok("D-1", "非 DOMAIN_MODELS 写入，跳过", {"write_target": target})
    m = _DOMAIN_PATH_RE.match(target)
    if not m:
        return _fail("D-1", f"DOMAIN_MODELS 路径形态不合法：{target}")
    return _ok("D-1", "DOMAIN_MODELS 路径形态合法",
               {"domain": m.group("domain"),
                "thesis": m.group("thesis") or "—"})


def d2_domain_registered(payload, today):
    """D-2 domain_id 必须在已登记列表内。"""
    task = payload.get("harness_task", {})
    target = _strip_dot_slash(payload.get("write_target") or "")
    if not _is_domain_models_write(target, task.get("write_intent")):
        return _ok("D-2", "非 DOMAIN_MODELS 写入，跳过")
    m = _DOMAIN_PATH_RE.match(target)
    if not m:
        return _fail("D-2", f"路径形态非法，无法解析 domain：{target}")
    domain = m.group("domain")
    if domain not in REGISTERED_DOMAIN_IDS:
        return _fail("D-2", f"未登记领域：{domain}（已登记：{sorted(REGISTERED_DOMAIN_IDS)}）")
    return _ok("D-2", f"领域已登记：{domain}")


def d3_thesis_status_enum(payload, today):
    """D-3 thesis_status 枚举。"""
    target = _strip_dot_slash(payload.get("write_target") or "")
    if "/THESES/" not in target:
        return _ok("D-3", "非主题卡，跳过")
    if payload.get("primary_role") == "domain_outlook" or payload.get("domain_outlook"):
        status = (payload.get("domain_outlook") or {}).get("outlook_status")
        if status not in {"active", "weakened", "failed", "expired"}:
            return _fail("D-3", f"domain_outlook.outlook_status 不合法：{status}")
        return _ok("D-3", f"domain_outlook 状态合法：{status}")
    thesis_state = payload.get("thesis_state") or {}
    status = thesis_state.get("thesis_status")
    if not status:
        return _fail("D-3", "主题卡 thesis_state 缺 thesis_status")
    if status not in ALLOWED_THESIS_STATUSES:
        return _fail("D-3", f"thesis_status 枚举外取值：{status}")
    return _ok("D-3", f"thesis_status 合法：{status}")


def _parse_date_strict(value):
    if not value or not isinstance(value, str):
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def d4_time_triple(payload, today):
    """D-4 时间三件套完整 + 主题≤180d / 映射≤90d / 复查≤30d。"""
    target = _strip_dot_slash(payload.get("write_target") or "")
    is_thesis = "/THESES/" in target
    is_map = target.endswith("/INVESTMENT_MAP.md")
    is_domain_home = target.endswith("/README.md") and "/DOMAIN_MODELS/" in target
    if not (is_thesis or is_map or is_domain_home):
        return _ok("D-4", "非时间约束文件，跳过")

    state_block = (payload.get("thesis_state") or payload.get("domain_outlook")
                   or payload.get("domain_model_state")
                   or payload.get("investment_map_state") or {})
    data_cutoff = state_block.get("data_cutoff")
    expires_at = state_block.get("expires_at")
    review_date = state_block.get("review_date")
    if not data_cutoff or not expires_at or not review_date:
        return _fail("D-4", f"时间三件套缺失：data_cutoff/expires_at/review_date 必填")
    cutoff_d = _parse_date_strict(data_cutoff)
    expires_d = _parse_date_strict(expires_at)
    review_d = _parse_date_strict(review_date)
    if not cutoff_d or not expires_d or not review_d:
        return _fail("D-4", "时间三件套日期格式不合法")
    if cutoff_d > expires_d:
        return _fail("D-4", f"data_cutoff > expires_at：{cutoff_d} > {expires_d}")
    delta_expiry = (expires_d - cutoff_d).days
    delta_review = (review_d - cutoff_d).days
    if delta_review < 0:
        return _fail("D-4", f"review_date 早于 data_cutoff：{review_d} < {cutoff_d}")
    if delta_review > 31:  # 容许 +0/-1 的工程抖动
        return _fail("D-4", f"review_date 超出 +30d 限制：{delta_review}d")
    if is_thesis or is_domain_home:
        if delta_expiry > 181:
            return _fail("D-4", f"主题/领域 expires_at 超出 +180d 限制：{delta_expiry}d")
    if is_map:
        if delta_expiry > 91:
            return _fail("D-4", f"映射表 expires_at 超出 +90d 限制：{delta_expiry}d")
    return _ok("D-4", "时间三件套完整且不超期",
               {"data_cutoff": data_cutoff,
                "expires_at": expires_at,
                "review_date": review_date,
                "expiry_delta_days": delta_expiry,
                "review_delta_days": delta_review})


def d5_no_capital_action(payload, today):
    """D-5 文件不得出现资本字段。"""
    target = _strip_dot_slash(payload.get("write_target") or "")
    if not _is_domain_models_write(target, payload.get("harness_task", {}).get("write_intent")):
        return _ok("D-5", "非 DOMAIN_MODELS 写入，跳过")
    body = payload.get("proposed_body") or ""
    # 1. frontmatter 检查：state 块里不得有资本字段
    state_block = (payload.get("thesis_state") or payload.get("domain_outlook")
                   or payload.get("domain_model_state")
                   or payload.get("investment_map_state") or {})
    leaked = [k for k in state_block if k in CAPITAL_ACTION_FIELDS]
    if leaked:
        return _fail("D-5", f"frontmatter 含资本字段：{leaked}")
    # 2. body 粗扫：`字段:` 形式出现资本字段
    if body:
        for field in CAPITAL_ACTION_FIELDS:
            pat = re.compile(rf"(?<![\w_]){re.escape(field)}\s*:", re.UNICODE)
            if pat.search(body):
                return _fail("D-5", f"正文含资本字段：{field}")
    return _ok("D-5", "未发现资本字段")


def d6_murphy_ai_split(payload, today):
    """D-6 旧主题卡检查三档；新 Outlook 拒绝重复稳定 belief。"""
    target = _strip_dot_slash(payload.get("write_target") or "")
    if "/THESES/" not in target:
        return _ok("D-6", "非主题卡，跳过")
    body = payload.get("proposed_body") or ""
    if payload.get("primary_role") == "domain_outlook" or payload.get("domain_outlook"):
        duplicate = re.search(
            r"(^|\n)\s*(proposition|mechanism)\s*:|###\s+Murphy confirmed",
            body,
            re.IGNORECASE | re.UNICODE,
        )
        if duplicate:
            return _fail("D-6", "domain_outlook 含重复稳定 belief 正文")
        return _ok("D-6", "domain_outlook 仅保留验证窗口与反链")
    if not body:
        return _fail("D-6", "主题卡缺 proposed_body，无法检查分账")
    missing = []
    for section in DOMAIN_JUDGMENT_SECTIONS:
        # 取每个判断段落之后的窗口（到下一个 ## 标题为止）
        idx = body.find(section)
        if idx == -1:
            # 段落缺失也视为分账缺失
            missing.append(f"{section}（段落缺失）")
            continue
        window = body[idx + len(section):]
        # 截到下一个 ## 标题
        nxt = window.find("\n## ")
        if nxt != -1:
            window = window[:nxt]
        for heading in MURPHY_AI_SPLIT_HEADINGS:
            if heading not in window:
                missing.append(f"{section} 缺 {heading}")
    if missing:
        return _fail("D-6", f"Murphy/AI 三档分账缺失：{missing}")
    return _ok("D-6", "所有判断段落三档分账标题齐全")


def d7_canonical_sink_match(payload, today):
    """D-7 写入路径必须命中已登记 canonical sink。"""
    target = _strip_dot_slash(payload.get("write_target") or "")
    if not _is_domain_models_write(target, payload.get("harness_task", {}).get("write_intent")):
        return _ok("D-7", "非 DOMAIN_MODELS 写入，跳过")
    # 复用 V-1 的 sink 列表
    for prefix in CANONICAL_SINK_PREFIXES:
        if target.startswith(prefix):
            # 还需检查是否登记到合法文件形态（已由 D-1 覆盖）
            return _ok("D-7", f"命中已登记 sink：{prefix}")
    return _fail("D-7", f"DOMAIN_MODELS 写入路径未登记：{target}")


def d8_reviewer_pass(payload, today):
    """D-8 last_reviewer 必须含 PASS + 时间戳；DISAGREE 不得静默升 PASS。"""
    target = _strip_dot_slash(payload.get("write_target") or "")
    if not _is_domain_models_write(target, payload.get("harness_task", {}).get("write_intent")):
        return _ok("D-8", "非 DOMAIN_MODELS 写入，跳过")
    # 1. 从 state block 抓 last_reviewer
    state_block = (payload.get("thesis_state") or payload.get("domain_outlook")
                   or payload.get("domain_model_state")
                   or payload.get("investment_map_state") or {})
    last_reviewer = (state_block.get("last_reviewer") or payload.get("last_reviewer") or "").strip()
    if not last_reviewer:
        return _fail("D-8", "缺 last_reviewer 字段")
    if last_reviewer.lower() == "pending":
        return _fail("D-8", "last_reviewer 为 pending，Reviewer 未通过")
    if "PASS" not in last_reviewer:
        return _fail("D-8", f"last_reviewer 不含 PASS：{last_reviewer}")
    # 检查含时间戳（YYYY-MM-DD 形式）
    if not re.search(r"\d{4}-\d{2}-\d{2}", last_reviewer):
        return _fail("D-8", f"last_reviewer 缺时间戳：{last_reviewer}")
    # DISAGREE 不得静默升 PASS
    if "DISAGREE" in last_reviewer and "PASS" in last_reviewer:
        # 同时出现视为静默升 PASS
        return _fail("D-8", f"last_reviewer 同时含 DISAGREE 与 PASS（静默升级）：{last_reviewer}")
    # 同时校验 Reviewer verdict（如果存在 review_result）
    review = payload.get("review_result") or {}
    if review:
        verdict = review.get("verdict")
        if verdict == "DISAGREE":
            return _fail("D-8", "review_result.verdict=DISAGREE 但 last_reviewer 标 PASS")
    return _ok("D-8", f"last_reviewer 通过：{last_reviewer}")


# ---------------------------------------------------------------------------
# Research Knowledge / Belief / Expectation / Automation（K/U/E/A）
# ---------------------------------------------------------------------------

def k1_content_type_path(payload, today):
    """K-1 新内容类型与 canonical 路径必须精确匹配。"""
    target = _strip_dot_slash(payload.get("write_target") or "")
    content_type = payload.get("content_type")
    if target in _NEW_INDEX_PATHS:
        return _ok("K-1", "研究知识索引路径合法")
    touches_new = (
        target.startswith("05_EVIDENCE_META/KNOWLEDGE/")
        or target.startswith("05_EVIDENCE_META/MOMENTS/")
        or target.startswith("05_EVIDENCE_META/_ARCHIVE/MOMENTS/")
        or target.startswith("05_EVIDENCE_META/SOURCES/")
        or target.startswith("03_STATE/EXPECTATIONS/")
    )
    if not touches_new and not content_type:
        return _ok("K-1", "非新研究知识类型，跳过")
    if content_type not in ALLOWED_CONTENT_TYPES:
        return _fail("K-1", f"content_type 缺失或不合法：{content_type}")
    rule = _CONTENT_PATH_RULES[content_type]
    if not rule.match(target):
        return _fail("K-1", f"{content_type} 与路径不匹配：{target}")
    return _ok("K-1", f"{content_type} 路径合法")


def k2_belief_contract(payload, today):
    """K-2 domain/entity knowledge 的 belief 必须原子化且可证伪。"""
    content_type = payload.get("content_type")
    if content_type not in {"domain_knowledge", "entity_knowledge"}:
        return _ok("K-2", "非 Knowledge belief 写入，跳过")
    if content_type == "domain_knowledge" and payload.get(
        "knowledge_format"
    ) == "pattern_map":
        if "qualified_patterns" not in payload or not isinstance(
            payload.get("qualified_patterns"), list
        ):
            return _fail("K-2", "pattern_map 必须显式提供 qualified_patterns 列表")
        if payload.get("beliefs"):
            return _fail("K-2", "pattern_map 不应同时制造原子 beliefs")
        return _ok("K-2", "pattern_map 交由 K-5 模式准入校验")
    beliefs = payload.get("beliefs") or []
    if not beliefs:
        return _fail("K-2", "Knowledge 写入缺 beliefs")
    required = {
        "claim_id", "proposition", "origin", "origin_ref", "state",
        "mechanism", "supports_if", "weakens_if", "cannot_prove",
        "alternative_model", "source_refs", "latest_moment",
    }
    seen = set()
    for belief in beliefs:
        missing = [
            k for k in sorted(required)
            if not belief.get(k)
        ]
        if missing:
            return _fail("K-2", f"belief 缺字段：{missing}")
        claim_id = belief["claim_id"]
        if claim_id in seen:
            return _fail("K-2", f"重复 claim_id：{claim_id}")
        seen.add(claim_id)
        if belief["origin"] not in ALLOWED_BELIEF_ORIGINS:
            return _fail("K-2", f"belief origin 不合法：{belief['origin']}")
        if belief["state"] not in ALLOWED_BELIEF_STATES:
            return _fail("K-2", f"belief state 不合法：{belief['state']}")
        if belief["origin"] == "murphy_explicit":
            refs = [str(x) for x in belief.get("source_refs") or []]
            origin_ref = str(belief.get("origin_ref") or "")
            if "#EX-" not in origin_ref or not any("#EX-" in x for x in refs):
                return _fail(
                    "K-2",
                    f"{claim_id} 为 murphy_explicit 但缺逐字 excerpt 反链",
                )
    body = str(payload.get("proposed_body") or "")
    if SUBJECTIVE_PRECISION_PATTERN.search(body):
        return _fail("K-2", "Knowledge 含未校准主观精度或机械权重")
    return _ok("K-2", f"belief contract 完整（{len(beliefs)} 条）")


def k3_ljg_projection_boundary(payload, today):
    """K-3 ljg-invest 只读投影不得越过资本与来源边界。"""
    lens = payload.get("lens_output")
    if lens is None:
        return _ok("K-3", "无 ljg-invest 投影，跳过")
    if isinstance(lens, str):
        text = lens
    else:
        text = json.dumps(lens, ensure_ascii=False, sort_keys=True)
    hit = LJG_FORBIDDEN_PATTERN.search(text)
    if hit:
        return _fail("K-3", f"ljg-invest 投影含禁止内容：{hit.group(0)}")
    return _ok("K-3", "ljg-invest 投影保持只读")


def k4_single_active_canonical(payload, today):
    """K-4 同一治理角色只能有一个 active canonical 文件。"""
    registry = payload.get("canonical_registry")
    if registry is None:
        return _ok("K-4", "无 canonical registry，跳过")
    grouped = {}
    for item in registry:
        if item.get("status") != "active":
            continue
        role = item.get("role")
        path = item.get("path")
        if not role or not path:
            return _fail("K-4", "canonical registry 缺 role/path")
        grouped.setdefault(role, set()).add(path)
    duplicates = {k: sorted(v) for k, v in grouped.items() if len(v) > 1}
    if duplicates:
        return _fail("K-4", f"存在双 active canonical：{duplicates}")
    return _ok("K-4", "每个治理角色只有一个 active canonical")


def u1_belief_update_contract(payload, today):
    """U-1 belief_update 必须完整，且只能给建议。"""
    updates = payload.get("belief_updates")
    if updates is None:
        one = payload.get("belief_update")
        if one is None:
            return _ok("U-1", "无 belief_update，跳过")
        updates = [one]
    required = {
        "claim_id", "root_source_id", "direction", "independence",
        "diagnosticity", "evidence_channel", "updates_dimension",
        "update_reason", "counter_explanation", "old_state",
        "proposed_state", "authority",
    }
    for update in updates:
        missing = [k for k in sorted(required) if not update.get(k)]
        if missing:
            return _fail("U-1", f"belief_update 缺字段：{missing}")
        if update["direction"] not in ALLOWED_UPDATE_DIRECTIONS:
            return _fail("U-1", f"direction 不合法：{update['direction']}")
        if update["independence"] not in ALLOWED_INDEPENDENCE:
            return _fail("U-1", f"independence 不合法：{update['independence']}")
        if update["diagnosticity"] not in ALLOWED_DIAGNOSTICITY:
            return _fail("U-1", f"diagnosticity 不合法：{update['diagnosticity']}")
        if update["evidence_channel"] not in ALLOWED_UPDATE_CHANNELS:
            return _fail("U-1", f"evidence_channel 不合法：{update['evidence_channel']}")
        if update["updates_dimension"] not in ALLOWED_UPDATE_DIMENSIONS:
            return _fail("U-1", f"updates_dimension 不合法：{update['updates_dimension']}")
        if update["old_state"] not in ALLOWED_BELIEF_STATES:
            return _fail("U-1", f"old_state 不合法：{update['old_state']}")
        if update["proposed_state"] not in ALLOWED_BELIEF_STATES:
            return _fail("U-1", f"proposed_state 不合法：{update['proposed_state']}")
        if update["authority"] != "suggestion_only":
            return _fail("U-1", "belief_update.authority 必须为 suggestion_only")
        forbidden = {
            "posterior_probability", "weight_delta", "score_delta",
            "applied", "murphy_confirmed",
        } & set(update)
        if forbidden:
            return _fail("U-1", f"belief_update 含禁止字段：{sorted(forbidden)}")
    return _ok("U-1", f"belief_update contract 完整（{len(updates)} 条）")


def u2_root_source_dedupe(payload, today):
    """U-2 同一 claim + root source 只更新一次；same_root 不改状态。"""
    updates = payload.get("belief_updates")
    if updates is None:
        one = payload.get("belief_update")
        if one is None:
            return _ok("U-2", "无 belief_update，跳过")
        updates = [one]
    seen = set()
    for update in updates:
        key = (update.get("claim_id"), update.get("root_source_id"))
        if key in seen:
            return _fail("U-2", f"同根重复更新：{key}")
        seen.add(key)
        if (update.get("independence") == "same_root"
                and update.get("proposed_state") != update.get("old_state")):
            return _fail("U-2", f"same_root 不得改变状态：{key}")
    return _ok("U-2", "root source 去重一致")


def u3_evidence_channel_boundary(payload, today):
    """U-3 价格、资金与融资不能越权更新经营 belief。"""
    updates = payload.get("belief_updates")
    if updates is None:
        one = payload.get("belief_update")
        if one is None:
            return _ok("U-3", "无 belief_update，跳过")
        updates = [one]
    for update in updates:
        channel = update.get("evidence_channel")
        dimension = update.get("updates_dimension")
        if channel in {"market_price", "market_flow"} and dimension not in {
                "market_expectation", "H_R", "H_L"}:
            return _fail("U-3", f"{channel} 不得更新 {dimension}")
        if channel == "formal_financing" and dimension not in {
                "financing_capacity", "capital_cost"}:
            return _fail("U-3", f"formal_financing 不得更新 {dimension}")
    return _ok("U-3", "evidence channel 权限一致")


def e1_expectation_contract(payload, today):
    """E-1 Active Expectation 必须冻结、版本化且可结算。"""
    exp = payload.get("active_expectation")
    if exp is None:
        return _ok("E-1", "无 active_expectation，跳过")
    required = {
        "forecast_id", "forecast_version", "claim_ids", "scope", "as_of",
        "frozen_as_of", "state", "settlement_date",
        "settlement_date_status", "settlement_event", "review_by",
        "own_range",
    }
    missing = [k for k in sorted(required) if not exp.get(k)]
    if missing:
        return _fail("E-1", f"active_expectation 缺字段：{missing}")
    if exp["state"] not in {"frozen", "resolved"}:
        return _fail("E-1", f"expectation state 不合法：{exp['state']}")
    if not isinstance(exp.get("claim_ids"), list) or not exp["claim_ids"]:
        return _fail("E-1", "claim_ids 必须为非空列表")
    if exp["settlement_date"] == "unknown":
        if exp.get("settlement_date_status") != "not_announced":
            return _fail("E-1", "unknown date 必须声明 not_announced")
        window = exp.get("expected_window") or {}
        if not window.get("start") or not window.get("end"):
            return _fail("E-1", "unknown date 缺 expected_window.start/end")
    if exp["state"] == "resolved":
        if not exp.get("actual") or not exp.get("resolution_source"):
            return _fail("E-1", "resolved expectation 缺 actual/resolution_source")
    return _ok("E-1", "Active Expectation contract 完整")


def e2_funding_ledger(payload, today):
    """E-2 资金来源分账；RPO/ARR 不得冒充客户现金。"""
    ledger = payload.get("funding_ledger")
    if ledger is None:
        return _ok("E-2", "无 funding_ledger，跳过")
    seen = {}
    for item in ledger:
        metric = str(item.get("metric") or "").strip()
        bucket = str(item.get("bucket") or "").strip()
        if not metric or not bucket:
            return _fail("E-2", "funding_ledger 缺 metric/bucket")
        key = metric.casefold()
        if key in seen and seen[key] != bucket:
            return _fail("E-2", f"{metric} 被重复计入：{seen[key]} / {bucket}")
        seen[key] = bucket
        if key in {"rpo", "arr"} and bucket == "customer_cash":
            return _fail("E-2", f"{metric} 不得计入 customer_cash")
    return _ok("E-2", "资金来源分账无重复")


def e3_frozen_version(payload, today):
    """E-3 frozen expectation 不得原地覆盖。"""
    exp = payload.get("active_expectation")
    if exp is None:
        return _ok("E-3", "无 active_expectation，跳过")
    if exp.get("state") == "frozen" and payload.get("overwrite_previous") is True:
        return _fail("E-3", "frozen expectation 不得覆盖旧版本")
    if (payload.get("is_update") is True
            and payload.get("previous_forecast_version") == exp.get("forecast_version")):
        return _fail("E-3", "更新 frozen expectation 必须提升 forecast_version")
    return _ok("E-3", "expectation 版本冻结一致")


def a1_automation_authority(payload, today):
    """A-1 自动化只能 exclusive-create Staging 与脱敏 Run Log。"""
    if payload.get("actor") != "automation":
        return _ok("A-1", "非自动化 actor，跳过")
    target = _strip_dot_slash(payload.get("write_target") or "")
    allowed = (
        target.startswith("90_AUTOMATION/RUNTIME/STAGING/")
        or target.startswith("90_AUTOMATION/RUN_LOG/")
    )
    if not allowed:
        return _fail("A-1", f"自动化越权写入：{target}")
    updates = payload.get("belief_updates") or []
    if payload.get("belief_update"):
        updates = updates + [payload["belief_update"]]
    if any(u.get("authority") != "suggestion_only" for u in updates):
        return _fail("A-1", "自动化 belief_update 必须 suggestion_only")
    return _ok("A-1", "自动化写入范围合法")


def a2_automation_staging_contract(payload, today):
    """A-2 Staging/Run Log 必须使用精确类型、文件名和降权身份。"""
    if payload.get("actor") != "automation":
        return _ok("A-2", "非自动化 actor，跳过")
    target = _strip_dot_slash(payload.get("write_target") or "")
    content_type = payload.get("content_type")
    if content_type == "automation_staging":
        if not _CONTENT_PATH_RULES["automation_staging"].match(target):
            return _fail("A-2", f"automation_staging 路径不合法：{target}")
        record = payload.get("staging_record")
        if not isinstance(record, dict):
            return _fail("A-2", "automation_staging 缺 staging_record")
        required = {
            "schema_version", "runner_version", "created_at", "input_sha256",
            "verification_status", "promotion_authority", "root_source_id",
            "target_claim_ids", "belief_updates",
        }
        missing = [k for k in sorted(required) if not record.get(k)]
        if missing:
            return _fail("A-2", f"staging_record 缺字段：{missing}")
        if record["verification_status"] != "unverified_by_runner":
            return _fail("A-2", "Staging 必须标记 unverified_by_runner")
        if record["promotion_authority"] != "none":
            return _fail("A-2", "Staging promotion_authority 必须为 none")
        root_source_id = str(record.get("root_source_id") or "")
        if not re.fullmatch(
            r"(?=.{1,80}$)[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?",
            root_source_id,
        ):
            return _fail("A-2", "Staging root_source_id 不合法")
        updates = record.get("belief_updates")
        if not isinstance(updates, list) or not updates:
            return _fail("A-2", "Staging belief_updates 必须为非空列表")
        for update in updates:
            if update.get("authority") != "suggestion_only":
                return _fail("A-2", "Staging update 必须 suggestion_only")
            if update.get("independence") not in {"unknown", "same_root"}:
                return _fail("A-2", "Staging 不得声明 independent")
        digest = str(record.get("input_sha256") or "")
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            return _fail("A-2", "Staging input_sha256 不合法")
        expected = (
            "90_AUTOMATION/RUNTIME/STAGING/"
            f"{root_source_id}--{digest[:12]}.json"
        )
        if target != expected:
            return _fail("A-2", f"Staging 文件名与 root/hash 不一致：{target}")
        return _ok("A-2", "Staging 降权身份与精确路径合法")
    if content_type == "automation_run_log":
        if not _CONTENT_PATH_RULES["automation_run_log"].match(target):
            return _fail("A-2", f"automation_run_log 路径不合法：{target}")
        record = payload.get("run_log_record")
        if not isinstance(record, dict):
            return _fail("A-2", "automation_run_log 缺 run_log_record")
        digest = str(record.get("input_sha256") or "")
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            return _fail("A-2", "Run Log input_sha256 不合法")
        filename = target.rsplit("/", 1)[-1]
        root_part = filename.rsplit("--", 1)[0]
        if not re.fullmatch(
            r"(?=.{1,80}$)[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?",
            root_part,
        ):
            return _fail("A-2", "Run Log root_source_id 不合法")
        if not filename.endswith(f"--{digest[:12]}.json"):
            return _fail("A-2", "Run Log 文件名与 input hash 不一致")
        return _ok("A-2", "Run Log 精确路径合法")
    return _fail("A-2", f"自动化 content_type 不合法：{content_type}")


def a3_run_log_sanitization(payload, today):
    """A-3 Run Log 只允许最小脱敏字段。"""
    if payload.get("actor") != "automation":
        return _ok("A-3", "非自动化 actor，跳过")
    if payload.get("content_type") != "automation_run_log":
        return _ok("A-3", "非 Run Log，跳过")
    record = payload.get("run_log_record")
    if not isinstance(record, dict):
        return _fail("A-3", "Run Log 缺 record")
    allowed = {
        "schema_version", "runner_version", "created_at", "input_sha256",
        "mode", "result", "created_paths", "error_code",
    }
    extra = set(record) - allowed
    missing = allowed - set(record)
    if extra or missing:
        return _fail(
            "A-3",
            f"Run Log 字段不精确：extra={sorted(extra)}, missing={sorted(missing)}",
        )
    paths = record.get("created_paths")
    if not isinstance(paths, list) or any(not isinstance(x, str) for x in paths):
        return _fail("A-3", "created_paths 必须为字符串列表")
    serialized = json.dumps(record, ensure_ascii=False, sort_keys=True)
    forbidden = re.search(
        r"(excerpt|原文|api[_-]?key|authorization|credential|environment|"
        r"source_locator|moment_candidate|update_reason|counter_explanation)",
        serialized,
        re.IGNORECASE,
    )
    if forbidden:
        return _fail("A-3", f"Run Log 含禁止内容：{forbidden.group(0)}")
    return _ok("A-3", "Run Log 最小字段且已脱敏")


def g1_governance_migration_contract(payload, today):
    """G-1 一次性治理迁移必须逐文件命中冻结 contract 与哈希。"""
    task = payload.get("harness_task", {})
    if task.get("write_intent") != "governance_migration":
        return _ok("G-1", "非 governance_migration，跳过")
    contract = _governance_contract()
    entry = _governance_entry(payload)
    if not contract or not entry:
        return _fail("G-1", "缺治理 contract 或目标未登记")
    if contract.get("authorization") != "PLEASE IMPLEMENT THIS PLAN":
        return _fail("G-1", "用户授权语句不匹配")
    if contract.get("approved_plan_sha256") != (
        "cfb97d9e19bdcf930369ad7900fe7dc25e7bddfd47dbe3cc9409af97dbc9699d"
    ):
        return _fail("G-1", "完整计划 SHA256 不匹配")
    target = _strip_dot_slash(payload.get("write_target") or "")
    if payload.get("before_sha256") != entry.get("before_sha256"):
        return _fail("G-1", "payload before_sha256 与 contract 不一致")
    if payload.get("after_sha256") != entry.get("after_sha256"):
        return _fail("G-1", "payload after_sha256 与 contract 不一致")
    if payload.get("backup_path") != entry.get("backup_path"):
        return _fail("G-1", "payload backup_path 与 contract 不一致")
    phase = payload.get("migration_phase")
    if phase not in {"pre", "post"}:
        return _fail("G-1", f"migration_phase 不合法：{phase}")
    target_abs = REPO_ROOT / target
    actual = _sha256_file(target_abs) if target_abs.exists() else "MISSING"
    expected = (
        entry.get("before_sha256")
        if phase == "pre"
        else entry.get("after_sha256")
    )
    if actual != expected:
        return _fail(
            "G-1",
            f"{phase} 阶段目标哈希不匹配",
            {"actual": actual, "expected": expected},
        )
    before_hash = entry.get("before_sha256")
    if before_hash != "MISSING":
        backup = REPO_ROOT / _strip_dot_slash(entry.get("backup_path") or "")
        if not backup.exists() or _sha256_file(backup) != before_hash:
            return _fail("G-1", "备份不存在或哈希不等于 before_sha256")
    if not entry.get("restore_command"):
        return _fail("G-1", "contract 缺 restore_command")
    return _ok(
        "G-1",
        "一次性治理迁移 contract 与哈希一致",
        {"phase": phase, "write_target": target},
    )


def v20_structural_prior(payload, today):
    """V-20 结构先验必须短、未校准且不包含动作或资本字段。"""
    prior = payload.get("structural_prior")
    if prior is None:
        return _ok("V-20", "无 structural_prior，跳过")
    if not isinstance(prior, dict):
        return _fail("V-20", "structural_prior 必须是对象")
    domain_ids = prior.get("domain_ids")
    if not isinstance(domain_ids, list) or len(domain_ids) > 2:
        return _fail("V-20", "domain_ids 必须是最多两个领域的列表")
    unknown_domains = set(domain_ids) - REGISTERED_DOMAIN_IDS
    if unknown_domains:
        return _fail("V-20", f"未登记领域：{sorted(unknown_domains)}")
    if prior.get("structural_fit") not in ALLOWED_STRUCTURAL_FITS:
        return _fail("V-20", "structural_fit 不合法")
    if prior.get("evidence_status") != "uncalibrated":
        return _fail("V-20", "evidence_status 必须固定为 uncalibrated")
    patterns = prior.get("qualified_patterns")
    if not isinstance(patterns, list) or len(patterns) > 3:
        return _fail("V-20", "qualified_patterns 必须是最多三个模式的列表")
    questions = prior.get("first_questions")
    if not isinstance(questions, list) or len(questions) > 3:
        return _fail("V-20", "first_questions 必须是最多三个问题的列表")
    if prior.get("next_step") not in ALLOWED_STRUCTURAL_NEXT_STEPS:
        return _fail("V-20", "next_step 不合法")
    serialized = json.dumps(prior, ensure_ascii=False, sort_keys=True)
    forbidden = re.search(
        r"(target_price|position_size|buy_authorization|H_B|H_R|H_L|H_C|"
        r"建立验证仓|升级确认仓|不加仓|降级或退出)",
        serialized,
        re.UNICODE,
    )
    if forbidden:
        return _fail("V-20", f"structural_prior 含禁止内容：{forbidden.group(0)}")
    return _ok("V-20", "structural_prior 边界与长度合法")


def k5_qualified_pattern(payload, today):
    """K-5 合格模式必须满足双根来源、双复用和显式因果/证伪。"""
    patterns = payload.get("qualified_patterns")
    if patterns is None:
        return _ok("K-5", "无 qualified_patterns，跳过")
    if not isinstance(patterns, list) or len(patterns) > 5:
        return _fail("K-5", "领域前台 qualified_patterns 必须是 0–5 项")
    for idx, pattern in enumerate(patterns):
        if not isinstance(pattern, dict):
            return _fail("K-5", f"pattern[{idx}] 不是对象")
        required = {
            "pattern_id",
            "recognition_cues",
            "causal_chain",
            "payer_and_money_path",
            "profit_control",
            "favorable_fit",
            "counterpattern_and_falsifier",
            "applicable_asset_types",
            "linked_cases",
            "first_questions",
            "root_sources",
            "reused_targets_or_settled_cases",
        }
        missing = required - set(pattern.keys())
        if missing:
            return _fail("K-5", f"pattern[{idx}] 缺字段：{sorted(missing)}")
        roots = pattern.get("root_sources")
        reuse = pattern.get("reused_targets_or_settled_cases")
        if not isinstance(roots, list) or len(set(roots)) < 2:
            return _fail("K-5", f"pattern[{idx}] 独立根来源不足两个")
        if not isinstance(reuse, list) or len(set(reuse)) < 2:
            return _fail("K-5", f"pattern[{idx}] 复用标的/已结算 Case 不足两个")
        if not pattern.get("causal_chain") or not pattern.get(
            "counterpattern_and_falsifier"
        ):
            return _fail("K-5", f"pattern[{idx}] 缺因果链或失败条件")
    return _ok("K-5", f"{len(patterns)} 个合格模式通过准入")


VALIDATORS = [
    ("G-1", g1_governance_migration_contract),
    ("V-1", v1_write_path),
    ("V-2", v2_state_time),
    ("V-3", v3_reviewer_derived),
    ("V-4", v4_action),
    ("V-5", v5_source_fields),
    ("V-6", v6_reviewer_completeness),
    ("V-7", v7_canonical_protection),
    ("V-8", v8_backup),
    ("V-9", v9_state_expiry_scan),
    ("V-10", v10_disagree),
    ("V-11", v11_chat_only_route),
    ("V-12", v12_batch_cap),
    ("V-13", v13_batch_legacy_majority),
    ("V-14", v14_source_classification),
    ("V-15", v15_position_trigger),
    ("V-16", v16_odds_calibration),
    ("V-17", v17_research_trigger_provenance),
    ("V-18", v18_asset_route),
    ("V-19", v19_user_output_and_unknowns),
    ("V-20", v20_structural_prior),
    # Domain model 校验（D-X 系列）
    ("D-1", d1_domain_path),
    ("D-2", d2_domain_registered),
    ("D-3", d3_thesis_status_enum),
    ("D-4", d4_time_triple),
    ("D-5", d5_no_capital_action),
    ("D-6", d6_murphy_ai_split),
    ("D-7", d7_canonical_sink_match),
    ("D-8", d8_reviewer_pass),
    # Research Knowledge / Belief / Expectation / Automation
    ("K-1", k1_content_type_path),
    ("K-2", k2_belief_contract),
    ("K-3", k3_ljg_projection_boundary),
    ("K-4", k4_single_active_canonical),
    ("K-5", k5_qualified_pattern),
    ("U-1", u1_belief_update_contract),
    ("U-2", u2_root_source_dedupe),
    ("U-3", u3_evidence_channel_boundary),
    ("E-1", e1_expectation_contract),
    ("E-2", e2_funding_ledger),
    ("E-3", e3_frozen_version),
    ("A-1", a1_automation_authority),
    ("A-2", a2_automation_staging_contract),
    ("A-3", a3_run_log_sanitization),
]


def run(payload):
    today = _today(payload)
    results = []
    for code, fn in VALIDATORS:
        try:
            r = fn(payload, today)
        except Exception as e:  # pragma: no cover
            r = _fail(code, f"validator 异常：{type(e).__name__}: {e}")
        results.append(r)
    overall = "PASS" if all(r["status"] == "OK" for r in results) else "FAIL"
    return {"overall": overall, "checks": results}


def main(argv):
    try:
        payload = _read_input(argv)
    except (OSError, json.JSONDecodeError) as e:
        print(json.dumps({"overall": "FAIL",
                          "error": f"input read failed: {e}"},
                         ensure_ascii=False, indent=2))
        return 2
    report = run(payload)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["overall"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
