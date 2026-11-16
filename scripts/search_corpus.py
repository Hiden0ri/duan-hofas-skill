#!/usr/bin/env python3
"""Search Duan's unified full-text corpus (32 papers + 2026 Volume I) via SQLite FTS5."""

from __future__ import annotations

import argparse
import re
import sqlite3
from pathlib import Path

DEFAULT_DB = Path("/home/yzk/.cache/duan-hofas/duan_corpus.sqlite")


def norm_ws_keep_case(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"-\s*\n\s*", "", text)
    return re.sub(r"\s+", " ", text).strip()


def norm_ws(text: str) -> str:
    return norm_ws_keep_case(text).lower()


def fts_tokens(query: str) -> str:
    toks = re.findall(r"[\w\u4e00-\u9fa5]+", query, flags=re.UNICODE)
    if not toks:
        raise ValueError("Query has no searchable word tokens")
    return " AND ".join(f'"{t}"' for t in toks)


def main() -> None:
    parser = argparse.ArgumentParser(description="Search Duan full-text corpus (32 papers + Volume I).")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--query", help="Full-text BM25 search query")
    group.add_argument("--literal", help="Exact case-insensitive substring search")
    group.add_argument("--label", help="Formal landmark label, e.g. 'Proposition 4.1' or '定理 2'")
    group.add_argument("--list-docs", action="store_true", help="List all indexed documents")
    parser.add_argument("--series", choices=("aas", "ijss", "scis", "core", "ucfas", "odfas", "volume1"))
    parser.add_argument(
        "--kind",
        choices=("Definition", "Assumption", "Condition", "Problem", "Lemma", "Proposition", "Theorem", "Corollary", "Remark"),
    )
    parser.add_argument("--doc", help="Filter to a single doc_id, e.g. odfas_2026_part4")
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    args = parser.parse_args()

    if not args.db.is_file():
        raise SystemExit(f"Corpus DB not found: {args.db}\nRun scripts/build_papers_corpus.py first.")

    conn = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    conn.create_function("norm_ws", 1, norm_ws)
    try:
        if args.list_docs:
            sql = "SELECT doc_id, series, year, pdf_pages, title FROM documents WHERE 1=1"
            params: list = []
            if args.series:
                sql += " AND series=?"
                params.append(args.series)
            sql += " ORDER BY series, year, doc_id"
            for doc_id, series, year, pages, title in conn.execute(sql, params):
                print(f"{doc_id:25s} | {series:7s} | {year} | {pages:3d}p | {title}")
            return

        if args.label is not None:
            sql = """
                SELECT l.doc_id, l.series, l.kind, l.label, l.pdf_page, l.md_line, d.md_path, l.statement_start
                FROM landmarks l JOIN documents d ON d.doc_id=l.doc_id
                WHERE lower(l.label)=lower(?)
            """
            params = [args.label]
            if args.series:
                sql += " AND l.series=?"
                params.append(args.series)
            if args.doc:
                sql += " AND l.doc_id=?"
                params.append(args.doc)
            sql += " ORDER BY l.doc_id, l.pdf_page LIMIT ?"
            params.append(args.top)
            rows = conn.execute(sql, params).fetchall()
            for idx, (doc_id, series, kind, label, pno, md_ln, md_path, snip) in enumerate(rows, 1):
                loc = f"{md_path}#L{md_ln}" if md_path else f"printed p.{md_ln}"
                print(f"[{idx}] {doc_id} ({series}) | {label} | PDF p.{pno} | {loc}")
                print(f"    {snip}")
            if not rows:
                print("No matches.")
            return

        if args.kind is not None and args.query is not None:
            sql = """
                SELECT l.doc_id, l.series, l.label, l.pdf_page, l.md_line, d.md_path,
                       snippet(landmarks_fts, 4, '[', ']', ' … ', 32)
                FROM landmarks_fts
                JOIN landmarks l ON l.landmark_id=landmarks_fts.rowid
                JOIN documents d ON d.doc_id=l.doc_id
                WHERE landmarks_fts MATCH ? AND lower(l.kind)=lower(?)
            """
            params = [fts_tokens(args.query), args.kind]
            if args.series:
                sql += " AND l.series=?"
                params.append(args.series)
            if args.doc:
                sql += " AND l.doc_id=?"
                params.append(args.doc)
            sql += " ORDER BY bm25(landmarks_fts) LIMIT ?"
            params.append(args.top)
            rows = conn.execute(sql, params).fetchall()
            for idx, (doc_id, series, label, pno, md_ln, md_path, snip) in enumerate(rows, 1):
                loc = f"{md_path}#L{md_ln}" if md_path else f"printed p.{md_ln}"
                print(f"[{idx}] {doc_id} ({series}) | {label} | PDF p.{pno} | {loc}")
                print(f"    {snip}")
            if not rows:
                print("No matches.")
            return

        if args.query is not None:
            sql = """
                SELECT p.doc_id, p.series, p.pdf_page, p.md_line, d.md_path,
                       snippet(pages_fts, 2, '[', ']', ' … ', 32)
                FROM pages_fts
                JOIN pages p ON p.page_uid=pages_fts.rowid
                JOIN documents d ON d.doc_id=p.doc_id
                WHERE pages_fts MATCH ?
            """
            params = [fts_tokens(args.query)]
            if args.series:
                sql += " AND p.series=?"
                params.append(args.series)
            if args.doc:
                sql += " AND p.doc_id=?"
                params.append(args.doc)
            sql += " ORDER BY bm25(pages_fts) LIMIT ?"
            params.append(args.top)
            rows = conn.execute(sql, params).fetchall()
            for idx, (doc_id, series, pno, md_ln, md_path, snip) in enumerate(rows, 1):
                loc = f"{md_path}#L{md_ln}" if md_path else f"printed p.{md_ln}"
                print(f"[{idx}] {doc_id} ({series}) | PDF p.{pno} | {loc}")
                print(f"    {' '.join(snip.split())}")
            if not rows:
                print("No matches.")
            return

        # Literal substring search (whitespace- and linewrap-normalized across PDF line breaks)
        lit_norm = norm_ws(args.literal)
        sql = """
            SELECT p.doc_id, p.series, p.pdf_page, p.md_line, d.md_path, p.text
            FROM pages p JOIN documents d ON d.doc_id=p.doc_id
            WHERE instr(norm_ws(p.text), ?) > 0
        """
        params = [lit_norm]
        if args.series:
            sql += " AND p.series=?"
            params.append(args.series)
        if args.doc:
            sql += " AND p.doc_id=?"
            params.append(args.doc)
        sql += " ORDER BY p.doc_id, p.pdf_page LIMIT ?"
        params.append(args.top)
        rows = conn.execute(sql, params).fetchall()
        for idx, (doc_id, series, pno, md_ln, md_path, ptext) in enumerate(rows, 1):
            ctext = norm_ws_keep_case(ptext)
            pos = ctext.lower().find(lit_norm)
            s0 = max(0, pos - 120)
            s1 = min(len(ctext), pos + len(lit_norm) + 200)
            snip = ctext[s0:s1]
            loc = f"{md_path}#L{md_ln}" if md_path else f"printed p.{md_ln}"
            print(f"[{idx}] {doc_id} ({series}) | PDF p.{pno} | {loc}")
            print(f"    {snip}")
        if not rows:
            print("No matches.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
