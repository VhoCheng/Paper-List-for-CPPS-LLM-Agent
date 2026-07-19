# Related-Work Map for PhysChronoGrid

Snapshot: 2026-07-19

## 1. Closest work and the novelty boundary

| Prior-work cluster | Representative papers | What is already established | Remaining boundary for PhysChronoGrid |
|---|---|---|---|
| LLM + simulation tools | Jia et al., *Enhancing LLMs for Power System Simulations*; PowerChain; GridMind; X-GridAgent | LLM agents can call solvers, compose workflows, receive execution feedback, and expose natural-language interfaces | Do not claim that “LLM + multi-agent + solver” alone is novel. Focus on anticipatory multi-horizon risk evidence, cyber-physical diagnosis, report-level grounding, and a strict post-action AC-feasibility veto |
| LLM + distribution operation | LLM4DistReconfig; ADN automated modeling; Grid-Agent; PowerCon | LLMs can generate reconfiguration/dispatch formulations or action sequences | Compare against deterministic optimization and fixed-action-space baselines; demonstrate that the report-and-verifier framework improves safety rather than merely task accuracy |
| LLM + power forecasting | LFLLM; STELLM; BERT4ST; TimeGPT load forecasting; zero-shot load forecasting | Pre-trained language/time-series models can support load, wind, PV, and price prediction | The paper should not sell the forecaster alone as the main novelty; use a topology-aware multi-horizon predictor as the evidence generator inside the end-to-end framework |
| Graph and physics-guided learning | Physics-guided GNN for OPF; topology-transferable GNN; STGNN wind forecasting; GNN-based FDIA localization | Grid topology and physical constraints improve generalization and plausibility | Use graph structure and one auditable physics gate consistently; avoid an untestable collection of many informal “physics rules” |
| Cyber-physical diagnosis | FDIA detection/localization, incipient fault detection, graph fault diagnosis | Physical and cyber anomalies can be detected using temporal, graph, and residual features | Evaluate joint event attribution and report evidence under mixed physical/cyber scenarios, including abstention and human handoff |
| Explainability and oversight | XAI for power systems; human-AI safety-critical infrastructure; customized large-model agents | Explanations and HITL are recognized requirements | Evaluate evidence correctness, unsafe recommendation rate, calibrated abstention, and whether natural-language claims trace to solver/forecast evidence |

## 2. Recommended Related Work structure

### 2.1 Data-driven multi-horizon forecasting in active distribution grids

Cover PatchTST/iTransformer/TimeMixer/TFT, then transition to power-specific STGNN and time-series foundation models. State that forecast accuracy alone does not answer how future violations should be diagnosed and communicated.

### 2.2 Graph and physics-guided learning for grid state/risk inference

Cover topology-aware GNNs, OPF surrogates, physics-guided voltage control, and graph-based FDIA detection. Explain that these methods usually output numerical states/actions rather than an auditable diagnostic report.

### 2.3 LLM and agentic AI for power-system analysis and operation

Start with `Large Foundation Models for Power Systems` and the TSG security perspective, then cover Jia et al., RePower, PowerChain, GridMind, Grid-Agent, X-GridAgent, LLM4DistReconfig, and ADN-dispatch agents. Separate peer-reviewed Transactions papers from preprints.

### 2.4 Trustworthy decision support and human oversight

Cover physical/tool verification, XAI, human supervision, structured outputs, and abstention. End with the gap: few works jointly evaluate proactive multi-horizon anticipation, evidence-grounded cyber-physical diagnosis, structured report quality, post-action AC feasibility, and human escalation.

## 3. Baseline implications

The literature implies that the paper needs four baseline families:

1. **Prediction baselines:** persistence, LSTM/TCN, PatchTST, iTransformer, STGCN/Graph WaveNet, and the proposed topology-aware model.
2. **Decision/report baselines:** deterministic rules or AC-OPF + template report; LLM-only; single-agent + tools; multi-agent without verifier; full framework.
3. **LLM sensitivity:** one frozen local open model as the main setting, smaller/larger open models for scaling, and one version-locked closed API model on a fixed subset.
4. **Safety baselines:** no physics gate, pre-action rule check only, post-action AC power-flow verifier, and human-review triggering.

## 4. Reviewer-facing claims to avoid

- “The first multi-agent framework for power systems.” Existing work invalidates this claim.
- “The first use of LLMs for power dispatch/forecasting/fault diagnosis.” Each area already has prior work.
- “Physics-informed” when the only mechanism is a prompt containing physical terms.
- Treating arXiv papers as peer-reviewed Transactions papers.
- Comparing only different LLM brands without a deterministic optimization/rule baseline.
- Reporting only BLEU/ROUGE or subjective report quality without physical feasibility and evidence correctness.

## 5. Defensible contribution statement

> A simulation-grounded, proactive decision-support framework for active distribution grids that links topology-aware multi-horizon risk forecasting to cyber-physical evidence synthesis, structured LLM reporting, a post-action AC power-flow veto, and uncertainty-triggered human handoff; evaluated end to end against deterministic, single-agent, multi-agent, and no-verifier baselines.
