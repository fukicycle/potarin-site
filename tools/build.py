#!/usr/bin/env python3
"""画面モックを fukicycle/potarin の design/canvas/project から取り出して index.html を組み立てる。

使い方: python3 tools/build.py  （potarin リポジトリを隣に clone しておくか、POTARIN_DESIGN で場所を指定）

Extract mock screens from the design canvas files into static HTML partials
and assemble index.html from template.html."""
import os, re, pathlib

DESIGN = pathlib.Path(os.environ.get('POTARIN_DESIGN', pathlib.Path(__file__).resolve().parents[2] / 'potarin' / 'design' / 'canvas' / 'project'))
SITE = pathlib.Path(__file__).resolve().parents[1]
TEMPLATE = pathlib.Path(__file__).with_name('template.html')

def screen(name):
    src = (DESIGN / f'{name}.dc.html').read_text(encoding='utf-8')
    body = src.split('</helmet>', 1)[1].split('</x-dc>', 1)[0].strip()
    body = body.replace('{{accent}}', '#1F7A4D')
    body = body.replace("'Zen Kaku Gothic New'", "'Zen Maru Gothic'")
    # headings and nav inside the decorative screens must not compete with the page outline
    body = re.sub(r'<(/?)(h1|h2|h3|nav)\b', lambda m: f'<{m.group(1)}div', body)
    # links between mock screens would be dead links for crawlers
    body = re.sub(r'<a\b([^>]*?)\s+href="[^"]*"', r'<span\1', body)
    body = body.replace('</a>', '</span>')
    body = re.sub(r'<a\b', '<span', body)
    body = re.sub(r'\saria-label="[^"]*"', '', body)
    body = re.sub(r'\saria-current="[^"]*"', '', body)
    body = re.sub(r'\srole="img"', '', body)
    if '{{' in body:
        raise SystemExit(f'unresolved template hole in {name}')
    return body

html = TEMPLATE.read_text(encoding='utf-8')
for key, name in {'HOMEFUN': 'HomeFun', 'RECORD': 'Record', 'RIDEDETAIL': 'RideDetail', 'MAIN': 'Main'}.items():
    html = html.replace(f'<!--SCREEN:{key}-->', screen(name))
(SITE / 'index.html').write_text(html, encoding='utf-8')
print('index.html written', len(html), 'bytes')
