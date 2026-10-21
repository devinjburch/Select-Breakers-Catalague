"""Shared helpers for the EDH catalogue toolchain."""
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CONF_RANK = {"A": 4, "B": 3, "C": 2, "D": 1}

MANUFACTURERS = {
    "EAT": ("Eaton lineage", "Eaton, Cutler-Hammer, Westinghouse (distribution products), Challenger, Bryant"),
    "SQD": ("Square D / Schneider Electric", "Square D, Schneider Electric, Federal Pioneer (Canada)"),
    "GEA": ("GE / ABB lineage", "General Electric Industrial Solutions; ABB from 2018; ReliaGear"),
    "SIE": ("Siemens lineage", "Siemens, ITE, ITE Imperial, Gould, Murray"),
    "FPE": ("Federal Pacific Electric", "Federal Pacific Electric (Stab-Lok, NA/NE/NF/NH panelboards)"),
    "ZIN": ("Zinsco / Sylvania", "Zinsco, GTE-Sylvania"),
    "ABB": ("ABB (non-GE heritage)", "ABB product lines not originating with GE"),
    "OTH": ("Other manufacturers", "Other / unassigned"),
}

CLAIM_FIELDS = [
    "oem_part_number", "alt_part_numbers", "description", "application", "location",
    "breaker_compat", "frame", "poles", "voltage", "ampacity", "kit_contents",
    "wire_range", "material", "finish", "dimensions", "hole_pattern", "fasteners", "torque",
    "install_doc", "status", "replacement", "aftermarket", "id_features",
]
FIELD_LABELS = {
    "oem_part_number": "OEM part number", "alt_part_numbers": "Alternate / superseded numbers",
    "description": "Description", "application": "Application", "location": "Installation location",
    "breaker_compat": "Breaker compatibility", "frame": "Breaker frame", "poles": "Poles",
    "voltage": "Voltage rating", "ampacity": "Current rating", "kit_contents": "Kit contents",
    "material": "Material", "finish": "Finish / plating", "dimensions": "Dimensions",
    "hole_pattern": "Mounting-hole pattern", "fasteners": "Fasteners", "torque": "Torque values",
    "install_doc": "OEM instruction document", "status": "Status", "replacement": "Replacement / successor",
    "aftermarket": "Aftermarket / reproduction", "id_features": "Identification features",
    "era": "Era of manufacture", "successor": "Successor", "voltage_rating": "Voltage rating",
    "main_ampacity": "Main ampacity", "branch_breakers": "Branch breakers accepted",
    "mounting": "Mounting", "wire_range": "Wire range", "package_data": "Package data (not part dims)",
    "listing": "Listing / approvals", "install_requirements": "Installation requirements",
    "install_constraint": "Installation constraint", "requires": "Requires (stated)", "amps": "Ampere range", "interrupting": "Interrupting ratings",
}


def load(path, default):
    p = Path(path)
    if not p.exists():
        return default
    with open(p) as f:
        return json.load(f)


def save(path, obj):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=1, ensure_ascii=False, sort_keys=False)
        f.write("\n")
    os.replace(tmp, p)


def norm_pn(pn):
    """Normalise a part number for duplicate detection."""
    return re.sub(r"[^A-Z0-9]", "", (pn or "").upper())


def norm_url(u):
    u = (u or "").strip().lower()
    u = re.sub(r"^https?://(www\.)?", "", u)
    return u.rstrip("/")


def best(claims):
    """Highest-confidence claim from a list (first wins on ties)."""
    if not claims:
        return None
    if isinstance(claims, dict):
        return claims
    return sorted(claims, key=lambda c: -CONF_RANK.get(c.get("conf", "D"), 0))[0]


def as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def load_all():
    return {
        "sources": load(DATA / "sources.json", []),
        "families": load(DATA / "families.json", []),
        "breakers": load(DATA / "breakers.json", []),
        "parts": [p for f in sorted((DATA / "parts").glob("*.json")) for p in load(f, [])],
        "leads": load(DATA / "leads.json", []),
        "meta": load(DATA / "meta.json", {}),
    }
