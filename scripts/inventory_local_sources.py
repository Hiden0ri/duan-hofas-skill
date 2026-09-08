#!/usr/bin/env python3
"""List likely FAS/HOFAS PDFs in a Zotero storage tree without modifying Zotero."""

from __future__ import annotations

import argparse
from pathlib import Path


TERMS = ("fully actuated", "fully-actuated", "subfully", "sub-fully", "全驱")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "root",
        nargs="?",
        default="/home/yzk/Zotero/storage",
        help="Zotero storage directory",
    )
    args = parser.parse_args()
    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    matches = [
        path
        for path in root.rglob("*.pdf")
        if any(term.casefold() in path.name.casefold() for term in TERMS)
    ]
    for path in sorted(matches, key=lambda item: str(item).casefold()):
        print(path)
    print(f"\nTotal unique PDF paths: {len(matches)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
