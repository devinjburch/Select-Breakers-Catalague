# Research log — B0006-siemens-ite

* Date: 2026-10-21
* Researcher: Claude Code research agent (Opus) - web + PDF extraction session
* Scope: Siemens / ITE / Gould panelboards and switchboards: P1 (original & Revised), S1/S2/SE legacy, P2, P3, P4/S4/SPP, P5/S5, SB1/SB2/SB3, Series 5/6 CDP/VB/FC20/FCI/FCII. Branch strap/connector kits, main/subfeed strap kits, main & feed-thru lug kits, neutral kits, filler/blank plates, deadfront parts, SEB barriers, provision hardware.
* Merge stats: {'sources_new': 15, 'families_new': 10, 'breakers_new': 15, 'parts_new': 244, 'parts_updated': 0, 'leads_new': 9, 'docs_filed': 0, 'batch': 'B0006-siemens-ite'}

## Narrative

B0006-siemens-ite research log (2026-10-21).
FOUND: Siemens SPEEDFAX Section 11 Panelboards (06/2021, 132 pp, distributor-hosted DDS mirror) - the core source: Revised P1 kit tables (p.11-13/14), Original P1 / S1-S2-SE legacy kit table (p.11-15), P1 spare parts + deadfront filler chart (p.11-20..23), P2/P3 spare parts (p.11-53/54, 11-66/67), P4 strap kits (p.11-96), P5 strap kits (p.11-110). Siemens Canada Section 11 Switchboards (2025): SB1/SB2/SB3 strap kit table (p.11-5), provision kits/nut keepers/6FPB blanks (p.11-14), CSA Series 6 strap kits (p.11-15). 2005 Siemens EDP price list p.8-13 (USESI mirror): Series 5/6 CDP / FC20 / FCI / FCII / SB strap kits 'for switchboards manufactured since 1974' with list prices. Also SpeedFax 2007-08 P1 pages, P1 & P3 data sheets, Revised P1 flyer, NextGen P1 brochure (Canada), MBKBFA data sheet, 2016 Panelboards Selection & Application Guide (only grep-checked).
METHOD: pdftotext -layout; whole kit tables transcribed. All OEM-table values are conf A with page refs. Distributor-only facts (search summaries) at C.
NOT FOUND / FAILED: stoneway.com MBKQR3 spec sheet returned HTML (deleted). steinerelectric DFFP01A datasheet 404/no file. No ITE / Gould-ITE / ITE Imperial panelboard catalogue or renewal parts list located; legacy ITE types named in scope (NQB, NLAB, NHB, EQ panelboard, 'Imperial') remain unconfirmed - no records created for them. No US SpeedFax Section 12 (switchboards p.12-32). No installation instructions (dimensions, torque, materials largely unknown).
NOTES/CONFLICTS: Revised P1 introduction date 2014 vs 2015 inside the same SpeedFax; P5 table maps SJD to SCJD whereas SB table gives SSJ1D; MG1D mapped to 'NM, HM, LM' in 2005 list vs 'VL MG' in SpeedFax; distributor SBL descriptions inconsistent. Canadian strap kits: base number = aluminum connectors, suffix C = copper (several copper-only) - merged as aliases of US/2005 numbers where the base existed. Original P1 kits fit 250A-max S1/S2; SMBK* kits for 400/600A S1/S2 and all SE; Revised P1 kits fit neither.
SCOPE: ~200 records exceeds the 150 target because full kit tables were transcribed (per brief: 'work through entire kit tables'); with-breaker factory kits, SMM kits, fusible kits, number strips/locks deferred to leads.
