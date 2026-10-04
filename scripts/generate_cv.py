"""Generate the downloadable CV from the built online CV.

Run after `bundle exec jekyll build --safe`.
Requires beautifulsoup4 and reportlab. Install them with pip in a virtual environment.
"""
from pathlib import Path
from html import escape

from bs4 import BeautifulSoup
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://farhadabedinzadeh.github.io"
OUT = ROOT / "files/cv/Farhad-Abedinzadeh-CV.pdf"
soup = BeautifulSoup((ROOT / "_site/cv/index.html").read_text(), "html.parser")
font_dir = Path("/usr/share/fonts/truetype/dejavu")
for name, filename in [("CV", "DejaVuSans.ttf"), ("CV-Bold", "DejaVuSans-Bold.ttf")]:
    pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
pdfmetrics.registerFontFamily("CV", normal="CV", bold="CV-Bold")
INK, MUTED, ACCENT = map(colors.HexColor, ["#203536", "#536461", "#a14e30"])
styles = {
    "name": ParagraphStyle("name", fontName="CV-Bold", fontSize=19, leading=24, textColor=INK, spaceAfter=9),
    "sub": ParagraphStyle("sub", fontName="CV", fontSize=10, leading=15, textColor=MUTED, spaceAfter=10),
    "heading": ParagraphStyle("heading", fontName="CV-Bold", fontSize=13, leading=16, textColor=ACCENT, spaceBefore=10, spaceAfter=7, keepWithNext=True),
    "rowtitle": ParagraphStyle("rowtitle", fontName="CV-Bold", fontSize=9, leading=12, textColor=INK, spaceAfter=3, keepWithNext=True),
    "body": ParagraphStyle("body", fontName="CV", fontSize=8.6, leading=11.2, textColor=MUTED, spaceAfter=4),
    "meta": ParagraphStyle("meta", fontName="CV", fontSize=7.6, leading=11, textColor=ACCENT, spaceAfter=3),
}

def text(tag):
    return tag.get_text(" ", strip=True).replace("–", "-").replace("—", "-").replace("‑", "-").replace("↗", "").strip()

def para(value, style="body"):
    return Paragraph(escape(value), styles[style])

def footer(canvas, doc):
    canvas.setStrokeColor(colors.HexColor("#dedfd7"))
    canvas.line(48, 39, A4[0] - 48, 39)
    canvas.setFillColor(MUTED)
    canvas.setFont("CV", 7)
    canvas.drawString(48, 26, "Farhad Abedinzadeh Torghabeh | Academic CV")
    canvas.drawRightString(A4[0] - 48, 26, str(doc.page))

story = [para("Farhad Abedinzadeh Torghabeh", "name"), para("PhD researcher | Durham University | AI & Medical Imaging", "sub")]
story += [para("Durham, United Kingdom | farhaad.abedinzade@gmail.com", "body"), para("farhadabedinzadeh.github.io | ORCID: 0000-0002-0021-2009", "body"), Spacer(1, 5)]
for section in soup.select(".cv-section"):
    heading = text(section.h2)
    story.append(para(heading, "heading"))
    rows = section.select(".cv-row")
    if rows:
        for row in rows:
            block = [para(text(row.select_one(".timeline-date")), "meta"), para(text(row.h3), "rowtitle")]
            block.extend(para(text(p)) for p in row.select("p"))
            block.append(Spacer(1, 1))
            story.append(KeepTogether(block))
    elif section.select(".publication"):
        for paper in section.select(".publication"):
            link = paper.h3.a
            title = escape(text(link))
            block = [Paragraph(f'<a href="{escape(link["href"], quote=True)}" color="#163e40">{title}</a>', styles["rowtitle"])]
            block.extend([para(text(paper.select_one(".paper-meta")), "meta"), para(text(paper.select_one(".authors"))), Spacer(1, 4)])
            story.append(KeepTogether(block))
        story.append(Paragraph(f'Complete bibliography: <a href="{SITE_URL}/publications/" color="#163e40">{SITE_URL}/publications/</a>', styles["body"]))
    elif section.select(".cv-skills"):
        for div in section.select(".cv-skills > div"):
            story.append(KeepTogether([para(text(div.h3), "rowtitle"), para(text(div.p))]))
    elif section.ul:
        story.extend(para("- " + text(li)) for li in section.select("li"))
    else:
        story.extend(para(text(p)) for p in section.select("p"))

OUT.parent.mkdir(parents=True, exist_ok=True)
SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=48, rightMargin=48, topMargin=38, bottomMargin=48,
                  title="Academic CV - Farhad Abedinzadeh Torghabeh", author="Farhad Abedinzadeh Torghabeh").build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
