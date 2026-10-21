#!/usr/bin/env python3
"""Merge research batches (research/incoming/*.json) into the canonical data store.

Assigns permanent IDs, de-duplicates sources/families/breakers/parts, merges claims
without ever discarding existing evidence, files downloaded documents into
docs/library/<MFR>/, appends leads to the backlog and writes a research log entry.

Usage: python3 tools/merge.py [batch.json ...]   (default: all files in research/incoming)
"""
import hashlib
import shutil
import sys
from datetime import date
from pathlib import Path

from common import (CONF_RANK, DATA, ROOT, as_list, load, norm_pn, norm_url, save)

INCOMING = ROOT / "research" / "incoming"
MERGED = INCOMING / "merged"
LIB = ROOT / "docs" / "library"

PUBLISHER_MFR = [
    ("square d", "SQD"), ("schneider", "SQD"), ("federal pioneer", "SQD"),
    ("cutler", "EAT"), ("westinghouse", "EAT"), ("eaton", "EAT"), ("challenger", "EAT"), ("bryant", "EAT"),
    ("general electric", "GEA"), ("ge ", "GEA"), ("ge industrial", "GEA"), ("abb", "GEA"), ("reliagear", "GEA"),
    ("siemens", "SIE"), ("ite", "SIE"), ("gould", "SIE"), ("murray", "SIE"),
    ("federal pacific", "FPE"), ("zinsco", "ZIN"), ("sylvania", "ZIN"),
]


class Store:
    def __init__(self):
        self.meta = load(DATA / "meta.json", {"counters": {}, "batches": []})
        self.sources = load(DATA / "sources.json", [])
        self.families = load(DATA / "families.json", [])
        self.breakers = load(DATA / "breakers.json", [])
        self.parts = {}
        for f in sorted((DATA / "parts").glob("*.json")):
            for p in load(f, []):
                self.parts[p["id"]] = p
        self.leads = load(DATA / "leads.json", [])

    def next_id(self, prefix, width):
        c = self.meta["counters"]
        c[prefix] = c.get(prefix, 0) + 1
        return f"{prefix}-{c[prefix]:0{width}d}"

    def save(self):
        save(DATA / "meta.json", self.meta)
        save(DATA / "sources.json", self.sources)
        save(DATA / "families.json", sorted(self.families, key=lambda x: x["id"]))
        save(DATA / "breakers.json", sorted(self.breakers, key=lambda x: x["id"]))
        by_mfr = {}
        for p in self.parts.values():
            by_mfr.setdefault(p["mfr"], []).append(p)
        for f in (DATA / "parts").glob("*.json"):
            f.unlink()
        for m, lst in by_mfr.items():
            save(DATA / "parts" / f"{m}.json", sorted(lst, key=lambda x: x["id"]))
        save(DATA / "leads.json", self.leads)


def guess_mfr(text):
    t = " " + (text or "").lower() + " "
    for kw, code in PUBLISHER_MFR:
        if kw in t:
            return code
    return "OTH"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def norm_claim(c, srcmap, batch, warnings, where):
    if c is None:
        return None
    if not isinstance(c, dict):
        c = {"value": c, "conf": "D", "src": []}
    val = c.get("value")
    if isinstance(val, list):
        val = "; ".join(str(v) for v in val)
    if val is None or str(val).strip() == "":
        return None
    conf = str(c.get("conf", "D")).strip().upper()[:1]
    if conf not in CONF_RANK:
        warnings.append(f"{where}: bad conf {c.get('conf')!r} -> D")
        conf = "D"
    src = []
    for k in as_list(c.get("src")):
        if k in srcmap:
            src.append(srcmap[k])
        elif str(k).startswith("SRC-"):
            src.append(k)
        else:
            warnings.append(f"{where}: unknown source key {k!r}")
    if conf in ("A", "B") and not src:
        warnings.append(f"{where}: conf {conf} without sources -> C")
        conf = "C"
    out = {"value": str(val).strip(), "conf": conf, "src": src}
    for k in ("page", "basis", "note", "relation"):
        if c.get(k):
            out[k] = str(c[k])
    out["batch"] = batch
    return out


def merge_claim_lists(existing, new):
    """Append new claims; identical values merge their sources. Nothing is dropped."""
    existing = list(existing or [])
    for n in new:
        dup = None
        for e in existing:
            if norm_pn(e["value"]) == norm_pn(n["value"]) and e.get("relation") == n.get("relation"):
                dup = e
                break
        if dup:
            for s in n["src"]:
                if s not in dup["src"]:
                    dup["src"].append(s)
            if CONF_RANK[n["conf"]] > CONF_RANK[dup["conf"]]:
                dup["conf"] = n["conf"]
                for k in ("page", "basis"):
                    if n.get(k):
                        dup[k] = n[k]
        else:
            existing.append(n)
    existing.sort(key=lambda c: -CONF_RANK[c["conf"]])
    return existing


def claims_block(raw, srcmap, batch, warnings, where):
    out = {}
    for field, c in (raw or {}).items():
        lst = [norm_claim(x, srcmap, batch, warnings, f"{where}.{field}") for x in as_list(c)]
        lst = [x for x in lst if x]
        if lst:
            out[field] = lst
    return out


def merge_batch(store, path, warnings):
    b = load(path, None)
    batch = b.get("batch_id") or path.stem
    if batch in [x["batch_id"] for x in store.meta["batches"]]:
        warnings.append(f"{batch}: already merged, skipping")
        return None
    stats = {"sources_new": 0, "families_new": 0, "breakers_new": 0, "parts_new": 0,
             "parts_updated": 0, "leads_new": 0, "docs_filed": 0, "batch": batch}

    # ---- sources
    srcmap = {}
    by_url = {norm_url(s.get("url")): s for s in store.sources if s.get("url")}
    by_doc = {(s.get("publisher", "").lower(), norm_pn(s.get("doc_number"))): s
              for s in store.sources if s.get("doc_number")}
    for s in b.get("sources", []):
        key = s.get("key")
        hit = by_url.get(norm_url(s.get("url"))) if s.get("url") else None
        if not hit and s.get("doc_number"):
            hit = by_doc.get((s.get("publisher", "").lower(), norm_pn(s.get("doc_number"))))
        if hit:
            srcmap[key] = hit["id"]
            for k, v in s.items():
                if k not in ("key",) and v and not hit.get(k):
                    hit[k] = v
            rec = hit
        else:
            rec = {k: v for k, v in s.items() if k != "key"}
            rec["id"] = store.next_id("SRC", 5)
            rec["mfr"] = guess_mfr(f"{s.get('publisher', '')} {s.get('title', '')}")
            rec["batches"] = []
            store.sources.append(rec)
            srcmap[key] = rec["id"]
            stats["sources_new"] += 1
            if rec.get("url"):
                by_url[norm_url(rec["url"])] = rec
        if batch not in rec.setdefault("batches", []):
            rec["batches"].append(batch)
        # file local document
        lf = rec.get("local_file")
        if lf and "_incoming" in lf:
            src_path = ROOT / lf
            if src_path.exists():
                dest_dir = LIB / rec.get("mfr", "OTH")
                dest_dir.mkdir(parents=True, exist_ok=True)
                dest = dest_dir / src_path.name
                digest = sha256(src_path)
                if dest.exists() and sha256(dest) != digest:
                    dest = dest_dir / f"{src_path.stem}__{digest[:8]}{src_path.suffix}"
                if not dest.exists():
                    shutil.move(str(src_path), dest)
                rec["local_file"] = str(dest.relative_to(ROOT))
                rec["sha256"] = digest
                rec["bytes"] = dest.stat().st_size
                stats["docs_filed"] += 1
            else:
                warnings.append(f"{batch}: local_file missing {lf}")
                rec.pop("local_file", None)

    # ---- families
    fammap = {}
    for f in b.get("families", []):
        mfr = f.get("mfr", "OTH")
        names = {norm_pn(x) for x in [f.get("code"), f.get("name")] + as_list(f.get("aliases")) if x}
        hit = None
        for e in store.families:
            if e["mfr"] != mfr:
                continue
            enames = {norm_pn(x) for x in [e.get("code"), e.get("name")] + e.get("aliases", []) if x}
            if names & enames:
                hit = e
                break
        where = f"{batch}.family.{f.get('key')}"
        cl = claims_block(f.get("claims"), srcmap, batch, warnings, where)
        for fld in ("era", "status", "successor", "voltage_rating", "main_ampacity", "branch_breakers"):
            if f.get(fld):
                cl.setdefault(fld, [])
                c = norm_claim(f[fld], srcmap, batch, warnings, f"{where}.{fld}")
                if c:
                    cl[fld] = merge_claim_lists(cl[fld], [c])
        srcs = [srcmap[k] for k in as_list(f.get("source_keys")) if k in srcmap]
        if hit:
            for fld, lst in cl.items():
                hit["claims"][fld] = merge_claim_lists(hit["claims"].get(fld), lst)
            hit["aliases"] = sorted(set(hit.get("aliases", [])) | set(as_list(f.get("aliases"))))
            hit["brand_markings"] = sorted(set(hit.get("brand_markings", [])) | set(as_list(f.get("brand_markings"))))
            if f.get("overview") and f["overview"] not in hit.get("overview_notes", []):
                hit.setdefault("overview_notes", []).append(f["overview"])
            hit["source_ids"] = sorted(set(hit.get("source_ids", [])) | set(srcs))
            fammap[f.get("key")] = hit["id"]
        else:
            rec = {"id": store.next_id(f"FAM-{mfr}", 3), "mfr": mfr,
                   "name": f.get("name"), "code": f.get("code"),
                   "aliases": as_list(f.get("aliases")), "brand_markings": as_list(f.get("brand_markings")),
                   "equipment_type": f.get("equipment_type", "other"),
                   "overview": f.get("overview", ""), "overview_notes": [],
                   "claims": cl, "source_ids": srcs, "created_batch": batch}
            store.families.append(rec)
            fammap[f.get("key")] = rec["id"]
            stats["families_new"] += 1

    # ---- breakers
    brkmap = {}
    for x in b.get("breakers", []):
        mfr = x.get("mfr", "OTH")
        names = {norm_pn(n) for n in [x.get("name")] + as_list(x.get("aliases")) if n}
        hit = next((e for e in store.breakers if e["mfr"] == mfr and
                    names & {norm_pn(n) for n in [e["name"]] + e.get("aliases", [])}), None)
        where = f"{batch}.breaker.{x.get('key')}"
        cl = claims_block(x.get("claims"), srcmap, batch, warnings, where)
        for fld in ("mounting", "frame", "poles", "amps", "voltage", "interrupting", "status"):
            if x.get(fld):
                c = norm_claim(x[fld], srcmap, batch, warnings, f"{where}.{fld}")
                if c:
                    cl[fld] = merge_claim_lists(cl.get(fld), [c])
        fams = [fammap[k] for k in as_list(x.get("used_in_family_keys")) if k in fammap]
        srcs = [srcmap[k] for k in as_list(x.get("source_keys")) if k in srcmap]
        if hit:
            for fld, lst in cl.items():
                hit["claims"][fld] = merge_claim_lists(hit["claims"].get(fld), lst)
            hit["family_ids"] = sorted(set(hit["family_ids"]) | set(fams))
            hit["aliases"] = sorted(set(hit.get("aliases", [])) | set(as_list(x.get("aliases"))))
            hit["source_ids"] = sorted(set(hit["source_ids"]) | set(srcs))
            brkmap[x.get("key")] = hit["id"]
        else:
            rec = {"id": store.next_id(f"BRK-{mfr}", 3), "mfr": mfr, "name": x.get("name"),
                   "aliases": as_list(x.get("aliases")), "claims": cl, "family_ids": fams,
                   "source_ids": srcs, "created_batch": batch}
            store.breakers.append(rec)
            brkmap[x.get("key")] = rec["id"]
            stats["breakers_new"] += 1

    # ---- parts
    partmap, pending_req = {}, []
    index = {}
    for p in store.parts.values():
        k = (p["mfr"], norm_pn(p.get("oem_part_number"))) if p.get("oem_part_number") else (p["mfr"], "T:" + p["title"].lower())
        index[k] = p
    for x in b.get("parts", []):
        mfr = x.get("mfr", "OTH")
        pn = (x.get("oem_part_number") or "").strip()
        k = (mfr, norm_pn(pn)) if pn else (mfr, "T:" + (x.get("title") or "").lower())
        where = f"{batch}.part.{x.get('key')}:{pn}"
        cl = claims_block(x.get("claims"), srcmap, batch, warnings, where)
        fams = [fammap[k2] for k2 in as_list(x.get("family_keys")) if k2 in fammap]
        brks = [brkmap[k2] for k2 in as_list(x.get("breaker_keys")) if k2 in brkmap]
        srcs = [srcmap[k2] for k2 in as_list(x.get("source_keys")) if k2 in srcmap]
        for k2 in as_list(x.get("family_keys")):
            if k2 not in fammap:
                warnings.append(f"{where}: unknown family key {k2}")
        hit = index.get(k)
        if hit:
            for fld, lst in cl.items():
                hit["claims"][fld] = merge_claim_lists(hit["claims"].get(fld), lst)
            hit["family_ids"] = sorted(set(hit["family_ids"]) | set(fams))
            hit["breaker_ids"] = sorted(set(hit["breaker_ids"]) | set(brks))
            hit["source_ids"] = sorted(set(hit["source_ids"]) | set(srcs))
            hit["unknowns"] = sorted((set(hit["unknowns"]) | set(as_list(x.get("unknowns")))) - set(hit["claims"]))
            hit["questions"] = hit["questions"] + [q for q in as_list(x.get("questions")) if q not in hit["questions"]]
            if batch not in hit["batches"]:
                hit["batches"].append(batch)
            hit["updated"] = b.get("date") or str(date.today())
            rec = hit
            stats["parts_updated"] += 1
        else:
            rec = {"id": store.next_id(f"EDH-{mfr}", 5), "mfr": mfr,
                   "brand_marking": x.get("brand_marking", ""), "oem_part_number": pn,
                   "title": x.get("title") or pn, "component_type": x.get("component_type", "other"),
                   "family_ids": fams, "breaker_ids": brks, "claims": cl,
                   "requires": [], "unknowns": sorted(set(as_list(x.get("unknowns"))) - set(cl)),
                   "questions": as_list(x.get("questions")), "source_ids": srcs,
                   "batches": [batch], "created": b.get("date") or str(date.today()),
                   "updated": b.get("date") or str(date.today())}
            store.parts[rec["id"]] = rec
            index[k] = rec
            stats["parts_new"] += 1
        partmap[x.get("key")] = rec["id"]
        pending_req.append((rec, as_list(x.get("requires_part_keys"))))
    for rec, keys in pending_req:
        for k2 in keys:
            pid = partmap.get(k2)
            if pid and pid not in rec["requires"] and pid != rec["id"]:
                rec["requires"].append(pid)

    # ---- leads
    topics = {l["topic"].lower() for l in store.leads}
    for l in b.get("leads", []):
        if not l.get("topic") or l["topic"].lower() in topics:
            continue
        topics.add(l["topic"].lower())
        store.leads.append({"id": store.next_id("LEAD", 4), "priority": int(l.get("priority", 3)),
                            "topic": l["topic"], "detail": l.get("detail", ""),
                            "doc_numbers": as_list(l.get("doc_numbers")), "urls": as_list(l.get("urls")),
                            "status": "open", "batch": batch})
        stats["leads_new"] += 1

    # ---- log
    logdir = ROOT / "research" / "log"
    logdir.mkdir(parents=True, exist_ok=True)
    with open(logdir / f"{batch}.md", "w") as f:
        f.write(f"# Research log — {batch}\n\n")
        f.write(f"* Date: {b.get('date', '')}\n* Researcher: {b.get('researcher', '')}\n")
        f.write(f"* Scope: {b.get('scope', '')}\n* Merge stats: {stats}\n\n## Narrative\n\n")
        f.write((b.get("log") or "(none)") + "\n")
    store.meta["batches"].append({"batch_id": batch, "date": b.get("date"), "merged": str(date.today()),
                                  "file": path.name, "stats": stats})
    return stats


def main():
    files = [Path(a) for a in sys.argv[1:]] or sorted(INCOMING.glob("*.json"))
    store = Store()
    MERGED.mkdir(parents=True, exist_ok=True)
    for path in files:
        warnings = []
        stats = merge_batch(store, path, warnings)
        print(f"{path.name}: {stats}")
        for w in warnings[:200]:
            print("  WARN", w)
        if len(warnings) > 200:
            print(f"  ... {len(warnings) - 200} more warnings")
        if stats is not None:
            shutil.move(str(path), MERGED / path.name)
            inc = ROOT / "docs" / "library" / "_incoming" / (stats.get("batch") or path.stem)
            if inc.exists():
                # derived text extractions are discarded; unreferenced originals are kept for review
                for f in sorted(inc.rglob("*")):
                    if f.is_file() and f.suffix.lower() == ".txt":
                        f.unlink()
                    elif f.is_file():
                        dest = LIB / "_unlinked" / inc.name / f.name
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(f), dest)
                        print(f"  NOTE unreferenced document kept at {dest.relative_to(ROOT)}")
                shutil.rmtree(inc, ignore_errors=True)
    store.save()


if __name__ == "__main__":
    main()
