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
def case_section(home, case_id, filename):
    marker=f'<a id="{case_id}"></a>'
    require(home.count(marker)==1,f'{filename}: expected one case anchor {case_id}')
    if marker not in home:return ''
    # Stop at the next case or top-level section; a missing resource in the
    # final case must not be satisfied by a later catalogue or source list.
    return re.split(r'<a\s+id=|^## ',home.split(marker,1)[1],maxsplit=1,flags=re.M)[0]

def check_case_resources(home, records, resource_keys, filename):
    for record in records:
        case=case_section(home,record['id'],filename)
        for key in resource_keys:
            require(record[key] in case,f"{filename}: {record['id']} missing its {key}")
            # Shared source articles are valid; another case's distinct image
            # or video in this block usually means an accidental mismatch.
            for other in records:
                if other[key]!=record[key]:
                    require(other[key] not in case,f"{filename}: {record['id']} contains {other['id']}'s {key}")
        require(any(block.strip() for block in re.findall(r'```text[ \t]*\n(.*?)```',case,re.S)),
                f"{filename}: {record['id']} missing nonempty prompt code block")
        if record['id'].startswith('official-'):
            source_explanation=case.split('<details>',1)[0]
            require(any(block.strip() for block in re.findall(r'```text[ \t]*\n(.*?)```',source_explanation,re.S)),
                    f"{filename}: {record['id']} missing visible official prompt summary")
            for image_path in record.get('image_paths',[]):
                require(image_path in case,f"{filename}: {record['id']} missing its still {image_path}")
            for other in records:
                if other['id']!=record['id']:
                    for image_path in other.get('image_paths',[]):
                        require(image_path not in case,f"{filename}: {record['id']} contains another case's still {image_path}")
        if record['id'].startswith('x'):
            require('<details>' in case and '</details>' in case,
                    f"{filename}: missing copyable adaptation {record['id']}")

official_path=ROOT/'docs/official-homepage-cases.json'
require(official_path.is_file(),'Missing official homepage case manifest')
official=json.loads(official_path.read_text())['entries'] if official_path.is_file() else []
require(len(official)==3 and {e['id'] for e in official}==
        {'official-route','official-references','official-camera'},'Expected three official teaching cases')
for record in official:
    require(record['image_path'] in record.get('image_paths',[]),f"{record['id']}: primary still missing from image_paths")
    for image_path in record.get('image_paths',[]):
        require((ROOT/image_path).is_file(),f'Missing official still: {image_path}')
for filename in ['README.md', 'README_ZH.md']:
    home=(ROOT/filename).read_text()
    check_case_resources(home,entries,['original_post','video_url','thumbnail_url'],filename)
    check_case_resources(home,official,['video_url','image_path','source_url'],filename)
    for asset in ['cinematic-rescue-reference.png','product-sparkling-tea-reference.png','paper-fox-story-reference.png','night-garden-storyboard.png']:
        require(home.count(f'assets/{asset}')==1,f'{filename}: expected one display of {asset}')
    headings=list(re.finditer(r'^## (.+)$',home,re.M))
    brand_title='Create with SeaImagine' if filename=='README.md' else '在 SeaImagine 使用 Seedance 2.5'
    faq_title='Seedance 2.5 prompt FAQ' if filename=='README.md' else '常见问题'
    brand=[i for i,h in enumerate(headings) if h.group(1)==brand_title]
    require(len(brand)==1,f'{filename}: expected one brand section')
    if len(brand)==1:
        i=brand[0]
        require(i+1<len(headings) and headings[i+1].group(1)==faq_title,
                f'{filename}: brand section must immediately precede FAQ')
        end=headings[i+1].start() if i+1<len(headings) else len(home)
        require('assets/seaimagine-paper-sea.jpg' in home[headings[i].end():end],
                f'{filename}: brand section missing its image')
for lang in manifest['languages']:
    filename=lang['readme']
    home=(ROOT/filename).read_text()
    english_links=re.findall(r'\[English\]\((README[^)]*)\)',home)
    require(bool(english_links) and all(link=='README.md' for link in english_links),
            f'{filename}: English navigation must point to README.md')
    if lang['code'] not in ['en','cn']:
        require('assets/seaimagine-paper-sea.jpg' in home,f'{filename}: missing localized brand image')
alias=(ROOT/'README_EN.md').read_text()
require(bool(re.search(r'\[[^]]+\]\(README\.md\)',alias)),
        'README_EN.md: missing redirect link to complete English homepage')
require(len(alias.splitlines())<=20 and not re.search(r'^## |<a id="x',alias,re.M),
        'README_EN.md must remain a concise redirect, not a second English homepage')
if errors:
    print('\n'.join(errors));sys.exit(1)
print('PASS: 120 intact recipes, 15 locales, 14 practice sets, matched X/official cases, brand placement, navigation and local links.')
