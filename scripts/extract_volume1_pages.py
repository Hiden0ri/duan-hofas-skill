#!/usr/bin/env python3
"""Extract at most 21 consecutive PDF pages from Duan Volume I."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


DEFAULT_PDF = Path("/home/yzk/Zotero/storage/688CMT53/978-981-96-8395-6.pdf")


def page_range(value: str) -> tuple[int, int]:
    try:
        first_text, last_text = value.split(":", 1)
        first, last = int(first_text), int(last_text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Use FIRST:LAST, for example 120:124") from exc
    if first < 1 or last < first or last - first > 20:
        raise argparse.ArgumentTypeError("Range must be ordered and contain at most 21 pages")
    return first, last


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf-pages", required=True, type=page_range)
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    args = parser.parse_args()
    first, last = args.pdf_pages
    result = subprocess.run(
        ["pdftotext", "-f", str(first), "-l", str(last), "-layout", str(args.pdf), "-"],
        check=False,
    )
    if result.returncode not in (0, -13, 141):
        raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
