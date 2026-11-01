# Search and Verification Strategy — 2026-11-01

## Baseline and scope

- Baseline: supplied ZIP dated **2026-07-19**, commit `9a10f0a605d85bbcb5ea2ef19bc365fc9fd150e6`, matched against the public repository's latest commit.
- Search cutoff: **2026-11-01, Asia/Shanghai**. This is the search date, not a guarantee of database completeness.
- Preserved all 156 legacy records/IDs; added 68 and corrected 6, yielding 224 records.
- Additions comprise 27 date-verified post-cutoff public/preprint/conference releases, 39 historical backfills, and 2 confirmed bibliographic identities with unresolved first-online dates.
- Graph + LLM adds 34 records and 2 cross-references. Cross-references and Transactions spotlight entries do not add data rows.
- P016/P029 are inherited PowerChain versions, not independent studies; counts use “records.”

## Sources actually used

1. arXiv search and official Atom API: titles, authors, first submission, update dates, abstracts, comments, journal references and related DOIs.
2. Crossref publisher-deposited DOI metadata, checked against titles and primary publication records. DOI `created` is a registration date, not a publication date.
3. IEEE Xplore records/search extracts; Elsevier, Springer, ACM and AAAI; institutional author records when direct access was restricted.
4. ACL Anthology, PMLR, NeurIPS proceedings, OpenReview and official research-lab pages.
5. Paper-linked GitHub repositories for code provenance; public repository HEAD checked with the connected GitHub tool.

Secondary search results were discovery leads, not the sole basis for new bibliographic identities. This was not a Scopus/Web of Science export. OpenAlex and Semantic Scholar APIs were not used.

## Search families

```text
("power system" OR "power grid" OR "smart grid")
AND ("language model" OR LLM OR agentic)

("power system" OR "smart grid")
AND (MCP OR "tool use" OR "dynamic simulation" OR "fault diagnosis"
     OR "load forecasting" OR restoration OR verification)

(graph OR "graph computation" OR GNN OR GraphRAG)
AND (LLM OR "large language model")

("IEEE Transactions on Smart Grid" OR "IEEE Transactions on Power Systems"
 OR "IEEE Transactions on Industrial Informatics")
AND ("large language" OR agent)
```

Recent searches included `after:2026-07-19 before:2026-11-02` and September/October windows. Search filters aid discovery; inclusion dates come from records.

The broad official arXiv API query was:

```text
(all:"power system" OR all:"power grid" OR all:"smart grid")
AND (all:"language model" OR all:LLM OR all:agentic)
sortBy=submittedDate; sortOrder=descending; max_results=100
```

The 100 returned candidates reached back into March 2026. They were screened for relevance; conventional control/MARL without a meaningful LLM connection and GPU-efficiency papers unrelated to grid decision support were not automatically included. Targeted searches and ID lookups supplemented this list, including VeraGrid-Agent and graph foundations. Boolean queries can be noisy or incomplete; this list is not definitive coverage.

## Selection and dates

- Include grid LLM agents, simulation/optimization, risk/fault diagnosis, evidence reporting, validation and relevant benchmarks.
- Curate Graph + LLM computation/encoding, GNN alignment, GraphRAG/reasoning/memory and electrical applications. Older foundations are explicitly backfills.
- Prefer verified formal versions; separately link open arXiv/PDF versions.
- A submission, unverified acceptance comment or arXiv DOI does not establish formal publication.
- Preprints use first-submission year. Formal versions use the verified conference/final-publication year; Early Access is explicit.
- P020 explicitly distinguishes online availability in 2026 from its January 2027 issue. Cite 2027 when using final-issue metadata.
- Later arXiv uploads do not make older publications new: GraLan is ISWC 2025 despite its 2026 arXiv ID.
- Existing IDs are updated in place rather than adding another row for a formal version. P020/P028/P041/P053 were upgraded this way.
- New entries with earlier preprints use the earliest verified release for date grouping. The FCS position paper is a backfill with an October 2026 formal publication.
- Two entries with unresolved first-online dates are separated as `date_unresolved`; DOI registration dates appear only in notes.

## Verification trail and limits

`data/verification_2026-11-01.json` records sources, arXiv dates, PDFs, subcategories and caveats for every added/modified entry. `data/changes_2026-11-01.json` preserves six before/after corrections.

GraLan's mismatched arXiv-related DOI was corrected against the Springer chapter (`_33`, not `_3`). The `PAKDD 2066` comment on another record was not accepted as publication evidence. Revised PowerAtlas, GraphWiz and GNN-RAG titles were checked.

- This is a curated update, not an exhaustive or full-text systematic review. Most screening used bibliographic metadata and abstracts; experimental claims were not independently reproduced.
- Unchanged legacy entries were not all re-audited. Check publication status before manuscript citation.
- Anti-bot restrictions prevented reading some IEEE/publisher pages. Crossref confirmed identities/venues/years where possible; unresolved dates remain explicit.
- All 17 distinct GitHub repositories reported for new code/resource links were checked: 16 were accessible; GraphInfer-Bench returned 404 and its code link was removed from the main list while preserving the reported URL in verification metadata. Code links do not imply execution or reproducibility verification. Code availability and publication status may change after this snapshot.
- GraphRAG findings do not prove electrical feasibility. Generic graph methods are supporting literature unless tested on a power task.
- Chinese databases were not systematically searched; English primary records for an IEEE-facing manuscript were prioritized.

## Local validation

Run `python3 scripts/validate_catalog.py` and `python3 scripts/validate_update.py`. They check fields, duplicate titles/DOIs, IDs, URL format, CSV/JSON agreement, change evidence, graph counts, README inclusion and local Markdown targets. They are not a complete live-link audit or scientific replication.
