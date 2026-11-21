# news-image-20261120 v2 — STATUS (FACTS ONLY)

## Entry
- Competition: news-image-20261120 — "Sum up 20 November's world news in one image"
- Prizes: 1st $50, 2nd $30, 3rd $15, 4th–10th $5, 11th–50th $3 (total $250)
- Closes: 2026-11-22T00:00:00Z (22 Nov 07:00 WIB). Result ~4 Dec 2026.
- Goal: beat top 1 (992,057) / top 1-3; top-50 bar 988,744. v1 scored judge 980,686, rank 894.
- Entry dir: /home/hatch/workspace/makefun/news-image-20261120-v2-entry
- Intended repo (NOT created yet — parent creates after Wahyu approves preview): https://github.com/wahyunp26-source/news-image-20261120-v2 (public, main)
- NOT submitted. No commit. No repo. Parent does repo + commit + bundle + submit after Wahyu approves the preview.

## Files
- main.py (40 lines, 1,146 B, stdlib only): copies entry.png beside it to $MAKEFUN_OUTPUT_DIR (default /output); verifies size + bytes match source.
- build.py (398 lines, 15,956 B, Pillow, build-time only): composes the 1024x1024 page from assets/ with Liberation Sans/Serif.
- entry.png: 327,751 B, 1024x1024, JPEG magic bytes. sha256 b7cb32750b0a85fa220baa153d76c671a40f59d105845cc2e9cf2d0f7a4715e7
- assets/: f01.jpg–f13.jpg (13 feature illustrations) + map.jpg (world map), ALL generated fresh in-session with the image tool, flat-vector style (deep red / navy / teal / ochre on cream). No v1 files copied.
- README.md: 3 live badges for news-image-20261120 (repo path news-image-20261120-v2) + referral amzcd6wq.
- LICENSE: MIT, SPDX-License-Identifier: MIT first line.
- .makefun/owner.json: wallet 72g4GnNmjWeE2sLoKp5VtbDptQyUdz7am6MSXmkpRxB7.

## Layout (copies top 1-3)
- Header: kicker "THE WORLD IN ONE DAY" + "FRIDAY'S NEWS · ONE PAGE · 36 STORIES · 6 CONTINENTS", huge serif "Friday 20 November 2026", italic red sub-headline naming top 3 + AI sell-off.
- Stats strip (6): 300,000+ evacuated; 3 Kyiv bridges; -4.1% Nikkei; 2.3% Japan CPI; 118 Phillips; 250,000 landmines.
- Region tabs: EUROPE 9, AMERICAS 9, ASIA-PACIFIC 6, MIDEAST 4, AFRICA 3, OCEANIA 3, WORLD / SPACE 2.
- 3 BIG features (image + bottom band + kicker + headline + caption): 1 Odisha cyclone, 2 Kyiv missiles, 3 COP31 Antalya.
- 10 MEDIUM (2 rows of 5, badge tag on image): 4 Asia sell-off, 5 Japan CPI, 6 Phillips 118, 7 Russell Las Vegas, 8 Raoni, 9 Malatya crash, 10 UK drones, 11 Gaza Yellow Line, 12 BepiColombo Mercury, 13 Zimbabwe landmines.
- WHERE IT HAPPENED world map (cream land on navy) with 13 numbered pins + pin key; 23 briefs (14-36) in 2 columns.
- DATE CHECK strip: Trump–Xi–Putin Shenzhen summit · ICJ Myanmar Rohingya verdict · Houthi missile Riyadh tower · US Senate rejects Iran war-powers bill · Denmark Greenland defence deal · Microsoft explains 12 Nov outage.
- Footer: "36 STORIES · 6 CONTINENTS · SOURCES: Reuters, AP, AFP, BBC, IMD, UN News, Al Jazeera, ICC, EU Council, PBOC."

## Content — 36 stories
- Features 1-13: (1) Cyclone Akvan landfall Odisha, 300,000+ evacuated, Gopalpur, winds 90-100 gusting 110 km/h, 423 rescue teams (IMD/Reuters); (2) Russia fires ~30 ballistic missiles at Kyiv, 7 waves, energy/transport sites, fires in 3 districts, Dutch + Austrian embassies damaged (Kyiv Post, Reuters); (3) COP31 final day deadlocked, draft omits fossil-fuel phase-out, $120bn adaptation finance unresolved, "35 by 35" clean-power goal (UN News, Reuters); (4) AI sell-off sinks Asia, Nikkei -4.5%, KOSPI -4.7%, SoftBank -16%, MSCI Asia-Pacific -7% (Reuters); (5) Japan CPI 2.3%, BoJ hike eyed (Reuters); (6) Phillips 118 vs India, first NZ batter with centuries in all 3 formats vs India in a year, NZ 368 (ICC, AP); (7) Russell fastest wet Las Vegas GP practice, FP2 1:47.272, FP1 washed out (formula1.com); (8) Brazil recognises Chief Raoni's ancestral land (Brazil govt); (9) Turkey helicopter crash Malatya, 4 dead (Turkish media); (10) UK pledges 1,000+ drones, £280m for Kyiv (UK govt); (11) Gaza Yellow Line crossed (News wires); (12) BepiColombo reaches Mercury, 6bn-mile trip ends, orbit insertion Saturday (ESA, BBC); (13) HALO Trust destroys 250,000 landmines (HALO Trust).
- Briefs 14-36: (14) Sudan mine strike; (15) US–Venezuela deal; (16) al-Dahi mosque fire; (17) Bangladesh violence; (18) Iraq militia order; (19) IAEA North Korea enrichment; (20) Brazil central bank $1bn; (21) Spain campaign; (22) Italy 3-1 France; (23) Rosalía Latin Grammy; (24) Scaloni to 2030; (25) Alcaraz/Sinner Turin; (26) Cyclone Xavier; (27) Fujairah crash; (28) PBOC holds rate; (29) US reporters bag phones; (30) Malawi fuel crisis; (31) Czech leaders in Israel; (32) US sanctions Comancheros/'Ndrangheta; (33) youth strike 25+ nations; (34) Poland $50bn nuclear deal; (35) Meta 2030 climate revision; (36) Australia terror-law call. Dropped from v1's 24 briefs: "US court faith emails" (weakest).
- Region counts recomputed for 36: EUROPE 9, AMERICAS 9, ASIA-PACIFIC 6, MIDEAST 4, AFRICA 3, OCEANIA 3, WORLD/SPACE 2 (v1 was 9/10/6/4/4/3/2; dropped Senegal boat = AFRICA -1, US court emails = AMERICAS -1).

## Checks (all passed, 21 Nov ~01:00 WIB)
- entry.png 327,751 B <= 1,048,576; 1024x1024; JPEG magic bytes.
- main.py run twice from /tmp with different MAKEFUN_OUTPUT_DIR: byte-identical (sha256 b7cb3275... both runs, matches entry.png), exit 0.
- Clean venv (python3 -m venv --without-pip): main.py exits 0.
- Visual check of entry.png: date headline unmissable; all 13 illustrations match their headlines; no garbled text; no overlap; DATE CHECK strip present; map pins visible and on the right landmasses.
- Fixes during build: (1) kicker "THE WORLD IN ONE DAY" was cut off (draw_tracked centered on x=16) — fixed to left-aligned tracked draw; (2) map pins misplaced (equirectangular lon mapping off ~120px in Europe/India on the Robinson map) — recalibrated by eye against the map's landmasses, cluster spread so all 12 land pins stay readable.
- makefun check (kit ~/workspace/makefun/kit-fresh-news-20261120/news-image-20261120-kit, --worktree): 4 passed (competition_open, snapshot, license_osi, entrypoint), 1 failed (transcripts_present — expected, bundle is made at submit time by the parent, as with v1), 14 skipped, 5 at submission (repo_public, repo_owner, repo_created_after_open, commit_in_repo, duplicate_snapshot — repo not created yet). Kit level 27 vs site 30 (known trap — do NOT refresh).

## Flags for parent
- Nikkei figure inconsistency (both from the brief): stats strip says -4.1%, feature #4 caption says -4.5%. Parent to decide whether to harmonise before submit.
- Submit path is --bundle (news-image-20261120 does not take recorded transcripts; v1's recording attempt got HTTP 400). Bundle flags per skill: --harness muse-app --harness-version 1.3 --model ipnext/avocado-5.17-v2 --provider meta --effort default --mcp none --no-discover --no-family, plus --dry-run first. Usage file: parent must query muse.db for this builder session after it ends and overwrite ~/.makefun/muse-usage-news-image-20261120.jsonl before bundling.
- Quota: v1 used round 1/3. v2 would be round 2/3 (1 left after).
