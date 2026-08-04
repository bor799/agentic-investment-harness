---
title: ai_belief_loop_run_log
date: 2026-07-28
layer: AUTOMATION
primary_role: sanitized_run_log
status: active
decision_authority: none
---

# AI Belief Loop Run Log

运行日志只保存：

- `schema_version`
- `runner_version`
- `created_at`
- `input_sha256`
- `mode`
- `result`
- `created_paths`
- `error_code`

禁止保存输入原文、excerpt、凭证、环境变量和原始异常文本。日志不提供研究
或资本授权。
