#!/usr/bin/env python3
import csv
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "papers.csv"
REQUIRED = {"id", "category", "year", "venue", "title", "paper_url", "code_url", "status", "relevance", "tags"}

def canonical(text):
    return "".join(ch.lower() for ch in text if ch.isalnum())

def valid_url(url):
    if not url:
        return True
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)

def main():
    errors = []
    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if set(reader.fieldnames or []) != REQUIRED:
            errors.append(f"CSV fields mismatch: {reader.fieldnames}")
        rows = list(reader)

    ids = set()
    titles = {}
    for row_num, row in enumerate(rows, 2):
        for key in REQUIRED - {"code_url"}:
            if not row.get(key, "").strip():
                errors.append(f"row {row_num}: missing {key}")
        if row["id"] in ids:
            errors.append(f"row {row_num}: duplicate id {row['id']}")
        ids.add(row["id"])
        title_key = canonical(row["title"])
        if title_key in titles:
            errors.append(f"row {row_num}: duplicate title; first seen at row {titles[title_key]}")
        titles[title_key] = row_num
        for key in ("paper_url", "code_url"):
            if not valid_url(row[key]):
                errors.append(f"row {row_num}: invalid {key}: {row[key]}")
        try:
            year = int(row["year"])
            if year < 1900 or year > 2100:
                errors.append(f"row {row_num}: implausible year {year}")
        except ValueError:
            errors.append(f"row {row_num}: non-integer year {row['year']}")

    if errors:
        print("Catalog validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Catalog validation passed: {len(rows)} unique records.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
