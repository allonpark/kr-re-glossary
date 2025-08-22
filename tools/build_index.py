#!/usr/bin/env python3
import os, json, re, datetime, pathlib
root = pathlib.Path(__file__).resolve().parents[1]
terms_dir = root / "terms"
index_md = root / "index.md"
index_json = terms_dir / "_index.json"
def parse_frontmatter(mdpath):
    text = mdpath.read_text(encoding='utf-8')
    m = re.match(r"---\s*(.*?)---\s*(.*)$", text, flags=re.S|re.M)
    if not m: return None
    fm = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            k,v = line.split(':',1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm
items = []
for p in terms_dir.glob('*.md'):
    if p.name.startswith('_'): continue
    fm = parse_frontmatter(p)
    if not fm: continue
    slug = p.stem
    items.append({'title': fm.get('title', slug),'slug': slug,'category': fm.get('category',''),'summary': fm.get('summary','')})
index_json.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding='utf-8')
text = index_md.read_text(encoding='utf-8')
text = re.sub(r"(업데이트:\s*)(\d{4}-\d{2}-\d{2})", r"\g<1>" + datetime.date.today().isoformat(), text)
index_md.write_text(text, encoding='utf-8')
print('Updated index json & timestamp')
