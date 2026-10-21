#!/usr/bin/env python3
"""Build SQLite database, CSV exports, documentation index, research register and backlog
from the canonical JSON store (data/). All outputs are regenerated; never edit them by hand."""
import csv
import sqlite3
from collections import defaultdict

from common import (CLAIM_FIELDS, CONF_RANK, MANUFACTURERS, ROOT, best, load_all)

BUILD = ROOT / "build"
SCHEMA = """
CREATE TABLE manufacturers(code TEXT PRIMARY KEY, name TEXT, lineage TEXT);
CREATE TABLE sources(id TEXT PRIMARY KEY, mfr TEXT, title TEXT, publisher TEXT, doc_number TEXT,
  date TEXT, url TEXT, type TEXT, accessed TEXT, access_status TEXT, local_file TEXT, sha256 TEXT, notes TEXT);
CREATE TABLE families(id TEXT PRIMARY KEY, mfr TEXT, code TEXT, name TEXT, equipment_type TEXT,
  aliases TEXT, brand_markings TEXT, overview TEXT);
CREATE TABLE breakers(id TEXT PRIMARY KEY, mfr TEXT, name TEXT, aliases TEXT);
CREATE TABLE parts(id TEXT PRIMARY KEY, mfr TEXT, oem_part_number TEXT, title TEXT, component_type TEXT,
  brand_marking TEXT, best_conf TEXT, status TEXT, unknowns TEXT, questions TEXT, created TEXT, updated TEXT);
CREATE TABLE claims(entity_type TEXT, entity_id TEXT, field TEXT, value TEXT, conf TEXT,
  src TEXT, page TEXT, basis TEXT, relation TEXT, note TEXT, batch TEXT);
CREATE TABLE part_family(part_id TEXT, family_id TEXT);
CREATE TABLE part_breaker(part_id TEXT, breaker_id TEXT);
CREATE TABLE breaker_family(breaker_id TEXT, family_id TEXT);
CREATE TABLE part_requires(part_id TEXT, required_part_id TEXT);
CREATE TABLE part_source(part_id TEXT, source_id TEXT);
CREATE TABLE family_source(family_id TEXT, source_id TEXT);
CREATE TABLE leads(id TEXT PRIMARY KEY, priority INTEGER, topic TEXT, detail TEXT, doc_numbers TEXT,
  urls TEXT, status TEXT, batch TEXT);
CREATE VIEW part_numbers AS
  SELECT oem_part_number AS pn, id AS part_id, 'primary' AS relation FROM parts WHERE oem_part_number<>''
  UNION SELECT value, entity_id, COALESCE(relation,'alternate') FROM claims
  WHERE entity_type='part' AND field='alt_part_numbers';
"""


def j(lst):
    return "; ".join(str(x) for x in lst or [])


def part_sources(p):
    s = set(p.get("source_ids", []))
    for lst in p["claims"].values():
        for c in lst:
            s.update(c["src"])
    return sorted(s)


def main():
    d = load_all()
    BUILD.mkdir(exist_ok=True)
    dbp = BUILD / "edh_catalogue.sqlite"
    if dbp.exists():
        dbp.unlink()
    db = sqlite3.connect(dbp)
    db.executescript(SCHEMA)
    for code, (name, lineage) in MANUFACTURERS.items():
        db.execute("INSERT INTO manufacturers VALUES(?,?,?)", (code, name, lineage))
    for s in d["sources"]:
        db.execute("INSERT INTO sources VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                   tuple(s.get(k, "") for k in ("id", "mfr", "title", "publisher", "doc_number", "date", "url",
                                                 "type", "accessed", "access_status", "local_file", "sha256", "notes")))

    def claims(etype, eid, cl):
        for field, lst in cl.items():
            for c in lst:
                db.execute("INSERT INTO claims VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                           (etype, eid, field, c["value"], c["conf"], j(c["src"]), c.get("page", ""),
                            c.get("basis", ""), c.get("relation", ""), c.get("note", ""), c.get("batch", "")))

    for f in d["families"]:
        db.execute("INSERT INTO families VALUES(?,?,?,?,?,?,?,?)",
                   (f["id"], f["mfr"], f.get("code"), f.get("name"), f.get("equipment_type"),
                    j(f.get("aliases")), j(f.get("brand_markings")),
                    "\n\n".join([f.get("overview", "")] + f.get("overview_notes", []))))
        claims("family", f["id"], f["claims"])
        for s in f.get("source_ids", []):
            db.execute("INSERT INTO family_source VALUES(?,?)", (f["id"], s))
    for b in d["breakers"]:
        db.execute("INSERT INTO breakers VALUES(?,?,?,?)", (b["id"], b["mfr"], b["name"], j(b.get("aliases"))))
        claims("breaker", b["id"], b["claims"])
        for fid in b.get("family_ids", []):
            db.execute("INSERT INTO breaker_family VALUES(?,?)", (b["id"], fid))
    for p in d["parts"]:
        st = best(p["claims"].get("status"))
        confs = [c["conf"] for lst in p["claims"].values() for c in lst]
        bc = max(confs, key=lambda c: CONF_RANK[c]) if confs else "D"
        db.execute("INSERT INTO parts VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                   (p["id"], p["mfr"], p.get("oem_part_number", ""), p["title"], p["component_type"],
                    p.get("brand_marking", ""), bc, st["value"] if st else "unknown", j(p.get("unknowns")),
                    j(p.get("questions")), p.get("created"), p.get("updated")))
        claims("part", p["id"], p["claims"])
        for fid in p["family_ids"]:
            db.execute("INSERT INTO part_family VALUES(?,?)", (p["id"], fid))
        for bid in p["breaker_ids"]:
            db.execute("INSERT INTO part_breaker VALUES(?,?)", (p["id"], bid))
        for r in p.get("requires", []):
            db.execute("INSERT INTO part_requires VALUES(?,?)", (p["id"], r))
        for s in part_sources(p):
            db.execute("INSERT INTO part_source VALUES(?,?)", (p["id"], s))
    for l in d["leads"]:
        db.execute("INSERT INTO leads VALUES(?,?,?,?,?,?,?,?)",
                   (l["id"], l["priority"], l["topic"], l["detail"], j(l["doc_numbers"]), j(l["urls"]),
                    l["status"], l["batch"]))
    db.commit()
    db.close()

    # ---- CSV exports
    fams = {f["id"]: f for f in d["families"]}
    brks = {b["id"]: b for b in d["breakers"]}
    with open(BUILD / "parts_master.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["catalogue_id", "mfr", "oem_part_number", "title", "component_type", "families", "breakers"]
                   + [x for fld in CLAIM_FIELDS for x in (fld, fld + "_conf")]
                   + ["requires", "unknowns", "questions", "sources", "updated"])
        for p in d["parts"]:
            row = [p["id"], p["mfr"], p.get("oem_part_number", ""), p["title"], p["component_type"],
                   j(fams[x].get("code") or fams[x]["name"] for x in p["family_ids"] if x in fams),
                   j(brks[x]["name"] for x in p["breaker_ids"] if x in brks)]
            for fld in CLAIM_FIELDS:
                lst = p["claims"].get(fld, [])
                if fld == "alt_part_numbers":
                    row += [j(f"{c['value']} ({c.get('relation', 'alt')})" for c in lst),
                            j(c["conf"] for c in lst)]
                else:
                    c = best(lst)
                    row += [c["value"] if c else "", c["conf"] if c else ""]
            row += [j(p.get("requires")), j(p.get("unknowns")), j(p.get("questions")), j(part_sources(p)),
                    p.get("updated", "")]
            w.writerow(row)
    with open(BUILD / "claims.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["entity_type", "entity_id", "field", "value", "conf", "sources", "page", "basis", "relation", "note", "batch"])
        for etype, coll in (("family", d["families"]), ("breaker", d["breakers"]), ("part", d["parts"])):
            for e in coll:
                for fld, lst in e["claims"].items():
                    for c in lst:
                        w.writerow([etype, e["id"], fld, c["value"], c["conf"], j(c["src"]), c.get("page", ""),
                                    c.get("basis", ""), c.get("relation", ""), c.get("note", ""), c.get("batch", "")])
    with open(BUILD / "families.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["family_id", "mfr", "code", "name", "equipment_type", "aliases", "status", "era", "successor", "overview"])
        for x in d["families"]:
            g = lambda k: (best(x["claims"].get(k)) or {}).get("value", "")
            w.writerow([x["id"], x["mfr"], x.get("code"), x["name"], x["equipment_type"], j(x["aliases"]),
                        g("status"), g("era"), g("successor"), x.get("overview", "")])
    with open(BUILD / "breakers.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["breaker_id", "mfr", "name", "aliases", "mounting", "frame", "poles", "amps", "voltage", "status", "families"])
        for x in d["breakers"]:
            g = lambda k: (best(x["claims"].get(k)) or {}).get("value", "")
            w.writerow([x["id"], x["mfr"], x["name"], j(x["aliases"]), g("mounting"), g("frame"), g("poles"),
                        g("amps"), g("voltage"), g("status"),
                        j(fams[i].get("code") or fams[i]["name"] for i in x["family_ids"] if i in fams)])

    # ---- documentation index (sources -> linked families/parts)
    src_parts, src_fams = defaultdict(set), defaultdict(set)
    for p in d["parts"]:
        for s in part_sources(p):
            src_parts[s].add(p["id"])
            for fid in p["family_ids"]:
                src_fams[s].add(fid)
    for fa in d["families"]:
        for s in fa.get("source_ids", []):
            src_fams[s].add(fa["id"])
        for lst in fa["claims"].values():
            for c in lst:
                for s in c["src"]:
                    src_fams[s].add(fa["id"])
    cols = ["source_id", "mfr", "type", "doc_number", "title", "publisher", "date", "url", "access_status",
            "local_file", "sha256", "families", "parts"]
    with open(ROOT / "docs" / "DOCUMENT_INDEX.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for s in sorted(d["sources"], key=lambda s: (s.get("mfr", ""), s.get("type", ""), s.get("doc_number") or "~")):
            w.writerow([s["id"], s.get("mfr"), s.get("type"), s.get("doc_number", ""), s.get("title"),
                        s.get("publisher"), s.get("date", ""), s.get("url", ""), s.get("access_status", ""),
                        s.get("local_file", ""), s.get("sha256", ""),
                        j(sorted(src_fams[s["id"]])), j(sorted(src_parts[s["id"]]))])
    db_ok = True

    # ---- research register (markdown) and backlog
    with open(ROOT / "research" / "RESEARCH_REGISTER.md", "w") as f:
        f.write("# Research Register\n\n_Generated by tools/build_db.py — do not edit._\n\n")
        f.write("## Merged batches\n\n| Batch | Date | Stats |\n|---|---|---|\n")
        for b in d["meta"].get("batches", []):
            f.write(f"| {b['batch_id']} | {b.get('date', '')} | {b.get('stats', '')} |\n")
        f.write("\n## Evidence profile\n\n")
        conf = defaultdict(int)
        for p in d["parts"]:
            for lst in p["claims"].values():
                for c in lst:
                    conf[c["conf"]] += 1
        for k in "ABCD":
            f.write(f"* Class {k}: {conf[k]} part claims\n")
        f.write("\n## Parts with open questions or unknowns\n\n| ID | OEM PN | Unknown fields | Questions |\n|---|---|---|---|\n")
        for p in d["parts"]:
            if p.get("unknowns") or p.get("questions"):
                f.write(f"| {p['id']} | {p.get('oem_part_number', '')} | {', '.join(p.get('unknowns', []))} | "
                        f"{' / '.join(q.replace('|', '/') for q in p.get('questions', []))} |\n")
        f.write("\n## Inaccessible sources\n\n| ID | Title | URL | Status |\n|---|---|---|---|\n")
        for s in d["sources"]:
            if s.get("access_status") not in (None, "", "ok"):
                f.write(f"| {s['id']} | {s.get('title', '')} | {s.get('url', '')} | {s.get('access_status')} |\n")
    with open(ROOT / "research" / "BACKLOG.md", "w") as f:
        f.write("# Research Backlog\n\n_Generated from data/leads.json by tools/build_db.py. "
                "Close a lead by setting its status in data/leads.json._\n\n")
        for pr in range(1, 6):
            ls = [l for l in d["leads"] if l["priority"] == pr and l["status"] == "open"]
            if not ls:
                continue
            f.write(f"## Priority {pr}\n\n")
            for l in ls:
                f.write(f"* **{l['id']} — {l['topic']}** ({l['batch']})  \n  {l['detail']}")
                if l["doc_numbers"]:
                    f.write(f"  \n  Docs: {', '.join(l['doc_numbers'])}")
                if l["urls"]:
                    f.write(f"  \n  URLs: {' '.join(l['urls'])}")
                f.write("\n")
            f.write("\n")
    print(f"parts={len(d['parts'])} families={len(d['families'])} breakers={len(d['breakers'])} "
          f"sources={len(d['sources'])} leads={len(d['leads'])} db_ok={db_ok}")


if __name__ == "__main__":
    main()
