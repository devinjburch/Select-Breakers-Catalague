# Incoming Research Batch Format (v1)

Every research session writes ONE JSON file to `research/incoming/<batch_id>.json`.
`tools/merge.py` validates it, assigns permanent catalogue IDs, de-duplicates
against existing records, and moves it to `research/incoming/merged/`.

Researchers never assign permanent IDs. Use local keys (`"key"`) that are unique
inside the batch; the merge tool maps them to permanent IDs.

## Top level

```json
{
  "batch_id": "B0001-eaton-prl",
  "researcher": "agent/session description",
  "date": "YYYY-MM-DD",
  "scope": "what was researched",
  "sources":   [ <Source>, ... ],
  "families":  [ <Family>, ... ],
  "breakers":  [ <BreakerFamily>, ... ],
  "parts":     [ <Part>, ... ],
  "leads":     [ <Lead>, ... ],
  "log":       "free-text narrative: what was searched, what failed, what remains"
}
```

## Claim (the unit of evidence)

Every factual statement is a claim with its own confidence.

```json
{ "value": "...", "conf": "A|B|C|D", "src": ["s1","s2"], "page": "p. 14, Table 3",
  "basis": "oem_spec|oem_drawing|distributor|surplus_listing|photo|field_measurement|inference",
  "note": "optional qualifier" }
```

Confidence:
* **A — OEM Verified**: explicitly stated in a manufacturer document (cite page).
* **B — Strongly Corroborated**: multiple independent credible non-OEM sources agree.
* **C — Tentative**: one non-OEM source, or plausible but incomplete.
* **D — Unverified**: lead / hearsay / inference needing investigation.

Rules: a distributor listing alone is at most **C** for compatibility. Matching
dimensions never prove electrical interchangeability. Never invent values; put
gaps in `unknowns`.

## Source

```json
{ "key": "s1", "title": "Exact document title", "publisher": "Eaton",
  "doc_number": "IL 29C107", "date": "2014-03", "url": "https://...",
  "type": "oem_catalog|oem_instruction|oem_drawing|oem_bulletin|oem_web|oem_renewal_parts|distributor|surplus|forum|archive|other",
  "accessed": "YYYY-MM-DD", "access_status": "ok|blocked|404|paywalled|not_found",
  "local_file": "docs/library/... (if downloaded)", "notes": "" }
```

## Family (panelboard / switchboard / loadcenter / breaker-carrier equipment)

```json
{ "key": "f1", "mfr": "EAT", "brand_markings": ["Westinghouse","Cutler-Hammer","Eaton"],
  "name": "Pow-R-Line 1a", "code": "PRL1A", "aliases": ["PRL1a","PRL-1A"],
  "equipment_type": "panelboard|switchboard|loadcenter|busway|other",
  "era": {Claim}, "status": {Claim}, "successor": {Claim},
  "voltage_rating": {Claim}, "main_ampacity": {Claim}, "branch_breakers": {Claim},
  "overview": "2-6 sentence engineering overview",
  "claims": { "<field>": {Claim} },
  "source_keys": ["s1"] }
```

## BreakerFamily

```json
{ "key": "b1", "mfr": "EAT", "name": "BAB", "aliases": [],
  "mounting": {Claim}, "frame": {Claim}, "poles": {Claim}, "amps": {Claim},
  "voltage": {Claim}, "interrupting": {Claim}, "status": {Claim},
  "used_in_family_keys": ["f1"], "claims": {}, "source_keys": [] }
```

## Part

```json
{ "key": "p1", "mfr": "EAT", "brand_marking": "Cutler-Hammer",
  "oem_part_number": "PRL1AB1",
  "title": "Short descriptive title",
  "component_type": "<see controlled vocabulary>",
  "family_keys": ["f1"],
  "breaker_keys": ["b1"],
  "claims": {
    "oem_part_number":    {Claim},
    "alt_part_numbers":   [{Claim + "relation":"supersedes|superseded_by|equivalent|alias|style_number"}],
    "description":        {Claim},
    "application":        {Claim},   // main | branch | sub-feed | through-feed | accessory
    "breaker_compat":     {Claim},
    "frame":              {Claim},
    "poles":              {Claim},
    "voltage":            {Claim},
    "ampacity":           {Claim},
    "kit_contents":       {Claim},
    "material":           {Claim},
    "finish":             {Claim},
    "dimensions":         {Claim},
    "hole_pattern":       {Claim},
    "fasteners":          {Claim},
    "torque":             {Claim},
    "install_doc":        {Claim},
    "status":             {Claim},   // current | discontinued | superseded | unknown
    "replacement":        {Claim},
    "aftermarket":        {Claim},
    "id_features":        {Claim},   // how to recognise it without a label
    "location":           {Claim}    // where in the equipment it installs
  },
  "requires_part_keys": ["p2"],
  "unknowns": ["dimensions", "material"],
  "questions": ["Is the 1-pole version the same strap as ...?"],
  "source_keys": ["s1"] }
```

Omit claim fields with no evidence (list them in `unknowns`).

### component_type vocabulary
`branch-connector-kit, main-breaker-kit, main-lug-kit, sub-feed-lug-kit, through-feed-lug-kit,
lug, lug-kit, connector-strap, busbar, bus-assembly, neutral-assembly, ground-bar, interior,
mounting-bracket, mounting-rail, standoff, insulator, barrier, deadfront, filler-plate, trim,
box/enclosure, hardware-kit, fastener, breaker-accessory, handle-lock, padlock-attachment,
breaker-mounting-kit, conversion-kit, spd-kit, meter-kit, other`

## Lead

```json
{ "priority": 1-5 (1 = highest), "topic": "...", "detail": "...",
  "doc_numbers": [], "urls": [] }
```

## Manufacturer codes (lineage groups)

| Code | Lineage |
|------|---------|
| EAT | Eaton, Cutler-Hammer, Westinghouse (distribution), Challenger, Bryant, Crouse-Hinds (dist.), Moeller |
| SQD | Schneider Electric, Square D, Federal Pioneer (Canada) |
| GEA | General Electric Industrial Solutions, ABB (post-2018), ReliaGear |
| SIE | Siemens, ITE, ITE Imperial, Gould, Murray, Bulldog Pushmatic |
| FPE | Federal Pacific Electric (Stab-Lok, NE/NF/NH panelboards) |
| ZIN | Zinsco, GTE-Sylvania, Sylvania |
| ABB | ABB pre-GE heritage (non-GE lines) |
| OTH | Other / unassigned |
