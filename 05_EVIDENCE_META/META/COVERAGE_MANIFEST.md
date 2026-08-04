---
title: coverage_manifest
date: 2026-07-23
updated: 2026-07-23
layer: META
primary_role: coverage_manifest
status: active
authored_by: human_ai
source_type: P0
human_reviewed: true
decision_authority: none
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---

# 全库迁移 Manifest

## 先说人话

**今天发生了什么：**第二阶段建立了逐文件迁移记录。当前本地旧结构扫描到 `633` 个文件，其中 `612` 个 Markdown。

**为什么重要：**每个旧文件都有去向，旧内容不会因为不在前台就消失，也不会因为还能被搜索到就继续拥有决策权限。

**现在做什么：**前台先使用 `00_HOME/HOME.md`、`01_道/CONSTITUTION.md`、`01_道/MINDSET.md` 和 `02_术/`。旧路径只作为来源、历史、State 或 Evidence 使用，不能越级授权交易或哲学。

CSV 版本：[[05_EVIDENCE_META/META/COVERAGE_MANIFEST.csv]]

| 旧路径 | 动作 | 目标层 | 建议去向 | 迁移后权限 |
|---|---|---|---|---|
| `.claude/agents/ai-cycle-cross-market-v2.md` | `K+M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `.claude/commands/ai-cycle-cross-market-v2.md` | `K+M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `.claude/commands/ai-research-loop-pro.md` | `A` | `AUTOMATION` | `90_AUTOMATION/PROMPTS or 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `none` |
| `AGENTS.md` | `K+M` | `AUTOMATION` | `AGENTS.md + 00_HOME/DECISION_AUTHORITY.md` | `operational` |
| `AI周期探索/.DS_Store` | `X?` | `SYSTEM` | `99_ARCHIVE/LEGACY_LAYOUT or delete after review` | `none` |
| `AI周期探索/01_赛道研究/A_AI企业效率与上下文入口.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/THEMES + 03_STATE` | `none` |
| `AI周期探索/01_赛道研究/B_AI基础设施瓶颈.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/THEMES + 03_STATE` | `none` |
| `AI周期探索/01_赛道研究/C_高弹性期权资产.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/THEMES + 03_STATE` | `none` |
| `AI周期探索/01_赛道研究/D_中国平台与消费品牌.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/THEMES + 03_STATE` | `none` |
| `AI周期探索/01_赛道研究/E_暂不研究与降权资产.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/THEMES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/.DS_Store` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Alibaba/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Alibaba/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Alibaba/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Alibaba/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Alibaba/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Alibaba/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Atlassian/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Atlassian/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Atlassian/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Atlassian/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Atlassian/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Atlassian/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Aux Electric/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Aux Electric/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Aux Electric/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Aux Electric/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Aux Electric/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Aux Electric/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Beike/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Beike/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Beike/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Beike/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Beike/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Beike/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Berkshire Hathaway B/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Berkshire Hathaway B/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Berkshire Hathaway B/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Berkshire Hathaway B/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Berkshire Hathaway B/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Berkshire Hathaway B/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Bilibili/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Bilibili/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Bilibili/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Bilibili/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Bilibili/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Bilibili/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/BitGo Holdings/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/BitGo Holdings/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/BitGo Holdings/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/BitGo Holdings/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/BitGo Holdings/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/BitGo Holdings/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/CRRC/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/CRRC/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/CRRC/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/CRRC/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/CRRC/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/CRRC/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Circle/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Circle/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Circle/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Circle/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Circle/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Circle/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Cloudflare/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Cloudflare/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Cloudflare/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Cloudflare/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Cloudflare/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Cloudflare/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Coinbase/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Coinbase/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Coinbase/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Coinbase/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Coinbase/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Coinbase/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Corning/260701GLW_AI光互连瓶颈与价格判断.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Corning/260701GLW_AI光互连瓶颈与价格判断_AI长报告原文.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Datadog/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Datadog/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Datadog/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Datadog/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Datadog/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Datadog/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Duolingo/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Duolingo/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Duolingo/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Duolingo/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Duolingo/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Duolingo/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/ETF工具/科创50ETF/README.md` | `M` | `EVIDENCE_ROUTER` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/ETF工具/通信光互联ETF/README.md` | `M` | `EVIDENCE_ROUTER` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/ETF工具/锂电储能ETF/README.md` | `M` | `EVIDENCE_ROUTER` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Figure Technology/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Figure Technology/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Figure Technology/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Figure Technology/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Figure Technology/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Figure Technology/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Fuyao Glass/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Fuyao Glass/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Fuyao Glass/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Fuyao Glass/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Fuyao Glass/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Fuyao Glass/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/GitLab/260711GitLab_关键经营数据验证增量.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/GitLab/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/GitLab/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/GitLab/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/GitLab/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/GitLab/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/GitLab/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Google/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Google/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Google/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Google/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Google/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Google/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Hang Seng Tech Index/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Hang Seng Tech Index/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Hang Seng Tech Index/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Hang Seng Tech Index/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Hang Seng Tech Index/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Hang Seng Tech Index/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/HashKey Holdings/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/HashKey Holdings/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/HashKey Holdings/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/HashKey Holdings/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/HashKey Holdings/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/HashKey Holdings/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Horizon Robotics/260606Horizon_竞争看空与护城河验证.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Horizon Robotics/260617地平线_价格胜率与信号验证.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Horizon Robotics/260629地平线_单日大涨归因.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Horizon Robotics/260722地平线_证据状态刷新.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Horizon Robotics/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Horizon Robotics/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Horizon Robotics/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Horizon Robotics/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Horizon Robotics/next_signals.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Horizon Robotics/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Horizon Robotics/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Lemonade/260722LMND_证据状态刷新.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Lemonade/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Lemonade/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Lemonade/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Lemonade/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Lemonade/next_signals.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Lemonade/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Lemonade/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Li Auto/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Li Auto/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Li Auto/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Li Auto/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Li Auto/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Li Auto/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Lumentum/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Lumentum/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Lumentum/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Lumentum/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Lumentum/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Lumentum/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Marvell Technology/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Marvell Technology/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Marvell Technology/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Marvell Technology/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Marvell Technology/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Marvell Technology/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Meituan/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Meituan/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Meituan/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Meituan/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Meituan/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Meituan/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Meta/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Meta/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Meta/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Meta/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Meta/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Meta/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/MicroStrategy/README.md` | `M` | `EVIDENCE_ROUTER` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Micron/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Micron/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Micron/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Micron/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Micron/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Micron/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Microsoft/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Microsoft/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Microsoft/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Microsoft/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Microsoft/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Microsoft/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Miniso/20260606MINISO_财务分析.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Miniso/260722名创优品_证据状态刷新.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Miniso/MINISO_DEEP_RESEARCH.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Miniso/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Miniso/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Miniso/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Miniso/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Miniso/next_signals.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Miniso/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Miniso/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Miniso/名创优品深度分析.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/MongoDB/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/MongoDB/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/MongoDB/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/MongoDB/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/MongoDB/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/MongoDB/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Nebius/README.md` | `M` | `EVIDENCE_ROUTER` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/NuScale Power/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/NuScale Power/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/NuScale Power/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/NuScale Power/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/NuScale Power/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/NuScale Power/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Nvidia/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Nvidia/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Nvidia/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Nvidia/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Nvidia/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Nvidia/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Oracle/260701ORCL_Agent数据库逻辑与长期看涨期权策略.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Oracle/260701ORCL_Agent数据库逻辑与长期看涨期权策略_AI长报告原文.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Oracle/260722ORCL_证据状态刷新.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Oracle/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Oracle/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Oracle/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Oracle/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Oracle/next_signals.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Oracle/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Oracle/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Ouster/260629OUST_物理AI感知逻辑审计.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Ouster/260629OUST_物理AI感知逻辑审计_AI长报告原文.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Ouster/260630OUST_每日贝叶斯监控.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Ouster/260701OUST_每日贝叶斯监控.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Ouster/260702OUST_每日贝叶斯监控.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Ouster/260707OUST_每日贝叶斯监控.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Ouster/260708OUST_每日贝叶斯监控.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Ouster/260709OUST_每日贝叶斯监控.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Ouster/260711OUST_每日贝叶斯监控.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/PDD/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/PDD/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/PDD/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/PDD/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/PDD/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/PDD/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Palantir/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Palantir/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Palantir/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Palantir/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Palantir/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Palantir/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Pop Mart/260722泡泡玛特_证据状态刷新.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/Pop Mart/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Pop Mart/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Pop Mart/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Pop Mart/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Pop Mart/next_signals.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Pop Mart/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Pop Mart/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Rocket Lab/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Rocket Lab/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Rocket Lab/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Rocket Lab/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Rocket Lab/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Rocket Lab/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Salesforce/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Salesforce/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Salesforce/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Salesforce/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Salesforce/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Salesforce/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/ServiceNow/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/ServiceNow/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/ServiceNow/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/ServiceNow/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/ServiceNow/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/ServiceNow/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/TQQQ/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/TQQQ/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/TQQQ/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/TQQQ/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/TQQQ/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/TQQQ/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Tempus AI/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Tempus AI/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Tempus AI/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Tempus AI/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Tempus AI/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Tempus AI/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Tencent/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Tencent/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Tencent/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Tencent/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Tencent/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Tencent/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Tesla/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Tesla/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Tesla/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Tesla/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Tesla/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Tesla/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Vistra/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Vistra/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Vistra/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Vistra/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Vistra/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Vistra/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/Xiaomi/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/Xiaomi/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Xiaomi/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/Xiaomi/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Xiaomi/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/Xiaomi/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/亨通光电/260722亨通光电_证据状态刷新.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/亨通光电/README.md` | `M` | `EVIDENCE_ROUTER` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/亨通光电/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/亨通光电/next_signals.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/分众传媒/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/分众传媒/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/分众传媒/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/分众传媒/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/分众传媒/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/分众传媒/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/天华新能/260710天华新能_财报前经营验证基线.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/天华新能/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/天华新能/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/天华新能/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/天华新能/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/天华新能/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/天华新能/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/广合科技/260709广合科技_财报前经营验证基线.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/广合科技/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/广合科技/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/广合科技/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/广合科技/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/广合科技/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/广合科技/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/沪电股份/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/沪电股份/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/沪电股份/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/沪电股份/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/沪电股份/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/沪电股份/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/深南电路/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/深南电路/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/深南电路/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/深南电路/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/深南电路/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/深南电路/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/湖南裕能/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260616天赐材料_产业结构秩序创造机器判断.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260616天赐材料_价格信号与赚钱概率判断.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260616天赐材料_旧框架复盘与投资假设萃取.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260622天赐材料_涨跌叙事事实审计与1至3年判断.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260704天赐材料_产能重配经营验证增量.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260706天赐材料_暴跌后的买点与双层结构判断.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260706天赐材料_暴跌后的买点与双层结构判断_AI长报告原文.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260709天赐材料_6F定价权与缺货窗口校验.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260709天赐材料_储能假设交叉验证与贝叶斯交易结论.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260709天赐材料_定价权与难攻破节点判断.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260709天赐材料_挂单价格与PE安全边界.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260709天赐材料_新型储能趋势与高端材料瓶颈调研提纲.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260709天赐材料_财报穿透与公募挤兑假设校验.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260709天赐材料_雪球电解液之王逻辑链与证据更新.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260709天赐材料_雪球电解液之王逻辑链与证据更新_AI长报告原文.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260717天赐材料_资金承接与最佳赔率监控.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/260722天赐材料_证据状态刷新.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/湖南裕能/天赐材料/next_signals.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/生益电子/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/生益电子/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/生益电子/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/生益电子/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/生益电子/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/生益电子/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/紫金矿业/260722紫金矿业_证据状态刷新.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/紫金矿业/README.md` | `M` | `EVIDENCE_ROUTER` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/紫金矿业/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/紫金矿业/next_signals.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/胜宏科技/PROMPT.md` | `M` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/02_公司研究/胜宏科技/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/胜宏科技/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/胜宏科技/next_questions.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/胜宏科技/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/02_公司研究/胜宏科技/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `AI周期探索/02_公司研究/顺丰控股/260715顺丰控股_投资价值评估.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/顺丰控股/260715顺丰控股_投资价值评估_AI长报告原文.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/顺丰控股/260721顺丰控股_跨境叙事反方估值.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/顺丰控股/260722顺丰控股_证据状态刷新.md` | `D+S` | `EVIDENCE/STATE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 03_STATE` | `none` |
| `AI周期探索/02_公司研究/顺丰控股/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/02_公司研究/顺丰控股/next_signals.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/04_投资池/三倍候选池.md` | `D+M` | `STATE` | `03_STATE/WATCHLISTS` | `none` |
| `AI周期探索/04_投资池/中国消费与品牌池.md` | `D+M` | `STATE` | `03_STATE/WATCHLISTS` | `none` |
| `AI周期探索/04_投资池/暂不研究池.md` | `D+M` | `STATE` | `03_STATE/WATCHLISTS` | `none` |
| `AI周期探索/04_投资池/期权池.md` | `D+M` | `STATE` | `03_STATE/WATCHLISTS` | `none` |
| `AI周期探索/04_投资池/核心候选池.md` | `D+M` | `STATE` | `03_STATE/WATCHLISTS` | `none` |
| `AI周期探索/04_投资池/瓶颈观察池.md` | `D+M` | `STATE` | `03_STATE/WATCHLISTS` | `none` |
| `AI周期探索/04_投资池/观察池.md` | `D+M` | `STATE` | `03_STATE/WATCHLISTS` | `none` |
| `AI周期探索/04_投资池/证据不足池.md` | `D+M` | `STATE` | `03_STATE/WATCHLISTS` | `none` |
| `AI周期探索/0_总览/AI投资主线.md` | `M` | `METHOD` | `02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK.md` | `operational` |
| `AI周期探索/0_总览/BOTTLENECK_3X_FRAMEWORK.md` | `M` | `METHOD` | `02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK.md` | `operational` |
| `AI周期探索/0_总览/CLAUDE_CODE_RUN_COMMAND.md` | `M+A` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/0_总览/CLAUDE_CODE_RUN_COMMAND_CN_REFRESH.md` | `M+A` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/0_总览/CLAUDE_CODE_RUN_COMMAND_COMPANY_DISCOVERY_PRO.md` | `M+A` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/0_总览/CLAUDE_CODE_RUN_COMMAND_ENGINEER_SIGNAL_3X.md` | `M+A` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/0_总览/CLAUDE_CODE_RUN_COMMAND_INDUSTRY_BOTTLENECK_DISCOVERY.md` | `M+A` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/0_总览/CLAUDE_CODE_RUN_COMMAND_PRO.md` | `M+A` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/0_总览/CROSS_MARKET_V2_RUN_BOUNDARIES.md` | `D+A` | `STATE/METHOD/AUTOMATION` | `03_STATE or 90_AUTOMATION` | `none` |
| `AI周期探索/0_总览/ENGINEER_SIGNAL_3X_RADAR.md` | `D+A` | `STATE/METHOD/AUTOMATION` | `03_STATE or 90_AUTOMATION` | `none` |
| `AI周期探索/0_总览/FRAMEWORK_TRAINING_LOG.md` | `D+A` | `STATE/METHOD/AUTOMATION` | `03_STATE or 90_AUTOMATION` | `none` |
| `AI周期探索/0_总览/LOOP_PROMPT.md` | `M+A` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/0_总览/LOOP_PROMPT_CN_CONSUMER_REFRESH.md` | `M+A` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/0_总览/LOOP_PROMPT_COMPANY_DISCOVERY_PRO.md` | `M+A` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/0_总览/LOOP_PROMPT_CROSS_MARKET_V2.md` | `M+A` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/0_总览/LOOP_PROMPT_ENGINEER_SIGNAL_3X.md` | `M+A` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/0_总览/LOOP_PROMPT_INDUSTRY_BOTTLENECK_DISCOVERY.md` | `M+A` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/0_总览/LOOP_PROMPT_PRO.md` | `M+A` | `AUTOMATION` | `90_AUTOMATION/PROMPTS` | `operational` |
| `AI周期探索/0_总览/MINDSPACE_SOURCE_MCP_SOP.md` | `D+A` | `STATE/METHOD/AUTOMATION` | `03_STATE or 90_AUTOMATION` | `none` |
| `AI周期探索/0_总览/README.md` | `D+A` | `STATE/METHOD/AUTOMATION` | `03_STATE or 90_AUTOMATION` | `none` |
| `AI周期探索/0_总览/cn_consumer_refresh_queue.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/AUTOMATION_STATE or 90_AUTOMATION/RUNTIME` | `none` |
| `AI周期探索/0_总览/company_queue.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/AUTOMATION_STATE or 90_AUTOMATION/RUNTIME` | `none` |
| `AI周期探索/0_总览/company_score_table.md` | `D+A` | `STATE/METHOD/AUTOMATION` | `03_STATE or 90_AUTOMATION` | `none` |
| `AI周期探索/0_总览/cross_market_queue_v2.json` | `D+A` | `STATE/AUTOMATION` | `03_STATE/AUTOMATION_STATE or 90_AUTOMATION/RUNTIME` | `none` |
| `AI周期探索/0_总览/new_company_intake_queue.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/AUTOMATION_STATE or 90_AUTOMATION/RUNTIME` | `none` |
| `AI周期探索/0_总览/refresh_targets_2026-05-24.md` | `D+A` | `STATE/METHOD/AUTOMATION` | `03_STATE or 90_AUTOMATION` | `none` |
| `AI周期探索/0_总览/run_log.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/AUTOMATION_STATE or 90_AUTOMATION/RUNTIME` | `none` |
| `AI周期探索/0_总览/run_nightly_research_loop.sh` | `M+D` | `AUTOMATION` | `90_AUTOMATION/PIPELINES or 90_AUTOMATION/TESTS` | `operational` |
| `AI周期探索/0_总览/source_health_2026-05-24.md` | `D+A` | `STATE/METHOD/AUTOMATION` | `03_STATE or 90_AUTOMATION` | `none` |
| `AI周期探索/0_总览/tests/test_cross_market_v2.py` | `M+D` | `AUTOMATION` | `90_AUTOMATION/PIPELINES or 90_AUTOMATION/TESTS` | `operational` |
| `AI周期探索/0_总览/v2_last_outcome.json` | `D+A` | `STATE/AUTOMATION` | `03_STATE/AUTOMATION_STATE or 90_AUTOMATION/RUNTIME` | `none` |
| `AI周期探索/0_总览/v2_queue.py` | `M+D` | `AUTOMATION` | `90_AUTOMATION/PIPELINES or 90_AUTOMATION/TESTS` | `operational` |
| `AI周期探索/0_总览/v2_run_log.jsonl` | `D+A` | `STATE/AUTOMATION` | `03_STATE/AUTOMATION_STATE or 90_AUTOMATION/RUNTIME` | `none` |
| `AI周期探索/0_总览/v2_write_guard.py` | `M+D` | `AUTOMATION` | `90_AUTOMATION/PIPELINES or 90_AUTOMATION/TESTS` | `operational` |
| `AI周期探索/0_总览/validate_cross_market_v2.py` | `M+D` | `AUTOMATION` | `90_AUTOMATION/PIPELINES or 90_AUTOMATION/TESTS` | `operational` |
| `AI周期探索/0_总览/watchlist_master.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/AUTOMATION_STATE or 90_AUTOMATION/RUNTIME` | `none` |
| `AI周期探索/0_总览/信息重整与趋势刷新计划_2026-05-24.md` | `D+A` | `STATE/METHOD/AUTOMATION` | `03_STATE or 90_AUTOMATION` | `none` |
| `AI周期探索/0_总览/研究对象清单.md` | `D+A` | `STATE/METHOD/AUTOMATION` | `03_STATE or 90_AUTOMATION` | `none` |
| `AI周期探索/0_总览/结构性转变判断框架.md` | `M` | `METHOD` | `02_术/SKILLS/STRUCTURAL_CHANGE_BOTTLENECK.md` | `operational` |
| `AI周期探索/标的研究/四方股份_601126/README.md` | `M` | `EVIDENCE_ROUTER` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/标的研究/四方股份_601126/company_research.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/标的研究/四方股份_601126/evidence_log.md` | `D+M` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `AI周期探索/标的研究/四方股份_601126/next_signals.md` | `D+M` | `STATE` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/标的研究/四方股份_601126/research_task.md` | `D+A` | `STATE/AUTOMATION` | `03_STATE/HYPOTHESIS_QUEUE` | `none` |
| `AI周期探索/标的研究/四方股份_601126/scorecard.md` | `A+D` | `ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `codeex 版本/美股AI投资日报自动化计划_cc.md` | `A+M` | `AUTOMATION_ARCHIVE` | `90_AUTOMATION + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `none` |
| `codeex 版本/美股AI投资日报自动化计划_codeex版本.md` | `A+M` | `AUTOMATION_ARCHIVE` | `90_AUTOMATION + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `none` |
| `交易宪法/CONSTITUTION.md` | `S+A` | `CONSTITUTION` | `01_道/CONSTITUTION.md + 01_道/_HISTORY` | `murphy_confirmed` |
| `交易宪法/MURPHY_CURRENT_COGNITIVE_MODEL.md` | `S+A` | `MINDSET/STATE/META` | `01_道/MINDSET.md + 01_道/PHILOSOPHY_INBOX/INFERRED_PATTERNS.md + 03_STATE` | `none` |
| `交易宪法/_meta/全库投资资料覆盖清单.md` | `S+M+D` | `META` | `05_EVIDENCE_META/META/COVERAGE_MANIFEST.md` | `none` |
| `交易宪法/_meta/规则溯源与冲突裁决表.md` | `S+M+D` | `META` | `05_EVIDENCE_META/META` | `none` |
| `交易宪法/_meta/认知命题证据账本.md` | `S+M+D` | `META` | `05_EVIDENCE_META/META/CLAIM_LEDGER.md` | `none` |
| `交易宪法/_meta/认知模型来源分级与版本记录.md` | `S+M+D` | `META` | `05_EVIDENCE_META/META` | `none` |
| `交易宪法/skills/01_投资主框架.md` | `M` | `METHOD` | `02_术/TRADING_SYSTEM or 02_术/SKILLS` | `operational` |
| `交易宪法/skills/02_泊松供需闭环.md` | `M` | `METHOD` | `02_术/TRADING_SYSTEM or 02_术/SKILLS` | `operational` |
| `交易宪法/skills/03_流动性过滤器.md` | `M` | `METHOD` | `02_术/TRADING_SYSTEM or 02_术/SKILLS` | `operational` |
| `交易宪法/skills/04_行为纠偏系统.md` | `K+M` | `METHOD` | `02_术/SKILLS/BEHAVIOR_REVIEW.md` | `operational` |
| `交易宪法/skills/05_资本纪律.md` | `K+S` | `METHOD` | `02_术/TRADING_SYSTEM/02_CAPITAL_AND_EXECUTION.md + PARAMETERS.md` | `operational` |
| `交易宪法/skills/06_认知训练协议.md` | `M` | `METHOD` | `02_术/TRADING_SYSTEM or 02_术/SKILLS` | `operational` |
| `交易宪法/skills/07_认知模型维护协议.md` | `S+A` | `META/METHOD` | `05_EVIDENCE_META/META + 02_术/SKILLS` | `none` |
| `交易宪法/每日投资观察和思考/2026-07-22.md` | `D+S` | `STATE/MINDSET_INBOX` | `03_STATE + 01_道/PHILOSOPHY_INBOX` | `none` |
| `分析报告/.DS_Store` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE` | `none` |
| `分析报告/20260331-铜资源+AI基础设施+苹果供应链供给价值合并版.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE` | `none` |
| `分析报告/20260416-奥克斯电器+02580+秩序创造机器分析.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE` | `none` |
| `分析报告/20260606-加密基建+智驾+云基础设施-供给端交易假设.md` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE` | `none` |
| `分析报告/archive/260614储能材料链基金筛选与每日跟踪假设.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260615储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260615储能材料链基金报告对比审计.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260616储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260617AI算力连接与材料瓶颈_挖掘端框架.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260617AI算力连接与材料瓶颈_挖掘端框架_AI长报告原文.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260617AI算力链_训练集溯源.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260617储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260617特高压设备链拆解_用v1.1验证.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260617目标标的_市场情报监控与策略更新.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260617铜资源链下游拆解_紫金到PCB.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260618储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260618恒生科技ETF_重仓选择.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260619储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260620储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260622储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260623储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260624储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260625储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260625加密基建_智驾_云基础设施_6月底证据权重重估.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260625加密基建_智驾_云基础设施_6月底证据权重重估_AI长报告原文.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260626储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260627储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260628储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260629AI电力液冷光互连核能_ETF筛选.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260629AI电力液冷光互连核能_ETF筛选_AI长报告原文.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260629储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260630A股AI电力液冷光互连核电_标的筛选.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260630A股AI电力液冷光互连核电_标的筛选_AI长报告原文.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260630储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260630财报季_经营验证与定时任务体系.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260701储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260701重点标的_长期经营贝叶斯监控基线.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260701锂电池与储能产业链_第一性原理与基金决策.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260701锂电池与储能产业链_第一性原理与基金决策_AI长报告原文.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260702储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260703储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260704储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260705储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260705目标标的_月度经营与资本配置.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260706储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260706财报季_未来30天经营验证准备.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260707储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260708储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260709储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260709锂电材料链_修复逻辑再校验与波动策略.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260710储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260711储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260712储能材料链_每日假设跟踪.md` | `D+M` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260712重点标的_本周期假设更新与胜率赔率重估.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260713AI主题资产_Token需求传导与安全边际胜率.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260713投资_每日决策简报.md` | `D` | `STATE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260713财报季_未来30天经营验证准备.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260714投资_每日决策简报.md` | `D` | `STATE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260715投资_每日决策简报.md` | `D` | `STATE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260716投资_每日决策简报.md` | `D` | `STATE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260717投资_每日决策简报.md` | `D` | `STATE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260717组合_单日最大亏损纪律复盘与9万元配置.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260718投资_每日决策简报.md` | `D` | `STATE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260719投资_每日决策简报.md` | `D` | `STATE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260719组合_行为纠偏与资本纪律操作系统.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260719组合_行为纠偏与资本纪律操作系统_AI长报告原文.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260720AI算力制造_开源云定制ASIC与国产制造候选池.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260720投资_每日决策简报.md` | `D` | `STATE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260721投资_每日决策简报.md` | `D` | `STATE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260721组合_交易认知体系首轮训练.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/260722投资_每日决策简报.md` | `D` | `STATE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260723投资_每日决策简报.md` | `D` | `STATE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/SUPERSEDED_STATE` | `none` |
| `分析报告/archive/260723系统_Murphy投资系统工程重构方案.md` | `K` | `META` | `分析报告/archive/260723系统_Murphy投资系统工程重构方案.md` | `operational` |
| `分析报告/archive/BTGO_综合投资分析_2026-03-21_v2.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/BTGO_综合投资分析_2026-03-21_v3.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/BTGO_综合投资分析_2026-03.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/BitGo_BIT_综合投资分析_2026-03.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/archive/merged_sources/2026-06-06/20260331-立讯精密+工业富联+AI铜连接+双轨分析.md` | `D+A` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS` | `none` |
| `分析报告/archive/merged_sources/2026-06-06/20260331-铜产业+苹果AI供应链+双轨评级汇总.md` | `D+A` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS` | `none` |
| `分析报告/archive/merged_sources/2026-06-06/20260331-铜产业+苹果AI供应链投资分析.md` | `D+A` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS` | `none` |
| `分析报告/archive/merged_sources/2026-06-06/20260606-BTGO+Circle+地平线+Oracle+三年翻倍候选研究.md` | `D+A` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS` | `none` |
| `分析报告/archive/merged_sources/2026-06-06/20260606-BTGO+Circle+地平线+Oracle+供给价值历史合并版.md` | `D+A` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS` | `none` |
| `分析报告/archive/merged_sources/2026-06-06/20260606-BTGO+Circle+地平线+Oracle+基础设施收费权.md` | `D+A` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS` | `none` |
| `分析报告/archive/merged_sources/2026-06-06/20260606-BTGO+Circle+地平线+Oracle+结构窗口与财务窗口判断.md` | `D+A` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS` | `none` |
| `分析报告/archive/merged_sources/2026-06-06/20260606-BTGO+Circle+地平线+供给逻辑重审.md` | `D+A` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS` | `none` |
| `分析报告/archive/merged_sources/2026-06-06/20260606-CRCL+Circle+三年翻倍投资论文验证.md` | `D+A` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS` | `none` |
| `分析报告/archive/merged_sources/2026-06-06/20260606-地平线机器人+9660HK+三年翻倍验证.md` | `D+A` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS` | `none` |
| `分析报告/archive/merged_sources/2026-06-06/260606BTGO_Circle_地平线_Oracle_结构窗口与财务窗口判断.md` | `D+A` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS` | `none` |
| `分析报告/archive/merged_sources/2026-06-06/260606BTGO_HashKey_Circle_稳定币供给方数字拆解.md` | `D+A` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS` | `none` |
| `分析报告/archive/新能源汽车产业链投资报告.md` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术` | `none` |
| `分析报告/个人投资组合经营与资本配置/260715组合_候选公司证据表.md` | `S+D+A` | `EVIDENCE/STATE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 03_STATE + 02_术` | `none` |
| `分析报告/个人投资组合经营与资本配置/260715组合_贝叶斯监控基线.md` | `S+D+A` | `EVIDENCE/STATE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 03_STATE + 02_术` | `none` |
| `分析报告/个人投资组合经营与资本配置/260715组合_长期经营与资本配置.md` | `S+D+A` | `EVIDENCE/STATE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 03_STATE + 02_术` | `none` |
| `分析报告/个人投资组合经营与资本配置/260715组合_长期经营与资本配置_AI长报告原文.md` | `S+D+A` | `EVIDENCE/STATE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 03_STATE + 02_术` | `none` |
| `分析报告/分析报告合并索引.md` | `M+A` | `EVIDENCE_ARCHIVE` | `05_EVIDENCE_META/EVIDENCE` | `none` |
| `基础概念/.DS_Store` | `D+S` | `EVIDENCE/METHOD` | `05_EVIDENCE_META/EVIDENCE + 02_术/SKILLS` | `none` |
| `基础概念/IP 消费类/IP 价值&泡泡.md` | `D+S` | `EVIDENCE/CASE/MINDSET_INBOX` | `05_EVIDENCE_META/EVIDENCE/THEMES + 04_CASE_GYM + 01_道/PHILOSOPHY_INBOX` | `none` |
| `基础概念/ploymarket/.100x-monitor.sh` | `A+D` | `EVIDENCE/AUTOMATION` | `05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS + 90_AUTOMATION` | `none` |
| `基础概念/ploymarket/.100x-state` | `A+D` | `EVIDENCE/AUTOMATION` | `05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS + 90_AUTOMATION` | `none` |
| `基础概念/ploymarket/100X 萃取内容看板.md` | `A+D` | `EVIDENCE/AUTOMATION` | `05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS + 90_AUTOMATION` | `none` |
| `基础概念/ploymarket/monitor-100x.sh` | `A+D` | `EVIDENCE/AUTOMATION` | `05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS + 90_AUTOMATION` | `none` |
| `基础概念/ploymarket/monitor.log` | `A+D` | `EVIDENCE/AUTOMATION` | `05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS + 90_AUTOMATION` | `none` |
| `基础概念/ploymarket/update-dataview.sh` | `A+D` | `EVIDENCE/AUTOMATION` | `05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS + 90_AUTOMATION` | `none` |
| `基础概念/ploymarket/资料/信息看板.md` | `A+D` | `EVIDENCE/AUTOMATION` | `05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS + 90_AUTOMATION` | `none` |
| `基础概念/交易策略组合/260606投资框架_供需泊松闭环.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/260617三大材料链对照表_AI_储能_铜.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/260617挖掘端SOP_v1.1.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/260617挖掘端三分布应用决策表.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/260617挖掘端工作流SOP_v1.0.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/260617挖掘端训练完成报告.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/260617挖掘端训练循环与评估手册.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/260622基金与个股_从个人约束出发的1至3年框架.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/260622电解液_需求强度非线性信号框架.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/260622电解液_需求强度非线性信号框架.pdf` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/260622电解液_需求强度非线性信号框架_AI长报告原文.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/260624电解液_物理需求线性与利润估值非线性.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/260709投资框架_股价三层肉估值三段式与不做清单.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/260713AI_Token需求增长与稀缺性迁移投资框架.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/260720投资框架_宏观流动性过滤器与认知退出纪律.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/期权卖方统计学与Roll策略实战.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/期权基础.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/期权策略与认知演进总结.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/波动率收割与期权量化策略体系.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/稳定币与财务指标概念路径.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/交易策略组合/量化交易数学基础设施.md` | `M+S+A` | `METHOD/EVIDENCE_ARCHIVE` | `02_术/SKILLS + 05_EVIDENCE_META/ARCHIVE/HISTORICAL_SYSTEMS` | `operational` |
| `基础概念/实体商/.DS_Store` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/.claude/settings.local.json` | `M` | `AUTOMATION` | `90_AUTOMATION/RUNTIME` | `none` |
| `基础概念/实体商/.codepilot-uploads/1777528651722-SKILL_3.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/BItGO/BTGO_投资决策.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/BItGO/未命名.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/CRCL/Circle (CRCL) 公司基本面分析.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/CRCL/Circle (CRCL) 投资洞察.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/CRCL/E71. Circle暴涨70%- OpenClaw引爆Agent支付新叙事.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/CRCL/lufeieth关于CRCL的20条思考.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/CRCL/资料/Circle转型Agent支付对标Stripe.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/HashKey/20260606-HashKey中国资产RWA基础设施验证.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/HashKey/HashKey vs BitGo 投资对比.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/HashKey/HashKey_投资决策.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/HashKey/未命名.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/LMND/20260430T120000==z--投资分析-LMND.org` | `D` | `EVIDENCE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES` | `none` |
| `基础概念/实体商/LMND/LMND_Q1_2026_财报会深度分析_8维框架.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/LMND/LMND_Q4_2025_财报会深度分析_8维框架.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/LMND/LMND_投资决策手册.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/LMND/LMND_深度研究底稿.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/LMND/LMND_深度研究底稿_v2_20260430.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/LMND/LMND交易方案.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/TEMP/TEM_市场时机分析_20260321.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/TEMP/TEM_综合投资分析_2026-03-21.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/TEMP/未命名.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/储能材料链基金研究/00_储能材料链基金研究总报告_20260614.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/储能材料链基金研究/01_每日跟踪信号表.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/储能材料链基金研究/02_产业链龙头公司全表.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/储能材料链基金研究/03_daily/2026-06-15.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/储能材料链基金研究/03_daily/2026-06-17.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/储能材料链基金研究/03_daily/2026-06-18.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/储能材料链基金研究/03_daily/2026-06-19.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/储能材料链基金研究/03_daily/2026-06-20.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/储能材料链基金研究/03_daily/2026-06-22.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/储能材料链基金研究/03_daily/2026-06-24.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/储能材料链基金研究/03_daily/2026-06-28.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/储能材料链基金研究/03_daily/2026-06-29.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `基础概念/实体商/储能材料链基金研究/20260712 能源认识.md` | `D+S` | `EVIDENCE/CASE` | `05_EVIDENCE_META/EVIDENCE/COMPANIES + 04_CASE_GYM` | `none` |
| `我的投资框架：从宏观到企业的系统思考.md` | `S+A` | `METHOD/MINDSET/EVIDENCE` | `99_ARCHIVE/LEGACY_LAYOUT + 02_术/SKILLS + 01_道/PHILOSOPHY_INBOX` | `none` |
| `📈 个人交易手册.md` | `S` | `STATE/CASE/METHOD` | `03_STATE/PORTFOLIO_LEDGER.md + 04_CASE_GYM/TRADE_LOG + 02_术/TRADING_SYSTEM` | `operational` |
| `📊 股票投资看板.md` | `A+M` | `HOME` | `00_HOME/HOME.md` | `none` |
