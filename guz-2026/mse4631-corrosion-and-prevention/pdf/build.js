// MSE4631 ders notlarini tek PDF'e derler.
// Kullanim:  cd pdf && npm install && node build.js
// Gereken: pandoc, playwright (chromium), katex (npm)
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const katex = require('katex');
const { chromium } = require('playwright');

const ROOT = __dirname;
const NOTLAR = path.join(ROOT, '..', 'notlar');
const OUT_DIR = path.join(ROOT, '_build');
const PDF = path.join(ROOT, 'mse4631-korozyon-ders-notlari.pdf');

// PDF'e girecek dosyalar (ders klasorune gore), sirasiyla
const BOLUMLER = JSON.parse(fs.readFileSync(path.join(ROOT, 'icerik.json'), 'utf8'));

function unescapeHtml(s) {
  return s.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'").replace(/&amp;/g, '&');
}

function renderMath(html) {
  return html.replace(/<span\s+class="math (inline|display)">([\s\S]*?)<\/span>/g, (_, kind, tex) => {
    try {
      return katex.renderToString(unescapeHtml(tex), {
        displayMode: kind === 'display', throwOnError: true, strict: 'ignore',
      });
    } catch (e) {
      console.error('KaTeX hata:', e.message.split('\n')[0], '\n   ->', unescapeHtml(tex).slice(0, 120));
      process.exitCode = 1;
      return `<span style="color:red">${tex}</span>`;
    }
  });
}

fs.mkdirSync(OUT_DIR, { recursive: true });
let body = '';
for (const f of BOLUMLER) {
  const src = path.join(ROOT, '..', f);
  let md = fs.readFileSync(src, 'utf8');
  // Repo icindeki baglantilar PDF'te anlamsiz: [metin](x.md) -> metin
  md = md.replace(/\[([^\]]+)\]\((?!http)[^)]*\.md\)/g, '$1');
  const html = execFileSync('pandoc', ['-f', 'markdown+tex_math_dollars', '-t', 'html5', '--katex', '--wrap=none',
    '--resource-path', path.dirname(src)], { input: md, maxBuffer: 1 << 26 }).toString();
  // Gorsel yollarini mutlak yap
  const dir = path.dirname(src);
  body += `<section class="bolum">${renderMath(html).replace(/src="(?!http|file:|data:)([^"]+)"/g,
    (_, p) => `src="file://${path.resolve(dir, p)}"`)}</section>\n`;
}

const katexCss = 'file://' + path.join(ROOT, 'node_modules', 'katex', 'dist', 'katex.min.css');
const css = fs.readFileSync(path.join(ROOT, 'stil.css'), 'utf8');
const kapak = fs.readFileSync(path.join(ROOT, 'kapak.html'), 'utf8');
const page = `<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>MSE4631 Korozyon ve Korunma - Ders Notlari</title>
<link rel="stylesheet" href="${katexCss}"><style>${css}</style></head>
<body>${kapak}${body}</body></html>`;
const htmlPath = path.join(OUT_DIR, 'notlar.html');
fs.writeFileSync(htmlPath, page);

(async () => {
  const browser = await chromium.launch();
  const p = await browser.newPage();
  await p.goto('file://' + htmlPath, { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({
    path: PDF, format: 'A4', printBackground: true,
    margin: { top: '18mm', bottom: '18mm', left: '17mm', right: '17mm' },
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: `<div style="width:100%;font:8px Inter,sans-serif;color:#888;padding:0 17mm;display:flex;justify-content:space-between">
      <span>MSE4631 Corrosion and Prevention — Ders Notları</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
  });
  await browser.close();
  console.log('PDF:', PDF);
})();
