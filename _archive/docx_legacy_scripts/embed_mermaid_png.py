#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mermaid→high-DPI PNG→pandoc .docx pipeline."""
import os, re, subprocess, hashlib
from PIL import Image

BASE = "<PROJECT_ROOT>"
MD_SRC = f"{BASE}/AI协作项目全生命周期框架.md"
MD_TMP = f"{BASE}/_mermaid_png/_temp_for_docx.md"
DOCX_REF = f"{BASE}/_backups/AI协作项目全生命周期框架.docx.v155.backup2"
DOCX_OUT = f"{BASE}/AI协作项目全生命周期框架.docx"
OUT_DIR = f"{BASE}/_mermaid_png"
os.makedirs(OUT_DIR, exist_ok=True)

MMDC_W = 3000       # render width (px)
MAX_W_IN = 5.0
MAX_H_IN = 8.0
SPLIT_THRESHOLD = 7.0

# ====== 1. Extract & render Mermaid → PNG ======
with open(MD_SRC, 'r', encoding='utf-8') as f:
    md = f.read()

blocks = {}
for m in re.finditer(r'```mermaid\n(.*?)```', md, re.DOTALL):
    code = m.group(1).strip()
    h = hashlib.md5(code.encode()).hexdigest()[:8]
    before = md[:m.start()]
    headings = re.findall(r'^#{2,4}\s+(.+)$', before, re.MULTILINE)
    blocks[h] = {'code': code, 'ctx': headings[-1].strip()[:60] if headings else '?',
                 'start': m.start(), 'end': m.end()}

for h, b in blocks.items():
    mmd = f"{OUT_DIR}/{h}.mmd"
    png = f"{OUT_DIR}/{h}.png"
    with open(mmd, 'w', encoding='utf-8') as f:
        f.write(b['code'])
    r = subprocess.run(f'mmdc -i "{mmd}" -o "{png}" -w {MMDC_W} -b white',
                       capture_output=True, text=True, timeout=30, shell=True)
    ok = r.returncode == 0 and os.path.exists(png) and os.path.getsize(png) > 1000
    b['png'] = ok
    print(f'  {"OK" if ok else "FAIL"} {h}: {b["ctx"]}')

ok = sum(1 for b in blocks.values() if b['png'])
print(f'Rendered: {ok}/{len(blocks)}')

# ====== 2. Split tall images ======
for h, b in blocks.items():
    if not b.get('png'):
        continue
    png_path = f"{OUT_DIR}/{h}.png"
    img = Image.open(png_path)
    w, h_px = img.size
    dpi = img.info.get('dpi', (96, 96))
    dpi_x = dpi[0] if isinstance(dpi, tuple) else dpi
    natural_w = w / dpi_x
    embed_w = min(natural_w, MAX_W_IN)
    embed_h = h_px * embed_w / w

    if embed_h > SPLIT_THRESHOLD:
        n_parts = max(2, int(embed_h / SPLIT_THRESHOLD) + 1)
        part_h = h_px // n_parts
        overlap = max(5, h_px // 200)
        parts = []
        for i in range(n_parts):
            y1 = max(0, i * part_h - overlap)
            y2 = min(h_px, (i + 1) * part_h + overlap) if i < n_parts - 1 else h_px
            part = img.crop((0, y1, w, y2))
            part_path = f"{OUT_DIR}/{h}_p{i+1}.png"
            part.save(part_path)
            parts.append(part_path)
        b['parts'] = parts
        b['split'] = True
    else:
        b['parts'] = [png_path]
        b['split'] = False

# ====== 3. Replace Mermaid with images ======
repl = sorted([(b['start'], b['end'], h) for h, b in blocks.items() if b.get('png')], reverse=True)
md2 = md
for start, end, h in repl:
    b = blocks[h]
    if b.get('split'):
        imgs = '\n\n'.join(
            f'![Mermaid({i+1}/{len(b["parts"])})]({p})'
            for i, p in enumerate(b['parts']))
    else:
        imgs = f'![Mermaid]({b["parts"][0]})'
    md2 = md2[:start] + f'\n{imgs}\n\n' + md2[end:]

with open(MD_TMP, 'w', encoding='utf-8') as f:
    f.write(md2)

# ====== 4. Pandoc ======
import pypandoc
pypandoc.convert_file(MD_TMP, 'docx', outputfile=DOCX_OUT, extra_args=[
    f'--reference-doc={DOCX_REF}',
    '--from=markdown+pipe_tables+fenced_code_blocks',
])
print(f'Pandoc: {os.path.getsize(DOCX_OUT)} bytes')
os.remove(MD_TMP)

# ====== 5. Resize images ======
from docx import Document
from docx.shared import Inches
from docx.oxml.ns import qn
from io import BytesIO

doc = Document(DOCX_OUT)
MAX_W = int(MAX_W_IN * 914400)
MAX_H = int(MAX_H_IN * 914400)
resized = 0

for rel_id, rel in list(doc.part.rels.items()):
    if 'image' not in rel.reltype:
        continue
    img = Image.open(BytesIO(rel.target_part.blob))
    w_px, h_px = img.size
    dpi = img.info.get('dpi', (96, 96))
    dpi_x = dpi[0] if isinstance(dpi, tuple) else dpi
    w_emu = int(w_px * 914400 / dpi_x)
    h_emu = int(h_px * 914400 / dpi_x)

    if w_emu <= MAX_W and h_emu <= MAX_H:
        continue

    scale = min(MAX_W / w_emu, MAX_H / h_emu, 1.0)
    new_w = int(w_emu * scale)
    new_h = int(h_emu * scale)

    for elem in doc.element.iter():
        tag = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
        if tag == 'blip':
            embed = elem.get(qn('r:embed'))
            if embed == rel_id:
                inline = elem.getparent()
                for _ in range(5):
                    if inline is None:
                        break
                    tag2 = inline.tag.split('}')[-1] if '}' in inline.tag else inline.tag
                    if tag2 == 'inline':
                        for child in inline.iter():
                            child_tag = child.tag.split('}')[-1] if '}' in child.tag else child.tag
                            if child_tag == 'extent':
                                child.set('cx', str(new_w))
                                child.set('cy', str(new_h))
                            if child_tag == 'xfrm':
                                for gc in child:
                                    gc_tag = gc.tag.split('}')[-1] if '}' in gc.tag else gc.tag
                                    if gc_tag == 'ext':
                                        gc.set('cx', str(new_w))
                                        gc.set('cy', str(new_h))
                        resized += 1
                        break
                    inline = inline.getparent()
                break

doc.save(DOCX_OUT)
print(f'Resized {resized} images')

# ====== 6. Style post-process ======
os.chdir(BASE)
os.environ['STYLE_DOCX_PATH'] = DOCX_OUT
import runpy
runpy.run_path(f'{BASE}/_archive/docx_legacy_scripts/style_v16_docx.py', run_name='__main__')

print(f'\nDone: {DOCX_OUT}')
