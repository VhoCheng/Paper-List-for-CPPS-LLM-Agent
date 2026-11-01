#!/usr/bin/env python3
"""Check synchronized snapshot artifacts without network access."""
import csv
import json
import re
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parents[1]

def main():
    rows = json.loads((ROOT / 'data/papers.json').read_text())
    changes = json.loads((ROOT / 'data/changes_2026-11-01.json').read_text())
    evidence = json.loads((ROOT / 'data/verification_2026-11-01.json').read_text())['records']
    errors = []
    with (ROOT / 'data/papers.csv').open(encoding='utf-8', newline='') as f:
        csv_rows = list(csv.DictReader(f))
    for r in csv_rows:
        r['year'] = int(r['year'])
    if rows != csv_rows:
        errors.append('CSV and JSON differ')
    ids = {r['id'] for r in rows}
    new = set(changes['added_ids'])
    updated = {r['id'] for r in changes['updated_records']}
    if not new.isdisjoint(updated):
        errors.append('Added and updated IDs overlap')
    if not (new | updated) <= ids:
        errors.append('Unknown change ID')
    if set(evidence) != new | updated:
        errors.append('Evidence IDs differ from changed IDs')
    for rid, e in evidence.items():
        if not e.get('verification_sources'):
            errors.append(f'{rid}: no source')
        if e.get('verified_on') != '2026-11-01':
            errors.append(f'{rid}: wrong snapshot')
        for key in ['arxiv_first_submitted', 'arxiv_last_updated']:
            if e.get(key, '') > '2026-11-01':
                errors.append(f'{rid}: future arXiv {key}')
        for u in e.get('verification_sources', []):
            if urlparse(u).scheme not in {'http', 'https'}:
                errors.append(f'{rid}: malformed URL')
    readme = (ROOT / 'README.md').read_text()
    graph = (ROOT / 'docs/GRAPH_LLM.md').read_text()
    for r in rows:
        if f"| {r['title']} |" not in readme:
            errors.append(f"{r['id']}: absent from README")
        if r['category'] == 'graph_llm' and f"| {r['title']} |" not in graph:
            errors.append(f"{r['id']}: absent from graph chapter")
    graph_rows = [r for r in rows if r['category'] == 'graph_llm']
    if (len(rows), len(new), len(updated), len(graph_rows)) != (224, 68, 6, 34):
        errors.append('Snapshot count mismatch')
    doi_seen = {}
    for r in rows:
        if 'doi.org/' in r['paper_url']:
            doi = r['paper_url'].split('doi.org/', 1)[1].lower()
            if doi in doi_seen:
                errors.append(f"Duplicate DOI: {r['id']} and {doi_seen[doi]}")
            doi_seen[doi] = r['id']
    for md in ROOT.rglob('*.md'):
        for target in re.findall(r'\]\(([^\s)]+)\)', md.read_text()):
            if '://' in target or target.startswith(('#', '<')):
                continue
            filename = unquote(target.split('#', 1)[0])
            if filename and not (md.parent / filename).exists():
                errors.append(f'{md.relative_to(ROOT)}: broken local link {target}')
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'Update validation passed: {len(rows)} records, {len(new)} additions, {len(updated)} updates, {len(graph_rows)} graph records.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
