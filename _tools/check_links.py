#!/usr/bin/env python3
"""Check that every wikilink in _design/ and _backlog/ resolves to a real document.

Catches: links to documents that were renamed, never written, or misspelled.
Does not catch: links that resolve but point somewhere unhelpful.

Wikilinks inside inline code or fenced code blocks are ignored -- those are
illustrative (`[[wikilink]]`, `[[Some-NPC]]`), not references.

Usage:  python3 _tools/check_links.py
Exit:   0 clean, 1 broken links found
"""
import re
import sys
from pathlib import Path

SEARCH_DIRS = ["_design", "_backlog"]
# Link targets outside the searched dirs that are known-good, with a reason.
ALLOWED_EXTERNAL: dict[str, str] = {}

FENCE = re.compile(r"^\s*```")
INLINE_CODE = re.compile(r"`[^`]*`")
WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")


def strip_code(text: str) -> str:
    """Remove fenced blocks and inline code so illustrative links are ignored."""
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        out.append(INLINE_CODE.sub(" ", line))
    return "\n".join(out)


def link_targets(text: str):
    """Yield (target, line_number) for each real wikilink."""
    for n, line in enumerate(strip_code(text).splitlines(), 1):
        for m in WIKILINK.finditer(line):
            # Strip |alias and #anchor
            target = m.group(1).split("|")[0].split("#")[0].strip()
            if target:
                yield target, n


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    docs, files = set(), []
    for d in SEARCH_DIRS:
        for p in sorted((root / d).glob("*.md")):
            docs.add(p.stem)
            files.append(p)

    broken = []
    for p in files:
        for target, line in link_targets(p.read_text(encoding="utf-8")):
            if target not in docs and target not in ALLOWED_EXTERNAL:
                broken.append((p.relative_to(root), line, target))

    if broken:
        print(f"BROKEN LINKS: {len(broken)}\n")
        for path, line, target in broken:
            print(f"  {path}:{line}  ->  [[{target}]]")
        print("\nFix the link, write the document, or add it to ALLOWED_EXTERNAL")
        print("in this script with a reason.")
        return 1

    print(f"Links OK -- {len(files)} documents, all wikilinks resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
