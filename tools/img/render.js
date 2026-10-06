const sharp = require('sharp');
const fs = require('fs');
const site = '/home/claude/repo-potarin-site';

const ogp = `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<rect width="1200" height="630" fill="#5DB7EE"/>
<rect y="250" width="1200" height="200" fill="#8FCFF4"/>
<g fill="#FFFFFF"><circle cx="930" cy="110" r="30"/><circle cx="968" cy="92" r="40"/><circle cx="1010" cy="112" r="28"/><rect x="900" y="110" width="140" height="30" rx="15"/></g>
<g fill="#FFFFFF" opacity="0.85"><circle cx="1110" cy="210" r="16"/><circle cx="1130" cy="200" r="22"/><circle cx="1152" cy="212" r="15"/><rect x="1094" y="212" width="74" height="16" rx="8"/></g>
<path d="M0 420 L180 340 L330 400 L570 300 L800 390 L980 330 L1200 410 V630 H0 Z" fill="#8CCBA6"/>
<path d="M0 500 C250 455 430 490 640 480 C850 470 1030 490 1200 465 V630 H0 Z" fill="#3E9B5E"/>
<rect y="548" width="1200" height="82" fill="#1F7A4D"/>
<g fill="none" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round" stroke-linejoin="round">
<circle cx="820" cy="506" r="42"/><circle cx="949" cy="506" r="42"/>
<path d="M820 506 L876 506 L856 447 Z"/><path d="M856 447 L926 447 L876 506"/><path d="M926 447 L949 506"/>
<path d="M842 436 L873 436"/><path d="M918 430 C926 425 937 425 943 433"/>
</g>
<circle cx="876" cy="506" r="10" fill="#FFFFFF"/>
<g stroke="#FFFFFF" stroke-width="7" stroke-linecap="round" opacity="0.8"><path d="M736 476 L756 476"/><path d="M726 498 L752 498"/></g>
<text x="80" y="150" font-family="Noto Sans CJK JP" font-weight="700" font-size="40" fill="#16302A">のんびり走る人のための自転車アプリ</text>
<text x="76" y="268" font-family="Noto Sans CJK JP" font-weight="700" font-size="112" fill="#16302A">ぽたりん</text>
<text x="80" y="340" font-family="Noto Sans CJK JP" font-weight="500" font-size="36" fill="#16302A">週末、ちょっとそこまで。</text>
</svg>`;

(async () => {
  await sharp(Buffer.from(ogp)).png().toFile(`${site}/ogp.png`);
  await sharp(fs.readFileSync(`${site}/icon.svg`), { density: 300 }).resize(180, 180).png().toFile(`${site}/apple-touch-icon.png`);
  const square = fs.readFileSync(`${site}/icon.svg`, 'utf8').replace('rx="54"', 'rx="0"');
  await sharp(Buffer.from(square), { density: 600 }).resize(1024, 1024).flatten({ background: '#5DB7EE' }).png().toFile(`${__dirname}/AppIcon-1024.png`);
  console.log('done');
})();
