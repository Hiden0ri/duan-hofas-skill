#!/usr/bin/env python3
"""Inventory Duan-first-author FAS records from a Zotero database, read-only."""

from __future__ import annotations

import argparse
import re
import sqlite3
from pathlib import Path


TITLE_TERMS = (
    "fully actuated",
    "fully-actuated",
    "subfully",
    "sub-fully",
    "全驱",
    "high-order system approach",
    "高阶系统方法",
)
FAS_TOKEN = re.compile(r"(?<![a-z])(?:ho)?fas(?:s)?(?![a-z])", re.IGNORECASE)

QUERY = """
WITH first_creator AS (
  SELECT ic.itemID, c.firstName, c.lastName
  FROM itemCreators AS ic
  JOIN creators AS c ON c.creatorID = ic.creatorID
  WHERE ic.orderIndex = 0
), titles AS (
  SELECT d.itemID, v.value AS title
  FROM itemData AS d
  JOIN fields AS f ON f.fieldID = d.fieldID
  JOIN itemDataValues AS v ON v.valueID = d.valueID
  WHERE f.fieldName = 'title'
)
SELECT p.key, t.title, a.key, ia.path, fc.firstName, fc.lastName
FROM items AS p
JOIN first_creator AS fc ON fc.itemID = p.itemID
JOIN titles AS t ON t.itemID = p.itemID
LEFT JOIN itemAttachments AS ia ON ia.parentItemID = p.itemID
LEFT JOIN items AS a ON a.itemID = ia.itemID
WHERE lower(fc.lastName) = 'duan' OR fc.lastName LIKE '%段%'
ORDER BY lower(t.title), a.key
"""


def relevant(title: str) -> bool:
    folded = title.casefold()
    return any(term.casefold() in folded for term in TITLE_TERMS) or bool(
        FAS_TOKEN.search(title)
    )


def attachment_path(storage: Path, key: str | None, raw: str | None) -> str:
    if not raw:
        return "[no attachment]"
    if raw.startswith("storage:") and key:
        return str(storage / key / raw.removeprefix("storage:"))
    return raw


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default="~/Zotero/zotero.sqlite")
    parser.add_argument("--storage", default="~/Zotero/storage")
    args = parser.parse_args()

    db = Path(args.db).expanduser().resolve()
    storage = Path(args.storage).expanduser().resolve()
    if not db.is_file():
        parser.error(f"Zotero database not found: {db}")

    uri = f"file:{db}?mode=ro&immutable=1"
    with sqlite3.connect(uri, uri=True) as connection:
        rows = connection.execute(QUERY).fetchall()

    seen: set[tuple[str, str]] = set()
    title_keys: set[str] = set()
    selected = []
    for _, title, attachment_key, raw_path, first_name, last_name in rows:
        if not relevant(title):
            continue
        path = attachment_path(storage, attachment_key, raw_path)
        title_key = " ".join(title.split()).casefold()
        identity = (title_key, path)
        if identity in seen:
            continue
        seen.add(identity)
        title_keys.add(title_key)
        selected.append((title, f"{first_name} {last_name}".strip(), path))

    for title, author, path in selected:
        exists = Path(path).is_file() if not path.startswith("[") else False
        print(f"TITLE\t{title}")
        print(f"FIRST_AUTHOR\t{author}")
        print(f"PDF\t{path}")
        print(f"EXISTS\t{str(exists).lower()}\n")
    print(f"Unique Duan-first-author FAS titles: {len(title_keys)}")
    print(f"Total matching attachment records: {len(selected)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
