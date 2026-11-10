#!/usr/bin/env python3
"""Render a CV written in Markdown to DOCX and PDF with a clean one-column A4 layout.

Usage: python3 render_cv.py cv.md [--out DIR] [--size 10] [--name FILE_STEM]

Markdown format (see SKILL.md):
  # Full Name
  contact line                      (plain lines before the first ## are centred header lines)
  status line
  ## Section
  plain paragraph                   (**bold** supported)
  ### Title — Organisation | Location | Dates
  _optional italic context line_
  - bullet
Requires: python-docx, LibreOffice (soffice) for PDF.
"""
import argparse, re, subprocess, sys
from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_TAB_ALIGNMENT, WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def base_doc(size):
    d = Document()
    for s in d.sections:
        s.page_width, s.page_height = Inches(8.27), Inches(11.69)  # A4
        s.left_margin = s.right_margin = Inches(0.6)
        s.top_margin = s.bottom_margin = Inches(0.42)
    st = d.styles['Normal']; st.font.name = 'Arial'; st.font.size = Pt(size)
    st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial')
    pf = st.paragraph_format; pf.space_after = Pt(0); pf.space_before = Pt(0); pf.line_spacing = 1.0
    return d

def rich(p, text):
    for part in re.split(r'(\*\*[^*]+\*\*)', text):
        if part.startswith('**') and part.endswith('**'): p.add_run(part[2:-2]).bold = True
        elif part: p.add_run(part)

def border_bottom(p):
    pPr = p._p.get_or_add_pPr(); b = OxmlElement('w:pBdr'); e = OxmlElement('w:bottom')
    for k, v in (('val', 'single'), ('sz', '6'), ('space', '1'), ('color', '444444')): e.set(qn('w:' + k), v)
    b.append(e); pPr.append(b)

def section(d, title):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(5); p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(title.upper()); r.bold = True; r.font.size = Pt(10.5); border_bottom(p)

def entry(d, title, org, loc, dates):
    p = d.add_paragraph(); p.paragraph_format.tab_stops.add_tab_stop(Inches(7.07), WD_TAB_ALIGNMENT.RIGHT)
    p.paragraph_format.space_before = Pt(4); p.paragraph_format.keep_with_next = True
    p.add_run(title).bold = True
    if org: p.add_run(f', {org}')
    inline = len(title) + len(org) + len(loc) + len(dates) + 5 <= 100
    if loc and inline: p.add_run(f' | {loc}').italic = True
    if dates: p.add_run(f'\t{dates}')
    return None if (inline or not loc) else loc

def sub(d, text):
    p = d.add_paragraph(); r = p.add_run(text); r.italic = True; r.font.size = Pt(8.5)
    p.paragraph_format.keep_with_next = True

def bullet(d, text):
    p = d.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Inches(0.22); rich(p, text)

def render(md, size):
    d = base_doc(size); lines = [l.rstrip() for l in md.splitlines()]
    in_header = True; pending_loc = None
    for i, l in enumerate(lines):
        s = l.strip()
        if not s or s.startswith('<!--'): continue
        if s.startswith('# '):
            p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(s[2:].strip()); r.bold = True; r.font.size = Pt(17); continue
        if s.startswith('## '):
            in_header = False; section(d, s[3:].strip()); continue
        if in_header:
            p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(s); r.font.size = Pt(9.5); continue
        if s.startswith('### '):
            head = s[4:].strip(); parts = [x.strip() for x in head.split('|')]
            to = re.split(r'\s+[—–]\s+', parts[0], maxsplit=1)
            title, org = to[0], (to[1] if len(to) > 1 else '')
            loc = parts[1] if len(parts) > 2 else ''
            dates = parts[-1] if len(parts) > 1 else ''
            pending_loc = entry(d, title, org, loc, dates)
            nxt = next((x.strip() for x in lines[i+1:] if x.strip()), '')
            if pending_loc and not (nxt.startswith('_') and nxt.endswith('_')):
                sub(d, pending_loc); pending_loc = None
            continue
        if s.startswith('_') and s.endswith('_') and len(s) > 2:
            t = s[1:-1]; sub(d, f'{pending_loc}. {t}' if pending_loc else t); pending_loc = None; continue
        if s.startswith(('- ', '* ')): bullet(d, s[2:].strip()); continue
        p = d.add_paragraph(); rich(p, s); p.paragraph_format.space_after = Pt(1)
    return d

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('cv'); ap.add_argument('--out')
    ap.add_argument('--size', type=float, default=10); ap.add_argument('--name')
    a = ap.parse_args(); src = Path(a.cv); out = Path(a.out or src.parent); out.mkdir(parents=True, exist_ok=True)
    stem = a.name or src.stem
    docx_path = out / f'{stem}.docx'; render(src.read_text(encoding='utf-8'), a.size).save(docx_path)
    soffice = 'soffice'
    if sys.platform == 'darwin' and not subprocess.run(['which', 'soffice'], capture_output=True).stdout:
        soffice = '/Applications/LibreOffice.app/Contents/MacOS/soffice'
    pdf = None
    pages = None
    try:
        subprocess.run([soffice, '--headless', '--convert-to', 'pdf', '--outdir', str(out), str(docx_path)], check=True, capture_output=True)
        pdf = out / f'{stem}.pdf'
        try:
            info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True).stdout
            m = re.search(r'Pages:\s+(\d+)', info); pages = int(m.group(1)) if m else None
        except FileNotFoundError: pass
    except (FileNotFoundError, subprocess.CalledProcessError):
        pass

    out_msg = f'DOCX {docx_path}'
    if pdf and pdf.exists():
        out_msg += f'\nPDF  {pdf}' + (f'\nPAGES {pages}' if pages else '')
    else:
        out_msg += '\n(Notice: LibreOffice not found or failed; DOCX generated. Open DOCX or install LibreOffice for PDF)'
    print(out_msg)

if __name__ == '__main__': main()
