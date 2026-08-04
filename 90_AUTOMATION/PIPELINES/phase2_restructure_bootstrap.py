from __future__ import annotations

import csv
import hashlib
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATE = "2026-07-23"
SOURCE_PLAN = "分析报告/archive/260723系统_Murphy投资系统工程重构方案.md"


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text.strip() + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def archive_original(src: str, dst: str) -> None:
    source = ROOT / src
    target = ROOT / dst
    target.parent.mkdir(parents=True, exist_ok=True)
    if source.exists() and not target.exists():
        shutil.copy2(source, target)


def frontmatter(layer: str, primary_role: str, status: str, authority: str, extra: str = "") -> str:
    return f"""---
title: {primary_role}
date: {DATE}
updated: {DATE}
layer: {layer}
primary_role: {primary_role}
status: {status}
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: {authority}
source_paths:
  - {SOURCE_PLAN}
{extra}---"""


def target_for(path: str) -> tuple[str, str, str, str]:
    p = path.replace("\\", "/")
    name = Path(p).name

    if p == "AGENTS.md":
        return ("K+M", "AUTOMATION", "AGENTS.md + 00_HOME/DECISION_AUTHORITY.md", "operational")
    if p == "我的投资框架：从宏观到企业的系统思考.md":
        return ("S+A", "METHOD/MINDSET/EVIDENCE", "99_ARCHIVE/LEGACY_LAYOUT + 02_术/SKILLS + 01_道/PHILOSOPHY_INBOX", "none")
    if p == "📈 个人交易手册.md":
        return ("S", "STATE/CASE/METHOD", "03_STATE/PORTFOLIO_LEDGER.md + 04_CASE_GYM/TRADE_LOG + 02_术/TRADING_SYSTEM", "operational")
    if p == "📊 股票投资看板.md":
        return ("A+M", "HOME", "00_HOME/HOME.md", "none")

    if p.startswith(".claude/"):
        if "ai-research-loop-pro" in p:
            return ("A", "AUTOMATION", "90_AUTOMATION/PROMPTS or 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS", "none")
        return ("K+M", "AUTOMATION", "90_AUTOMATION/PROMPTS", "operational")

    if p == "交易宪法/CONSTITUTION.md":
        return ("S+A", "CONSTITUTION", "01_道/CONSTITUTION.md + 01_道/_HISTORY", "murphy_confirmed")
    if p == "交易宪法/MURPHY_CURRENT_COGNITIVE_MODEL.md":
        return ("S+A", "MINDSET/STATE/META", "01_道/MINDSET.md + 01_道/PHILOSOPHY_INBOX/INFERRED_PATTERNS.md + 03_STATE", "none")
    if p.startswith("交易宪法/_meta/"):
        if "认知命题证据账本" in p:
            return ("S+M+D", "META", "05_EVIDENCE_META/META/CLAIM_LEDGER.md", "none")
        if "全库投资资料覆盖清单" in p:
            return ("S+M+D", "META", "05_EVIDENCE_META/META/COVERAGE_MANIFEST.md", "none")
        return ("S+M+D", "META", "05_EVIDENCE_META/META", "none")
    if p.startswith("交易宪法/skills/"):
        if name.startswith("04_"):
            return ("K+M", "METHOD", "02_术/SKILLS/BEHAVIOR_REVIEW.md", "operational")
        if name.startswith("05_"):
            return ("K+S", "METHOD", "02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION.md + PARAMETERS.md", "operational")
        if name.startswith("07_"):
            return ("S+A", "META/METHOD", "05_EVIDENCE_META/META + 02_术/SKILLS", "none")
        return ("M", "METHOD", "02_术/TRADING_SYSTEM or 02_术/SKILLS", "operational")
    if p.startswith("交易宪法/每日投资观察和思考/"):
        return ("D+S", "STATE/MINDSET_INBOX", "03_STATE + 01_道/PHILOSOPHY_INBOX", "none")

    if p.startswith("AI周期探索/0_总览/"):
        if name.startswith("LOOP_PROMPT") or name.startswith("CLAUDE_CODE_RUN_COMMAND"):
            return ("M+A", "AUTOMATION", "90_AUTOMATION/PROMPTS", "operational")
        if name in {"AI投资主线.md", "BOTTLENECK_3X_FRAMEWORK.md", "结构性转变判断框架.md"}:
            return ("M", "METHOD", "02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK.md", "operational")
        if name.endswith((".py", ".sh")):
            return ("M+D", "AUTOMATION", "90_AUTOMATION/PIPELINES or 90_AUTOMATION/TESTS", "operational")
        if name.endswith((".json", ".jsonl")) or "queue" in name or "log" in name or "watchlist" in name:
            return ("D+A", "STATE/AUTOMATION", "03_STATE/AUTOMATION_STATE or 90_AUTOMATION/RUNTIME", "none")
        return ("D+A", "STATE/METHOD/AUTOMATION", "03_STATE or 90_AUTOMATION", "none")

    if p.startswith("AI周期探索/01_赛道研究/"):
        return ("D+S", "EVIDENCE/STATE", "05_EVIDENCE_META/EVIDENCE/THEMES + 03_STATE", "none")

    if p.startswith("AI周期探索/02_公司研究/") or p.startswith("AI周期探索/标的研究/"):
        if name == "PROMPT.md":
            return ("M", "AUTOMATION", "90_AUTOMATION/PROMPTS", "operational")
        if name == "research_task.md":
            return ("D+A", "STATE/AUTOMATION", "03_STATE/HYPOTHESIS_QUEUE", "none")
        if name == "company_research.md":
            return ("D", "EVIDENCE", "05_EVIDENCE_META/EVIDENCE/COMPANIES", "none")
        if name == "evidence_log.md":
            return ("D+M", "EVIDENCE", "05_EVIDENCE_META/EVIDENCE/COMPANIES", "none")
        if name == "scorecard.md":
            return ("A+D", "ARCHIVE", "05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE", "none")
        if name in {"next_questions.md", "next_signals.md"}:
            return ("D+M", "STATE", "03_STATE/HYPOTHESIS_QUEUE", "none")
        if name == "README.md":
            return ("M", "EVIDENCE_ROUTER", "05_EVIDENCE_META/EVIDENCE/COMPANIES", "none")
        return ("D+S", "EVIDENCE/STATE", "05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE", "none")

    if p.startswith("AI周期探索/04_投资池/"):
        return ("D+M", "STATE", "03_STATE/WATCHLISTS", "none")

    if p.startswith("分析报告/个人投资组合经营与资本配置/"):
        return ("S+D+A", "EVIDENCE/STATE/METHOD", "05_EVIDENCE_META/EVIDENCE + 03_STATE + 02_术", "none")
    if p.startswith("分析报告/archive/merged_sources/"):
        return ("D+A", "EVIDENCE_ARCHIVE", "05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS", "none")
    if p.startswith("分析报告/archive/"):
        if "每日假设跟踪" in name:
            return ("D+M", "EVIDENCE_ARCHIVE", "05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE", "none")
        if "每日决策简报" in name:
            return ("D", "STATE_ARCHIVE", "05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE", "none")
        if p == SOURCE_PLAN:
            return ("K", "META", SOURCE_PLAN, "operational")
        return ("D+S", "EVIDENCE/METHOD", "05_EVIDENCE_META/EVIDENCE + 02_术", "none")
    if p.startswith("分析报告/"):
        if name == "分析报告合并索引.md":
            return ("M+A", "EVIDENCE_ARCHIVE", "05_EVIDENCE_META/EVIDENCE", "none")
        return ("D", "EVIDENCE", "05_EVIDENCE_META/EVIDENCE", "none")

    if p.startswith("基础概念/交易策略组合/"):
        return ("M+S+A", "METHOD/EVIDENCE_ARCHIVE", "02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS", "operational")
    if p.startswith("基础概念/实体商/"):
        if name.endswith(".json"):
            return ("M", "AUTOMATION", "90_AUTOMATION/RUNTIME", "none")
        if name.endswith(".org"):
            return ("D", "EVIDENCE", "05_EVIDENCE_META/EVIDENCE/COMPANIES", "none")
        return ("D+S", "EVIDENCE/CASE", "05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM", "none")
    if p.startswith("基础概念/IP 消费类/"):
        return ("D+S", "EVIDENCE/CASE/MINDSET_INBOX", "05_EVIDENCE_META/EVIDENCE/THEMES + 04_CASE_GYM + 01_道/PHILOSOPHY_INBOX", "none")
    if p.startswith("基础概念/ploymarket/"):
        return ("A+D", "EVIDENCE/AUTOMATION", "05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS + 90_AUTOMATION", "none")
    if p.startswith("基础概念/"):
        return ("D+S", "EVIDENCE/METHOD", "05_EVIDENCE_META/EVIDENCE + 02_术/SKILLS", "none")

    if p.startswith("codeex 版本/"):
        return ("A+M", "AUTOMATION_ARCHIVE", "90_AUTOMATION + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS", "none")

    if name == ".DS_Store":
        return ("X?", "SYSTEM", "99_ARCHIVE/LEGACY_LAYOUT or delete after review", "none")
    return ("D?", "UNCLASSIFIED", "05_EVIDENCE_META/META/MIGRATION_REVIEW_QUEUE.md", "none")


def legacy_files() -> list[Path]:
    roots = [
        "AGENTS.md",
        "我的投资框架：从宏观到企业的系统思考.md",
        "📈 个人交易手册.md",
        "📊 股票投资看板.md",
        ".claude",
        "AI周期探索",
        "交易宪法",
        "分析报告",
        "基础概念",
        "codeex 版本",
    ]
    files: list[Path] = []
    for item in roots:
        path = ROOT / item
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend([p for p in path.rglob("*") if p.is_file()])
    return sorted(set(files), key=lambda p: str(p.relative_to(ROOT)))


def build_manifest() -> list[dict[str, str]]:
    rows = []
    for file in legacy_files():
        rel = str(file.relative_to(ROOT))
        action, layer, target, authority = target_for(rel)
        rows.append({
            "path": rel,
            "ext": file.suffix or "(none)",
            "sha256": sha256(file)[:16],
            "action": action,
            "target_layer": layer,
            "target": target,
            "post_migration_decision_authority": authority,
        })
    return rows


def write_manifest(rows: list[dict[str, str]]) -> None:
    csv_path = ROOT / "05_EVIDENCE_META/META/COVERAGE_MANIFEST.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    md_rows = "\n".join(
        f"| `{r['path']}` | `{r['action']}` | `{r['target_layer']}` | `{r['target']}` | `{r['post_migration_decision_authority']}` |"
        for r in rows
    )
    md = f"""
{frontmatter("META", "coverage_manifest", "active", "none")}

# 全库迁移 Manifest

## 先说人话

**今天发生了什么：**第二阶段建立了逐文件迁移记录。当前本地旧结构扫描到 `{len(rows)}` 个文件，其中 `{sum(1 for r in rows if r['ext'] == '.md')}` 个 Markdown。

**为什么重要：**每个旧文件都有去向，旧内容不会因为不在前台就消失，也不会因为还能被搜索到就继续拥有决策权限。

**现在做什么：**前台先使用 `00_HOME/HOME.md`、`01_道/CONSTITUTION.md`、`01_道/MINDSET.md` 和 `02_术/`。旧路径只作为来源、历史、State 或 Evidence 使用，不能越级授权交易或哲学。

CSV 版本：[[05_EVIDENCE_META/META/COVERAGE_MANIFEST.csv]]

| 旧路径 | 动作 | 目标层 | 建议去向 | 迁移后权限 |
|---|---|---|---|---|
{md_rows}
"""
    write("05_EVIDENCE_META/META/COVERAGE_MANIFEST.md", md)


def main() -> None:
    archive_original("交易宪法/CONSTITUTION.md", "01_道/_HISTORY/260721旧CONSTITUTION_历史原文.md")
    archive_original("交易宪法/MURPHY_CURRENT_COGNITIVE_MODEL.md", "01_道/_HISTORY/260722旧MURPHY_CURRENT_COGNITIVE_MODEL_历史原文.md")
    archive_original("交易宪法/_meta/认知命题证据账本.md", "01_道/_HISTORY/260722旧认知命题证据账本_历史原文.md")
    archive_original("交易宪法/_meta/规则溯源与冲突裁决表.md", "01_道/_HISTORY/旧规则溯源与冲突裁决表_历史原文.md")
    archive_original("交易宪法/_meta/认知模型来源分级与版本记录.md", "01_道/_HISTORY/旧认知模型来源分级与版本记录_历史原文.md")
    archive_original("交易宪法/_meta/全库投资资料覆盖清单.md", "01_道/_HISTORY/旧全库投资资料覆盖清单_历史原文.md")
    archive_original("📊 股票投资看板.md", "99_ARCHIVE/LEGACY_LAYOUT/旧股票投资看板_历史原文.md")

    write("00_HOME/HOME.md", HOME)
    write("00_HOME/SYSTEM_MAP.md", SYSTEM_MAP)
    write("00_HOME/CONTENT_ROUTER.md", CONTENT_ROUTER)
    write("00_HOME/DECISION_AUTHORITY.md", DECISION_AUTHORITY)

    write("01_道/CONSTITUTION.md", CONSTITUTION)
    write("01_道/MINDSET.md", MINDSET)
    write("01_道/PHILOSOPHY_INBOX/CANDIDATE_CLAIMS.md", CANDIDATE_CLAIMS)
    write("01_道/PHILOSOPHY_INBOX/DECISION_LOG.md", DECISION_LOG)
    write("01_道/PHILOSOPHY_INBOX/INFERRED_PATTERNS.md", INFERRED_PATTERNS)

    write("02_术/TRADING_SYSTEM/00_DECISION_CONTRACT.md", DECISION_CONTRACT)
    write("02_术/TRADING_SYSTEM/01_RESEARCH_FLOW.md", RESEARCH_FLOW)
    write("02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION.md", CAPITAL_EXECUTION)
    write("02_术/TRADING_SYSTEM/03_FEEDBACK_LOOP.md", FEEDBACK_LOOP)
    write("02_术/TRADING_SYSTEM/PARAMETERS.md", PARAMETERS)

    for path, body in SKILLS.items():
        write(f"02_术/SKILLS/{path}.md", body)

    write("03_STATE/PORTFOLIO_LEDGER.md", PORTFOLIO_LEDGER)
    write("03_STATE/MARKET_STATE/README.md", STATE_README)
    write("03_STATE/WATCHLISTS/README.md", WATCHLISTS_README)
    write("03_STATE/HYPOTHESIS_QUEUE/README.md", HYPOTHESIS_QUEUE_README)
    write("03_STATE/AUTOMATION_STATE/README.md", AUTOMATION_STATE_README)

    write("04_CASE_GYM/CASE_INDEX.md", CASE_INDEX)
    write("04_CASE_GYM/TRADE_LOG/README.md", TRADE_LOG_README)
    write("04_CASE_GYM/RESEARCH_CASES/README.md", RESEARCH_CASES_README)
    write("04_CASE_GYM/METHOD_TESTS/README.md", METHOD_TESTS_README)
    write("04_CASE_GYM/ERROR_LIBRARY/README.md", ERROR_LIBRARY_README)

    write("05_EVIDENCE_META/EVIDENCE/README.md", EVIDENCE_README)
    write("05_EVIDENCE_META/EVIDENCE/COMPANIES/README.md", COMPANIES_README)
    write("05_EVIDENCE_META/EVIDENCE/THEMES/README.md", THEMES_README)
    write("05_EVIDENCE_META/EVIDENCE/SOURCE_POINTERS/README.md", SOURCE_POINTERS_README)
    write("05_EVIDENCE_META/META/PROVENANCE_SCHEMA.md", PROVENANCE_SCHEMA)
    write("05_EVIDENCE_META/META/CLAIM_LEDGER.md", CLAIM_LEDGER)
    write("05_EVIDENCE_META/META/CONFLICT_REGISTER.md", CONFLICT_REGISTER)
    write("05_EVIDENCE_META/META/METHOD_REGISTRY.md", METHOD_REGISTRY)
    write("05_EVIDENCE_META/META/ABSORPTION_RECEIPT_TEMPLATE.md", ABSORPTION_TEMPLATE)
    write("05_EVIDENCE_META/ARCHIVE/README.md", ARCHIVE_README)
    write("90_AUTOMATION/README.md", AUTOMATION_README)
    write("90_AUTOMATION/PROMPTS/README.md", PROMPTS_README)
    write("90_AUTOMATION/RUNTIME/README.md", RUNTIME_README)
    write("99_ARCHIVE/LEGACY_LAYOUT/README.md", LEGACY_README)

    write("交易宪法/CONSTITUTION.md", OLD_CONSTITUTION_STUB)
    write("交易宪法/MURPHY_CURRENT_COGNITIVE_MODEL.md", OLD_MODEL_STUB)
    write("交易宪法/_meta/认知命题证据账本.md", OLD_CLAIM_LEDGER_STUB)
    write("交易宪法/_meta/全库投资资料覆盖清单.md", OLD_COVERAGE_STUB)
    write("交易宪法/_meta/规则溯源与冲突裁决表.md", OLD_RULES_STUB)
    write("交易宪法/_meta/认知模型来源分级与版本记录.md", OLD_PROVENANCE_STUB)
    write("📊 股票投资看板.md", OLD_DASHBOARD_STUB)

    rows = build_manifest()
    write_manifest(rows)
    write("05_EVIDENCE_META/META/PHASE2_EXECUTION_LOG.md", EXECUTION_LOG.format(file_count=len(rows), md_count=sum(1 for r in rows if r["ext"] == ".md")))


HOME = f"""
{frontmatter("META", "home", "active", "operational")}

# Murphy 投资系统 HOME

## 先说人话

**今天发生了什么：**股票投资库的前台入口切换到分层结构：道、术、State、Case、Evidence、Automation 各自只做一件事。

**为什么重要：**以后不能再因为某段内容写在“宪法”“认知模型”或长报告里，就自动拥有最高权限。先看它属于哪一层，再决定它能改变什么。

**现在做什么：**从这里进入系统。要做投资判断，先走 [[02_术/TRADING_SYSTEM/00_DECISION_CONTRACT|决策合同]]；要查长期边界，看 [[01_道/CONSTITUTION|Constitution]]；要吸收新材料，看 [[00_HOME/CONTENT_ROUTER|内容路由]]。

## 前台入口

| 入口 | 用途 | 权限 |
|---|---|---|
| [[00_HOME/DECISION_AUTHORITY|权限说明]] | 先判断道、术、治理谁有权决定 | operational |
| [[01_道/CONSTITUTION|Constitution]] | 长期 Guardrail + Router | murphy_confirmed |
| [[01_道/MINDSET|MINDSET]] | Murphy 已确认的长期认知前台 | murphy_confirmed |
| [[01_道/PHILOSOPHY_INBOX/CANDIDATE_CLAIMS|Philosophy Inbox]] | 候选命题、反例和待裁决项 | none |
| [[02_术/TRADING_SYSTEM/00_DECISION_CONTRACT|Trading System]] | 研究、资本、执行与反馈合同 | operational |
| [[02_术/SKILLS/COMPANY_FUNDAMENTALS|Skills]] | 可进化的方法模块 | operational |
| [[03_STATE/PORTFOLIO_LEDGER|State]] | 持仓、市场、观察池和待验证状态 | none |
| [[04_CASE_GYM/CASE_INDEX|Case Gym]] | 真实交易、研究结算和错误库 | none |
| [[05_EVIDENCE_META/EVIDENCE/README|Evidence]] | 原始证据、公司和主题材料 | none |
| [[05_EVIDENCE_META/META/COVERAGE_MANIFEST|Coverage Manifest]] | 全库迁移记录 | none |

## 一句话规则

道由 Murphy 裁决；术由系统训练；治理由 Codex 执行；State 会过期；Case 要结算；Evidence 只能提供证据，不能冒充信念。
"""

SYSTEM_MAP = f"""
{frontmatter("META", "system_map", "active", "operational")}

# 系统地图

| 层 | 唯一主职责 | 不允许做什么 |
|---|---|---|
| `00_HOME` | 入口、路由、权限 | 不保存投资结论 |
| `01_道` | 已确认长期认知与禁止事项 | 不放 State、公司判断、参数、AI 推断 |
| `02_术` | 可进化的研究和交易方法 | 不自动升级成道 |
| `03_STATE` | 当前状态、待验证、观察池 | 不进入长期页面，必须过期 |
| `04_CASE_GYM` | 真实案例、训练样本、结算 | 单个 Case 不直接生成原则 |
| `05_EVIDENCE_META` | 证据、来源、冲突、覆盖 | 不替 Murphy 裁决 |
| `90_AUTOMATION` | prompts、脚本、测试、运行态 | 不与投资内容混放 |
| `99_ARCHIVE` | 旧结构、历史系统、待复核内容 | 不在前台授权 |

## 旧结构的状态

旧 `交易宪法/CONSTITUTION.md`、`MURPHY_CURRENT_COGNITIVE_MODEL.md` 和 `_meta` 账本已经降为兼容入口。完整历史原文保存在 [[01_道/_HISTORY]]，前台权威以本新结构为准。
"""

CONTENT_ROUTER = f"""
{frontmatter("META", "content_router", "active", "operational")}

# 内容路由

## 新材料吸收

任何文章、研报、财报、截图、PDF、播客或长文本进入后，不以摘要完成为标准，而是回答：

- **新东西是什么：**
- **改变了什么：**
- **写到哪里：**

## 四种合法影响

| 结果 | 使用条件 | 写到哪里 | 权限 |
|---|---|---|---|
| `METHOD_UPDATE` | 新方法、机制或检查项 | `02_术` | 可更新术，不能改道 |
| `STATE_UPDATE` | 改变当前宏观、行业、公司、资金、持仓 | `03_STATE` | 必须有 `data_cutoff/expires_at` |
| `PHILOSOPHY_CANDIDATE` | 挑战或强化长期底层认知 | `01_道/PHILOSOPHY_INBOX` | 只能候选 |
| `NO_INCREMENT` | 同根重复或无决策增量 | 回执 | 不新增概念 |

## 外部信源前置路由

用户直接提供文章、链接、截图、PDF 或长文本并要求解读、伴读、提炼时，如果没有明确归档位置，写文件前先问：进入当前周信息源、进入某个主题或标的体系，还是两边都要。未回答前可以在对话里解释，但不得创建、移动或改写笔记文件。

## 股票调研归档

单一标的优先进入已有标的目录；多个标的、组合比较、跨标的主题和场景分析进入 `分析报告/archive/`。长报告必须保留，但进入分析体系的是萃取版。
"""

DECISION_AUTHORITY = f"""
{frontmatter("META", "decision_authority", "active", "operational")}

# 权限说明

## 三类问题

| 类型 | 定义 | 谁决定 | Codex 可以做 | Codex 不得做 |
|---|---|---|---|---|
| 道 | 投资本质、长期原则、长期不可违背边界 | Murphy | 搜原文、整理候选、找反例、记录裁决 | 自行确认，冒充第一人称 |
| 术 | 宏观、产业、企业、估值、交易的方法 | 系统 | 根据 Evidence 和 Case 合并、拆分、升级、降级、退役 | 违反已确认的道，自动升级成道 |
| 治理 | 文件职责、目录、权限、版本、TTL、归档、路由、来源标签 | Codex | 直接执行并记录 | 借治理改写道 |

## 停问规则

不需要询问 Murphy：目录命名、Archive 分层、State TTL 默认值、旧标签双状态迁移、Evidence 去重、Skill 合并拆分、HOME、Router、索引、链接修复、manifest、历史长报告归档。

必须暂停对应项目：把候选写成 MINDSET、改变 Constitution Guardrail 核心含义、无法确认原话却准备第一人称使用、两条已确认的道冲突、需要不可恢复删除唯一原始材料。
"""

CONSTITUTION = f"""
{frontmatter("CONSTITUTION", "guardrail_router", "active", "murphy_confirmed")}

# Constitution

## 先说人话

**今天发生了什么：**旧 Constitution 被收缩为长期 Guardrail + Router。人格、方法、State、Case、AI 权限和证据协议不再混在个人宪法里。

**为什么重要：**宪法只负责防止投资系统越界，不负责证明某个公司好、某个价格便宜，或某个方法永远有效。

**现在做什么：**任何增加风险的动作，先检查七条 Guardrail；具体怎么研究和执行，转入 Router 指向的 Trading System 与 Skills。

## Guardrail

| ID | 长期边界 |
|---|---|
| G-01 | **生活与投资隔离：**不拿不能失去的钱承担投资风险。 |
| G-02 | **不让单一好理由代替完整投资：**至少知道赚什么、为什么现在、错了损失什么。 |
| G-03 | **不让价格替基本面投票：**价格、政策、Attention、AI 共识都不能代替企业事实。 |
| G-04 | **不在情绪最强时增加不可逆风险：**恐慌、FOMO、回本和踏空不能成为增加风险的主要理由。 |
| G-05 | **不承担可能使自己出局的风险：**不使用最大损失无法承受、退出依赖运气、Roll 或持续融资才能生存的结构。 |
| G-06 | **不伪造确定性：**没有样本不伪造概率，没有依据不制造精确目标价，多个 AI 一致不等于独立证据。 |
| G-07 | **不让过去拥有今天的投票权：**成本价、沉没投入和过去判断不能决定今天是否继续持有。 |

## Router

| 需要解决的问题 | 去哪里 |
|---|---|
| 研究是否能进入动作 | [[02_术/TRADING_SYSTEM/00_DECISION_CONTRACT]] |
| 资本、风险、期权、成交事实 | [[02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION]] |
| 宏观和流动性传导 | [[02_术/SKILLS/LIQUIDITY_TRANSMISSION]] |
| 产业卡点、供需和必经之路 | [[02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK]]、[[02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND]] |
| 公司基本面 | [[02_术/SKILLS/COMPANY_FUNDAMENTALS]] |
| 市场预期与估值 | [[02_术/SKILLS/EXPECTATIONS_LEDGER]]、[[02_术/SKILLS/EXPECTATIONS_VALUATION]] |
| 行为触发、亏损后加风险、AI 共识 | [[02_术/SKILLS/BEHAVIOR_REVIEW]] |
| ETF、LOF、基金 | [[02_术/SKILLS/ETF_LOF_FUND]] |
| 期权 | [[02_术/SKILLS/OPTIONS]] |
| 当前持仓、市场状态、观察池 | [[03_STATE/PORTFOLIO_LEDGER]] |
| 真实交易和方法训练样本 | [[04_CASE_GYM/CASE_INDEX]] |
| 来源、命题、冲突、覆盖 | [[05_EVIDENCE_META/META/PROVENANCE_SCHEMA]]、[[05_EVIDENCE_META/META/CLAIM_LEDGER]]、[[05_EVIDENCE_META/META/CONFLICT_REGISTER]] |
| AI 操作权限 | [[AGENTS]] |

## 边界

AI 权限、文件版本、State TTL、成交确认和自动化规则不属于个人 Constitution。它们可以约束 Codex 操作，但不能冒充 Murphy 的长期哲学。
"""

MINDSET = f"""
{frontmatter("MINDSET", "confirmed_frontstage_principles", "active", "murphy_confirmed")}

# MINDSET

## 先说人话

**今天发生了什么：**前台只保留已经在重构方案第 7.3 节给出方向性裁决的长期认知，不展示候选数据库。

**为什么重要：**长期认知要少而硬。方法、参数、案例和当前市场判断都可以很重要，但不应该挤进 MINDSET。

**现在做什么：**用这些原则规定方向；用 `02_术` 训练方法；用 `03_STATE` 保存当前判断；用 `04_CASE_GYM` 结算对错。

## 利从哪里来

股票赚的是未来现实与当前预期之间的差。政策可以改变水流，但不能替利润背书；增长不是价值，能被股东留下的增长才是价值。

## 变化如何变成利润

看十年，想三年，投一年。长期看方向，1 到 3 年找必经之路，约一年找最可能兑现的现实变化与预期差。必经不等于好投资，必须继续验证稀缺、收费权、利润留存和供给反噬。

## 为什么现实与价格会分离

先认清自己参加的是什么游戏。产业决定锚，资金形成趋势，情绪制造偏离。用什么逻辑买入，就用什么证据验证和退出。

## 人为什么容易犯错

人可以解释未来，数字必须验证过去。创始人、文化和组织只生成持续性假设；资本配置、历史兑现、利润和现金流负责验证。

## 如何在不确定中长期生存

先保证长期生存，再等待幂律机会。观点必须随证据更新；有参考类和样本才概率化，否则只写增强、削弱、未改变或推翻。

## 不写进这里的内容

四票表格、冷静期、H/O 资本桶、具体仓位、价格阈值、期权结构、当前能力圈、持仓、公司判断、市场判断和任何单次 Case 都留在术、State 或 Case Gym。
"""

CANDIDATE_CLAIMS = f"""
{frontmatter("MINDSET", "philosophy_inbox", "active", "none")}

# 候选命题 Inbox

## 先说人话

**今天发生了什么：**候选命题统一降到无决策权限的 Inbox，并使用 `evidence_status` 与 `murphy_status` 双状态。

**为什么重要：**证据强不等于 Murphy 已认同；AI 重复不等于独立证据；Case 有价值但不能直接写成人格。

**现在做什么：**只有 `murphy_status: confirmed` 且有裁决来源的命题，才允许进入 MINDSET 或 Constitution。

| ID | 候选命题 | evidence_status | murphy_status | 备注 |
|---|---|---|---|---|
| C-01 | 看十年，想三年，投一年 | mixed | confirmed | 第 7.3 节已给方向，前台只保留短句，执行细节入术 |
| C-02 | 超额利润来自变化中的稀缺 | mixed | candidate | 与必经/稀缺/收费权相关，需拆反例 |
| C-03 | 必经 → 稀缺 → 收费权 → 利润留存 | strong | candidate | 原始问题有来源，完整四段链仍作术中验证 |
| C-04 | 股票赚现实与市场预期之间的差 | mixed | confirmed | 第 7.3 节已确认方向 |
| C-05 | 产业 / 资金 / 情绪分层 | mixed | confirmed | 前台使用简单表达；三层肉留作 Skill |
| C-06 | 贝叶斯、幂律、生存等思想 | mixed | partial_confirmed | 生存和随证据更新已入前台；工具细节留术 |
| C-07 | 政策必须继续走到落地和数据验证 | strong | candidate | 已作为政策原则的执行要求 |
| C-08 | 能力圈之外优先用指数/ETF 表达 | mixed | unreviewed | 方案明确属于术，不单列哲学 |
| C-09 | 投资研究系统应像模型一样训练并检验泛化 | strong | candidate | 更像系统治理原则 |
| C-10 | 人的需求较稳定，商品与表达形式变化 | mixed | unreviewed | IP/消费主题候选 |
| C-11 | 创始人的诚实、愿景和文化可能是长期经营线索 | mixed | candidate | 已被“数字必须验证过去”约束 |
| C-12 | 物流一线经验可能形成局部信息优势 | mixed | unreviewed | 需要真实样本验证 |
| C-13 | 不行动也是决策，但持仓失败条件触发后不动是主动承担风险 | mixed | candidate | 入术和 Case，是否入道待裁决 |
| C-14 | 成本价不应替代未来价值 | strong | confirmed | 已进入 G-07 |
| C-15 | 价格和 Attention 不能直接提高业务胜率 | strong | confirmed | 已进入 G-03 |
| C-16 | AI 只有研究、反证、计算、记录和提醒权 | strong | operational | 留在 AGENTS，不写个人 Constitution |
| C-17 | 身体经验和类比可以生成研究假设，但不能证明产业结论 | mixed | candidate | 进入方法边界 |
"""

DECISION_LOG = f"""
{frontmatter("MINDSET", "decision_log", "active", "none")}

# 裁决记录

| 日期 | 来源 | 裁决 | 写入位置 |
|---|---|---|---|
| 2026-07-23 | `260723系统_Murphy投资系统工程重构方案.md` 第 7.2 节 | 治理类问题由 Codex 直接执行；术可进化；道只由 Murphy 裁决 | [[00_HOME/DECISION_AUTHORITY]] |
| 2026-07-23 | 同上第 7.4 节 | Constitution 重构为七条 Guardrail + Router | [[01_道/CONSTITUTION]] |
| 2026-07-23 | 同上第 7.3 节 | 若干长期认知方向不再重新辩论，但执行细节不得整段写入 MINDSET | [[01_道/MINDSET]] |
| 2026-07-23 | 用户本轮 `/goal` | 严格执行重构方案，不逐项请示治理参数 | 本次第二阶段执行日志 |
"""

INFERRED_PATTERNS = f"""
{frontmatter("MINDSET", "inferred_patterns", "active", "none")}

# INFERRED_PATTERNS

## 文件性质

这里保存 AI 从历史文本和 Case 中观察到的模式。它们可以启发研究和流程设计，但不得使用 Murphy 第一人称，不得进入 MINDSET，不得授权交易。

| 模式 | 来源类型 | evidence_status | murphy_status | 合法用途 |
|---|---|---|---|---|
| 更关注控制权而非热门标签 | 历史人机共建 + AI 观察 | mixed | unreviewed | 生成公司基本面检查问题 |
| 喜欢大趋势中的第一现金接收者 | AI 观察 | mixed | unreviewed | 加入供给反噬时钟 |
| 企业观偏向厚度和自我纠错 | 历史 Case + AI 观察 | mixed | unreviewed | 只作持续性假设 |
| 入场前纪律强、亏损后纪律弱 | 两个 Case 对照 | weak | unreviewed | 设计下单前冻结和退出记录 |
| 用身体经验和类比提出问题 | 多个主题材料 | mixed | unreviewed | 必须经过尺度、付款人、工程、供给、财务验收 |
"""

DECISION_CONTRACT = f"""
{frontmatter("METHOD", "decision_contract", "active", "operational")}

# 00 Decision Contract

## 先说人话

**今天发生了什么：**投资动作不再由长报告、评分表或 AI 共识直接推出，必须先通过同一份决策合同。

**为什么重要：**好故事、好公司、好价格和好情绪都可能只回答了一部分问题。增加风险前要知道自己到底在赚哪种钱，错了会损失什么。

**现在做什么：**任何结论只输出六档动作之一：`不投入 / 继续观察 / 建立验证仓 / 升级确认仓 / 不加仓 / 降级或退出`。

## 最小输入

- `business_horizon`：公司或行业变化的真实周期。
- `thesis_horizon`：这条 thesis 需要多久被验证。
- `execution_horizon`：本次动作打算承担多久的路径风险。
- `review_date`：下一次复查日期。
- `money_source`：赚基本面钱、流动性钱、风险偏好钱、认知差钱，还是事件跳变钱。
- `failure_condition`：什么事实说明我错了。

## 四票

| 票 | 问题 | 价格能否直接更新 |
|---|---|---|
| `H_B` 经营票 | 公司是否真的更赚钱 | 不能 |
| `H_R` 赔率票 | 当前价格给的回报是否足够 | 可以 |
| `H_L` 周期票 | 能否等到验证并退出 | 可以 |
| `H_C` 仓位票 | 错了是否能活下来 | 不能只靠价格 |

任一失败或未知，默认不增加风险。
"""

RESEARCH_FLOW = f"""
{frontmatter("METHOD", "research_flow", "active", "operational")}

# 01 Research Flow

## 输入

一个标的、主题、政策、财报或外部材料。

## 输出

结论、原因、要验证的数字、什么情况说明我错了、六档动作之一。

## 主流程

1. 问题分类：道、术、治理、State、Case、Evidence。
2. 期限合同：十年经营、三年 thesis、一年兑现窗口或更短事件。
3. 宏观和政策只确定环境，不替利润背书。
4. 产业找付款人、必经点、绕开路径和供给反噬。
5. 公司走收入、直接成本、毛利、经营费用、经营利润、净利润、现金流、估值。
6. 市场预期账本记录当前价格隐含了什么。
7. 四票和资本约束决定能否动作。
8. 结果进入 Case Gym，方法可被更新，道不可自动改变。

## 不能证明什么

研究完成不等于可以交易；AI 自评不等于方法有效；同一新闻多次转述不等于证据变强。
"""

CAPITAL_EXECUTION = f"""
{frontmatter("METHOD", "capital_execution", "active", "operational")}

# 02 Capital And Execution

## 输入

任何风险增加、风险降低、期权、基金申赎、成交、撤单、仓位变化或资本压力问题。

## 输出

允许动作、禁止动作、订单事实、复查时间。

## 执行边界

- 生活资金不进入投资风险。
- AI 没有交易授权权、仓位参数修改权和自动成交权。
- 主账只认券商成交、撤单、废单或到账回报。
- 亏损后想加仓、抄底或卖 Put，默认进入反方审查和冷静期；风险降低动作不被阻断。
- 期权必须定义最大损失，不能依赖 Roll、融资或运气才能生存。

## 不写在这里

具体仓位比例、账户金额和交易参数写入 [[02_术/TRADING_SYSTEM/PARAMETERS]]，且必须标注版本、来源和是否已确认。
"""

FEEDBACK_LOOP = f"""
{frontmatter("METHOD", "feedback_loop", "active", "operational")}

# 03 Feedback Loop

## Case 进入系统

Case 记录当时发生了什么、事前判断是什么、实际结果是什么、哪个方法版本参与、什么事实说明方法错了。

## Case 能改变什么

单个 Case 可以生成临时防火墙、研究问题或实验性 Skill 更新。它不能直接生成道或 Constitution 条款。

## Case 进入 Philosophy Inbox 的条件

1. 多个相互独立案例反复出现。
2. 有明确因果机制，不只是结果相似。
3. 已做反例审查。
4. 在不同市场状态下仍有解释力。

满足四项也只获得候选资格，仍不能自动进入 MINDSET。
"""

PARAMETERS = f"""
{frontmatter("METHOD", "parameters", "active", "operational")}

# Parameters

## 文件性质

这里保存会随经验和资本状态变化的参数。参数不是 Constitution，不是长期哲学，也不能从旧报告自动继承。

| 参数 | 当前状态 | 来源 | 权限 |
|---|---|---|---|
| 24 小时冷静期 | active_operational | AGENTS 与行为纪律系统 | operational |
| `uncalibrated` 概率状态 | active_operational | AGENTS 与重构方案 | operational |
| 旧 `/70` 评分 | superseded | AI 周期旧 scorecard | none |
| 固定 LR / 固定加分 | retired | 旧报告 | none |
| 未校准单点概率 | retired | 旧报告 | none |
| 旧仓位比例 | superseded | 历史报告 | none |

新增或改变参数时，必须写清依据、适用范围、失效条件和回滚方式。
"""


def skill_doc(title: str, purpose: str, inputs: str, outputs: str, cannot: str, fail: str) -> str:
    return f"""
{frontmatter("METHOD", title.lower(), "active", "operational")}

# {title}

## 职责

{purpose}

## 输入

{inputs}

## 输出

{outputs}

## 不能证明什么

{cannot}

## 失败条件

{fail}
"""


SKILLS = {
    "MACRO_REGIME": skill_doc("MACRO_REGIME", "只判断宏观状态、传导假设、可验证数据和不能证明什么。", "政策、利率、信用、成交、融资、ETF、行业宽度。", "宏观环境、传导链、待验证数字。", "宏观顺风不能证明具体公司更赚钱。", "宏观信号无法传到需求、订单、利润或现金。"),
    "LIQUIDITY_TRANSMISSION": skill_doc("LIQUIDITY_TRANSMISSION", "验收政策水、市场水、板块水、标的水。", "政策、资金流、成交深度、ETF 申赎、折溢价、退出深度。", "`H_R/H_L` 更新和传导待验证清单。", "资金和情绪不能直接更新 `H_B`。", "只有政策或价格，没有市场、板块、标的层的连续证据。"),
    "STRUCTURAL_CHANGE_BOTTLENECK": skill_doc("STRUCTURAL_CHANGE_BOTTLENECK", "发现新秩序中的必经点和瓶颈。", "产业变化、技术路线、监管、CapEx、客户预算。", "必经点、绕开路径、稀缺持续期、供给反噬时钟。", "必经不等于好投资，三倍候选不授权交易。", "客户自建、替代、扩产或监管使瓶颈失效。"),
    "INDUSTRY_SUPPLY_DEMAND": skill_doc("INDUSTRY_SUPPLY_DEMAND", "判断需求付款人、供给反应和利润池。", "需求、付款人、产能、库存、交付期、ASP、成本。", "供需链路、利润池归属、下一验证数字。", "事件密度或泊松类比不能直接当概率或仓位参数。", "需求无法穿透到收入、毛利、经营利润和现金流。"),
    "COMPANY_FUNDAMENTALS": skill_doc("COMPANY_FUNDAMENTALS", "公司怎么真正赚钱。", "收入、直接成本、毛利、经营费用、经营利润、净利润、现金流、股数和资本配置。", "`H_B` 结论、证据缺口和反证。", "高收入、高增长和好创始人不能替代股东现金。", "增长不能留下利润和现金，或每股价值被稀释。"),
    "GROWTH_TECH": skill_doc("GROWTH_TECH", "处理高增长、未盈利或资本强度高的科技资产。", "TAM、RPO、ARR、订单、容量、利用率、毛利、SBC、CapEx、完全稀释股数。", "兑现阶梯、稀释风险、资本强度和单位经济。", "TAM、签约容量和调整后指标不能证明每股 FCF。", "需求热但交付、毛利、费用和现金流不能兑现。"),
    "EXPECTATIONS_LEDGER": skill_doc("EXPECTATIONS_LEDGER", "记录市场当前隐含预期和证伪事件。", "当前价格、共识预期、管理层指引、估值倍数、事件日程。", "市场已经相信什么、下一事件如何改变预期。", "价格上涨或下跌不能证明业务变化。", "无法写清预期分母或证伪事件。"),
    "EXPECTATIONS_VALUATION": skill_doc("EXPECTATIONS_VALUATION", "先判断市场估值语法，再选择估值方式。", "资产阶段、利润/现金流、增速、资本效率、可比公司、反推情景。", "估值语法、合理区间、反证和安全边际。", "单一 PE/DCF/PEG 不能解释所有阶段。", "估值依赖伪概率、旧成本价或未校准目标价。"),
    "ETF_LOF_FUND": skill_doc("ETF_LOF_FUND", "处理 ETF、LOF、基金和包装层路径。", "成分权重、目标 ETF、申赎规则、折溢价、证券借贷、经理口径、NAV。", "底层业务、包装层资金和交易路径的分账。", "分散不等于低风险，折价不等于底层便宜。", "无法验收持仓、申赎、券商路径、费用和退出深度。"),
    "OPTIONS": skill_doc("OPTIONS", "只允许定义最大损失、合约可核验、退出路径可执行的期权表达。", "合约、到期、IV、希腊值、最大损失、流动性、退出计划。", "是否可用期权表达和最坏损失。", "Roll 不能作为生存前提，卖 Put 降成本不能绕开风险增加审查。", "最大损失不可承受，或退出依赖运气、融资、持续 Roll。"),
    "BEHAVIOR_REVIEW": skill_doc("BEHAVIOR_REVIEW", "在情绪强、亏损、踏空、AI 共识、回本愿望出现时先做反方审查。", "用户语言、持仓状态、浮盈亏、连续涨跌、纪律触发、AI 依赖迹象。", "最大漏洞、反证、最坏代价、低风险表达和允许动作。", "行为触发器不能证明标的变差，也不能替代业务证据。", "用户观点被顺着找理由，或亏损后无新增经营证据却增加风险。"),
}

STATE_EXTRA = """data_cutoff:
expires_at:
"""

PORTFOLIO_LEDGER = f"""
{frontmatter("STATE", "portfolio_ledger_index", "active", "none", STATE_EXTRA)}

# Portfolio Ledger

当前持仓、成交和账户事实只认券商回报。历史主账 [[📈 个人交易手册]] 仍是来源，但其中的方法、人格推断和单次 Case 规则不再拥有长期权限。

## 最小记录

| 字段 | 含义 |
|---|---|
| data_cutoff | 数据截止时间 |
| expires_at | 失效时间 |
| broker_fact | 成交、撤单、废单、到账等券商事实 |
| thesis_state | 当前 thesis 状态 |
| allowed_action | 六档动作之一 |
"""

STATE_README = f"{frontmatter('STATE', 'market_state_index', 'active', 'none', STATE_EXTRA)}\n\n# Market State\n\n保存会过期的宏观、市场、行业和标的水位。任何 State 必须有 `data_cutoff`、`expires_at` 或 `refresh_trigger`。"
WATCHLISTS_README = f"{frontmatter('STATE', 'watchlist_index', 'active', 'none', STATE_EXTRA)}\n\n# Watchlists\n\n观察池、核心池、暂不研究池和投资池都属于 State，不拥有交易授权。"
HYPOTHESIS_QUEUE_README = f"{frontmatter('STATE', 'hypothesis_queue', 'active', 'none', STATE_EXTRA)}\n\n# Hypothesis Queue\n\n保存公司问题、下一信号、待研究假设。问题队列会过期，不能冒充公司长期结论。"
AUTOMATION_STATE_README = f"{frontmatter('STATE', 'automation_state', 'active', 'none', STATE_EXTRA)}\n\n# Automation State\n\n保存队列、运行状态、last outcome 和日志索引。脚本和 prompt 放在 `90_AUTOMATION`。"

CASE_INDEX = f"""
{frontmatter("CASE", "case_index", "active", "none")}

# Case Gym

Case 是训练样本，不是规则证明。这里记录真实交易、研究结算、方法测试和错误库。

| 区域 | 职责 |
|---|---|
| [[04_CASE_GYM/TRADE_LOG/README]] | 真实成交、撤单、未成交和退出 |
| [[04_CASE_GYM/RESEARCH_CASES/README]] | 研究 thesis 的事前与事后 |
| [[04_CASE_GYM/METHOD_TESTS/README]] | 方法版本的盲测和回测 |
| [[04_CASE_GYM/ERROR_LIBRARY/README]] | 可复现错误模式 |
"""
TRADE_LOG_README = f"{frontmatter('CASE', 'trade_log', 'active', 'none')}\n\n# Trade Log\n\n记录券商事实、事前条件、触发器、实际动作和结果。"
RESEARCH_CASES_README = f"{frontmatter('CASE', 'research_cases', 'active', 'none')}\n\n# Research Cases\n\n记录研究判断如何被后续事实验证或推翻。"
METHOD_TESTS_README = f"{frontmatter('CASE', 'method_tests', 'active', 'none')}\n\n# Method Tests\n\n记录方法版本、样本、参考类、期限、结算规则和结果。"
ERROR_LIBRARY_README = f"{frontmatter('CASE', 'error_library', 'active', 'none')}\n\n# Error Library\n\n错误库只描述触发器和防火墙，不直接新增 Constitution。"

EVIDENCE_README = f"{frontmatter('EVIDENCE', 'evidence_index', 'active', 'none')}\n\n# Evidence\n\nEvidence 保存事实、来源、摘录和回链。Evidence 可以挑战命题，但不能自动变成 Murphy 信念。"
COMPANIES_README = f"{frontmatter('EVIDENCE', 'company_evidence_index', 'active', 'none')}\n\n# Companies\n\n一家公司一个 dossier：Evidence、State、问题队列分开。"
THEMES_README = f"{frontmatter('EVIDENCE', 'theme_evidence_index', 'active', 'none')}\n\n# Themes\n\n主题 Evidence 保存产业、政策、行业和跨标的材料。"
SOURCE_POINTERS_README = f"{frontmatter('EVIDENCE', 'source_pointers', 'active', 'none')}\n\n# Source Pointers\n\n外部原文优先留在信息源库；本库只保存决策相关摘录、事实、反证和回链。"

PROVENANCE_SCHEMA = f"""
{frontmatter("META", "provenance_schema", "active", "none")}

# Provenance Schema

```yaml
layer: MINDSET | CONSTITUTION | METHOD | STATE | CASE | EVIDENCE | META | AUTOMATION
primary_role: one_role_only
status: active | candidate | experimental | superseded | archived | retired
authored_by: murphy | human_ai | ai | external
source_type: P0 | P1 | P2 | P3 | PX
human_reviewed: true | false
decision_authority: none | operational | murphy_confirmed
data_cutoff:
expires_at:
supersedes:
source_paths:
```

`authored_by: murphy` 只用于可定位的 Murphy 原文。`human_reviewed: true` 不等于 Murphy 认同所有内容。Evidence 和 Case 永远不能靠脚本把自己改成 `murphy_confirmed`。
"""

CLAIM_LEDGER = f"""
{frontmatter("META", "claim_ledger", "active", "none")}

# Claim Ledger

## 双状态

```yaml
evidence_status: strong | mixed | weak | contradicted
murphy_status: unreviewed | candidate | confirmed | rejected
legacy_status:
```

历史“高置信、已吸收、已采纳”不得直接映射成 `confirmed`。有可定位 Murphy 裁决才可 confirmed；没有裁决时写 `unreviewed` 或 `candidate`，旧标签进入 `legacy_status`。

旧账本历史原文：[[01_道/_HISTORY/260722旧认知命题证据账本_历史原文]]
"""

CONFLICT_REGISTER = f"""
{frontmatter("META", "conflict_register", "active", "none")}

# Conflict Register

| 冲突 | 类型 | 当前处理 | 是否暂停 |
|---|---|---|---|
| 旧“已吸收/采纳/最高效力”标签与新双状态冲突 | 治理 | 旧标签保留为 `legacy_status`，不映射 confirmed | 否 |
| 旧 Constitution 混入 AI 权限和方法 | 治理 | 原文归档，旧路径改兼容入口，新 Constitution 只保留 Guardrail + Router | 否 |
| AI 推断人格与 Murphy 已确认认知混同 | 道/治理 | 推断进入 INFERRED_PATTERNS，`murphy_status: unreviewed` | 否 |
| 单次 Case 生成硬规则 | 术/道 | Case 可改术和防火墙，不能直接改道 | 否 |
"""

METHOD_REGISTRY = f"""
{frontmatter("META", "method_registry", "active", "none")}

# Method Registry

| Canonical Method | 状态 | 旧来源 |
|---|---|---|
| [[02_术/TRADING_SYSTEM/00_DECISION_CONTRACT]] | active | 旧投资主框架、旧 Constitution |
| [[02_术/SKILLS/LIQUIDITY_TRANSMISSION]] | active | `03_流动性过滤器`、`260720宏观流动性过滤器` |
| [[02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK]] | active | AI 投资主线、BOTTLENECK、结构性转变框架 |
| [[02_术/SKILLS/INDUSTRY_SUPPLY_DEMAND]] | active | 泊松供需闭环、260606、挖掘端 SOP |
| [[02_术/SKILLS/COMPANY_FUNDAMENTALS]] | active | 公司研究模板、基础概念规则 |
| [[02_术/SKILLS/EXPECTATIONS_VALUATION]] | active | 三层肉、估值语法 |
| 旧 `/70` scorecard | retired | AI 周期 scorecard |
"""

ABSORPTION_TEMPLATE = f"""
{frontmatter("META", "absorption_receipt_template", "active", "none")}

# Absorption Receipt Template

```yaml
new_information:
change: strengthen | weaken | revise | overturn | none
affected_item:
result: METHOD_UPDATE | STATE_UPDATE | PHILOSOPHY_CANDIDATE | NO_INCREMENT
write_to:
source:
```

前台只显示：

- **新东西是什么：**
- **改变了什么：**
- **写到哪里：**
"""

ARCHIVE_README = f"{frontmatter('META', 'archive_index', 'active', 'none')}\n\n# Archive\n\n旧系统、AI 长报告、历史 State 和 superseded 文件保留为证据线索，统一 `decision_authority: none`。"
AUTOMATION_README = f"{frontmatter('AUTOMATION', 'automation_index', 'active', 'operational')}\n\n# Automation\n\nPrompts、脚本、测试和运行态统一在这里管理。自动化最多运行到 Philosophy Inbox，不能写 MINDSET/CONSTITUTION。"
PROMPTS_README = f"{frontmatter('AUTOMATION', 'prompts_index', 'active', 'operational')}\n\n# Prompts\n\n当前有效 prompt 在这里 canonical 化，旧 prompt 进入历史。"
RUNTIME_README = f"{frontmatter('AUTOMATION', 'runtime_index', 'active', 'none')}\n\n# Runtime\n\n运行日志、queue、last outcome 和状态快照。"
LEGACY_README = f"{frontmatter('META', 'legacy_layout_index', 'active', 'none')}\n\n# Legacy Layout\n\n旧结构先保留一个只读周期。完整迁移记录见 [[05_EVIDENCE_META/META/COVERAGE_MANIFEST]]。"

OLD_CONSTITUTION_STUB = f"""
---
title: 旧 Constitution 兼容入口
date: {DATE}
updated: {DATE}
layer: CONSTITUTION
primary_role: legacy_redirect
status: superseded
decision_authority: none
superseded_by: [[01_道/CONSTITUTION]]
source_paths:
  - [[01_道/_HISTORY/260721旧CONSTITUTION_历史原文]]
---

# 旧 Constitution 兼容入口

本文件已按 `260723系统_Murphy投资系统工程重构方案` 降为历史兼容入口，不再拥有“最高效力”。

当前个人 Constitution：[[01_道/CONSTITUTION]]

旧全文历史原文：[[01_道/_HISTORY/260721旧CONSTITUTION_历史原文]]

AI 操作权限：[[AGENTS]]

方法与执行：[[02_术/TRADING_SYSTEM/00_DECISION_CONTRACT]]
"""

OLD_MODEL_STUB = f"""
---
title: 旧当前认知模型兼容入口
date: {DATE}
updated: {DATE}
layer: META
primary_role: legacy_ai_hypothesis_redirect
status: superseded
decision_authority: none
superseded_by:
  - [[01_道/MINDSET]]
  - [[01_道/PHILOSOPHY_INBOX/INFERRED_PATTERNS]]
source_paths:
  - [[01_道/_HISTORY/260722旧MURPHY_CURRENT_COGNITIVE_MODEL_历史原文]]
---

# 旧当前认知模型兼容入口

本文件原文已归档为历史 AI 假设库，不再描述 Murphy 当前人格，不再保存 State，不再授权交易。

当前 MINDSET：[[01_道/MINDSET]]

AI 推断模式：[[01_道/PHILOSOPHY_INBOX/INFERRED_PATTERNS]]

旧全文历史原文：[[01_道/_HISTORY/260722旧MURPHY_CURRENT_COGNITIVE_MODEL_历史原文]]
"""

OLD_CLAIM_LEDGER_STUB = f"""
---
title: 旧认知命题证据账本兼容入口
date: {DATE}
updated: {DATE}
layer: META
primary_role: legacy_claim_ledger_redirect
status: superseded
decision_authority: none
superseded_by: [[05_EVIDENCE_META/META/CLAIM_LEDGER]]
source_paths:
  - [[01_道/_HISTORY/260722旧认知命题证据账本_历史原文]]
---

# 旧认知命题证据账本兼容入口

旧账本中的“已吸收、高、采纳”等标签只作为 `legacy_status`，不得自动映射为 `murphy_status: confirmed`。

新 Claim Ledger：[[05_EVIDENCE_META/META/CLAIM_LEDGER]]

旧全文历史原文：[[01_道/_HISTORY/260722旧认知命题证据账本_历史原文]]
"""

OLD_COVERAGE_STUB = f"""
---
title: 旧全库覆盖清单兼容入口
date: {DATE}
updated: {DATE}
layer: META
primary_role: legacy_coverage_redirect
status: superseded
decision_authority: none
superseded_by: [[05_EVIDENCE_META/META/COVERAGE_MANIFEST]]
---

# 旧全库覆盖清单兼容入口

旧覆盖清单是某一时点的 State，已经过期。当前覆盖与迁移记录见 [[05_EVIDENCE_META/META/COVERAGE_MANIFEST]]。
"""

OLD_RULES_STUB = f"""
---
title: 旧规则溯源与冲突裁决表兼容入口
date: {DATE}
updated: {DATE}
layer: META
primary_role: legacy_rules_redirect
status: superseded
decision_authority: none
superseded_by: [[05_EVIDENCE_META/META/CONFLICT_REGISTER]]
source_paths:
  - [[01_道/_HISTORY/旧规则溯源与冲突裁决表_历史原文]]
---

# 旧规则溯源与冲突裁决表兼容入口

旧表中的“采纳、覆盖、最高效力、已吸收”等表达只保留为历史 AI 判断，不再提供当前裁决权限。

当前冲突登记：[[05_EVIDENCE_META/META/CONFLICT_REGISTER]]

旧全文历史原文：[[01_道/_HISTORY/旧规则溯源与冲突裁决表_历史原文]]
"""

OLD_PROVENANCE_STUB = f"""
---
title: 旧来源分级与版本记录兼容入口
date: {DATE}
updated: {DATE}
layer: META
primary_role: legacy_provenance_redirect
status: superseded
decision_authority: none
superseded_by: [[05_EVIDENCE_META/META/PROVENANCE_SCHEMA]]
source_paths:
  - [[01_道/_HISTORY/旧认知模型来源分级与版本记录_历史原文]]
---

# 旧来源分级与版本记录兼容入口

旧来源分级可以作为审计材料，但当前 frontmatter、来源身份和权限规则以新 Schema 为准。

当前来源 Schema：[[05_EVIDENCE_META/META/PROVENANCE_SCHEMA]]

旧全文历史原文：[[01_道/_HISTORY/旧认知模型来源分级与版本记录_历史原文]]
"""

OLD_DASHBOARD_STUB = f"""
---
title: 旧股票投资看板兼容入口
date: {DATE}
updated: {DATE}
layer: META
primary_role: legacy_home_redirect
status: superseded
decision_authority: none
superseded_by: [[00_HOME/HOME]]
source_paths:
  - [[99_ARCHIVE/LEGACY_LAYOUT/旧股票投资看板_历史原文]]
---

# 旧股票投资看板兼容入口

本看板已被新 HOME 取代，不再承担系统入口和权限导航。

当前 HOME：[[00_HOME/HOME]]

旧全文历史原文：[[99_ARCHIVE/LEGACY_LAYOUT/旧股票投资看板_历史原文]]
"""

EXECUTION_LOG = """
{fm}

# Phase 2 Execution Log

## 先说人话

**今天发生了什么：**第二阶段已建立新目录、前台 HOME、权限说明、Constitution、MINDSET、候选 Inbox、Trading System、Skills、State、Case、Evidence、Automation 和逐文件迁移 manifest。

**为什么重要：**系统现在先完成“减权限”：旧核心页不再因为文件名拥有最高效力，AI 推断、State、Case 和 Evidence 都有了明确边界。

**现在做什么：**使用新前台继续工作；后续再逐步把旧内容物理迁入对应 dossier 和 archive。

## 本次覆盖

- 旧结构扫描文件数：`{file_count}`
- Markdown 数：`{md_count}`
- 完整 manifest：[[05_EVIDENCE_META/META/COVERAGE_MANIFEST]]
- CSV：[[05_EVIDENCE_META/META/COVERAGE_MANIFEST.csv]]

## 本次已执行

- 新建第 5 章建议的目录骨架。
- 新建 HOME、SYSTEM_MAP、CONTENT_ROUTER、DECISION_AUTHORITY。
- 新建 Constitution，只保留七条 Guardrail 和 Router。
- 新建 MINDSET，只保留第 7.3 节已给方向性裁决的前台原则。
- 新建 Philosophy Inbox、Decision Log 和 Inferred Patterns。
- 新建 Trading System、核心 Skills 和方法注册表。
- 新建 State、Case、Evidence、Automation 索引。
- 将旧 Constitution、旧认知模型、旧命题账本、旧来源/覆盖文件复制到 `01_道/_HISTORY/`。
- 将旧核心路径改为兼容入口，不再显示最高效力。

## 未执行或保留

- 未不可恢复删除任何唯一原始材料。
- 未物理移动全部旧文件；先由 manifest 接管权限与去向，降低链接风险。
- 未把候选命题自动晋升到 MINDSET。
- 未把具体仓位、概率、冷静期、期权参数写成 Constitution。
""".format(fm=frontmatter("META", "execution_log", "active", "none"), file_count="{file_count}", md_count="{md_count}")


if __name__ == "__main__":
    main()
