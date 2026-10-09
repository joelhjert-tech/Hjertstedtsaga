"""Import only published novel text and public universe dossiers; no production files."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def write(path, text):
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding='utf-8', newline='\n')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('site', type=Path, help='Explicit approved release site directory')
    parser.add_argument('--release', required=True)
    args = parser.parse_args()
    source = args.site / 'downloads/the-shattered-lane-chapters-1-8.md'
    raw = source.read_bytes()
    novel = raw.decode('utf-8-sig').replace('\r\n', '\n')
    chapters = list(re.finditer(r'^# Chapter (\d+): (.+)$', novel, re.M))
    assert [int(m[1]) for m in chapters] == list(range(1, 9)), 'Expected eight ordered chapters'
    write('novel/complete-novel.md', novel)
    index = ['# Novel index', '', 'Exact published prose. Chapter numbers follow the revised eight-chapter novel, not comic issue numbers.', '']
    records = []
    for i, match in enumerate(chapters):
        text = novel[match.start():chapters[i+1].start() if i+1 < len(chapters) else len(novel)]
        path = f'novel/chapters/chapter-{int(match[1]):02}.md'
        write(path, text)
        index.extend([f'## [Chapter {match[1]}: {match[2]}]({path.removeprefix("novel/")})', ''])
        scenes = list(re.finditer(r'^## (\d+)\. (.+)$', text, re.M))
        for j, scene in enumerate(scenes):
            start = text[:scene.start()].count('\n') + 1
            end_pos = scenes[j+1].start() if j+1 < len(scenes) else len(text)
            end = text[:end_pos].count('\n')
            anchor = re.sub(r'[^\w\- ]', '', f'{scene[1]}. {scene[2]}'.lower()).replace(' ', '-')
            index.append(f'- [{scene[1]}. {scene[2]}]({path.removeprefix("novel/")}#{anchor}) — lines {start}–{end}')
            records.append(dict(chapter=int(match[1]), scene=int(scene[1]), title=scene[2], file=path, start_line=start, end_line=end))
        index.append('')
    write('novel/INDEX.md', '\n'.join(index) + '\n')
    write('novel/scene-index.json', json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    bundle = args.site / 'content/public-v1.json'
    data = json.loads(bundle.read_text(encoding='utf-8'))
    lore_index = ['# Published universe reference', '', 'Website dossiers are supplemental. Read each entry’s scope; compare claims with the relevant novel scene. These are not new canon approvals.', '']
    count = 0
    for endpoint, payload in sorted(data['endpoints'].items()):
        if not endpoint.startswith('/api/public/universe/') or not isinstance(payload, dict) or 'entry' not in payload:
            continue
        entry = payload['entry']
        suffix = endpoint.removeprefix('/api/public/universe/')
        path = f'reference/{suffix}.md'
        parts = [f'# {entry["title"]}', '', f'Source: https://tales-from-the-known-reach.pages.dev/universe/{suffix}', '', f'Snapshot: {args.release}', '']
        for key in ['subtitle', 'summary', 'lore_scope']:
            if entry.get(key):
                parts += [str(entry[key]), '']
        for paragraph in entry.get('body', []):
            parts += [paragraph if isinstance(paragraph, str) else json.dumps(paragraph, ensure_ascii=False), '']
        for fact in entry.get('facts', []):
            parts += [f'- **{fact["label"]}:** {fact["value"]}']
        write(path, '\n'.join(parts) + '\n')
        lore_index.append(f'- [{entry["title"]}]({suffix}.md) ({suffix.split("/")[0]})')
        count += 1
    write('reference/INDEX.md', '\n'.join(lore_index) + '\n')
    revision = args.site / 'content/novel-revision-map.json'
    write('sources/novel-revision-map.json', revision.read_text(encoding='utf-8'))
    sources = {str(p.relative_to(args.site)).replace('\\', '/'): hashlib.sha256(p.read_bytes()).hexdigest() for p in [source, bundle, revision]}
    files = {str(p.relative_to(ROOT)).replace('\\', '/'): hashlib.sha256(p.read_bytes()).hexdigest() for folder in ['novel', 'reference', 'sources'] for p in sorted((ROOT/folder).rglob('*')) if p.is_file() and p.name != 'manifest.json'}
    write('sources/manifest.json', json.dumps(dict(release=args.release, imported_on='2026-10-09', scope='Published novel chapters 1–8 and published universe dossier text only', source_sha256=sources, chapter_count=8, scene_count=len(records), reference_count=count, files=files), ensure_ascii=False, indent=2) + '\n')
    reconstructed = novel[:chapters[0].start()] + ''.join((ROOT/f'novel/chapters/chapter-{i:02}.md').read_text(encoding='utf-8') for i in range(1,9))
    assert reconstructed == novel, 'Chapter extraction altered prose'
    print(json.dumps(dict(chapters=8, scenes=len(records), references=count, exact_prose_verified=True)))

if __name__ == '__main__':
    main()
