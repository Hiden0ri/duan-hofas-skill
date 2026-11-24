#!/usr/bin/env python3
"""Skill-local wrapper for querying the graded secondary/backup FAS literature library."""

from __future__ import annotations

import os
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
CANDIDATE_ROOTS = [
    SKILL_ROOT / "corpus" / "backup_fas",
    Path(os.environ.get("FAS_BACKUP_LIBRARY", "")) if os.environ.get("FAS_BACKUP_LIBRARY") else None,
    Path("/home/yzk/fas-library"),
]


def _resolve_root() -> Path | None:
    for p in CANDIDATE_ROOTS:
        if p is not None and (p / "fas_library.sqlite").exists() and (p / "scripts" / "search_fas_library.py").exists():
            return p.resolve()
    return None


def main() -> None:
    root = _resolve_root()
    if root is None:
        print(
            "Error: backup FAS library not found (expected corpus/backup_fas/fas_library.sqlite or /home/yzk/fas-library).",
            file=sys.stderr,
        )
        sys.exit(1)

    scripts_dir = str(root / "scripts")
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)

    import search_fas_library as sfl

    if "--db" not in sys.argv:
        sys.argv.extend(["--db", str(root / "fas_library.sqlite")])
    sfl.main()


if __name__ == "__main__":
    main()
