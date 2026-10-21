# Research Backlog

_Generated from data/leads.json by tools/build_db.py. Close a lead by setting its status in data/leads.json._

## Priority 1

* **LEAD-0001 — Eaton instruction leaflets for KB/KL/KPRL3/KPRL4 kits** (B0001-eaton-prl-panelboards)  
  Renewal-parts guides give catalog numbers and compatibility but no kit drawings, torque values, strap dimensions or hole patterns. Each kit ships with instructions (IL/IB numbers not cited in the guides). Search Eaton document library for IL numbers packed with KPRL4X32, KPRL3AFD3, KB13AFT, KL23AMS, PRLSEBFD.
* **LEAD-0002 — Supersession mapping 2017 -> 2021 (PRL4 KPRL4FD/FD1/FD2/ED/ED2/LD; PRL1a/2a deadfronts 4180B03/4180B61/4180B05; PRL3a covers 4176B68/4180B93/4178B08/4179B39-42; filler 4178B06H01)** (B0001-eaton-prl-panelboards)  
  April 2021 edition replaced these numbers with KPRL4X12/X22/X32/LC and 42C80xx covers (same table rows). Distributor text says 4178B06H01 is for panels built before April 2019 and 42C8083H01 after - implies a chassis change, so old and new are probably NOT interchangeable. Confirm with Eaton Sumter aftermarket (803-481-6677) or a December 2020 edition of RP01400001E.  
  Docs: RP01400001E  
  URLs: https://rexelusa.com/p/120408/eaton/panel-board-prl3a-cover-filler-plate-1p-for-f-frame-breakers/786685467672/4178b06h01
* **LEAD-0014 — Pow-R-Line C switchboard branch provision / connector kit catalog numbers** (B0002-eaton-switchboards-legacy)  
  Vol 12 p. V12-T15-5 says provisions/connectors are available for all PRLC ratings, but no catalog numbers are public. Obtain the PRLC distribution chassis renewal-parts/price list (Sumter) or a PRLC field-installation IL for adding group-mounted FD/JD/KD/LD/MDL/ND devices; confirm whether KPRL4/KPRL4X kits are the same parts.  
  Docs: IM01500001E, CA08100003E Tab 4  
  URLs: https://www.eaton.com/content/dam/eaton/products/low-voltage-power-distribution-controls-systems/switchboards/pow-r-line-switchboard-manual-im01500001e.pdf
* **LEAD-0015 — WF/WRP switchboard distribution-section connector and retrofit kits** (B0002-eaton-switchboards-legacy)  
  RP01400002E p.20 lists 'Retrofit kits for WF and WRP distribution sections' and 'Connector kits for WF and WRP distribution sections' from Sumter but gives no numbers. Check whether KCDP/KFDP kits are used, since WF/WRP feeders were CDP-type breakers and FDP switches.  
  Docs: RP01400002E, PL01400002E
* **LEAD-0025 — 2700CT1601 OEM QED-2 I-Line interiors catalog** (B0004-squared-switchboards)  
  Contains single/double-row OEM interior selection tables (CF... numbers), likely end closures, splice/main lug kits. Blocked by Akamai (productinfo.se.com, download.se.com 403). Try a distributor mirror (media.distributordatasolutions.com), Rexel/Graybar spec-sheet links, or a browser session.  
  Docs: 2700CT1601  
  URLs: https://www.productinfo.schneider-electric.com/power_style_qed_2/2700ct1601-oem-qed-2-switchboard-i-linetm-interiors-catalog/English/2700CT1601.pdf
* **LEAD-0026 — QED-2 instruction bulletin 80043-055-16 (2024) and -13 (2018)** (B0004-squared-switchboards)  
  Handling, assembly, splice (through-bus) and torque data for QED-2; likely gives splice plate hardware and torque values. Blocked.  
  Docs: 80043-055-16, 80043-055-13  
  URLs: https://www.productinfo.schneider-electric.com/power_style_qed_2/80043-055-power-style-qed-2-switchboards-instruction-bulletin/English/80043-055-016_en.pdf
* **LEAD-0027 — OEM interiors IB 80235-597-09** (B0004-squared-switchboards)  
  Schneider FAQ cites IB 80235-597-09 for single/double-row OEM I-Line interiors.  
  Docs: 80235-597-09
* **LEAD-0038 — Current ABB BuyLog Section 11 (2021/2022) - ReliaGear neXT kit numbers and Spectra retrofit kits** (B0005-ge-abb)  
  Contains ReliaGear neXT catalog nomenclature, single breaker-installation-kit catalog number, 'Retrofit kit for Spectra panelboards' and 'Spectra (obsoleted) bolt-on mounting hardware'. Host electrification.us.abb.com returns 503/empty reply from this container; try another network or distributor mirror.  
  Docs: BuyLog Section 11 (ABB)  
  URLs: https://electrification.us.abb.com/catalog/buylog/11_BuyLog_Panelboards.pdf https://electrification.us.abb.com/products/panelboards/reliagear-oem-next-power-panelboards
* **LEAD-0039 — Spectra bolt-on strap instruction leaflets DEH-047, DEH-059, DEH-060, DEH-061, DEH-062 and DEH042 cover supports** (B0005-ge-abb)  
  Would give strap part numbers, kit contents and torques for AMCB EB/SE, SF, SG, SK/KM and EY kits, plus cover-support catalog numbers by panel width. Copies exist on manualmachine.com (HTTP 403 here) - e.g. DEH061 AMCB3KM/AMCB2KM, DEH042 SE/SF/TE/TF/TQ/TEL cover supports, AMCB4GB/AMCB6GB, AMCB2GM/AMCB3GM.  
  Docs: DEH-047, DEH-059, DEH-060, DEH-061, DEH-062, DEH042  
  URLs: https://manualmachine.com/ge/amcb3km/12960805-user-manual/ https://manualmachine.com/ge/tq/12960839-user-manual/ https://manualmachine.com/ge/amcb4gb/1574529-user-manual/ https://manualmachine.com/ge/amcb2gm/1574305-user-manual/
* **LEAD-0047 — Legacy ITE / Gould-ITE lighting panelboard renewal parts (pre-Siemens S1/S2)** (B0006-siemens-ite)  
  No OEM ITE, ITE Imperial or Gould-ITE panelboard renewal-parts catalogue was found online. Type designations in the scope (ITE NQB/NLAB/NHB, EQ panelboards, 'CDP' early series) were NOT confirmed in any document reached. Need scanned ITE 'Distribution Products' catalogues (1960s-1980s) or Siemens-Allis price lists; try archive.org, worldradiohistory, eBay catalogue scans, and Siemens legacy support (1-800-333-7421).  
  URLs: https://forums.mikeholt.com/goto/post?id=1425085
* **LEAD-0048 — SpeedFax Section 12 (Switchboards) page 12-32 branch device mounting kits** (B0006-siemens-ite)  
  SpeedFax Sec.11 p.11-15 says: 'For Series 5, Series 6, CDP6 and VB6 panels as well as FC20, FCI, FCII, SB1, SB2 and SB3 distribution switchboards, see page 12-32 for branch device mounting kits.' US Section 12 PDF not retrieved; try media.distributordatasolutions.com siemenscomplete documents or usa.siemens.com/speedfax.  
  Docs: SPEEDFAX Section 12 p.12-32
* **LEAD-0056 — Current Eaton Volume 4 Tab 2 (CA08100005E) terminal and accessory tables** (B0007-breaker-terminal-kits-eaton-squared)  
  eaton.com blocked from container. Needed to confirm newer interphase barrier numbering (IPB2 vs IPB3), J-frame shield line/load, TA350K 350 vs 400 A, 3T225FD and 3TA150FB, K-frame keeper nut pack size, and status/supersessions.  
  Docs: CA08100005E  
  URLs: https://www.eaton.com/content/dam/eaton/products/electrical-circuit-protection/molded-case-circuit-breakers/mccb-catalog-v4-t2-ca08100005e.pdf
* **LEAD-0057 — Square D PowerPact M/P/R catalog lug tables** (B0007-breaker-terminal-kits-eaton-squared)  
  Need OEM tables for AL800M23K, AL800P6K, AL800P7K, AL1200P25K, CU800M..., R-frame lugs; only tapped versions (…TK) found in Digest.  
  Docs: 0612CT0101
* **LEAD-0070 — FPE OEM panelboard catalog / renewal parts list** (B0009-legacy-other-manufacturers)  
  Find original Federal Pacific (or American Circuit Breaker / Federal Pacific Equipment) panelboard catalog giving CDP/BDP/NDP/FDP/NA1B/NH1B/NBLP definitions and the KCDP/KBDP/KFDP/KQB kit tables with breaker compatibility, dimensions and bus details. Circuit Breaker Sales (Matthews NC, 704-882-1875) holds FPE technical documents per fpeparts.com.  
  URLs: https://fpeparts.com/pages/fpe-panelboard.html https://fpeparts.com/pages/history.html
* **LEAD-0071 — Confirm KBDP3C frame and KCDP5C/KBDP5C ratings** (B0009-legacy-other-manufacturers)  
  Numbering pattern (1=NE/NEF, 2=NEJ, 3=NFJ, 4=NJL, 5=NM) is inferred; Superbreakers gives 225 A for KCDP5C (NM/NN) which looks wrong.
* **LEAD-0074 — Eaton CH/BR retrofit kits current status** (B0009-legacy-other-manufacturers)  
  Verify whether RACH*/RBCH*/RCCH*/RDCH*/RABR*/RBBR*/RCBR*/RDBR*/REBR*/RAABR* kit numbers are still orderable (Lincoln Flex Center 800-330-6479) and find the original Eaton publication number/date; look for 480Y/277 V retrofit (PRL-based) offerings and Square D/Siemens equivalents.  
  URLs: https://inspectapedia.com/fpe/CHRetrofitGuide.pdf
* **LEAD-0084 — NQOD / NEHB legacy kit part numbers** (B0003-squared-panelboards)  
  No OEM table of NQOD main breaker kits (bulletin 80043-699-03 covers a 250 A NQOD main kit but prints no catalog number), NQOD neutral/lug kits or NEHB kits found. Search Supplemental and Obsolescence Digest (Digest Plus 'Supplemental and Obsolescence Digest') and older Digest 170-175 PDFs for NQOD/NEHB accessory tables.  
  Docs: 80043-699-03, 80043-687-03  
  URLs: https://productinfo.se.com/nadigest/
* **LEAD-0085 — SKNQOD225 finger part numbers for reproduction** (B0003-squared-panelboards)  
  OEM FAQ FA124209 gives component numbers 80110-005-01 (A/C finger), 80110-006-01 (B finger), 80025-068-01 (screw). Obtain drawings/dimensions; check whether a 400 A NQOD connector kit existed.  
  URLs: https://www.se.com/us/en/faqs/FA124209
* **LEAD-0095 — Eaton RP01400003E - Vintage Cutler-Hammer panelboards and switchboards renewal parts (MP40, MP-200, PB, PH, PH-L, EP, EE)** (B0012-archival-legacy-panelboards)  
  Primary kit tables for MP40/MP2/PH/EE/EP. eaton.com blocked from container (HTTP/2 error, empty reply); usermanual.wiki mirror redirects to manuals.plus captcha; Wayback unreachable. Try from a normal browser or ask Eaton Sumter Aftermarket Center (803-481-6677 per search snippet).  
  Docs: RP01400003E  
  URLs: https://www.eaton.com/content/dam/eaton/products/low-voltage-power-distribution-controls-systems/panelboards/eaton-vintage-cutler-hammer-swithboard-panelboard-rp01400003e-en-us.pdf https://usermanual.wiki/Pdf/152612Attachmenturl.613627626.pdf
* **LEAD-0096 — Eaton PL01400003E - Vintage Cutler-Hammer price list (Jan 2008)** (B0012-archival-legacy-panelboards)  
  Gives the OEM catalog numbers for MP40 retrofit kits ('KMP40...' pattern per snippet), PH cover plates/deadfront kits/trim lock, neutral assemblies, ground bars. Wesco copy 403, Carlton-Bates behind Cloudflare.  
  Docs: PL01400003E  
  URLs: https://buy.wesco.com/static/catalog/products/images/PDF/EATON_pl01400003e.pdf https://carltonbates.com/static/catalog/products/images/PDF/EATON_pl01400003e.pdf
* **LEAD-0097 — GE GEJ-3006A / GEG-13610B scan (archive.org, access-restricted)** (B0012-archival-legacy-panelboards)  
  Borrow/view the scanned pages to confirm part-number-to-row mapping for bus supports and lugs, and capture remaining rows (blank filler 1X, screw assembly use, any interior/bus parts).  
  Docs: GEJ-3006A, GEG-13610B  
  URLs: https://archive.org/details/General_Electric_Circuit_Breaker_Panelboard_GEJ_3006A_
* **LEAD-0107 — QED-2 IB 80043-055 torque tables (exact row pairing)** (B0011-docs-ge-squared)  
  Section 9 tables (printed pp.51-52 of -13; pp.53-54 of -12) read only through ManualsLib text rendering; hardware-type to torque pairing ambiguous. Get the PDF (productinfo.se.com / download.se.com 403; Scribd copy 881634201 JS-only) and re-transcribe Tables 6-8; also capture through-bus splice bolt size/grade (shipping-split instructions) and Qwik-Flange busway hardware.  
  Docs: 80043-055-12, 80043-055-13, 80043-055-16  
  URLs: https://www.manualslib.com/manual/1766524/Square-Qed-2.html https://www.scribd.com/document/881634201/80043-055-16
* **LEAD-0108 — 2700CT1601 OEM QED-2 I-Line interiors catalog and IB 80235-597-09** (B0011-docs-ge-squared)  
  Still blocked (productinfo.se.com 403). Schneider STEP-model pages (se.com/us/en/download/document/<CF...>UMS-03) are readable by WebFetch and give interior titles, e.g. CF16KF63C = 1600A 63H double-row centre-feed copper; could be used to decode the CF nomenclature for all OEM interiors.  
  Docs: 2700CT1601, 80235-597-09, CF16KF63C117UMS-03  
  URLs: https://www.se.com/us/en/download/document/CF16KF63C117UMS-03
* **LEAD-0120 — Siemens instruction-sheet bucket (remaining sheets)** (B0010-docs-eaton-siemens)  
  Public S3 bucket dcc-data-extract 'Compas/Instruction Sheet Quick Guide' holds ~1,290 Siemens SIE_IS_* sheets; this batch processed panelboard/switchboard kit sheets only. Not yet processed: MCCB terminal/lug kits (TA*/TC* lug sheets, e.g. SIE_IS_JD-LD_Distribution-Lug, SIE_IS_FD_Compression-Lug), Vacu-Break/HCP switch kits, PowerMod/meter-stack kits (reppartsspdfax: GMBC1/2, MMCVR1, MMBMT1, MMSCK1, MMPK11/13), MG1/SMND/NG1D image sheets, F672/F6162D fusible kits.  
  URLs: https://s3.amazonaws.com/dcc-data-extract?list-type=2&prefix=new-delta/asset/Compas/daily/Compas/Instruction%20Sheet%20Quick%20Guide/SIE_IS
* **LEAD-0123 — Eaton classified breaker compatibility chart / brochure BR003034EN and whitepaper WP003005EN** (B0016-aftermarket-retrofit)  
  Eaton CL/CLCAF/CLGF/CLDF classified breakers: obtain the official load-centre catalog-number compatibility chart (eaton.com unreachable from container). Needed for an authoritative classified cross-reference table.  
  Docs: BR003034EN, WP003005EN, 5651B63SH09  
  URLs: https://www.eaton.com/content/dam/eaton/products/low-voltage-power-distribution-controls-systems/circuit-breakers/classified-circuit-breakers/eaton-classified-breaker-brochure-br003034en.pdf
* **LEAD-0124 — Identify 'PCS' maker of Breaker King aftermarket panelboard kits** (B0016-aftermarket-retrofit)  
  Breaker King labels many kits '(PCS) Aftermarket Assembly' / 'Provided as PCS Brand Aftermarket Kit' with PCS kit numbers (NEF1K, FD3K, ED4K, SED1K, ED65K ...). Identify PCS, obtain drawings/material specs and any test/listing basis. Remaining Breaker King pages not captured: Westinghouse page 1 items BCDPFW/BCDPJW/BCDPKW/BCDPKLW (no OEM xref), GE A-Series II 'unspecified/specified space' kits (BASPP...) without OEM xref.  
  URLs: https://www.breakerking.com/catalog/index.php?main_page=index&cPath=4_187

## Priority 2

* **LEAD-0003 — RP.38F.01.T.E (February 2000) Cutler-Hammer panelboard renewal parts** (B0001-eaton-prl-panelboards)  
  Predecessor of RP01400001E; would cover earlier PRL1a/2a/3a/4B part numbers and possibly vintage PRL1/2/3 connector straps. Not found online.  
  Docs: RP.38F.01.T.E
* **LEAD-0004 — RP01400002E April 2009 edition and PL01400002E price list** (B0001-eaton-prl-panelboards)  
  Earlier vintage-Westinghouse renewal parts edition and price list referenced by Feb 2013 edition.  
  Docs: RP01400002E, PL01400002E, PL01400001E
* **LEAD-0005 — Drawings 42c8083.pdf etc. on Rexel** (B0001-eaton-prl-panelboards)  
  Rexel product page for 42C8083H01 links a drawing file '42c8083.pdf' (not opened). Similar drawing links may exist for other 42C80xx/4176Bxx covers - source of dimensions/hole patterns.  
  URLs: https://www.rexelusa.com/p/2273430/eaton/filler-plate-panelboard-prl3a-for-panelboards-built-after-april-2019/42c8083h01
* **LEAD-0006 — KPRL4LFD3 (distributor: 'CON KIT FD+LFD PRL4')** (B0001-eaton-prl-panelboards)  
  Dixon Electric (Canada) lists Eaton KPRL4LFD3; not in any OEM table found (2021 table lists FD/LFD under KPRL4FBP). Redirect to dixon.ca not followed.  
  URLs: https://dixon.ca/products/20-power-distribution/08-panelboards/05-panelboard-parts-accessories/p-Q1VIS1BSTDRMRkQz-eaton-kprl4lfd3-con-kit-fdlfd-prl4
* **LEAD-0007 — Pow-R-Xpress PRL4X branch fillers PRXP4PD34FILL, PRXP4PD2FILL1 and P44X25** (B0001-eaton-prl-panelboards)  
  Distributor-only numbers for PRL4X fillers and PRL4 4X blank cover (P44X25). Relationship to OEM 6554C0x not established.  
  URLs: https://www.elliottelectric.com/Media/P44X25-CHS https://www.gexpro.com/p/2925374/eaton/prl4x-pd2-1-pole-filler/786689814915/prxp4pd2fill1
* **LEAD-0016 — Price list PL01400002E (CDP/HCDP, FDP, PRL1-LX, PRL1, PRL2, PRL3) and PL01400001E** (B0002-eaton-switchboards-legacy)  
  Price lists would confirm full catalog-number sets (e.g. all KCDP retrofit permutations, KCDPnX fillers) and current availability.  
  Docs: PL01400002E, PL01400001E
* **LEAD-0017 — RP01400003E renewal parts for Cutler-Hammer MP40, MP-200, PB, PH, PH-L, EP, EE panelboards** (B0002-eaton-switchboards-legacy)  
  Referenced in Vol 12 Tab 4 for branch-device retrofit kits for Cutler-Hammer legacy panelboards (also plug-in power panels/switchboards EE/EP). Not retrieved.  
  Docs: RP01400003E, PL01400003E
* **LEAD-0018 — RP01414001E Panelboard Renewal Parts Supplement** (B0002-eaton-switchboards-legacy)  
  Referenced with RP01400001E in Vol 12 Tab 4 pp. V12-T4-15..19. Not found.  
  Docs: RP01414001E
* **LEAD-0019 — PRL4 kit renumbering 2017 -> 2022 (KPRL4FD/ED/LD/MC/ND -> KPRL4X32/X22/LC/X34/X35)** (B0002-eaton-switchboards-legacy)  
  Comparison of RP01400001E Oct 2017 Table 37 and May 2022 Tables 46-47 suggests renumbering with Pow-R-Line Xpert (PD2-PD5 frames). Need explicit OEM supersession statement (April 2021 / Dec 2020 editions, Eaton product pages).  
  Docs: RP01400001E  
  URLs: https://eatonarabia.com/wp-content/uploads/2022/03/pow-r-line-1.pdf
* **LEAD-0028 — Data Bulletin 0600DB1004 I-Line plug-on connection design** (B0004-squared-switchboards)  
  Jaw design, bolt-on clamp details, I-Line busway/switchgear connections.  
  Docs: 0600DB1004  
  URLs: https://www.se.com/us/en/download/document/0600DB1004
* **LEAD-0029 — Current 2700CT1101 (v02, 2025-12, 140 MB) and 2110CT9701 v2.1 (2025-02)** (B0004-squared-switchboards)  
  Newer revisions may add QED-2 Series 2 changes (QMB 63 in. only) and accessory tables. Only 2012 and 2019 editions retrieved.  
  Docs: 2700CT1101, 2110CT9701  
  URLs: https://www.se.com/us/en/download/document/2110CT9701
* **LEAD-0030 — Legacy QMB replacement attachment 'QMB Replacements.pdf' and Supplemental Digest** (B0004-squared-switchboards)  
  Several se.com FAQs reference an attached QMB Replacements.pdf and the Supplemental Digest for QMB3400LA/QMB3300LA and EX/LEX extension kits. Would give full legacy cross-reference table.  
  URLs: https://www.se.com/us/en/faqs/FA123288 https://www.se.com/us/en/faqs/FA87289
* **LEAD-0031 — Unverified FAQs FA123288, FA87289, FA99653** (B0004-squared-switchboards)  
  QMB3640, QMB303T and QMB306T replacement answers seen only in search summaries (rate-limited 403). Re-fetch to upgrade s36 claims to A.  
  Docs: FA123288, FA87289, FA99653
* **LEAD-0040 — Spectra plug-in module instructions GEH-5623/5624/5625/5626/5643/5673/5675/5677 and hardware kits GEH-5913** (B0005-ge-abb)  
  Module-level torques and bus-clip part numbers; GEH-5913 should confirm AHK/AHKB kit contents and the module-to-AHK mapping (PDF text column alignment on BuyLog p.11-44 is ambiguous).  
  Docs: GEH-5623, GEH-5624, GEH-5625, GEH-5626, GEH-5643, GEH-5673, GEH-5675, GEH-5677, GEH-5913
* **LEAD-0041 — GEH5589 APN/APNB interiors installation** (B0005-ge-abb)  
  Install of Spectra interiors into APB boxes; listed on manualmachine (blocked).  
  Docs: GEH5589  
  URLs: https://manualmachine.com/ge/apnb/12960816-user-manual/
* **LEAD-0042 — Main lug kit instructions GEH-5588 / GEH-5630 and AMB-numbered main lug kits (p.11-28)** (B0005-ge-abb)  
  BuyLog p.11-28 lists a second main-lug numbering (AMB3600MAF, AMB3120MAF, AMB3120DMAF, AMB3250CAF, AMB3600CAF, AMB3800CAF, AMB3120CAF, AMB3120NF, cover plates AFPML4X/6X/6XW) apparently for factory-installed/merchandise panels; relationship to AML modules (p.11-45) unresolved. Not yet catalogued as parts.  
  Docs: GEH-5588, GEH-5630
* **LEAD-0043 — Spectra ANK neutral kit full table (p.11-27) and ADS switch load bases 331A1519Gxx / 331A1545Gx / 331A1543G1** (B0005-ge-abb)  
  About 70 ANK/ANKT neutral kit numbers by box width/main config and ~30 ADS load base renewal numbers are in the BuyLog but were not individually catalogued in this batch.  
  Docs: BuyLog p.11-27, BuyLog p.11-44
* **LEAD-0049 — Installation instructions for P1/P2/P3/P4/P5 strap kits** (B0006-siemens-ite)  
  SpeedFax references Installation Instructions for S3VA41T(D) accommodating xGB/xGB2, and drawing refs (11-D-2267-01 BBKB32, 11-D-2894-01 BBKVA5262P2S, 11-A-2010-01 P1SCRWS, etc.). Siemens SIOS (support.industry.siemens.com) likely hosts these as PDFs; search by kit number. Needed for torque, fastener and dimension data (currently unknown for nearly all parts).  
  Docs: 11-D-2267-01, 11-D-2894-01, 11-D-2895-61, 13-D-2011-13, 11-D-2572-02, 11-D-2573-01, 11-D-2573-02  
  URLs: https://support.industry.siemens.com
* **LEAD-0050 — Original P1 / S1 / S2 branch connector replacement parts** (B0006-siemens-ite)  
  2021 SpeedFax lists only Revised P1 branch connectors (P1CONACPHCU, P1CONBPHAL, P1CONBPHCU). Whether these fit original P1 or S1/S2 interiors is not stated (table column marks Revised P1 only). Older SpeedFax editions (2010-2014) should be checked for original P1 connector kits.
* **LEAD-0051 — Revised P1 main breaker kits with breaker (MBK...A with amp rating)** (B0006-siemens-ite)  
  SpeedFax p.11-14 lists ~47 factory kits with breaker included (MBKED3100A, MBKQR1125A..MBKQR3225HA, MBKVAM3150A..MBKVAH3400A, MBKFD3150A..MBKFD3250A, MBKJD1300A..MBKJD32400A). These are referenced in 'replacement' notes on strap-kit records but not catalogued individually in this batch. Canadian equivalents (MBKQR12225A, MBKFD33250A, MBKJD33400A, MBKHF33250A, MBKED33100A) in SI-LP-1633.  
  Docs: SPEEDFAX p.11-14, SI-LP-1633
* **LEAD-0058 — Square D KA/KH lug kit supersession and FY/E-frame/QB-QD-QG-QJ lugs** (B0007-breaker-terminal-kits-eaton-squared)  
  2012 Digest lists AL250KA only against KI; KA/KH lists need older Digest (e.g., Digest 172/173) or instruction bulletins. No E-frame (EDB/EGB/EJB) or Q2/QB lug kits located; 2012 Digest notes threaded insert kit for EDB/EGB/EJB/FJA (table text partly garbled).  
  Docs: Digest 172, Digest 173  
  URLs: https://productinfo.se.com/nadigest/viewer/5cc35b7ed6593c0001ba8661/5cc36299d6593c0001baa72f/r/_SD17711023_65557
* **LEAD-0059 — Square D lug-kit instruction bulletins** (B0007-breaker-terminal-kits-eaton-squared)  
  48940-221-02 (H/J lug kits) and AL100FA4 instructions exist; download blocked (se.com 403). Would give torque values and kit contents.  
  Docs: 48940-221-02  
  URLs: https://www.schneider-electric.us/en/download/document/48940-221-02/
* **LEAD-0060 — Current 0611CT1001 v5.0 (2024) PowerPact H/J/L catalog** (B0007-breaker-terminal-kits-eaton-squared)  
  Verify whether 2013 lug tables (esp. column-scrambled CU L-frame rows in Table 121) changed; check PDC3JD20 vs PDC3JD2.  
  Docs: 0611CT1001  
  URLs: https://www.se.com/us/en/download/document/0611CT1001/
* **LEAD-0063 — GE TCAL28 / TCAL38 / TCAL39 / TCAL51 / TCAL62 not found** (B0008-breaker-terminal-kits-ge-siemens)  
  These numbers appear in the batch scope but are not in the GE BuyLog 2008 excerpt or the 2012, 2013 or 2019 lug tables. TCAL28 may be confused with TCAL28PD1/PD3 (SF power distribution lugs). Older GE lug numbers (TCAL2x/3x for the 1980s-90s TF/TJ lines) may appear in GEP-1100 / GET-xxxx renewal catalogs or older BuyLog editions (pre-2008).  
  Docs: GEP-1100
* **LEAD-0064 — GE footnote digits fused into part numbers** (B0008-breaker-terminal-kits-ge-siemens)  
  The pdftotext extraction of GE BuyLog runs footnote superscripts into part numbers (TCAL1212 = TCAL121 + fn2, TCAL811 = TCAL81 + fn1, TCLK3652 = TCLK365 + fn2, SKLVK6 = SKLVK + fn6, etc.). Base numbers were reconciled across the 2012 and 2019 editions (different footnote numbering). TCAL122, TCALK2122/3122, TCAL91, TCALK291/391, TCAL131 and 789A448G3 are inferred bases (conf B/C). Check them against distributor or ABB product pages.  
  Docs: BuyLog Section 6 Rev 1/19, BuyLog Section 3 Rev 9/12
* **LEAD-0065 — Siemens QJ2 / pre-Sentron ITE lug kits** (B0008-breaker-terminal-kits-ge-siemens)  
  SPEEDFAX 2017/2021 no longer lists QJ2, so the only QJ2 lug found is TA1Q300 (distributor). Old ITE numbers such as TA1D/3TA1D/TA1E/TA1F/TA1G/TA2DS/TA3J6500/TA2P400 were not found in the 2017 tables. Search older SPEEDFAX editions (e.g. SPEEDFAX 2004-2011, Section 7) and ITE 'Breaker Lug Selection' leaflets.  
  Docs: SPEEDFAX 2011 Section 7  
  URLs: https://media.distributordatasolutions.com/springfieldts/2018q4/e0ee4273acd983d79661d7d52bf9db41374e924f.pdf
* **LEAD-0072 — Breaker King / PCS aftermarket FPE kits** (B0009-legacy-other-manufacturers)  
  PCS (manufacturer of NEF1K/NEJ1K/NFJ1K/NJL1K/NEF3K/NEJ3K/NJL3K/NFJ3K) - identify company (Power Circuit Specialists?), obtain installation instructions and confirm listing status.  
  URLs: https://www.breakerking.com/catalog/index.php?main_page=index&cPath=4_187_189
* **LEAD-0073 — Breaker King Obsolete Breaker Guide PDF** (B0009-legacy-other-manufacturers)  
  Linked PDF https://www.breakerking.com/catalog/breaker_king_obsolete_book.pdf returned an HTML page to curl; try browser/WebFetch.  
  URLs: https://www.breakerking.com/catalog/breaker_king_obsolete_book.pdf
* **LEAD-0075 — Square D / Siemens retrofit interiors for FPE and Zinsco** (B0009-legacy-other-manufacturers)  
  Forum posts say Square D (NQ/NF) and Eaton build custom interiors to fit existing enclosures; find Schneider 'retrofit panelboard' or 'replacement interior' literature and any listed-for-enclosure marking practice.  
  URLs: https://forums.mikeholt.com/threads/retrofit-kit-for-federal-pacific.53588/post-867625
* **LEAD-0076 — Schneider/Federal Pioneer FAQs on FPE replacement breakers** (B0009-legacy-other-manufacturers)  
  se.com FAQ000278110 and FA234570 blocked (403). Retrieve via browser to capture exact wording on NBLP/NB and CDP.  
  URLs: https://www.se.com/nl/en/faqs/FAQ000278110/ https://se.com/ca/en/faqs/FA234570/
* **LEAD-0077 — Zinsco/Sylvania commercial panelboard catalogue** (B0009-legacy-other-manufacturers)  
  Need GTE-Sylvania/Zinsco catalogue for QSF and double-slot/single-slot split-bus distribution panelboards, DSL* kit numbering (are DSL*/QSF*DS/SB OEM numbers or relectric dealer numbers?), and Sylvania SE/SEH/SC/SJD/SKM kit compatibility.  
  URLs: https://www.relectric.com/part-catalog/zinsco-circuit-breaker-parts-and-accessories https://www.relectric.com/part-catalog/sylvania-circuit-breaker-parts-and-accessories
* **LEAD-0078 — Challenger PM4a/PM4b panelboard documentation** (B0009-legacy-other-manufacturers)  
  Identify Challenger panelboard types (PM4a, PM4b) and the breaker frames for C?D?K kits; check whether Eaton KPRL4C*/KPRL4AC*/KPRL4BC* kits are Eaton OEM conversion kits for Challenger breakers in PRL4. Possibly overlaps Eaton batches (B0001/B0002).  
  URLs: https://www.relectric.com/part-catalog/challenger-circuit-breaker-parts-and-accessories
* **LEAD-0086 — NQ/NF branch connector part numbers inside SKNQBC/SKNF250/SKNF600** (B0003-squared-panelboards)  
  Bulletins 80043-735-01 and 80043-767-01 give contents but not component part numbers or dimensions. SKNF250 torque text is internally inconsistent (30-40 lb-in vs 6.74-8.99 N-m).  
  Docs: 80043-735-01, 80043-767-01
* **LEAD-0087 — Bulletin number scan gaps** (B0003-squared-panelboards)  
  download.schneider-electric.com accepts p_Doc_Ref=<doc number> (browser UA); HEAD scan found 80043-6xx..8xx bulletins, but rate-limiting (403) means some numbers were missed. 80043-0xx..5xx was scanned single-pass (only 9 hits) - rescan slowly with suffixes -01..-06. Also scan 48041-xxx and 80030-xxx series.  
  Docs: 80043-xxx, 48041-xxx, 80030-xxx
* **LEAD-0088 — Downloaded but not yet mined bulletins** (B0003-squared-panelboards)  
  80043-616-03 / 80043-449-03 (I-Line 4-piece trim & door kits), 80043-660-04 (HCP trim), 80043-706-02 & 80043-789-01 (I-Line CT neutral bonding), 80043-817/818/820/822/826-01 (fingersafe replacement parts QOFSBF, QOFSLALB, QOFSHALB, NQHJLSC, NQQLSC, NQLALHLSC, NQMLLSC, NQNCC), 80043-844-01 (RPINTBK800HCP, RPINTBK1200HCPC, RPINTBK1200HCR barrier kits), 80043-772-01 (quarter-turn fastener kit, LP9503), 80043-773-01 (endwall/closing plate MHCOEW20A/F), 80043-350-04 (box extension), 80043-455-04 / 80043-771-01 / 80043-850-01 (MH WP enclosures), 80043-252-04 (MH NEMA 4/4X). Only some copied to library; re-download as needed.  
  Docs: 80043-616-03, 80043-449-03, 80043-660-04, 80043-706-02, 80043-789-01, 80043-817-01, 80043-822-01, 80043-826-01, 80043-844-01, 80043-772-01, 80043-773-01, 80043-350-04
* **LEAD-0098 — GE AV-Line Switchboards publication GEA-7931** (B0012-archival-legacy-panelboards)  
  Cited in 'Electrical Wiring and Design' (1983). Search archive.org/HathiTrust/eBay for GEA-7931 and AV-Line instruction books (GEH-xxxx).  
  Docs: GEA-7931  
  URLs: https://archive.org/details/electricalwiring0000star
* **LEAD-0099 — Electrozad 1985 (Copel) price book - full ITE-Siemens / Square D / Federal Pioneer panelboard pages** (B0012-archival-legacy-panelboards)  
  archive.org lending item; borrow to read full NLAB/NHB/HR-7 selector tables, Square D NQO/NQOB/NYIB accessory list (more SF-/LK- part numbers) and Federal Pioneer NALP/NBLP.  
  URLs: https://archive.org/details/bwb_P9-BJG-737
* **LEAD-0100 — Schneider FAQs on NQO/NQOB/NEHB/NA1B/NY1B (blocked 403)** (B0012-archival-legacy-panelboards)  
  Read individually to map statements to FAQ numbers: FA97632, FA124608, FA232958, FA87904, FA100575, FA332061, FAQ000266417, FA129512, FA119163, FA122757, FA166748, FA121261, FA125651, FA128561.  
  URLs: https://www.se.com/us/en/faqs/FA97632/
* **LEAD-0101 — Cutler-Hammer pre-1994 switchboard designations** (B0012-archival-legacy-panelboards)  
  Only MP2 / MP-200 (group-mounted) and Type ES (existing family) found. 'Type MS' and Pow-R-Line predecessors for Cutler-Hammer switchboards not confirmed. Search ECM 1965-1990 issues on archive.org for Cutler-Hammer switchboard ads.
* **LEAD-0105 — Square D Digest 152 (1970) further mining** (B0012-archival-legacy-panelboards)  
  Only panelboard index/accessory pages were mined. Pages 56-83 contain full NQO/NQOB/NA1B/NH1B/I-Line/QMB interior, box and front catalog numbers (e.g. HCN-0936-1M interiors, MTX cable ducts, QMB-1832-2 interior) and the Q1/QO breaker tables; Section 600 breaker catalog referenced.  
  Docs: Digest 152  
  URLs: https://archive.org/details/squareddigest152
* **LEAD-0109 — I-Line plug-on data bulletin 0600DB1004 and SL250/SL800M5/SL1200P5-P7 instruction bulletins** (B0011-docs-ge-squared)  
  0600DB1004 (12/2010) blocked on se.com. SL400 IB 48040-651-03 found via graybar.com (Salsify CDN) - same route likely works for SL250/SL800M5/SL1200Px product pages on graybar.com (search page is JS; need product page URLs). docs.steinerelectric.com hosts Schneider instruction sheets (e.g. Schneider_Electric_HCM18736MP_Instruction_Sheet.pdf) but its TLS certificate is expired (not fetched).  
  Docs: 0600DB1004, 48040-651-03  
  URLs: https://graybar.com/sub-feed-lug-kit/p/88243518
* **LEAD-0110 — I-Line HCM/HCR-U neutral bonding straps 80043-446-06, 80121-082-02, 80010-600-01, hardware kit BBV57291** (B0011-docs-ge-squared)  
  Seen only in search-result summaries of se.com FAQs FA225933/FA117902/FA339459 (403 on fetch). Would add neutral bonding strap part numbers for HCR-U with/without neutral CT.  
  Docs: 80043-446-06, 80121-082-02, 80010-600-01, BBV57291  
  URLs: https://www.se.com/us/en/download/document/80043-446-06
* **LEAD-0111 — Current ABB BuyLog Section 11 Panelboards (2021/2022, ReliaGear neXT, "Spectra (obsoleted) bolt-on panelboard mounting hardware" p.11-63)** (B0011-docs-ge-squared)  
  electrification.us.abb.com PDF: curl HTTP/2 INTERNAL_ERROR / empty reply, WebFetch 503. pdf4pro.com has a text preview (TOC confirms p.11-63 Spectra obsoleted bolt-on hardware) but download is 403. ABB quick-selector guide (simplebooklet) gives the retrofit-kit table; product-number columns of its Spectra renewal tables are images.  
  URLs: https://electrification.us.abb.com/catalog/buylog/11_BuyLog_Panelboards.pdf https://pdf4pro.com/view/panelboards-buylog-section-11-abb-789fc0.html
* **LEAD-0112 — Tmax XT Spectra retrofit kit (SRFB/SRFN) installation instructions** (B0011-docs-ge-squared)  
  No instruction document number found; empower lists SRFB kits only inside breaker cross-reference entries (e.g. Tmax27292). Need kit contents, strap part numbers and torques.  
  URLs: https://empower.abb.com/ecatalog/ec/EN_NA/p/Tmax27292
* **LEAD-0116 — Eaton KB/KL/KCDP/KFDP/1C96608 kit instruction leaflets not public** (B0010-docs-eaton-siemens)  
  No Eaton instruction leaflet or SKU page exists online for KB* vertical main breaker kits, KL* lug kits, KCDP*, KFDP* or 1C96608/2C11642/1C96609 branch assemblies (skuPage 404 on Eaton mirror). Kit ILs ship in the box: obtain physical kits or Eaton satellite-plant copies to capture strap dimensions/torques.  
  URLs: http://cooperindustries.com/us/en-us/skuPage.KB13AFT.html
* **LEAD-0117 — Eaton SPX0361126 project O&M manual (585 pp) on ManualsLib** (B0010-docs-eaton-siemens)  
  ManualsLib manual 1538842 'Eaton Pow-R-Line SPX0361126' compiles IM01500001E (2011), Pow-R-Line panelboard renewal parts (Feb 2009) and switchboard unit data incl. 'Circuit Breaker Mounting Bolt Drilling Plan' (p.413) and 'Branch Devices' (p.363). Curl/manualzz blocked (403); WebFetch works page by page.  
  Docs: SPX0361126  
  URLs: https://www.manualslib.com/manual/1538842/Eaton-Pow-R-Line-Spx0361126.html?page=413
* **LEAD-0121 — Siemens US SPEEDFAX Section 12 switchboard branch kit table** (B0010-docs-eaton-siemens)  
  Locate SPEEDFAX (2017-2021) Section 12 switchboard 'distribution section branch mounting kits' page (SB1/SB2/SB3, CDP6/FC) for US catalog numbers and breaker compatibility; distributordatasolutions 2021q3/q4 documents host Section 11 - try sibling document hashes for Section 12.
* **LEAD-0122 — Eaton cooperindustries.com mirror** (B0010-docs-eaton-siemens)  
  cooperindustries.com mirrors eaton.com DAM and skuPage URLs (www.eaton.com times out from container). Use it for Eaton switchboard ILs (e.g. Pow-R-Line C/i branch device instructions, IL 29C101H breaker leaflets) and for current RP01400001E.  
  URLs: http://cooperindustries.com/content/dam/eaton/products/low-voltage-power-distribution-controls-systems/switchboards/pow-r-line-switchboard-manual-im01500001e.pdf
* **LEAD-0125 — ABB Spectra to Tmax XT smart cross-reference and plug-in (APN) retrofit kits** (B0016-aftermarket-retrofit)  
  new.abb.com page 'Tmax XT Retrofit Kits for Spectra Plug-in Panelboards and Switchboards' and empower.abb.com eCatalog returned 503. Capture full kit list for plug-in Spectra (APN) and the frame/rating-plug cross-reference table.  
  URLs: https://new.abb.com/low-voltage/service/service-for-low-voltage-products/tmax-xt-retrofit-kits-for-spectra-plug-in-panelboards-and-switchboards https://empower.abb.com/ecatalog/ec/EN_NA/p/Tmax27402
* **LEAD-0126 — Schneider Electric retrofit FAQs and retrofit form (se.com 403)** (B0016-aftermarket-retrofit)  
  Read FA239605, FA124771, FA116402, FA283569, FA339443, FA129258 directly and obtain the Square D retrofit form; confirm whether 'RTI' 14 in NQ interiors have distinct catalog numbers and whether I-Line retrofit for competitor switchboards is offered.  
  Docs: FA239605, FA124771, FA116402, FA283569, FA339443, FA129258  
  URLs: https://www.se.com/ca/en/faqs/FA239605
* **LEAD-0127 — Connecticut Electric current UBI catalog (post-2005) incl. bolt-on UBIF...NB, UBIFPE NE-frame, 3-pole UBIF3xxN** (B0016-aftermarket-retrofit)  
  2005 sheet lists only plug-in NA/NC, Pushmatic and Zinsco Q/QC/R/RC. Resellers cite UBIF340N, UBIF380NB, UBIFPE1003 and BRK-FPE-001 alias 'UBIF...NB'. Obtain current catalog and listing/classification documents (ETL file numbers).  
  URLs: https://www.connecticut-electric.com
* **LEAD-0131 — Supplemental and Obsolescence Digest Section 4 (Panelboards) full PDF** (B0015-squared-legacy-and-unmined)  
  2009 Digest Sec.13 (s24) refers to 'Supplemental & Obsolescence Digest, Section 4' for NQOD door-in-door trims and other legacy items. Only the DigestPLUS online viewer shell was found (productinfo.schneider-electric.com/nadigest/viewer/5cc35b7ed6593c0001ba8661/5cc36299d6593c0001baa700). Try download.schneider-electric.com p_Doc_Ref guesses or a distributor mirror; earlier Digest 175/176 Section 13 copies may also exist on distributor hosts (search 'Obsolescent Panelboards 13-1').  
  Docs: Supplemental Digest Section 4  
  URLs: https://www.productinfo.schneider-electric.com/nadigest/viewer/5cc35b7ed6593c0001ba8661/5cc36299d6593c0001baa700
* **LEAD-0132 — NQ fingersafe IB 80043-831-01 and drip-hood IB 80043-401-03** (B0015-squared-legacy-and-unmined)  
  All fingersafe replacement-part bulletins (80043-817/818/820/822/826-01) defer removal/installation of trim and deadfront to 80043-831-01; I-Line drip hood kits HCT2DH* reference 80043-401-03. Neither downloaded yet (download.schneider-electric.com/files?p_Doc_Ref=<n> works with browser UA).  
  Docs: 80043-831-01, 80043-401-03
* **LEAD-0137 — Siemens 6CLE2C / 6CLF1C ('C' suffix) strap kit variants** (B0014-siemens-instruction-sheets)  
  Lumen (Canada) lists 6CLE2C (125 A CED6 twin) and 6CLF1C (250 A CFD6 single) besides 6CLE2/6CLF1. Relationship (Canadian/copper variant? supersession?) unknown; no OEM document found.  
  URLs: https://www.lumen.ca/en/products/20-power-distribution/08-panelboards/01-main-breaker-kits/p-U0lFNkNMRTJD-sie6cle2c-siemens-6cle2c-switchboards-branch-breaker-mounting-kit-copper-3-ph-600-v-125-a
* **LEAD-0138 — BNK2 instruction 12-A-1085-01 missing from bucket** (B0014-siemens-instruction-sheets)  
  SIE_IS_BNK2_12-A-1085-1.pdf in dcc-data-extract is a stored SharePoint error page (HTML), not the PDF. Find another copy (distributor sites, Siemens SIOS).  
  Docs: 12-A-1085-01  
  URLs: https://s3.amazonaws.com/dcc-data-extract/new-delta/asset/Compas/daily/Compas/Instruction%20Sheet%20Quick%20Guide/SIE_IS_BNK2_12-A-1085-1.pdf
* **LEAD-0141 — SPEEDFAX 2011 Section 13 remaining pages** (B0014-siemens-instruction-sheets)  
  USESI_93254_catalog.pdf holds only pp.13-11..13-20 of SPEEDFAX 2011 Section 13 (Switchboards). The rest (SB1/SB2/SB3 main and branch device tables, SMM metering) not found; search assets.usesi.com product-media catalogs for adjacent USESI_932xx files.  
  Docs: SPEEDFAX 2011 Section 13  
  URLs: https://assets.usesi.com/product-media/catalogs/USESI_93254_catalog.pdf

## Priority 3

* **LEAD-0008 — CA08104001E Tab 22 deeper tables** (B0001-eaton-prl-panelboards)  
  Tab 22 (Jan 2018) contains PRL4 branch breaker table 22.4-3, fusible table 22.4-4, terminal wire range tables, series ratings and box sizing for PRL1a-PRL4 - can enrich family/breaker claims. Saved locally as tab22.txt.  
  Docs: CA08104001E  
  URLs: https://eatonarabia.com/wp-content/uploads/2022/03/eaton-panelboard-cag-tb01400003e-tab-22.pdf
* **LEAD-0009 — OSHPD OSP-0009 Eaton panelboard seismic pre-approval** (B0001-eaton-prl-panelboards)  
  Search snippet: PRL1a/1aF/1a-LX/Pow-R-Command 240 V 400 A; PRL2a 480 V 400 A; PRL3a 600 V 800 A; PRL4 600 V 1200 A. Not downloaded.  
  Docs: OSP-0009  
  URLs: https://hcai.ca.gov/wp-content/uploads/2020/10/OSP-0009-2.pdf
* **LEAD-0010 — Westinghouse NLAB / NHB / pre-1980s lighting panels** (B0001-eaton-prl-panelboards)  
  Requested scope item; no Eaton/Westinghouse document found that names NLAB or NHB panelboards. RP01400002E covers only PRL1/2/3, PRL1-LX, PRL3-LX, CDP/HCDP, FDP. Try archive.org Westinghouse 'Distribution Equipment' catalogs (1960s-80s) and Mike Holt forum.  
  URLs: https://forums.mikeholt.com/threads/westinghouse-prl2-panelboards.133286/latest
* **LEAD-0011 — SPD kits for Pow-R-Line panelboards** (B0001-eaton-prl-panelboards)  
  Catalogs state PRL1a/2a/3a/4 available with integrated SPD (Tab 34 reference) but no field-installable SPD kit numbers appear in renewal-parts guides. Search Eaton SPD 'integrated panelboard' kit catalog (SPD series SPD250/SPD100 panelboard mounting kits).  
  Docs: Tab 34
* **LEAD-0012 — PRL4 retrofit kit catalog strings** (B0001-eaton-prl-panelboards)  
  Retrofit kits are built as KPRL4 + breaker catalog + T/S (e.g. KPRL4KD3400S; Xpert: KPRL4XPG33400S) and KPRL4 + switch catalog (e.g. KPRL4FDPWT3633R); individual catalog numbers not enumerated - not recorded as part records.  
  Docs: RP01400001E
* **LEAD-0020 — TAD3 adapter kit contents and drawing** (B0002-eaton-switchboards-legacy)  
  Referenced in RP01400002E p.13 and Vol 12 Tab 3/4. Need kit contents, dimensions and whether it applies to switchboard LB provisions.  
  Docs: Application Data 29-160
* **LEAD-0021 — Volume 12 CA08100014E Tab 15 cites CA08100003E Vol 2 Tab 4 (Switchboards) and RP01301013E** (B0002-eaton-switchboards-legacy)  
  Vol 2 Tab 4 may list PRLC field-installable kits; RP01301013E covers Systems Pow-R breaker renewal parts.  
  Docs: CA08100003E, RP01301013E
* **LEAD-0022 — PRL1/PRL2 branch deadfront covers and boxes/trims (RP01400002E Tables 2, 6, 12-14)** (B0002-eaton-switchboards-legacy)  
  Not transcribed in this batch to stay in scope: deadfront style numbers 5156C10H01-H09 (PRL1) / 5156C09H01-H09 (PRL2); boxes YS20xx, trims LT20xxS/F, LTT20xxS/F; Type 12/3R GWPB/LWPT/LWT; column panels 114D939Gxx, 6724D78Gxx; PRL3-LX 6726D69Gxx/6726D70Gxx.  
  Docs: RP01400002E  
  URLs: https://www.farnell.com/datasheets/2307937.pdf
* **LEAD-0023 — PRL4 blank covers 6554C01Hxx / 6554C02Hxx** (B0002-eaton-switchboards-legacy)  
  RP01400001E 2017 Table 36 / 2022 Table 45 list 1X-20X blank covers (style numbers) for 24 in and 36/44 in boxes; not transcribed here.  
  Docs: RP01400001E
* **LEAD-0032 — QW1BL / QW3BL obsolete legacy fillers** (B0004-squared-switchboards)  
  OEM says obsolete, fabricate locally - remanufacture opportunity. Need physical sample for dimensions/hole pattern.
* **LEAD-0033 — I-Line plug-in units 45123-680-01 (busway) and panelboard install 80043-309-20** (B0004-squared-switchboards)  
  May provide I-Line jaw torque/lubrication and mounting details.  
  Docs: 45123-680-01, 80043-309-20  
  URLs: https://se.com/us/en/download/document/80043-309-20
* **LEAD-0034 — QMB circuit breaker unit catalog numbers (twin H-frame, single J/L)** (B0004-squared-switchboards)  
  4620CT9601 text lists ratings and lug kits but not the CB unit catalog numbers (only legacy QMB3400LA / QMB3300LA found). Check Digest Section for QMB.  
  Docs: 4620CT9601
* **LEAD-0035 — QMB 'TD' and 'T' suffix units (QMB322TD, QMB323TD, QMB362T, QMB362T1)** (B0004-squared-switchboards)  
  Distributor and FAQ numbers differ from current 'TW' numbering; determine whether TD = legacy-interior version.
* **LEAD-0044 — Original (pre-II) A-Series lighting panel branch connector hardware** (B0005-ge-abb)  
  No OEM renewal-parts table found for AQ/AE branch bus connectors or deadfront filler pieces beyond TQLFP1/TEDFP1 and ASPTED3P/ASPTQD3P/ASPFB kits. Look for DEH-40007 and older GEH-xxxx A-Series instruction books.  
  Docs: DEH-40007, DEP-104A, DEA-185
* **LEAD-0045 — Legacy NLAB, NHB, NAB, CDP, AV-Line OEM documentation** (B0005-ge-abb)  
  Only distributor/surplus evidence (NHB150PK; AV-Line switchboard listings). Seek GE GEH/GEF renewal parts bulletins for NLAB/NHB panelboards and AV-Line switchboards (e.g. archive.org, Bay Power, Relectric).  
  URLs: https://www.relectric.com/nhb150pk https://www.baypower.com/general-electric/switchboards
* **LEAD-0046 — A-Series II kits for other frames (FE, TFJ, TEYH 125A) and single-pole THQB** (B0005-ge-abb)  
  DEH40150-40158 series covers SG, SF, TQD, SE/TED, THQB 6/12, TEY 6/12, FB; check DEH40159+ for further ASPP kits.  
  Docs: DEH40159?  
  URLs: https://catalog.carboncontrolsltd.com/
* **LEAD-0052 — SMM/SMD metering switchboard connecting kits and meter socket kits** (B0006-siemens-ite)  
  2005 price list p.8-13: SMMBQMK, SMMQJMK, SMMEDMK, SMMFDMK, SMMCEMK, SMMTFMK (connecting kits for SMM and SMD metering switchboards) and MSK2001/MSK2003 replacement meter socket kits. Not catalogued in this batch.  
  Docs: 2005 EDP price list p.8-13  
  URLs: https://assets.usesi.com/product-media/brochures/USESI_93250_brochure.pdf
* **LEAD-0053 — Fusible branch connecting strap kits (F602, F657, F671, F672, F6150D, F6162D, VB657, VB671, VB610, VB6150) and Vacu-Break/VK switch kits** (B0006-siemens-ite)  
  Listed on SpeedFax pp.11-96, 11-110 and s3/s2; outside breaker-mounting focus; not catalogued.
* **LEAD-0054 — Integral bus-mounted SPD kits for P1 (TPS3/TPS4) and P2/P3 (TPS4 01 / TPS4 L1)** (B0006-siemens-ite)  
  P1 has space for one TPS3 or TPS4 SPD kit (p.11-9). SPD catalog numbers are in SpeedFax Section 10 (TPS), not retrieved.  
  Docs: SPEEDFAX Section 10
* **LEAD-0061 — Eaton terminal kit instruction leaflets / torque** (B0007-breaker-terminal-kits-eaton-squared)  
  IL29C402D (J-frame HMCP) reportedly lists TA250KB torque 275 lb-in; K-frame IL29C104E / IL29C403F list TA300K/TA350K/TA400K torque (search snippets: 275/375/275 lb-in). Download to raise torque claims to A.  
  Docs: IL29C402D, IL29C104E, IL29C403F, IL012090EN  
  URLs: https://www.eaton.com/content/dam/eaton/products/electrical-circuit-protection/molded-case-circuit-breakers/series-c-molded-case-circuit-breakers/k-frame-breakers-il29c104e.pdf
* **LEAD-0062 — Eaton Westinghouse-era terminal numbers superseded by TA/T series** (B0007-breaker-terminal-kits-eaton-squared)  
  No supersession data for pre-Series C (Westinghouse) terminal style numbers found; TAD3 adapter for replacing LB/DA breakers suggests legacy mapping exists.
* **LEAD-0066 — GE install docs for lugs / shields** (B0008-breaker-terminal-kits-ge-siemens)  
  The E150 reference list cites GEJ-3609 (back-connected studs) and GEH-4610 (plug-in mounting base). The lug kit instruction GEH/DEH numbers were not found; download them from library.e.abb.com.  
  Docs: GEJ-3609, GEH-4610, GEH-4342, DEH-41556
* **LEAD-0067 — GE breaker mounting screw kits and plug-in bases not recorded** (B0008-breaker-terminal-kits-ge-siemens)  
  BuyLog p. 6-101 lists mounting screw kits SEMSK1-4, SFGMSK1/2, SFMSK1/2, SKMSK1/2, mounting bases 343L162G1/G7/G11, 343L184G18 and cup washer 254V644P1. P. 6-105 lists plug-in mounting bases (TE12PD1/2, TE13PD1/2, TF22/23PD, TJ42/43PD1A, TJ62/63PD1A, SGPC1/2/7, TK83/103/123PD1A) and mounting plates TMP1-4/SMP3. None of these are recorded in this batch; capture them in a breaker-mounting batch.  
  Docs: BuyLog 6-101, BuyLog 6-105
* **LEAD-0068 — Siemens plug-in assemblies/tulips and VL (DG/FG/JG/MG/NG) lugs not recorded** (B0008-breaker-terminal-kits-ge-siemens)  
  SPEEDFAX p. 7-165 lists plug-in assemblies PC2637/PC2638/PC2657/PC2658, PC4753/4754, PC5777/5778, PC5660/5661, PC5662/5663, PC5664/5666, PCCJD/PCCLD, mounting plates PL2616/2617/4762/4763/5796/5797/5680/9698/9699 and tulip assemblies TCE3/TCF3/TCJ3/TCL3/TCM3/TCN3. VL-series lugs (3TA1DG30, 3TC1DG30, 3TA3DG02, 3TA6DG04, 3TA3FG20, 3TA1JG750, 3TA2JG250, 3TA2MG750, 3TA3MG500, 3TA3NG750, 3TA4NG500...) are on p. 7-175 onward. None are recorded here.  
  Docs: SPEEDFAX 7-165, SPEEDFAX 7-175
* **LEAD-0079 — Connecticut Electric / UBI full catalogue** (B0009-legacy-other-manufacturers)  
  Download Connecticut Electric 'UBI' replacement breaker catalogue for UBIF (FPE NA/NB/NC), UBIZ (Zinsco incl. bolt-on QB/UBIZ243xxx and mains UBITBFP), UBIP (Pushmatic) and bus kit UBIZRBK12 with listing basis.
* **LEAD-0080 — Westinghouse NLAB pre-Pow-R-Line panelboards** (B0009-legacy-other-manufacturers)  
  No sources found in this batch; check Eaton batches B0001/B0002 coverage and Westinghouse 1960s panelboard catalogues (NLAB, NHB) for connector straps.
* **LEAD-0081 — Kingsbury, Powell, Crouse-Hinds distribution, Bryant commercial panelboards** (B0009-legacy-other-manufacturers)  
  Not researched to any depth in this batch - no sources found for Kingsbury or Powell panelboard hardware.
* **LEAD-0082 — Frank Adam CU-NFJ kit** (B0009-legacy-other-manufacturers)  
  Determine whether late Frank Adam panelboards used FPE NFJ breakers (kit CU-NFJ on relectric) and whether Frank Adam was acquired by FPE or another firm.  
  URLs: https://www.relectric.com/part-catalog/frank-adams-circuit-breaker-parts-and-accessories
* **LEAD-0083 — FPE catalog number structure** (B0009-legacy-other-manufacturers)  
  Decode FPE breaker catalog numbers (e.g., NEF431100, NJL631175, HEF213020: digit meanings for voltage/poles/IC) from an FPE/American price list.
* **LEAD-0089 — I-Line SE replacement side covers and combo SE kits** (B0003-squared-panelboards)  
  IB 80043-839-01 Table 2 (ILBFMHCJHJUL, ILBFMHCPHJUL, ILBFMHCPRLUL, ILBFMHCPMPHCRMUL, ILBFMHCRPRUL) and Table 4 (ILCOMBLUL26W/32W/44W, ILCOMBMPUL26W/32W/44W) and M-frame lug covers ILMLC2W/3W/4W not entered as parts.  
  Docs: 80043-839-01
* **LEAD-0090 — MH box family** (B0003-squared-panelboards)  
  Standard MH boxes MH26..MH92 (20 in. W x 5.75 in. D, height = number, BE suffix = both endwalls blank, WP = Type 3R/5/12) and NC trims NCxx(F/S)(HR) not entered individually; tables on Digest pp. 9-9/9-10, 9-31. MH..D9 entered.  
  Docs: 0100CT2401-SEC-09
* **LEAD-0091 — SurgeLoc SPD for NQ** (B0003-squared-panelboards)  
  Digest p. 9-19 lists SSP01SBA08D..24D (120/240 V), SSP02SBA08D..24D (208Y/120 V), SSP03SBA24D (240/120 high-leg delta) plug-on SPDs; 96-space interiors needed in 84-ckt NQ; ref 998-21173700_GMA-US (downloaded). Not entered as parts.  
  Docs: 998-21173700_GMA-US
* **LEAD-0092 — I-Line breaker mounting hardware** (B0003-squared-panelboards)  
  No separately cataloged I-Line breaker mounting bracket / retaining screw kit found; manual 80043-309-20 describes bracket fingers into pan keyslots, retaining screw in 7/32 in. hole, PJC-7201 joint compound. Look for renewal parts list for HCP/HCR-U bus stacks and Supplemental Digest I-Line legacy (HCN, HCW, HCM) interiors.  
  Docs: 80043-309-20
* **LEAD-0102 — Square D I-Line pre-HCN types (HCW, 1950s I-Line panelboard)** (B0012-archival-legacy-panelboards)  
  Square D Digest 152 (1970) shows HCN/HCM/HCW/HCWM I-Line already catalogued; introduction date and the pre-1970 I-Line types are still unknown. Look for earlier Square D Digests (pre-1970) and Square D panelboard Service Bulletins (Digest p.85 says service bulletins and service-parts sheets exist for all catalogued panelboards). HathiTrust was blocked by Cloudflare from this container.  
  URLs: https://babel.hathitrust.org/cgi/ls?q1=%22I-Line%22%20panelboard
* **LEAD-0103 — ITE panelboard designations (EQ, NQB, Type HE, ITE CDP pre-Series 5)** (B0012-archival-legacy-panelboards)  
  Archive FTS found only ITE switchboard/unit substation ads (1950, 1957), EQ-225 breaker launch (May 1962) and Canadian NLAB/NHB/HR-7. ITE pre-Series 5 CDP and CDP-7 known only from dealer kit names.  
  URLs: https://archive.org/details/sim_ecm_1962-05_61_5
* **LEAD-0104 — McLaughlin Electric Supply House catalogs (1950/1951) on archive.org** (B0012-archival-legacy-panelboards)  
  Full text available (McLaughlinElectricSupplyHouse, McLaughlin_201806); contain Trumbull distribution panelboards (Converti-Fuse, NTPR) with box/gutter dimensions - not yet mined in detail.  
  URLs: https://archive.org/details/McLaughlinElectricSupplyHouse
* **LEAD-0113 — GE DEH/GEH Spectra instructions still missing** (B0011-docs-ge-squared)  
  Not on manualsdir: DEH-063/064/066 (FB/FC/FG bolt-on kits AMCB*FB, *FDB, *FGB/FGM, AMCB3LB), GEH-5592 (SKPA top cover), GEH-6501 ANKT and GEH-5683 GF neutral (no catalog numbers), DEH-043 (?), GEH-5588/5630 main lug kits. manualmachine.com still 403.  
  Docs: DEH063, DEH064, DEH066, GEH5592, GEH5588, GEH5630  
  URLs: https://www.manualsdir.com/brands/ge-industrial-solutions/193.html
* **LEAD-0114 — AFP4SGC vs AFP4SGD** (B0011-docs-ge-squared)  
  GEH5673 R03 names filler kit AFP4SGC for AMC4GB/AMC6GB modules; BuyLog lists AFP4SGD (dual SG). Confirm whether AFP4SGC exists.  
  Docs: GEH5673
* **LEAD-0115 — Square D QMQB switches** (B0011-docs-ge-squared)  
  80043-055-13 p.41 names "QMQB Main and Branch (available in Canada only)" - contradicts B0004 note that QMQB is probably not a real designation; research Canadian QMQB fusible switch units.  
  Docs: 80043-055-13
* **LEAD-0118 — Eaton 3FQS labels 3A1063/3A1064/3A1066** (B0010-docs-eaton-siemens)  
  Fastener torque values for 3FQS live on agency label 3A1064 (not reproduced in E3A1071). Field photo of label needed.  
  Docs: 3A1064, E3A1064
* **LEAD-0119 — KPRL3A* '140A max' vs RP01400001E 100 A** (B0010-docs-eaton-siemens)  
  Eaton web SKU pages state 'Amperage Rating 140A max' for KPRL3ABA*/KPRL3AGB*/KPRL3AFD* while catalogue holds RP01400001E-derived 100 A/150 A device limits. Resolve with kit label/IL.
* **LEAD-0128 — Siemens / ABB ReliaGear retrofit interior offerings** (B0016-aftermarket-retrofit)  
  No Siemens retrofit interior (P1 into existing box) or ABB ReliaGear retrofit interior found; only Siemens unassembled P1 interiors and IMK1 interior mounting kit. Ask Siemens/ABB or search Siemens SPEEDFAX for 'retrofit'.  
  URLs: https://steinerelectric.com/Catalog/Circuit-BreakersEV-Charging-And-Power-Distribution/Panelboards-And-Accessories/Panelboard-Mounting-Accessories/Siemens-IMK1-Interior-Mounting-KitFor-Use-With-P1-P2-P3-Panelboards-314082
* **LEAD-0129 — Eaton CH/BR retrofit stocking kit complete catalog (I-suffix interiors, RxCHFRAME collars, RTBR series)** (B0016-aftermarket-retrofit)  
  New numbers RACH24L125I, RDCH42B200I, RDCHFRAME, RTBR12L125R/Q, RTBR10B100Q seen at distributors; need Eaton list price/catalog page for full series and meaning of I/Q/R/K suffixes (automa.net lists RACH24L125K).  
  URLs: https://elliottelectric.com/P/Item/CHD/RDCHFRAME https://automa.net/eaton/rach24l125k
* **LEAD-0133 — MHCOEW20A vs MHCOEW20F difference; HCR12SNCT vs HCR12SNCTW** (B0015-squared-legacy-and-unmined)  
  Bulletin 80043-773-01 covers both endwall/closing-plate kits without explaining the suffix. Digest lists HCR12SNCT (neutral with CT) while IB 80043-706-02 uses HCR12SNCTW. Check se.com product pages.  
  Docs: 80043-773-01, 80043-706-02
* **LEAD-0134 — Digest 152 (1970) remaining pages** (B0015-squared-legacy-and-unmined)  
  This batch read leaf 59/60 (NQO/NQOB unassembled), 73/74 (I-Line unassembled) and 79 (QMB unassembled) as images. Still unmined: leaf 61-70 factory-assembled NQO/NQOB/NA1B/NH1B (box dims and front catalog numbers per assembled panel), leaf 64 column-width cable duct/pull boxes (MTX/MPX 1970 numbers), leaf 77 NTFB, leaf 78 telephone cabinets, leaf 85-86 additional features, leaf 74 lower third (HCW main breaker rows). Page images: https://archive.org/download/squareddigest152/page/n<leaf>.jpg  
  Docs: Digest 152  
  URLs: https://archive.org/details/squareddigest152
* **LEAD-0135 — NQRPLMB2HJ and other NQ/NF deadfront replacement kits** (B0015-squared-legacy-and-unmined)  
  NQRPLMB2HJ seen only in search summary of blocked se.com FAQ. Likely a family NQRPLMB2Q, NFRPLMB... exists; confirm via se.com product pages or Digest Sec.9 replacement-parts table.  
  URLs: https://www.se.com/us/en/faqs/FAQ000259238/
* **LEAD-0139 — SIE_IS_SMND_SSMND.pdf is corrupt; SSMND kit contents unconfirmed** (B0014-siemens-instruction-sheets)  
  The bucket copy cannot be rendered. SMND contents were taken from 11-B-1017-01 (image file). SSMND (SMD/SND solid-state) kit list not confirmed; SPEEDFAX 2011 p.13-20 lists SSMND 10in single 800/1200 A.  
  Docs: 11-B-1017-01  
  URLs: https://s3.amazonaws.com/dcc-data-extract/new-delta/asset/Compas/daily/Compas/Instruction%20Sheet%20Quick%20Guide/SIE_IS_SMND_SSMND.pdf
* **LEAD-0140 — VL (DG-PG) accessory sheets: per-fastener torque mapping** (B0014-siemens-instruction-sheets)  
  VL accessory instruction sheets (I.L. 8068xx) print several torque values inside figures; this batch recorded them as 'printed values'. Read figures visually to assign torques per fastener; also US cat. nos. for 3VL9300-8CE01 / 3VL9600-8CE01 / 3VL9800-8CE01 (3-pole interphase barriers) and CG-FG TSS covers (3VL9300-8CB31/41) not legible in text layer.  
  Docs: 806886A02, 806883A02, 806866A01, 806863A02
* **LEAD-0142 — SMSKHCP vs SMSKHCPP catalog number** (B0014-siemens-instruction-sheets)  
  Bucket file SIE_IS_SMSKHCPP.pdf; document 11-D-1023-01 title reads 'SMSKHCP for Main Mounting Type SENTRON HCP SWITCH'. Confirm the orderable number in SPEEDFAX P5 tables.  
  Docs: 11-D-1023-01
* **LEAD-0143 — No TPS3/TPS4 SPD, SMM connecting-kit or ITE-era instruction sheets in bucket** (B0014-siemens-instruction-sheets)  
  The dcc-data-extract SIE_IS_* listing (1,274 keys) contains no TPS3/TPS4 integral SPD kit sheets, no SMM*MK connecting kit sheets and no ITE/Siemens-Allis era kit sheets beyond the Series 5/6 drawings (11-5068, 11-5383, 12-5719..12-5772, 11-5073..11-5075, 11-5570). Siemens-Allis/ITE literature remains a gap (see LEAD-0047/0103).
* **LEAD-0145 — PQ/PE/PF Super Blue Pennant distribution panel kit table alignment** (B0014-siemens-instruction-sheets)  
  Voltage rows in the extracted SPEEDFAX 2011 p.13-16 table may be offset; verify against PDF before relying on voltage per catalog number.  
  Docs: SPEEDFAX 2011 p.13-16  
  URLs: https://assets.usesi.com/product-media/catalogs/USESI_93254_catalog.pdf

## Priority 4

* **LEAD-0013 — Boxes, trims, EZ Box/EZ Trim, Type 12/3R enclosures, side gutter covers, door-in-door kits** (B0001-eaton-prl-panelboards)  
  Not recorded as parts in this batch (scope = mounting hardware). Tables available: s1 p.31 side gutter covers 6555C20H01-6555C28H01; s1 p.36 EZB/EZT 42C1999/42C4255/42C4258/42C4261/42C4264; s1 p.37-38 VWPB/LWPT, LDD...STW/FTW, mounting channels 8708C82G02-G08, RPCB/DPC; s4 p.10-11 DD2457K..DD4490K, EZ flanges 42C1993H01, 42C1995Hxx, 42C1987/42C1988Gxx, EZ anti-lift 1A85195H01; s5 pp.3-9 YS20xx boxes, LT/LTT trims, column boxes 114D939Gxx, 6726D69Gxx.  
  Docs: RP01400001E, RP01414001E, RP01400002E
* **LEAD-0024 — Challenger panelboards (non-loadcenter) data** (B0002-eaton-switchboards-legacy)  
  No OEM renewal data found for Challenger-branded commercial panelboards; Vol 12 only gives BR loadcenter lineage (Challenger bought 1988).
* **LEAD-0036 — QED-2 through-bus splice plates, end closures, main lug kits** (B0004-squared-switchboards)  
  No orderable catalog numbers found; FAQs say parts ordered by switchboard factory order (FO) number. Busbar connection kit '36967' seen on distributor page - unverified relevance.  
  URLs: https://www.standardelectricsupply.com/2250993-Square-D-Schneider-Electric-36967
* **LEAD-0037 — Legacy Power-Style QED (QED-1, QED-3, QED-4, QED-2/S) and Model 6 MCC connections** (B0004-squared-switchboards)  
  Only names found (2700CT1101 p. 9; FA116225 mentions QED-1). No legacy QED catalogs retrieved.
* **LEAD-0055 — Number strips, directory cards, locks, keys** (B0006-siemens-ite)  
  NBK01A-03A (P1), NBK3-8 (P2/P3), LPDC01/02, MCHK, LPJSPDNUT01, LPTS01, LP3RHP01, LPKEY01A/B (key B363A), LPLOCK01A/02A/03A (FAS-Latch, 11-1895-61/62/63), XTP060 touch-up paint - listed on pp.11-20, 11-21, 11-54; not catalogued as parts.
* **LEAD-0069 — Siemens 3TC1QR250 vs 3TC1QR2520** (B0008-breaker-terminal-kits-ge-siemens)  
  P. 7-40 prints 3TC1QR250 and p. 7-155 prints 3TC1QR2520. Resolve with a distributor listing.
* **LEAD-0093 — NF L-frame bulletin 80043-766-03 catalog number** (B0003-squared-panelboards)  
  Bulletin does not print catalog number in text extraction; confirm it is N400M (and older LA/LH kit numbers).  
  Docs: 80043-766-03
* **LEAD-0094 — NQ 14 in. neutral bonding screw and NF gutter bonding strap catalog numbers** (B0003-squared-panelboards)  
  Bulletins 80043-786-01 and 80043-768-01 give contents/torque (10-12 lb-in; 20-25 lb-in) but no catalog numbers; 80043-770-01 (NF column-width connector kit) likewise.  
  Docs: 80043-786-01, 80043-768-01, 80043-770-01
* **LEAD-0106 — Westinghouse NOFUZE catalog B-series (1946) page B62 and bulletin B-3714** (B0012-archival-legacy-panelboards)  
  The 1946 ECM insert reproduces Westinghouse catalog pages (B62); the full Westinghouse 'Electrical Contracting' catalog insert may list NLAB/NMM part numbers.  
  URLs: https://archive.org/details/sim_ecm_1946-09_45
* **LEAD-0130 — Custom/reproduction mounting kit fabricators (Breaker Outlet, IEM, others)** (B0016-aftermarket-retrofit)  
  Forum: breakeroutlet.com offered to have an Arrow-Hart kit made but would not supply drawings. IEM (Industrial Electric Mfg) makes CDP-type kits for GE/Eaton breakers. Survey fabricators and what evidence (drawings, testing) they provide.  
  URLs: https://forums.mikeholt.com/threads/need-leads-for-suppliers-of-obsolete-breaker-mounting-kits.2580007 https://www.relectric.com/circuit-breaker-parts-and-accessories/mounting-hardware?page=20
* **LEAD-0136 — Physical dimensions of legacy fronts (NQC-xxTF, MSC, MDC, LX, HC-26xx-C, MHC) for remanufacture** (B0015-squared-legacy-and-unmined)  
  Catalogs give box sizes only. Need PBA drawings (PBA600, PBA603WP, PBA604, PBA711, PBA555 referenced in Digest Sec.9 footnotes) or field measurement.  
  Docs: PBA600, PBA603WP, PBA604, PBA711, PBA555
* **LEAD-0144 — Unprocessed out-of-scope sheets in bucket** (B0014-siemens-instruction-sheets)  
  Load-center (EC*, LoadCenter_*, EQBreaker, MBK150A-225A EQ8693/8695/8696 main breaker kit, MainBreaker*, QJ main breaker inversion P/N 48100025, Renovation Interior kit 48100108), Power Mod / Uni-Pak meter-stack (PowerMod_*, WPK*, UNIPAK_*, ECRLK250 riser panel lug kit), WL power breaker, 3VA, safety switch (HF/HN/LBR/CFS/VBII, ReplacentLine HFB67/HFB68/HNB678) and AFCI/GFCI sheets were not processed.

