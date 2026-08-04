---
title: "new_company_intake_queue"
date: 2026-07-24
updated: 2026-07-24
layer: STATE
primary_role: legacy_automation_state
status: superseded
authored_by: human_ai
source_type: PX
human_reviewed: false
decision_authority: none
legacy_metadata_added: true
legacy_path: "AI周期探索/0_总览/new_company_intake_queue.md"
migration_target: "90_AUTOMATION/RUNTIME + 03_STATE"
source_paths:
  - 分析报告/archive/260723系统_Murphy投资系统工程重构方案.md
---
# New Company Intake Queue

用途：记录新发现、手动新增或工程师信号带出的公司。这里的目标是“先研究起来”，交易权限只作为独立字段，不作为跳过研究的理由。

状态规则：
- `pending_research`：等待公司级研究。
- `in_progress`：当前循环正在处理。
- `research_complete`：公司级研究文件已完成，并同步到总览表。
- `blocked_mcp_unavailable`：Mindspace MCP health_check 失败，本轮未研究。
- `evidence_limited_after_fallback`：已完成 MCP 和 agent-reach fallback，但关键证据仍有限。

交易权限标签：
- `direct_buy_likely`：常规账户或已开通对应市场后大概率可直接交易。
- `requires_chinext_permission`：需要创业板交易权限。
- `requires_star_permission`：需要科创板交易权限。
- `h_share_watch`：H 股上市/代码/可交易状态需要继续观察。

| status | 公司 | 代码 | 市场 | 板块 | 交易权限 | 是否可直接买 | 来源信号 | 初始分组 | watch_trigger |
|---|---|---|---|---|---|---|---|---|---|
| evidence_limited_after_fallback | 湖南裕能 | 301358.SZ | A股 | 深交所创业板 | requires_chinext_permission | 需确认创业板权限 | 手动新增 | 锂电材料/磷酸铁锂 | 创业板权限确认；磷酸铁锂供需反转；宁德时代/比亚迪客户集中变化 |
| evidence_complete | Marvell Technology | MRVL | 美股 | Nasdaq | direct_buy_likely | 可直接买（美股权限） | 手动新增/AI网络瓶颈 | AI网络/定制芯片/数据中心互联瓶颈 | ASIC/光互联/交换芯片收入增速；大客户订单；AI网络毛利率 |
| evidence_limited_after_fallback | 天华新能 | 300390.SZ | A股 | 深交所创业板 | requires_chinext_permission; h_share_watch | 需确认创业板权限；H股尚未正式上市 | 手动新增 | 锂电材料/氢氧化锂 | H股上市进度；锂价反转；氢氧化锂产能利用率；CATL/SK等客户订单 |
| evidence_limited_after_fallback | 胜宏科技 | 300476.SZ | A股 | 深交所创业板 | requires_chinext_permission | 需确认创业板权限 | 手动新增/AI PCB | AI服务器PCB/高密度互联 | AI服务器PCB收入占比；海外大客户；扩产兑现；毛利率持续性 |
| evidence_limited_after_fallback | 沪电股份 | 002463.SZ | A股 | 深交所主板 | direct_buy_likely | 可直接买（A股主板权限） | 手动新增/AI PCB | AI服务器PCB/高速互联 | AI PCB收入占比；毛利率趋势；大客户验证；与胜宏/深南对比 |
| evidence_limited_after_fallback | 生益电子 | 688183.SH | A股 | 上交所科创板 | requires_star_permission | 未开科创板则不能直接买 | 手动新增/AI PCB | 高端PCB/服务器与通信设备 | Q1 GM 35%+；核心ASIC客户；客户切换过渡期；新产能投产进度 |
| evidence_limited_after_fallback | 深南电路 | 002916.SZ | A股 | 深交所主板 | direct_buy_likely | 可直接买（A股主板权限） | 手动新增/PCB+载板 | PCB/封装基板/高速互联 | IC载板良率；无锡46亿扩产进度；AI PCB收入占比；载板盈利时间表 |
| evidence_limited_after_fallback | 广合科技 | 001389.SZ / 01989.HK | A股/H股 | 深交所主板/港股主板 | direct_buy_likely | 可直接买（A股主板或港股权限） | 手动新增/算力PCB | 算力服务器PCB/高速高频PCB | PCIE6.0 Q3量产；GM 37%可持续性；限售股解禁；新客户认证 |
