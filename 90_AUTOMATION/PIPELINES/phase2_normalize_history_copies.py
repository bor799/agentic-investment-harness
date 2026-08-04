from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATE = "2026-07-24"
PLAN = "分析报告/archive/260723系统_Murphy投资系统工程重构方案.md"

HISTORY_FILES = [
    "01_道/_HISTORY/260721旧CONSTITUTION_历史原文.md",
    "01_道/_HISTORY/260722旧MURPHY_CURRENT_COGNITIVE_MODEL_历史原文.md",
    "01_道/_HISTORY/260722旧认知命题证据账本_历史原文.md",
    "01_道/_HISTORY/旧全库投资资料覆盖清单_历史原文.md",
    "01_道/_HISTORY/旧规则溯源与冲突裁决表_历史原文.md",
    "01_道/_HISTORY/旧认知模型来源分级与版本记录_历史原文.md",
    "99_ARCHIVE/LEGACY_LAYOUT/旧股票投资看板_历史原文.md",
]

REQUIRED = {
    "layer": "META",
    "primary_role": "historical_source_copy",
    "status": "archived",
    "authored_by": "human_ai",
    "source_type": "PX",
    "human_reviewed": "false",
    "decision_authority": "none",
    "history_copy_metadata_added": "true",
}


def quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


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
    return any(line.startswith(key + ":") for line in lines)


def patch(path: Path) -> bool:
    rel = str(path.relative_to(ROOT))
    text = path.read_text(encoding="utf-8", errors="replace")
    parsed = split_frontmatter(text)
    if parsed is None:
        lines = [
            f"title: {quote(path.stem)}",
            f"date: {DATE}",
            f"updated: {DATE}",
        ]
        body = text
    else:
        lines, body = parsed
    original = list(lines)
    for key, value in REQUIRED.items():
        if not has_key(lines, key):
            lines.append(f"{key}: {value}")
    if not has_key(lines, "history_copy_path"):
        lines.append(f"history_copy_path: {quote(rel)}")
    if not has_key(lines, "source_paths"):
        lines.extend(["source_paths:", f"  - {PLAN}"])
    if lines == original and parsed is not None:
        return False
    path.write_text("---\n" + "\n".join(lines) + "\n---\n\n" + body, encoding="utf-8")
    return True


def main() -> None:
    changed = []
    for rel in HISTORY_FILES:
        path = ROOT / rel
        if path.exists() and patch(path):
            changed.append(rel)

    report = ROOT / "05_EVIDENCE_META/META/HISTORY_COPY_FRONTMATTER_REPORT.md"
    rows = "\n".join(f"| `{rel}` | normalized |" for rel in changed)
    report.write_text(
        f"""---
title: history_copy_frontmatter_report
date: {DATE}
updated: {DATE}
layer: META
primary_role: history_copy_frontmatter_report
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - {PLAN}
---

# History Copy Frontmatter Report

## 先说人话

**今天发生了什么：**`01_道/_HISTORY` 与 `99_ARCHIVE/LEGACY_LAYOUT` 的历史原文副本已补齐降权 metadata。

**为什么重要：**历史副本里可能保留“最高效力”“采纳”等旧语义；frontmatter 明确它们现在只是历史来源，不拥有当前决策权限。

**现在做什么：**需要引用历史原文时可以查这里，但不能把历史副本当当前 Constitution、MINDSET 或交易授权。

| 文件 | 动作 |
|---|---|
{rows}
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
