#!/usr/bin/env python3
"""Validate structural integrity of the Duan HOFAS skill references."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED = {
    "SKILL.md",
    "references/adversarial-tests.md",
    "references/canonical-theorems.md",
    "references/concept-lineage.md",
    "references/concepts-and-notation.md",
    "references/derivation-patterns.md",
    "references/duan-first-author-habits.md",
    "references/example-library.md",
    "references/proof-templates.md",
    "references/rigor-audit.md",
    "references/simulation-patterns.md",
    "references/source-catalog.md",
    "references/symbol-dictionary.md",
    "references/writing-style.md",
}

LINK = re.compile(r"\[[^]]+\]\(([^)]+\.md)\)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "skill",
        nargs="?",
        default=str(Path(__file__).resolve().parents[1]),
    )
    args = parser.parse_args()
    root = Path(args.skill).expanduser().resolve()
    errors: list[str] = []

    for relative in sorted(REQUIRED):
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for markdown in root.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        if "TODO" in text:
            errors.append(f"unfinished TODO in {markdown.relative_to(root)}")
        if text.count("$$") % 2:
            errors.append(f"unbalanced display-math delimiters in {markdown.relative_to(root)}")
        if "\\[" in text or "\\]" in text:
            errors.append(f"non-project math delimiter in {markdown.relative_to(root)}")
        for target in LINK.findall(text):
            resolved = (markdown.parent / target).resolve()
            if not resolved.is_file():
                errors.append(
                    f"broken Markdown link in {markdown.relative_to(root)}: {target}"
                )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Duan HOFAS distillation structure valid: {root}")
    print(f"Required knowledge files: {len(REQUIRED)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
