# Contributing

## AI Agent Contributions

AI agents (Claude Code, Codex, Antigravity, etc.) are welcome to contribute,
but must follow the governance flow:

1. Work on `agent/*` branches only — never commit directly to `main`
2. Open draft PRs with the PR template filled out
3. All CI checks must pass (tests + validator + publication auditor)
4. `main` is protected — no force push, no deletion
5. Only the human owner can merge

## Method Proposals

Method or rule changes (`01_道/` or `02_术/`) require the full governance cycle:

```
Proposal (in conversation) → Independent Reviewer → Validator → Human Merge
```

AI agents **cannot** directly modify canonical governance files. Use the
Method Proposal Issue template to start.

## Evidence Contributions

New sources, moments, or knowledge updates must:

1. Pass the Validator (`validate_investment_output.py`)
2. Include traceable root sources (path or URL, published date, data caliber)
3. Respect Murphy/AI boundary — AI-suggested beliefs are marked `suggestion_only`

## Test Requirements

- All existing tests must pass: `python3 -m unittest discover -s 90_AUTOMATION/TESTS -p 'test_*.py'`
- New features must include tests
- Publication-affecting changes must pass: `python3 90_AUTOMATION/PIPELINES/audit_publication.py .`

## Security

Never commit credentials, tokens, or private keys. See `SECURITY.md`.
