#!/usr/bin/env python3
"""Find Glossary terms that appear to be re-defined outside the Glossary.

A concept should be defined in one place. Everywhere else links to it and
may state implications -- never the definition. A second copy is what
drifts, and every definitional problem found by hand was a term carrying
two or three definitions at once.

The check is deliberately crude. It looks for the restatement pattern --
a bolded term followed by a dash or 'is' -- which is how a definition
gets written in these documents. It will over-report; a term appearing
definitionally in three documents is the signal worth a look, not any
single hit.

Usage:  python3 _tools/check_definitions.py [--min N]
        --min N   only report terms restated in N or more documents (default 2)
Exit:   always 0 -- this is a report, not a gate.
"""
import argparse
import re
import sys
from pathlib import Path

GLOSSARY = "_design/Glossary.md"
SEARCH_DIRS = ["_design", "_backlog"]

# A glossary entry: **Term** *[marking]* -- ...
ENTRY = re.compile(r"^\*\*(.+?)\*\*\s*(?:,\s*[^*]+)?\*\[")
FENCE = re.compile(r"^\s*```")


def glossary_terms(path: Path) -> list[str]:
    terms = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ENTRY.match(line)
        if m:
            # "Game master**, GM *[game]*" -> take the first name only
            terms.append(m.group(1).split("**")[0].strip())
    return terms


def restatements(text: str, term: str):
    """Yield line numbers where the term looks like it is being defined."""
    pattern = re.compile(
        r"\*\*" + re.escape(term) + r"\*\*\s*(?:\*\[[^\]]*\]\*\s*)?[\u2014\u2013-]|"
        r"\*\*" + re.escape(term) + r"\*\*\s+is\s",
        re.IGNORECASE,
    )
    in_fence = False
    for n, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if "[[Glossary]]" in line:
            # Linking to the definition and then elaborating is the correct
            # pattern, not a restatement.
            continue
        if pattern.search(line):
            yield n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--min", type=int, default=2,
                    help="only report terms restated in N or more documents")
    args = ap.parse_args()

    root = Path(__file__).resolve().parent.parent
    gpath = root / GLOSSARY
    if not gpath.exists():
        print(f"Glossary not found at {GLOSSARY}")
        return 0

    terms = glossary_terms(gpath)
    findings = {}
    for d in SEARCH_DIRS:
        for p in sorted((root / d).glob("*.md")):
            if p == gpath:
                continue
            text = p.read_text(encoding="utf-8")
            for term in terms:
                hits = list(restatements(text, term))
                if hits:
                    findings.setdefault(term, []).append(
                        (str(p.relative_to(root)), hits)
                    )

    reported = {t: f for t, f in findings.items() if len(f) >= args.min}
    print(f"Glossary terms: {len(terms)}")

    if not reported:
        print(f"No term is restated definitionally in {args.min}+ documents.")
        return 0

    print(f"RESTATED IN {args.min}+ DOCUMENTS: {len(reported)} terms\n")
    for term in sorted(reported, key=lambda t: -len(reported[t])):
        print(f"  {term}  ({len(reported[term])} documents)")
        for path, lines in reported[term]:
            print(f"      {path}:{','.join(str(n) for n in lines)}")
        print()
    print("Not every hit is a problem -- a document may legitimately restate a")
    print("term it owns. Check whether the definitions actually agree, and")
    print("whether one of them should be a link instead.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
