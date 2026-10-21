#!/usr/bin/env python3
"""Generate the Master Catalogue PDF from the canonical data store.

Two-pass build: pass 1 records the page of every anchor (parts, families, breakers,
sources); pass 2 renders indexes with page numbers. Output: catalogue/EDH_Master_Catalogue.pdf
"""
import subprocess
from collections import defaultdict
from datetime import date
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (BaseDocTemplate, CondPageBreak, Flowable, Frame, KeepTogether, NextPageTemplate,
                                PageBreak, PageTemplate, Paragraph, Spacer, Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

import illustrations as ill
from common import (CLAIM_FIELDS, CONF_RANK, FIELD_LABELS, MANUFACTURERS, ROOT, best, load_all, norm_pn)

OUT = ROOT / "catalogue" / "EDH_Master_Catalogue.pdf"
NAVY = colors.HexColor("#1b2a3a")
ACCENT = colors.HexColor("#c8691c")
RULE = colors.HexColor("#c9d1d8")
SHADE = colors.HexColor("#f1f4f6")
CONF_COL = {"A": colors.HexColor("#2e7d32"), "B": colors.HexColor("#1565c0"),
            "C": colors.HexColor("#b7791f"), "D": colors.HexColor("#9b2c2c")}
CONF_NAME = {"A": "OEM Verified", "B": "Strongly Corroborated", "C": "Tentative", "D": "Unverified"}
COMPONENT_ORDER = [
    "main-breaker-kit", "main-lug-kit", "sub-feed-lug-kit", "through-feed-lug-kit", "lug-kit", "lug",
    "branch-connector-kit", "breaker-mounting-kit", "connector-strap", "busbar", "bus-assembly",
    "neutral-assembly", "ground-bar", "interior", "mounting-bracket", "mounting-rail", "standoff",
    "insulator", "barrier", "deadfront", "filler-plate", "trim", "box/enclosure", "hardware-kit", "fastener",
    "conversion-kit", "spd-kit", "meter-kit", "breaker-accessory", "handle-lock", "padlock-attachment", "other"]

ss = getSampleStyleSheet()
BASE = ParagraphStyle("base", parent=ss["Normal"], fontName="Helvetica", fontSize=8.2, leading=10.2)
SMALL = ParagraphStyle("small", parent=BASE, fontSize=7, leading=8.6)
TINY = ParagraphStyle("tiny", parent=BASE, fontSize=6.3, leading=7.6, textColor=colors.HexColor("#4a5560"))
BODY = ParagraphStyle("body", parent=BASE, fontSize=9, leading=12, spaceAfter=5)
H1 = ParagraphStyle("h1", parent=BASE, fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=NAVY,
                    spaceAfter=8)
H2 = ParagraphStyle("h2", parent=BASE, fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=NAVY,
                    spaceBefore=8, spaceAfter=5)
H3 = ParagraphStyle("h3", parent=BASE, fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=ACCENT,
                    spaceBefore=6, spaceAfter=3)
CELL = ParagraphStyle("cell", parent=BASE, fontSize=7.4, leading=9)
CELLB = ParagraphStyle("cellb", parent=CELL, fontName="Helvetica-Bold")
HDR = ParagraphStyle("hdr", parent=CELL, fontName="Helvetica-Bold", textColor=colors.white)


def e(s):
    return escape(str(s or ""))


def sid(src_id):
    return "S" + str(int(src_id.split("-")[1]))


class Anchor(Flowable):
    """Zero-size flowable that records its page and sets a PDF destination."""

    def __init__(self, key, pagemap, outline=None, level=0):
        super().__init__()
        self.key, self.pagemap, self.outline, self.level = key, pagemap, outline, level
        self.width = self.height = 0

    def wrap(self, *a):
        return 0, 0

    def draw(self):
        c = self.canv
        self.pagemap[self.key] = c.getPageNumber()
        c.bookmarkPage(self.key)
        if self.outline:
            c.addOutlineEntry(self.outline, self.key, level=self.level, closed=self.level > 0)


class Doc(BaseDocTemplate):
    def __init__(self, path, meta, **kw):
        super().__init__(str(path), pagesize=letter, leftMargin=0.6 * inch, rightMargin=0.6 * inch,
                         topMargin=0.75 * inch, bottomMargin=0.7 * inch, title="EDH Master Catalogue",
                         author="EDH Catalogue Project", subject="Electrical distribution hardware reference", **kw)
        self.meta = meta
        self.section = ""
        fr = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="f")
        self.addPageTemplates([PageTemplate("cover", [fr], onPage=self.cover),
                               PageTemplate("body", [fr], onPageEnd=self.chrome)])

    def beforeDocument(self):
        self.section = ""

    def afterFlowable(self, f):
        if isinstance(f, Paragraph) and getattr(f, "toc_level", None) is not None:
            self.notify("TOCEntry", (f.toc_level, f.getPlainText(), self.page, getattr(f, "toc_key", None)))
            self.section = f.getPlainText() if f.toc_level == 0 else self.section

    def cover(self, c, doc):
        w, h = letter
        c.saveState()
        c.setFillColor(NAVY)
        c.rect(0, h - 4.6 * inch, w, 4.6 * inch, fill=1, stroke=0)
        c.setFillColor(ACCENT)
        c.rect(0, h - 4.75 * inch, w, 0.15 * inch, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica", 11)
        c.drawString(0.8 * inch, h - 1.1 * inch, "TECHNICAL REFERENCE LIBRARY")
        c.setFont("Helvetica-Bold", 30)
        c.drawString(0.8 * inch, h - 1.9 * inch, "Master Electrical Distribution")
        c.drawString(0.8 * inch, h - 2.4 * inch, "Hardware Catalogue")
        c.setFont("Helvetica", 12.5)
        c.drawString(0.8 * inch, h - 3.0 * inch,
                     "Panelboards  ·  Switchboards  ·  Circuit Breakers  ·  Mounting & Connection Hardware")
        c.setFont("Helvetica", 10)
        c.drawString(0.8 * inch, h - 3.5 * inch, "Identification · Compatibility · Supersession · OEM Documentation")
        m = self.meta
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(0.8 * inch, 4.9 * inch, f"Edition {m['version']}")
        c.setFont("Helvetica", 10)
        y = 4.55 * inch
        for line in [f"Generated {m['date']} from database build {m['commit']}",
                     f"{m['parts']} hardware entries  ·  {m['families']} equipment families  ·  "
                     f"{m['breakers']} breaker families  ·  {m['sources']} sources"]:
            c.drawString(0.8 * inch, y, line)
            y -= 0.25 * inch
        c.setFont("Helvetica-Bold", 9)
        c.drawString(0.8 * inch, 2.6 * inch, "Manufacturer lineages covered")
        c.setFont("Helvetica", 8.5)
        y = 2.38 * inch
        for code in m["mfrs"]:
            c.drawString(0.8 * inch, y, f"{code}  —  {MANUFACTURERS[code][1]}")
            y -= 0.18 * inch
        c.setFont("Helvetica-Oblique", 7.5)
        c.setFillColor(colors.HexColor("#5a6875"))
        c.drawString(0.8 * inch, 0.7 * inch, "Independent research reference. Not affiliated with or endorsed by any "
                     "manufacturer named. Trademarks belong to their owners.")
        c.drawString(0.8 * inch, 0.55 * inch, "Compatibility statements carry evidence classes A–D; only class A is "
                     "manufacturer-documented. Verify before installation.")
        c.restoreState()

    def chrome(self, c, doc):
        w, h = letter
        c.saveState()
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.2)
        c.line(self.leftMargin, h - 0.55 * inch, w - self.rightMargin, h - 0.55 * inch)
        c.setFont("Helvetica-Bold", 7.5)
        c.setFillColor(NAVY)
        c.drawString(self.leftMargin, h - 0.5 * inch, "EDH MASTER CATALOGUE")
        c.setFont("Helvetica", 7.5)
        c.drawRightString(w - self.rightMargin, h - 0.5 * inch, self.section[:90])
        c.setStrokeColor(RULE)
        c.setLineWidth(0.5)
        c.line(self.leftMargin, 0.55 * inch, w - self.rightMargin, 0.55 * inch)
        c.setFont("Helvetica", 7)
        c.setFillColor(colors.HexColor("#4a5560"))
        c.drawString(self.leftMargin, 0.4 * inch,
                     f"Edition {self.meta['version']} · {self.meta['date']} · Evidence: A OEM verified · "
                     "B corroborated · C tentative · D unverified")
        c.drawRightString(w - self.rightMargin, 0.4 * inch, f"Page {c.getPageNumber()}")
        c.restoreState()


def heading(text, style, level, key=None, pagemap=None):
    out = []
    if key and pagemap is not None:
        out.append(Anchor(key, pagemap, outline=text, level=level))
    p = Paragraph(e(text), style)
    p.toc_level = level
    p.toc_key = key
    out.append(p)
    return out


def tbl(rows, widths, header=True, zebra=True, font=None):
    t = Table(rows, colWidths=widths, repeatRows=1 if header else 0)
    st = [("GRID", (0, 0), (-1, -1), 0.35, RULE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
          ("TOPPADDING", (0, 0), (-1, -1), 1.8), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.8)]
    if header:
        st += [("BACKGROUND", (0, 0), (-1, 0), NAVY)]
    if zebra:
        for i in range(1 if header else 0, len(rows)):
            if i % 2 == 0:
                st.append(("BACKGROUND", (0, i), (-1, i), SHADE))
    t.setStyle(TableStyle(st))
    return t


def P(text, style=CELL):
    return Paragraph(text, style)


def badge(conf):
    col = CONF_COL.get(conf, colors.grey).hexval()[2:]
    return f'<font color="#{col}"><b>{conf}</b></font>'


class Catalogue:
    def __init__(self, data, pagemap):
        self.d = data
        self.pm = pagemap
        self.fams = {f["id"]: f for f in data["families"]}
        self.brks = {b["id"]: b for b in data["breakers"]}
        self.parts = {p["id"]: p for p in data["parts"]}
        self.srcs = {s["id"]: s for s in data["sources"]}
        self.primary_family = {}
        for p in data["parts"]:
            self.primary_family[p["id"]] = p["family_ids"][0] if p["family_ids"] else None

    # ---------- link helpers
    def pg(self, key):
        n = self.pm.get(key)
        return str(n) if n else "—"

    def link(self, key, text):
        return f'<a href="#{key}" color="#1b2a3a">{e(text)}</a>'

    def fam_label(self, fid):
        f = self.fams.get(fid)
        if not f:
            return fid
        return f.get("code") or f["name"]

    def src_refs(self, ids):
        return ", ".join(self.link(i, sid(i)) for i in ids if i in self.srcs)

    # ---------- front matter
    def front(self, story, meta):
        story += [NextPageTemplate("body"), PageBreak()]
        story += heading("Document Control", H1, 0, "doc-control", self.pm)
        rows = [[P("Item", HDR), P("Value", HDR)],
                [P("Edition"), P(e(meta["version"]))], [P("Generated"), P(e(meta["date"]))],
                [P("Database build (git)"), P(e(meta["commit"]))],
                [P("Hardware entries"), P(str(meta["parts"]))], [P("Equipment families"), P(str(meta["families"]))],
                [P("Breaker families"), P(str(meta["breakers"]))], [P("Sources registered"), P(str(meta["sources"]))],
                [P("Documents preserved in library"), P(str(meta["docs"]))],
                [P("Open research leads"), P(str(meta["leads"]))]]
        story.append(tbl(rows, [2.2 * inch, 4.8 * inch]))
        story.append(Spacer(1, 10))
        story.append(Paragraph("Revision history (research batches merged)", H3))
        rows = [[P("Batch", HDR), P("Research date", HDR), P("Merged", HDR), P("New parts", HDR),
                 P("Updated", HDR), P("New sources", HDR)]]
        for b in self.d["meta"].get("batches", []):
            s = b.get("stats", {})
            rows.append([P(e(b["batch_id"])), P(e(b.get("date"))), P(e(b.get("merged"))),
                         P(str(s.get("parts_new", ""))), P(str(s.get("parts_updated", ""))),
                         P(str(s.get("sources_new", "")))])
        story.append(tbl(rows, [2.4 * inch, 0.9 * inch, 0.9 * inch, 0.8 * inch, 0.8 * inch, 0.9 * inch]))
        story.append(Spacer(1, 10))
        story.append(Paragraph(
            "This catalogue is generated automatically from the structured parts database "
            "(<i>data/</i> → <i>build/edh_catalogue.sqlite</i>). Corrections must be made in the database, never "
            "in this PDF. Catalogue identifiers (EDH-…, FAM-…, BRK-…, SRC-…) are permanent and are never reused.",
            BODY))
        story.append(PageBreak())
        toc = TableOfContents()
        toc.levelStyles = [
            ParagraphStyle("t0", parent=BASE, fontName="Helvetica-Bold", fontSize=9.5, leading=13, leftIndent=0),
            ParagraphStyle("t1", parent=BASE, fontSize=8.3, leading=10.5, leftIndent=14),
            ParagraphStyle("t2", parent=BASE, fontSize=7.6, leading=9.5, leftIndent=28,
                           textColor=colors.HexColor("#3b4652"))]
        story += [Paragraph("Table of Contents", H1), toc, PageBreak()]

    def how_to_use(self, story):
        story += heading("1  How to Use This Catalogue", H1, 0, "sec-howto", self.pm)
        txt = [
            "The catalogue is organised by <b>manufacturer lineage</b>, then <b>equipment family</b> "
            "(panelboard, switchboard or loadcenter series), then <b>component type</b>. Every hardware item has a "
            "permanent catalogue identifier of the form <b>EDH-&lt;MFR&gt;-nnnnn</b>.",
            "<b>To identify an unknown part:</b> (1) establish the manufacturer and equipment family from the "
            "enclosure nameplate, interior label or breaker type; (2) use Section 2 to decide the component type "
            "from its function and mounting style; (3) look up any stamped number in the Part-Number Index "
            "(partial numbers are listed in normalised alphanumeric order); (4) if no number is legible, use the "
            "Breaker Compatibility Index and the identification-feature table to narrow candidates, then compare "
            "dimensions and hole patterns against the part entry.",
            "<b>Claims, not records, carry confidence.</b> Each line in a part entry shows the evidence class of "
            "that specific statement and the sources supporting it (S-numbers link to the Source Register in "
            "Appendix B). A part may have an OEM-verified part number (A) and only a tentative breaker "
            "compatibility (C).",
        ]
        story += [Paragraph(t, BODY) for t in txt]
        rows = [[P("Class", HDR), P("Meaning", HDR), P("Typical evidence", HDR)],
                [P(badge("A")), P("<b>OEM Verified</b>"), P("Explicitly documented in a manufacturer catalogue, "
                                                             "instruction leaflet, drawing or bulletin (page cited).")],
                [P(badge("B")), P("<b>Strongly Corroborated</b>"), P("Multiple independent credible sources agree "
                                                                      "(e.g. two distributors plus a photo of the label).")],
                [P(badge("C")), P("<b>Tentative</b>"), P("Single non-OEM source, or plausible but incomplete evidence. "
                                                          "Distributor compatibility claims are never above C on their own.")],
                [P(badge("D")), P("<b>Unverified</b>"), P("Lead, hearsay or inference requiring investigation.")]]
        story.append(tbl(rows, [0.6 * inch, 1.6 * inch, 4.8 * inch]))
        story.append(Spacer(1, 8))
        story.append(Paragraph("Evidence basis codes", H3))
        rows = [[P("Code", HDR), P("Meaning", HDR)]] + [[P(k), P(v)] for k, v in [
            ("oem_spec", "Manufacturer specification text or table"), ("oem_drawing", "Manufacturer drawing"),
            ("distributor", "Distributor catalogue / listing"), ("surplus_listing", "Surplus / used-equipment listing"),
            ("photo", "Photograph of an actual part or label"),
            ("field_measurement", "Measured from a physical sample (record instrument and date)"),
            ("inference", "Engineering inference — never sufficient for compatibility")]]
        story.append(tbl(rows, [1.4 * inch, 5.6 * inch]))
        story.append(Spacer(1, 8))
        story.append(Paragraph("Safety and interchangeability notice", H3))
        story.append(Paragraph(
            "Matching dimensions do not establish electrical interchangeability. Panelboard and switchboard "
            "assemblies are listed as systems; substituting non-OEM or cross-manufacturer components may void the "
            "listing and short-circuit rating. Nothing in this catalogue states that a reproduced or aftermarket "
            "part is approved, listed or electrically equivalent unless an explicit, cited source says so. "
            "Distinguish OEM specifications from field measurements and manufacturing assumptions at all times.",
            BODY))
        story.append(PageBreak())

    def ident_guide(self, story):
        story += heading("2  Hardware Identification Guide", H1, 0, "sec-ident", self.pm)
        story.append(Paragraph(
            "The drawings in this section are generic schematics prepared for this catalogue to illustrate "
            "terminology and measurement practice. They are not reproductions of manufacturer drawings and do not "
            "depict any specific OEM part.", BODY))
        for title, fig, cap in [
            ("2.1  Anatomy of a panelboard interior", ill.panel_interior(), "Figure 2-1. Generic panelboard interior "
             "showing where each component type installs."),
            ("2.2  Breaker mounting styles", ill.mounting_styles(), "Figure 2-2. Bolt-on, plug-on and "
             "panel/switchboard plug-on unit mounting."),
            ("2.3  Branch connector straps — what to measure", ill.connector_strap(), "Figure 2-3. Measurement "
             "practice for connector straps and bus links."),
            ("2.4  Terminal lug types", ill.lug_types(), "Figure 2-4. Common lug constructions found in main, "
             "sub-feed and feed-through lug kits.")]:
            story.append(KeepTogether(heading(title, H2, 1, None) + [fig, Paragraph(cap, TINY), Spacer(1, 6)]))
        story.append(Paragraph("2.5  Component-type key", H2))
        counts = defaultdict(int)
        for p in self.d["parts"]:
            counts[p["component_type"]] += 1
        desc = {
            "main-breaker-kit": "Converts a main-lug interior to main-breaker; includes breaker mounting, connectors to bus.",
            "main-lug-kit": "Incoming-cable lugs bolted to bus top/bottom; ampere rating set by lug and bus.",
            "sub-feed-lug-kit": "Second set of lugs to feed a downstream panel from the same bus.",
            "through-feed-lug-kit": "Lugs at opposite bus end for feeding through to another panel.",
            "branch-connector-kit": "Straps/connectors joining branch breakers to phase bus; series-specific.",
            "breaker-mounting-kit": "Hardware to mount a breaker frame in a panel/switchboard space.",
            "connector-strap": "Individual copper/aluminium link between bus and device terminal.",
            "filler-plate": "Closes unused breaker space in the deadfront.",
            "neutral-assembly": "Neutral bar/lug assembly, incl. 200% neutral options.",
            "ground-bar": "Equipment grounding bar kit.",
            "deadfront": "Inner cover exposing only breaker handles.",
            "trim": "Front cover/door assembly (surface or flush).",
            "insulator": "Insulating support or standoff for bus or connectors.",
            "barrier": "Insulating barrier between phases or sections.",
            "conversion-kit": "Adapts later breakers or interiors into legacy equipment.",
            "spd-kit": "Surge-protective-device mounting/connection kit.",
            "lug-kit": "Lug sets for breakers or assemblies.",
        }
        rows = [[P("Component type", HDR), P("Function / recognition", HDR), P("Entries", HDR)]]
        for ct in COMPONENT_ORDER:
            if counts.get(ct) or ct in desc:
                rows.append([P(f"<b>{e(ct)}</b>"), P(e(desc.get(ct, ""))), P(str(counts.get(ct, 0)))])
        story.append(tbl(rows, [1.6 * inch, 4.8 * inch, 0.6 * inch]))
        idf = [p for p in self.d["parts"] if p["claims"].get("id_features")]
        if idf:
            story.append(Paragraph("2.6  Identification by physical feature", H2))
            story.append(Paragraph("Parts for which distinguishing physical features are recorded. Use with the "
                                   "dimensions and hole-pattern fields of the entry.", BODY))
            rows = [[P("Catalogue ID", HDR), P("OEM PN", HDR), P("Features", HDR), P("Pg", HDR)]]
            for p in sorted(idf, key=lambda x: (x["mfr"], x["component_type"], x["oem_part_number"])):
                c = best(p["claims"]["id_features"])
                rows.append([P(self.link(p["id"], p["id"])), P(e(p["oem_part_number"])),
                             P(f"{e(c['value'])} {badge(c['conf'])}"), P(self.pg(p["id"]))])
            story.append(tbl(rows, [1.15 * inch, 1.2 * inch, 4.25 * inch, 0.4 * inch]))
        story.append(PageBreak())

    # ---------- manufacturer sections
    def mfr_sections(self, story, start_no):
        no = start_no
        by_mfr = defaultdict(list)
        for f in self.d["families"]:
            by_mfr[f["mfr"]].append(f)
        parts_by_mfr = defaultdict(list)
        for p in self.d["parts"]:
            parts_by_mfr[p["mfr"]].append(p)
        for code in MANUFACTURERS:
            if not by_mfr.get(code) and not parts_by_mfr.get(code):
                continue
            name, lineage = MANUFACTURERS[code]
            story += heading(f"{no}  {name}", H1, 0, f"mfr-{code}", self.pm)
            story.append(Paragraph(f"<b>Lineage / brand markings:</b> {e(lineage)}", BODY))
            fams = sorted(by_mfr.get(code, []), key=lambda f: (f["equipment_type"], f.get("code") or f["name"]))
            rows = [[P("Family", HDR), P("Type", HDR), P("Status", HDR), P("Era", HDR), P("Entries", HDR), P("Pg", HDR)]]
            for f in fams:
                n = sum(1 for p in parts_by_mfr[code] if f["id"] in p["family_ids"])
                st, era = best(f["claims"].get("status")), best(f["claims"].get("era"))
                rows.append([P(self.link(f["id"], f"{f.get('code') or ''} {f['name']}".strip())),
                             P(e(f["equipment_type"])), P(e(st["value"]) if st else "unknown"),
                             P(e(era["value"]) if era else "—"), P(str(n)), P(self.pg(f["id"]))])
            story.append(tbl(rows, [2.4 * inch, 0.9 * inch, 1.3 * inch, 1.5 * inch, 0.5 * inch, 0.4 * inch]))
            sub = 1
            for f in fams:
                self.family_sheet(story, f, f"{no}.{sub}", parts_by_mfr[code])
                sub += 1
            orphans = [p for p in parts_by_mfr[code] if not p["family_ids"]]
            if orphans:
                story += heading(f"{no}.{sub}  General / family not yet assigned", H2, 1, f"mfr-{code}-gen", self.pm)
                self.part_group(story, orphans)
            story.append(PageBreak())
            no += 1
        return no

    def claims_table(self, claims, fields):
        rows = []
        for fld in fields:
            lst = claims.get(fld) or []
            for i, c in enumerate(lst):
                lab = FIELD_LABELS.get(fld, fld) if i == 0 else ""
                extra = []
                if c.get("relation"):
                    extra.append(c["relation"])
                if c.get("page"):
                    extra.append(e(c["page"]))
                if c.get("basis"):
                    extra.append(e(c["basis"]))
                note = f' <font size="6.3" color="#5a6875">({e(c["note"])})</font>' if c.get("note") else ""
                rows.append([P(f"<b>{e(lab)}</b>" if lab else ""), P(e(c["value"]) + note), P(badge(c["conf"])),
                             P(self.src_refs(c["src"]) + (f'<br/><font size="6" color="#5a6875">{"; ".join(extra)}</font>'
                                                          if extra else ""), TINY)])
        return rows

    def family_sheet(self, story, f, num, mparts):
        story.append(CondPageBreak(2.5 * inch))
        title = f"{num}  {(f.get('code') + ' — ') if f.get('code') and f.get('code') != f['name'] else ''}{f['name']}"
        story += heading(title, H2, 1, f["id"], self.pm)
        meta = [f"<b>{e(f['id'])}</b>", e(f["equipment_type"])]
        if f.get("aliases"):
            meta.append("aka " + e(", ".join(f["aliases"])))
        if f.get("brand_markings"):
            meta.append("markings: " + e(", ".join(f["brand_markings"])))
        story.append(Paragraph(" · ".join(meta), SMALL))
        for o in [f.get("overview")] + f.get("overview_notes", []):
            if o:
                story.append(Paragraph(e(o), BODY))
        fields = ["status", "era", "successor", "voltage_rating", "main_ampacity", "branch_breakers"] + \
                 [k for k in f["claims"] if k not in ("status", "era", "successor", "voltage_rating", "main_ampacity",
                                                       "branch_breakers")]
        rows = self.claims_table(f["claims"], fields)
        if rows:
            story.append(tbl([[P("Attribute", HDR), P("Value", HDR), P("Cl.", HDR), P("Sources", HDR)]] + rows,
                             [1.4 * inch, 4.3 * inch, 0.35 * inch, 0.95 * inch]))
        brks = [b for b in self.d["breakers"] if f["id"] in b["family_ids"]]
        if brks:
            story.append(Paragraph("<b>Breaker families associated:</b> " + ", ".join(
                self.link(b["id"], b["name"]) for b in sorted(brks, key=lambda b: b["name"])), SMALL))
        docs = sorted(set(f.get("source_ids", [])) | {s for lst in f["claims"].values() for c in lst for s in c["src"]})
        if docs:
            story.append(Paragraph("<b>Key documents:</b> " + "; ".join(
                f"{self.link(s, sid(s))} {e(self.srcs[s].get('doc_number') or '')} {e(self.srcs[s].get('title', ''))[:90]}"
                for s in docs if s in self.srcs), TINY))
        own = [p for p in mparts if self.primary_family.get(p["id"]) == f["id"]]
        other = [p for p in mparts if f["id"] in p["family_ids"] and self.primary_family.get(p["id"]) != f["id"]]
        if other:
            story.append(Paragraph("<b>Also fits this family (entry printed elsewhere):</b> " + ", ".join(
                f"{self.link(p['id'], p['oem_part_number'] or p['id'])} (p.{self.pg(p['id'])})" for p in other), TINY))
        if own:
            self.part_group(story, own)

    def part_group(self, story, parts):
        groups = defaultdict(list)
        for p in parts:
            groups[p["component_type"]].append(p)
        order = [c for c in COMPONENT_ORDER if c in groups] + sorted(c for c in groups if c not in COMPONENT_ORDER)
        for ct in order:
            story.append(Paragraph(ct.replace("-", " ").title(), H3))
            # compact summary table
            rows = [[P("Catalogue ID", HDR), P("OEM part no.", HDR), P("Description", HDR), P("Breakers", HDR),
                     P("Status", HDR)]]
            for p in sorted(groups[ct], key=lambda x: norm_pn(x["oem_part_number"])):
                bc, st = best(p["claims"].get("breaker_compat")), best(p["claims"].get("status"))
                rows.append([P(self.link(p["id"], p["id"])), P(f"<b>{e(p['oem_part_number'])}</b>"),
                             P(e(p["title"])), P(e(bc["value"][:70]) + " " + badge(bc["conf"]) if bc else "—"),
                             P(e(st["value"]) if st else "unknown")])
            story.append(tbl(rows, [1.05 * inch, 1.15 * inch, 2.6 * inch, 1.45 * inch, 0.75 * inch]))
            story.append(Spacer(1, 4))
            for p in sorted(groups[ct], key=lambda x: norm_pn(x["oem_part_number"])):
                story.append(self.part_entry(p))

    def part_entry(self, p):
        out = [Anchor(p["id"], self.pm)]
        st = best(p["claims"].get("status"))
        head = Table([[P(f'<font color="white"><b>{e(p["id"])}</b></font>', CELL),
                       P(f'<font color="white" size="10"><b>{e(p["oem_part_number"] or "(no OEM number)")}</b></font>', CELL),
                       P(f'<font color="white">{e(p.get("brand_marking") or MANUFACTURERS[p["mfr"]][0])}</font>', CELL),
                       P(f'<font color="white">{e(p["component_type"])}</font>', CELL),
                       P(f'<font color="white"><b>{e(st["value"].upper()[:22]) if st else "STATUS UNKNOWN"}</b></font>', CELL)]],
                     colWidths=[1.1 * inch, 2.0 * inch, 1.5 * inch, 1.4 * inch, 1.0 * inch])
        head.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY), ("BACKGROUND", (-1, 0), (-1, 0), ACCENT),
                                  ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 2.5),
                                  ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5)]))
        out.append(head)
        out.append(Paragraph(f"<b>{e(p['title'])}</b>", SMALL))
        fields = [f for f in CLAIM_FIELDS if f != "oem_part_number"]
        rows = self.claims_table(p["claims"], ["oem_part_number"] + fields)
        extra = [k for k in p["claims"] if k not in CLAIM_FIELDS]
        rows += self.claims_table(p["claims"], extra)
        fits = []
        if p["family_ids"]:
            fits.append("Families: " + ", ".join(self.link(x, self.fam_label(x)) for x in p["family_ids"]))
        if p["breaker_ids"]:
            fits.append("Breakers: " + ", ".join(self.link(x, self.brks[x]["name"]) for x in p["breaker_ids"]
                                                 if x in self.brks))
        if fits:
            rows.append([P("<b>Cross-links</b>"), P(" · ".join(fits)), P(""), P("")])
        if p.get("requires"):
            rows.append([P("<b>Requires</b>"), P(", ".join(
                f"{self.link(r, (self.parts[r]['oem_part_number'] or r))} ({r})" for r in p["requires"]
                if r in self.parts)), P(""), P("")])
        if p.get("unknowns"):
            rows.append([P("<b>Not yet documented</b>"),
                         P(f'<font color="#9b2c2c">{e(", ".join(FIELD_LABELS.get(u, u) for u in p["unknowns"]))}</font>'),
                         P(""), P("")])
        for q in p.get("questions", []):
            rows.append([P("<b>Open question</b>"), P(f"<i>{e(q)}</i>"), P(""), P("")])
        t = Table(rows or [[P("No claims recorded")]], colWidths=[1.4 * inch, 4.3 * inch, 0.35 * inch, 0.95 * inch])
        t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.3, RULE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                               ("TOPPADDING", (0, 0), (-1, -1), 1.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
                               ("LEFTPADDING", (0, 0), (-1, -1), 3), ("BACKGROUND", (0, 0), (0, -1), SHADE)]))
        out.append(t)
        out.append(Spacer(1, 7))
        return KeepTogether(out) if len(rows) < 16 else _Group(out)

    # ---------- registers & indexes
    def breaker_register(self, story, no):
        story += heading(f"{no}  Breaker Family Register", H1, 0, "sec-breakers", self.pm)
        story.append(Paragraph("Breaker families referenced by the hardware entries. Mounting style and frame "
                               "determine which connector and mounting kits apply.", BODY))
        for b in sorted(self.d["breakers"], key=lambda x: (x["mfr"], x["name"])):
            blk = [Anchor(b["id"], self.pm),
                   Paragraph(f"<b>{e(b['name'])}</b>  <font size='7' color='#5a6875'>{e(b['id'])} · "
                             f"{e(MANUFACTURERS[b['mfr']][0])}{(' · aka ' + e(', '.join(b['aliases']))) if b.get('aliases') else ''}"
                             "</font>", H3)]
            rows = self.claims_table(b["claims"], ["mounting", "frame", "poles", "amps", "voltage", "interrupting",
                                                   "status"] + [k for k in b["claims"] if k not in (
                "mounting", "frame", "poles", "amps", "voltage", "interrupting", "status")])
            if b["family_ids"]:
                rows.append([P("<b>Used in</b>"), P(", ".join(self.link(f, self.fam_label(f)) for f in b["family_ids"])),
                             P(""), P("")])
            if rows:
                t = Table(rows, colWidths=[1.4 * inch, 4.3 * inch, 0.35 * inch, 0.95 * inch])
                t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.3, RULE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                                       ("BACKGROUND", (0, 0), (0, -1), SHADE)]))
                blk.append(t)
            story.append(KeepTogether(blk))
        story.append(PageBreak())

    def crossref(self, story, no):
        story += heading(f"{no}  Cross-Reference Tables", H1, 0, "sec-xref", self.pm)
        story += heading(f"{no}.1  Supersession and alternate numbers", H2, 1, "xref-super", self.pm)
        rows = [[P("Number", HDR), P("Relation", HDR), P("Primary OEM PN", HDR), P("Catalogue ID", HDR),
                 P("Cl.", HDR), P("Pg", HDR)]]
        items = []
        for p in self.d["parts"]:
            for c in p["claims"].get("alt_part_numbers", []):
                items.append((norm_pn(c["value"]), c, p))
        for _, c, p in sorted(items, key=lambda x: x[0]):
            rows.append([P(f"<b>{e(c['value'])}</b>"), P(e(c.get("relation", "alternate"))), P(e(p["oem_part_number"])),
                         P(self.link(p["id"], p["id"])), P(badge(c["conf"])), P(self.pg(p["id"]))])
        story.append(tbl(rows, [1.7 * inch, 1.2 * inch, 1.7 * inch, 1.3 * inch, 0.4 * inch, 0.5 * inch]) if items
                     else Paragraph("No alternate numbers recorded yet.", BODY))
        story += heading(f"{no}.2  Replacement and successor statements", H2, 1, "xref-repl", self.pm)
        rows = [[P("Catalogue ID", HDR), P("OEM PN", HDR), P("Replacement / successor", HDR), P("Cl.", HDR)]]
        n = 0
        for p in sorted(self.d["parts"], key=lambda x: (x["mfr"], norm_pn(x["oem_part_number"]))):
            for c in p["claims"].get("replacement", []):
                rows.append([P(self.link(p["id"], p["id"])), P(e(p["oem_part_number"])), P(e(c["value"])),
                             P(badge(c["conf"]))])
                n += 1
        story.append(tbl(rows, [1.2 * inch, 1.4 * inch, 4.0 * inch, 0.4 * inch]) if n
                     else Paragraph("No replacement statements recorded yet.", BODY))
        story += heading(f"{no}.3  Companion parts required for installation", H2, 1, "xref-req", self.pm)
        rows = [[P("Part", HDR), P("Requires", HDR)]]
        for p in self.d["parts"]:
            if p.get("requires"):
                rows.append([P(f"{self.link(p['id'], p['oem_part_number'] or p['id'])} ({e(p['id'])})"),
                             P(", ".join(f"{self.link(r, self.parts[r]['oem_part_number'] or r)}"
                                         for r in p["requires"] if r in self.parts))])
        story.append(tbl(rows, [3 * inch, 4 * inch]) if len(rows) > 1 else Paragraph("None recorded yet.", BODY))
        story.append(PageBreak())

    def indexes(self, story, no):
        story += heading(f"{no}  Indexes", H1, 0, "sec-index", self.pm)
        # manufacturer index
        story += heading(f"{no}.1  Manufacturer index", H2, 1, "idx-mfr", self.pm)
        rows = [[P("Code", HDR), P("Lineage", HDR), P("Brand markings", HDR), P("Families", HDR), P("Parts", HDR),
                 P("Pg", HDR)]]
        for code, (name, lineage) in MANUFACTURERS.items():
            nf = sum(1 for f in self.d["families"] if f["mfr"] == code)
            np_ = sum(1 for p in self.d["parts"] if p["mfr"] == code)
            if nf or np_:
                rows.append([P(f"<b>{code}</b>"), P(self.link(f"mfr-{code}", name)), P(e(lineage)), P(str(nf)),
                             P(str(np_)), P(self.pg(f"mfr-{code}"))])
        story.append(tbl(rows, [0.5 * inch, 1.7 * inch, 3.3 * inch, 0.6 * inch, 0.5 * inch, 0.4 * inch]))
        # family index (incl. aliases)
        story += heading(f"{no}.2  Equipment family index (including aliases)", H2, 1, "idx-fam", self.pm)
        items = []
        for f in self.d["families"]:
            for nm in {f.get("code"), f["name"], *f.get("aliases", [])}:
                if nm:
                    items.append((nm.upper(), nm, f))
        rows = [[P("Name / alias", HDR), P("Family", HDR), P("Mfr", HDR), P("Type", HDR), P("ID", HDR), P("Pg", HDR)]]
        for _, nm, f in sorted(items, key=lambda x: x[0]):
            rows.append([P(f"<b>{e(nm)}</b>"), P(self.link(f["id"], f["name"])), P(f["mfr"]), P(e(f["equipment_type"])),
                         P(e(f["id"])), P(self.pg(f["id"]))])
        story.append(tbl(rows, [1.6 * inch, 2.4 * inch, 0.5 * inch, 0.9 * inch, 1.1 * inch, 0.5 * inch]))
        # part-number index
        story += heading(f"{no}.3  Part-number index (primary and alternate numbers)", H2, 1, "idx-pn", self.pm)
        story.append(Paragraph("Sorted by normalised number (punctuation and spaces removed). Search a partial "
                               "number by its leading characters.", SMALL))
        items = []
        for p in self.d["parts"]:
            if p["oem_part_number"]:
                items.append((norm_pn(p["oem_part_number"]), p["oem_part_number"], "primary", p))
            for c in p["claims"].get("alt_part_numbers", []):
                items.append((norm_pn(c["value"]), c["value"], c.get("relation", "alternate"), p))
        rows = [[P("Number", HDR), P("Type", HDR), P("Mfr", HDR), P("Description", HDR), P("Catalogue ID", HDR),
                 P("Pg", HDR)]]
        for _, pn, rel, p in sorted(items, key=lambda x: x[0]):
            rows.append([P(f"<b>{e(pn)}</b>"), P(e(rel)), P(p["mfr"]), P(e(p["title"][:80])),
                         P(self.link(p["id"], p["id"])), P(self.pg(p["id"]))])
        story.append(tbl(rows, [1.35 * inch, 0.8 * inch, 0.4 * inch, 2.95 * inch, 1.05 * inch, 0.45 * inch]))
        # breaker compatibility index
        story += heading(f"{no}.4  Breaker compatibility index", H2, 1, "idx-brk", self.pm)
        story.append(Paragraph("Parts linked to each breaker family. The confidence shown is that of the part's "
                               "breaker-compatibility claim.", SMALL))
        rows = [[P("Breaker family", HDR), P("Part", HDR), P("Component", HDR), P("Equipment family", HDR),
                 P("Cl.", HDR), P("Pg", HDR)]]
        for b in sorted(self.d["breakers"], key=lambda x: (x["name"], x["mfr"])):
            linked = [p for p in self.d["parts"] if b["id"] in p["breaker_ids"]]
            for p in sorted(linked, key=lambda x: norm_pn(x["oem_part_number"])):
                bc = best(p["claims"].get("breaker_compat"))
                rows.append([P(f"<b>{self.link(b['id'], b['name'])}</b> ({b['mfr']})"),
                             P(self.link(p["id"], p["oem_part_number"] or p["id"])), P(e(p["component_type"])),
                             P(e(", ".join(self.fam_label(f) for f in p["family_ids"]))),
                             P(badge(bc["conf"]) if bc else "—"), P(self.pg(p["id"]))])
        story.append(tbl(rows, [1.5 * inch, 1.4 * inch, 1.3 * inch, 1.9 * inch, 0.4 * inch, 0.5 * inch]))
        # component type index
        story += heading(f"{no}.5  Component-type index", H2, 1, "idx-ct", self.pm)
        rows = [[P("Component type", HDR), P("Parts (OEM PN → page)", HDR)]]
        groups = defaultdict(list)
        for p in self.d["parts"]:
            groups[p["component_type"]].append(p)
        for ct in [c for c in COMPONENT_ORDER if c in groups] + sorted(c for c in groups if c not in COMPONENT_ORDER):
            rows.append([P(f"<b>{e(ct)}</b>"), P(", ".join(
                f"{self.link(p['id'], p['oem_part_number'] or p['id'])} ({p['mfr']}, {self.pg(p['id'])})"
                for p in sorted(groups[ct], key=lambda x: (x["mfr"], norm_pn(x["oem_part_number"])))))])
        story.append(tbl(rows, [1.5 * inch, 5.5 * inch]))
        # ampere / poles quick index
        story += heading(f"{no}.6  Rating and pole index", H2, 1, "idx-rating", self.pm)
        rows = [[P("Catalogue ID", HDR), P("OEM PN", HDR), P("Current rating", HDR), P("Poles", HDR),
                 P("Voltage", HDR), P("Pg", HDR)]]
        for p in sorted(self.d["parts"], key=lambda x: (x["mfr"], norm_pn(x["oem_part_number"]))):
            a, po, v = (best(p["claims"].get(k)) for k in ("ampacity", "poles", "voltage"))
            if a or po:
                rows.append([P(self.link(p["id"], p["id"])), P(e(p["oem_part_number"])),
                             P(e(a["value"]) if a else "—"), P(e(po["value"]) if po else "—"),
                             P(e(v["value"]) if v else "—"), P(self.pg(p["id"]))])
        story.append(tbl(rows, [1.1 * inch, 1.3 * inch, 2.0 * inch, 0.8 * inch, 1.3 * inch, 0.5 * inch]))
        # dimensions / hole pattern index
        dims = [p for p in self.d["parts"] if p["claims"].get("dimensions") or p["claims"].get("hole_pattern")]
        story += heading(f"{no}.7  Physical dimension and hole-pattern index", H2, 1, "idx-dim", self.pm)
        if dims:
            rows = [[P("Catalogue ID", HDR), P("OEM PN", HDR), P("Dimensions", HDR), P("Hole pattern", HDR), P("Pg", HDR)]]
            for p in dims:
                dm, hp = best(p["claims"].get("dimensions")), best(p["claims"].get("hole_pattern"))
                rows.append([P(self.link(p["id"], p["id"])), P(e(p["oem_part_number"])),
                             P((e(dm["value"]) + " " + badge(dm["conf"])) if dm else "—"),
                             P((e(hp["value"]) + " " + badge(hp["conf"])) if hp else "—"), P(self.pg(p["id"]))])
            story.append(tbl(rows, [1.1 * inch, 1.2 * inch, 2.4 * inch, 1.9 * inch, 0.4 * inch]))
        else:
            story.append(Paragraph("No dimensional data recorded yet. Dimensions are a principal research gap; "
                                   "field measurements of physical samples should be added as class C/A evidence "
                                   "with basis 'field_measurement'.", BODY))
        story.append(PageBreak())

    def appendix_docs(self, story):
        story += heading("Appendix A  Documentation Library", H1, 0, "app-docs", self.pm)
        story.append(Paragraph(
            "OEM and supporting documents, grouped by manufacturer lineage and document type. 'Local' identifies "
            "documents preserved in docs/library/ (see docs/DOCUMENT_INDEX.csv for checksums). Documents not "
            "preserved are cited by URL; inaccessible documents are listed as research leads.", BODY))
        linked = defaultdict(set)
        for p in self.d["parts"]:
            for lst in p["claims"].values():
                for c in lst:
                    for s in c["src"]:
                        linked[s].add(p["id"])
            for s in p.get("source_ids", []):
                linked[s].add(p["id"])
        by_mfr = defaultdict(list)
        for s in self.d["sources"]:
            if s.get("type", "").startswith("oem") or s.get("local_file"):
                by_mfr[s.get("mfr", "OTH")].append(s)
        for code in MANUFACTURERS:
            if not by_mfr.get(code):
                continue
            story.append(Paragraph(MANUFACTURERS[code][0], H2))
            rows = [[P("Ref", HDR), P("Doc no.", HDR), P("Title / date", HDR), P("Type", HDR), P("Avail.", HDR),
                     P("Entries", HDR)]]
            for s in sorted(by_mfr[code], key=lambda s: (s.get("type", ""), s.get("doc_number") or "~")):
                avail = "Local" if s.get("local_file") else (s.get("access_status") or "link")
                rows.append([P(self.link(s["id"], sid(s["id"]))), P(e(s.get("doc_number", ""))),
                             P(f"{e(s.get('title', ''))}<br/><font size='6' color='#5a6875'>{e(s.get('date', ''))}</font>"),
                             P(e(s.get("type", "").replace("oem_", ""))), P(e(avail)),
                             P(str(len(linked.get(s["id"], [])))) ])
            story.append(tbl(rows, [0.45 * inch, 1.1 * inch, 3.6 * inch, 0.8 * inch, 0.55 * inch, 0.5 * inch]))
        story.append(PageBreak())

    def appendix_sources(self, story):
        story += heading("Appendix B  Bibliography and Source Register", H1, 0, "app-src", self.pm)
        for s in sorted(self.d["sources"], key=lambda s: s["id"]):
            line = (f"<b>{sid(s['id'])}</b> [{e(s['id'])}] {e(s.get('publisher', ''))}. <i>{e(s.get('title', ''))}</i>"
                    f"{'. ' + e(s['doc_number']) if s.get('doc_number') else ''}"
                    f"{'. ' + e(s['date']) if s.get('date') else ''}. Type: {e(s.get('type', ''))}. "
                    f"{('URL: ' + e(s['url'])) if s.get('url') else ''} "
                    f"{('(accessed ' + e(s['accessed']) + ')') if s.get('accessed') else ''} "
                    f"{('Status: ' + e(s['access_status']) + '.') if s.get('access_status') not in (None, '', 'ok') else ''}"
                    f"{(' Local copy: ' + e(s['local_file'])) if s.get('local_file') else ''}"
                    f"{(' Note: ' + e(s['notes'])) if s.get('notes') else ''}")
            story.append(KeepTogether([Anchor(s["id"], self.pm), Paragraph(line, SMALL), Spacer(1, 2)]))
        story.append(PageBreak())

    def appendix_status(self, story):
        story += heading("Appendix C  Research Status and Open Questions", H1, 0, "app-status", self.pm)
        conf = defaultdict(int)
        for p in self.d["parts"]:
            for lst in p["claims"].values():
                for c in lst:
                    conf[c["conf"]] += 1
        rows = [[P("Evidence class", HDR), P("Part claims", HDR)]] + [
            [P(f"{badge(k)} {CONF_NAME[k]}"), P(str(conf[k]))] for k in "ABCD"]
        story.append(tbl(rows, [3 * inch, 1.5 * inch]))
        gaps = defaultdict(int)
        for p in self.d["parts"]:
            for u in p.get("unknowns", []):
                gaps[u] += 1
        if gaps:
            story.append(Paragraph("Most frequent documentation gaps", H3))
            rows = [[P("Field", HDR), P("Parts lacking it", HDR)]] + [
                [P(e(FIELD_LABELS.get(k, k))), P(str(v))] for k, v in sorted(gaps.items(), key=lambda x: -x[1])]
            story.append(tbl(rows, [3 * inch, 1.5 * inch]))
        story.append(Paragraph("Open research leads (priority 1–2)", H3))
        rows = [[P("Lead", HDR), P("Pri.", HDR), P("Topic / detail", HDR)]]
        for l in sorted(self.d["leads"], key=lambda l: (l["priority"], l["id"])):
            if l["status"] == "open" and l["priority"] <= 2:
                rows.append([P(e(l["id"])), P(str(l["priority"])),
                             P(f"<b>{e(l['topic'])}</b> — {e(l['detail'])}"
                               f"{(' Docs: ' + e(', '.join(l['doc_numbers']))) if l['doc_numbers'] else ''}")])
        story.append(tbl(rows, [0.8 * inch, 0.4 * inch, 5.8 * inch]))
        story.append(Paragraph("The complete backlog is maintained in research/BACKLOG.md.", SMALL))


class _Group(Flowable):
    """Splittable sequence (used for long part entries that cannot be kept together)."""

    def __init__(self, flowables):
        super().__init__()
        self.fl = flowables

    def wrap(self, aw, ah):
        return aw, 0

    def split(self, aw, ah):
        return self.fl

    def draw(self):
        pass


def git_commit():
    try:
        return subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"],
                                       stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return "uncommitted"


def build(data, pagemap, meta):
    cat = Catalogue(data, pagemap)
    story = []
    cat.front(story, meta)
    cat.how_to_use(story)
    cat.ident_guide(story)
    n = cat.mfr_sections(story, 3)
    cat.breaker_register(story, n)
    cat.crossref(story, n + 1)
    cat.indexes(story, n + 2)
    cat.appendix_docs(story)
    cat.appendix_sources(story)
    cat.appendix_status(story)
    OUT.parent.mkdir(exist_ok=True)
    doc = Doc(OUT, meta)
    doc.multiBuild(story)
    return doc


def main():
    data = load_all()
    mfrs = sorted({x["mfr"] for x in data["families"] + data["parts"]}, key=list(MANUFACTURERS).index)
    meta = {"version": data["meta"].get("edition", "0.1"), "date": str(date.today()), "commit": git_commit(),
            "parts": len(data["parts"]), "families": len(data["families"]), "breakers": len(data["breakers"]),
            "sources": len(data["sources"]), "docs": sum(1 for s in data["sources"] if s.get("local_file")),
            "leads": sum(1 for l in data["leads"] if l["status"] == "open"), "mfrs": mfrs}
    pagemap = {}
    build(data, pagemap, meta)              # pass 1: collect anchor pages
    pm2 = dict(pagemap)
    build(data, pm2, meta)                  # pass 2: indexes carry page numbers
    print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
