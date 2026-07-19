# Search and Verification Strategy

## Snapshot and objective

- Search snapshot: **2026-07-19**
- Objective: build a reproducible, living literature catalog for the PhysChronoGrid research line.
- Included records after title-level deduplication: **156**.

## Sources searched

1. IEEE Xplore and official IEEE-hosted accepted manuscripts.
2. Crossref DOI metadata for title, venue, and year verification.
3. arXiv for fast-moving LLM, agentic AI, time-series foundation model, and code-generation work.
4. OpenReview, ACL Anthology, PMLR, AAAI, IJCAI, ACM Digital Library, Nature Portfolio, Elsevier/ScienceDirect, Wiley/IET, and institutional repositories.
5. GitHub project pages only for locating code linked to an identifiable paper; GitHub projects without a paper are placed in resources rather than silently treated as publications.

## Query families

```text
("large language model" OR LLM OR "foundation model") AND
("power system" OR "smart grid" OR "active distribution network")

(agent OR "multi-agent" OR MCP OR RAG OR "tool calling") AND
("power flow" OR OPF OR dispatch OR contingency OR diagnosis)

("multi-horizon" OR "multi-scale" OR "time series foundation model") AND
(load OR wind OR PV OR voltage OR "power forecasting")

("graph neural network" OR STGNN OR "spatio-temporal") AND
(distribution OR grid OR OPF OR FDIA OR fault)

("physics-informed" OR "physics-guided" OR verifier OR feasibility) AND
(power OR voltage OR dispatch OR control)

("false data injection" OR cyber-physical OR "incipient fault") AND
(detection OR localization OR diagnosis OR explanation)
```

Targeted venue filters included `IEEE Transactions on Smart Grid`, `IEEE Transactions on Power Systems`, `IEEE Transactions on Sustainable Energy`, `IEEE Transactions on Industrial Informatics`, `IEEE Transactions on Power Delivery`, `IEEE Transactions on Neural Networks and Learning Systems`, and `CSEE Journal of Power and Energy Systems`.

## Inclusion criteria

- Directly studies LLMs, agents, forecasting, graph learning, cyber-physical diagnosis, physics-guided verification, XAI, or benchmark infrastructure relevant to PhysChronoGrid.
- Peer-reviewed journal/conference papers, reputable preprints, official white papers, or benchmark/tool papers with stable primary records.
- English-language metadata and a stable paper URL.
- Generic time-series/graph papers are retained only when they are influential baselines or practically useful for the planned experiments.

## Exclusion criteria

- Energy articles with no meaningful connection to electric grids, forecasting, operation, or diagnostic decision support.
- Purely promotional pages without an identifiable scholarly record.
- Duplicate preprint/published versions, except where the preprint has a distinct open-source artifact and is explicitly labeled.
- References whose title or publication record could not be independently confirmed.

## Verification protocol

1. Normalize titles and remove exact-title duplicates.
2. Prefer DOI, IEEE Xplore, publisher, arXiv, OpenReview, ACL Anthology, or institutional repository links over aggregator pages.
3. Check that year and venue match the primary record or Crossref metadata.
4. Mark arXiv/SSRN/Research Square/white papers as non-peer-reviewed.
5. Add a code link only when a paper/project page identifies the repository or the repository identifies the paper.
6. Run `python scripts/validate_catalog.py` to check required fields, duplicate titles, unique IDs, and URL schemes.

## Distribution summary

- Status counts: {'published': 124, 'preprint': 26, 'workshop': 2, 'preprint-version': 1, 'early-access': 1, 'project': 1, 'white-paper': 1}
- Publication years: {2026: 21, 2025: 34, 2024: 35, 2023: 14, 2022: 10, 2021: 12, 2020: 12, 2019: 6, 2018: 4, 2017: 3, 2016: 1, 2011: 1, 2009: 2, 2001: 1}
- Most represented venues: {'arXiv': 22, 'IEEE Transactions on Smart Grid': 11, 'ICLR': 11, 'IEEE Transactions on Power Systems': 9, 'IEEE Access': 7, 'ICML': 7, 'NeurIPS': 7, 'AAAI': 5, 'IEEE Transactions on Industrial Informatics': 3, 'Energy and AI': 2}

## Coverage advisory

The direct LLM/agent literature is heavily concentrated in 2024–2026 because the field is new. The catalog intentionally compensates by including older foundational work on FDIA, power-system simulation, OPF, time-series forecasting, graph learning, and physical validation. This temporal skew reflects field emergence, not a claim that earlier power-system AI research is unimportant.

## Known limitations

- No database can guarantee “all papers,” especially for newly posted preprints and early-access records.
- Some 2026 records may later receive final volume/issue/page metadata.
- The generic time-series and graph-learning fields are too large for exhaustive coverage; these sections are curated baseline sets.
- Code availability can change after the snapshot date.
- Chinese-language databases were not treated as a primary corpus; English-language formal records are prioritized for an IEEE-facing manuscript.

## Maintenance rule

Re-run targeted searches monthly during active manuscript development and immediately before submission. When a preprint receives a formal DOI, update the venue/status and prefer the published record.
