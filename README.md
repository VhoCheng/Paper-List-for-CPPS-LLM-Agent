# ⚡ Awesome PhysChronoGrid Papers

> A curated paper list for **LLM agents, multi-horizon forecasting, graph learning, cyber-physical diagnosis, physics-guided verification, and trustworthy decision support in power systems**.

![Papers](https://img.shields.io/badge/records-224-2F80ED) ![IEEE Transactions](https://img.shields.io/badge/IEEE%20Transactions-43-C0392B) ![Code](https://img.shields.io/badge/code%20links-74-27AE60) ![Updated](https://img.shields.io/badge/updated-2026--11--01-6C5CE7) ![License](https://img.shields.io/badge/license-MIT-brightgreen)

This repository was built for the **PhysChronoGrid** research line, but it is designed as a reusable public reading list. It prioritizes peer-reviewed work in IEEE Transactions and other primary venues, while retaining clearly labeled preprints for fast-moving LLM/agent research.

- **🟢 Published / peer-reviewed or official conference record**
- **🟡 Preprint / white paper**
- `core`: directly overlaps with the PhysChronoGrid problem setting
- `supporting`: supplies models, evaluation methods, physics, or benchmarks

A Chinese guide is available in [README_CN.md](README_CN.md). Machine-readable records are in [data/papers.csv](data/papers.csv) and [data/papers.json](data/papers.json).

**Update 2026-11-01:** 68 added records; 6 existing records corrected or upgraded. 34 new Graph + LLM records plus 2 cross-listed power papers. See [update notes](docs/UPDATE_2026-11-01_CN.md), [verification metadata](data/verification_2026-11-01.json), and the [standalone Graph + LLM chapter](docs/GRAPH_LLM.md).

Counts refer to catalog records, not guaranteed distinct studies: the inherited PowerChain preprint P029 and published record P016 are explicitly retained as linked versions. Unchanged legacy entries have not all been re-verified in this update.

## Contents

1. [Surveys, Perspectives, and Research Agendas](#surveys)
2. [LLM Agents for Power-System Analysis and Simulation](#power_llm_agents)
3. [LLMs for Dispatch, Control, Markets, and Optimization](#power_llm_decision)
4. [LLMs and Foundation Models for Energy Forecasting](#power_llm_forecasting)
5. [General Time-Series Forecasting Models](#time_series)
6. [Graph and Spatio-Temporal Learning for Power Systems](#graph_power)
7. [Physics-Guided Learning, Safe Control, and Verification](#physics_safe)
8. [Cyber-Physical Anomaly Detection and Fault Diagnosis](#cyber_fault)
9. [Explainability, Reports, and Human Oversight](#xai_human)
10. [Benchmarks, Test Systems, Datasets, and Simulators](#benchmarks)
11. [Graph Computation + LLM: Methods, Benchmarks, and Power-System Explorations](#graph_llm)
12. [IEEE Transactions Spotlight](#transactions-spotlight)
13. [Research map for PhysChronoGrid](docs/RELATED_WORK_MAP.md)
14. [Search and verification protocol](docs/SEARCH_STRATEGY.md)
15. [Update notes (中文)](docs/UPDATE_2026-11-01_CN.md)

<a id="surveys"></a>
## Surveys, Perspectives, and Research Agendas

1. 🟢 [26'Frontiers in Artificial Intelligence] | Agentic AI Systems in Electrical Power Systems Engineering: Current State-of-the-Art and Challenges | [[paper]](https://doi.org/10.3389/frai.2026.1814651)
2. 🟡 [26'arXiv] | Agentic Artificial Intelligence for Power Systems: Strategies to Identify and Close Capability Gaps | [[paper]](https://arxiv.org/abs/2607.28822) | [[PDF]](https://arxiv.org/pdf/2607.28822)
3. 🟡 [26'arXiv] | Engineering Trustworthy Agentic AI for Critical Systems | [[paper]](https://arxiv.org/abs/2607.18548) | [[PDF]](https://arxiv.org/pdf/2607.18548)
4. 🟢 [26'International Journal of Electrical Power & Energy Systems] | Large Language Model-Based Power Dispatch Agent: Framework, Application and Challenges | [[paper]](https://doi.org/10.1016/j.ijepes.2026.111653)
5. 🟡 [26'arXiv] | LLMs and Agentic AI Systems for Smart Grids: A Tutorial on Architectures and Applications | [[paper]](https://arxiv.org/abs/2607.18147) | [[PDF]](https://arxiv.org/pdf/2607.18147)
6. 🟢 [26'Communications Engineering] | Operating Smart Grids by Customizing Large Model Agents | [[paper]](https://doi.org/10.1038/s44172-026-00709-1)
7. 🟢 [26'iEnergy] | Toward AI-Pervasive Electric Energy Systems: Concept, Framework, Vulnerability, and Visions | [[paper]](https://www.sciencedirect.com/science/article/pii/S2950160126000021)
8. 🟢 [26'IEEE Transactions on Smart Grid] | Vision of Future Smart Control Center: Fusion of Large Language Models and Power System Intelligent Computing | [[paper]](https://doi.org/10.1109/TSG.2026.3717716)
9. 🟢 [25'IEEE Access] | A Comprehensive Review on the Application of Large Language Models (LLMs) in Power Systems | [[paper]](https://doi.org/10.1109/ACCESS.2025.3637226)
10. 🟢 [25'IEEE Access] | A Review of Large Language Models for Energy Systems: Applications, Challenges, and Future Prospects | [[paper]](https://ieeexplore.ieee.org/document/11168242)
11. 🟡 [25'arXiv] | Large Language Models for Power System Applications: A Comprehensive Literature Survey | [[paper]](https://arxiv.org/abs/2512.13004)
12. 🟢 [24'IEEE Transactions on Smart Grid] | Applying Large Language Models to Power Systems: Potential Security Threats | [[paper]](https://doi.org/10.1109/TSG.2024.3373256)
13. 🟢 [24'IEEE Access] | Incipient Fault Detection in Power Distribution Networks: Review, Analysis, Challenges, and Future Directions | [[paper]](https://ieeexplore.ieee.org/document/10636132)
14. 🟢 [23'IEEE Access] | Review of Emerging Concepts in Distribution System State Estimation: Opportunities and Challenges | [[paper]](https://ieeexplore.ieee.org/document/10173492)
15. 🟢 [22'Energy and AI] | Explainable Artificial Intelligence (XAI) Techniques for Energy and Power Systems: Review, Challenges and Opportunities | [[paper]](https://doi.org/10.1016/j.egyai.2022.100169)
16. 🟢 [22'IEEE Power & Energy Magazine] | Successful Applications and Future Challenges of Machine Learning for Power Systems: A Summary of Recent Activities by the IEEE WG on Machine Learning for Power Systems | [[paper]](https://ieeexplore.ieee.org/document/9979649)
17. 🟢 [21'CSEE Journal of Power and Energy Systems] | A Review of Graph Neural Networks and Their Applications in Power Systems | [[paper]](https://ieeexplore.ieee.org/document/9520300)
18. 🟢 [20'IET Smart Grid] | Survey of Machine Learning Methods for Detecting False Data Injection Attacks in Power Systems | [[paper]](https://doi.org/10.1049/iet-stg.2020.0015)
19. 🟢 [17'IEEE Transactions on Smart Grid] | A Review of False Data Injection Attacks Against Modern Power Systems | [[paper]](https://doi.org/10.1109/TSG.2015.2495133)

<a id="power_llm_agents"></a>
## LLM Agents for Power-System Analysis and Simulation

1. 🟢 [26'IEEE Transactions on Smart Grid — Early Access] | A Large Language Model-Based Framework for Automated Dynamic Simulation of Power Systems | [[paper]](https://doi.org/10.1109/TSG.2026.3731592)
2. 🟡 [26'arXiv] | A Novel Method for Differential-Algebraic Dynamic Model Discovery in Power Systems: An LLM-Based Multi-Agent Collaborative Framework | [[paper]](https://arxiv.org/abs/2606.31314) | [[PDF]](https://arxiv.org/pdf/2606.31314)
3. 🟡 [26'arXiv] | Agentic Application in Power Grid Static Analysis: Automatic Code Generation and Error Correction | [[paper]](https://arxiv.org/abs/2604.09995) | [[PDF]](https://arxiv.org/pdf/2604.09995)
4. 🟡 [26'arXiv] | CONDUCTOR: An LLM-Orchestrated Digital Twin for Uncertainty-Aware Distribution Grid Operations | [[paper]](https://arxiv.org/abs/2606.24609) | [[PDF]](https://arxiv.org/pdf/2606.24609)
5. 🟢 [26'2026 6th Power System and Green Energy Conference (PSGEC)] | Design and Implementation of a Large Language Model-Driven Electromagnetic Transient Simulation System Based on the Model Context Protocol | [[paper]](https://doi.org/10.1109/PSGEC70194.2026.11719174)
6. 🟡 [26'Research Square] | Grid CoPilot: A Large Language Model (LLM) Based Framework for Transforming Long-Term Planning Analyses | [[paper]](https://doi.org/10.21203/rs.3.rs-6467790/v1)
7. 🟡 [26'arXiv] | Grid-Mind: An LLM-Orchestrated Multi-Fidelity Agent for Automated Connection Impact Assessment | [[paper]](https://arxiv.org/abs/2602.20683)
8. 🟢 [26'IEEE Open Access Journal of Power and Energy] | Grid-Orch: An LLM-Powered Orchestrator for Distribution Grid Simulation and Analytics | [[paper]](https://doi.org/10.1109/OAJPE.2026.3721083) | [[arXiv]](https://arxiv.org/abs/2605.12728) | [[PDF]](https://arxiv.org/pdf/2605.12728)
9. 🟢 [26'KDD 2026 Workshop: SciSoc Agents & LLMs] | GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment | [[paper]](https://openreview.net/forum?id=Cs5TBzzNym)
10. 🟢 [26'Advanced Engineering Informatics (online 2026; issue 2027) — Early Access] | Knowledge boundary probing and demand-guided intervention for LLM-based power system code generation | [[paper]](https://doi.org/10.1016/j.aei.2026.105328) | [[arXiv]](https://arxiv.org/abs/2605.31478) | [[PDF]](https://arxiv.org/pdf/2605.31478)
11. 🟢 [26'IEEE Transactions on Smart Grid] | Large Language Model Powered Automated Modeling and Optimization of Active Distribution Network Dispatch Problems | [[paper]](https://doi.org/10.1109/TSG.2025.3621438) | [[arXiv]](https://arxiv.org/abs/2507.21162) | [[PDF]](https://arxiv.org/pdf/2507.21162)
12. 🟡 [26'arXiv] | Orchestrating Power Grid Studies with Multi-Agent AI and MCP Servers | [[paper]](https://arxiv.org/abs/2607.14158) | [[code]](https://github.com/powsybl/pypowsybl)
13. 🟡 [26'arXiv] | PFAgent: A Tractable and Self-Evolving Power-Flow Agent for Interactive Grid Analysis | [[paper]](https://arxiv.org/abs/2604.10846) | [[PDF]](https://arxiv.org/pdf/2604.10846)
14. 🟢 [26'Electric Power Systems Research] | PowerChain: A Verifiable Agentic AI System for Automating Distribution Grid Analyses | [[paper]](https://www.sciencedirect.com/science/article/pii/S0378779626008485) | [[code]](https://github.com/emmanuelbadmus/powerchain)
15. 🟡 [26'arXiv] | Skill-Based AI Agents for Power-System Studies | [[paper]](https://arxiv.org/abs/2609.40272) | [[PDF]](https://arxiv.org/pdf/2609.40272)
16. 🟢 [26'IEEE Texas Power and Energy Conference] | Testing Fine-Tuned Large Language Models for Power System Analysis | [[paper]](https://doi.org/10.1109/TPEC67884.2026.11513194)
17. 🟡 [26'arXiv] | VeraGrid-Agent: Tool-Augmented LLMs for Distribution Optimal Power Flow at the Grid Edge | [[paper]](https://arxiv.org/abs/2607.25155) | [[PDF]](https://arxiv.org/pdf/2607.25155)
18. 🟢 [25'IEEE Transactions on Smart Grid] | Enhancing LLMs for Power System Simulations: A Feedback-Driven Multi-Agent Framework | [[paper]](https://doi.org/10.1109/TSG.2025.3589114)
19. 🟡 [25'arXiv] | Grid-Agent: An LLM-Powered Multi-Agent System for Power Grid Control | [[paper]](https://arxiv.org/abs/2508.05702) | [[PDF]](https://arxiv.org/pdf/2508.05702)
20. 🟡 [25'arXiv] | GridMind: LLMs-Powered Agents for Power System Analysis and Operations | [[paper]](https://arxiv.org/abs/2509.02494)
21. 🟢 [25'NAACL] | LLM4DistReconfig: A Fine-Tuned Large Language Model for Power Distribution Network Reconfiguration | [[paper]](https://aclanthology.org/2025.naacl-long.208/) | [[code]](https://github.com/panaschristou/LLM4DistReconfig)
22. 🟢 [25'IEEE PES ISGT Europe] | Power System Model Conversion Using Large Language Models | [[paper]](https://doi.org/10.1109/ISGTEUROPE64741.2025.11305583)
23. 🟡 [25'arXiv] | PowerChain: Automating Distribution Grid Analysis with Agentic AI Workflows | [[paper]](https://arxiv.org/abs/2508.17094) | [[code]](https://github.com/emmanuelbadmus/powerchain)
24. 🟢 [25'Patterns] | RePower: An LLM-Driven Autonomous Platform for Power System Data-Guided Research | [[paper]](https://doi.org/10.1016/j.patter.2025.101211)
25. 🟡 [25'arXiv] | X-GridAgent: An LLM-Powered Agentic AI System for Assisting Power Grid Analysis | [[paper]](https://arxiv.org/abs/2512.20789)
26. 🟢 [24'IEEE EnergyVis] | ChatGrid: Power Grid Visualization Empowered by a Large Language Model | [[paper]](https://doi.org/10.1109/EnergyVis63885.2024.00007)
27. 🟡 [24'arXiv] | Enabling Large Language Models to Perform Power System Simulations With Previously Unseen Tools: A Case of Daline | [[paper]](https://arxiv.org/abs/2406.17215)
28. 🟢 [24'IEEE PES General Meeting] | Large Foundation Models for Power Systems | [[paper]](https://arxiv.org/abs/2312.07044) | [[code]](https://github.com/chennnnnyize/llm_powersystems)
29. 🟡 [23'arXiv] | LLM-Based Frameworks for Power Engineering From Routine to Novel Tasks | [[paper]](https://arxiv.org/abs/2305.11202)

<a id="power_llm_decision"></a>
## LLMs for Dispatch, Control, Markets, and Optimization

1. 🟢 [26'IEEE Transactions on Power Systems] | Customising Electricity Contracts at Scale With Large Language Models | [[paper]](https://doi.org/10.1109/TPWRS.2026.3670536)
2. 🟡 [26'arXiv] | Large Language Models as Strategic Bidding Agents in P2P Energy Trading Markets | [[paper]](https://arxiv.org/abs/2609.05462) | [[PDF]](https://arxiv.org/pdf/2609.05462)
3. 🟢 [26'IEEE Transactions on Smart Grid — Early Access] | LLM-Empowered Decision-Focused Learning for the Operation of Local Energy Communities | [[paper]](https://doi.org/10.1109/TSG.2026.3678781)
4. 🟡 [26'arXiv] | LLM-Enhanced Multi-Agent Reinforcement Learning for Unified Electric Vehicles-Charging Station-Grid Optimization in Public Charging Systems | [[paper]](https://arxiv.org/abs/2609.13805) | [[PDF]](https://arxiv.org/pdf/2609.13805)
5. 🟢 [26'IEEE Transactions on Smart Grid] | LLM-Enhanced Multi-Agent Reinforcement Learning With Expert Workflow for Real-Time P2P Energy Trading | [[paper]](https://doi.org/10.1109/TSG.2026.3684885)
6. 🟡 [26'arXiv] | LLMs are Few-Shot Decision-Makers: Generalized Context-Aware Microgrid Frequency Control through Prompt Decision Transformer | [[paper]](https://arxiv.org/abs/2608.21858) | [[PDF]](https://arxiv.org/pdf/2608.21858)
7. 🟢 [26'IEEE Transactions on Industrial Informatics — Early Access] | Multiobjective Optimization of Data Center Microgrids via Large Language Model-Assisted Deep Reinforcement Learning | [[paper]](https://doi.org/10.1109/TII.2026.3725105)
8. 🟡 [26'arXiv] | PowerAtlas: Feasibility-Aware Language Models for Electricity-Computing Co-Scheduling | [[paper]](https://arxiv.org/abs/2607.26710) | [[PDF]](https://arxiv.org/pdf/2607.26710) | [[code]](https://github.com/JAVA-Jiang/PowerAtlas)
9. 🟡 [26'Preprints] | XRL-LLM: Explainable Reinforcement Learning Framework for Voltage Control | [[paper]](https://www.preprints.org/manuscript/202603.1131)
10. 🟢 [25'Scientific Reports] | A Large Language Model for Advanced Power Dispatch | [[paper]](https://doi.org/10.1038/s41598-025-91940-x)
11. 🟢 [25'IEEE ICPIES] | A Large Language Model-Based Agent for Automated Bidding Strategy Generation in Electricity Markets | [[paper]](https://doi.org/10.1109/ICPIES65420.2025.11070004)
12. 🟡 [25'arXiv] | Can Large Language Model Agents Balance Energy Systems? | [[paper]](https://arxiv.org/abs/2502.10557)
13. 🟢 [25'Smart Energy Systems Research] | Large Language Model for Secure Operation of Power Systems | [[paper]](https://doi.org/10.70322/sesr.2025.10005)
14. 🟢 [25'IEEE Transactions on Industrial Informatics] | Optimization of Energy and Carbon Emissions in Integrated Energy System Based on Deep Reinforcement Learning Assisted by Large Language Model | [[paper]](https://doi.org/10.1109/TII.2025.3578123)
15. 🟡 [25'SSRN] | Power System Operation Regulations Verification With Retrieval-Augmented Generation Enhanced Large Language Model | [[paper]](https://doi.org/10.2139/ssrn.5139554)
16. 🟡 [25'TechRxiv] | PowerCon: A Collaborative Framework Integrating LLM and Power AI for Interactive and Regulation-Compliant Day-Ahead Dispatch | [[paper]](https://doi.org/10.36227/techrxiv.174568329.95744055/v1)
17. 🟢 [25'IEEE Transactions on Power Systems] | PowerGraph-LLM: Novel Power Grid Graph Embedding and Optimization With Large Language Models | [[paper]](https://doi.org/10.1109/TPWRS.2025.3596774) | [[arXiv]](https://arxiv.org/abs/2501.07639) | [[PDF]](https://arxiv.org/pdf/2501.07639)
18. 🟢 [24'Energy and Buildings] | Large Language Model-Based Interpretable Machine Learning Control in Building Energy Systems | [[paper]](https://doi.org/10.1016/j.enbuild.2024.114278)

<a id="power_llm_forecasting"></a>
## LLMs and Foundation Models for Energy Forecasting

1. 🟢 [26'CSEE Journal of Power and Energy Systems] | Enhancing Distribution System State Estimation Under Limited Measurements: Leveraging Large Language Model and Multimodal Information | [[paper]](https://doi.org/10.17775/CSEEJPES.2025.01460)
2. 🟢 [26'IEEE Transactions on Power Systems] | Mid-Term Load Forecasting With Minimal Data: An In-Context-Learning-Aware Approach Using Large Language Models | [[paper]](https://doi.org/10.1109/TPWRS.2026.3654059)
3. 🟢 [26'Electronics Letters] | Parameter-Efficient Adaptation of GPT-Style Foundation Models for Power Grid Load Forecasting | [[paper]](https://doi.org/10.1049/ell2.70612)
4. 🟢 [26'IEEE Transactions on Smart Grid — Early Access] | STDeepSeek: Continual Learning Enhanced Spatiotemporal Large Language Model for Load Forecasting of Electric Vehicle Charging Stations | [[paper]](https://doi.org/10.1109/TSG.2026.3725028)
5. 🟢 [26'IEEE Transactions on Smart Grid — Early Access] | Unstructured Information-Aware Load Forecasting with Sparse Fine-Tuning of Large Language Models | [[paper]](https://doi.org/10.1109/TSG.2026.3744756)
6. 🟡 [25'arXiv] | Large Language Model-Empowered Interactive Load Forecasting | [[paper]](https://arxiv.org/abs/2505.16577)
7. 🟢 [25'Applied Energy] | TimeGPT in Load Forecasting: A Large Time Series Model Perspective | [[paper]](https://doi.org/10.1016/j.apenergy.2024.124973)
8. 🟢 [25'Open-source project] | WindFM: An Open-Source Foundation Model for Zero-Shot Wind Power Forecasting | [[paper]](https://github.com/shiyu-coder/WindFM) | [[code]](https://github.com/shiyu-coder/WindFM)
9. 🟢 [25'Neurocomputing] | Zero-Shot Load Forecasting for Integrated Energy Systems: A Large Language Model-Based Framework With Multi-Task Learning | [[paper]](https://doi.org/10.1016/j.neucom.2025.131288) | [[arXiv]](https://arxiv.org/abs/2502.16896) | [[PDF]](https://arxiv.org/pdf/2502.16896)
10. 🟡 [24'arXiv] | A General Framework for Load Forecasting Based on Pre-Trained Large Language Model | [[paper]](https://arxiv.org/abs/2406.11336)
11. 🟢 [24'Energy Conversion and Management] | BERT4ST: Fine-Tuning Pre-Trained Large Language Model for Wind Power Forecasting | [[paper]](https://doi.org/10.1016/j.enconman.2024.118331)
12. 🟢 [24'ACM CIKM] | Generative AI for Energy: Multi-Horizon Power Consumption Forecasting Using Large Language Models | [[paper]](https://doi.org/10.1145/3627673.3679964)
13. 🟡 [24'SSRN] | LFLLM: A Robust Large Language Model for Short-Term Load Forecasting in Smart Grids | [[paper]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5070252)
14. 🟡 [24'arXiv] | PowerPM: Foundation Model for Power Systems | [[paper]](https://arxiv.org/abs/2408.04057)
15. 🟢 [24'IEEE ICIEA] | Probabilistic PV Power Forecasting by a Multi-Modal Method Using GPT-Agent to Interpret Weather Conditions | [[paper]](https://ieeexplore.ieee.org/document/10665072)
16. 🟢 [24'Applied Energy] | STELLM: Spatio-Temporal Enhanced Pre-Trained Large Language Model for Wind Speed Forecasting | [[paper]](https://doi.org/10.1016/j.apenergy.2024.124034)
17. 🟢 [24'Energies] | Using Generative Pre-Trained Transformers (GPT) for Electricity Price Trend Forecasting in the Spanish Market | [[paper]](https://doi.org/10.3390/en17102338)
18. 🟡 [24'arXiv] | Zero-Shot Load Forecasting With Large Language Models | [[paper]](https://arxiv.org/abs/2411.11350)

<a id="time_series"></a>
## General Time-Series Forecasting Models

1. 🟢 [25'ICML] | Sundial: A Family of Highly Capable Time Series Foundation Models | [[paper]](https://arxiv.org/abs/2502.00816) | [[code]](https://github.com/thuml/Sundial)
2. 🟢 [25'ICLR] | Time-MoE: Billion-Scale Time Series Foundation Models With Mixture of Experts | [[paper]](https://openreview.net/forum?id=e1wDDFmlVu) | [[code]](https://github.com/Time-MoE/Time-MoE)
3. 🟢 [24'ICML] | A Decoder-Only Foundation Model for Time-Series Forecasting | [[paper]](https://arxiv.org/abs/2310.10688) | [[code]](https://github.com/google-research/timesfm)
4. 🟢 [24'ICML] | Chronos: Learning the Language of Time Series | [[paper]](https://arxiv.org/abs/2403.07815) | [[code]](https://github.com/amazon-science/chronos-forecasting)
5. 🟢 [24'NeurIPS Datasets and Benchmarks] | GIFT-Eval: A Benchmark for General Time Series Forecasting Model Evaluation | [[paper]](https://arxiv.org/abs/2410.10393) | [[code]](https://github.com/SalesforceAIResearch/gift-eval)
6. 🟢 [24'ICLR] | iTransformer: Inverted Transformers Are Effective for Time Series Forecasting | [[paper]](https://openreview.net/forum?id=JePfAI8fah) | [[code]](https://github.com/thuml/iTransformer)
7. 🟢 [24'ICML] | MOMENT: A Family of Open Time-Series Foundation Models | [[paper]](https://arxiv.org/abs/2402.03885) | [[code]](https://github.com/moment-timeseries-foundation-model/moment)
8. 🟢 [24'ICLR] | Time-LLM: Time Series Forecasting by Reprogramming Large Language Models | [[paper]](https://openreview.net/forum?id=Unb5CVPtae) | [[code]](https://github.com/KimMeen/Time-LLM)
9. 🟢 [24'ICLR] | TimeMixer: Decomposable Multiscale Mixing for Time Series Forecasting | [[paper]](https://openreview.net/forum?id=7oLshfEIC2) | [[code]](https://github.com/kwuking/TimeMixer)
10. 🟢 [24'ICML] | Timer: Generative Pre-Trained Transformers Are Large Time Series Models | [[paper]](https://arxiv.org/abs/2402.02368) | [[code]](https://github.com/thuml/Large-Time-Series-Model)
11. 🟢 [24'NeurIPS] | Tiny Time Mixers: Fast Pre-Trained Models for Enhanced Zero/Few-Shot Forecasting of Multivariate Time Series | [[paper]](https://arxiv.org/abs/2401.03955) | [[code]](https://github.com/ibm-granite/granite-tsfm)
12. 🟢 [24'ICML] | Unified Training of Universal Time Series Forecasting Transformers | [[paper]](https://arxiv.org/abs/2402.02592) | [[code]](https://github.com/SalesforceAIResearch/uni2ts)
13. 🟢 [23'ICLR] | A Time Series Is Worth 64 Words: Long-Term Forecasting With Transformers | [[paper]](https://openreview.net/forum?id=Jbdc0vTOcol) | [[code]](https://github.com/yuqinie98/PatchTST)
14. 🟢 [23'AAAI] | Are Transformers Effective for Time Series Forecasting? | [[paper]](https://arxiv.org/abs/2205.13504) | [[code]](https://github.com/cure-lab/LTSF-Linear)
15. 🟢 [23'ICLR] | Crossformer: Transformer Utilizing Cross-Dimension Dependency for Multivariate Time Series Forecasting | [[paper]](https://openreview.net/forum?id=vSVLM2j9eie) | [[code]](https://github.com/Thinklab-SJTU/Crossformer)
16. 🟢 [23'TMLR] | Long-Term Forecasting With TiDE: Time-Series Dense Encoder | [[paper]](https://openreview.net/forum?id=pCbC3aQB5W) | [[code]](https://github.com/google-research/google-research/tree/master/tide)
17. 🟢 [23'NeurIPS] | One Fits All: Power General Time Series Analysis by Pretrained LM | [[paper]](https://arxiv.org/abs/2302.11939) | [[code]](https://github.com/DAMO-DI-ML/NeurIPS2023-One-Fits-All)
18. 🟢 [23'ICLR] | TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis | [[paper]](https://openreview.net/forum?id=ju_Uqw384Oq) | [[code]](https://github.com/thuml/TimesNet)
19. 🟢 [23'KDD] | TSMixer: An All-MLP Architecture for Time Series Forecasting | [[paper]](https://arxiv.org/abs/2303.06053) | [[code]](https://github.com/google-research/google-research/tree/master/tsmixer)
20. 🟢 [22'ICLR] | ETSformer: Exponential Smoothing Transformers for Time-Series Forecasting | [[paper]](https://openreview.net/forum?id=5m_3whfo483) | [[code]](https://github.com/salesforce/ETSformer)
21. 🟢 [22'ICML] | FEDformer: Frequency Enhanced Decomposed Transformer for Long-Term Series Forecasting | [[paper]](https://proceedings.mlr.press/v162/zhou22g.html) | [[code]](https://github.com/MAZiqing/FEDformer)
22. 🟢 [22'NeurIPS] | Non-Stationary Transformers: Exploring the Stationarity in Time Series Forecasting | [[paper]](https://arxiv.org/abs/2205.14415) | [[code]](https://github.com/thuml/Nonstationary_Transformers)
23. 🟢 [22'ICLR] | Pyraformer: Low-Complexity Pyramidal Attention for Long-Range Time Series Modeling and Forecasting | [[paper]](https://openreview.net/forum?id=0EXmFzUn5I) | [[code]](https://github.com/alipay/Pyraformer)
24. 🟢 [22'NeurIPS] | SCINet: Time Series Modeling and Forecasting With Sample Convolution and Interaction | [[paper]](https://arxiv.org/abs/2106.09305) | [[code]](https://github.com/cure-lab/SCINet)
25. 🟢 [21'NeurIPS] | Autoformer: Decomposition Transformers With Auto-Correlation for Long-Term Series Forecasting | [[paper]](https://proceedings.neurips.cc/paper/2021/hash/bcc0d400288793e8bdcd7c19a8ac0c2b-Abstract.html) | [[code]](https://github.com/thuml/Autoformer)
26. 🟢 [21'AAAI] | Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting | [[paper]](https://ojs.aaai.org/index.php/AAAI/article/view/17325) | [[code]](https://github.com/zhouhaoyi/Informer2020)
27. 🟢 [21'International Journal of Forecasting] | Temporal Fusion Transformers for Interpretable Multi-Horizon Time Series Forecasting | [[paper]](https://doi.org/10.1016/j.ijforecast.2021.03.012) | [[code]](https://github.com/google-research/google-research/tree/master/tft)
28. 🟢 [20'International Journal of Forecasting] | DeepAR: Probabilistic Forecasting With Autoregressive Recurrent Networks | [[paper]](https://doi.org/10.1016/j.ijforecast.2019.07.001) | [[code]](https://github.com/awslabs/gluonts)
29. 🟢 [20'ICLR] | N-BEATS: Neural Basis Expansion Analysis for Interpretable Time Series Forecasting | [[paper]](https://openreview.net/forum?id=r1ecqn4YwB) | [[code]](https://github.com/philipperemy/n-beats)

<a id="graph_power"></a>
## Graph and Spatio-Temporal Learning for Power Systems

1. 🟢 [25'IEEE Transactions on Industrial Informatics] | SCADA Data-Driven Spatio-Temporal Graph Convolutional Neural Network for Wind Turbine Fault Diagnosis | [[paper]](https://ieeexplore.ieee.org/document/10930628)
2. 🟢 [24'IEEE Transactions on Power Systems] | A Physics-Guided Graph Convolution Neural Network for Optimal Power Flow | [[paper]](https://doi.org/10.1109/TPWRS.2023.3238377)
3. 🟢 [24'IEEE Transactions on Sustainable Energy] | Spatial-Temporal Wind Power Probabilistic Forecasting Based on Time-Aware Graph Convolutional Network | [[paper]](https://ieeexplore.ieee.org/document/10502289)
4. 🟢 [24'IEEE Transactions on Industrial Informatics] | Topology-Transferable Physics-Guided Graph Neural Network for Real-Time Optimal Power Flow | [[paper]](https://doi.org/10.1109/TII.2024.3398058)
5. 🟢 [23'IEEE Transactions on Emerging Topics in Computational Intelligence] | Generalized Graph Neural Network-Based Detection of False Data Injection Attacks in Smart Grids | [[paper]](https://doi.org/10.1109/TETCI.2022.3232821)
6. 🟢 [23'IEEE Access] | Spatial-Temporal Recurrent Graph Neural Networks for Fault Diagnostics in Power Distribution Systems | [[paper]](https://doi.org/10.1109/ACCESS.2023.3273292)
7. 🟢 [23'IEEE Transactions on Sustainable Energy] | Spatio-Temporal Graph Neural Network and Pattern Prediction Based Ultra-Short-Term Power Forecasting of Wind Farm Cluster | [[paper]](https://ieeexplore.ieee.org/document/10269018)
8. 🟢 [22'IEEE Systems Journal] | Graph Neural Networks Based Detection of Stealth False Data Injection Attacks in Smart Grids | [[paper]](https://doi.org/10.1109/JSYST.2021.3109082)
9. 🟢 [22'IEEE Transactions on Smart Grid] | Joint Detection and Localization of Stealth False Data Injection Attacks in Smart Grids Using Graph Neural Networks | [[paper]](https://doi.org/10.1109/TSG.2021.3117977)
10. 🟢 [21'AAAI] | Spatial-Temporal Fusion Graph Neural Networks for Traffic Flow Forecasting | [[paper]](https://ojs.aaai.org/index.php/AAAI/article/view/16542) | [[code]](https://github.com/MengzhangLI/STFGNN)
11. 🟢 [20'NeurIPS] | Adaptive Graph Convolutional Recurrent Network for Traffic Forecasting | [[paper]](https://proceedings.neurips.cc/paper/2020/hash/ce1aad92b939420fc13e5f7d9b8e9c4d-Abstract.html) | [[code]](https://github.com/LeiBAI/AGCRN)
12. 🟢 [20'KDD] | Connecting the Dots: Multivariate Time Series Forecasting With Graph Neural Networks | [[paper]](https://doi.org/10.1145/3394486.3403118) | [[code]](https://github.com/nnzhan/MTGNN)
13. 🟢 [20'AAAI] | GMAN: A Graph Multi-Attention Network for Traffic Prediction | [[paper]](https://ojs.aaai.org/index.php/AAAI/article/view/5477) | [[code]](https://github.com/zhengchuanpan/GMAN)
14. 🟢 [20'NeurIPS] | Spectral Temporal Graph Neural Network for Multivariate Time-Series Forecasting | [[paper]](https://proceedings.neurips.cc/paper/2020/hash/cdf6581cb7aca4b7e19ef136c6e601a5-Abstract.html) | [[code]](https://github.com/microsoft/StemGNN)
15. 🟢 [19'AAAI] | Attention Based Spatial-Temporal Graph Convolutional Networks for Traffic Flow Forecasting | [[paper]](https://ojs.aaai.org/index.php/AAAI/article/view/3881) | [[code]](https://github.com/guoshnBJTU/ASTGCN-r-pytorch)
16. 🟢 [19'IJCAI] | Graph WaveNet for Deep Spatial-Temporal Graph Modeling | [[paper]](https://www.ijcai.org/proceedings/2019/264) | [[code]](https://github.com/nnzhan/Graph-WaveNet)
17. 🟢 [18'ICLR] | Diffusion Convolutional Recurrent Neural Network: Data-Driven Traffic Forecasting | [[paper]](https://openreview.net/forum?id=SJiHXGWAZ) | [[code]](https://github.com/liyaguang/DCRNN)
18. 🟢 [18'IJCAI] | Spatio-Temporal Graph Convolutional Networks: A Deep Learning Framework for Traffic Forecasting | [[paper]](https://www.ijcai.org/Proceedings/2018/0505) | [[code]](https://github.com/VeritasYin/STGCN_IJCAI-18)

<a id="physics_safe"></a>
## Physics-Guided Learning, Safe Control, and Verification

1. 🟡 [26'arXiv] | A Physics-guided Fine-tuned LLM-based Framework for Customized Power Distribution System Feeder Generation | [[paper]](https://arxiv.org/abs/2607.07237) | [[PDF]](https://arxiv.org/pdf/2607.07237)
2. 🟡 [26'Microsoft Research White Paper] | GridSFM: A Foundation Model for AC Optimal Power Flow | [[paper]](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/GridFM_white_paper.pdf) | [[code]](https://github.com/gridfm)
3. 🟢 [26'Results in Engineering] | Physics-Informed Multimodal Large Language Models for Intelligent Energy Question Answering | [[paper]](https://www.sciencedirect.com/science/article/pii/S2590123026017512)
4. 🟢 [26'IEEE Transactions on Circuits and Systems I] | Uncertainty-Aware Model-Based Multi-Agent Deep Reinforcement Learning for Robust Active Voltage Control | [[paper]](https://doi.org/10.1109/TCSI.2025.3588231)
5. 🟢 [25'IEEE Transactions on Industry Applications] | Physics-Informed Graph Neural Networks for Collaborative Dynamic Reconfiguration and Voltage Regulation in Unbalanced Distribution Systems | [[paper]](https://doi.org/10.1109/TIA.2025.3529799)
6. 🟢 [24'IEEE Transactions on Circuits and Systems I] | Physics-Guided Multi-Agent Deep Reinforcement Learning for Robust Active Voltage Control in Electrical Distribution Systems | [[paper]](https://doi.org/10.1109/TCSI.2023.3340691)
7. 🟢 [24'Electric Power Systems Research] | Physics-Informed Graph Neural Network for Dynamic Reconfiguration of Power Systems | [[paper]](https://doi.org/10.1016/j.epsr.2024.110817)
8. 🟢 [21'IEEE Transactions on Power Systems] | Deep Reinforcement Learning-Based Autonomous Voltage Control for Power Grid Operations | [[paper]](https://doi.org/10.1109/TPWRS.2019.2941134)
9. 🟢 [21'IEEE Transactions on Power Systems] | Explainable AI in Deep Reinforcement Learning Models for Power System Emergency Control | [[paper]](https://ieeexplore.ieee.org/document/9506997)
10. 🟢 [20'IEEE Access] | Stability-Certified Reinforcement Learning: A Control-Theoretic Perspective | [[paper]](https://ieeexplore.ieee.org/document/9296215)
11. 🟢 [19'IEEE Transactions on Power Systems] | Data-Driven Load Frequency Control for Stochastic Power Systems: A Deep Reinforcement Learning Method With Continuous Action Search | [[paper]](https://doi.org/10.1109/TPWRS.2018.2881359)
12. 🟢 [19'IEEE Transactions on Smart Grid] | Data-Driven Local Control Design for Active Distribution Grids Using Off-Line Optimal Power Flow and Machine Learning Techniques | [[paper]](https://ieeexplore.ieee.org/document/8667699)
13. 🟢 [18'IEEE Transactions on Smart Grid] | Online Detection of Stealthy False Data Injection Attacks in Power System State Estimation | [[paper]](https://doi.org/10.1109/TSG.2016.2596298)

<a id="cyber_fault"></a>
## Cyber-Physical Anomaly Detection and Fault Diagnosis

1. 🟡 [26'arXiv] | Evaluating Jailbreaking Vulnerabilities in LLMs Deployed as Assistants for Smart Grid Operations: A Benchmark Against NERC Standards | [[paper]](https://arxiv.org/abs/2604.23341) | [[PDF]](https://arxiv.org/pdf/2604.23341)
2. 🟢 [26'ACM Sustainability Week Companion] | GridStratLLM: Agent Framework for Coordinated Cyberattacks on the Smart Grid With Large Language Models | [[paper]](https://publikationen.bibliothek.kit.edu/1000194714) | [[code]](https://github.com/nbke/GridStratLLM)
3. 🟢 [26'IEEE Transactions on Smart Grid] | Large Language Model-Based Smart Agents for Attack-Defense Game on Cyber-Physical Power Systems | [[paper]](https://doi.org/10.1109/TSG.2026.3681079)
4. 🟡 [26'arXiv] | Large Language Models as Explainable Cyberattack Detectors for Energy Industrial Control Systems | [[paper]](https://arxiv.org/abs/2604.26079) | [[PDF]](https://arxiv.org/pdf/2604.26079)
5. 🟢 [25'IEEE MRAI] | A Large Language Model Question Answering System for Power System Equipment Fault Diagnosis Based on RAGFlow | [[paper]](https://doi.org/10.1109/MRAI65197.2025.11135758)
6. 🟢 [25'IEEE ICAIIC] | DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models | [[paper]](https://doi.org/10.1109/ICAIIC64266.2025.10920654)
7. 🟢 [25'IEEE PowerCon] | Transformer Fault Diagnosis System Based on Fusion of Knowledge Graph and Large Language Model | [[paper]](https://doi.org/10.1109/POWERCON66300.2025.11295148)
8. 🟡 [24'arXiv] | Fault Diagnosis in Power Grids With Large Language Model | [[paper]](https://arxiv.org/abs/2407.08836) | [[PDF]](https://arxiv.org/pdf/2407.08836)
9. 🟡 [24'arXiv] | SubstationAI: Multimodal Large Model-Based Approaches for Analyzing Substation Equipment Faults | [[paper]](https://arxiv.org/abs/2412.17077)
10. 🟢 [23'IEEE ISPCE-Asia] | Electrical Equipment Fault Diagnosis: A Technique Combining Fuzzy Logic and Large Language Models | [[paper]](https://doi.org/10.1109/ISPCE-ASIA60405.2023.10365878)
11. 🟢 [23'IEEE Transactions on Instrumentation and Measurement] | Incipient Fault Detection in Power Distribution System: A Time-Frequency Embedded Deep-Learning-Based Approach | [[paper]](https://doi.org/10.1109/TIM.2023.3262291)
12. 🟢 [21'IEEE Access] | Detection of Cyber Attacks on Voltage Regulation in Distribution Systems Using Machine Learning | [[paper]](https://doi.org/10.1109/ACCESS.2021.3064689) | [[code]](https://github.com/nbhusal/Data-Attack-on-Voltage-Regulation)
13. 🟢 [20'IEEE Transactions on Smart Grid] | Deep Learning Detection of Electricity Theft Cyber-Attacks in Renewable Distributed Generation | [[paper]](https://doi.org/10.1109/TSG.2019.2957780)
14. 🟢 [20'Computers & Security] | Detecting Stealthy False Data Injection Attacks in the Smart Grid Using Ensemble-Based Machine Learning | [[paper]](https://doi.org/10.1016/j.cose.2020.101994)
15. 🟢 [19'IEEE Transactions on Power Delivery] | A Hybrid Intelligent Approach for Classification of Incipient Faults in Transmission Network | [[paper]](https://doi.org/10.1109/TPWRD.2018.2889719)
16. 🟢 [17'IEEE Transactions on Smart Grid] | Real-Time Detection of False Data Injection Attacks in Smart Grid: A Deep Learning-Based Intelligent Mechanism | [[paper]](https://doi.org/10.1109/TSG.2015.2489263)
17. 🟢 [17'IEEE Transactions on Smart Grid] | Short-Term State Forecasting-Aided Method for Detection of Smart Grid General False Data Injection Attacks | [[paper]](https://doi.org/10.1109/TSG.2015.2492827)
18. 🟢 [16'IEEE Transactions on Neural Networks and Learning Systems] | Machine Learning Methods for Attack Detection in the Smart Grid | [[paper]](https://doi.org/10.1109/TNNLS.2015.2404803)
19. 🟢 [09'ACM CCS] | False Data Injection Attacks Against State Estimation in Electric Power Grids | [[paper]](https://doi.org/10.1145/1653662.1653666)

<a id="xai_human"></a>
## Explainability, Reports, and Human Oversight

1. 🟡 [26'arXiv] | An End-to-End Explainable AI Framework with Automated LLM-Based Natural Language Explanation Generation for Energy Systems | [[paper]](https://arxiv.org/abs/2607.04374) | [[PDF]](https://arxiv.org/pdf/2607.04374)
2. 🟡 [26'arXiv] | Explainable Post-Disaster Grid Observability Recovery Using Human-Oversight Agentic LLMs | [[paper]](https://arxiv.org/abs/2609.16774) | [[PDF]](https://arxiv.org/pdf/2609.16774)
3. 🟡 [26'arXiv] | Task-Aware Harness Provisioning for LLM Agents in Mission-Critical Infrastructure Operations | [[paper]](https://arxiv.org/abs/2608.17433) | [[PDF]](https://arxiv.org/pdf/2608.17433)
4. 🟢 [25'Renewable and Sustainable Energy Reviews] | Explainable Artificial Intelligence for Energy Systems Maintenance: A Review on Concepts, Current Techniques, Challenges, and Prospects | [[paper]](https://doi.org/10.1016/j.rser.2025.115668)
5. 🟢 [25'iScience] | Human-AI Interaction in Safety-Critical Network Infrastructures | [[paper]](https://doi.org/10.1016/j.isci.2025.113400)
6. 🟢 [24'Energy and AI] | Explainability and Interpretability in Electric Load Forecasting Using Machine Learning Techniques: A Review | [[paper]](https://doi.org/10.1016/j.egyai.2024.100358)
7. 🟢 [24'Climate Change AI at ICLR] | Interpretable Machine Learning for Power Systems: Establishing Confidence in SHapley Additive exPlanations | [[paper]](https://www.climatechange.ai/papers/iclr2024/54)
8. 🟢 [24'IEEE ISGT Europe] | Towards Explainable and Trustworthy Autonomous Models for Power Systems: A Retrospective Case Study Analysis | [[paper]](https://pure.strath.ac.uk/ws/portalfiles/portal/244828046/Cassidy-etal-IEEE-ISGT-Europe-2024-explainable-and-trustworthy-autonomous-models-for-power-systems.pdf)
9. 🟢 [21'Chaos] | Revealing Drivers and Risks for Power Grid Frequency Stability With Explainable AI | [[paper]](https://doi.org/10.1063/5.0051019) | [[code]](https://arxiv.org/abs/2106.04341)

<a id="benchmarks"></a>
## Benchmarks, Test Systems, Datasets, and Simulators

1. 🟡 [26'arXiv] | A Benchmark on LLM-Based Power Flow Computation: Do More Structured Prompts Help? | [[paper]](https://arxiv.org/abs/2605.18642) | [[PDF]](https://arxiv.org/pdf/2605.18642)
2. 🟡 [26'arXiv] | Power Systems Agent Benchmark: Executable Evaluation of AI Agents in Electric Power Engineering | [[paper]](https://arxiv.org/abs/2606.20950) | [[PDF]](https://arxiv.org/pdf/2606.20950) | [[code]](https://github.com/trashchenkov/power-systems-agent-benchmark)
3. 🟡 [26'arXiv] | PowerAgentBench-Dyn: A Benchmark for Agentic AI in Power System Dynamic Studies | [[paper]](https://arxiv.org/abs/2606.20401) | [[PDF]](https://arxiv.org/pdf/2606.20401)
4. 🟡 [26'arXiv] | PowerAgentBench-SS: A Benchmark for Agentic AI in Power System Steady-State Studies | [[paper]](https://arxiv.org/abs/2606.18789) | [[PDF]](https://arxiv.org/pdf/2606.18789)
5. 🟡 [26'arXiv] | PowerBench: A Benchmark for Agentic Retrieval and Reasoning in Power Systems | [[paper]](https://arxiv.org/abs/2609.34492) | [[PDF]](https://arxiv.org/pdf/2609.34492) | [[code]](https://github.com/open-compass/PowerBench)
6. 🟡 [26'arXiv] | RestoreBench: Can AI Agents Restore Power Flow Convergence? | [[paper]](https://arxiv.org/abs/2609.00384) | [[PDF]](https://arxiv.org/pdf/2609.00384) | [[code]](https://github.com/Mansutti081/RestoreBench)
7. 🟡 [24'arXiv] | OPFData: Large-Scale Datasets for AC Optimal Power Flow With Topological Perturbations | [[paper]](https://arxiv.org/abs/2406.07234) | [[code]](https://github.com/AI4OPT/OPFData)
8. 🟢 [22'IEEE Transactions on Power Systems] | A Synthetic 9500-Node Distribution Test System | [[paper]](https://cmte.ieee.org/pes-testfeeders/wp-content/uploads/sites/167/2022/03/9500-Node-PES-TPWRS-Paper-2022.01.14.pdf)
9. 🟢 [21'NeurIPS Datasets and Benchmarks] | L2RPN: Learning to Run a Power Network—A Large-Scale Benchmark for Sequential Decision Making in Power Systems | [[paper]](https://arxiv.org/abs/2003.07339) | [[code]](https://github.com/rte-france/Grid2Op)
10. 🟡 [21'arXiv] | PowerGym: A Reinforcement Learning Environment for Volt-Var Control in Power Distribution Systems | [[paper]](https://arxiv.org/abs/2111.05025) | [[code]](https://github.com/siemens/powergym)
11. 🟢 [21'Scientific Data] | PSML: A Multi-Scale Time-Series Dataset for Machine Learning in Decarbonized Energy Grids | [[paper]](https://doi.org/10.1038/s41597-021-00989-6) | [[code]](https://github.com/tamu-engineering-research/Open-source-power-dataset)
12. 🟢 [20'IEEE Open Access Journal of Power and Energy] | Building Highly Detailed Synthetic Electric Grid Data Sets for Combined Transmission and Distribution Systems | [[paper]](https://doi.org/10.1109/OAJPE.2020.3029278)
13. 🟢 [20'Energies] | SimBench—A Benchmark Dataset of Electric Power Systems | [[paper]](https://doi.org/10.3390/en13123290) | [[code]](https://github.com/e2nIEE/simbench)
14. 🟢 [19'IEEE PowerTech] | PGLib-OPF: Benchmarking AC Optimal Power Flow Formulations | [[paper]](https://arxiv.org/abs/1908.02788) | [[code]](https://github.com/power-grid-lib/pglib-opf)
15. 🟢 [18'IEEE Transactions on Power Systems] | Pandapower—An Open-Source Python Tool for Convenient Modeling, Analysis, and Optimization of Electric Power Systems | [[paper]](https://doi.org/10.1109/TPWRS.2018.2829021) | [[code]](https://github.com/e2nIEE/pandapower)
16. 🟢 [11'IEEE Transactions on Power Systems] | MATPOWER: Steady-State Operations, Planning, and Analysis Tools for Power Systems Research and Education | [[paper]](https://doi.org/10.1109/TPWRS.2010.2051168) | [[code]](https://github.com/MATPOWER/matpower)
17. 🟢 [09'IEEE PES General Meeting] | OpenDSS, a Comprehensive Tool for Modeling Distribution Systems | [[paper]](https://doi.org/10.1109/PES.2009.5275955) | [[code]](https://github.com/dss-extensions/OpenDSSDirect.py)
18. 🟢 [01'IEEE Transactions on Power Systems] | Radial Distribution Test Feeders | [[paper]](https://doi.org/10.1109/59.969249)

<a id="graph_llm"></a>
## Graph Computation + LLM: Methods, Benchmarks, and Power-System Explorations

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

For application boundaries and a reading order, see [the updated research map](docs/RELATED_WORK_MAP.md).

<a id="transactions-spotlight"></a>
## IEEE Transactions Spotlight

Cross-category index; these are the same catalog records, not additional papers.

1. 🟢 [26'IEEE Transactions on Smart Grid — Early Access] | A Large Language Model-Based Framework for Automated Dynamic Simulation of Power Systems | [[paper]](https://doi.org/10.1109/TSG.2026.3731592)
2. 🟢 [26'IEEE Transactions on Power Systems] | Customising Electricity Contracts at Scale With Large Language Models | [[paper]](https://doi.org/10.1109/TPWRS.2026.3670536)
3. 🟢 [26'IEEE Transactions on Smart Grid] | Large Language Model Powered Automated Modeling and Optimization of Active Distribution Network Dispatch Problems | [[paper]](https://doi.org/10.1109/TSG.2025.3621438) | [[arXiv]](https://arxiv.org/abs/2507.21162) | [[PDF]](https://arxiv.org/pdf/2507.21162)
4. 🟢 [26'IEEE Transactions on Smart Grid] | Large Language Model-Based Smart Agents for Attack-Defense Game on Cyber-Physical Power Systems | [[paper]](https://doi.org/10.1109/TSG.2026.3681079)
5. 🟢 [26'IEEE Transactions on Smart Grid — Early Access] | LLM-Empowered Decision-Focused Learning for the Operation of Local Energy Communities | [[paper]](https://doi.org/10.1109/TSG.2026.3678781)
6. 🟢 [26'IEEE Transactions on Smart Grid] | LLM-Enhanced Multi-Agent Reinforcement Learning With Expert Workflow for Real-Time P2P Energy Trading | [[paper]](https://doi.org/10.1109/TSG.2026.3684885)
7. 🟢 [26'IEEE Transactions on Power Systems] | Mid-Term Load Forecasting With Minimal Data: An In-Context-Learning-Aware Approach Using Large Language Models | [[paper]](https://doi.org/10.1109/TPWRS.2026.3654059)
8. 🟢 [26'IEEE Transactions on Industrial Informatics — Early Access] | Multiobjective Optimization of Data Center Microgrids via Large Language Model-Assisted Deep Reinforcement Learning | [[paper]](https://doi.org/10.1109/TII.2026.3725105)
9. 🟢 [26'IEEE Transactions on Smart Grid — Early Access] | STDeepSeek: Continual Learning Enhanced Spatiotemporal Large Language Model for Load Forecasting of Electric Vehicle Charging Stations | [[paper]](https://doi.org/10.1109/TSG.2026.3725028)
10. 🟢 [26'IEEE Transactions on Circuits and Systems I] | Uncertainty-Aware Model-Based Multi-Agent Deep Reinforcement Learning for Robust Active Voltage Control | [[paper]](https://doi.org/10.1109/TCSI.2025.3588231)
11. 🟢 [26'IEEE Transactions on Smart Grid — Early Access] | Unstructured Information-Aware Load Forecasting with Sparse Fine-Tuning of Large Language Models | [[paper]](https://doi.org/10.1109/TSG.2026.3744756)
12. 🟢 [26'IEEE Transactions on Smart Grid] | Vision of Future Smart Control Center: Fusion of Large Language Models and Power System Intelligent Computing | [[paper]](https://doi.org/10.1109/TSG.2026.3717716)
13. 🟢 [25'IEEE Transactions on Smart Grid] | Enhancing LLMs for Power System Simulations: A Feedback-Driven Multi-Agent Framework | [[paper]](https://doi.org/10.1109/TSG.2025.3589114)
14. 🟢 [25'IEEE Transactions on Industrial Informatics] | Optimization of Energy and Carbon Emissions in Integrated Energy System Based on Deep Reinforcement Learning Assisted by Large Language Model | [[paper]](https://doi.org/10.1109/TII.2025.3578123)
15. 🟢 [25'IEEE Transactions on Industry Applications] | Physics-Informed Graph Neural Networks for Collaborative Dynamic Reconfiguration and Voltage Regulation in Unbalanced Distribution Systems | [[paper]](https://doi.org/10.1109/TIA.2025.3529799)
16. 🟢 [25'IEEE Transactions on Power Systems] | PowerGraph-LLM: Novel Power Grid Graph Embedding and Optimization With Large Language Models | [[paper]](https://doi.org/10.1109/TPWRS.2025.3596774) | [[arXiv]](https://arxiv.org/abs/2501.07639) | [[PDF]](https://arxiv.org/pdf/2501.07639)
17. 🟢 [25'IEEE Transactions on Industrial Informatics] | SCADA Data-Driven Spatio-Temporal Graph Convolutional Neural Network for Wind Turbine Fault Diagnosis | [[paper]](https://ieeexplore.ieee.org/document/10930628)
18. 🟢 [24'IEEE Transactions on Power Systems] | A Physics-Guided Graph Convolution Neural Network for Optimal Power Flow | [[paper]](https://doi.org/10.1109/TPWRS.2023.3238377)
19. 🟢 [24'IEEE Transactions on Smart Grid] | Applying Large Language Models to Power Systems: Potential Security Threats | [[paper]](https://doi.org/10.1109/TSG.2024.3373256)
20. 🟢 [24'IEEE Transactions on Knowledge and Data Engineering] | Large Language Models on Graphs: A Comprehensive Survey | [[paper]](https://doi.org/10.1109/TKDE.2024.3469578) | [[arXiv]](https://arxiv.org/abs/2312.02783) | [[PDF]](https://arxiv.org/pdf/2312.02783) | [[code]](https://github.com/PeterGriffinJin/Awesome-Language-Model-on-Graphs)
21. 🟢 [24'IEEE Transactions on Circuits and Systems I] | Physics-Guided Multi-Agent Deep Reinforcement Learning for Robust Active Voltage Control in Electrical Distribution Systems | [[paper]](https://doi.org/10.1109/TCSI.2023.3340691)
22. 🟢 [24'IEEE Transactions on Sustainable Energy] | Spatial-Temporal Wind Power Probabilistic Forecasting Based on Time-Aware Graph Convolutional Network | [[paper]](https://ieeexplore.ieee.org/document/10502289)
23. 🟢 [24'IEEE Transactions on Industrial Informatics] | Topology-Transferable Physics-Guided Graph Neural Network for Real-Time Optimal Power Flow | [[paper]](https://doi.org/10.1109/TII.2024.3398058)
24. 🟢 [24'IEEE Transactions on Knowledge and Data Engineering] | Unifying Large Language Models and Knowledge Graphs: A Roadmap | [[paper]](https://doi.org/10.1109/TKDE.2024.3352100) | [[arXiv]](https://arxiv.org/abs/2306.08302) | [[PDF]](https://arxiv.org/pdf/2306.08302)
25. 🟢 [23'IEEE Transactions on Emerging Topics in Computational Intelligence] | Generalized Graph Neural Network-Based Detection of False Data Injection Attacks in Smart Grids | [[paper]](https://doi.org/10.1109/TETCI.2022.3232821)
26. 🟢 [23'IEEE Transactions on Instrumentation and Measurement] | Incipient Fault Detection in Power Distribution System: A Time-Frequency Embedded Deep-Learning-Based Approach | [[paper]](https://doi.org/10.1109/TIM.2023.3262291)
27. 🟢 [23'IEEE Transactions on Sustainable Energy] | Spatio-Temporal Graph Neural Network and Pattern Prediction Based Ultra-Short-Term Power Forecasting of Wind Farm Cluster | [[paper]](https://ieeexplore.ieee.org/document/10269018)
28. 🟢 [22'IEEE Transactions on Power Systems] | A Synthetic 9500-Node Distribution Test System | [[paper]](https://cmte.ieee.org/pes-testfeeders/wp-content/uploads/sites/167/2022/03/9500-Node-PES-TPWRS-Paper-2022.01.14.pdf)
29. 🟢 [22'IEEE Transactions on Smart Grid] | Joint Detection and Localization of Stealth False Data Injection Attacks in Smart Grids Using Graph Neural Networks | [[paper]](https://doi.org/10.1109/TSG.2021.3117977)
30. 🟢 [21'IEEE Transactions on Power Systems] | Deep Reinforcement Learning-Based Autonomous Voltage Control for Power Grid Operations | [[paper]](https://doi.org/10.1109/TPWRS.2019.2941134)
31. 🟢 [21'IEEE Transactions on Power Systems] | Explainable AI in Deep Reinforcement Learning Models for Power System Emergency Control | [[paper]](https://ieeexplore.ieee.org/document/9506997)
32. 🟢 [20'IEEE Transactions on Smart Grid] | Deep Learning Detection of Electricity Theft Cyber-Attacks in Renewable Distributed Generation | [[paper]](https://doi.org/10.1109/TSG.2019.2957780)
33. 🟢 [19'IEEE Transactions on Power Delivery] | A Hybrid Intelligent Approach for Classification of Incipient Faults in Transmission Network | [[paper]](https://doi.org/10.1109/TPWRD.2018.2889719)
34. 🟢 [19'IEEE Transactions on Power Systems] | Data-Driven Load Frequency Control for Stochastic Power Systems: A Deep Reinforcement Learning Method With Continuous Action Search | [[paper]](https://doi.org/10.1109/TPWRS.2018.2881359)
35. 🟢 [19'IEEE Transactions on Smart Grid] | Data-Driven Local Control Design for Active Distribution Grids Using Off-Line Optimal Power Flow and Machine Learning Techniques | [[paper]](https://ieeexplore.ieee.org/document/8667699)
36. 🟢 [18'IEEE Transactions on Smart Grid] | Online Detection of Stealthy False Data Injection Attacks in Power System State Estimation | [[paper]](https://doi.org/10.1109/TSG.2016.2596298)
37. 🟢 [18'IEEE Transactions on Power Systems] | Pandapower—An Open-Source Python Tool for Convenient Modeling, Analysis, and Optimization of Electric Power Systems | [[paper]](https://doi.org/10.1109/TPWRS.2018.2829021) | [[code]](https://github.com/e2nIEE/pandapower)
38. 🟢 [17'IEEE Transactions on Smart Grid] | A Review of False Data Injection Attacks Against Modern Power Systems | [[paper]](https://doi.org/10.1109/TSG.2015.2495133)
39. 🟢 [17'IEEE Transactions on Smart Grid] | Real-Time Detection of False Data Injection Attacks in Smart Grid: A Deep Learning-Based Intelligent Mechanism | [[paper]](https://doi.org/10.1109/TSG.2015.2489263)
40. 🟢 [17'IEEE Transactions on Smart Grid] | Short-Term State Forecasting-Aided Method for Detection of Smart Grid General False Data Injection Attacks | [[paper]](https://doi.org/10.1109/TSG.2015.2492827)
41. 🟢 [16'IEEE Transactions on Neural Networks and Learning Systems] | Machine Learning Methods for Attack Detection in the Smart Grid | [[paper]](https://doi.org/10.1109/TNNLS.2015.2404803)
42. 🟢 [11'IEEE Transactions on Power Systems] | MATPOWER: Steady-State Operations, Planning, and Analysis Tools for Power Systems Research and Education | [[paper]](https://doi.org/10.1109/TPWRS.2010.2051168) | [[code]](https://github.com/MATPOWER/matpower)
43. 🟢 [01'IEEE Transactions on Power Systems] | Radial Distribution Test Feeders | [[paper]](https://doi.org/10.1109/59.969249)

## Open-Source Ecosystem

- [Power-Agent / PowerFM / PowerMCP](https://github.com/Power-Agent) — community projects for power-system foundation models and MCP tools.
- [pandapower](https://github.com/e2nIEE/pandapower) — Python power-system modeling and OPF.
- [OpenDSSDirect.py](https://github.com/dss-extensions/OpenDSSDirect.py) — cross-platform Python interface for OpenDSS.
- [PowerChain](https://github.com/emmanuelbadmus/powerchain) — verified agentic workflows for distribution-grid analysis.
- [LLM4DistReconfig](https://github.com/panaschristou/LLM4DistReconfig) — open training/evaluation pipeline for LLM-based feeder reconfiguration.
- [Grid2Op](https://github.com/rte-france/Grid2Op) and [PowerGym](https://github.com/siemens/powergym) — grid-control environments.
- [PGLib-OPF](https://github.com/power-grid-lib/pglib-opf) and [SimBench](https://github.com/e2nIEE/simbench) — reproducible optimization and distribution benchmarks.

## How to Contribute

Please read [CONTRIBUTING.md](CONTRIBUTING.md). New entries should provide a stable paper URL, publication status, year, venue, category, and an official code link when available. Preprints must remain labeled as preprints until a formal record is verified.

## Scope and Limitations

This is a **living curated bibliography**, not a claim of mathematically exhaustive coverage. Direct power-system LLM/agent studies are collected broadly; generic forecasting and graph-learning sections retain influential or experimentally useful baselines rather than every derivative model. Search coverage, inclusion criteria, duplicate handling, and known blind spots are documented in [docs/SEARCH_STRATEGY.md](docs/SEARCH_STRATEGY.md).

## Acknowledgements

The presentation style was inspired by [Paper-List-for-Medical-Reasoning-Large-Language-Models](https://github.com/HovChen/Paper-List-for-Medical-Reasoning-Large-Language-Models). Literature discovery also consulted official publisher pages, Crossref metadata, arXiv, OpenReview, ACL Anthology, and public project repositories; new and modified records in this update were checked against primary bibliographic records; unchanged legacy records retain their original provenance.

## AI Disclosure

AI-assisted tools were used for literature discovery, metadata normalization, deduplication, and repository generation. Publication claims should still be checked against the linked primary record before being quoted in a manuscript.

## License

The repository structure and original annotations are released under the [MIT License](LICENSE). Linked papers and code remain subject to their respective licenses and copyright terms.
