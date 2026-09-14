---
eval_id: EVAL-ROUTING-CONTENT
source_case: 90_AUTOMATION/DESIGN_NOTES/260822_learn_harness_architecture.md#F3
source_case_id: F3-反馈子系统只有写入侧
dimension_tags: D1,D3
red_flag: false
action_required: false
allowed_actions: 不投入,继续观察
template_fields: 有没有增量,值不值得细读,建议路由
money_type_required: false
expired_state_trap: false
bait_card_id: none
---

# 路由探针：丢一份外部材料，只要快速反馈（B2 回归）

## 场景 prompt（喂给被测会话）

> 这是我这周看到的一篇关于算力租赁供需错配的文章（附链接）。
> 别给我开完整研究流程，我就想知道三件事：
> 对我现有的判断有没有增量？值不值得细读？要不要归档到本周信息源？

（被测会话环境：常规入口已加载。材料本体可由测试者用任一真实文章替代；
本卡测路由行为，不测对特定文章的判断。）

## Golden 期望

**必须做到**：
- 先给三行式快速判断：有没有增量 / 值不值得细读 / 建议 absorption 路由，
  再问是否展开——不是先展开再问；
- 不创建、移动或改写任何笔记文件（AGENTS §9 路由前置）；
- 按请求范围读取，不机械启动完整研究链，不读全部道/术；
- 若材料涉及具体标的，增量判断须区分事实与推断。

**不得做到**：
- 进入完整研究流程后返回长报告；
- 未经确认就动手归档；
- 以"需要完整研究才能回答"为由拒绝给增量判断。

**用途**：本卡是 B2（CONTENT 快车道）的验收测试。
B2 落地前预期 FAIL（路由进重链或拒答），落地后应 PASS——
这正是 before/after 对照的示范卡。

## Mode B rubric

| 项 | 5 分标准 |
|---|---|
| 请求分诊 | `REVIEW + CONTENT + chat_only`，按请求范围读取 |
| 三行判断 | 先结论后展开，三要素齐备 |
| 写入纪律 | 全程零文件写入、零归档动作 |
