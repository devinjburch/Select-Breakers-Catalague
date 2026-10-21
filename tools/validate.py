#!/usr/bin/env python3
"""Integrity checks on the canonical store. Exit code 1 on errors; warnings are informational.

Checks: dangling references, duplicate part numbers, A/B claims without sources,
conflicting values of equal confidence, alt numbers colliding with another part's primary number.
"""
import re
import sys
from collections import defaultdict

from common import CONF_RANK, load_all, norm_pn

SINGLE_VALUED = {"poles", "voltage", "ampacity", "material"}


def main():
    d = load_all()
    errors, warns = [], []
    src_ids = {s["id"] for s in d["sources"]}
    fam_ids = {f["id"] for f in d["families"]}
    brk_ids = {b["id"] for b in d["breakers"]}
    part_ids = {p["id"] for p in d["parts"]}
    ids = [x["id"] for coll in ("sources", "families", "breakers", "parts", "leads") for x in d[coll]]
    for i in {x for x in ids if ids.count(x) > 1}:
        errors.append(f"duplicate id {i}")

    def check_claims(eid, claims):
        for fld, lst in claims.items():
            for c in lst:
                if c["conf"] not in CONF_RANK:
                    errors.append(f"{eid}.{fld}: invalid conf {c['conf']}")
                if c["conf"] in "AB" and not c["src"]:
                    errors.append(f"{eid}.{fld}: class {c['conf']} claim without source")
                for s in c["src"]:
                    if s not in src_ids:
                        errors.append(f"{eid}.{fld}: dangling source {s}")
            if fld in SINGLE_VALUED and len(lst) > 1:
                top = [c for c in lst if c["conf"] == lst[0]["conf"]]
                # wording differences are fine; flag only when the numbers stated differ
                if len({tuple(sorted(set(re.findall(r"\d+(?:\.\d+)?", c["value"])))) for c in top}) > 1:
                    warns.append(f"{eid}.{fld}: conflicting class-{lst[0]['conf']} values: "
                                 + " | ".join(c["value"] for c in top))

    for f in d["families"]:
        check_claims(f["id"], f["claims"])
    for b in d["breakers"]:
        check_claims(b["id"], b["claims"])
        for x in b["family_ids"]:
            if x not in fam_ids:
                errors.append(f"{b['id']}: dangling family {x}")
    primary = defaultdict(list)
    for p in d["parts"]:
        check_claims(p["id"], p["claims"])
        for x in p["family_ids"]:
            if x not in fam_ids:
                errors.append(f"{p['id']}: dangling family {x}")
        for x in p["breaker_ids"]:
            if x not in brk_ids:
                errors.append(f"{p['id']}: dangling breaker {x}")
        for x in p.get("requires", []):
            if x not in part_ids:
                errors.append(f"{p['id']}: dangling requires {x}")
        if p.get("oem_part_number"):
            primary[(p["mfr"], norm_pn(p["oem_part_number"]))].append(p["id"])
        if not p["family_ids"] and not p["breaker_ids"]:
            warns.append(f"{p['id']} ({p.get('oem_part_number')}): no equipment family assigned")
        if not p["claims"]:
            warns.append(f"{p['id']}: no claims")
    for k, v in primary.items():
        if len(v) > 1:
            errors.append(f"duplicate primary part number {k}: {v}")
    for p in d["parts"]:
        for c in p["claims"].get("alt_part_numbers", []):
            hit = primary.get((p["mfr"], norm_pn(c["value"])))
            if hit and p["id"] not in hit:
                warns.append(f"{p['id']}: alternate number {c['value']} is primary number of {hit} "
                             "(possible duplicate or supersession pair - review)")
    for w in warns:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"{len(errors)} errors, {len(warns)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
