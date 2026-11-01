# Awesome PhysChronoGrid Papers 中文说明

检索更新至 **2026-11-01**。当前共有 **224 条文献/正式资源记录**，其中 **43 条 IEEE Transactions 记录**；本轮新增 **68 条**，修订原有 **6 条**。完整明细见 [更新说明](docs/UPDATE_2026-11-01_CN.md)。计数包含原有 PowerChain 的早期预印本和正式版关联记录，不等同于独立研究数。

## 研究边界

多时间尺度预测 → 拓扑/时空推理 → 信息物理异常诊断 → LLM/多智能体报告与建议 → 物理可行性验证 → 人工监督。

新增独立章节 [Graph 计算 + LLM 技术探索](docs/GRAPH_LLM.md)，包括综述、图算法与基准、GNN–LLM 融合、GraphRAG/证据记忆以及电网应用。通用方法用于研究借鉴，其结论不能直接当作电网安全验证。

## 分类数量

- 综述、观点与研究议程：19 条
- 电力系统分析、仿真与科研智能体：29 条
- 调度、控制、市场与优化：18 条
- 能源预测中的 LLM 与基础模型：18 条
- 通用时间序列预测模型：29 条
- 电力系统图学习与时空建模：18 条
- 物理引导学习、安全控制与验证：13 条
- 信息物理异常检测与故障诊断：19 条
- 可解释性、报告生成与人工监督：9 条
- 基准网络、数据集与仿真工具：18 条
- Graph 计算 + LLM：方法、基准与电力系统探索：34 条

## 文件说明

- `README.md`：沿用原版年份、期刊/会议/预印本、题目和链接的首页清单。
- `data/papers.csv`、`data/papers.json`：保持原十个字段，方便继续维护。
- `data/verification_2026-11-01.json`：本次新增和修改条目的核验来源、日期、开放 PDF、版本说明。
- `data/changes_2026-11-01.json`：新增 ID 及旧条目修改前后对照。
- `docs/GRAPH_LLM.md`：独立 Graph + LLM 文献专章。
- `docs/UPDATE_2026-11-01_CN.md`：新增、补录、状态升级和上传方式。
- `docs/RELATED_WORK_MAP.md`：更新后的阅读优先级与研究边界。
- `docs/SEARCH_STRATEGY.md`：本次检索方法和局限。
- `docs/TRANSACTIONS_INDEX.md`：IEEE Transactions 专项索引。

## 状态与日期

🟢 为正式论文/可核验会议记录；🟡 为预印本/白皮书。Early Access 单独注明。年份按所链接正式版本的年标或预印本首发年；跨年 online-first 条目明确标注在线年和正式刊期年。日期未核准的记录不计入“截止日期后首次公开”数量。

原仓库中的未改动旧条目没有在本轮逐条重新审计。最新文献清单是截至检索日的精选更新，不是数据库穷尽检索。

## 建议阅读

先读 2026 年智能电网 Agent 教程、PowerAgentBench-SS、RestoreBench 和 PowerBench；Graph 路线先读图计算综述、GraphArena、G-Retriever、PowerGraph-LLM、CIM/CGMES 图检索和电网级联预测融合论文。详见 [相关工作地图](docs/RELATED_WORK_MAP.md)。

## 上传

将更新包内仓库文件上传至你现有仓库根目录并替换同名文件；不需要重新初始化仓库。上传前可执行两个验证脚本。`CITATION.cff` 的维护者名称沿用原版，可自行改为真实维护者。
