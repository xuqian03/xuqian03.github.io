from pathlib import Path
import shutil
import re

root = Path(".")
site = root / "_site"

html_path = site / "index.html"
html = html_path.read_text(encoding="utf-8")

html = html.replace(
    '<li class="masthead__menu-item "> <a href="/#publications">Publications</a></li><li class="masthead__menu-item "> <a href="/#education">Education</a></li>',
    '<li class="masthead__menu-item "> <a href="/#publications">Publications</a></li>',
)

old_block_start = '<h2 id="news">News</h2>'
old_block_end = '<h2 id="honors-awards">Honors &amp; Awards</h2>'
start = html.find(old_block_start)
end = html.find(old_block_end)
if start < 0 or end < 0:
    raise SystemExit(f"markers not found start={start} end={end}")

new_block = """<h2 id="news">📢 News</h2><div class="news-scroller" role="region" aria-label="News"><ul><li>[10/2026] One paper has been selected as the best student paper at ICIG 2026 (CCF-C).</li><li>[03/2026] One paper Light Field Referring Segmentation: A Benchmark and an LLM-Based Approach was published in IEEE Transactions on Broadcasting.</li></ul><div class="news-hint" aria-hidden="true">scroll for more &darr;</div></div><h2 id="publications">📄 Publications [<a href="https://orcid.org/0009-0001-3547-2900">ORCID</a>]</h2><div class="pub-gallery"><article class="pub-card"><div class="pub-card__media"><img src="/images/publications/icig2026.png" alt="Structure-Aware Light Field Referring Image Segmentation via Epipolar Geometric Priors"></div><div class="pub-card__body"><div class="pub-list__title">Structure-Aware Light Field Referring Image Segmentation via Epipolar Geometric Priors</div><div><b>Qian Xu</b>, Qiong Wang, Tiantian Zeng, Ting Su, Yan Li, Huiyu Duan, Shishun Tian, Guangtao Zhai</div><div><em>14th International Conference on Image and Graphics (<b>ICIG</b> 2026), CCF-C, Best Student Paper</em></div></div></article><article class="pub-card"><a class="pub-card__media" href="https://doi.org/10.1109/TBC.2026.3659013" target="_blank" rel="noopener"><img src="/images/publications/tbc2026.png" alt="Light Field Referring Segmentation: A Benchmark and an LLM-Based Approach"></a><div class="pub-card__body"><div class="pub-list__title"><a href="https://doi.org/10.1109/TBC.2026.3659013" target="_blank" rel="noopener">Light Field Referring Segmentation: A Benchmark and an LLM-Based Approach</a></div><div>Shishun Tian, <b>Qian Xu</b>, He Gui, Ting Su, Yan Li, Qiong Wang</div><div><em>IEEE Transactions on Broadcasting (<b>TBC</b>), 2026</em></div><div>[<a href="https://doi.org/10.1109/TBC.2026.3659013" target="_blank" rel="noopener">Paper</a>][<a href="https://github.com/ShishunTian/LFLLM-TBC2026" target="_blank" rel="noopener">Code</a>]</div></div></article></div>"""

html = html[:start] + new_block + html[end:]
html_path.write_text(html, encoding="utf-8")

css_path = site / "assets" / "css" / "main.css"
css = css_path.read_text(encoding="utf-8")
# Replace compiled pub-card rules with updated left-image layout.
old_css = re.search(
    r"\.pub-gallery\{.*?@media \(max-width: 640px\)\{\.pub-card\{flex-direction:column;align-items:flex-start\}\.pub-card__media\{width:100%;flex-basis:auto\}\}",
    css,
)
new_css = (
    ".pub-gallery{display:grid;gap:1.5rem;margin-block:1.25rem 2rem}"
    ".pub-card{display:flex;flex-direction:row;gap:1rem;padding:0.75rem;border-radius:0.5rem;"
    "background:var(--global-bg-color);border:1px solid var(--global-border-color);"
    "box-shadow:0 0.3rem 1.4rem rgba(15,23,42,0.14);align-items:center}"
    ".pub-card__media{flex:0 0 280px;max-width:280px;align-self:center;border-radius:0.3rem;"
    "overflow:hidden;background:var(--global-bg-color)}"
    ".pub-card__media img{display:block;width:100%;height:auto;object-fit:contain}"
    ".pub-card__body{flex:1;padding-block:0.1rem;display:flex;flex-direction:column;justify-content:center}"
    "@media (max-width: 640px){.pub-card{flex-direction:column;align-items:flex-start}"
    ".pub-card__media{width:100%;flex-basis:auto;max-width:100%}}"
)
if old_css:
    css = css[: old_css.start()] + new_css + css[old_css.end() :]
else:
    css = new_css + css
css_path.write_text(css, encoding="utf-8")

dest = site / "images" / "publications"
dest.mkdir(parents=True, exist_ok=True)
for name in ("icig2026.png", "tbc2026.png"):
    shutil.copy2(root / "images" / "publications" / name, dest / name)

print("patched _site")
