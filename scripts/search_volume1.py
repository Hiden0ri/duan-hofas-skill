#!/usr/bin/env python3
"""Search Duan Volume I by page and return source locators."""

from __future__ import annotations

import argparse
import re
import sqlite3
from pathlib import Path


DEFAULT_DB = Path("/home/yzk/.cache/duan-hofas/volume1.sqlite")


def normalized_fts_query(query: str) -> str:
    tokens = re.findall(r"[\w]+", query, flags=re.UNICODE)
    if not tokens:
        raise ValueError("Query contains no searchable tokens")
    return " AND ".join(f'"{token}"' for token in tokens)


def search_fts(connection: sqlite3.Connection, query: str, top: int):
    return connection.execute(
        """
        SELECT p.pdf_page, p.printed_page, p.chapter,
               snippet(pages_fts, 0, '[', ']', ' … ', 28),
               bm25(pages_fts)
        FROM pages_fts
        JOIN pages p ON p.pdf_page=pages_fts.rowid
        WHERE pages_fts MATCH ?
        ORDER BY bm25(pages_fts)
        LIMIT ?
        """,
        (normalized_fts_query(query), top),
    ).fetchall()


def search_literal(connection: sqlite3.Connection, literal: str, top: int):
    rows = connection.execute(
        """
        SELECT pdf_page, printed_page, chapter, text
        FROM pages
        WHERE instr(lower(text), lower(?)) > 0
        ORDER BY pdf_page
        LIMIT ?
        """,
        (literal, top),
    ).fetchall()
    output = []
    for pdf_page, printed, chapter, page_text in rows:
        position = page_text.lower().find(literal.lower())
        start = max(0, position - 180)
        end = min(len(page_text), position + len(literal) + 260)
        snippet = " ".join(page_text[start:end].split())
        output.append((pdf_page, printed, chapter, snippet, None))
    return output


def search_label(connection: sqlite3.Connection, label: str, top: int):
    return connection.execute(
        """
        SELECT pdf_page, printed_page, chapter, statement_start, NULL
        FROM landmarks
        WHERE lower(label)=lower(?)
        ORDER BY pdf_page
        LIMIT ?
        """,
        (label, top),
    ).fetchall()


def search_landmarks(connection: sqlite3.Connection, query: str, kind: str, top: int):
    sql = """
        SELECT l.pdf_page, l.printed_page, l.chapter,
               snippet(landmarks_fts, 1, '[', ']', ' … ', 32),
               bm25(landmarks_fts)
        FROM landmarks_fts
        JOIN landmarks l ON l.landmark_id=landmarks_fts.rowid
        WHERE landmarks_fts MATCH ? AND lower(l.kind)=lower(?)
        ORDER BY bm25(landmarks_fts)
        LIMIT ?
    """
    return connection.execute(sql, (normalized_fts_query(query), kind, top)).fetchall()


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--query")
    group.add_argument("--literal")
    group.add_argument("--label", help="Exact landmark label, e.g. 'Theorem 5.1'")
    parser.add_argument(
        "--kind",
        choices=("Definition", "Assumption", "Lemma", "Theorem", "Proposition", "Corollary"),
        help="With --query, search only extracted statement openings of this kind",
    )
    parser.add_argument("--top", type=int, default=8)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    args = parser.parse_args()

    if not args.db.is_file():
        raise SystemExit(f"Index not found: {args.db}\nRun build_volume1_index.py first.")
    connection = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    try:
        if args.label is not None:
            rows = search_label(connection, args.label, args.top)
        elif args.query is not None and args.kind is not None:
            rows = search_landmarks(connection, args.query, args.kind, args.top)
        elif args.query is not None:
            rows = search_fts(connection, args.query, args.top)
        else:
            rows = search_literal(connection, args.literal, args.top)
    finally:
        connection.close()

    if not rows:
        print("No matches")
        return
    for number, (pdf_page, printed, chapter, snippet, score) in enumerate(rows, 1):
        printed_label = str(printed) if printed is not None else "front matter"
        score_label = f" | score={score:.4f}" if score is not None else ""
        print(f"[{number}] PDF p.{pdf_page} | printed p.{printed_label} | {chapter}{score_label}")
        print(snippet.strip())
        print()


if __name__ == "__main__":
    main()
