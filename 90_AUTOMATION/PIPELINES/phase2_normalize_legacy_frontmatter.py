from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from phase2_patch_legacy_frontmatter import DATE, PLAN, SKIP_TOP_METADATA, classify, legacy_files, quote


CORE_FIELDS = [
    "layer",
    "primary_role",
    "status",
    "authored_by",
    "source_type",
    "human_reviewed",
    "decision_authority",
    "legacy_metadata_added",
    "legacy_path",
    "migration_target",
]


def split_frontmatter(text: str) -> tuple[list[str], str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fm = text[4:end].splitlines()
    body = text[end + len("\n---") :]
    if body.startswith("\n"):
        body = body[1:]
    return fm, body


def has_key(lines: list[str], key: str) -> bool:
    prefix = key + ":"
    return any(line.startswith(prefix) for line in lines)


def value_for(key: str, path: Path, meta: dict[str, str]) -> str:
    rel = str(path.relative_to(ROOT))
    values = {
        "layer": meta["layer"],
        "primary_role": meta["primary_role"],
        "status": meta["status"],
        "authored_by": "human_ai",
        "source_type": "PX",
        "human_reviewed": "false",
        "decision_authority": meta["decision_authority"],
        "legacy_metadata_added": "normalized",
        "legacy_path": quote(rel),
        "migration_target": quote(meta["target"]),
    }
    return values[key]


def rewrite_status(lines: list[str], status: str) -> tuple[list[str], str | None, bool]:
    out: list[str] = []
    old_status: str | None = None
    replaced = False
    for line in lines:
        if line.startswith("status:") and not replaced:
            old_status = line.split(":", 1)[1].strip()
            if old_status != status:
                out.append(f"status: {status}")
                replaced = True
            else:
                out.append(line)
            continue
        out.append(line)
    return out, old_status, replaced


def normalize_file(path: Path) -> dict[str, str] | None:
    rel = str(path.relative_to(ROOT))
    if rel in SKIP_TOP_METADATA:
        return None

    text = path.read_text(encoding="utf-8", errors="replace")
    parsed = split_frontmatter(text)
    if parsed is None:
        return None

    lines, body = parsed
    meta = classify(path)
    original = list(lines)
    added: list[str] = []
    status_replaced = "false"
    legacy_status_added = "false"

    lines, old_status, replaced = rewrite_status(lines, meta["status"])
    if replaced:
        status_replaced = "true"
        if old_status and not has_key(lines, "legacy_status"):
            insert_at = next((i + 1 for i, line in enumerate(lines) if line.startswith("status:")), len(lines))
            lines.insert(insert_at, f"legacy_status: {quote(old_status)}")
            legacy_status_added = "true"

    for key in CORE_FIELDS:
        if not has_key(lines, key):
            lines.append(f"{key}: {value_for(key, path, meta)}")
            added.append(key)

    if not has_key(lines, "source_paths"):
        lines.extend(["source_paths:", f"  - {PLAN}"])
        added.append("source_paths")

    if lines == original:
        return None

    new_text = "---\n" + "\n".join(lines) + "\n---\n\n" + body
    path.write_text(new_text, encoding="utf-8")
    return {
        "path": rel,
        "layer": meta["layer"],
        "primary_role": meta["primary_role"],
        "status": meta["status"],
        "decision_authority": meta["decision_authority"],
        "fields_added": ";".join(added),
        "status_replaced": status_replaced,
        "legacy_status_added": legacy_status_added,
    }


def audit(files: list[Path]) -> dict[str, int]:
    required = ["layer", "primary_role", "status", "decision_authority"]
    counts = {f"missing_{key}": 0 for key in required}
    counts["total"] = len(files)
    counts["frontmatter"] = 0
    for path in files:
        rel = str(path.relative_to(ROOT))
        if rel in SKIP_TOP_METADATA:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        parsed = split_frontmatter(text)
        if parsed is None:
            for key in required:
                counts[f"missing_{key}"] += 1
            continue
        counts["frontmatter"] += 1
        lines, _ = parsed
        for key in required:
            if not has_key(lines, key):
                counts[f"missing_{key}"] += 1
    return counts


def main() -> None:
    files = legacy_files()
    normalized = []
    for path in files:
        row = normalize_file(path)
        if row:
            normalized.append(row)

    report_dir = ROOT / "05_EVIDENCE_META/META"
    report_dir.mkdir(parents=True, exist_ok=True)
    csv_path = report_dir / "LEGACY_FRONTMATTER_NORMALIZATION_REPORT.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "path",
                "layer",
                "primary_role",
                "status",
                "decision_authority",
                "fields_added",
                "status_replaced",
                "legacy_status_added",
            ],
        )
        writer.writeheader()
        writer.writerows(normalized)

    counts = audit(files)
    report = f"""---
title: legacy_frontmatter_normalization_report
date: {DATE}
updated: {DATE}
layer: META
primary_role: legacy_frontmatter_normalization_report
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - {PLAN}
---

# Legacy Frontmatter Normalization Report

## 先说人话

**今天发生了什么：**已有 YAML frontmatter 的旧文件已补齐 `layer / primary_role / decision_authority` 等权限字段；旧 `status` 如与迁移权限冲突，已写入 `legacy_status` 保留原语义。

**为什么重要：**旧研究报告、旧观察状态和旧方法草稿仍可作为证据、案例或历史来源被检索，但不会因为原来的 `status` 或标题误拿当前决策权限。

**现在做什么：**继续按新前台工作；需要引用旧材料时，优先通过新索引、dossier、Case Gym 或吸收回执进入，而不是直接把旧文件当当前系统。

## 结果

| 指标 | 数量 |
|---|---:|
| 旧结构 Markdown | {counts['total']} |
| 有 frontmatter（不含特殊跳过） | {counts['frontmatter']} |
| 本次规范化文件 | {len(normalized)} |
| 缺 `layer` | {counts['missing_layer']} |
| 缺 `primary_role` | {counts['missing_primary_role']} |
| 缺 `status` | {counts['missing_status']} |
| 缺 `decision_authority` | {counts['missing_decision_authority']} |

CSV 明细：[[05_EVIDENCE_META/META/LEGACY_FRONTMATTER_NORMALIZATION_REPORT.csv]]

## 特殊说明

- `AGENTS.md` 仍作为 Codex 操作规则文件保留原样，不在顶部加入 YAML。
- 本脚本不移动、不删除旧正文；它只补权限 metadata 与迁移目标。
- `legacy_status` 是旧文件自己的历史状态，不再授权当前交易动作。
"""
    (report_dir / "LEGACY_FRONTMATTER_NORMALIZATION_REPORT.md").write_text(report, encoding="utf-8")


if __name__ == "__main__":
    main()
