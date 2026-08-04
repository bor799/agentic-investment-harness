# Security Policy

## Credentials

This repository is publicly visible. Never commit:

- API tokens (GitHub `ghp_*`, AWS `AKIA*`, Stripe `sk_live_*`, etc.)
- Private keys (`-----BEGIN ... PRIVATE KEY-----`)
- Database connection strings with embedded passwords
- Any `.env` or secrets file

The publication auditor (`90_AUTOMATION/PIPELINES/audit_publication.py`)
scans for credential patterns before each release. If it blocks,
**do not bypass** — investigate and remove the credential.

## Reporting

If you find credentials or sensitive data in this repository,
do **not** open a public issue. Contact the repository owner directly.

## AI Agent Safety

AI agents (Claude Code, Codex, etc.) operating in this repository:

- Have **no** trading authority
- Have **no** position modification authority
- Must pass the Validator before any canonical write
- Must pass an independent Reviewer before any reviewed write
- Must default to `chat_only` (no file writes) unless explicitly authorized

The default answer to any user request is `write_intent: chat_only`.
Writing is the exception, not the rule.
