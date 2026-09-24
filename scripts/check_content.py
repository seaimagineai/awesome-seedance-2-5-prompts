#!/usr/bin/env python3
"""Check corpus preservation, locale coverage, local links and provenance."""
from pathlib import Path
import hashlib, json, re, sys, urllib.parse
ROOT = Path(__file__).resolve().parents[1]
errors=[]
def require(ok, message):
    if not ok: errors.append(message)
def anchors(text):
    result=set(re.findall(r'<a\s+id="([^"]+)"',text))
    seen={}
    # Ignore headings inside fenced prompt blocks.
    text=re.sub(r'```.*?```','',text,flags=re.S)
    for title in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):
        slug=re.sub(r'[^\w\- ]','',title.lower()).replace(' ','-')
        n=seen.get(slug,0);seen[slug]=n+1
        result.add(slug+(f'-{n}' if n else ''))
    return result
manifest=json.loads((ROOT/'data/languages.json').read_text())
require(len(manifest['languages'])==15,'Expected 15 website locales')
for lang in manifest['languages']:
    for key in ['readme','practice_file']:require((ROOT/lang[key]).is_file(),f"Missing {lang[key]}")
    if lang['code']!='cn':
        t=(ROOT/lang['practice_file']).read_text()
        require(len(re.findall(r'^## I18N-\d+',t,re.M))==6,f"Not six scenes: {lang['practice_file']}")
checks=json.loads((ROOT/'data/source-content.json').read_text())['prompt_blocks']
ids=[]
for name,record in checks.items():
    t=(ROOT/name).read_text()
    blocks=re.findall(r'```[^\n]*\n(.*?)```',t,re.S)
    require(len(blocks)==record['blocks'],f'Prompt count changed: {name}')
    require(hashlib.sha256('\n'.join(blocks).encode()).hexdigest()==record['sha256'],f'Prompt text changed: {name}')
    ids += [int(n) for n in re.findall(r'^#{2,3} (\d+)\.',t,re.M)]
require(sorted(ids)==list(range(1,121)),f'Expected IDs 1–120 exactly; found {len(ids)}')
for p in ROOT.rglob('*.md'):
    if '.git' in p.parts:continue
    t=p.read_text()
    require('https://flaq.ai/' not in t,f'Old product CTA: {p.relative_to(ROOT)}')
    for link in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)',t):
        if re.match(r'(?:https?://|mailto:|data:)',link):continue
        u=urllib.parse.urlsplit(link)
        target=(p.parent/urllib.parse.unquote(u.path)).resolve() if u.path else p
        require(target.exists(),f'{p.relative_to(ROOT)}: missing {link}')
        if target.is_file() and target.suffix=='.md' and u.fragment:
            require(urllib.parse.unquote(u.fragment) in anchors(target.read_text()),f'{p.relative_to(ROOT)}: missing anchor {link}')
require('Copyright (c) 2026 Flaq AI' in (ROOT/'LICENSE').read_text(),'Missing upstream copyright')
entries=json.loads((ROOT/'docs/x-showcase-sources.json').read_text())['entries']
require(len({e['original_post'] for e in entries})==12,'Expected 12 unique X posts')
home=(ROOT/'README.md').read_text()
for e in entries:require(e['original_post'] in home and e['video_url'] in home and e['thumbnail_url'] in home,f"Missing showcase: {e['id']}")
if errors:
    print('\n'.join(errors));sys.exit(1)
print('PASS: 120 intact recipes, 15 language entry pages, 14 six-scene sets, 12 X cases, copyright and local links.')
