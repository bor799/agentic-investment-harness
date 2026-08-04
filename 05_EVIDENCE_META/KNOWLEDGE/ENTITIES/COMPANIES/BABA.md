---
knowledge:
  knowledge_id: ENTITY-BABA
  knowledge_type: entity_knowledge
  entity_id: BABA
  entity_name: 阿里巴巴集团
  belief_ids: [BABA-B01, BABA-B02, BABA-B03]
  decision_authority: none
layer: KNOWLEDGE
primary_role: entity_knowledge
status: active
authored_by: human_ai
source_type: P3
human_reviewed: false
last_reviewer: "pending | murphy_review | 2026-07-30"
write_intent: explicit_persist
research_protocol_ref: 03_STATE/DOMAIN_MODELS/AI/AI_CSP_domain_knowledge_codex_protocol_v1.md
---

# 阿里巴巴｜稳定实体知识（研究层 working belief）

阿里巴巴在本次 CSP 研究中的定位：中国主池核心标的，AI 云商业化最直接的表达之一，但 FY26 Q4 EBITA 暴跌与集团 FCF 转负证明"AI 投入→利润/现金流"链条尚未打通。

### BABA-B01｜云外部收入加速由 AI 驱动

```yaml
belief:
  claim_id: BABA-B01
  proposition: 阿里云外部收入 FY26 Q4 加速至 +40%，AI 占比 ~30%，证明 AI 真实驱动云消费增长。
  origin: ai_narrative
  origin_ref: 03_STATE/DOMAIN_MODELS/AI/AI_CSP_domain_knowledge_codex_protocol_v1.md（协议基线）
  state: supported
  mechanism: 开放模型（Qwen）+ Model Studio 客户增长 8x + AI 推理与训练需求带动 IaaS/PaaS 消费
  supports_if: 云外部收入增速维持 30%+，AI 占比维持 25%+
  weakens_if: 增速回落至 20% 以下，或 AI 占比下降，或增长来自低毛利项目
  cannot_prove: 增速可以自动转为集团利润
  alternative_model: 模型价格战压低单价，量增长但收入增长不能持续
  source_refs:
    - 05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/260730CSP消费端拐点_完整研究_AI长报告原文.md
    - https://www.alibabacloud.com/blog/alibaba-cloud-revenue-growth-accelerates-to-40-as-ai-strategy-delivers
  latest_moment: MOM-260730-AI-CSP-RESEARCH-01
```

### BABA-B02｜云 EBITA 与集团 FCF 暂未跟上 AI 投入

```yaml
belief:
  claim_id: BABA-B02
  proposition: FY26 Q4 云 EBITA -84% YoY、集团 FCF 转负（约 -RMB 17-22B），AI 投入 ~$56B 暂未在利润和现金流上兑现。
  origin: ai_narrative
  origin_ref: 05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/260730CSP消费端拐点_完整研究_AI长报告原文.md
  state: supported
  mechanism: AI IaaS CapEx 巨大、扩产冲击当季 EBITA、电商与新业务投入抵消云利润
  supports_if: FY27 Q1 云 EBITA 季度环比恢复 + 集团 FCF 季度转正
  weakens_if: FY27 Q1 EBITA 同比持续 -50% 以下、FCF 持续负值
  cannot_prove: 当前是扩产一次性冲击还是结构性利润压力
  alternative_model: AI 投入长期覆盖不了资本成本，云业务成为低回报公用事业
  source_refs:
    - 05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/260730CSP消费端拐点_完整研究_AI长报告原文.md
    - https://www.stocktitan.net/sec-filings/BABA/6-k-alibaba-group-holding-ltd-current-report-foreign-issuer-164c9931befd.html
    - https://finance.yahoo.com/markets/stocks/articles/alibaba-group-holding-ltd-baba-230305063.html
  latest_moment: MOM-260730-AI-CSP-RESEARCH-01
```

### BABA-B03｜控制面齐全但估值未完整反映 FCF 风险

```yaml
belief:
  claim_id: BABA-B03
  proposition: 阿里掌握算力/数据/数据库（PolarDB）/权限（钉钉）/安全/工作流/应用分发（淘宝+支付宝+钉钉）7/7 控制面，但当前估值未充分计入 FCF 转负。
  origin: ai_narrative
  origin_ref: 05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/260730CSP消费端拐点_完整研究_AI长报告原文.md
  state: working
  mechanism: 控制面齐全是 CSP 控制面理论的最佳候选之一，但 H_P 触底（[0.14-0.51]）尚未解除
  supports_if: FY27 Q1 后云 EBITA 恢复 + FCF 转正 + 市场对 FCF 转负充分定价（股价 -15% 至 -20%）
  weakens_if: 控制面虽齐全但盈利兑现路径不清晰，市场继续给予折价
  cannot_prove: 控制面齐全必然带来高毛利 AI 收入
  alternative_model: 阿里仅作为低价容量承接方，数据引力不足以形成定价权
  source_refs:
    - 05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/260730CSP消费端拐点_完整研究_AI长报告原文.md
  latest_moment: MOM-260730-AI-CSP-RESEARCH-01
```

## 资金分账

| 项目 | 含义 | 不能混成什么 |
|---|---|---|
| 云外部收入 | 来自阿里集团外部客户的云收入 | 不是利润，也不是现金 |
| 云 EBITA | 云集团息税摊销前利润 | 不是自由现金流，受 CapEx 和折旧影响 |
| 集团 FCF | 集团整体自由现金流 | FY26 转负，不能由云收入增长自动推导为正 |
| AI 投入 | 资本开支+研发+运营投入 | 不能直接当成未来收入 |
| 调整后净利润 | 剔除一次性项目后的净利润 | FY26 几乎归零（~$12M），不能作为估值分母 |

## 当前研究层判断

- 协议 H_B 业务票：posterior [0.71, 0.875, 0.94]（强，AI 占比 + 30% 印证）
- 协议 H_P 利润捕获票：posterior **[0.14, 0.29, 0.51]**（**触底**，< 0.65 阈值）
- 协议 H_R 回报票：posterior [0.40, 0.55, 0.70]（临界）
- 协议 H_T 时点票：posterior [0.40, 0.50, 0.60]（临界）
- 研究层分类：C 偏 B（当前不入场，等待 FY27 Q1 验证）

## 验证窗口

- FY27 Q1 财报（约 2026-08 中下旬）：云 EBITA 恢复 + 集团 FCF 季度转正 + AI 占比上行
- 失效条件：FY27 Q1 云 EBITA 同比 < -50% 持续、FCF 持续负值、AI 占比下降

## 关联

- 协议：`03_STATE/DOMAIN_MODELS/AI/AI_CSP_domain_knowledge_codex_protocol_v1.md`
- 主长报告：`05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/260730CSP消费端拐点_完整研究_AI长报告原文.md`
- AI Domain：`05_EVIDENCE_META/KNOWLEDGE/DOMAINS/AI/README.md`（AI-P01 利润穿透合格模式）
- ETF 513050 实体知识：`05_EVIDENCE_META/KNOWLEDGE/ENTITIES/ETFS/513050.md`（阿里占 24.72% 权重）
- 无 current thesis 卡（未达"可买"门槛）
