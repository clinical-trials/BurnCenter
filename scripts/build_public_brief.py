#!/usr/bin/env python3
"""
Build the PUBLIC-SAFE Feasibility Brief (markdown + PDF) for The Burn Center of the Caribbean.

This is the donor/partner-facing summary. It deliberately OMITS the candid internal
material in the v2 brief — donor-capture strategy, competitive "moat" framing, and blunt
reimbursement/economics commentary. Keep the full internal brief private and share on request.

Run:  python3 scripts/build_public_brief.py
Out:  docs/Feasibility-Brief-Public.md  and  docs/Feasibility-Brief-Public.pdf
"""
import os

# ---- single source of content (blocks) ----------------------------------
# ("h2", text) section heading | ("p", text) paragraph | ("ul", [items]) bullets
TITLE = "The Burn Center of the Caribbean"
SUBTITLE = "Feasibility Brief — Public Summary"
META = ("Feasibility-stage summary for prospective partners and supporters. "
        "Figures are directional pending primary-data validation. "
        "Not legal, tax, clinical, or investment advice.")

BLOCKS = [
    ("h2", "1. The Opportunity"),
    ("p", "Puerto Rico — an island of roughly 3.2 million residents — has no centralized burn "
          "center of its own. The most serious cases are delayed and frequently flown more than "
          "a thousand miles to the mainland, away from families during the most frightening days "
          "of a child's life, and at catastrophic cost. We are developing the island's first "
          "comprehensive, child-focused burn center — paired with a financial safety net so that "
          "no family is bankrupted for saving their child's life."),

    ("h2", "2. Mission, Vision & Pillars"),
    ("p", "Mission. The Burn Center of the Caribbean protects the children of Puerto Rico from the "
          "lasting harm of severe burns — healing their injuries close to home, and shielding their "
          "families from the catastrophic medical debt that can turn one tragic moment into lasting "
          "poverty. Every child is treated with dignity and expertise, regardless of what their "
          "family can pay."),
    ("p", "Misión. El Centro de Quemados del Caribe protege a la niñez de Puerto Rico del daño "
          "duradero de las quemaduras graves: sanando sus heridas cerca de casa y protegiendo a sus "
          "familias de la deuda médica catastrófica."),
    ("p", "Vision. A Caribbean where every child can heal from a burn close to home, and no family "
          "is bankrupted for saving their child's life."),
    ("p", "Four pillars:"),
    ("ul", [
        "Charity care — free or subsidized burn treatment for children of low-income families.",
        "Family financial protection — a fund that absorbs catastrophic burn costs and heads off "
        "the medical debt that drives household impoverishment.",
        "Prevention where risk is highest — burn-safety outreach in underserved communities.",
        "Recovery & reintegration — rehabilitation and scar care that keep an injured child from "
        "being disabled out of school and future earning power.",
    ]),

    ("h2", "3. The Need"),
    ("ul", [
        "No centralized burn facility serves Puerto Rico's ~3.2M residents.",
        "Only four professionals on-island are certified in Advanced Burn Life Support (ABLS) — an "
        "emergency burn-care course open to nurses, EMS, ER physicians and surgeons, not a surgical "
        "credential — alongside a documented shortage of fellowship-trained burn surgeons (JBCR, 2025).",
        "US guideline benchmark: at least one burn center per million people, and 1–2 burn surgeons "
        "per 500k–1M; Puerto Rico falls far below.",
        "Documented delays average roughly six days to reach a burn surgeon, with most patients "
        "passing through at least one other facility first.",
        "Severe cases are transferred to the mainland — e.g., the widely reported Puerto Rican "
        "patient billed $1.7M at Brooke Army Medical Center — illustrating both the dependence and "
        "the human cost.",
        "Puerto Rico's high diabetes prevalence (~40%) drives a large chronic-wound population, "
        "expanding the clinical need beyond acute burns.",
    ]),

    ("h2", "4. The Workforce Reality"),
    ("p", "Burn surgery is among the scarcest specialties in American medicine — on the order of "
          "~300 burn surgeons nationally, clustered in mainland academic centers, in a field that is "
          "aging and contracting. Puerto Rico's absence of a burn surgeon reflects this uneven "
          "national distribution. Our approach does not wait for an impossible number of specialists: "
          "we recruit one expert burn surgeon and multiply their reach through a bench of "
          "burn-trained nurse practitioners."),

    ("h2", "5. The Care Model — Two-Tier Hub-and-Spoke"),
    ("p", "Tier 1 — the hub (surgeon-anchored). A central burn center for inpatient and critical "
          "care, surgical excision and grafting, emergency stabilization, and complex case "
          "management — reinforced by telemedicine backup, a mainland verified-center affiliation, "
          "transfer protocols, and, as the program matures, a second surgeon."),
    ("p", "Tier 2 — the spokes (NP-led). Outpatient burn and wound-care clinics at multiple sites "
          "across the island, staffed by nurse practitioners who provide daily continuity: wound "
          "assessment and dressing changes, infection and healing monitoring, scar management, "
          "follow-up, family education, and triage and escalation. This is where most patient "
          "volume and the island's geographic-access gap live."),
    ("p", "Connective tissue. Telemedicine links the surgeon to the spokes between in-person days, "
          "and clear escalation and transfer criteria (aligned to American Burn Association referral "
          "criteria) route patients to the hub when needed. The model extends the scarce resource "
          "without diluting it. Practice details under Puerto Rico's nurse-practitioner framework "
          "will be confirmed with the PR Board of Nursing before scaling."),

    ("h2", "6. Funding Approach"),
    ("p", "The Center's charitable arm is being established as a Puerto Rico nonprofit, intended to "
          "qualify — once certified and listed by the relevant authorities (CECFL / DDEC) — as a "
          "recipient of Act 60 child-poverty donations, and to draw on a diversified funding base: "
          "disaster-preparedness funding, disease-specific grants and philanthropy, regional "
          "self-pay, and clinical reimbursement. The foundation will be governed independently of "
          "its donors, with restricted-funds accounting that keeps charitable dollars funding "
          "charitable care. Charitable listing and tax-exempt status are pending."),

    ("h2", "7. Regulatory & Accreditation Pathway"),
    ("ul", [
        "Clinical/hospital: CMS conditions of participation, EMTALA, HIPAA, territory licensing, "
        "and hospital accreditation (Joint Commission).",
        "Burn credibility: American Burn Association Burn Center Verification across the full "
        "continuum of care is the standard we are building toward.",
        "Nurse-practitioner model: collaborative-agreement terms, supervision ratios, and "
        "prescriptive authority confirmed with the PR Board of Nursing.",
        "Nonprofit/funding: nonprofit formation, PR tax-exempt status, and child-poverty "
        "certification, with restricted-funds accounting.",
        "Professional counsel — healthcare, PR nonprofit/tax, and nursing-regulatory — is engaged "
        "to shape structure and certification before commitments.",
    ]),

    ("h2", "8. Key Considerations & Risks"),
    ("p", "We hold these openly with partners:"),
    ("ul", [
        "Recruiting scarce specialist talent — materially mitigated by the nurse-practitioner "
        "multiplier model, with reliance on a single surgeon reduced as a second is added.",
        "A challenging reimbursement environment and Medicaid funding uncertainty — addressed by "
        "diversifying revenue beyond clinical reimbursement.",
        "Certification is plausible but not automatic — being pursued directly with the relevant "
        "Puerto Rico bodies.",
        "Nurse-practitioner scaling depends on regulatory ratios and sound supervision and "
        "liability protocols.",
        "Capital intensity of the inpatient hub — de-risked by affiliating with or embedding in an "
        "existing Puerto Rico hospital rather than building greenfield.",
        "Coordination across a hybrid clinical model — addressed with shared protocols and order "
        "sets from day one.",
    ]),

    ("h2", "9. Ecosystem & Partners"),
    ("ul", [
        "American Burn Association — verification, ABLS training pathway, and workforce data.",
        "Phoenix Society for Burn Survivors — survivor support and advocacy.",
        "Puerto Rico institutions — the PR Medical Center trauma complex and the VA Caribbean.",
        "Aligned Puerto Rico nonprofits supporting burn-injured children.",
        "Puerto Rico medical schools — toward a long-term burn fellowship pipeline for the wider "
        "Caribbean.",
    ]),

    ("h2", "10. Status & Next Steps"),
    ("p", "This initiative is at the feasibility stage. Immediate next steps:"),
    ("ul", [
        "Finalize the mission and one-page case for support.",
        "Establish the nonprofit arm and begin tax-exempt and child-poverty certification.",
        "Confirm the nurse-practitioner framework with the PR Board of Nursing.",
        "Determine site and structure — a host-hospital embed versus greenfield, and a mainland affiliate.",
        "Size demand and model two-tier unit economics to break-even.",
        "Build the talent plan — surgeon recruitment and an NP upskilling pipeline.",
        "Assemble the funding stack — donor outreach plus disaster-preparedness and grant targets.",
    ]),
]

DISCLAIMER = ("Feasibility-stage public summary. Figures are directional pending primary-data "
              "validation. The Center's charitable arm is being established; charitable listing and "
              "tax-exempt status are pending. Confirm all legal, tax, nursing-regulatory, and "
              "certification specifics with appropriate Puerto Rico counsel before any commitment. "
              "A detailed working brief is shared with partners and funders on request.")

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(os.path.dirname(HERE), "docs")
os.makedirs(DOCS, exist_ok=True)


def write_markdown():
    lines = [f"# {TITLE}", f"## {SUBTITLE}", "", f"*{META}*", ""]
    for kind, val in BLOCKS:
        if kind == "h2":
            lines += ["", f"### {val}", ""]
        elif kind == "p":
            lines += [val, ""]
        elif kind == "ul":
            lines += [f"- {item}" for item in val] + [""]
    lines += ["---", "", f"*{DISCLAIMER}*", ""]
    path = os.path.join(DOCS, "Feasibility-Brief-Public.md")
    with open(path, "w") as f:
        f.write("\n".join(lines))
    return path


def write_pdf():
    from reportlab.lib.pagesizes import LETTER
    from reportlab.lib.units import inch
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib import colors
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                    ListFlowable, ListItem, HRFlowable)

    DEEP = colors.HexColor("#0E3A43")
    TEAL = colors.HexColor("#127C8E")
    MUTED = colors.HexColor("#5C6F77")

    title = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=20,
                           textColor=DEEP, leading=24, spaceAfter=2)
    subtitle = ParagraphStyle("subtitle", fontName="Helvetica-Bold", fontSize=12.5,
                              textColor=TEAL, leading=16, spaceAfter=8)
    meta = ParagraphStyle("meta", fontName="Helvetica-Oblique", fontSize=9,
                          textColor=MUTED, leading=12, spaceAfter=14)
    h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12.5,
                        textColor=DEEP, leading=15, spaceBefore=14, spaceAfter=5)
    body = ParagraphStyle("body", fontName="Helvetica", fontSize=10.2,
                          textColor=colors.HexColor("#22323A"), leading=15,
                          alignment=TA_LEFT, spaceAfter=7)
    bullet = ParagraphStyle("bullet", parent=body, spaceAfter=3)
    disc = ParagraphStyle("disc", fontName="Helvetica-Oblique", fontSize=8.2,
                          textColor=MUTED, leading=11)

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(0.9 * inch, 0.55 * inch,
                          "The Burn Center of the Caribbean  |  Feasibility Brief — Public Summary")
        canvas.drawRightString(LETTER[0] - 0.9 * inch, 0.55 * inch, f"Page {doc.page}")
        canvas.restoreState()

    story = [Paragraph(TITLE, title), Paragraph(SUBTITLE, subtitle), Paragraph(META, meta)]
    for kind, val in BLOCKS:
        if kind == "h2":
            story.append(Paragraph(val, h2))
        elif kind == "p":
            story.append(Paragraph(val, body))
        elif kind == "ul":
            items = [ListItem(Paragraph(i, bullet), leftIndent=10, value="•") for i in val]
            story.append(ListFlowable(items, bulletType="bullet", bulletColor=TEAL,
                                      bulletFontSize=8, leftIndent=14, spaceAfter=8))
    story += [Spacer(1, 12),
              HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#D8E6E6")),
              Spacer(1, 8), Paragraph(DISCLAIMER, disc)]

    path = os.path.join(DOCS, "Feasibility-Brief-Public.pdf")
    doc = SimpleDocTemplate(path, pagesize=LETTER,
                            leftMargin=0.9 * inch, rightMargin=0.9 * inch,
                            topMargin=0.85 * inch, bottomMargin=0.85 * inch,
                            title="Feasibility Brief — Public Summary",
                            author="The Burn Center of the Caribbean")
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    return path


if __name__ == "__main__":
    md = write_markdown()
    pdf = write_pdf()
    print("wrote:", md)
    print("wrote:", pdf)
