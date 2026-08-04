#!/usr/bin/env python3
"""Publication Auditor 测试。"""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

# 把 auditor 目录加入 import 路径
sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_publication import run, _sha256_file


def _write(repo, rel_path, content):
    abs_path = Path(repo) / rel_path
    abs_path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, bytes):
        abs_path.write_bytes(content)
    else:
        abs_path.write_text(content, encoding="utf-8")
    return abs_path


def _make_minimal_repo(repo):
    """创建最小合规仓库（P-2~P-6 全绿）。"""
    _write(repo, "README.md", "# Test")
    _write(repo, "AGENTS.md", "# Agents")
    _write(repo, "LICENSE", "Apache License")
    _write(repo, ".gitignore",
           ".DS_Store\n.harness_backup/\n__pycache__/\n*.pyc\n"
           "90_AUTOMATION/RUNTIME/STAGING/\n")
    files = ["README.md", "AGENTS.md", "LICENSE", ".gitignore"]
    manifest = {
        "schema_version": "1.0",
        "files": [
            {"path": p, "include": True, "rights": "own",
             "reason": "test", "sha256": _sha256_file(Path(repo) / p)}
            for p in files
        ],
    }
    _write(repo, "PUBLICATION_MANIFEST.json",
           json.dumps(manifest, ensure_ascii=False, indent=2))


class TestP1CredentialScan(unittest.TestCase):
    """P-1 凭证泄漏检测。"""

    def test_pass_clean_repo(self):
        with tempfile.TemporaryDirectory() as repo:
            _make_minimal_repo(repo)
            report = run(repo)
            p1 = [c for c in report["checks"] if c["code"] == "P-1"][0]
            self.assertEqual(p1["status"], "OK")

    def test_fail_github_token(self):
        with tempfile.TemporaryDirectory() as repo:
            _make_minimal_repo(repo)
            _write(repo, "config.yml",
                   "token: ghp_1234567890abcdefghijklmnOPQRSTUVWXYZ")
            report = run(repo)
            p1 = [c for c in report["checks"] if c["code"] == "P-1"][0]
            self.assertEqual(p1["status"], "FAIL")
            self.assertIn("GitHub token", p1["evidence"]["hits"][0]["type"])

    def test_pass_masked_token_in_docs(self):
        """掩码 token（星号）不算泄漏。"""
        with tempfile.TemporaryDirectory() as repo:
            _make_minimal_repo(repo)
            _write(repo, "notes.md",
                   "Token: ghp_************************************")
            report = run(repo)
            p1 = [c for c in report["checks"] if c["code"] == "P-1"][0]
            self.assertEqual(p1["status"], "OK")

    def test_fail_aws_key(self):
        with tempfile.TemporaryDirectory() as repo:
            _make_minimal_repo(repo)
            _write(repo, "deploy.sh",
                   "export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE")
            report = run(repo)
            p1 = [c for c in report["checks"] if c["code"] == "P-1"][0]
            self.assertEqual(p1["status"], "FAIL")

    def test_fail_db_url_with_password(self):
        with tempfile.TemporaryDirectory() as repo:
            _make_minimal_repo(repo)
            _write(repo, "app.cfg",
                   "DATABASE_URL=postgresql://user:s3cr3t@dbhost:5432/mydb")
            report = run(repo)
            p1 = [c for c in report["checks"] if c["code"] == "P-1"][0]
            self.assertEqual(p1["status"], "FAIL")

    def test_pass_allowlist_security_md(self):
        """SECURITY.md 在 allowlist 中，讨论凭证模式不触发。"""
        with tempfile.TemporaryDirectory() as repo:
            _make_minimal_repo(repo)
            _write(repo, "SECURITY.md",
                   "Don't commit tokens like ghp_1234567890abcdefghijklmnOPQRSTUVWXYZ")
            report = run(repo)
            p1 = [c for c in report["checks"] if c["code"] == "P-1"][0]
            self.assertEqual(p1["status"], "OK")


class TestP2ForbiddenPaths(unittest.TestCase):

    def test_pass_clean_repo(self):
        with tempfile.TemporaryDirectory() as repo:
            _make_minimal_repo(repo)
            report = run(repo)
            p2 = [c for c in report["checks"] if c["code"] == "P-2"][0]
            self.assertEqual(p2["status"], "OK")

    def test_pass_staging_excluded(self):
        """Staging 目录被 .gitignore 排除，审计器不应扫描到其中的文件。"""
        with tempfile.TemporaryDirectory() as repo:
            _make_minimal_repo(repo)
            _write(repo, "90_AUTOMATION/RUNTIME/STAGING/test--abcdef123456.json",
                   '{"unverified": true}')
            report = run(repo)
            p2 = [c for c in report["checks"] if c["code"] == "P-2"][0]
            self.assertEqual(p2["status"], "OK")


class TestP3FileSize(unittest.TestCase):

    def test_pass_small_files(self):
        with tempfile.TemporaryDirectory() as repo:
            _make_minimal_repo(repo)
            report = run(repo)
            p3 = [c for c in report["checks"] if c["code"] == "P-3"][0]
            self.assertEqual(p3["status"], "OK")

    def test_fail_oversized(self):
        with tempfile.TemporaryDirectory() as repo:
            _make_minimal_repo(repo)
            _write(repo, "big.bin", b"\x00" * (101 * 1024 * 1024))
            report = run(repo)
            p3 = [c for c in report["checks"] if c["code"] == "P-3"][0]
            self.assertEqual(p3["status"], "FAIL")


class TestP4Manifest(unittest.TestCase):

    def test_pass_complete_manifest(self):
        with tempfile.TemporaryDirectory() as repo:
            _make_minimal_repo(repo)
            report = run(repo)
            p4 = [c for c in report["checks"] if c["code"] == "P-4"][0]
            self.assertEqual(p4["status"], "OK")

    def test_fail_missing_manifest(self):
        with tempfile.TemporaryDirectory() as repo:
            _write(repo, "README.md", "# Test")
            report = run(repo)
            p4 = [c for c in report["checks"] if c["code"] == "P-4"][0]
            self.assertEqual(p4["status"], "FAIL")

    def test_fail_incomplete_manifest(self):
        with tempfile.TemporaryDirectory() as repo:
            _make_minimal_repo(repo)
            _write(repo, "extra.md", "not in manifest")
            report = run(repo)
            p4 = [c for c in report["checks"] if c["code"] == "P-4"][0]
            self.assertEqual(p4["status"], "FAIL")


class TestP5CriticalEntries(unittest.TestCase):

    def test_pass_all_present(self):
        with tempfile.TemporaryDirectory() as repo:
            _make_minimal_repo(repo)
            report = run(repo)
            p5 = [c for c in report["checks"] if c["code"] == "P-5"][0]
            self.assertEqual(p5["status"], "OK")

    def test_fail_missing_readme(self):
        with tempfile.TemporaryDirectory() as repo:
            _write(repo, "AGENTS.md", "# Agents")
            _write(repo, "LICENSE", "MIT")
            _write(repo, ".gitignore", ".DS_Store\n")
            report = run(repo)
            p5 = [c for c in report["checks"] if c["code"] == "P-5"][0]
            self.assertEqual(p5["status"], "FAIL")


class TestP6Gitignore(unittest.TestCase):

    def test_pass_complete_gitignore(self):
        with tempfile.TemporaryDirectory() as repo:
            _make_minimal_repo(repo)
            report = run(repo)
            p6 = [c for c in report["checks"] if c["code"] == "P-6"][0]
            self.assertEqual(p6["status"], "OK")

    def test_fail_missing_gitignore(self):
        with tempfile.TemporaryDirectory() as repo:
            _write(repo, "README.md", "# Test")
            report = run(repo)
            p6 = [c for c in report["checks"] if c["code"] == "P-6"][0]
            self.assertEqual(p6["status"], "FAIL")

    def test_fail_partial_gitignore(self):
        with tempfile.TemporaryDirectory() as repo:
            _write(repo, "README.md", "# Test")
            _write(repo, ".gitignore", ".DS_Store\n")
            report = run(repo)
            p6 = [c for c in report["checks"] if c["code"] == "P-6"][0]
            self.assertEqual(p6["status"], "FAIL")


class TestOverallAggregation(unittest.TestCase):

    def test_overall_pass(self):
        with tempfile.TemporaryDirectory() as repo:
            _make_minimal_repo(repo)
            report = run(repo)
            self.assertEqual(report["overall"], "PASS")

    def test_overall_fail_on_credential(self):
        with tempfile.TemporaryDirectory() as repo:
            _make_minimal_repo(repo)
            _write(repo, "leak.txt",
                   "ghp_1234567890abcdefghijklmnOPQRSTUVWXYZ")
            report = run(repo)
            self.assertEqual(report["overall"], "FAIL")


if __name__ == "__main__":
    unittest.main()
