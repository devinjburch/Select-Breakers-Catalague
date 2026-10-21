# Project Research Log

Chronological, human-maintained summary of research sessions. Per-batch narratives written by
the researchers are in `research/log/<batch>.md`; generated statistics are in
`research/RESEARCH_REGISTER.md`; open work is in `research/BACKLOG.md`.

## Session 1 — 2026-10-21

### Foundation
* Designed the claim-level evidence model (`schema/INCOMING_FORMAT.md`), permanent ID scheme,
  merge/validate/build toolchain, and the PDF generator (indexed and hyperlinked, with generic
  identification schematics).
* Environment constraints: www.eaton.com timed out, and se.com / download.se.com /
  library.e.abb.com returned 403 to automated fetches. Distributor-hosted copies of OEM PDFs
  (USESI, Elliott, Coburn's, IPS, Carbon Controls, etc.) were used instead and recorded as mirror URLs.

### Batches merged
| Batch | Scope | Result |
|---|---|---|
| B0001 | Eaton Pow-R-Line PRL1a/2a/3a/3E/4, Xpert 1X-4X, vintage PRL1/2/3 | 422 parts from RP01400001E (2009/2017/2021) and RP01414001E |
| B0002 | Eaton switchboards (PRLC, WF/WRP, ES, PRLi, CS, IFS), CDP/FDP, BR | 38 new + 89 updated; Volume 12 CA08100014E; PRLC kit numbers not public |
| B0004 | Square D QED-2, QMB/QMJ, I-Line distribution hardware | 176 parts; 2700CT1101, 4620CT9601, 2110CT9701 |
| B0005 | GE A-Series, Spectra, SCP+, CCB/QMR, ReliaGear | 280 parts; BuyLog Sec. 11; DEH40150-40158; "APN" resolved = Spectra plug-in interior type |
| B0006 | Siemens P1 (original/revised), P2-P5, S1/S2, SE, CDP6/FC/SB | 244 parts; SPEEDFAX Sec. 11 (2021), 2005 price list |
| B0007 | Eaton Series C/G and Square D breaker terminal kits | 381 parts; CA08101001E Tab 12 (2008), 0611CT1001, Digest Sec. 3 |
| B0008 | GE and Siemens breaker terminal kits | 184 parts; BuyLog Sec. 6 (2019), SPEEDFAX Sec. 7 (2017-2020) |
| B0009 | FPE, Zinsco/Sylvania, Challenger, Murray, Pushmatic, minor makers | 152 parts; Eaton CH/BR retrofit-kit guide; mostly class C/D compatibility |

### Data-quality incidents and corrections
* B0001 listed "Pow-R-Line C" as a PRL1a alias, and the family merge folded PRL1a into the PRLC
  switchboard. Fix: families with different explicit codes never merge on shared aliases;
  the alias was removed with an explanatory note.
* Breaker-family alias matching merged distinct frames (e.g. Eaton FD into an EHD group, Square D
  KA into I-Limiter). Fix: breaker families now match on exact name only. All batches were
  re-merged from the archive (IDs were reassigned before any publication; this is the baseline
  ID set from commit e22940e onward).
* A batch that was still being written was merged by mistake, then reverted. `merge.py` now
  requires explicit batch files (or `--all`).
* A third-party mirror page (novapart) contained text addressed to AI assistants. The researcher
  ignored it; only the OEM PDF content was used.

### In progress / next
* B0003 Square D NQ/NF/I-Line panelboards, B0010 and B0011 (instruction-leaflet hunts for
  dimensions and torque), B0012 (archival legacy lines).
* Biggest systematic gap: dimensions, hole patterns, materials and torque. Renewal-parts guides
  rarely give these, and kit instruction leaflets are the target. See BACKLOG priority 1.
