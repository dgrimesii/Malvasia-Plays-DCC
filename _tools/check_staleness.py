#!/usr/bin/env python3
"""Flag documents whose dependencies changed after they last did.

If A links to B, and B was edited after A, then A may be describing a
version of B that no longer exists. Every stale epic found by hand was
this shape: the model moved, the epic did not.

Crude by design -- it uses commit dates, so it has false positives (a
typo fix in B flags A) and no false negatives that matter. A false
positive costs a glance; a missed staleness costs a wrong implementation.

Usage:  python3 _tools/check_staleness.py [--days N]
        --days N   only flag gaps wider than N days (default 7)

The default skips same-week churn. During a heavy editing session almost
everything looks stale for a few hours; --days 0 shows that and is rarely
what you want.
Exit:   always 0 -- this is a report, not a gate.
"""
import argparse
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

SEARCH_DIRS = ["_design", "_backlog"]
FENCE = re.compile(r"^\s*```")
INLINE_CODE = re.compile(r"`[^`]*`")
WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")


def strip_code(text: str) -> str:
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        out.append(INLINE_CODE.sub(" ", line))
    return "\n".join(out)


def targets(text: str) -> set[str]:
    found = set()
    for m in WIKILINK.finditer(strip_code(text)):
        t = m.group(1).split("|")[0].split("#")[0].strip()
        if t:
            found.add(t)
    return found


def last_commit(root: Path, rel: str):
    """ISO date of the last commit touching this path, or None."""
    out = subprocess.run(
        ["git", "log", "-1", "--format=%cI", "--", rel],
        cwd=root, capture_output=True, text=True,
    ).stdout.strip()
    if not out:
        return None
    return datetime.fromisoformat(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7,
                    help="only flag gaps wider than N days (default 7)")
    args = ap.parse_args()

    root = Path(__file__).resolve().parent.parent
    paths, dates = {}, {}
    for d in SEARCH_DIRS:
        for p in sorted((root / d).glob("*.md")):
            rel = str(p.relative_to(root))
            paths[p.stem] = (p, rel)
            dates[p.stem] = last_commit(root, rel)

    stale = []
    for stem, (p, rel) in paths.items():
        mine = dates.get(stem)
        if mine is None:
            continue
        newer = []
        for t in sorted(targets(p.read_text(encoding="utf-8"))):
            theirs = dates.get(t)
            if theirs and theirs > mine:
                gap = (theirs - mine).days
                if gap >= args.days:
                    newer.append((t, gap))
        if newer:
            stale.append((rel, mine, sorted(newer, key=lambda x: -x[1])))

    if not stale:
        print("No staleness found -- every document is at least as new as what it links to.")
        return 0

    stale.sort(key=lambda x: -max(g for _, g in x[2]))
    print(f"POSSIBLY STALE: {len(stale)} documents\n")
    for rel, mine, newer in stale:
        print(f"  {rel}  (last touched {mine:%Y-%m-%d})")
        for t, gap in newer:
            print(f"      {t} changed {gap}d later")
        print()
    print("A flag means 'reread this', not 'this is wrong'. Clear it by")
    print("reviewing and touching the document, or by ignoring it knowingly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
