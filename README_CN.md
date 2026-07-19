# Awesome PhysChronoGrid Papers 中文说明

本仓库是面向 PhysChronoGrid 论文项目整理的可持续更新文献库，快照日期为 **2026-07-19**。当前收录 **156** 篇论文/正式资源，其中 **32** 篇来自 IEEE Transactions 系列。

## 研究边界

仓库围绕以下链路组织文献：

> 多时间尺度预测 → 拓扑/时空推理 → 信息物理异常诊断 → LLM/多智能体报告与建议 → 物理可行性验证 → 人工审批

因此，它既包含直接研究“电力系统大模型/智能体”的论文，也包含支撑实验设计的 PatchTST、时空图网络、物理引导 GNN、安全控制、FDIA 检测、可解释性和标准仿真网络。

## 建议阅读顺序

1. 先读 `Surveys, Perspectives, and Research Agendas`，建立领域全景。
2. 再读 `LLM Agents for Power-System Analysis and Simulation`，了解与本项目最接近的工作。
3. 重点对比 `PowerChain`、`Enhancing LLMs for Power System Simulations`、`GridMind`、`Grid-Agent`、`X-GridAgent` 和 `LLM4DistReconfig`。
4. 从预测、图学习、物理校验和信息物理异常四个板块选择基线。
5. 使用 [相关工作地图](docs/RELATED_WORK_MAP.md)撰写论文 Related Work 和 novelty boundary。

## 分类数量

- 综述、观点与研究议程：15
- 电力系统分析、仿真与科研智能体：20
- 调度、控制、市场与优化：13
- 能源预测中的 LLM 与基础模型：15
- 通用时间序列预测模型：29
- 电力系统图学习与时空建模：18
- 物理引导学习、安全控制与验证：12
- 信息物理异常检测与故障诊断：16
- 可解释性、报告生成与人工监督：6
- 基准网络、数据集与仿真工具：12

## 文件说明

- `README.md`：GitHub 首页论文清单。
- `data/papers.csv`：适合 Excel、Pandas 和人工筛选。
- `data/papers.json`：适合脚本和网页生成。
- `docs/TRANSACTIONS_INDEX.md`：IEEE Transactions 专项索引。
- `docs/RELATED_WORK_MAP.md`：对 PhysChronoGrid 的直接启示与创新重叠。
- `docs/SEARCH_STRATEGY.md`：检索、纳排、核验和局限性。
- `scripts/validate_catalog.py`：本地或 GitHub Actions 自动检查重复、字段和 URL 格式。

## 状态说明

- 🟢：正式期刊、正式会议或可核验出版记录。
- 🟡：arXiv、Research Square、SSRN 或白皮书。
- 预印本不能在论文中写成“已发表于某 Transactions”，除非后续核验到正式 DOI。

## 上传 GitHub

解压后进入仓库目录，执行：

```bash
git init
git add .
git commit -m "Initial literature catalog"
git branch -M main
git remote add origin <your-repository-url>
git push -u origin main
```

正式上传前，可在 `CITATION.cff` 中把维护者名称改成你的姓名或团队名称。
