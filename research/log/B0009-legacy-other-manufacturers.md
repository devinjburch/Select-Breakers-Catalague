# Research log — B0009-legacy-other-manufacturers

* Date: 2026-10-21
* Researcher: agent/Claude Code research subagent (web search + distributor catalog JSON extraction)
* Scope: Obsolete commercial/industrial panelboards & switchboards outside the big-four lineages (FPE, Zinsco/Sylvania/Challenger, Murray, Bulldog Pushmatic, Trumbull, Frank Adam, Wadsworth, Commander, Kinney, etc.) and their mounting hardware, kits, replacement interiors and aftermarket replacement parts.
* Merge stats: {'sources_new': 39, 'families_new': 18, 'breakers_new': 14, 'parts_new': 152, 'parts_updated': 1, 'leads_new': 14, 'docs_filed': 0, 'batch': 'B0009-legacy-other-manufacturers'}

## Narrative

Searched web (WebSearch) for FPE commercial panelboards/kits, Zinsco/Sylvania commercial, Pushmatic, Murray, Trumbull, Frank Adam, Wadsworth, Commander, Kinney, NLAB, retrofit interiors.
Key finds: (1) Breaker King FPE kit listings giving explicit 'replaces OEM KCDP1C..KCDP4C / KBDP1C, KBDP2C, KBDP4C' cross references to PCS aftermarket kits; (2) relectric FPE/Zinsco/Sylvania/Challenger/Frank Adams accessory catalogues (FPE KFDP/KQB/NDP/NAIB kits, NM lugs; Zinsco DSL*/QSF*DS kits; Sylvania SEHT/SECT/SJD4T/SKM8S/QSF*SB; Challenger C?D?K kits); (3) Superbreakers Shopify products.json for FPE (639 items), Zinsco, Sylvania, Murray, Wadsworth - machine-read for kit descriptions and ratings; (4) OEM document: Eaton/Cutler-Hammer 'Retrofit Kits Type CH and BR' selection guide (10 pp, mirrored by InspectAPedia, downloaded to docs/library/_incoming/B0009-legacy-other-manufacturers/CHRetrofitGuide.pdf) - ~60 retrofit kit catalog numbers recorded at conf A; (5) histories from Wikipedia (FPE, Zinsco), fpeparts.com (Circuit Breaker Sales), InspectAPedia.
No original FPE/Zinsco/Sylvania OEM catalogue or renewal-parts list was found, so all FPE/Zinsco/Sylvania/Challenger kit compatibility is conf C (distributor/surplus) or D (inference from numbering).
Blocked/failed: se.com FAQs (403), Mike Holt forums (403 on fetch; used search summaries), jrlelectricsupplyinc (429), Breaker King obsolete-book PDF (served HTML), fpeparts.com products.html (404).
Not covered / thin: Westinghouse NLAB, Kingsbury, Powell, Crouse-Hinds commercial, Trumbull hardware, Murray commercial panelboards, Pushmatic 3-phase hardware. QMQB/QSF switch units, breakers themselves and residential Stab-Lok items were recorded at breaker-family level rather than as parts (except accessories).
Mfr coding: Challenger kits coded EAT and Trumbull GEA per lineage table; Eaton retrofit kits coded EAT; Connecticut Electric UBIZRBK12 coded ZIN (fits Zinsco) with brand_marking Connecticut Electric/UBI.
