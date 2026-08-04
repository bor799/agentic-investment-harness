# Roadmap

## v0.1.0 — Public Harness Skeleton (current)

- Evidence → Knowledge → State → Decision → Case → Method Evolution pipeline
- 42-check Validator (fail-closed write gating)
- Independent Reviewer protocol (read-only, tool-restricted)
- 169 regression tests
- Publication auditor (credential scan, path audit, manifest completeness)
- Governance migration contract mechanism (frozen SHA256, per-file authorization)
- Human-authority-first boundary: AI cannot trade, modify positions, or bypass review

## v0.2 — Micro Trading System

Build the missing execution layer between State and Decision:

```
赚什么钱 → 市场结构 → 进入条件 → 持有期管理 → 证伪/风险/时间/收益退出 → Case
```

### Principles (frozen before implementation)

- 上升、震荡、下降只是执行环境，**不自动授权买入**。
- 趋势只能更新赔率（H_R）、周期（H_L）和进入时点，**不能替代经营证据（H_B）**。
- 每份计划必须有：可执行价格、期限、期望净收益、最大损失、四类退出条件。
- 未校准计划只允许 shadow test，**不产生资本授权**。
- 完成真实交易后才能进入 Trade Log；未触发计划进入 Method Tests。

## v0.3 — Method Pattern Library

- Qualified patterns extracted from settled cases (dual-root, dual-reuse, explicit causal/falsifier)
- Pattern recognition cues for new target screening
- Counterpattern library for adversarial review

## v0.4 — Domain Model Federation

- Cross-domain structural prior reuse
- Domain failure library consolidation
- Investment map versioning and expiry tracking at scale

---

**This roadmap records direction, not promises.** Each version lands only after
passing the full governance cycle: proposal → independent review → CI/Validator →
human merge.
