#!/usr/bin/env python3
"""
Publication Auditor for Agentic Investment Harness.

公开发布前的安全扫描。fail-closed，不判断投资内容。

校验项 P-1 ~ P-7：
- P-1  凭证泄漏（token / 私钥 / API key）
- P-2  禁止路径被跟踪（.harness_backup / __pycache__ / Staging）
- P-3  文件大小超过 GitHub 限制（100 MB 硬限 / 50 MB 警告）
- P-4  PUBLICATION_MANIFEST.json 缺失或不完整
- P-5  关键入口文件缺失（README / AGENTS / LICENSE）
- P-6  .gitignore 缺少必需排除项
- P-7  清单中声明 exclude 的文件实际出现在仓库中

只使用 Python 标准库，不联网。

输入：仓库根目录（argv[1]，默认当前目录）
输出：JSON 校验报告 + 人类可读摘要
"""

import hashlib
import json
import os
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# 路径排除规则（这些路径不会被扫描，也不应该出现在发布仓库中）
# ---------------------------------------------------------------------------

EXCLUDED_DIR_PREFIXES = (
    ".git/",
    ".harness_backup/",
    "__pycache__/",
    "90_AUTOMATION/RUNTIME/STAGING/",
)

EXCLUDED_FILE_NAMES = {
    ".DS_Store",
    "settings.local.json",
}

EXCLUDED_SUFFIXES = (
    ".pyc",
    ".pyo",
    ".swp",
    "~",
)

# 如果这些路径被 git 跟踪（即会发布），P-2 直接 FAIL
FORBIDDEN_TRACKED_PATTERNS = [
    re.compile(r"^\.DS_Store$"),
    re.compile(r"^\.harness_backup/"),
    re.compile(r"__pycache__/"),
    re.compile(r"\.pyc$"),
    re.compile(r"^90_AUTOMATION/RUNTIME/STAGING/"),
]

# ---------------------------------------------------------------------------
# 凭证模式（匹配真实 token，不匹配文档描述）
# ---------------------------------------------------------------------------

CREDENTIAL_PATTERNS = [
    (
        re.compile(r"gh[pousr]_[A-Za-z0-9]{36,255}", re.UNICODE),
        "GitHub token",
    ),
    (
        re.compile(
            r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----"
            r"\s*\n[A-M][A-Za-z0-9+/=\n]{20,}",
        ),
        "Private key block",
    ),
    (
        re.compile(r"AKIA[0-9A-Z]{16}"),
        "AWS access key ID",
    ),
    (
        re.compile(
            r'aws_secret_access_key\s*[=:]\s*["\'][A-Za-z0-9/+=]{40}["\']'
        ),
        "AWS secret key assignment",
    ),
    (
        re.compile(r"xox[bp]-[A-Za-z0-9-]{20,}"),
        "Slack token",
    ),
    (
        re.compile(r"AIza[0-9A-Za-z_-]{35}"),
        "Google API key",
    ),
    (
        re.compile(r"sk_live_[A-Za-z0-9]{24,}"),
        "Stripe secret key",
    ),
    (
        re.compile(
            r"(?:mongodb(?:\+srv)?|postgres(?:ql)?|redis)://"
            r"[^:/\s]+:[^@/\s]+@"
        ),
        "Database URL with embedded credentials",
    ),
]

# 允许讨论凭证模式的文件（这些文件 mention 凭证但不存储真实凭证）
CREDENTIAL_SCAN_ALLOWLIST = {
    "SECURITY.md",
    "90_AUTOMATION/PIPELINES/audit_publication.py",
    "90_AUTOMATION/TESTS/test_audit_publication.py",
}

# ---------------------------------------------------------------------------
# 文件大小限制
# ---------------------------------------------------------------------------

FILE_SIZE_WARN = 50 * 1024 * 1024   # 50 MB — GitHub warns
FILE_SIZE_HARD = 100 * 1024 * 1024  # 100 MB — GitHub rejects push

# ---------------------------------------------------------------------------
# 关键入口文件（必须存在）
# ---------------------------------------------------------------------------

CRITICAL_ENTRIES = [
    "README.md",
    "AGENTS.md",
    "LICENSE",
]

# ---------------------------------------------------------------------------
# .gitignore 必须包含的排除项
# ---------------------------------------------------------------------------

REQUIRED_GITIGNORE_ENTRIES = [
    ".DS_Store",
    ".harness_backup/",
    "__pycache__/",
    "*.pyc",
    "90_AUTOMATION/RUNTIME/STAGING/",
]

# ---------------------------------------------------------------------------
# 辅助函数
# ---------------------------------------------------------------------------


def _ok(code, message, evidence=None):
    return {"code": code, "status": "OK", "message": message,
            "evidence": evidence or {}}


def _warn(code, message, evidence=None):
    return {"code": code, "status": "WARN", "message": message,
            "evidence": evidence or {}}


def _fail(code, message, evidence=None):
    return {"code": code, "status": "FAIL", "message": message,
            "evidence": evidence or {}}


def _is_excluded(rel_path):
    """路径是否被排除（不扫描、不发布）。"""
    if os.path.basename(rel_path) in EXCLUDED_FILE_NAMES:
        return True
    for suffix in EXCLUDED_SUFFIXES:
        if rel_path.endswith(suffix):
            return True
    for prefix in EXCLUDED_DIR_PREFIXES:
        if rel_path.startswith(prefix):
            return True
    return False


def _walk_repo(repo_root):
    """遍历仓库，yield (rel_path, abs_path) 用于所有非排除文件。"""
    repo_root = Path(repo_root).resolve()
    for dirpath, dirnames, filenames in os.walk(repo_root):
        # 原地修改 dirnames 以阻止递归进入排除目录
        dirnames[:] = [
            d for d in dirnames
            if not _is_excluded(
                str((Path(dirpath) / d).relative_to(repo_root)) + "/"
            )
        ]
        for filename in filenames:
            abs_path = Path(dirpath) / filename
            rel_path = str(abs_path.relative_to(repo_root))
            if _is_excluded(rel_path):
                continue
            yield rel_path, abs_path


def _sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _is_text_file(path, sample_size=8192):
    """粗略判断是否为文本文件（用于凭证扫描）。"""
    try:
        with open(path, "rb") as f:
            sample = f.read(sample_size)
        if b"\x00" in sample:
            return False
        return True
    except (OSError, IOError):
        return False


# ---------------------------------------------------------------------------
# 校验函数
# ---------------------------------------------------------------------------


def p1_credential_scan(repo_root, tracked_files):
    """P-1 凭证泄漏扫描。"""
    hits = []
    for rel_path, abs_path in tracked_files:
        if rel_path in CREDENTIAL_SCAN_ALLOWLIST:
            continue
        if not _is_text_file(abs_path):
            continue
        try:
            with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except (OSError, IOError):
            continue
        for pattern, label in CREDENTIAL_PATTERNS:
            match = pattern.search(content)
            if match:
                # 只截取匹配文本的前 12 字符做证据（不暴露完整凭证）
                preview = match.group(0)[:12] + "..."
                hits.append({
                    "file": rel_path,
                    "type": label,
                    "preview": preview,
                })
    if hits:
        return _fail(
            "P-1",
            f"发现 {len(hits)} 处疑似凭证泄漏",
            {"hits": hits[:20]},
        )
    return _ok("P-1", "未发现凭证泄漏")


def p2_forbidden_paths(repo_root, tracked_files):
    """P-2 禁止路径不应被跟踪。"""
    forbidden = []
    for rel_path, _ in tracked_files:
        for pattern in FORBIDDEN_TRACKED_PATTERNS:
            if pattern.search(rel_path):
                forbidden.append(rel_path)
                break
    if forbidden:
        return _fail(
            "P-2",
            f"禁止路径被跟踪：{len(forbidden)} 个文件",
            {"forbidden": forbidden[:20]},
        )
    return _ok("P-2", "无禁止路径")


def p3_file_size(repo_root, tracked_files):
    """P-3 文件大小限制。"""
    oversized = []
    warnings = []
    for rel_path, abs_path in tracked_files:
        try:
            size = abs_path.stat().st_size
        except (OSError, IOError):
            continue
        if size >= FILE_SIZE_HARD:
            oversized.append({"file": rel_path, "size_mb": round(size / 1048576, 1)})
        elif size >= FILE_SIZE_WARN:
            warnings.append({"file": rel_path, "size_mb": round(size / 1048576, 1)})
    if oversized:
        return _fail(
            "P-3",
            f"{len(oversized)} 个文件超过 GitHub 100 MB 硬限",
            {"oversized": oversized, "warnings": warnings},
        )
    if warnings:
        return _warn(
            "P-3",
            f"{len(warnings)} 个文件超过 50 MB 警告线",
            {"warnings": warnings},
        )
    return _ok("P-3", "文件大小合规")


def p4_manifest_completeness(repo_root, tracked_files):
    """P-4 PUBLICATION_MANIFEST.json 存在且覆盖所有跟踪文件。"""
    manifest_path = Path(repo_root) / "PUBLICATION_MANIFEST.json"
    if not manifest_path.exists():
        return _fail("P-4", "PUBLICATION_MANIFEST.json 不存在")
    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        return _fail("P-4", f"manifest 解析失败：{e}")

    manifest_files = {
        entry["path"] for entry in manifest.get("files", [])
        if entry.get("include", True)
    }
    actual_files = {rel_path for rel_path, _ in tracked_files}

    missing_from_manifest = actual_files - manifest_files - {"PUBLICATION_MANIFEST.json"}
    missing_from_repo = manifest_files - actual_files

    problems = []
    if missing_from_manifest:
        problems.append(
            f"仓库中有 {len(missing_from_manifest)} 个文件未登记在 manifest"
        )
    if missing_from_repo:
        problems.append(
            f"manifest 声明了 {len(missing_from_repo)} 个不存在的文件"
        )
    if problems:
        return _fail(
            "P-4",
            "；".join(problems),
            {
                "missing_from_manifest": sorted(missing_from_manifest)[:20],
                "missing_from_repo": sorted(missing_from_repo)[:20],
            },
        )
    return _ok("P-4", f"manifest 完整（{len(manifest_files)} 个文件）")


def p5_critical_entries(repo_root, tracked_files):
    """P-5 关键入口文件必须存在。"""
    tracked_set = {rel_path for rel_path, _ in tracked_files}
    missing = [e for e in CRITICAL_ENTRIES if e not in tracked_set]
    if missing:
        return _fail(
            "P-5",
            f"关键入口文件缺失：{missing}",
        )
    return _ok("P-5", "关键入口文件齐全")


def p6_gitignore(repo_root, tracked_files):
    """P-6 .gitignore 必须包含必需排除项。"""
    gitignore_path = Path(repo_root) / ".gitignore"
    if not gitignore_path.exists():
        return _fail("P-6", ".gitignore 不存在")
    try:
        with open(gitignore_path, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, IOError):
        return _fail("P-6", ".gitignore 读取失败")
    missing = [
        entry for entry in REQUIRED_GITIGNORE_ENTRIES
        if entry not in content
    ]
    if missing:
        return _fail(
            "P-6",
            f".gitignore 缺少必需排除项：{missing}",
        )
    return _ok("P-6", ".gitignore 包含所有必需排除项")


def p7_excluded_files_present(repo_root, tracked_files):
    """P-7 manifest 中声明 exclude 的文件不应出现在跟踪文件中。"""
    manifest_path = Path(repo_root) / "PUBLICATION_MANIFEST.json"
    if not manifest_path.exists():
        return _ok("P-7", "无 manifest，跳过")
    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
    except (OSError, json.JSONDecodeError):
        return _ok("P-7", "manifest 不可读，跳过")

    excludedDeclared = {
        entry["path"] for entry in manifest.get("files", [])
        if not entry.get("include", True)
    }
    tracked_set = {rel_path for rel_path, _ in tracked_files}
    leaked = excludedDeclared & tracked_set
    if leaked:
        return _fail(
            "P-7",
            f"声明 exclude 的文件仍被跟踪：{sorted(leaked)[:10]}",
            {"leaked": sorted(leaked)[:20]},
        )
    return _ok("P-7", "声明 exclude 的文件未被跟踪")


# ---------------------------------------------------------------------------
# 主入口
# ---------------------------------------------------------------------------

CHECKS = [
    ("P-1", p1_credential_scan),
    ("P-2", p2_forbidden_paths),
    ("P-3", p3_file_size),
    ("P-4", p4_manifest_completeness),
    ("P-5", p5_critical_entries),
    ("P-6", p6_gitignore),
    ("P-7", p7_excluded_files_present),
]


def run(repo_root):
    repo_root = Path(repo_root).resolve()
    tracked_files = list(_walk_repo(repo_root))

    results = []
    for code, fn in CHECKS:
        try:
            r = fn(repo_root, tracked_files)
        except Exception as e:
            r = _fail(code, f"auditor 异常：{type(e).__name__}: {e}")
        results.append(r)

    has_fail = any(r["status"] == "FAIL" for r in results)
    overall = "FAIL" if has_fail else "PASS"
    return {"overall": overall, "checks": results,
            "files_scanned": len(tracked_files)}


def main(argv):
    repo_root = argv[1] if len(argv) >= 2 else "."
    report = run(repo_root)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["overall"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
