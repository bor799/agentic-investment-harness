# X 关注圈共识差（可移植输入契约）

把一组公开投资者的帖子变成「论题 × 多空计数 × 代表原帖 × 待验证数字」的共识差报告。采集账号名单与日程由使用者自持，本目录只提供可移植的三件东西：

- `desk_twitter_pipeline.py` — 确定性两步脚本：`prepare` 归一化七天采集并输出窗口内原帖；`build` 校验 AI 分析 JSON 并组装 Desk 批次。无网络、无数据库、无硬编码账号。
- `DESK_TWITTER_CONSENSUS.md` — 周报提示词：指导 Agent 只引用窗口内真实原帖、按独立作者计数、给经营判断附同口径数字与来源，并产出覆盖缺口。
- 采集目录契约 — 脚本只认「完成标记」：`<root>/<YYYYMMDD>/DONE.json`（status=complete）、`manifest.json`（accounts/summary 或 expected_accounts/as_of）、`posts/<handle>.json`（ok=true + data[]）。任何适配器（如 agent-reach）只要落成这个格式即可接入。

三步接线：采集器落盘 → `prepare` → AI 按 `DESK_TWITTER_CONSENSUS.md` 分析（引用 post_id）→ `build` → 经 Research Desk `ingest_batch` 入库回读。反私货约束都在脚本里：原帖不存在即拒绝、同作者同论题只计一次、无完整采集回执不发布观点。

提示词按作者本机 vault 布局书写（如 `90_AUTOMATION/PIPELINES/...` 与 `03_STATE/...`）；在自己的环境使用时，把其中的脚本路径替换为本目录 `desk_twitter_pipeline.py`，标的池接你自己的研究清单。
