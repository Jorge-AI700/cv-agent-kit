#!/usr/bin/env python3
"""Render a tailored CV Markdown file to DOCX and, when possible, PDF.

The expected Markdown structure is documented in
../references/markdown-format.md (next to this skill).

Dependencies:
  pip install python-docx
  LibreOffice (soffice) for PDF export
  poppler-utils (pdfinfo, pdftoppm) for --check page count and preview
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

try:
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_TAB_ALIGNMENT
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Emu, Inches, Mm, Pt
except ImportError:
    sys.stderr.write(
        "This script needs python-docx. Install it with:\n"
        "  pip install python-docx\n"
    )
    sys.exit(1)


FONT_NAME = "Arial"
MARGIN_SIDE = Inches(0.6)
MARGIN_TOP_BOTTOM = Inches(0.42)
BULLET_LEFT = Inches(0.2)
BULLET_HANGING = Inches(-0.13)
BULLET_MARKER = "• "

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)(?:\s+#*)?\s*$")
BULLET_RE = re.compile(r"^[-*+]\s+(.*\S)\s*$")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)


@dataclass
class Entry:
    title: str
    dates: str = ""
    org: str = ""
    bullets: list[str] = field(default_factory=list)


@dataclass
class Section:
    heading: str
    blocks: list[object] = field(default_factory=list)


@dataclass
class CV:
    name: str = ""
    headline: str = ""
    contact: str = ""
    sections: list[Section] = field(default_factory=list)


def strip_markup_wrappers(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if text.startswith("\ufeff"):
        text = text[1:]
    text = HTML_COMMENT_RE.sub("", text)
    text = FRONTMATTER_RE.sub("", text, count=1)
    return text.strip("\n")


def looks_like_contact(text: str) -> bool:
    lowered = text.lower()
    return bool(
        "@" in text
        or "linkedin." in lowered
        or "github." in lowered
        or "http://" in lowered
        or "https://" in lowered
        or "tel:" in lowered
        or re.search(r"\+\d", text)
    )


def split_title_and_dates(heading: str) -> tuple[str, str]:
    if " | " in heading:
        title, dates = heading.rsplit(" | ", 1)
        return title.strip(), dates.strip()
    return heading.strip(), ""


def parse_cv(markdown: str) -> CV:
    """Parse a tailored CV written in the documented Markdown structure."""
    lines = strip_markup_wrappers(markdown).split("\n")
    cv = CV()
    i = 0
    n = len(lines)

    def skip_blank(idx: int) -> int:
        while idx < n and not lines[idx].strip():
            idx += 1
        return idx

    i = skip_blank(0)
    if i >= n or not HEADING_RE.match(lines[i]) or HEADING_RE.match(lines[i]).group(1) != "#":
        raise ValueError(
            "The Markdown file must start with a level-1 heading "
            "containing the candidate's name, for example: # Firstname Lastname"
        )
    cv.name = HEADING_RE.match(lines[i]).group(2).strip()
    i += 1
    i = skip_blank(i)

    preamble: list[str] = []
    while i < n:
        raw = lines[i].strip()
        if not raw:
            i += 1
            if preamble:
                # A blank line after the first preamble paragraph is fine;
                # stop only once a heading or two paragraphs have been seen
                # and the next non-blank line is a heading.
                peek = skip_blank(i)
                if peek < n and HEADING_RE.match(lines[peek]):
                    break
            continue
        if HEADING_RE.match(lines[i]) or BULLET_RE.match(raw):
            break
        preamble.append(raw)
        i += 1
        if len(preamble) == 2:
            i = skip_blank(i)
            break

    if len(preamble) == 1:
        if looks_like_contact(preamble[0]):
            cv.contact = preamble[0]
        else:
            cv.headline = preamble[0]
    elif len(preamble) >= 2:
        cv.headline = preamble[0]
        cv.contact = preamble[1]

    current: Section | None = None

    def ensure_section() -> Section:
        nonlocal current
        if current is None:
            current = Section(heading="")
            cv.sections.append(current)
        return current

    while i < n:
        raw = lines[i].rstrip()
        stripped = raw.strip()
        if not stripped:
            i += 1
            continue

        heading = HEADING_RE.match(stripped)
        if heading:
            level = len(heading.group(1))
            text = heading.group(2).strip()
            if level <= 2:
                current = Section(heading=text)
                cv.sections.append(current)
                i += 1
                continue
            # ### entry title | dates
            title, dates = split_title_and_dates(text)
            entry = Entry(title=title, dates=dates)
            i += 1
            i = skip_blank(i)
            if i < n:
                peek = lines[i].strip()
                if (
                    peek
                    and not HEADING_RE.match(peek)
                    and not BULLET_RE.match(peek)
                ):
                    entry.org = peek
                    i += 1
            while i < n:
                row = lines[i].strip()
                if not row:
                    peek_i = skip_blank(i)
                    if peek_i < n and BULLET_RE.match(lines[peek_i].strip()):
                        i = peek_i
                        continue
                    break
                bullet = BULLET_RE.match(row)
                if bullet:
                    entry.bullets.append(bullet.group(1).strip())
                    i += 1
                    continue
                break
            ensure_section().blocks.append(entry)
            continue

        bullet = BULLET_RE.match(stripped)
        if bullet:
            ensure_section().blocks.append(("bullet", bullet.group(1).strip()))
            i += 1
            continue

        ensure_section().blocks.append(("para", stripped))
        i += 1

    if not cv.name:
        raise ValueError("Could not find a candidate name in the Markdown file.")
    return cv


def set_run_font(run, size_pt: float, bold: bool | None = None) -> None:
    run.font.name = FONT_NAME
    run.font.size = Pt(size_pt)
    if bold is not None:
        run.bold = bold
    run.font.color.rgb = None
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.insert(0, rFonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rFonts.set(qn(attr), FONT_NAME)


def add_text_with_inline(paragraph, text: str, size_pt: float, bold: bool = False) -> None:
    """Add text, honoring **bold** markers and [label](url) links."""
    text = LINK_RE.sub(lambda m: m.group(1) or m.group(2), text)
    pos = 0
    for match in BOLD_RE.finditer(text):
        if match.start() > pos:
            run = paragraph.add_run(text[pos : match.start()])
            set_run_font(run, size_pt, bold)
        run = paragraph.add_run(match.group(1))
        set_run_font(run, size_pt, True)
        pos = match.end()
    if pos < len(text):
        run = paragraph.add_run(text[pos:])
        set_run_font(run, size_pt, bold)
    if not text:
        run = paragraph.add_run("")
        set_run_font(run, size_pt, bold)


def set_paragraph_style(
    paragraph,
    *,
    before: float = 0,
    after: float = 1,
    keep_with_next: bool = False,
    left: object | None = None,
    first_line: object | None = None,
) -> None:
    fmt = paragraph.paragraph_format
    fmt.space_before = Pt(before)
    fmt.space_after = Pt(after)
    fmt.line_spacing_rule = WD_LINE_SPACING.SINGLE
    fmt.line_spacing = 1.0
    fmt.keep_with_next = keep_with_next
    if left is not None:
        fmt.left_indent = left
    if first_line is not None:
        fmt.first_line_indent = first_line
    pPr = paragraph._p.get_or_add_pPr()
    for tag in ("autoSpaceDE", "autoSpaceDN"):
        el = pPr.find(qn(f"w:{tag}"))
        if el is None:
            el = OxmlElement(f"w:{tag}")
            pPr.append(el)
        el.set(qn("w:val"), "0")


def set_bottom_border(paragraph, color: str = "000000", sz: str = "8", space: str = "3") -> None:
    pPr = paragraph._p.get_or_add_pPr()
    for child in pPr.findall(qn("w:pBdr")):
        pPr.remove(child)
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), sz)
    bottom.set(qn("w:space"), space)
    bottom.set(qn("w:color"), color)
    pBdr.append(bottom)
    pPr.append(pBdr)


def add_tab_stop(paragraph, position) -> None:
    tabs = paragraph.paragraph_format.tab_stops
    tabs.add_tab_stop(position, WD_TAB_ALIGNMENT.RIGHT)


def configure_document(doc: Document, page_size: str, body_size: float) -> object:
    section = doc.sections[0]
    if page_size == "letter":
        section.page_width = Inches(8.5)
        section.page_height = Inches(11)
    else:
        section.page_width = Mm(210)
        section.page_height = Mm(297)
    section.left_margin = MARGIN_SIDE
    section.right_margin = MARGIN_SIDE
    section.top_margin = MARGIN_TOP_BOTTOM
    section.bottom_margin = MARGIN_TOP_BOTTOM
    section.header_distance = Inches(0.3)
    section.footer_distance = Inches(0.3)

    normal = doc.styles["Normal"]
    normal.font.name = FONT_NAME
    normal.font.size = Pt(body_size)
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.line_spacing = 1.0
    rPr = normal.element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.insert(0, rFonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rFonts.set(qn(attr), FONT_NAME)
    return section


def text_width_of(section) -> Emu:
    return Emu(int(section.page_width) - int(section.left_margin) - int(section.right_margin))


def build_docx(cv: CV, dest: Path, page_size: str, font_size: float) -> Path:
    heading_size = font_size + 0.5
    contact_size = max(font_size - 0.5, 8.5)
    name_size = 16.0
    headline_size = font_size + 0.5

    doc = Document()
    section = configure_document(doc, page_size, font_size)
    text_width = text_width_of(section)

    name_p = doc.add_paragraph()
    set_paragraph_style(name_p, before=0, after=2, keep_with_next=True)
    add_text_with_inline(name_p, cv.name, name_size, bold=True)

    if cv.headline:
        headline_p = doc.add_paragraph()
        set_paragraph_style(headline_p, before=0, after=1, keep_with_next=True)
        add_text_with_inline(headline_p, cv.headline, headline_size, bold=False)

    if cv.contact:
        contact_p = doc.add_paragraph()
        set_paragraph_style(contact_p, before=0, after=8, keep_with_next=True)
        add_text_with_inline(contact_p, cv.contact, contact_size, bold=False)

    for section_index, cv_section in enumerate(cv.sections):
        if cv_section.heading:
            heading_p = doc.add_paragraph()
            before = 6 if section_index == 0 else 11
            set_paragraph_style(heading_p, before=before, after=4, keep_with_next=True)
            set_bottom_border(heading_p)
            add_text_with_inline(
                heading_p, cv_section.heading.upper(), heading_size, bold=True
            )

        first_entry = True
        for block in cv_section.blocks:
            if isinstance(block, Entry):
                title_p = doc.add_paragraph()
                set_paragraph_style(
                    title_p,
                    before=2 if first_entry else 8,
                    after=1,
                    keep_with_next=True,
                )
                add_text_with_inline(title_p, block.title, font_size, bold=True)
                if block.dates:
                    add_tab_stop(title_p, text_width)
                    run = title_p.add_run("\t" + block.dates)
                    set_run_font(run, font_size, bold=False)
                if block.org:
                    org_p = doc.add_paragraph()
                    set_paragraph_style(org_p, before=0, after=1, keep_with_next=True)
                    add_text_with_inline(org_p, block.org, font_size, bold=False)
                for bullet_text in block.bullets:
                    add_bullet(doc, bullet_text, font_size)
                first_entry = False
            elif isinstance(block, tuple) and block[0] == "bullet":
                add_bullet(doc, block[1], font_size)
                first_entry = False
            elif isinstance(block, tuple) and block[0] == "para":
                para = doc.add_paragraph()
                set_paragraph_style(para, before=0, after=3)
                add_text_with_inline(para, block[1], font_size, bold=False)
                first_entry = False

    dest.parent.mkdir(parents=True, exist_ok=True)
    if cv.name:
        doc.core_properties.title = cv.name
        doc.core_properties.author = cv.name
    doc.core_properties.subject = "CV"
    doc.save(dest)
    return dest


def add_bullet(doc: Document, text: str, font_size: float) -> None:
    paragraph = doc.add_paragraph()
    set_paragraph_style(
        paragraph,
        before=0,
        after=1,
        left=BULLET_LEFT,
        first_line=BULLET_HANGING,
    )
    run = paragraph.add_run(BULLET_MARKER)
    set_run_font(run, font_size, bold=False)
    add_text_with_inline(paragraph, text, font_size, bold=False)


def find_soffice() -> str | None:
    return shutil.which("soffice") or shutil.which("libreoffice")


def convert_to_pdf(docx_path: Path, pdf_path: Path) -> Path:
    soffice = find_soffice()
    if not soffice:
        raise FileNotFoundError("soffice")

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="cv-render-") as tmp:
        profile = Path(tmp) / "lo-profile"
        profile.mkdir()
        outdir = Path(tmp) / "out"
        outdir.mkdir()
        cmd = [
            soffice,
            "--headless",
            "--norestore",
            "--nolockcheck",
            "--nodefault",
            "--nofirststartwizard",
            f"-env:UserInstallation={profile.resolve().as_uri()}",
            "--convert-to",
            "pdf",
            "--outdir",
            str(outdir),
            str(docx_path.resolve()),
        ]
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=180, check=False
        )
        produced = outdir / (docx_path.stem + ".pdf")
        if result.returncode != 0 or not produced.exists():
            detail = (result.stderr or result.stdout or "").strip()
            raise RuntimeError(
                "LibreOffice failed to convert the DOCX to PDF"
                + (f": {detail}" if detail else f" (exit {result.returncode}).")
            )
        shutil.copy2(produced, pdf_path)
    return pdf_path


def pdf_page_count(pdf_path: Path) -> int:
    pdfinfo = shutil.which("pdfinfo")
    if not pdfinfo:
        raise FileNotFoundError("pdfinfo")
    result = subprocess.run(
        [pdfinfo, str(pdf_path)], capture_output=True, text=True, check=True
    )
    for line in result.stdout.splitlines():
        if line.lower().startswith("pages:"):
            return int(line.split(":", 1)[1].strip())
    raise RuntimeError("Could not parse a page count from pdfinfo output.")


def render_preview(pdf_path: Path, png_path: Path) -> Path:
    pdftoppm = shutil.which("pdftoppm")
    if not pdftoppm:
        raise FileNotFoundError("pdftoppm")
    png_path = png_path.with_suffix(".png")
    png_path.parent.mkdir(parents=True, exist_ok=True)
    prefix = png_path.with_suffix("")
    cmd = [
        pdftoppm,
        "-png",
        "-f",
        "1",
        "-l",
        "1",
        "-singlefile",
        "-r",
        "150",
        str(pdf_path),
        str(prefix),
    ]
    subprocess.run(cmd, capture_output=True, check=True)
    if not png_path.exists():
        raise RuntimeError(f"pdftoppm did not write {png_path}")
    return png_path


def resolve_output_paths(input_path: Path, output: str | None) -> tuple[Path, Path]:
    if output:
        out = Path(output)
        if out.suffix.lower() in {".pdf", ".docx", ".md"}:
            stem = out.with_suffix("")
        else:
            stem = out
        return stem.with_suffix(".docx"), stem.with_suffix(".pdf")
    return input_path.with_suffix(".docx"), input_path.with_suffix(".pdf")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Convert a tailored CV Markdown file into DOCX and PDF. "
            "See ../references/markdown-format.md for the input structure."
        )
    )
    parser.add_argument("input", type=Path, help="Path to the tailored cv.md file")
    parser.add_argument(
        "-o",
        "--output",
        help="Output path or stem (for example Firstname-Lastname-CV-Company.pdf)",
    )
    parser.add_argument(
        "--page-size",
        choices=("a4", "letter"),
        default="a4",
        help="Page size (default: a4)",
    )
    parser.add_argument(
        "--font-size",
        type=float,
        default=10.0,
        help="Body font size in points (default: 10.0; QA range is about 9.5 to 10.5)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Print the PDF page count and render page 1 to a PNG preview",
    )
    parser.add_argument(
        "--preview",
        type=Path,
        help="Where to write the page-1 PNG when using --check (default: alongside the PDF)",
    )
    parser.add_argument(
        "--docx-only",
        action="store_true",
        help="Write DOCX only, even if LibreOffice is available",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    input_path = args.input.expanduser()
    if not input_path.is_file():
        sys.stderr.write(f"Input file not found: {input_path}\n")
        return 1

    try:
        cv = parse_cv(input_path.read_text(encoding="utf-8"))
    except ValueError as exc:
        sys.stderr.write(f"{exc}\n")
        return 1

    docx_path, pdf_path = resolve_output_paths(input_path, args.output)
    try:
        build_docx(cv, docx_path, args.page_size, args.font_size)
    except OSError as exc:
        sys.stderr.write(f"Could not write DOCX: {exc}\n")
        return 1
    print(f"Wrote DOCX: {docx_path}")

    if args.docx_only:
        if args.check:
            sys.stderr.write("--check needs a PDF; omit --docx-only.\n")
            return 1
        return 0

    if not find_soffice():
        message = (
            "LibreOffice (soffice) was not found, so no PDF was created. "
            "Install LibreOffice to enable PDF export, or use the DOCX above."
        )
        print(message)
        if args.check:
            sys.stderr.write("--check needs LibreOffice to create a PDF.\n")
            return 1
        return 0

    try:
        convert_to_pdf(docx_path, pdf_path)
    except Exception as exc:  # noqa: BLE001 — surface conversion errors cleanly
        sys.stderr.write(f"{exc}\n")
        return 1
    print(f"Wrote PDF:  {pdf_path}")

    page_count = None
    if shutil.which("pdfinfo"):
        try:
            page_count = pdf_page_count(pdf_path)
            print(f"Pages: {page_count}")
        except Exception as exc:  # noqa: BLE001
            sys.stderr.write(f"Could not read page count: {exc}\n")
            if args.check:
                return 1
    elif args.check:
        sys.stderr.write(
            "pdfinfo was not found. Install poppler-utils to report the page count.\n"
        )
        return 1
    else:
        print("Pages: unknown (install poppler-utils to print the page count)")

    if args.check:
        preview_path = args.preview
        if preview_path is None:
            preview_path = pdf_path.with_suffix(".png")
        try:
            written = render_preview(pdf_path, preview_path)
        except FileNotFoundError:
            sys.stderr.write(
                "pdftoppm was not found. Install poppler-utils to render a preview PNG.\n"
            )
            return 1
        except Exception as exc:  # noqa: BLE001
            sys.stderr.write(f"Could not render preview: {exc}\n")
            return 1
        print(f"Wrote preview: {written}")

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
