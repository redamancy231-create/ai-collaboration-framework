"""全量重生成 DOCX —— Mermaid渲染 + pandoc转换 + 样式后处理"""
import subprocess, re, os, tempfile, shutil, hashlib
from pathlib import Path

# mmdc: try PATH first, fall back to common npm global install locations
def _find_mmdc():
    """Find mmdc executable. Tries PATH first, then common locations."""
    # Try 'mmdc' from PATH (works on Linux/macOS/Git Bash)
    for candidate in ["mmdc", "mmdc.cmd", "npx mmdc"]:
        try:
            subprocess.run([candidate, "--version"], capture_output=True, timeout=10)
            return candidate
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue
    # Fallback: check common npm global locations
    import platform
    if platform.system() == "Windows":
        npm_prefix = subprocess.run(
            ["npm", "config", "get", "prefix"], capture_output=True, text=True
        ).stdout.strip()
        mmdc_path = Path(npm_prefix) / "mmdc.cmd"
        if mmdc_path.exists():
            return str(mmdc_path)
    # Last resort
    return "mmdc"

MMDC = _find_mmdc()
PANDOC = "pandoc"  # In Git Bash PATH

PROJECT = Path(__file__).parent.parent
MD_SOURCE = PROJECT / "AI协作项目全生命周期框架.md"
DOCX_OUT = PROJECT / "AI协作项目全生命周期框架.docx"
MERMAID_DIR = PROJECT / "_mermaid_png"
WORK_DIR = PROJECT / "_pipeline_output" / "work"
WORK_DIR.mkdir(parents=True, exist_ok=True)
MERMAID_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# Step 1: Extract Mermaid blocks, render to PNG
# ============================================================
md_text = MD_SOURCE.read_text(encoding='utf-8')
mermaid_blocks = list(re.finditer(r'```mermaid\n(.*?)```', md_text, re.DOTALL))

print(f"Found {len(mermaid_blocks)} Mermaid blocks")

rendered = {}
for i, m in enumerate(mermaid_blocks):
    code = m.group(1).strip()
    # Create hash-based filename
    h = hashlib.md5(code.encode()).hexdigest()[:8]
    mmd_path = MERMAID_DIR / f"{h}.mmd"
    png_path = MERMAID_DIR / f"{h}.png"

    mmd_path.write_text(code, encoding='utf-8')

    # Render with mmdc
    result = subprocess.run(
        [MMDC, '-i', str(mmd_path), '-o', str(png_path),
         '-w', '1200', '-b', 'white', '-s', '1'],
        capture_output=True, text=True, timeout=60
    )
    if result.returncode != 0:
        print(f"  ERROR rendering diagram {i+1}: {result.stderr[:200]}")
        # Try without scale
        result = subprocess.run(
            [MMDC, '-i', str(mmd_path), '-o', str(png_path),
             '-w', '1200', '-b', 'white'],
            capture_output=True, text=True, timeout=60
        )
    if png_path.exists():
        rendered[h] = png_path
        print(f"  Rendered diagram {i+1}/{len(mermaid_blocks)}: {h}.png ({png_path.stat().st_size} bytes)")
    else:
        print(f"  FAILED diagram {i+1}: {result.stderr[:300]}")

# ============================================================
# Step 2: Replace Mermaid blocks with image references
# ============================================================
processed = md_text
for m in mermaid_blocks:
    code = m.group(1).strip()
    h = hashlib.md5(code.encode()).hexdigest()[:8]
    if h in rendered:
        img_path = rendered[h]
        # Use relative path for pandoc
        rel_path = os.path.relpath(img_path, WORK_DIR)
        processed = processed.replace(
            m.group(0),
            f'![Mermaid diagram]({rel_path})\\ '
        )

preprocessed_path = WORK_DIR / "preprocessed.md"
preprocessed_path.write_text(processed, encoding='utf-8')
print(f"\nPreprocessed MD: {preprocessed_path} ({len(processed)} chars)")

# ============================================================
# Step 3: pandoc conversion
# ============================================================
pandoc_args = [
    PANDOC,
    str(preprocessed_path),
    '-o', str(WORK_DIR / 'output.docx'),
    '--from', 'markdown+smart',
    '--reference-doc=' + str(PROJECT / 'AI协作项目全生命周期框架.docx'),  # use old docx as ref for styles
    '--metadata', 'title=AI协作项目全生命周期框架',
    '--number-sections',
    '--table-of-contents',
    '--toc-depth=3',
    '-V', 'mainfont=微软雅黑',
    '-V', 'CJKmainfont=微软雅黑',
    '-V', 'geometry:margin=1.8cm',
    '-V', 'papersize=a4',
]

result = subprocess.run(pandoc_args, capture_output=True, text=True, timeout=120, cwd=str(PROJECT))
if result.returncode != 0:
    print(f"Pandoc ERROR: {result.stderr[:500]}")
    # Retry without reference-docx
    pandoc_args.remove('--reference-doc=' + str(PROJECT / 'AI协作项目全生命周期框架.docx'))
    result = subprocess.run(pandoc_args, capture_output=True, text=True, timeout=120, cwd=str(PROJECT))

output_docx = WORK_DIR / 'output.docx'
if output_docx.exists():
    print(f"Pandoc output: {output_docx} ({output_docx.stat().st_size} bytes)")
else:
    print(f"Pandoc FAILED: {result.stderr[:500]}")
    exit(1)

# ============================================================
# Step 4: Copy to final location (backup old)
# ============================================================
backup_path = PROJECT / f"AI协作项目全生命周期框架.docx.v164_pre_regenerate.bak"
if DOCX_OUT.exists():
    shutil.copy2(DOCX_OUT, backup_path)
    print(f"Backup: {backup_path}")

shutil.copy2(output_docx, DOCX_OUT)
print(f"Final DOCX: {DOCX_OUT} ({DOCX_OUT.stat().st_size} bytes)")

# ============================================================
# Step 5: Clean docx metadata
# ============================================================
import zipfile, tempfile as tmpf
fd, tmp_path = tmpf.mkstemp(suffix='.docx')
os.close(fd)
with zipfile.ZipFile(DOCX_OUT, 'r') as zin:
    with zipfile.ZipFile(tmp_path, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == 'docProps/core.xml':
                data = re.sub(rb'<cp:lastModifiedBy>[^<]*</cp:lastModifiedBy>', b'<cp:lastModifiedBy/>', data)
                data = re.sub(rb'<dc:creator>[^<]*</dc:creator>', b'<dc:creator/>', data)
                data = re.sub(rb'<cp:lastPrinted>[^<]*</cp:lastPrinted>', b'<cp:lastPrinted/>', data)
                data = re.sub(rb'<cp:revision>[^<]*</cp:revision>', b'<cp:revision>1</cp:revision>', data)
                # Add version if missing
                if b'<cp:version>' not in data:
                    data = data.replace(b'</cp:coreProperties>',
                        b'<cp:version>v1.6.4</cp:version></cp:coreProperties>')
            zout.writestr(item, data)
shutil.move(tmp_path, str(DOCX_OUT))
print("Metadata cleaned")

print("\n=== DONE ===")
print(f"Final: {DOCX_OUT} ({DOCX_OUT.stat().st_size} bytes)")
