---
title: "CLAUDE_CODE_RUN_COMMAND_INDUSTRY_BOTTLENECK_DISCOVERY"
date: 2026-07-24
updated: 2026-07-24
layer: AUTOMATION
primary_role: legacy_prompt_or_command
status: superseded
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: operational
legacy_metadata_added: true
legacy_path: "AI周期探索/0_总览/CLAUDE_CODE_RUN_COMMAND_INDUSTRY_BOTTLENECK_DISCOVERY.md"
migration_target: "90_AUTOMATION/PROMPTS"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# INDUSTRY_BOTTLENECK_DISCOVERY_LOOP 启动命令

用途：把文章、研报、政策、产业现象和用户口述判断当作训练样本，持续优化 Murphy 的科技产业投资框架。这个循环不默认写长篇行业报告，而是产出框架差分、可泛化判别式、失败条件和下一轮训练样本。

## 新对话目标

```text
/goal 持续优化 Murphy 的科技产业投资框架：把用户提供的文章、研报、政策、产业现象和口述判断当作训练样本，通过循环方式抽象出“宏观需求 -> 工程参数 -> 产业链传导 -> 供给瓶颈 -> 控制定价权 -> 财务兑现”的可泛化判别式，并持续更新 /Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索/0_总览/BOTTLENECK_3X_FRAMEWORK.md、结构性转变判断框架.md、AI投资主线.md、01_赛道研究/B_AI基础设施瓶颈.md 或 FRAMEWORK_TRAINING_LOG.md。不要默认写长篇行业报告；优先输出框架差分、判别式、失败条件和下一轮训练样本。
```

## 新对话首条消息

```text
读取 /Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索/0_总览/LOOP_PROMPT_INDUSTRY_BOTTLENECK_DISCOVERY.md。你是 INDUSTRY_BOTTLENECK_DISCOVERY_LOOP。接下来我给你的每篇文章、研报、政策、产业现象或口述判断，都不是让你写普通分析报告，而是让你训练并优化我的投资框架。每轮必须抽象出可泛化判别式，做传导链拆解、反简单叙事测试、七步瓶颈测试和贝叶斯更新，并把框架差分写入本地库。默认不要输出买卖建议，不要直接把标的塞进三倍候选；新标的只进入候选问题或后续公司级研究队列。
```

## 循环运行命令

```text
/ralph-loop "读取 /Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/AI周期探索/0_总览/LOOP_PROMPT_INDUSTRY_BOTTLENECK_DISCOVERY.md。你是 INDUSTRY_BOTTLENECK_DISCOVERY_LOOP。每轮只处理一个训练样本：先读旧框架，再读样本，抽象出传导链、反简单叙事测试、七步瓶颈测试、贝叶斯更新和新判别式；默认不写长篇行业报告，只写框架差分；每轮必须更新 BOTTLENECK_3X_FRAMEWORK.md、结构性转变判断框架.md、B_AI基础设施瓶颈.md 或 FRAMEWORK_TRAINING_LOG.md；完成所有训练样本后输出 <promise>INDUSTRY_BOTTLENECK_DISCOVERY_COMPLETE</promise>。" --max-iterations 80 --completion-promise "INDUSTRY_BOTTLENECK_DISCOVERY_COMPLETE"
```

## 完成条件

每轮必须满足：

1. 读取训练样本和相关旧框架。
2. 拆出事实、推论、预测、投资含义。
3. 完成传导链拆解。
4. 完成反简单叙事测试。
5. 通过七步瓶颈测试。
6. 完成贝叶斯更新表。
7. 产出至少一条可泛化判别式。
8. 写入框架文件或 `FRAMEWORK_TRAINING_LOG.md`。
9. 给出下一轮训练队列或验证信号。
