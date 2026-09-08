#!/usr/bin/env python3
"""Build a page-level SQLite FTS5 index for Duan's 2026 Volume I."""

from __future__ import annotations

import argparse
import hashlib
import re
import sqlite3
import subprocess
from pathlib import Path


DEFAULT_PDF = Path("/home/yzk/Zotero/storage/688CMT53/978-981-96-8395-6.pdf")
DEFAULT_DB = Path("/home/yzk/.cache/duan-hofas/volume1.sqlite")
EXPECTED_SHA256 = "3ac437c2a236bbfe902a22401c535cb6787bae0a5b385cbb22efca609e223a78"

CHAPTERS = (
    (1, 48, "Chapter 1 — Introduction"),
    (49, 90, "Chapter 2 — Models of Global FASs"),
    (91, 126, "Chapter 3 — Control of FASs"),
    (127, 160, "Chapter 4 — Disturbance Attenuation and Decoupling"),
    (161, 196, "Chapter 5 — Robust and Adaptive Control"),
    (197, 226, "Chapter 6 — Strict Feedback Systems with Uniform Dimensions"),
    (227, 258, "Chapter 7 — Strict Feedback Systems with Increasing Dimensions"),
    (259, 302, "Chapter 8 — Nonaffine Strict Feedback Systems"),
    (303, 326, "Chapter 9 — High-Order Backstepping for Robust Control"),
    (327, 346, "Chapter 10 — High-Order Backstepping for Adaptive Control"),
    (347, 376, "Chapter 11 — Observer-Based Control"),
    (377, 404, "Chapter 12 — Robust Stabilization of Type I Systems"),
    (405, 420, "Appendix A — Controller Parameterization"),
    (421, 476, "Appendix B — Proofs of Some Theorems"),
    (477, 500, "Bibliography"),
    (501, 9999, "Index and end matter"),
)

CHAPTER_STARTS = {
    1: 1,
    2: 49,
    3: 91,
    4: 127,
    5: 161,
    6: 197,
    7: 227,
    8: 259,
    9: 303,
    10: 327,
    11: 347,
    12: 377,
}

LANDMARK_PATTERN = re.compile(
    r"^\s*(Definition|Assumption|Lemma|Theorem|Proposition|Corollary)\s+"
    r"(\d+\.\d+|\d+)\b",
    re.IGNORECASE,
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def extract_pages(pdf: Path) -> list[str]:
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf), "-"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    pages = result.stdout.decode("utf-8", errors="replace").split("\f")
    if pages and not pages[-1].strip():
        pages.pop()
    return pages


def printed_page_from_text(text: str) -> int | None:
    """Read the printed page from a running head or known chapter opener."""
    chapter = re.search(r"^Chapter\s+(\d+)\s*$", text, re.MULTILINE)
    if chapter:
        return CHAPTER_STARTS.get(int(chapter.group(1)))
    if re.search(r"^Appendix A\b", text, re.MULTILINE):
        return 405
    if re.search(r"^Appendix B\b", text, re.MULTILINE):
        return 421
    if re.search(r"^Bibliography\s*$", text, re.MULTILINE):
        return 477
    if re.search(r"^Index\s*$", text, re.MULTILINE):
        return 501

    lines = [line for line in text.splitlines() if line.strip()][:8]
    for line in lines:
        left = re.match(r"^\s*(\d{1,3})\s{2,}\S", line)
        if left:
            return int(left.group(1))
        right = re.search(r"\S\s{2,}(\d{1,3})\s*$", line)
        if right:
            return int(right.group(1))
    return None


def chapter_for(printed_page: int | None) -> str:
    if printed_page is None:
        return "Front matter"
    for first, last, title in CHAPTERS:
        if first <= printed_page <= last:
            return title
    return "Unmapped"


def build(pdf: Path, db: Path, allow_changed_source: bool) -> None:
    if not pdf.is_file():
        raise FileNotFoundError(pdf)
    source_hash = sha256(pdf)
    if source_hash != EXPECTED_SHA256 and not allow_changed_source:
        raise RuntimeError(
            "Source checksum changed. Inspect the edition, then use "
            "--allow-changed-source only if the change is intentional."
        )

    pages = extract_pages(pdf)
    chapter_one_marker = re.compile(r"Chapter\s+1\s*\n\s*Introduction", re.IGNORECASE)
    first_main = next(
        number
        for number, text in enumerate(pages, 1)
        if chapter_one_marker.search(text)
    )
    db.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(db)
    try:
        connection.executescript(
            """
            DROP TABLE IF EXISTS pages;
            DROP TABLE IF EXISTS pages_fts;
            DROP TABLE IF EXISTS metadata;
            DROP TABLE IF EXISTS landmarks;
            DROP TABLE IF EXISTS landmarks_fts;
            CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
            CREATE TABLE pages (
                pdf_page INTEGER PRIMARY KEY,
                printed_page INTEGER,
                chapter TEXT NOT NULL,
                text TEXT NOT NULL
            );
            CREATE VIRTUAL TABLE pages_fts USING fts5(
                text,
                content='pages',
                content_rowid='pdf_page',
                tokenize='unicode61 remove_diacritics 2'
            );
            CREATE TABLE landmarks (
                landmark_id INTEGER PRIMARY KEY,
                kind TEXT NOT NULL,
                label TEXT NOT NULL,
                pdf_page INTEGER NOT NULL,
                printed_page INTEGER,
                chapter TEXT NOT NULL,
                statement_start TEXT NOT NULL,
                FOREIGN KEY(pdf_page) REFERENCES pages(pdf_page)
            );
            CREATE VIRTUAL TABLE landmarks_fts USING fts5(
                label,
                statement_start,
                content='landmarks',
                content_rowid='landmark_id',
                tokenize='unicode61 remove_diacritics 2'
            );
            """
        )
        metadata = {
            "title": "Fully Actuated System Approach: Volume I. Global Fully Actuated Systems",
            "author": "Guang-Ren Duan",
            "doi": "10.1007/978-981-96-8395-6",
            "source_pdf": str(pdf.resolve()),
            "source_sha256": source_hash,
            "pdf_pages": str(len(pages)),
            "printed_page_1_pdf_page": str(first_main),
        }
        connection.executemany(
            "INSERT INTO metadata(key,value) VALUES (?,?)", metadata.items()
        )
        rows = []
        last_printed = None
        for pdf_page, text in enumerate(pages, 1):
            printed = printed_page_from_text(text) if pdf_page >= first_main else None
            if pdf_page >= first_main and printed is None and last_printed is not None:
                printed = last_printed + 1
            if printed is not None:
                last_printed = printed
            rows.append((pdf_page, printed, chapter_for(printed), text))
        connection.executemany(
            "INSERT INTO pages(pdf_page,printed_page,chapter,text) VALUES (?,?,?,?)",
            rows,
        )
        connection.execute("INSERT INTO pages_fts(pages_fts) VALUES ('rebuild')")
        landmarks = []
        for pdf_page, printed, chapter, text in rows:
            lines = text.splitlines()
            for line_number, line in enumerate(lines):
                match = LANDMARK_PATTERN.match(line)
                if not match:
                    continue
                kind = match.group(1).capitalize()
                number = match.group(2)
                label = f"{kind} {number}"
                continuation = [line.strip()]
                for following in lines[line_number + 1 : line_number + 7]:
                    if following.strip():
                        continuation.append(following.strip())
                statement = " ".join(continuation)[:1800]
                landmarks.append(
                    (kind, label, pdf_page, printed, chapter, statement)
                )
        connection.executemany(
            """INSERT INTO landmarks(
                   kind,label,pdf_page,printed_page,chapter,statement_start
               ) VALUES (?,?,?,?,?,?)""",
            landmarks,
        )
        connection.execute("INSERT INTO landmarks_fts(landmarks_fts) VALUES ('rebuild')")
        connection.commit()
    finally:
        connection.close()

    print(f"Indexed {len(pages)} PDF pages")
    print(f"Printed page 1 = PDF page {first_main}")
    print(f"SHA-256 = {source_hash}")
    print(f"Landmark candidates = {len(landmarks)}")
    print(f"Index = {db.resolve()}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--allow-changed-source", action="store_true")
    args = parser.parse_args()
    build(args.pdf, args.db, args.allow_changed_source)


if __name__ == "__main__":
    main()
