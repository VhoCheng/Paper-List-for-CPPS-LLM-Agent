# Graph Computation + LLM / Graph 计算 + LLM 技术探索

Snapshot: **2026-11-01**.

The following subsections separate exact graph computation, learned graph representations, knowledge retrieval, and power-system applications. A graph-derived explanation is not a proof of AC feasibility. Entries keep the original `year / venue / title / links` format. Cross-listed items do not create duplicate data records.

本章区分图算法/结构推理、GNN–LLM 融合、知识图谱检索以及电网应用。文末两条跨章节关联保留同一记录 ID，不重复计数。

### Surveys and Design Principles / 综述与设计原则

1. 🟡 [26'arXiv] | Are Large Language Models Suitable for Graph Computation? Progress and Prospects | [[paper]](https://arxiv.org/abs/2606.06865) | [[PDF]](https://arxiv.org/pdf/2606.06865)
2. 🟡 [26'arXiv] | Integrating Graphs, Large Language Models, and Agents: Reasoning and Retrieval | [[paper]](https://arxiv.org/abs/2604.15951) | [[PDF]](https://arxiv.org/pdf/2604.15951)
3. 🟡 [26'arXiv] | LLMs+Graphs: Toward Graph-Native, Synergistic AI Systems | [[paper]](https://arxiv.org/abs/2606.11560) | [[PDF]](https://arxiv.org/pdf/2606.11560)
4. 🟢 [26'Frontiers of Computer Science] | Position: How can Graphs Help Large Language Models? | [[paper]](https://doi.org/10.1007/s11704-026-51651-6) | [[arXiv]](https://arxiv.org/abs/2605.02452) | [[PDF]](https://arxiv.org/pdf/2605.02452)
5. 🟢 [24'IEEE Transactions on Knowledge and Data Engineering] | Large Language Models on Graphs: A Comprehensive Survey | [[paper]](https://doi.org/10.1109/TKDE.2024.3469578) | [[arXiv]](https://arxiv.org/abs/2312.02783) | [[PDF]](https://arxiv.org/pdf/2312.02783) | [[code]](https://github.com/PeterGriffinJin/Awesome-Language-Model-on-Graphs)
6. 🟢 [24'IEEE Transactions on Knowledge and Data Engineering] | Unifying Large Language Models and Knowledge Graphs: A Roadmap | [[paper]](https://doi.org/10.1109/TKDE.2024.3352100) | [[arXiv]](https://arxiv.org/abs/2306.08302) | [[PDF]](https://arxiv.org/pdf/2306.08302)

### Graph Computation, Encoding, and Benchmarks / 图计算、编码与基准

1. 🟡 [26'arXiv] | GABench: A Comprehensive Benchmark for Evaluating LLM Agents on Graph Analysis Tasks | [[paper]](https://arxiv.org/abs/2608.01684) | [[PDF]](https://arxiv.org/pdf/2608.01684)
2. 🟡 [26'arXiv] | GraphInfer-Bench: Benchmarking LLM's Inference Capability on Graphs | [[paper]](https://arxiv.org/abs/2606.11562) | [[PDF]](https://arxiv.org/pdf/2606.11562)
3. 🟡 [26'arXiv] | Language-encoded network topology enables large language models to reason about complex networks | [[paper]](https://arxiv.org/abs/2609.03229) | [[PDF]](https://arxiv.org/pdf/2609.03229)
4. 🟢 [25'ICLR] | GraphArena: Evaluating and Exploring Large Language Models on Graph Computation | [[paper]](https://openreview.net/forum?id=Y1r9yCMzeA) | [[arXiv]](https://arxiv.org/abs/2407.00379) | [[PDF]](https://arxiv.org/pdf/2407.00379) | [[code]](https://github.com/squareRoot3/GraphArena)
5. 🟢 [24'ACM KDD] | GraphWiz: An Instruction-Following Language Model for Graph Computational Problems | [[paper]](https://doi.org/10.1145/3637528.3672010) | [[arXiv]](https://arxiv.org/abs/2402.16029) | [[PDF]](https://arxiv.org/pdf/2402.16029)
6. 🟢 [24'ICLR] | Talk like a Graph: Encoding Graphs for Large Language Models | [[paper]](https://research.google/pubs/talk-like-a-graph-encoding-graphs-for-large-language-models/) | [[arXiv]](https://arxiv.org/abs/2310.04560) | [[PDF]](https://arxiv.org/pdf/2310.04560)
7. 🟢 [23'NeurIPS] | Can Language Models Solve Graph Problems in Natural Language? | [[paper]](https://arxiv.org/abs/2305.10037) | [[PDF]](https://arxiv.org/pdf/2305.10037) | [[code]](https://github.com/Arthur-Heng/NLGraph)

### GNN–LLM Alignment and Fusion / GNN 与 LLM 对齐融合

1. 🟢 [25'ISWC] | The Graph Language: How Knowledge Graphs Speak to Large Language Models | [[paper]](https://doi.org/10.1007/978-3-032-09527-5_33) | [[arXiv]](https://arxiv.org/abs/2608.01175) | [[PDF]](https://arxiv.org/pdf/2608.01175) | [[code]](https://github.com/giuseppepirro/gralan)
2. 🟢 [24'ACM SIGIR] | GraphGPT: Graph Instruction Tuning for Large Language Models | [[paper]](https://doi.org/10.1145/3626772.3657775) | [[arXiv]](https://arxiv.org/abs/2310.13023) | [[PDF]](https://arxiv.org/pdf/2310.13023) | [[code]](https://github.com/HKUDS/GraphGPT)
3. 🟢 [24'ICLR] | Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning | [[paper]](https://openreview.net/forum?id=RXFVcynVe1) | [[arXiv]](https://arxiv.org/abs/2305.19523) | [[PDF]](https://arxiv.org/pdf/2305.19523) | [[code]](https://github.com/XiaoxinHe/TAPE)
4. 🟢 [24'ICML] | LLaGA: Large Language and Graph Assistant | [[paper]](https://proceedings.mlr.press/v235/chen24bh.html) | [[arXiv]](https://arxiv.org/abs/2402.08170) | [[PDF]](https://arxiv.org/pdf/2402.08170) | [[code]](https://github.com/VITA-Group/LLaGA)

### GraphRAG, Graph Reasoning, and Evidence Memory / 图检索、推理与证据记忆

1. 🟡 [26'arXiv] | GraphRAG-LTM: A Layered Threat Modeling Framework for Attacks on Graph Retrieval-Augmented Generation | [[paper]](https://arxiv.org/abs/2610.19549) | [[PDF]](https://arxiv.org/pdf/2610.19549)
2. 🟡 [26'arXiv] | GraphRAGProv: GraphRAG Meets How-Provenance | [[paper]](https://arxiv.org/abs/2610.37237) | [[PDF]](https://arxiv.org/pdf/2610.37237)
3. 🟡 [26'arXiv] | LADDER: Graph-Guided Diffusion Language Models for Efficient Multi-Hop Reasoning | [[paper]](https://arxiv.org/abs/2609.24346) | [[PDF]](https://arxiv.org/pdf/2609.24346)
4. 🟡 [26'arXiv] | STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents | [[paper]](https://arxiv.org/abs/2610.19386) | [[PDF]](https://arxiv.org/pdf/2610.19386)
5. 🟡 [26'arXiv] | When Is Graph Structure Worth Its Cost? The Case for Structure Pricing in Retrieval-Augmented Generation | [[paper]](https://arxiv.org/abs/2609.18099) | [[PDF]](https://arxiv.org/pdf/2609.18099)
6. 🟢 [25'ICML] | From RAG to Memory: Non-Parametric Continual Learning for Large Language Models | [[paper]](https://proceedings.mlr.press/v267/gutierrez25a.html) | [[arXiv]](https://arxiv.org/abs/2502.14802) | [[PDF]](https://arxiv.org/pdf/2502.14802) | [[code]](https://github.com/OSU-NLP-Group/HippoRAG)
7. 🟢 [25'Findings of ACL] | GNN-RAG: Graph Neural Retrieval for Efficient Large Language Model Reasoning on Knowledge Graphs | [[paper]](https://aclanthology.org/2025.findings-acl.856/) | [[arXiv]](https://arxiv.org/abs/2405.20139) | [[PDF]](https://arxiv.org/pdf/2405.20139) | [[code]](https://github.com/cmavro/GNN-RAG)
8. 🟢 [25'Findings of EMNLP] | LightRAG: Simple and Fast Retrieval-Augmented Generation | [[paper]](https://aclanthology.org/2025.findings-emnlp.568/) | [[arXiv]](https://arxiv.org/abs/2410.05779) | [[PDF]](https://arxiv.org/pdf/2410.05779) | [[code]](https://github.com/HKUDS/LightRAG)
9. 🟡 [24'arXiv] | From Local to Global: A Graph RAG Approach to Query-Focused Summarization | [[paper]](https://arxiv.org/abs/2404.16130) | [[PDF]](https://arxiv.org/pdf/2404.16130) | [[code]](https://github.com/microsoft/graphrag)
10. 🟢 [24'NeurIPS] | G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering | [[paper]](https://proceedings.neurips.cc/paper_files/paper/2024/hash/efaf1c9726648c8ba363a5c927440529-Abstract-Conference.html) | [[arXiv]](https://arxiv.org/abs/2402.07630) | [[PDF]](https://arxiv.org/pdf/2402.07630) | [[code]](https://github.com/XiaoxinHe/G-Retriever)
11. 🟢 [24'AAAI] | Graph of Thoughts: Solving Elaborate Problems with Large Language Models | [[paper]](https://doi.org/10.1609/aaai.v38i16.29720) | [[arXiv]](https://arxiv.org/abs/2308.09687) | [[PDF]](https://arxiv.org/pdf/2308.09687)
12. 🟢 [24'NeurIPS] | HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models | [[paper]](https://arxiv.org/abs/2405.14831) | [[PDF]](https://arxiv.org/pdf/2405.14831) | [[code]](https://github.com/OSU-NLP-Group/HippoRAG)
13. 🟢 [24'ICLR] | Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning | [[paper]](https://arxiv.org/abs/2310.01061) | [[PDF]](https://arxiv.org/pdf/2310.01061)
14. 🟢 [24'ICLR] | Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph | [[paper]](https://arxiv.org/abs/2307.07697) | [[PDF]](https://arxiv.org/pdf/2307.07697)

### Power-System Explorations / 电力系统探索

1. 🟡 [26'arXiv] | Foundation Models Meet Power Grid Topology for Cascade Prediction | [[paper]](https://arxiv.org/abs/2610.32696) | [[PDF]](https://arxiv.org/pdf/2610.32696)
2. 🟡 [26'arXiv] | Seed-Anchored Budget-Bounded Graph Rendering for Question Answering on Industry-Standard Power-Grid Information and Exchange Models | [[paper]](https://arxiv.org/abs/2609.02011) | [[PDF]](https://arxiv.org/pdf/2609.02011)
3. 🟢 [26'2026 6th Power System and Green Energy Conference (PSGEC)] | TSAC-RAG: Type- and Structure-Aware Constraint Retrieval for Question Answering over Power-System Standards | [[paper]](https://doi.org/10.1109/PSGEC70194.2026.11719172)

### Cross-listed power-system papers / 跨章节关联

1. 🟢 [26'IEEE Transactions on Smart Grid — Early Access] | STDeepSeek: Continual Learning Enhanced Spatiotemporal Large Language Model for Load Forecasting of Electric Vehicle Charging Stations | [[paper]](https://doi.org/10.1109/TSG.2026.3725028)
2. 🟢 [25'IEEE Transactions on Power Systems] | PowerGraph-LLM: Novel Power Grid Graph Embedding and Optimization With Large Language Models | [[paper]](https://doi.org/10.1109/TPWRS.2025.3596774) | [[arXiv]](https://arxiv.org/abs/2501.07639) | [[PDF]](https://arxiv.org/pdf/2501.07639)

For application boundaries and a reading order, see [the updated research map](RELATED_WORK_MAP.md).
