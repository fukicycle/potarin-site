#!/usr/bin/env python3
"""Apply the ことり# brand footer, credits and operator details to the potarin site."""
import re, pathlib

SCRATCH = pathlib.Path(__file__).parent
SITE = pathlib.Path('/home/claude/repo-potarin-site')

LOGO = '''<svg width="44" height="44" viewBox="0 0 100 100" aria-hidden="true" focusable="false">
<defs><clipPath id="kf-clip"><rect x="11" y="11" width="78" height="78"/></clipPath><filter id="kf-blur" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="0.8"/></filter></defs>
<rect x="8" y="8" width="84" height="84" fill="#F3EBD8" stroke="#5C4A36" stroke-width="6"/>
<g clip-path="url(#kf-clip)"><g transform="translate(2 14) scale(0.47)">
<g opacity="0.52" filter="url(#kf-blur)" fill="#2E3D36">
<path d="M4 132 C40 126 80 118 110 113 C140 108 170 106 196 98" fill="none" stroke="#2E3D36" stroke-width="6" stroke-linecap="round"/>
<path d="M166 106 C172 96 178 90 188 82" fill="none" stroke="#2E3D36" stroke-width="2.6" stroke-linecap="round"/>
<path d="M30 128 C24 136 20 142 14 146" fill="none" stroke="#2E3D36" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="158" cy="96.5" r="4"/><circle cx="162.3" cy="99.6" r="4"/><circle cx="160.7" cy="104.6" r="4"/><circle cx="155.4" cy="104.6" r="4"/><circle cx="153.7" cy="99.6" r="4"/>
<circle cx="188" cy="76.2" r="3.4"/><circle cx="191.6" cy="78.8" r="3.4"/><circle cx="190.3" cy="83.1" r="3.4"/><circle cx="185.8" cy="83.1" r="3.4"/><circle cx="184.4" cy="78.8" r="3.4"/>
<circle cx="176" cy="91" r="2.6"/>
<g transform="rotate(-12 108 112)">
<path d="M78 99 L48 116 L52 123 L82 106 Z"/>
<path d="M150 58 C150 72 138 86 118 96 C102 104 86 106 76 104 L72 99 C78 88 92 70 112 56 C122 48 132 42 140 40 C148 40 153 45 153 52 Z"/>
<path d="M118 60 C106 70 92 84 82 96 L64 112 L69 115 L90 104 C106 96 118 84 124 70 Z"/>
<path d="M151 47.5 L171 50 L151 52.5 Z"/>
</g>
<g stroke="#2E3D36" stroke-width="2" stroke-linecap="round" fill="none"><path d="M102 103 L102 113"/><path d="M109.5 99 L112 111"/></g>
</g>
<circle cx="143" cy="49" r="4.2" fill="none" stroke="#F3EBD8" stroke-width="2.2" transform="rotate(-12 108 112)"/>
</g></g>
<line x1="36" y1="11" x2="36" y2="89" stroke="#5C4A36" stroke-width="3.5"/><line x1="64" y1="11" x2="64" y2="89" stroke="#5C4A36" stroke-width="3.5"/>
<line x1="11" y1="36" x2="89" y2="36" stroke="#5C4A36" stroke-width="3.5"/><line x1="11" y1="64" x2="89" y2="64" stroke="#5C4A36" stroke-width="3.5"/>
</svg>'''

def footer(links):
    nav = ''.join(f'<a href="{h}">{t}</a>' for h, t in links)
    return f'''<footer class="kotli-foot">
  <div class="wrap">
    <a class="kotli-brand" href="https://kotli-sharp.jp/">
      {LOGO}
      <span class="kotli-text"><span class="kotli-name">ことり#</span><span class="kotli-read">ぽたりんは、ことりしゃーぷのアプリです</span></span>
    </a>
    <nav aria-label="フッター">{nav}</nav>
    <p class="kotli-copy">© 2026 ことり#</p>
  </div>
</footer>'''

FOOT_CSS = '''
/* ことり# の腰板（ブランド共通のフッター） */
.kotli-foot{background:#6E5A43;border-top:3px solid #5C4A36;color:#EDE4D3;padding:40px 0;font-size:14px}
.kotli-foot .wrap{display:grid;grid-template-columns:1fr auto;gap:20px 40px;align-items:center}
.kotli-brand{display:flex;align-items:center;gap:14px;color:#F5F2EC;text-decoration:none}
.kotli-brand:hover{color:#FFFFFF}
.kotli-brand:hover .kotli-read{text-decoration:underline}
.kotli-text{display:flex;flex-direction:column;gap:2px}
.kotli-name{font-family:'Shippori Mincho',serif;font-weight:700;font-size:22px;letter-spacing:.06em;line-height:1.3}
.kotli-read{font-size:13px;color:#EDE4D3}
.kotli-foot nav{display:flex;flex-wrap:wrap;gap:4px 28px}
.kotli-foot nav a{color:#F5F2EC;text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
.kotli-foot nav a:hover{color:#FFFFFF;text-decoration:underline}
.kotli-copy{grid-column:1 / -1;margin:0;font-size:12px;border-top:1px solid rgba(237,228,211,.25);padding-top:18px}
@media (max-width:720px){.kotli-foot .wrap{grid-template-columns:1fr}}
'''

BRAND_FONT = '<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@700&text=%E3%81%93%E3%81%A8%E3%82%8A%23&display=swap" rel="stylesheet">'

def apply(path, links):
    s = path.read_text(encoding='utf-8')
    s = re.sub(r'<footer[\s\S]*?</footer>', footer(links), s, count=1)
    s = re.sub(r'\n(footer|footer \.wrap|footer nav|footer a|footer a:hover)\{[^}]*\}', '', s)
    if 'kotli-foot{' not in s:
        s = s.replace('</style>', FOOT_CSS + '</style>', 1)
    if 'Shippori+Mincho' not in s:
        s = s.replace('rel="stylesheet">', 'rel="stylesheet">\n' + BRAND_FONT, 1)
    if 'name="author"' not in s:
        s = s.replace('<meta name="viewport"', '<meta name="author" content="ことり#">\n<meta name="viewport"', 1)
    s = s.replace('[運営者名]', 'ことり#（ことりしゃーぷ）')
    s = s.replace('[お問い合わせ用メールアドレス]', '<a href="mailto:kotli.sharp@gmail.com">kotli.sharp@gmail.com</a>')
    s = s.replace('[中継サーバーの事業者名（例：Cloudflare）]', 'Cloudflare（Cloudflare Workers）')
    path.write_text(s, encoding='utf-8')

apply(SCRATCH / 'template.html', [('/support', 'サポート'), ('/privacy', 'プライバシーポリシー')])
apply(SITE / 'privacy.html', [('/', 'トップ'), ('/support', 'サポート')])
apply(SITE / 'support.html', [('/', 'トップ'), ('/privacy', 'プライバシーポリシー')])

t = SCRATCH / 'template.html'
s = t.read_text(encoding='utf-8')
s = s.replace('<cite>[作者名]（愛知県）</cite>', '<cite>ことり#（ことりしゃーぷ）</cite>')
s = s.replace('''  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "JPY" }''',
'''  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "JPY" },
  "author": { "@type": "Organization", "name": "ことり#", "alternateName": "ことりしゃーぷ", "url": "https://kotli-sharp.jp/" },
  "publisher": { "@type": "Organization", "name": "ことり#", "alternateName": "ことりしゃーぷ", "url": "https://kotli-sharp.jp/" }''')
t.write_text(s, encoding='utf-8')
print('applied')
