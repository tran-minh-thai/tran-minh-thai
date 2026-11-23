#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build the profile README from the account's public repositories.

    python3 tools/build_profile.py            write README.md
    python3 tools/build_profile.py --check    exit non-zero if README.md is stale
    python3 tools/build_profile.py --self-test

Reads the public, non-archived repositories of the account with the GitHub CLI (`gh repo list`). Each one is
placed in exactly one group of GROUPS; a public repository no group names goes to "Other projects" and is
reported, so a newly published repository is never left off the page silently. A name in GROUPS that is no
longer public is reported too and left out. The text of each entry is the repository's own description,
unless DESCRIPTIONS gives one (for an empty, keyword-only or non-English description).
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ACCOUNT = "tran-minh-thai"
ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

HEADER = """<div align="center">

# Thai Tran

**Researcher and Lecturer in Computer Science**<br>
Faculty of Information Technology · Ho Chi Minh City University of Foreign Languages - Information Technology (HUFLIT)

[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--7671--4785-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0000-0002-7671-4785)
![Affiliation](https://img.shields.io/badge/HUFLIT-Faculty%20of%20IT-005BAA)
![Location](https://img.shields.io/badge/Ho%20Chi%20Minh%20City-Vietnam-555555)

</div>

---

### Research

- **High-utility and sequential pattern mining**: exact and incremental algorithms, upper bounds that prune the search space, and parallel miners.
- **Graph mining**: weighted and high-utility subgraph mining in graph databases and single large graphs.
- **Privacy-preserving pattern mining**: hiding sensitive sequential patterns under gap constraints.
- **Evaluation methodology**: how splitting and evaluation protocols shape the conclusions drawn from experiments.

Each research repository holds the code, the data preparation and the measured results behind one study, so its
numbers can be rerun.
"""

# group title -> repositories, in the order shown
GROUPS = [
    ("High-utility and sequential pattern mining", [
        "pre-huspm-joint", "incremental-hausp-mining", "adaptive-itr-spm", "tkcm", "rhuspm-miner",
        "regular-huspm-parallel", "parallel-regular-incremental-husp", "huflit-mos-spm-h2025-01"]),
    ("Graph mining", ["wfsm-bench", "pivot-wfsm", "welt-weighted-fsm", "inchusm", "husm-aml-portsplit"]),
    ("Privacy-preserving pattern mining", ["HideNOSP"]),
    ("Datasets", ["huspm-datasets", "graph-datasets", "convert-spmf-to-quantitative"]),
    ("Tools", ["conf-tracker", "latex-to-word"]),
]
OTHER = "Other projects"
# shown in place of the repository's own description
DESCRIPTIONS = {
    "conf-tracker": "Calls for papers in computer science: deadlines in the venue's time zone and yours, CCF and CORE "
                    "ranks, acceptance-rate history and a personal submission plan "
                    "([live site](https://tran-minh-thai.github.io/conf-tracker/)).",
    "incremental-hausp-mining": "HAUSP-UB: incremental high-average-utility sequential pattern mining on quantitative "
                                "sequence databases that grow in batches; three baselines and the measurement campaign.",
    "huflit-mos-spm-h2025-01": "Multi-objective sequential pattern mining over data streams: a sliding window that "
                               "combines support, utility and regularity (HUFLIT university research project H2025-01).",
}
EXCLUDED = {ACCOUNT}   # the profile repository itself


def public_repositories() -> list[dict]:
    out = subprocess.run(["gh", "repo", "list", ACCOUNT, "--visibility", "public", "--limit", "500",
                          "--json", "name,description,isArchived,url,primaryLanguage"], capture_output=True, text=True, check=True).stdout
    return [r for r in json.loads(out) if not r["isArchived"] and r["name"] not in EXCLUDED]


def render(repos: list[dict]) -> tuple[str, list[str], list[str]]:
    """(README text, public repositories no group names, grouped names that are not public)."""
    by_name = {r["name"]: r for r in repos}
    placed = [n for _, names in GROUPS for n in names]
    duplicates = sorted({n for n in placed if placed.count(n) > 1})
    if duplicates:
        raise SystemExit(f"[refused] placed in two groups: {duplicates}")
    unplaced = sorted(set(by_name) - set(placed))
    gone = sorted(set(placed) - set(by_name))
    lines = [HEADER.rstrip(), "", "---", "", "### Projects", ""]
    for title, names in GROUPS + [(OTHER, unplaced)]:
        shown = [n for n in names if n in by_name]
        if not shown:
            continue
        lines += [f"#### {title}", "", "| Project | Description | Language |", "|:--|:--|:--|"]
        for n in shown:
            text = DESCRIPTIONS.get(n) or (by_name[n]["description"] or "").strip()
            if not text:
                raise SystemExit(f"[refused] {n} has no description; add one to DESCRIPTIONS")
            language = (by_name[n].get("primaryLanguage") or {}).get("name") or "-"
            cell = text.rstrip(".").replace("|", "\\|") + "."
            lines.append(f"| [**{n}**]({by_name[n]['url']}) | {cell} | {language} |")
        lines.append("")
    lines += ["---", "", "<sub>This page is generated by `tools/build_profile.py` from the public repositories of the "
              "account.</sub>", ""]
    return "\n".join(lines), unplaced, gone


def self_test() -> int:
    repos = [{"name": "tkcm", "description": "Top-k mining", "url": "u1"},
             {"name": "new-repo", "description": "Something new", "url": "u2"}]
    text, unplaced, gone = render(repos)
    checks = [("a repository no group names goes to the other group and is reported",
               unplaced == ["new-repo"] and "#### Other projects" in text and "new-repo" in text),
              ("a grouped repository that is not public is reported and left out",
               "wfsm-bench" in gone and "wfsm-bench" not in text),
              ("an empty group is not shown", "#### Tools" not in text),
              ("a table cell escapes a vertical bar", "a \\| b" in render([{"name": "tkcm", "description": "a | b",
                                                                            "url": "u"}])[0]),
              ("a description override replaces the repository's own",
               DESCRIPTIONS["conf-tracker"].split(":")[0] in render([{"name": "conf-tracker", "description": "", "url": "u"}])[0])]
    try:
        render([{"name": "pivot-wfsm", "description": "", "url": "u"}])
        checks.append(("a repository with no description is refused", False))
    except SystemExit:
        checks.append(("a repository with no description is refused", True))
    for name, ok in checks:
        print(f"  {'ok    ' if ok else 'FAILED'} {name}")
    passed = sum(ok for _, ok in checks)
    print(f"\n{passed}/{len(checks)} checks passed")
    return 0 if passed == len(checks) else 1


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()
    text, unplaced, gone = render(public_repositories())
    for n in unplaced:
        print(f"note: {n} is public and in no group; listed under '{OTHER}'")
    for n in gone:
        print(f"note: {n} is grouped but not public; left out")
    if "--check" in sys.argv:
        stale = not README.exists() or README.read_text(encoding="utf-8") != text
        print("stale" if stale else "up to date")
        return 1 if stale else 0
    README.write_text(text, encoding="utf-8")
    print(f"wrote {README.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
