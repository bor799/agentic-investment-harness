---
knowledge:
  knowledge_id: ENTITY-TCEHY
  knowledge_type: entity_knowledge
  entity_id: TCEHY
  entity_name: 腾讯控股
  belief_ids: [TCEHY-B01, TCEHY-B02, TCEHY-B03]
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

# 腾讯控股｜稳定实体知识（研究层 working belief）

腾讯在本次 CSP 研究中的定位：**平台 AI 综合受益标的（不是纯云计算）**。集团 FCF 和净现金强劲提供 AI 投入缓冲，但 2026 大幅削减回购是关键反证。

### TCEHY-B01｜平台 AI 综合受益而非纯云计算

```yaml
belief:
  claim_id: TCEHY-B01
  proposition: 腾讯通过广告 AI（+20%）、游戏 AI、金融科技 AI、企业服务（含云，+20%）多渠道变现 AI；云占集团总收入 < 10%。
  origin: ai_narrative
  origin_ref: 05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/260730CSP消费端拐点_完整研究_AI长报告原文.md
  state: supported
  mechanism: 微信+视频号+企业微信+游戏+广告多触点交叉变现 AI 能力
  supports_if: Business Services +20% 持续 + 广告 +20% 持续 + 海外云 +40% 持续
  weakens_if: Business Services 增速 < 12%、广告增速 < 10%、海外云增速 < 20%
  cannot_prove: 腾讯是"纯云计算"标的
  alternative_model: 集团增长主要由游戏周期驱动，AI 仅是辅助
  source_refs:
    - https://static.www.tencent.com/uploads/2026/05/13/47382ae415a209fd161bc19a1f9b3704.pdf
    - https://static.www.tencent.com/uploads/2026/05/13/aaeed028d215a9612da4b41aca17708b.pdf
  latest_moment: MOM-260730-AI-CSP-RESEARCH-01
```

### TCEHY-B02｜FCF + 净现金覆盖 AI 投入

```yaml
belief:
  claim_id: TCEHY-B02
  proposition: 26Q1 FCF RMB 56.7B（+20% YoY）、净现金 RMB 146.9B（+63% YoY），AI 投入 RMB 8.8B 影响被集团造血能力覆盖。
  origin: ai_narrative
  origin_ref: 05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/260730CSP消费端拐点_完整研究_AI长报告原文.md
  state: supported
  mechanism: 游戏+广告稳定现金流 + 金融科技 + 企业服务多业务组合 + 微信生态垄断地位
  supports_if: FCF 维持 +20% 增速、净现金维持增长
  weakens_if: FCF 增速 < 10%、AI 投入持续扩大拖累利润
  cannot_prove: 当前 FCF 强劲可以维持 4 个季度以上
  alternative_model: AI 投入规模扩大超过 FCF 承受能力，类似阿里路径
  source_refs:
    - https://static.www.tencent.com/uploads/2026/05/13/aaeed028d215a9612da4b41aca17708b.pdf
  latest_moment: MOM-260730-AI-CSP-RESEARCH-01
```

### TCEHY-B03｜微信身份+应用分发构成独特控制面

```yaml
belief:
  claim_id: TCEHY-B03
  proposition: 微信（13 亿用户）+ 企业微信 + 视频号 + 应用宝构成中国最广身份入口和应用分发渠道，是腾讯 CSP 控制面的独特优势。
  origin: ai_narrative
  origin_ref: 05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/260730CSP消费端拐点_完整研究_AI长报告原文.md
  state: working
  mechanism: 身份入口+应用分发决定 AI 产品（HunYuan、元宝、CodeBuddy 等）的触达效率
  supports_if: AI 产品矩阵通过微信生态持续获客 + 企业微信渗透提升
  weakens_if: 微信生态监管收紧或反垄断限制
  cannot_prove: 微信身份入口必然带来云业务定价权
  alternative_model: 监管限制微信对 AI 产品的导流，控制面优势受限
  source_refs:
    - 05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/260730CSP消费端拐点_完整研究_AI长报告原文.md
  latest_moment: MOM-260730-AI-CSP-RESEARCH-01
```

## 资金分账

| 项目 | 含义 | 不能混成什么 |
|---|---|---|
| Business Services 收入 | 含云+会议+企业微信+电商 TOS | 不是纯云收入，云占比未单独披露 |
| FCF | 集团自由现金流 | 不是云业务 FCF |
| 净现金 | 现金+短期投资-有息负债 | 不是经营造血 |
| AI 投入 | 影响 non-IFRS 利润 RMB 8.8B | 不是云业务成本，含集团 AI 全投入 |
| 回购 | 2026 大幅削减 | 不能既当成股东回报又当成 AI 投入 |

## 当前研究层判断

- 协议 H_B 业务票：posterior [0.65, 0.82, 0.92]（强）
- 协议 H_P 利润捕获票：posterior [0.60, 0.79, 0.89]（**通过 0.65 阈值**）
- 协议 H_R 回报票：posterior [0.50, 0.60, 0.72]（临界，未稳超 0.60）
- 协议 H_T 时点票：posterior [0.50, 0.60, 0.70]（临界，未稳超 0.55）
- 研究层分类：**B 类「可考虑小规模试探仓位」**

## 验证窗口

- 26Q2 财报（约 2026-08 中）：Business Services 是否维持 20% + FCF 是否维持 +20% + AI 投入变现路径 + 回购实际规模
- 升级为 A 类（方向仓）的信号：26Q2 FCF 增速 > 25%、Business Services > 22%、海外云 > 40%、AI 拖累持平或下降、回购 > RMB 80B/年、南向持续流入
- 失效降为 C 的信号：26Q2 FCF < 10%、Business Services < 12%、海外云 < 20%、AI 拖累扩大、回购 < RMB 30B、港股流出

## 关联

- 协议：`03_STATE/DOMAIN_MODELS/AI/AI_CSP_domain_knowledge_codex_protocol_v1.md`
- 主长报告：`05_EVIDENCE_META/ARCHIVE/AI_LONG_REPORTS/260730CSP消费端拐点_完整研究_AI长报告原文.md`
- AI Domain：`05_EVIDENCE_META/KNOWLEDGE/DOMAINS/AI/README.md`
- ETF 513050 实体知识：`05_EVIDENCE_META/KNOWLEDGE/ENTITIES/ETFS/513050.md`（腾讯占 32.34% 权重）
- 无 current thesis 卡（B 类未达"方向仓"，暂不创建正式 thesis 卡）
