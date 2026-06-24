#!/usr/bin/env python3
"""
Build the donor-facing Case for Support PDF for The Burn Center of the Caribbean.

Content mirrors docs/Case-for-Support.md. Charitable-status language is feasibility-accurate
("being established", "intended to qualify", "pending") — this is a public document.

Run:  python3 scripts/build_case_for_support.py
Out:  docs/Case-for-Support.pdf
"""
import os

TITLE = "The Burn Center of the Caribbean"
SUBTITLE = "A Case for Support"
HOOK = "When a child is severely burned in Puerto Rico, two emergencies begin at once."

BLOCKS = [
    ("p", "The first is medical. The second is financial. Puerto Rico — an island of 3.2 million "
          "people — has <b>no burn center of its own.</b> The most serious cases, many of them "
          "children, are flown more than a thousand miles to the mainland, away from their families "
          "during the most frightening days of their lives. One Puerto Rican family was billed "
          "<b>$1.7 million.</b> A severe burn can take a child's skin; the debt that follows can "
          "take a family's future."),
    ("h2", "A first for the island"),
    ("p", "We are building Puerto Rico's first comprehensive burn center built around its children — "
          "and a financial safety net so that <b>no family is bankrupted for saving their child's "
          "life.</b> Every child of a low-income family is treated with full expertise, regardless "
          "of what the family can pay."),
    ("h2", "A model built to actually work here"),
    ("p", "Burn surgery is among the scarcest specialties in American medicine: roughly <b>300 "
          "surgeons for the entire country,</b> almost none in the Caribbean. So we don't wait for "
          "an impossible number of specialists. We multiply the reach of a single expert burn "
          "surgeon through a network of specially trained nurse practitioners who bring wound care "
          "into communities across the island — <b>expert care, close to home, at a fraction of the "
          "cost.</b>"),
    ("h2", "Your required gift can build something that has never existed"),
    ("p", "As an Act 60 resident, your annual child-poverty contribution is already required. "
          "Directed here, it becomes <b>founding capital for the first pediatric burn safety net in "
          "Puerto Rico's history</b> — a cause being established as a CECFL-listed, fully compliant "
          "charitable arm, in the place you now call home. You won't be one more donor to an "
          "established charity. You will be a <i>founder</i> of something that protects children for "
          "generations."),
    ("h2", "Your impact"),
    ("table", [
        ["Gift", "Circle", "What it builds"],
        ["$5,000", "Guardian",
         "Your required child-poverty gift, transformed — weeks of expert burn care for low-income "
         "children through our nurse-practitioner network."],
        ["$25,000", "Protector",
         "The complete outpatient recovery of several children — every dressing, follow-up, and "
         "scar treatment — at no cost to their families."],
        ["$100,000", "Founder's Circle",
         "A full year of a specially trained burn nurse practitioner — one provider, hundreds of "
         "children cared for close to home."],
        ["$250,000+", "Founding Benefactor",
         "Establish and name a community burn clinic, or endow a program in perpetuity. Founding "
         "board invitation."],
    ]),
    ("h2", "Join us in building it"),
    ("p", "The Burn Center of the Caribbean's charitable arm is being established as a CECFL-listed "
          "nonprofit, so that an Act 60 child-poverty donation directed here is intended to qualify "
          "toward your annual requirement; listing and tax-exempt status are pending. "
          "<b>To give or learn more:</b> [name · email · phone]."),
]

TAGLINE = "Heal the child. Protect the family. Break the cycle."
TAGLINE_ES = "Sanar al niño. Proteger a la familia. Romper el ciclo."
FINEPRINT = ("Illustrative impact based on projected program costs at feasibility stage. The "
             "Center's charitable arm is being established as a CECFL-listed nonprofit; listing and "
             "tax-exempt status are pending.")

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(os.path.dirname(HERE), "docs")
os.makedirs(DOCS, exist_ok=True)


def build():
    from reportlab.lib.pagesizes import LETTER
    from reportlab.lib.units import inch
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib import colors
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                    TableStyle, HRFlowable)

    DEEP = colors.HexColor("#0E3A43")
    TEAL = colors.HexColor("#127C8E")
    AQUA = colors.HexColor("#5FB6C4")
    MIST = colors.HexColor("#EEF5F5")
    MUTED = colors.HexColor("#5C6F77")
    INK = colors.HexColor("#22323A")

    title = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=21, textColor=DEEP, leading=25)
    subtitle = ParagraphStyle("subtitle", fontName="Helvetica-Bold", fontSize=12.5, textColor=TEAL,
                              leading=16, spaceAfter=12)
    hook = ParagraphStyle("hook", fontName="Helvetica-BoldOblique", fontSize=14, textColor=DEEP,
                          leading=19, spaceAfter=12)
    h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12.5, textColor=DEEP, leading=15,
                        spaceBefore=14, spaceAfter=5)
    body = ParagraphStyle("body", fontName="Helvetica", fontSize=10.4, textColor=INK, leading=15,
                          spaceAfter=8)
    cell = ParagraphStyle("cell", fontName="Helvetica", fontSize=9.4, textColor=INK, leading=13)
    cellb = ParagraphStyle("cellb", fontName="Helvetica-Bold", fontSize=9.6, textColor=DEEP, leading=13)
    tag = ParagraphStyle("tag", fontName="Helvetica-Bold", fontSize=13.5, textColor=TEAL, leading=18)
    tages = ParagraphStyle("tages", fontName="Helvetica-Oblique", fontSize=10, textColor=MUTED, leading=13)
    disc = ParagraphStyle("disc", fontName="Helvetica-Oblique", fontSize=8.2, textColor=MUTED, leading=11)

    story = [Paragraph(TITLE, title), Paragraph(SUBTITLE, subtitle), Paragraph(HOOK, hook)]
    for kind, val in BLOCKS:
        if kind == "h2":
            story.append(Paragraph(val, h2))
        elif kind == "p":
            story.append(Paragraph(val, body))
        elif kind == "table":
            data = []
            for r, row in enumerate(val):
                if r == 0:
                    data.append([Paragraph(f"<b>{c}</b>", cellb) for c in row])
                else:
                    data.append([Paragraph(row[0], cellb), Paragraph(row[1], cellb),
                                 Paragraph(row[2], cell)])
            t = Table(data, colWidths=[0.95 * inch, 1.35 * inch, 4.1 * inch])
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), DEEP),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, MIST]),
                ("GRID", (0, 0), (-1, -1), 0.5, AQUA),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]))
            # header row white text
            for c in range(3):
                data[0][c] = Paragraph(f'<font color="white"><b>{val[0][c]}</b></font>', cellb)
            story += [Spacer(1, 6), t, Spacer(1, 6)]

    story += [Spacer(1, 14),
              HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#D8E6E6")),
              Spacer(1, 10), Paragraph(TAGLINE, tag), Paragraph(TAGLINE_ES, tages),
              Spacer(1, 12), Paragraph(FINEPRINT, disc)]

    path = os.path.join(DOCS, "Case-for-Support.pdf")
    SimpleDocTemplate(path, pagesize=LETTER, leftMargin=0.9 * inch, rightMargin=0.9 * inch,
                      topMargin=0.85 * inch, bottomMargin=0.8 * inch,
                      title="The Case for Support",
                      author="The Burn Center of the Caribbean").build(story)
    return path


if __name__ == "__main__":
    print("wrote:", build())
