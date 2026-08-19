// Render the repository's Markdown documents to a small static HTML site in dist/.
// Chinese (CJK) content, GFM tables and headings are all supported.
import { readFile, writeFile, mkdir, readdir } from 'node:fs/promises';
import { dirname, join, basename, extname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { marked } from 'marked';

const rootDir = join(dirname(fileURLToPath(import.meta.url)), '..');
const distDir = join(rootDir, 'dist');

marked.setOptions({ gfm: true, breaks: false });

async function markdownFiles() {
  const entries = await readdir(rootDir, { withFileTypes: true });
  return entries
    .filter((e) => e.isFile() && extname(e.name).toLowerCase() === '.md')
    .map((e) => e.name)
    .sort((a, b) => a.localeCompare(b, 'zh'));
}

function page(title, bodyHtml, css) {
  return `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>${title}</title>
<style>
${css}
body { box-sizing: border-box; min-width: 200px; max-width: 980px; margin: 0 auto; padding: 32px 45px; }
a.back { display: inline-block; margin-bottom: 16px; font: 14px/1.5 -apple-system, system-ui, sans-serif; }
</style>
</head>
<body class="markdown-body">
${bodyHtml}
</body>
</html>
`;
}

async function main() {
  const css = await readFile(
    join(rootDir, 'node_modules', 'github-markdown-css', 'github-markdown-light.css'),
    'utf8',
  );
  await mkdir(distDir, { recursive: true });

  const files = await markdownFiles();
  const rendered = [];
  for (const file of files) {
    const md = await readFile(join(rootDir, file), 'utf8');
    const html = marked.parse(md);
    const outName = `${basename(file, '.md')}.html`;
    const backLink = '<a class="back" href="./index.html">&larr; 返回目录 / Back to index</a>';
    await writeFile(join(distDir, outName), page(basename(file, '.md'), backLink + html, css), 'utf8');
    rendered.push({ file, outName });
    console.log(`rendered ${file} -> dist/${outName}`);
  }

  const list = rendered
    .map((r) => `<li><a href="./${encodeURIComponent(r.outName)}">${r.file}</a></li>`)
    .join('\n');
  const indexBody = `<h1>HUANGQIUXIA 文档预览 / Docs preview</h1>
<p>本站由仓库中的 Markdown 文档自动生成。 This site is generated from the repository's Markdown files.</p>
<ul>
${list}
</ul>`;
  await writeFile(join(distDir, 'index.html'), page('Docs preview', indexBody, css), 'utf8');
  console.log(`rendered index.html with ${rendered.length} document(s)`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
