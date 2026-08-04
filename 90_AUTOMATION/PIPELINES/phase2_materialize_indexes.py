from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATE = "2026-07-23"
PLAN = "分析报告/archive/260723系统_Murphy投资系统工程重构方案.md"
MONTH_STATE_EXTRA = """data_cutoff: 2026-07-23
expires_at: 2026-08-23
"""
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


def wikilink(path: Path, label: str | None = None) -> str:
    rel = str(path).replace("\\", "/")
    if label:
        return f"[[{rel}|{label}]]"
    return f"[[{rel}]]"


def safe_dir(name: str) -> str:
    cleaned = re.sub(r"[/:*?\"<>|]", "_", name)
    cleaned = cleaned.strip().replace("  ", " ")
    return cleaned or "UNNAMED"


def role_for_file(path: Path) -> str:
    name = path.name
    if name == "PROMPT.md":
        return "automation_prompt"
    if name == "research_task.md":
        return "state_research_task"
    if name == "company_research.md":
        return "evidence_company_research"
    if name == "evidence_log.md":
        return "evidence_log"
    if name == "scorecard.md":
        return "superseded_scorecard"
    if name == "next_questions.md":
        return "state_next_questions"
    if name == "next_signals.md":
        return "state_next_signals"
    if name == "README.md":
        return "legacy_router"
    if "AI长报告原文" in name:
        return "ai_long_report_original"
    if name.endswith(".md"):
        return "evidence_or_state_report"
    return "non_markdown_or_runtime"


def collect_company_sources() -> dict[str, list[Path]]:
    companies: dict[str, list[Path]] = defaultdict(list)
    base = ROOT / "AI周期探索/02_公司研究"
    if base.exists():
        for child in sorted(base.iterdir()):
            if child.is_dir():
                files = sorted([p for p in child.rglob("*") if p.is_file()])
                if files:
                    companies[child.name].extend(files)
    target_base = ROOT / "AI周期探索/标的研究"
    if target_base.exists():
        for child in sorted(target_base.iterdir()):
            if child.is_dir():
                files = sorted([p for p in child.rglob("*") if p.is_file()])
                if files:
                    companies[child.name].extend(files)
    return companies


def make_company_dossier(company: str, files: list[Path]) -> str:
    grouped: dict[str, list[Path]] = defaultdict(list)
    for file in files:
        grouped[role_for_file(file)].append(file.relative_to(ROOT))

    counts = {k: len(v) for k, v in grouped.items()}
    rows = []
    for role in sorted(grouped):
        links = "<br>".join(wikilink(p) for p in grouped[role])
        rows.append(f"| `{role}` | {len(grouped[role])} | {links} |")

    return f"""
{fm("EVIDENCE", "company_dossier", "active", "none")}

# {company}

## 先说人话

**今天发生了什么：**本 dossier 把旧公司研究目录接入新 Evidence 前台，但不移动旧文件。

**为什么重要：**公司研究中的 Prompt、Evidence、State、旧评分和长报告现在分账显示；旧 scorecard 和 AI 长报告不再拥有当前决策权限。

**现在做什么：**读公司证据时先看 `evidence_log` 与 `company_research`；看当前问题去 State 队列；不要用旧 `/70` scorecard 授权交易。

## 文件分账

| 角色 | 数量 | 旧文件 |
|---|---:|---|
{chr(10).join(rows)}

## 权限边界

- Evidence 可以更新研究问题，不能直接生成 `murphy_status: confirmed`。
- `scorecard.md` 属于历史 State / 旧评分，统一 `decision_authority: none`。
- `PROMPT.md` 属于 Automation 模板，不是公司事实。
- `next_questions.md`、`next_signals.md` 和 `research_task.md` 属于会过期的 State。

## 数量快照

```yaml
file_count: {len(files)}
role_counts: {counts}
```
"""


def build_company_indexes() -> None:
    companies = collect_company_sources()
    index_rows = []
    state_rows = []
    scorecard_rows = []
    for company, files in companies.items():
        dossier_dir = ROOT / "05_EVIDENCE_META/EVIDENCE/COMPANIES" / safe_dir(company)
        write(dossier_dir / "README.md", make_company_dossier(company, files))
        rel_dossier = dossier_dir.relative_to(ROOT) / "README.md"
        index_rows.append(f"| {wikilink(rel_dossier, company)} | {len(files)} | `{safe_dir(company)}` |")
        for file in files:
            rel = file.relative_to(ROOT)
            role = role_for_file(file)
            if role.startswith("state_"):
                state_rows.append(f"| `{company}` | `{role}` | {wikilink(rel)} |")
            if role == "superseded_scorecard":
                scorecard_rows.append(f"| `{company}` | {wikilink(rel)} | `decision_authority: none` |")

    company_index = f"""
{fm("EVIDENCE", "company_dossier_index", "active", "none")}

# Company Dossier Index

## 先说人话

**今天发生了什么：**旧 `AI周期探索/02_公司研究` 和 `AI周期探索/标的研究` 已按公司接入新 Evidence 前台。

**为什么重要：**这一步不是把旧报告删掉，而是让旧研究在新权限系统里有清晰位置：Evidence 是 Evidence，State 是 State，Prompt 是 Automation，旧 scorecard 是历史。

**现在做什么：**从下表进入单家公司 dossier。若要做当前投资判断，仍需回到 [[02_术/TRADING_SYSTEM/00_DECISION_CONTRACT]]。

| 公司 / 标的 | 旧文件数 | 新 dossier |
|---|---:|---|
{chr(10).join(index_rows)}
"""
    write(ROOT / "05_EVIDENCE_META/EVIDENCE/COMPANIES/COMPANY_DOSSIER_INDEX.md", company_index)

    state_index = f"""
{fm("STATE", "company_questions_index", "active", "none", MONTH_STATE_EXTRA)}

# Company Questions Index

## 先说人话

**今天发生了什么：**旧公司目录里的 `research_task`、`next_questions` 和 `next_signals` 统一接入 State 队列。

**为什么重要：**这些文件是当前研究状态，不是长期公司结论；必须定期刷新，过期后不能继续当作当前问题。

**现在做什么：**做公司研究前先看这里，再决定哪些问题需要刷新。

| 公司 / 标的 | State 类型 | 旧文件 |
|---|---|---|
{chr(10).join(state_rows)}
"""
    write(ROOT / "03_STATE/HYPOTHESIS_QUEUE/COMPANY_QUESTIONS_INDEX.md", state_index)

    scorecard_index = f"""
{fm("META", "old_scorecards_index", "active", "none")}

# Old Scorecards Index

## 先说人话

**今天发生了什么：**旧 `/70` scorecard 已集中登记为历史评分。

**为什么重要：**旧评分可以帮助理解当时 AI 怎么想，但不能进入 EV、仓位、动作或 Murphy 哲学。

**现在做什么：**需要追溯旧研究时可以查；做当前判断时先走新四票和决策合同。

| 公司 / 标的 | 旧 scorecard | 权限 |
|---|---|---|
{chr(10).join(scorecard_rows)}
"""
    write(ROOT / "05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE/OLD_SCORECARDS_INDEX.md", scorecard_index)


def build_watchlist_index() -> None:
    base = ROOT / "AI周期探索/04_投资池"
    rows = []
    if base.exists():
        for file in sorted(base.glob("*.md")):
            rows.append(f"| {file.stem} | {wikilink(file.relative_to(ROOT))} | `STATE_UPDATE only` |")
    text = f"""
{fm("STATE", "watchlists_ai_cycle_index", "active", "none", TWO_WEEK_STATE_EXTRA)}

# AI Cycle Watchlists Index

## 先说人话

**今天发生了什么：**旧投资池统一接入 `03_STATE/WATCHLISTS`。

**为什么重要：**投资池只是观察状态和研究优先级，不拥有哲学、估值或交易授权。

**现在做什么：**刷新观察池时必须带数据截止、失效日期和下一验证信号。

| 旧池 | 旧文件 | 权限 |
|---|---|---|
{chr(10).join(rows)}
"""
    write(ROOT / "03_STATE/WATCHLISTS/AI_CYCLE_WATCHLISTS_INDEX.md", text)


def build_automation_indexes() -> None:
    base = ROOT / "AI周期探索/0_总览"
    prompt_rows = []
    runtime_rows = []
    pipeline_rows = []
    if base.exists():
        for file in sorted([p for p in base.iterdir() if p.is_file()]):
            rel = file.relative_to(ROOT)
            name = file.name
            if name.startswith("LOOP_PROMPT") or name.startswith("CLAUDE_CODE_RUN_COMMAND") or name in {"CROSS_MARKET_V2_RUN_BOUNDARIES.md", "MINDSPACE_SOURCE_MCP_SOP.md"}:
                status = "current_or_historical_prompt"
                if name.endswith("_PRO.md") or name.endswith("PRO.md") or "DISCOVERY" in name:
                    status = "historical_or_specialized_prompt"
                prompt_rows.append(f"| `{name}` | {wikilink(rel)} | `{status}` |")
            elif file.suffix in {".py", ".sh"}:
                pipeline_rows.append(f"| `{name}` | {wikilink(rel)} | `pipeline_or_test` |")
            elif file.suffix in {".json", ".jsonl"} or "queue" in name or "log" in name or "watchlist" in name or "score" in name:
                runtime_rows.append(f"| `{name}` | {wikilink(rel)} | `runtime_or_state` |")

    prompt_text = f"""
{fm("AUTOMATION", "ai_cycle_prompts_index", "active", "operational")}

# AI Cycle Prompts Index

## 先说人话

**今天发生了什么：**旧 AI 周期 prompt 和 command 文件接入 `90_AUTOMATION/PROMPTS`。

**为什么重要：**Prompt 可以指导自动化研究，但不能把输出直接升级成 MINDSET 或 Constitution。

**现在做什么：**后续要挑一个 canonical prompt 时，从这里开始合并，旧 PRO 和 discovery 版本先保留历史。

| 文件 | 旧位置 | 状态 |
|---|---|---|
{chr(10).join(prompt_rows)}
"""
    write(ROOT / "90_AUTOMATION/PROMPTS/AI_CYCLE_PROMPTS_INDEX.md", prompt_text)

    runtime_text = f"""
{fm("AUTOMATION", "ai_cycle_runtime_index", "active", "none")}

# AI Cycle Runtime Index

## 先说人话

**今天发生了什么：**旧 queue、run log、watchlist 和评分表接入 runtime/state 区。

**为什么重要：**运行态会过期，只说明某次自动化跑到了哪里，不说明研究结论有效。

**现在做什么：**自动化复跑前先检查这些状态是否过期。

| 文件 | 旧位置 | 状态 |
|---|---|---|
{chr(10).join(runtime_rows)}
"""
    write(ROOT / "90_AUTOMATION/RUNTIME/AI_CYCLE_RUNTIME_INDEX.md", runtime_text)

    pipeline_text = f"""
{fm("AUTOMATION", "ai_cycle_pipelines_index", "active", "operational")}

# AI Cycle Pipelines Index

| 文件 | 旧位置 | 状态 |
|---|---|---|
{chr(10).join(pipeline_rows)}
"""
    write(ROOT / "90_AUTOMATION/PIPELINES/AI_CYCLE_PIPELINES_INDEX.md", pipeline_text)


def main() -> None:
    build_company_indexes()
    build_watchlist_index()
    build_automation_indexes()


if __name__ == "__main__":
    main()
