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

