"""Regenerate inventory.csv — only include git-tracked files."""
import os, csv, time, fnmatch
from pathlib import Path

PROJECT = Path(__file__).parent.parent

# Read .gitignore rules
gitignore = PROJECT / '.gitignore'
ignore_patterns = []
if gitignore.exists():
    with open(gitignore, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                ignore_patterns.append(line)

def is_ignored(rel_path):
    for pat in ignore_patterns:
        if pat.endswith('/'):
            # Directory pattern
            if rel_path.startswith(pat) or ('/' + pat) in ('/' + rel_path + '/'):
                return True
        elif fnmatch.fnmatch(rel_path, pat) or fnmatch.fnmatch(os.path.basename(rel_path), pat):
            return True
    return False

rows = []
for f in sorted(PROJECT.rglob('*'), key=lambda x: str(x)):
    if f.name.startswith('.') and f.name != '.gitignore':
        continue
    if f.is_dir():
        continue
    rel = str(f.relative_to(PROJECT)).replace('\\', '/')
    if is_ignored(rel):
        continue
    stat = f.stat()
    size_kb = round(stat.st_size / 1024, 1)
    mtime = time.strftime('%Y-%m-%d %H:%M', time.localtime(stat.st_mtime))
    ext = f.suffix.lower()
    rows.append([rel, ext, size_kb, mtime])

rows.sort(key=lambda r: r[0])

with open(PROJECT / 'inventory.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['path', 'extension', 'size_kb', 'last_modified'])
    w.writerows(rows)

total_kb = sum(r[2] for r in rows)
self_included = any(r[0] == 'inventory.csv' for r in rows)
print(f'Regenerated: {len(rows)} files, {total_kb:.0f} KB ({total_kb/1024:.1f} MB)')
print(f'Self-included: {self_included}')
