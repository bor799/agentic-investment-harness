---
receipt:
  receipt_id: MP-20260728-ABSORPTION
  migration_id: MP-20260728-01
  approved_plan_sha256: cfb97d9e19bdcf930369ad7900fe7dc25e7bddfd47dbe3cc9409af97dbc9699d
  applied_at: 2026-07-28
  status: applied
  deletion_count: 0
  decision_authority: none
layer: META
primary_role: absorption_receipt
status: active
authored_by: ai
source_type: P3
human_reviewed: false
last_reviewer: "PASS | independent_readonly | 2026-07-28"
---

# 投资“记忆宫殿”全库重构吸收回执

## 结果

系统入口已改成：

```text
研究触发
→ 稳定领域知识与 Case
→ structural_prior
→ Current 与新证据
→ 四票
→ 六档动作
```

`structural_prior` 只给领域、模式、反模式和首问，固定
`evidence_status: uncalibrated`，没有价格、四票、动作或仓位权限。

本次没有修改 Murphy 的道、Decision Contract、Portfolio Ledger、既有 Case 正文、
持仓、交易或资本参数。

## 七张领域判断地图与资格矩阵

| Domain | 合格模式 | 根来源 | 复用标的/Case | Holdout | 泛化结论 |
|---|---|---:|---:|---|---|
| `AI` | `AI-P01` 需求必须穿透利润与现金 | 2 | 2 | Microsoft | schema 通过，跨周期仍待结算 |
| `ENERGY_STORAGE_MATERIALS` | `unknown` | 0 | 0 | 湖南裕能 | `evidence_insufficient` |
| `CHINA_INTERNET` | `CI-P01` 先穿透产品再判断行业 | 3 | 2 | PDD | 公司型 holdout 不适用 ETF 模式，`evidence_insufficient` |
| `CONSUMER_IP` | `CIP-P01` 热度必须穿透周转与自由现金 | 3 | 2 | Sanrio | schema 通过，跨周期仍待结算 |
| `INNOVATIVE_DRUGS` | `unknown` | 0 | 0 | Akeso | `evidence_insufficient` |
| `STABLECOIN_CRYPTO_INFRA` | `SCI-P01` 分清收费池与普通股索取权 | 3 | 3 | Coinbase | schema 通过，跨周期仍待结算 |
| `RESOURCES_POWER_GRID` | `RPG-P01` 相同需求按资产钱路拆开 | 4 | 4 | Vistra | schema 通过，跨周期仍待结算 |

准入只表示满足“双根、双复用、因果链、证伪条件”，不表示已跨周期证明。
储能材料与创新药没有为完整性凑模式。

AI 母稿产生的“瓶颈迁移、Token 与效率、企业控制平面、Physical AI、泡沫后资源
迁移”只留为候选，没有进入 60 秒前台。七张地图均标记
`source_type: P3`、`human_reviewed: false`；Reviewer PASS 不冒充 Murphy 原话。

AI-B01～AI-B04 的唯一完整正文迁入
[[05_EVIDENCE_META/_SYSTEM/CLAIM_LEDGER]]，领域地图只反链，不再复制第二套正文。

## Current 追溯映射

所有 20 张 Current 只增加：

```yaml
domain_ids:
pattern_ids_relevant:
orientation_status: retrospectively_mapped
```

没有任何 `pattern_ids_used`，不声称历史判断当时使用过新模式。

| Current | Domain | Pattern |
|---|---|---|
| `002709` | `ENERGY_STORAGE_MATERIALS` | `[]` |
| `09660` | `AI` | `AI-P01` |
| `09896`、`09992` | `CONSUMER_IP` | `CIP-P01` |
| `159326`、`159611` | `RESOURCES_POWER_GRID` | `RPG-P01` |
| `513050`、`513130` | `CHINA_INTERNET` | `CI-P01` |
| `513120` | `INNOVATIVE_DRUGS` | `[]` |
| `515880`、`562500`、`588000` | `AI` | `AI-P01` |
| `600487` | `AI` + `RESOURCES_POWER_GRID` | `AI-P01` + `RPG-P01` |
| `601899`、`601985` | `RESOURCES_POWER_GRID` | `RPG-P01` |
| `BTGO`、`CRCL`、`MSTR` | `STABLECOIN_CRYPTO_INFRA` | `SCI-P01` |
| `NBIS`、`ORCL` | `AI` | `AI-P01` |

两条前台旧镜像入链已按证据身份修正：

- `600487`：字节完全一致的镜像改指 `归档/` 唯一保留件；
- `002709`：移除派生综合链接，直接保留 SMM、财联社、鑫椤锂电/东方财富三条
  时点来源；这些只支持价格与排产环境，不升级经营判断。

## AI Outlook

AI 领域只有 [[03_STATE/DOMAIN_MODELS/AI/README]] 一份顶层 `status: active`。

- `INVESTMENT_MAP.md`：`status: superseded`；
- `AI_PHYSICAL_INFRASTRUCTURE.md`：`status: superseded`；
- `ENTERPRISE_AI_CONTROL_PLANE.md`：`status: superseded`。

两张旧 Thesis 的 `outlook_status` 保持原值；退出前台是生命周期整理，不伪造成
“证据变弱”。

## 原文归档与下载区

- Vault 活动归档：
  [[05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/260728AI领域知识母稿_投资之道到Physical_AI_AI长报告原文]]
  `SHA256=1b75382a8a6bb915eb9475121a2a8fe52459712c260dac9f45c4a589d1be0614`；
- 改写前 AI Knowledge 原文：
  [[05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/260728AI领域知识_控制平面原子版_AI长报告原文]]
  `SHA256=97f87942a59e498dfb2ece530cae5d35cf9ae2833cc0bc15776ec2d282fe3c03`；
- 下载区母稿已移到 macOS 废纸篓，可恢复；废纸篓副本与 Vault 归档哈希一致；
- `Codex_AI研究知识层_持续吸收提示词_20260728.md` 仍在 Downloads，
  `SHA256=4f9ba8cbdc3bb870d2b00a8b0c3490d19898d905862eab0074dd7ad0443a5950`；
  Vault 中没有该 prompt，也没有激活它。

## 删除清单

```yaml
exact_duplicate_mirror_candidates: 536
incoming_link_documents:
  min: 1
  max: 8
eligible_zero_incoming: 0
deletion_entries: []
deleted_files: 0
```

536 个候选均存在兼容索引入链，没有一个同时满足“字节完全一致、保留件存在、
入链清零”。因此本次不删除文件，也没有把语义近似文件误当重复文件。兼容区退出
HOME 前台，继续作为冷验证层。

## 验收

### 结构先验

- 9 个已映射回归样本、7 个 holdout、1 个未知身份样本，共 17 个；
- 17 个均通过 `V-20`；
- 单次输出最多 2 个领域、3 个模式、3 个首问；
- 输出不含价格、四票、动作或仓位；
- 覆盖 ETF、经营公司、资源周期、公用事业、资本结构载体、跨领域与未知领域；
- holdout 只证明路由合同可运行；4 个为 provisional，3 个明确
  `evidence_insufficient`，没有宣称全域泛化通过。

17 个完整输入、逐项 `V-20` 输出与失败检查位于：

`.harness_backup/20260728_memory_palace_business/audit/structural_prior_tests.json`

`SHA256=fbb5935b05e5f5d81b2ee3cecc2bced4cd245530cb0a9102076d37413ffeb99d`。

### 前台

```yaml
frontstage_scope: HOME + domain index/maps + 20 Current + AI active Outlook
frontstage_files: 30
wiki_links_checked: 69
broken_links: 0
legacy_mirror_or_review_queue_links: 0
exact_duplicate_groups: 0
illegal_write_sinks: 0
active_ai_outlooks: 1
```

### Validator 与测试

- 所有正式目标分别取得独立 Reviewer PASS；
- 所有正式写入均以与 `write_target` 完全一致的 `allowed_write_route` 通过写前与
  写后 Validator；
- Validator/test suite：`156 passed`；
- Python compile：PASS；
- `structural_prior`、`pattern_map`、`governance_migration` 正反测试已纳入测试集。

### 哈希、权限与恢复

全库审计范围排除 `.harness_backup/`、`.git/` 和本回执自身：

```yaml
pre_files: 1557
post_files: 1568
pre_inventory_sha256: 83ce1c5bc26a60a74f9d55ab1edf75f6f19c76621fa28977c0b35cf24e1ee6eb
post_inventory_sha256: 61b3f5fee4f3449dd98ff0b3d818293d5289f7e0d3a517729f4b435fa1f782d5
backup_manifest_sha256: fc75ef8e719a3ac4b36c07548c170dbb28daab43be090c38102187a3b4caf2d2
backup_entries: 33
permission_checks: 26
permission_mismatches: 0
restore_samples: 5
restore_failures: 0
```

完整审计位于：

- `.harness_backup/20260728_memory_palace_business/audit/pre_inventory.jsonl`
- `.harness_backup/20260728_memory_palace_business/audit/post_inventory.jsonl`
- `.harness_backup/20260728_memory_palace_business/audit/backup_manifest.json`

保护文件逐字未变：

| 文件/集合 | SHA256 |
|---|---|
| `01_道/CONSTITUTION.md` | `9246926011302737e33c72306b5e290f3363f535a351daa914bf9d3a17568513` |
| `01_道/MINDSET.md` | `6d465732a98b7da24064d32f3843cbd9b6096014864f837cb194df64d91c2258` |
| `02_术/TRADING_SYSTEM/00_DECISION_CONTRACT.md` | `3a4bcdfd166e88c5e33d3c76ba9211e43aa4f06ed87f58c036f42b64fb1fe350` |
| `03_STATE/PORTFOLIO_LEDGER.md` | `05c14737ef3106d16d43869807b85b6652c8071da3ef1697eb6013bc1d7ede5c` |
| `01_道/` 11 个文件 | before/after 逐文件一致 |
| `04_CASE_GYM/` 28 个文件 | before/after 逐文件一致 |

迁移后的集合哈希：

```yaml
control_set_sha256: 08ea44abbc3cb70ef0ef77ad45f95d96b06e47a151d97e0963cb8ce8ee00df9b
domain_map_set_sha256: d6250d6eff8121013a6fc48b6756b6729a92392018fd1fdd5938cb9bb755b527
current_set_sha256: fd4f2a7c77ffa5eebb452c83ec095544f41d004ff19a0d48acb0e9c8a72c59d8
frontstage_set_sha256: 8adc9c3e91f59513c0592b832d4297b5aedd648edb0ff7c1be0cdecd11f5ea2f
claim_ledger_sha256: 1db1f8de30d067e28a1edaf21daeb3958fd63fd63ef9e2aa5bc2c59010d7c047
```

首轮治理控制变更的精确前后哈希、备份和恢复命令见
`05_EVIDENCE_META/_SYSTEM/ABSORPTION_RECEIPTS/260728_memory_palace_governance_contract.json`。
其后 Validator 与测试文件又经过一次窄补丁审查，因此该首轮合同不代表这两个文件的
最终哈希；最终文件哈希以 `post_inventory.jsonl` 和上方 `control_set_sha256` 为准。

## 边界

这次迁移建立的是“先调用经验，再读取当前事实”的研究顺序，不是投资结论。
任何有效标的仍必须进入 Current、新证据、四票与六档动作；历史类比不能阻止读取
反向的新证据。
