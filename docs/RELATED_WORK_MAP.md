# Related-Work Map for PhysChronoGrid — 2026-11-01

The interpretation below is a literature-based research guide, not evidence that any planned experiment has been completed. Results on different datasets and task definitions are not directly comparable.

## 1. Closest work / 建议优先阅读

| Work | What it studies | Relevance and boundary |
|---|---|---|
| [LLMs and Agentic AI Systems for Smart Grids](https://arxiv.org/abs/2607.18147), 2026 | Solver-grounded agents for forecasting, EV charging, power flow and diagnosis; explicit verification | “LLM 调用工具 + 物理校验”已有直接先例。创新应落实到预警时间窗、事件归因、证据链和动作后约束检查。 |
| [PowerAgentBench-SS](https://arxiv.org/abs/2606.18789), 2026 | Hidden physical evaluator, risk-sensitive metrics and evidence-backed reports; DC thermal contingency pilot | 借鉴 false-safe、证据支持与预算利用指标；其 DC 试验不等于 AC 配电恢复。 |
| [RestoreBench](https://arxiv.org/abs/2609.00384), 2026 | Agents repair non-convergent power-flow cases | 潮流收敛修复和故障后供电恢复是不同任务。借鉴失败原因记录，不混用成功率。 |
| [PowerBench](https://arxiv.org/abs/2609.34492), 2026 | Heterogeneous operational evidence retrieval and reasoning using synthetic data | 适合比较遥测、设备和文档的证据检索；不能描述为实网部署验证。 |
| [CONDUCTOR](https://arxiv.org/abs/2606.24609), 2026 | Distribution digital twin with uncertainty-aware studies and calibrated refusal | 与不确定性、调度建议、工具证据和拒答存在直接重叠。 |
| [Explainable Post-Disaster Grid Observability Recovery](https://arxiv.org/abs/2609.16774), 2026 | PMU restoration tools, traceable explanations and operator oversight | 人工监督与可追溯恢复解释已有先例；PMU 可观测性恢复不同于配电负荷恢复。 |
| [Foundation Models Meet Power Grid Topology for Cascade Prediction](https://arxiv.org/abs/2610.32696), 2026 | Confidence-gated graph/LLM fusion for cascade-severity prediction and transfer | 是 Graph + LLM、拓扑泛化与风险预测的直接近邻；输电级联预测不等于配电故障定位或动作安全验证。 |
| [Seed-Anchored Budget-Bounded Graph Rendering](https://arxiv.org/abs/2609.02011), 2026 | Budget-limited CIM/CGMES topology evidence for LLM QA | 可借鉴保留关键拓扑证据；属于电网问答/检索，不是潮流求解。 |
| [PowerGraph-LLM](https://doi.org/10.1109/TPWRS.2025.3596774), TPWRS 2025 | Power-grid graph embedding and LLM optimization | 原 SafePowerGraph-LLM 的正式版；电网图嵌入 + LLM 概念本身不能再作为新颖性声明。 |
| [STDeepSeek](https://doi.org/10.1109/TSG.2026.3725028), TSG 2026 | Graph-constrained spatiotemporal LLM adaptation for EV-station forecasting | 关注空间依赖、轻量适配与持续学习；预测精度、诊断与安全能力分别评估。 |

## 2. Graph + LLM 技术路线

| Route | Representative work | Useful for | Boundary |
|---|---|---|---|
| LLM plans; graph tools execute | [GraphArena](https://arxiv.org/abs/2407.00379), [GABench](https://arxiv.org/abs/2608.01684), [graph-computation survey](https://arxiv.org/abs/2606.06865) | Connectivity, shortest paths, components, candidate screening and tool evaluation | 正确的自然语言不等于精确图算法结果或 AC 可行性。 |
| GNN–LLM alignment/fusion | [GraphGPT](https://doi.org/10.1145/3626772.3657775), [LLaGA](https://proceedings.mlr.press/v235/chen24bh.html), [G-Retriever](https://arxiv.org/abs/2402.07630) | Topology representations and graph QA | 文本属性图上的效果不能自动外推到电气网络。 |
| Knowledge graph / GraphRAG | [GraphRAG](https://arxiv.org/abs/2404.16130), [LightRAG](https://aclanthology.org/2025.findings-emnlp.568/), [GNN-RAG](https://aclanthology.org/2025.findings-acl.856/), [HippoRAG 2](https://proceedings.mlr.press/v267/gutierrez25a.html) | Rules, equipment documents and event histories | 文档语义关系不一定是电气连接，需标注来源和关系类型。 |
| Provenance and robustness | [GraphRAGProv](https://arxiv.org/abs/2610.37237), [GraphRAG-LTM](https://arxiv.org/abs/2610.19549) | Trace claims to evidence; test retrieval/graph corruption | 来源可追踪不保证提取正确，也不保证动作物理安全。 |
| Native electrical topology + LLM | [CIM/CGMES rendering](https://arxiv.org/abs/2609.02011), [cascade prediction](https://arxiv.org/abs/2610.32696), [PowerGraph-LLM](https://doi.org/10.1109/TPWRS.2025.3596774) | Bus/branch identity, electrical adjacency and risk context | 各论文研究任务不同，不应拼接为统一性能榜。 |

A useful design hypothesis for PhysChronoGrid is to distinguish **electrical topology**, **document knowledge**, and **event/evidence relations**, with explicit mappings. Whether this improves traceability or performance must be tested; it is not an established result of this catalog.

## 3. Suggested reading order / 阅读顺序

1. Smart-grid agent tutorial → CONDUCTOR → PowerAgentBench-SS: establish what verified workflows already cover.
2. Graph-computation survey → GraphArena → GABench: separate planning from exact execution.
3. PowerGraph-LLM → STDeepSeek → cascade-prediction fusion: study electrical applications.
4. CIM/CGMES rendering → G-Retriever → GNN-RAG: choose topology/evidence interfaces.
5. GraphRAGProv → GraphRAG-LTM: study provenance and robustness.
6. RestoreBench → PowerBench: refine failure accounting and evidence-retrieval metrics.

## 4. Candidate experiments / 可考虑的对照

- **Topology:** plain text/edge list, deterministic graph-tool outputs, learned graph embedding, and retrieved graph evidence. Hold the LLM and information/token budget fixed where possible.
- **Retrieval:** no retrieval, vector RAG, knowledge-graph RAG, native topology-aware retrieval. Separate document-retrieval effects from electrical-topology effects.
- **Agent architecture:** deterministic solver + template, single agent + tools, multi-agent + tools, full framework. Use the same action space and validation budget.
- **Verification:** report source traceability, graph consistency, AC convergence, voltage/thermal constraints and served-load changes separately. Solver failure is not automatically an unsafe action or failed restoration.
- **Generalization:** hold out topologies/event families; distinguish zero-shot and calibrated transfer. Keep final-test data outside development.
- **Failure behavior:** unsupported claims, wrong evidence, invalid arguments, false-safe decisions, abstention/escalation, latency and tool/token cost.

Select experiments according to the final research question and available data; this is not a requirement to implement every cataloged method.

## 5. Novelty boundary

Avoid “the first LLM agent for power systems,” “the first graph + LLM power model,” or “the first solver-verified agent.” Contributions must specify the task, horizon, event model, evidence interface, post-action physical checks and evaluation protocol, then show gains over relevant baselines.

The July 2026 map's broad gap statement is not retained as an established fact. New agent, graph-fusion and verification papers narrow that boundary. Assessing the final combination's novelty requires comparing full methods and experiments, not only titles and abstracts.
