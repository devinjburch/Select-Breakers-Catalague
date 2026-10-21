#!/usr/bin/env python3
"""Generate catalogue/EDH_Lookup.html: a single-file, offline identification lookup.

Search by full or partial part number (primary and alternate), manufacturer, equipment family,
breaker family, component type, rating or free text. Data is embedded as JSON; no network needed.
"""
import json
from datetime import date

from common import CLAIM_FIELDS, FIELD_LABELS, MANUFACTURERS, ROOT, load_all, norm_pn

OUT = ROOT / "catalogue" / "EDH_Lookup.html"


def main():
    d = load_all()
    fams = {f["id"]: f.get("code") or f["name"] for f in d["families"]}
    brks = {b["id"]: b["name"] for b in d["breakers"]}
    srcs = {s["id"]: [s.get("doc_number") or "", s.get("title") or "", s.get("url") or "",
                      s.get("local_file") or ""] for s in d["sources"]}
    parts = []
    for p in d["parts"]:
        claims = {}
        for fld, lst in p["claims"].items():
            claims[fld] = [[c["value"], c["conf"], c["src"], c.get("page", ""), c.get("relation", "")] for c in lst]
        alts = [c["value"] for c in p["claims"].get("alt_part_numbers", [])]
        parts.append({"i": p["id"], "m": p["mfr"], "pn": p["oem_part_number"], "t": p["title"],
                      "ct": p["component_type"], "f": [fams.get(x, x) for x in p["family_ids"]],
                      "b": [brks.get(x, x) for x in p["breaker_ids"]], "c": claims,
                      "k": " ".join(norm_pn(x) for x in [p["oem_part_number"]] + alts),
                      "u": p.get("unknowns", []), "q": p.get("questions", []), "r": p.get("requires", [])})
    payload = {"parts": parts, "src": srcs, "labels": FIELD_LABELS, "order": CLAIM_FIELDS,
               "mfr": {k: v[0] for k, v in MANUFACTURERS.items()}, "built": str(date.today())}
    html = TEMPLATE.replace("/*DATA*/", json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
                            .replace("</", "<\\/"))
    OUT.write_text(html)
    print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB, {len(parts)} parts)")


TEMPLATE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>EDH Hardware Lookup</title>
<style>
:root{--ink:#1b2a3a;--acc:#c8691c;--rule:#c9d1d8;--shade:#f1f4f6;--bg:#fff;--muted:#5a6875;
--A:#2e7d32;--B:#1565c0;--C:#b7791f;--D:#9b2c2c}
@media (prefers-color-scheme:dark){:root{--ink:#e3e8ee;--rule:#3a4652;--shade:#1d252e;--bg:#12181e;--muted:#9aa7b4;
--A:#66bb6a;--B:#64b5f6;--C:#e0a84a;--D:#e57373}}
*{box-sizing:border-box}body{margin:0;font:14px/1.45 system-ui,Segoe UI,Helvetica,Arial,sans-serif;color:var(--ink);background:var(--bg)}
header{background:#1b2a3a;color:#fff;padding:14px 16px;border-bottom:4px solid var(--acc)}
header h1{margin:0;font-size:18px}header p{margin:2px 0 0;font-size:12px;opacity:.8}
.bar{display:flex;flex-wrap:wrap;gap:8px;padding:12px 16px;background:var(--shade);border-bottom:1px solid var(--rule);position:sticky;top:0}
input,select{font:inherit;padding:7px 9px;border:1px solid var(--rule);border-radius:4px;background:var(--bg);color:var(--ink)}
#q{flex:1 1 260px}main{padding:8px 16px 40px;max-width:1200px}
.row{border:1px solid var(--rule);border-radius:5px;margin:8px 0;overflow:hidden}
.row>summary{list-style:none;cursor:pointer;display:grid;grid-template-columns:120px 150px 1fr auto;gap:10px;padding:8px 10px;align-items:baseline}
.row>summary::-webkit-details-marker{display:none}
.id{font:12px ui-monospace,monospace;color:var(--muted)}.pn{font-weight:700}.ct{font-size:12px;color:var(--muted)}
table{border-collapse:collapse;width:100%;font-size:13px}td{border-top:1px solid var(--rule);padding:4px 8px;vertical-align:top}
td:first-child{width:200px;font-weight:600;background:var(--shade)}.cf{font-weight:700}
.cA{color:var(--A)}.cB{color:var(--B)}.cC{color:var(--C)}.cD{color:var(--D)}.src{font-size:11px;color:var(--muted)}
.unk{color:var(--D)}#count{padding:6px 16px;font-size:12px;color:var(--muted)}
@media (max-width:640px){.row>summary{grid-template-columns:1fr 1fr}td:first-child{width:110px}}
</style></head><body>
<header><h1>EDH Electrical Distribution Hardware — Lookup</h1>
<p>Offline companion to the Master Catalogue. Evidence: <b>A</b> OEM verified · <b>B</b> corroborated · <b>C</b> tentative · <b>D</b> unverified. Matching dimensions never prove interchangeability.</p></header>
<div class="bar"><input id="q" placeholder="Part number (full or partial), breaker, family, or words…" autofocus>
<select id="m"><option value="">All manufacturers</option></select>
<select id="ct"><option value="">All component types</option></select>
<select id="mc"><option value="">Any evidence</option><option value="A">Has class A claims</option></select></div>
<div id="count"></div><main id="out"></main>
<script>
const D=/*DATA*/;
const $=s=>document.querySelector(s),esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const norm=s=>s.toUpperCase().replace(/[^A-Z0-9]/g,'');
for(const[k,v]of Object.entries(D.mfr))$('#m').insertAdjacentHTML('beforeend',`<option value="${k}">${k} — ${esc(v)}</option>`);
[...new Set(D.parts.map(p=>p.ct))].sort().forEach(c=>$('#ct').insertAdjacentHTML('beforeend',`<option>${esc(c)}</option>`));
for(const p of D.parts){p.text=(p.t+' '+p.f.join(' ')+' '+p.b.join(' ')+' '+Object.values(p.c).flat().map(c=>c[0]).join(' ')).toUpperCase();
p.hasA=Object.values(p.c).flat().some(c=>c[1]=='A');}
function claimRows(p){const keys=[...D.order.filter(k=>p.c[k]),...Object.keys(p.c).filter(k=>!D.order.includes(k))];let h='';
for(const k of keys)p.c[k].forEach((c,i)=>{const s=c[2].map(id=>{const x=D.src[id]||[];return `<span title="${esc(x[1])}">${esc(id)}${x[0]?' '+esc(x[0]):''}</span>`}).join(', ');
h+=`<tr><td>${i?'':esc(D.labels[k]||k.replace(/_/g,' '))}</td><td>${esc(c[0])}${c[4]?` <span class="src">[${esc(c[4])}]</span>`:''} <span class="cf c${c[1]}">${c[1]}</span><div class="src">${s}${c[3]?' · '+esc(c[3]):''}</div></td></tr>`});
if(p.f.length)h+=`<tr><td>Equipment families</td><td>${esc(p.f.join(', '))}</td></tr>`;
if(p.b.length)h+=`<tr><td>Breaker families</td><td>${esc(p.b.join(', '))}</td></tr>`;
if(p.r.length)h+=`<tr><td>Requires</td><td>${esc(p.r.join(', '))}</td></tr>`;
if(p.u.length)h+=`<tr><td>Not yet documented</td><td class="unk">${esc(p.u.join(', '))}</td></tr>`;
p.q.forEach(q=>h+=`<tr><td>Open question</td><td><i>${esc(q)}</i></td></tr>`);return `<table>${h}</table>`}
function run(){const q=$('#q').value.trim(),m=$('#m').value,ct=$('#ct').value,mc=$('#mc').value;const nq=norm(q),uq=q.toUpperCase();
let r=D.parts.filter(p=>(!m||p.m==m)&&(!ct||p.ct==ct)&&(!mc||p.hasA));
if(q){const sc=p=>p.k.split(' ').some(k=>k==nq)?0:p.k.split(' ').some(k=>k.startsWith(nq))?1:p.k.includes(nq)?2:uq.split(/\s+/).every(w=>p.text.includes(w))?3:9;
r=r.map(p=>[sc(p),p]).filter(x=>x[0]<9).sort((a,b)=>a[0]-b[0]||a[1].pn.localeCompare(b[1].pn)).map(x=>x[1]);}
$('#count').textContent=`${r.length} of ${D.parts.length} entries · data built ${D.built}`+(r.length>300?' · showing first 300':'');
history.replaceState(null,'',q?'#'+encodeURIComponent(q):location.pathname);
$('#out').innerHTML=r.slice(0,300).map((p,i)=>`<details class="row"${r.length<=3||i==0&&q?' open':''}><summary><span class="id">${p.i}</span><span class="pn">${esc(p.pn||'(no OEM no.)')}</span><span>${esc(p.t)}</span><span class="ct">${p.m} · ${esc(p.ct)}</span></summary>${claimRows(p)}</details>`).join('');}
if(location.hash)$('#q').value=decodeURIComponent(location.hash.slice(1));
let t;['#q','#m','#ct','#mc'].forEach(s=>$(s).addEventListener('input',()=>{clearTimeout(t);t=setTimeout(run,150)}));run();
</script></body></html>
"""

if __name__ == "__main__":
    main()
