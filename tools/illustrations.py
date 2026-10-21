"""Generic, schematic identification illustrations drawn with ReportLab graphics.

These are explanatory drawings of *generic* construction, not reproductions of any OEM
drawing, and are labelled as such in the catalogue. Dimensions are not to scale.
"""
from reportlab.graphics.shapes import Circle, Drawing, Line, Polygon, Rect, String
from reportlab.lib import colors

INK = colors.HexColor("#1b2a3a")
COPPER = colors.HexColor("#c9773b")
TIN = colors.HexColor("#b9c2c8")
INSUL = colors.HexColor("#e8d9a8")
STEEL = colors.HexColor("#8a949c")
NOTE = colors.HexColor("#5a6875")


def _label(d, x, y, text, size=7, anchor="start", color=INK):
    d.add(String(x, y, text, fontName="Helvetica", fontSize=size, fillColor=color, textAnchor=anchor))


def _leader(d, x1, y1, x2, y2):
    d.add(Line(x1, y1, x2, y2, strokeColor=NOTE, strokeWidth=0.5))
    d.add(Circle(x1, y1, 1.2, fillColor=NOTE, strokeColor=NOTE))


def panel_interior(w=480, h=300):
    """Generic panelboard interior: main lugs, phase bus, branch connectors, fillers."""
    d = Drawing(w, h)
    d.add(Rect(10, 10, 200, 280, strokeColor=INK, fillColor=colors.white, strokeWidth=1.2))  # box
    d.add(Rect(30, 245, 160, 30, strokeColor=INK, fillColor=TIN))  # main lug block
    for i in range(3):
        d.add(Rect(45 + i * 50, 250, 30, 20, strokeColor=INK, fillColor=STEEL))
    for i, x in enumerate((90, 105, 120)):  # phase buses
        d.add(Rect(x - 4, 30, 8, 210, strokeColor=INK, fillColor=COPPER))
    for row in range(7):
        y = 50 + row * 26
        for side in (-1, 1):
            x0 = 105 + side * 18
            d.add(Rect(min(x0, x0 + side * 55), y, 55, 18, strokeColor=INK,
                       fillColor=colors.white if row != 4 else colors.HexColor("#eeeeee")))
        d.add(Rect(84, y + 6, 42, 6, strokeColor=INK, fillColor=TIN))  # connector strap
    d.add(Rect(25, 15, 170, 10, strokeColor=INK, fillColor=TIN))  # neutral
    _label(d, 330, 268, "Main lug kit (main-lug-only interior)")
    _leader(d, 160, 262, 328, 270)
    _label(d, 330, 232, "Phase bus (A-B-C), copper or aluminium")
    _leader(d, 120, 225, 328, 234)
    _label(d, 330, 196, "Branch connector strap / breaker connector")
    _leader(d, 115, 159, 328, 198)
    _label(d, 330, 160, "Branch breaker space (bolt-on or plug-on)")
    _leader(d, 175, 138, 328, 162)
    _label(d, 330, 124, "Unused space: filler plate / blank-off in deadfront")
    _leader(d, 175, 164, 328, 126)
    _label(d, 330, 88, "Neutral assembly / neutral lug kit")
    _leader(d, 180, 20, 328, 90)
    _label(d, 330, 52, "Enclosure (box); trim + deadfront fit over interior")
    _leader(d, 205, 60, 328, 54)
    _label(d, w / 2, 0, "Generic schematic for orientation only — not an OEM drawing, not to scale",
           size=6.5, anchor="middle", color=NOTE)
    return d


def connector_strap(w=480, h=170):
    """Generic bolt-on branch connector strap in plan and side view with measurement callouts."""
    d = Drawing(w, h)
    # plan view
    d.add(Rect(30, 80, 170, 26, strokeColor=INK, fillColor=COPPER))
    for x in (55, 175):
        d.add(Circle(x, 93, 6, strokeColor=INK, fillColor=colors.white))
    d.add(Line(55, 120, 175, 120, strokeColor=NOTE, strokeWidth=0.6))
    for x in (55, 175):
        d.add(Line(x, 112, x, 126, strokeColor=NOTE, strokeWidth=0.6))
    _label(d, 115, 128, "C-C hole spacing", anchor="middle")
    _label(d, 30, 64, "Measure: length, width, thickness, hole dia., C-C spacing,")
    _label(d, 30, 54, "offset/bend heights, plating (bare Cu / tin-plated Cu / Al).")
    _label(d, 115, 40, "Plan view", anchor="middle", color=NOTE)
    # side view with joggle
    pts = [260, 100, 330, 100, 345, 125, 430, 125, 430, 133, 340, 133, 325, 108, 260, 108]
    d.add(Polygon(pts, strokeColor=INK, fillColor=COPPER))
    d.add(Line(440, 100, 440, 133, strokeColor=NOTE, strokeWidth=0.6))
    _label(d, 444, 114, "offset")
    _label(d, 345, 80, "Side view (offset / joggle strap)", anchor="middle", color=NOTE)
    d.add(Rect(260, 140, 70, 14, strokeColor=INK, fillColor=INSUL))
    _label(d, 335, 144, "insulating support / barrier (if fitted)")
    _label(d, w / 2, 4, "Generic schematic — record actual measurements as field_measurement evidence",
           size=6.5, anchor="middle", color=NOTE)
    return d


def lug_types(w=480, h=150):
    d = Drawing(w, h)
    # mechanical lug
    d.add(Rect(30, 50, 70, 50, strokeColor=INK, fillColor=TIN))
    d.add(Rect(45, 60, 40, 22, strokeColor=INK, fillColor=colors.white))
    d.add(Rect(58, 100, 14, 14, strokeColor=INK, fillColor=STEEL))
    _label(d, 65, 30, "Mechanical (set-screw) lug", anchor="middle")
    # compression lug
    d.add(Rect(160, 70, 60, 16, strokeColor=INK, fillColor=TIN))
    d.add(Rect(220, 64, 50, 28, strokeColor=INK, fillColor=TIN))
    d.add(Circle(185, 78, 4, strokeColor=INK, fillColor=colors.white))
    d.add(Circle(205, 78, 4, strokeColor=INK, fillColor=colors.white))
    _label(d, 215, 30, "Compression lug (2-hole NEMA)", anchor="middle")
    # multi-barrel
    for i in range(3):
        d.add(Rect(320 + i * 40, 50, 34, 44, strokeColor=INK, fillColor=TIN))
        d.add(Rect(326 + i * 40, 58, 22, 18, strokeColor=INK, fillColor=colors.white))
    _label(d, 380, 30, "Multi-barrel lug (2-3 conductors / pole)", anchor="middle")
    _label(d, w / 2, 8, "Record: body material (Al / Cu / tin-plated Al), wire range, conductors per pole, "
           "mounting-hole size and spacing, markings (e.g. AL9CU)", size=6.5, anchor="middle", color=NOTE)
    return d


def mounting_styles(w=480, h=150):
    d = Drawing(w, h)
    # bolt-on
    d.add(Rect(40, 60, 60, 70, strokeColor=INK, fillColor=colors.white))
    d.add(Rect(100, 88, 50, 10, strokeColor=INK, fillColor=COPPER))
    d.add(Circle(140, 93, 3, strokeColor=INK, fillColor=STEEL))
    _label(d, 95, 40, "Bolt-on: line terminal screws", anchor="middle")
    _label(d, 95, 30, "to bus / connector strap", anchor="middle")
    # plug-on
    d.add(Rect(200, 60, 60, 70, strokeColor=INK, fillColor=colors.white))
    d.add(Polygon([260, 85, 280, 80, 280, 105, 260, 100], strokeColor=INK, fillColor=TIN))
    d.add(Rect(282, 75, 8, 35, strokeColor=INK, fillColor=COPPER))
    _label(d, 245, 40, "Plug-on: jaw/clip engages", anchor="middle")
    _label(d, 245, 30, "bus stab", anchor="middle")
    # I-Line style
    d.add(Rect(340, 60, 90, 70, strokeColor=INK, fillColor=colors.white))
    for i in range(3):
        d.add(Rect(430, 70 + i * 20, 14, 10, strokeColor=INK, fillColor=TIN))
    d.add(Rect(446, 60, 8, 75, strokeColor=INK, fillColor=COPPER))
    _label(d, 395, 40, "Plug-on panel/switchboard unit:", anchor="middle")
    _label(d, 395, 30, "jaws onto vertical bus stack", anchor="middle")
    _label(d, w / 2, 8, "Generic schematics — mounting style is a first-level identification key",
           size=6.5, anchor="middle", color=NOTE)
    return d
