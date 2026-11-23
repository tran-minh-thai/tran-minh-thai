# Thai Tran

Faculty of Information Technology, Ho Chi Minh City University of Foreign Languages - Information Technology
(HUFLIT), Ho Chi Minh City, Vietnam · ORCID [0000-0002-7671-4785](https://orcid.org/0000-0002-7671-4785)

Research on pattern mining and its evaluation: high-utility and sequential pattern mining, graph mining,
privacy-preserving pattern mining, and how evaluation protocols shape the conclusions drawn from experiments.
Each research repository below holds the code, the data preparation and the measured results behind one study,
so its numbers can be rerun.

## High-utility and sequential pattern mining

- [**pre-huspm-joint**](https://github.com/tran-minh-thai/pre-huspm-joint): Exact maintenance of high-utility sequential patterns under insertions, deletions and modifications with a joint pre-large budget: code, experiment harness, measured results and the scripts that produce the figures and tables.
- [**incremental-hausp-mining**](https://github.com/tran-minh-thai/incremental-hausp-mining): HAUSP-UB: incremental high-average-utility sequential pattern mining on quantitative sequence databases that grow in batches; three baselines and the measurement campaign.
- [**adaptive-itr-spm**](https://github.com/tran-minh-thai/adaptive-itr-spm): Adaptive Incremental Target Regular Sequential Pattern Mining (Ada-IncTaSPM): Java reference implementation and benchmark harness accompanying the submitted paper. MIT licensed.
- [**tkcm**](https://github.com/tran-minh-thai/tkcm): Top-k high-utility sequential pattern mining: one switchable engine, its baselines, and the tooling to measure them.
- [**rhuspm-miner**](https://github.com/tran-minh-thai/rhuspm-miner): Mining regular high utility sequential patterns by integrating sparse co-occurrence structures with look-ahead utility bounds — reference implementation and reproducible experiment pipeline.
- [**regular-huspm-parallel**](https://github.com/tran-minh-thai/regular-huspm-parallel): Reference implementation and experiment harness for RHUSPM-Par: parallel regular high-utility sequential pattern mining with recursive dynamic load balancing on shared-memory multi-core machines.
- [**parallel-regular-incremental-husp**](https://github.com/tran-minh-thai/parallel-regular-incremental-husp): Parallel Regular Incremental High-Utility Sequential Pattern Mining (Java).
- [**huflit-mos-spm-h2025-01**](https://github.com/tran-minh-thai/huflit-mos-spm-h2025-01): Multi-objective sequential pattern mining over data streams: a sliding window that combines support, utility and regularity (HUFLIT university research project H2025-01).

## Graph mining

- [**wfsm-bench**](https://github.com/tran-minh-thai/wfsm-bench): Weighted frequent subgraph mining as optimisation: search methods, exhaustive optima, a racing selector, and the measurements behind them.
- [**pivot-wfsm**](https://github.com/tran-minh-thai/pivot-wfsm): Memory-scalable weighted frequent subgraph mining on transactional multigraph databases via on-demand re-matching anchored at a pivot vertex.
- [**welt-weighted-fsm**](https://github.com/tran-minh-thai/welt-weighted-fsm): Reference implementation and experiments for the WeLT paper — weighted frequent subgraph mining in a single large graph via a lookup-table double filter.
- [**inchusm**](https://github.com/tran-minh-thai/inchusm): IncHUSM: incremental high-utility subgraph mining over add-only snapshot streams.
- [**husm-aml-portsplit**](https://github.com/tran-minh-thai/husm-aml-portsplit): Amount-conserving chain mining in transaction graphs: chain miner, experiment scripts and run records.

## Privacy-preserving pattern mining

- [**HideNOSP**](https://github.com/tran-minh-thai/HideNOSP): Hiding sensitive sequential patterns under non-overlapping support with gap constraints: Nettree cut index and CUT-HIDE.

## Datasets

- [**huspm-datasets**](https://github.com/tran-minh-thai/huspm-datasets): Quantitative sequence databases for high utility sequential pattern mining.
- [**graph-datasets**](https://github.com/tran-minh-thai/graph-datasets): Graph datasets for graph-mining studies: only the inputs that cannot be re-fetched from their own sources, with SHA-256 manifests.
- [**convert-spmf-to-quantitative**](https://github.com/tran-minh-thai/convert-spmf-to-quantitative): Converts standard SPMF datasets into Quantitative SPMF (QSDB) format with synthetically generated utilities for sequence mining research.

## Tools

- [**conf-tracker**](https://github.com/tran-minh-thai/conf-tracker): Calls for papers in computer science: deadlines in the venue's time zone and yours, CCF and CORE ranks, acceptance-rate history and a personal submission plan ([live site](https://tran-minh-thai.github.io/conf-tracker/)).
- [**latex-to-word**](https://github.com/tran-minh-thai/latex-to-word): A pandoc-based LaTeX-to-Word converter for academic papers. Builds an IEEE bibliography numbered by order of appearance with a DOI per entry, resolves \ref/\eqref to numbers, keeps pseudocode formulas as Word equations, and applies a .docx style template.

<sub>Generated by `tools/build_profile.py` from the public repositories of the account.</sub>
