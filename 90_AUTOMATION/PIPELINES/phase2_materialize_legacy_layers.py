from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATE = "2026-07-23"
PLAN = "分析报告/archive/260723系统_Murphy投资系统工程重构方案.md"
TWO_WEEK_STATE_EXTRA = """data_cutoff: 2026-07-23
expires_at: 2026-08-06
"""


def fm(layer: str, role: str, status: str = "active", authority: str = "none", extra: str = "") -> str:
    return f"""---
title: {role}
date: {DATE}
updated: {DATE}
layer: {layer}
primary_role: {role}
status: {status}
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: {authority}
source_paths:
  - {PLAN}
{extra}---"""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def wikilink(path: Path, label: str | None = None, anchor: str | None = None) -> str:
    rel = str(path).replace("\\", "/")
    target = rel + (f"#{anchor}" if anchor else "")
    if label:
        return f"[[{target}|{label}]]"
    return f"[[{target}]]"


def md_files_under(*parts: str) -> list[Path]:
    base = ROOT.joinpath(*parts)
    if not base.exists():
        return []
    return sorted([p for p in base.rglob("*.md") if p.is_file()])


def classify_report(path: Path) -> str:
    name = path.name
    if name == "260723系统_Murphy投资系统工程重构方案.md":
        return "system_meta_plan"
    if "AI长报告原文" in name:
        return "ai_long_report_original"
    if "投资_每日决策简报" in name:
        return "state_daily_decision_brief"
    if "储能材料链_每日假设跟踪" in name:
        return "state_energy_daily_tracking"
    if "每日" in name or "监控" in name or "基线" in name or "准备" in name:
        return "state_or_monitoring"
    if "行为纠偏" in name or "资本纪律" in name or "训练" in name or "框架" in name or "体系" in name:
        return "method_or_system_report"
    if "组合" in str(path):
        return "portfolio_evidence_or_state"
    return "theme_or_company_evidence"


def build_analysis_report_indexes() -> None:
    files = md_files_under("分析报告")
    grouped: dict[str, list[Path]] = defaultdict(list)
    for file in files:
        grouped[classify_report(file)].append(file.relative_to(ROOT))

    theme_rows = []
    state_rows = []
    long_rows = []
    method_rows = []
    all_rows = []
    for role in sorted(grouped):
        for rel in grouped[role]:
            row = f"| `{role}` | {wikilink(rel)} | `decision_authority: none` |"
            all_rows.append(row)
            if role.startswith("state_") or role == "state_or_monitoring" or role == "portfolio_evidence_or_state":
                state_rows.append(row)
            elif role == "ai_long_report_original":
                long_rows.append(row)
            elif role in {"method_or_system_report", "system_meta_plan"}:
                method_rows.append(row)
            else:
                theme_rows.append(row)

    theme_text = f"""
{fm("EVIDENCE", "analysis_reports_evidence_index", "active", "none")}

# Analysis Reports Evidence Index

## 先说人话

**今天发生了什么：**`分析报告/` 已接入 Evidence 前台，并按主题 Evidence、方法报告、State、AI 长报告分账。

**为什么重要：**长报告和每日简报都保留，但它们不自动拥有当前决策权限；每日简报是会过期的 State，AI 长报告是历史推理底稿。

**现在做什么：**查证据从这里进入；做当前动作仍回到 [[02_术/TRADING_SYSTEM/00_DECISION_CONTRACT]]。

| 角色 | 旧文件 | 权限 |
|---|---|---|
{chr(10).join(theme_rows + method_rows)}
"""
    write(ROOT / "05_EVIDENCE_META/EVIDENCE/THEMES/ANALYSIS_REPORTS_INDEX.md", theme_text)

    state_text = f"""
{fm("STATE", "analysis_state_archive_index", "active", "none", TWO_WEEK_STATE_EXTRA)}

# Analysis State Archive Index

## 先说人话

**今天发生了什么：**每日决策简报、每日假设跟踪、监控基线和组合 State 已集中登记。

**为什么重要：**这些内容记录某一时点的判断，不能反向污染长期 MINDSET 或 Constitution。

**现在做什么：**使用前先看日期、数据截止和是否已经过期。

| 角色 | 旧文件 | 权限 |
|---|---|---|
{chr(10).join(state_rows)}
"""
    write(ROOT / "05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/ANALYSIS_STATE_ARCHIVE_INDEX.md", state_text)

    long_text = f"""
{fm("EVIDENCE", "ai_long_reports_index", "active", "none")}

# AI Long Reports Index

## 先说人话

**今天发生了什么：**分析报告中的 `AI长报告原文` 已集中登记。

**为什么重要：**AI 长报告必须保留，作为历史推理和证据线索；但它不能因为篇幅长或 AI 一致而提高决策权限。

**现在做什么：**需要原始推理底稿时查这里；进入分析体系时必须萃取关键逻辑、证据链、失败条件和待验证信号。

| 角色 | 旧文件 | 权限 |
|---|---|---|
{chr(10).join(long_rows)}
"""
    write(ROOT / "05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/AI_LONG_REPORTS_INDEX.md", long_text)

    all_text = f"""
{fm("META", "analysis_reports_full_role_index", "active", "none")}

# Analysis Reports Full Role Index

| 角色 | 旧文件 | 权限 |
|---|---|---|
{chr(10).join(all_rows)}
"""
    write(ROOT / "05_EVIDENCE_META/META/ANALYSIS_REPORTS_FULL_ROLE_INDEX.md", all_text)


def classify_concept(path: Path) -> str:
    rel = str(path.relative_to(ROOT))
    name = path.name
    if rel.startswith("基础概念/交易策略组合/"):
        if "期权" in name or "Roll" in name or "波动率" in name:
            return "old_options_method"
        if "AI长报告原文" in name:
            return "ai_long_report_original"
        if "训练" in name or "SOP" in name or "框架" in name or "概念" in name:
            return "legacy_method_source"
        return "method_or_theme_evidence"
    if rel.startswith("基础概念/实体商/"):
        if name.endswith(".org"):
            return "raw_external_or_org_evidence"
        if "投资决策" in name or "交易方案" in name or "未命名" in name:
            return "case_or_company_state"
        return "company_evidence"
    if rel.startswith("基础概念/IP 消费类/"):
        return "ip_case_and_philosophy_candidate"
    if rel.startswith("基础概念/ploymarket/"):
        return "legacy_automation_or_dashboard"
    return "concept_misc"


def build_concept_indexes() -> None:
    files = md_files_under("基础概念")
    grouped: dict[str, list[Path]] = defaultdict(list)
    for file in files:
        grouped[classify_concept(file)].append(file.relative_to(ROOT))

    method_rows = []
    company_rows = []
    case_rows = []
    automation_rows = []
    long_rows = []
    all_rows = []
    for role in sorted(grouped):
        for rel in grouped[role]:
            row = f"| `{role}` | {wikilink(rel)} | `decision_authority: none` |"
            all_rows.append(row)
            if role in {"legacy_method_source", "old_options_method", "method_or_theme_evidence"}:
                method_rows.append(row)
            elif role in {"company_evidence", "raw_external_or_org_evidence"}:
                company_rows.append(row)
            elif role in {"case_or_company_state", "ip_case_and_philosophy_candidate"}:
                case_rows.append(row)
            elif role == "legacy_automation_or_dashboard":
                automation_rows.append(row)
            elif role == "ai_long_report_original":
                long_rows.append(row)

    method_text = f"""
{fm("METHOD", "basic_concepts_method_source_index", "active", "operational")}

# Basic Concepts Method Source Index

## 先说人话

**今天发生了什么：**`基础概念/交易策略组合` 的旧方法接入 `02_术`。

**为什么重要：**这些文件很多仍有方法价值，但旧期权、旧训练和旧框架不能继续绕过新权限。

**现在做什么：**方法更新时从这里找旧来源，再写入 canonical Skill 和 changelog。

| 角色 | 旧文件 | 权限 |
|---|---|---|
{chr(10).join(method_rows)}
"""
    write(ROOT / "02_术/SKILLS/BASIC_CONCEPTS_METHOD_SOURCE_INDEX.md", method_text)

    company_text = f"""
{fm("EVIDENCE", "basic_concepts_company_evidence_index", "active", "none")}

# Basic Concepts Company Evidence Index

| 角色 | 旧文件 | 权限 |
|---|---|---|
{chr(10).join(company_rows)}
"""
    write(ROOT / "05_EVIDENCE_META/EVIDENCE/COMPANIES/BASIC_CONCEPTS_COMPANY_EVIDENCE_INDEX.md", company_text)

    case_text = f"""
{fm("CASE", "basic_concepts_case_source_index", "active", "none")}

# Basic Concepts Case Source Index

## 先说人话

**今天发生了什么：**基础概念中的公司决策短记、IP 消费原文和原始情绪材料接入 Case Gym。

**为什么重要：**这些材料可以生成观察和候选，但不能直接写成人格或 Constitution。

**现在做什么：**需要提炼 Case 时，先按 [[04_CASE_GYM/CASE_CAPTURE_TEMPLATE]] 转成可结算格式。

| 角色 | 旧文件 | 权限 |
|---|---|---|
{chr(10).join(case_rows)}
"""
    write(ROOT / "04_CASE_GYM/RESEARCH_CASES/BASIC_CONCEPTS_CASE_SOURCE_INDEX.md", case_text)

    automation_text = f"""
{fm("AUTOMATION", "ploymarket_legacy_automation_index", "active", "none")}

# Ploymarket Legacy Automation Index

| 角色 | 旧文件 | 权限 |
|---|---|---|
{chr(10).join(automation_rows)}
"""
    write(ROOT / "90_AUTOMATION/RUNTIME/PLOYMARKET_LEGACY_AUTOMATION_INDEX.md", automation_text)

    long_text = f"""
{fm("EVIDENCE", "basic_concepts_ai_long_reports_index", "active", "none")}

# Basic Concepts AI Long Reports Index

| 角色 | 旧文件 | 权限 |
|---|---|---|
{chr(10).join(long_rows)}
"""
    write(ROOT / "05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/BASIC_CONCEPTS_AI_LONG_REPORTS_INDEX.md", long_text)

    all_text = f"""
{fm("META", "basic_concepts_full_role_index", "active", "none")}

# Basic Concepts Full Role Index

| 角色 | 旧文件 | 权限 |
|---|---|---|
{chr(10).join(all_rows)}
"""
    write(ROOT / "05_EVIDENCE_META/META/BASIC_CONCEPTS_FULL_ROLE_INDEX.md", all_text)


def extract_trade_cases() -> None:
    manual = ROOT / "📈 个人交易手册.md"
    if not manual.exists():
        return
    rows = []
    text = manual.read_text(encoding="utf-8")
    for line in text.splitlines():
        m = re.match(r"^##\s+(.+)$", line)
        if not m:
            continue
        heading = m.group(1).strip()
        if re.match(r"0\.[27]\b|[1-5]\.\s", heading):
            kind = "portfolio_state" if heading.startswith("0.2") else "trade_or_behavior_case"
            rows.append(f"| `{kind}` | {wikilink(manual.relative_to(ROOT), heading, heading)} | `decision_authority: none` |")

    case_text = f"""
{fm("CASE", "legacy_trade_cases_index", "active", "none")}

# Legacy Trade Cases Index

## 先说人话

**今天发生了什么：**个人交易手册里的持仓状态和真实交易/未交易案例接入 Case Gym。

**为什么重要：**真实 Case 很有价值，但单个 Case 不能直接生成道；它只能生成观察、临时防火墙、实验性 Skill 更新或 Philosophy Inbox 候选。

**现在做什么：**复盘时先把旧段落转成 [[04_CASE_GYM/CASE_CAPTURE_TEMPLATE]]，再决定是否进入方法反馈。

| 类型 | 旧段落 | 权限 |
|---|---|---|
{chr(10).join(rows)}
"""
    write(ROOT / "04_CASE_GYM/TRADE_LOG/LEGACY_TRADE_CASES_INDEX.md", case_text)


def build_root_legacy_index() -> None:
    files = [
        ROOT / "我的投资框架：从宏观到企业的系统思考.md",
        ROOT / "📈 个人交易手册.md",
        ROOT / "📊 股票投资看板.md",
        ROOT / "AGENTS.md",
    ]
    rows = []
    for file in files:
        if not file.exists():
            continue
        rel = file.relative_to(ROOT)
        if file.name == "我的投资框架：从宏观到企业的系统思考.md":
            role = "legacy_root_framework"
            target = "02_术 + 01_道/PHILOSOPHY_INBOX + Evidence"
        elif file.name == "📈 个人交易手册.md":
            role = "legacy_trade_manual"
            target = "03_STATE + 04_CASE_GYM + 02_术"
        elif file.name == "📊 股票投资看板.md":
            role = "legacy_dashboard_redirect"
            target = "00_HOME/HOME"
        else:
            role = "ai_operational_rules"
            target = "AGENTS.md + 00_HOME/DECISION_AUTHORITY"
        rows.append(f"| `{role}` | {wikilink(rel)} | `{target}` |")

    text = f"""
{fm("META", "root_legacy_index", "active", "none")}

# Root Legacy Index

## 先说人话

**今天发生了什么：**根目录旧框架、个人交易手册、旧看板和 AGENTS 已分账。

**为什么重要：**根目录文件最容易被误读成前台权威；现在它们各自只保留合法职责。

**现在做什么：**旧框架拆术、候选和 Evidence；个人交易手册拆 State 与 Case；旧看板看新 HOME；AGENTS 只约束 AI。

| 角色 | 旧文件 | 新去向 |
|---|---|---|
{chr(10).join(rows)}
"""
    write(ROOT / "05_EVIDENCE_META/META/ROOT_LEGACY_INDEX.md", text)


def write_case_templates() -> None:
    case_template = f"""
{fm("CASE", "case_capture_template", "active", "none")}

# Case Capture Template

```yaml
case_id:
case_type: trade | research | behavior | missed_opportunity | method_test
source:
date_opened:
date_closed:
pre_decision_context:
thesis_before_action:
action_or_non_action:
expected_result:
actual_result:
method_version:
evidence_used:
evidence_missing:
emotion_or_state:
what_changed:
what_would_have_proved_wrong:
lesson_type: observation | temporary_firewall | method_update | philosophy_candidate | no_increment
write_to:
```

## 规则

单个 Case 可以进入临时防火墙、研究问题或实验性 Skill 更新；不能直接写入 MINDSET / Constitution。
"""
    write(ROOT / "04_CASE_GYM/CASE_CAPTURE_TEMPLATE.md", case_template)

    method_template = f"""
{fm("CASE", "method_test_template", "active", "none")}

# Method Test Template

```yaml
method:
version:
reference_class:
sample:
prediction_or_rule:
time_horizon:
settlement_rule:
result:
false_positive:
false_negative:
changed_method:
rollback_needed:
```

没有参考类、期限和结算规则时，只能写 `uncalibrated`，不得输出单点概率。
"""
    write(ROOT / "04_CASE_GYM/METHOD_TESTS/METHOD_TEST_TEMPLATE.md", method_template)


def main() -> None:
    build_analysis_report_indexes()
    build_concept_indexes()
    extract_trade_cases()
    build_root_legacy_index()
    write_case_templates()


if __name__ == "__main__":
    main()
