# BC's 2022 Shared Recovery Mandate: The Binding Instrument Behind the NBA Wage Increase and COLA

*A non-partisan analysis for BCNU / Nurses' Bargaining Association (NBA) members and analysts: where the 2022–2025 wage numbers actually come from, whether a "me too" wage clause between unions exists, how nurses gained value outside the wage mandate, and how the successor 2025 mandate closed the loophole.*

**Prepared:** 2026-06-02 · **Mandate term:** 2022–2025 (now complete) · **Successor:** 2025 Balanced Measures Mandate

> **Independent and unofficial.** This is one person's independent analysis — **not affiliated with, authorized by, or endorsed by** BCNU, the Nurses' Bargaining Association, HEABC, the BC Public Sector Employers' Council (PSEC), or the Province of British Columbia, and **not legal, financial, or professional advice**. See the [repository README](README.md) for full disclaimers. Where this analysis and the official mandate / collective-agreement documents disagree, **the official documents govern.**

---

## How to read this document (methodology & honesty notes)

- **Primary sources are overwhelmingly public.** The mandate description (gov.bc.ca/PSEC), the *Public Sector Employers Act*, the BC government wage/COLA news releases, HEABC announcements, and the me-too Letters of Agreement themselves (BCGEU, CSSEA, and the 2025 CBA tentative agreement) are all citable online — URLs are given in the source list and footnotes.
- **Where a file path like `contracts/…` is cited, it points to an *unpublished working corpus*, not this repository,** so it won't resolve here. Those are given as provenance (the public source URL is alongside wherever one exists). The two me-too LOAs were extracted from their public source PDFs into that working corpus; the **operative clauses are quoted in full inline** (§5.7) so nothing load-bearing depends on an unresolvable path.
- **Verification.** External claims were put through a fan-out, adversarial multi-agent verification pass (16 sources, 25 falsifiable claims, 3-vote refutation, 0 dropped), and the load-bearing LOA text was confirmed by extracting it directly from the primary PDFs. Items still resting on inference — chiefly *why* the 2025 NBA-only carve-out exists — are flagged as such in §5.7 and §7.
- **A companion AI-research audit** (referenced as `[^metoo]`) is a **private working document, referenced not republished**; every load-bearing claim it raised was independently verified against primary text before being relied on here, and where it was wrong (an exclusions-list error) the correction is noted.

---

## Sources (primary first)

The research deliberately prioritised primary government, legislative, and employer-association text over commentary. Listed by tier.

### Primary — government / legislation / employer association

| # | Source | What it establishes |
|---|---|---|
| [^psec] | **PSEC, "Mandates and agreements" page**, gov.bc.ca — `www2.gov.bc.ca/gov/content/employment-business/employers/public-sector-employers/public-sector-bargaining/mandates-and-agreements` | The authoritative public description of the **2022 Shared Recovery Mandate**: scope, the 3-year wage schedule, the COLA maxima, and the trigger dates. |
| [^psea] | **Public Sector Employers Act [RSBC 1996] c. 384**, bclaws.gov.bc.ca — `bclaws.gov.bc.ca/civix/document/id/complete/statreg/96384_01` | The statute constituting PSEC (s. 4) and making its strategic directions binding on employers' associations (s. 7(1)(c.1)) and compensation plans binding as "employment compensation standards" (s. 14.3). The legal force behind the mandate. |
| [^psecrole] | **PSEC, "Public Sector Bargaining" landing page**, gov.bc.ca — `www2.gov.bc.ca/gov/content/employment-business/employers/public-sector-employers/public-sector-bargaining` | PSEC coordinates bargaining through sectoral employers' associations and "ensur[es] public sector compensation costs are aligned with the fiscal plan through the budget objectives set by government" — the funding-side basis for §1.3. |
| [^fin2022] | **BC Gov news release 2022FIN0075-001756** (mandate launch) | Year-1 structure ($0.25/hr + 3.24%) and the negotiable 0.25% flexibility allocation. |
| [^fin2023] | **BC Gov news release 2023FIN0022-000361** (Year-2 COLA) | The COLA formula and the Year-2 trigger: 12-month BC CPI avg = 7.1%. |
| [^fin2024] | **BC Gov news release 2024FIN0013-000387** (Year-3 COLA) | The COLA formula, Year-3 trigger (CPI avg = 3.4%), and the 400,000 / 99% coverage figure. |
| [^heabc] | **HEABC COLA announcement, 22 March 2023** — `heabc.bc.ca/public/News/2023/COLA-Announcement_22March2023.pdf` | Employer-side confirmation: "5.50 per cent guaranteed GWI in Year 2 plus a potential for up to 1.25 per cent COLA to a maximum of 6.75 per cent." |
| [^heabcsum] | **HEABC NBA 2022–2025 Summary of Changes** — `heabc.bc.ca/public/CAs/NBA/2022-2025_SummaryofChanges_NoInterps.pdf` | Employer-side summary of the NBA wage terms. |
| [^nbapca] | **NBA Provincial Collective Agreement 2022–2025 (PDF)** — `bcnu.org/Contracts-Bargaining/Documents/nba-pca_2022_2025.pdf` | The implementing contract: Article 63 (GWI) and Appendix VV (COLA definition). |
| [^bcnunews] | **BCNU news, 21 March 2024** — `bcnu.org/news-and-events/news/2024/...` | Confirms nurses received the full 3% (2% GWI + 1% COLA) in Year 3. |
| [^repo63] | **NBA PCA 2022–2025, Article 63** (working-corpus transcription of the public NBA PCA, `bcnu.org/.../nba-pca_2022_2025.pdf`) | Article 63 (GWI schedule). |
| [^repovv] | **NBA PCA 2022–2025, Appendix VV** (working corpus; public NBA PCA) | Appendix VV (COLA / AABC CPI peg). |
| [^repo28] | **NBA PCA 2022–2025, Article 28** (working corpus; public NBA PCA) | Article 28 premiums: 28.05 Regular Premium ($2.15/hr), 28.01 shift premiums, 28.06 OR/ER/ICU premium. |
| [^repo57] | **NBA PCA 2022–2025, Article 57** (working corpus; public NBA PCA) | Article 57.05(B): employer reimbursement of BCCNM registration fee. |
| [^heufba] | **HEU, Facilities Bargaining Association FAQ** — `heu.org/fba-faqs` | Confirms a per-CA "me too" clause: FBA matched if another BC public-sector union bargains a higher wage increase this round. |
| [^bcgeuloa] | **BCGEU agreements database — "LOA Public Sector Wage Increases (Me Too) Sep 2, 2022"** — `agreements.bcgeu.ca/document/eU9xYm95Z004clk9` | Primary text of the me-too LOA (BCGEU version, comparator = 19th Main Public Service Agreement): full trigger, $0.25 = 0.5% convention, 13.49% worked example, exclusions. |
| [^loatext] | **CSSEA 2022 Tentative Agreements — Public Sector Wage Increases LOA** (p. 25) — `cssea.bc.ca/PDFs/Bargaining/2022/TentativeAgreementsFebruary2022.pdf` | Second primary copy of the LOA (CSSEA version, comparator = "the Collective Agreement"); identical mechanics, with a plain-language "Comments" gloss. Quoted inline (§5.7). |
| [^bcgeu675] | **BCGEU, "April 1, 2023 GWI will be 6.75%"** — `bcgeu.ca/april_1_2023_general_wage_increase...` | Corroborates Year-2 6.75% and the ~13.75% realized three-year average. |
| [^hall] | **HSA, "HSA wins $10 million settlement"** — `hsabc.org/news/hsa-wins-10-million-settlement-health-science-professionals` (and `bcchs.cupe.ca`) | Arbitrator John Hall, decided Sept 28 2022: $9.44M to HSPBA, me-too triggered by the NBA's superior (no-joint-trust) benefit deal in 2014–2019. |
| [^psec2025] | **PSEC, 2025 Bargaining Update / Balanced Measures Mandate** — `www2.gov.bc.ca/.../psec/2025-bargaining-update.pdf` + PSEC bargaining page | Successor mandate: 3%/yr × 4 years (2025–2028), 0.2% flexibility allocation in years 2 & 4, no COLA. |
| [^cba2025] | **2025–2029 CBA Full Tentative Agreement** (NCI LOA, p. 2 of 4) — `bcnu.org/files/2025-2029_CBA_Full_Tentative_Agreement.pdf` | Primary text of the 2025 "Net Compensation Increases" me-too LOA: NCI definition (W&WIB base), flexibility allocations counted, 12.4% CBA baseline, and the verbatim NBA-only carve-out. Quoted inline (§5.7). |
| [^metoo] | **Companion AI-research audit** (private working document — *referenced, not republished*) | Raised LOA ubiquity across other unions, the trigger arithmetic, the exclusions list, and the 2025 NCI model + NBA carve-out. Treated as a lead only: every load-bearing claim was independently verified against the primary text above (and one exclusions-list error corrected). |

### Secondary — analysis / commentary (used only for interpretation, not core facts)

| # | Source | Used for |
|---|---|---|
| [^uvic] | **UVic Bargaining, "PSEC"** — `uvic.ca/bargaining/home/psec/index.php` | PSEC's coordinating role. |
| [^academic] | **Academic Matters, "Bargaining in the shadow of BC's PSEC"** — `academicmatters.ca/...` | The de-facto-uniformity / absence-of-matching analysis. |
| [^law] | **Canadian Lawyer**, coverage of the 2022 Shared Recovery Mandate | General confirmation of the mandate terms. |

---

## 0. The one-paragraph version (plain language)

If you are looking for a **binding agreement *between unions*** that houses a "me too" wage clause, **it does not exist.** The instrument behind every BC public-sector union's identical 2022–2025 wage numbers is the **2022 Shared Recovery Mandate** — an **employer-side government mandate** set by the **Public Sector Employers' Council (PSEC)** and made binding on employers (not negotiated among unions) by the **Public Sector Employers Act**.[^psec][^psea] It fixes a uniform three-year envelope — **Year 1:** $0.25/hr flat + 3.24%; **Year 2:** 5.5% + up to 1.25% COLA (max 6.75%); **Year 3:** 2% + up to 1% COLA (max 3%) — plus a negotiable 0.25% flexibility allocation in Years 1–2.[^psec][^fin2022] The NBA simply implements that envelope in **Article 63** and **Appendix VV** of its collective agreement.[^nbapca][^repo63][^repovv] Every public-sector union lands on the same numbers **because PSEC controls all ~400,000 (≈99%) covered employees' mandates by law — not because the unions matched each other.**[^fin2024][^psea] There is **no inter-union document and no mandate-level matching obligation.** What *does* exist is a **standardized "Public Sector Wage Increases (Me Too)" Letter of Agreement** that PSEC inserts into individual unions' collective agreements (employer↔union) — its operative text verified here from two primary sources, the BCGEU and CSSEA versions — which trues up a signatory if another union's cumulative GWI+COLA exceeds the mandate's worked maximum of 13.49% over three years.[^bcgeuloa][^loatext] **The NBA/nurses agreement does *not* contain this LOA** (verified against its full A→CCC appendix index); nurses instead took additional value *outside* the GWI envelope — premiums and nurse-to-patient ratios — which the LOA's GWI-only trigger does not capture (see §5.5, §5.7).[^nbapca]

---

## 1. The instrument and where its force comes from

### 1.1 It is a mandate, not a contract between unions

The single most common misconception is that a "me too" wage clause lives in some agreement signed among the public-sector unions. **It does not.** The chain of authority runs entirely **employer-side**:

```
Public Sector Employers Act (statute)
        │  s. 4 — PSEC sets "strategic directions"
        ▼
Public Sector Employers' Council (PSEC)
        │  issues the 2022 Shared Recovery Mandate
        ▼
Employers' associations (HEABC for nurses, BCPSEA, PSEA, …)
        │  s. 7(1)(c.1) — "must comply with any strategic direction"
        ▼
Each union's collective agreement (NBA Art. 63 + App. VV, etc.)
```

The PSEC page states the mandate "applied to **all** public sector employers with unionized employees whose collective agreements expired **on or after December 31, 2021**."[^psec] The *Public Sector Employers Act* supplies the legal teeth: PSEC's statutory function is "to **set and coordinate strategic directions** in human resource management and labour relations" (s. 4(1)); each employers' association "**must… comply with any strategic direction that is set by the council**" (s. 7(1)(c.1)); and a ministerially-approved compensation plan "**is adopted as an employment compensation standard**" (s. 14.3(5)).[^psea]

> **Why uniformity happens:** every union ends up on the same wage figures because **PSEC sets one identical envelope for every employer by statute**, and each union then bargains its own agreement within it. The matching is imposed on the *employer* side; it is **not** a "me too" promise the unions exchanged.[^psea][^academic]

### 1.2 The issuer

**PSEC is a statutory body** constituted by the *Public Sector Employers Act*, with members appointed by the Lieutenant Governor in Council, whose function (s. 4) is to set and coordinate labour-relations strategic direction.[^psea][^psec] The mandate envelope flows from that s. 4 function; related compensation directives sit with the Minister (s. 14.3) and Cabinet.

### 1.3 How the mandate becomes money — the funded floor vs. the me-too ceiling

A natural question follows from all of this: if the mandate is set *employer-side* and "pushed down" from PSEC, how do unions actually **get** the increase? The answer is that **the mandate figure is a *funded authorization*, not a deduction** — for 2025–2029, the 3%/year is the amount, not a cut from something larger. The loop runs:

1. **Government funds it in the fiscal plan.** PSEC's stated role is to "protect[] the interests of taxpayers by ensuring public sector compensation costs are **aligned with the fiscal plan through the budget objectives set by government**."[^psecrole] The wage envelope is sized to money the province has already budgeted across the public sector.
2. **PSEC sets the mandate and binds every employer to it.** Under the *Public Sector Employers Act*, each employers' association (HEABC for nurses) "must… comply with" the PSEC direction (s. 7(1)(c.1)).[^psea] The mandate authorises them to offer *up to* the envelope — and no more.
3. **The union bargains it into its own agreement and members ratify.** The increase is not automatic: the bargaining association negotiates within the envelope and members vote, after which the figure is written into the collective agreement's wage schedule (for nurses, Article 63).[^repo63] Government releases describe each union "ratifying [an] agreement under the mandate."[^fin2024]
4. **The employer pays it; the province funds the employer.** Once in the ratified agreement the increase is a contractual obligation the employer (health authority, district, Crown corporation) must pay — funded through the provincial budget that sized the envelope in step 1.

So PSEC effectively sets **both ends of the range at once**:

- **The floor** — the mandate figure (3%/yr for 2025–2029) is the *funded amount everyone gets*; it is not withheld.
- **The ceiling** — the **"me too" / NCI Letter of Agreement** (§5.7) stops any union from getting *more* without every union getting it too. That is the clause that caps the upside, **not** the one that delivers the base increase.

The practical consequence is that the wage *number* is largely pre-set and pre-funded, so a union's real bargaining room is on **non-wage structure** (premiums, benefits, staffing, workload) — though the 2025 NCI model now sweeps much of that into the comparison too (§5.7). *(This describes the normal negotiated path; where bargaining fails, the province's fallbacks are mediation or, rarely, back-to-work / imposed legislation — outside this analysis's scope.)*

---

## 2. What the mandate INCLUDES (the wage envelope)

| Year (effective) | Guaranteed base GWI | COLA top-up | Stated maximum | Triggered? |
|---|---|---|---|---|
| **Year 1** (Apr 1, 2022) | **$0.25/hr flat** (a greater % for lower-paid) **+ 3.24%** | — | — | n/a |
| **Year 2** (Apr 1, 2023) | **5.5%** | up to **+1.25%** | **6.75%** | ✅ **Mar 21, 2023** |
| **Year 3** (Apr 1, 2024) | **2%** | up to **+1.0%** | **3%** | ✅ **Mar 19, 2024** |

Sources: PSEC mandate page;[^psec] launch release;[^fin2022] HEABC.[^heabc]

Plus a **negotiable "flexibility allocation" of up to 0.25% in Years 1 and 2** — conditional, mutually agreed, and may be zero.[^fin2022][^psec]

**For nurses specifically**, Year 1's dollar-plus-percent works out to an **average of ~3.82%** across the grid, which is exactly how Article 63 states it.[^repo63][^nbapca]

---

## 3. The COLA mechanism in detail

The COLA is a **capped inflation top-up**, not uncapped inflation protection. Per the government releases, it is:

> "based on the **annualized average of B.C. CPI over the previous 12-month period of March to February**… The amount of the additional increase is the **difference between the 12-month average and the guaranteed general wage increase, up to the maximum**."[^fin2024][^fin2023]

The NBA's **Appendix VV** defines the same peg precisely — the "annualized average of BC CPI over twelve months" (**AABC CPI**) is "the Latest 12-month Average Index % Change reported by **BC Stats** in March… twelve months starting at the beginning of March in the preceding year and concluding at the end of the following February," calculated to one decimal (reference: Mar 2021–Feb 2022 = 3.4%).[^repovv]

**Both maxima were reached** because inflation overshot the caps:

| Year | 12-month BC CPI avg | Base GWI | Gap vs. base | Cap | Result |
|---|---|---|---|---|---|
| Year 2 | **7.1%** (Mar 2022–Feb 2023) | 5.5% | 1.6% | 1.25% | Cap binds → **6.75%** total |
| Year 3 | **3.4%** (Mar 2023–Feb 2024) | 2% | 1.4% | 1.0% | Cap binds → **3%** total |

Sources: PSEC page;[^psec] 2023FIN0022;[^fin2023] 2024FIN0013;[^fin2024] HEABC.[^heabc] BCNU confirmed nurses received the full **3%** (2% GWI + 1% COLA) effective April 1, 2024.[^bcnunews]

> **Note on framing:** the mandate expresses the ceiling as a single number (6.75% / 3%), while NBA **Article 63 and Appendix VV express the COLA as an additive cap (+1.25% / +1.0%)** on the base GWI — Article 63 never uses "6.75%" or "3%." Same economics, two notations.[^repo63][^repovv]

---

## 4. What the mandate does NOT include / explicitly excludes

- **No matching obligation *in the mandate itself*.** Nothing in the 2022 Shared Recovery Mandate or the *Public Sector Employers Act* tops up an earlier-settling union if a later one obtains a richer envelope. Any "me too" protection that exists lives in an *individual union's* collective agreement, not in the mandate — and it is not universal (see §5).[^heufba][^academic]
- **No uncapped inflation protection.** The COLA is explicitly capped; CPI above GWI + cap is **not** recovered. Had CPI come in *below* the base GWI, the COLA would have paid **zero** (the trigger is conditional on CPI exceeding the base).[^repovv][^fin2024]
- **Not retroactive / not a lump sum.** COLA folds permanently into all wage rates going forward.[^repovv]
- **Coverage boundary.** Applies to employers whose collective agreements **expired on or after Dec 31, 2021**.[^psec] Excluded/management and non-unionized staff are handled separately; bargaining units that expired earlier fall outside the mandate.

---

## 5. How "me too" / comparability *actually* operates in BC

There are **two distinct mechanisms**, and they are easy to conflate:

1. **Structural uniformity (the mandate).** PSEC sets one identical envelope for every employer under the *Public Sector Employers Act*, and each union ratifies its own agreement within it.[^psea][^academic] By March 2024, "**more than 400,000 or 99% of unionized provincial public-sector employees**" were covered by agreements reached under the mandate — teachers and K-12 support staff, all post-secondary and research universities, health-sector employees, community social services, and most Crown corporations.[^fin2024] This breadth is the product of **statutory employer-side coordination, not an inter-union pact.** It is what keeps everyone *at* the mandate.

2. **A standardized "Public Sector Wage Increases" me-too LOA (in most other unions' agreements — but *not* the NBA's).** Separately from the mandate, PSEC inserts a **standard, identically-worded Letter of Agreement** — its document title is literally *"LOA Public Sector Wage Increases (Me Too) Sep 2, 2022"* — into public-sector collective agreements.[^bcgeuloa] It is **confirmed in the BCGEU public-service agreement**[^bcgeuloa] and HEU's Facilities agreement (*"if any other BC public sector union bargains higher wage increases during this round, FBA would get that same wage increase"*),[^heufba] and the companion audit reports it across CSSEA/CBA, HSPBA, K-12 and university agreements as well.[^metoo] It is a contract term binding **the employer**, not a promise among unions. **The NBA/nurses agreement contains no such LOA** — verified against the full A→CCC appendix index of the NBA PCA (there is no "Public Sector Wage Increases" MOA), and consistent with public BCNU/HEABC materials.[^nbapca] The companion audit's suggestion that the NBA was nonetheless "bound by identical underlying language" is **speculation the agreement text does not support.**

**Why this distinction matters for nurses:** because HEU-style me-too clauses are pegged to "higher **wage increases**" (GWI), value the NBA took *outside* the GWI — premiums and ratios (§5.5) — would not, on its face, trigger another union's GWI-based me-too. This is a plausible reading of how the NBA could exceed the mandate's per-hour value without a province-wide spillover, but it is an **inference**, not a sourced statement of intent.

---

## 5.5 What nurses got OUTSIDE the mandate's GWI envelope

The mandate fixes the **GWI + COLA**. It does not cap classification-specific **premiums**, which the NBA bargained separately and which sit on top of the mandate wage. The largest is new:

- **Article 28.05 — Regular Premium:** "Effective April 1, 2023, **all regular employees will be paid a premium of $2.15 per hour for each hour worked excluding overtime**."[^repo28] At ~1,950 straight-time hours/year this is roughly **$4,000+/year** for a full-time nurse — a gain comparable in size to a full year's GWI, but *not* counted as GWI.
- **Article 28.01 — shift premiums raised** April 1, 2023: evening $1.05 → **$1.40**, night $4.25 → **$5.00**; weekend (28.02) $2.90 → $3.50; super-shift (28.03) $1.40 → $1.85.[^repo28]
- **Article 28.06 — new OR/PAR/ER/ICU/CCU premium** of $2.00/hr for permanently assigned staff, eff. April 1, 2023.[^repo28]
- **Article 57.05(B) — BCCNM registration fee** now fully **reimbursed by the employer**, not pro-rated by FTE.[^repo57]

These are NBA-specific, premium-and-conditions gains *layered on* the common GWI — which is how nurses' total package can exceed the bare mandate figure while the **GWI itself stays uniform** with the rest of the public sector. *(Caveat: a popular claim that the negotiable **0.25% flexibility allocation** specifically "funded" these items could not be sourced, and the $2.15 premium alone far exceeds a 0.25% envelope — so no funding-attribution is asserted here.)*

---

## 5.6 Successor context: the 2025 Balanced Measures Mandate

The 2022 Shared Recovery Mandate is a closed cycle (expired March 31, 2025). Its successor, the **2025 Balanced Measures Mandate**, is a **four-year** mandate providing a **3% general wage increase in each year (2025–2028)** plus a **flexibility allocation of 0.2% in years two and four** — and, unlike its predecessor, **no inflation-linked COLA**.[^psec2025] It also **replaces the GWI-only me-too with a broader "Net Compensation Increases" (NCI) test** that now captures wage *and* benefit increases and even flexibility allocations (detailed in §5.7).[^cba2025] Bargaining under it was still in progress as of this writing.

---

## 5.7 Origin and mechanics of the cross-union me-too LOA

*(This section incorporates findings first raised by a companion AI-research audit (`[^metoo]`, a private working document) that were then **verified against the underlying LOA text**, extracted directly from the primary tentative-agreement PDFs. Claims confirmed from that primary text are marked **[verified — primary text]**; the one element still resting on inference — *why* the 2025 NBA-only carve-out exists — is flagged where it appears.)*

**Why the 2022 me-too is GWI-only — the 2014–2019 Hall arbitration. [verified]** During the 2014–2019 round the government told health-sector unions that moving extended-health benefits into a joint trust was mandatory, but then signed an NBA agreement that *omitted* the joint trust, leaving nurses better off. The Health Science Professionals Bargaining Association invoked its (then broadly worded) me-too clause. **Arbitrator John Hall** ruled the employer had breached the HSPBA agreement and awarded **$9.44 million plus interest** to HSPBA members (decision **September 28, 2022**; later treated as funding for a classification redesign).[^hall] The lesson — that a me-too keyed to "overall compensation" exposes the treasury to large, unpredictable liabilities whenever a powerful outlier like the NBA wins a concession — is why the 2019 and 2022 LOAs were rewritten to trigger **only on general wage increases**, deliberately excluding premiums, benefits and market adjustments.[^metoo]

**How the 2022 trigger works. [verified — primary text]** The full LOA text was extracted from a primary source (the CSSEA community-social-services tentative agreement, p. 25, which carries a clean text layer) and reads, in its operative part:[^loatext]

> *"If a public sector employer… enters into a collective agreement with an effective date after December 31, 2021 and the first three years of the collective agreement under the Shared Recovery Mandate includes cumulative nominal (not compounded) general wage increases (GWIs) and Cost of Living Adjustments (COLAs)… [that] are paid out and exceed the sum of the GWIs and COLAs that are paid out in the [comparator] Collective Agreement, the total GWIs and COLAs paid out will be adjusted on the third anniversary… so that the cumulative nominal… GWIs and COLAs are equivalent. This Letter of Agreement is not triggered by any wage increase or lump sum awarded as a result of binding interest arbitration."*

Each LOA benchmarks against a comparator agreement — in the BCGEU version, explicitly the **19th Main Public Service Agreement**; in the CSSEA version, "the Collective Agreement" — and trues up on the **third anniversary**. Because the trigger is GWI+COLA only, value taken *outside* the GWI does not set it off — exactly the lane the NBA used (§5.5).

**The specific arithmetic. [verified — primary text]** Paragraph 2 defines a **$0.25/hr flat raise as a 0.5% GWI** "notwithstanding what it actually represents," and states: *"the combined GWIs of $0.25 per hour and 3.24% in Year 1 are considered to be a single increase of 3.74% for this LOA. For example purposes only, combining the 3.74%… in Year 1 with the maximum potential combined GWI and COLA increases of 6.75% in Year 2 and 3% in Year 3 would result in a cumulative nominal increases of 13.49% over three years."*[^loatext] So **13.49% is the LOA's own worked example** of the maximum cumulative-nominal increase another union would have to *exceed* to trigger matching — framed as illustrative, not a hard contractual ceiling. (Separately, the *realized average* increase was reported at ≈**13.75%**, a different measure.)[^bcgeu675]

**The exclusions (the loophole). [verified — primary text; corrects the audit]** Paragraph 3 states a GWI *"is one that applies to all members of a bargaining unit (e.g. everyone receives an additional $0.25 per hour, $400 per year, or 1% increase) and does not include wage comparability adjustments, lower wage redress adjustments, labour market adjustments, **flexibility allocations, classification system changes**, or any compensation increases that are funded by equivalent collective agreement savings or grievance resolutions."*[^loatext] Two notes: the companion audit's "service improvement allocations" is **not** in the actual text (the real list is the one quoted), and **flexibility allocations are themselves explicitly excluded** — so the 0.25% flexibility allocation (§2) could never trigger another union's me-too. Premiums are not named, but fall outside because a GWI must apply "to all members" and is a base-rate increase, whereas premiums are paid per hour-worked under specified conditions.

**The 2025 successor and the NBA carve-out. [verified — primary text]** The 2025 CBA tentative agreement **deletes the old "Memorandum of Agreement Re: Public Sector Wage Increases" and replaces it with a "Net Compensation Increases (NCI)" LOA** — quoted here from the 2025 CBA full tentative-agreement PDF (p. 2 of 4).[^cba2025] The NCI trigger is structurally the same as the 2022 me-too (cumulative nominal increases trued up to a comparator, now on the **fourth anniversary**) but the *measure* is far broader: an NCI is *"an increase to the total compensation envelope… expressed as a percentage increase to the combined **wages and wage-impacted benefits** (W&WIB) compensation base"* — and, reversing the 2022 rule, **flexibility allocations now count** (*"a 0.2% flexibility allocation shall be treated as a 0.2% NCI"*). The CBA's own four-year baseline is fixed at **12.4%**, plus "all other negotiated increases… including any low wage and benefit redress adjustments." This closes the premium loophole the NBA used in 2022 — any new money, not just GWI, now counts.

The audit's most striking claim — an explicit **NBA-only carve-out** — is **confirmed verbatim.** Among the NCI exclusions (line, p. 2): low-wage/benefit redress for CSSBA/BCGEU units; post-ratification labour-market adjustments; CUPE 873 paramedic increases; savings-funded compensation; untied policy funding; PSEA designation increases; *"**relief from provisions in a prior collective agreement that were to become effective after the term of the prior collective agreement for the NBA collective agreement only**"*; interest-arbitration awards; and grievance resolutions.[^cba2025] The carve-out **exists exactly as quoted**. What remains the audit's *inference* — not established by the text — is *why* it exists (its theory: the 2022 deal promised the NBA delayed relief that the government pre-immunised from the 2025 me-too). The literal effect is clear: when the NBA receives that delayed prior-agreement relief, it will not trigger a province-wide NCI match.

---

## 6. The bottom line

The document you can actually point to and read is the **PSEC "2022 Shared Recovery Mandate" page** — that *is* the authoritative public statement of the instrument, and there is no richer or more recent source.[^psec] Its legal force runs **government → PSEC → employers' associations (via the *Public Sector Employers Act*) → each union's collective agreement.**[^psea] There is **no signed inter-union "me too" agreement** behind it; for nurses, the mandate is operationalised in **Article 63 + Appendix VV** of the NBA 2022–2025 agreement.[^repo63][^repovv]

---

## 7. What this analysis could not verify

Honesty about the gaps, so you can weigh the evidence yourself:

1. **No standalone signed mandate instrument or Order in Council with a citable document number was located.** The mandate appears to exist as the published gov.bc.ca/PSEC description plus its replication into each collective agreement — *not* as a single executed contract. Whether a formal written PSEC/Treasury Board instrument exists behind the web page is **unresolved**.
2. **The statute never uses the words "Shared Recovery Mandate."** Treating it as a s. 4 "strategic direction" is a well-grounded **inference** from PSEC practice, not an explicit statutory label. (This characterization was the single least-consensus element in verification — a 2-1 vote — though the underlying statutory quotes are uncontested.)
3. **The me-too / NCI LOA text is now fully verified — only one *interpretation* remains inferential.** The 2022 LOA's full text (trigger, $0.25 = 0.5% convention, 13.49% worked example, exclusions) is confirmed from the BCGEU[^bcgeuloa] and CSSEA[^loatext] versions; its *absence* from the NBA agreement is confirmed against the full A→CCC appendix index;[^nbapca] and the 2025 **NCI model and the NBA-only carve-out are confirmed verbatim** from the 2025 CBA tentative agreement.[^cba2025] The single thing the primary text does **not** establish is the audit's *theory of why* the NBA carve-out exists (a claimed 2022 promise of delayed relief) — the clause's existence and literal effect are verified; its backstory is inference.
4. **How the up-to-0.25% flexibility allocation actually resolved in the NBA agreement** — whether any portion was used and on what — was not established. A reviewer's suggestion that it funded the BCCNM reimbursement and shift-premium increases is **plausible but unsourced**, and cannot explain the much larger Article 28.05 premium.
5. **The 400,000 / 99% coverage** is a March 2024 snapshot of "tentative or ratified agreements reached under the mandate," slightly narrower than "the mandate applies to."

---

### Footnotes / source links

[^psec]: PSEC, "Public sector bargaining — mandates and agreements," gov.bc.ca: https://www2.gov.bc.ca/gov/content/employment-business/employers/public-sector-employers/public-sector-bargaining/mandates-and-agreements
[^psea]: *Public Sector Employers Act* [RSBC 1996] c. 384: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96384_01 (ss. 4, 7(1)(c.1), 14.3)
[^psecrole]: PSEC, "Public Sector Bargaining" landing page: https://www2.gov.bc.ca/gov/content/employment-business/employers/public-sector-employers/public-sector-bargaining ("the PSEC Secretariat coordinates bargaining with unions through sectoral employers' associations and protects the interests of taxpayers by ensuring public sector compensation costs are aligned with the fiscal plan through the budget objectives set by government")
[^fin2022]: BC Government news release 2022FIN0075-001756: https://news.gov.bc.ca/releases/2022FIN0075-001756
[^fin2023]: BC Government news release 2023FIN0022-000361: https://news.gov.bc.ca/releases/2023FIN0022-000361
[^fin2024]: BC Government news release 2024FIN0013-000387: https://news.gov.bc.ca/releases/2024FIN0013-000387
[^heabc]: HEABC COLA Announcement, 22 March 2023: https://www.heabc.bc.ca/public/News/2023/COLA-Announcement_22March2023.pdf
[^heabcsum]: HEABC, NBA 2022–2025 Summary of Changes: https://www.heabc.bc.ca/public/CAs/NBA/2022-2025_SummaryofChanges_NoInterps.pdf
[^nbapca]: NBA Provincial Collective Agreement 2022–2025: https://www.bcnu.org/Contracts-Bargaining/Documents/nba-pca_2022_2025.pdf
[^bcnunews]: BCNU, "NBA collective agreement wage increase includes cost-of-living adjustment," 21 March 2024: https://www.bcnu.org/news-and-events/news/2024/nba-collective-agreement-wage-increase-includes-cost-living-adjustment
[^repo63]: NBA Provincial Collective Agreement 2022–2025, **Article 63** (General Wage Increases). Working-corpus transcription of the public NBA PCA (<https://www.bcnu.org/Contracts-Bargaining/Documents/nba-pca_2022_2025.pdf>).
[^repovv]: NBA PCA 2022–2025, **Appendix VV** (Cost of Living Adjustment definitions). Working corpus; public NBA PCA as above.
[^repo28]: NBA PCA 2022–2025, **Article 28** (Premiums) — 28.05 Regular Premium $2.15/hr eff. April 1, 2023; 28.01 shift premiums; 28.06 OR/PAR/ER/ICU/CCU premium. Working corpus; public NBA PCA as above.
[^repo57]: NBA PCA 2022–2025, **Article 57.05(B)** (BCCNM registration fee reimbursement). Working corpus; public NBA PCA as above.
[^heufba]: HEU, Facilities Bargaining Association FAQs: https://www.heu.org/fba-faqs ("we have a 'me too' clause in our agreement that if any other BC public sector union bargains higher wage increases during this round, FBA would get that same wage increase")
[^psec2025]: PSEC, 2025 Bargaining Update (Balanced Measures Mandate): https://www2.gov.bc.ca/assets/gov/british-columbians-our-governments/services-policies-for-government/public-sector-management/psec/2025-bargaining-update.pdf ; PSEC bargaining landing page: https://www2.gov.bc.ca/gov/content/employment-business/employers/public-sector-employers/public-sector-bargaining
[^bcgeuloa]: BCGEU agreements database, "LOA Public Sector Wage Increases (Me Too) Sep 2, 2022": https://agreements.bcgeu.ca/document/eU9xYm95Z004clk9 (BCGEU version; comparator = 19th Main Public Service Agreement; full operative text verified)
[^loatext]: CSSEA, "2022/23 Collective Bargaining – CSSEA and CSSBA Tentative Agreements – Summary of Changes," p. 25, "PUBLIC SECTOR WAGE INCREASES LETTER OF AGREEMENT (\"me-too\" clause)." Public source PDF (has a text layer; operative clauses quoted inline in §5.7): <https://www.cssea.bc.ca/PDFs/Bargaining/2022/TentativeAgreementsFebruary2022.pdf>
[^cba2025]: 2025–2029 Health Services & Support – Community Subsector Bargaining Association (CBA) Full Tentative Agreement, "CBA Net Compensation Increases" LOA, p. 2 of 4. Public source PDF (has a text layer; operative clauses, incl. the NBA-only carve-out, quoted inline in §5.7): <https://www.bcnu.org/files/2025-2029_CBA_Full_Tentative_Agreement.pdf>
[^bcgeu675]: BCGEU, "April 1, 2023 general wage increase for BCGEU public service members will be 6.75%": https://www.bcgeu.ca/april_1_2023_general_wage_increase_for_bcgeu_public_service_members_will_be_6_75
[^hall]: HSA, "HSA wins $10 million settlement for health science professionals": https://hsabc.org/news/hsa-wins-10-million-settlement-health-science-professionals ; CUPE BC Health, "HSA legal challenge results in nearly $10 million payout for HSPBA members": https://bcchs.cupe.ca/2022/10/03/hsa-legal-challenge-results-in-nearly-10-million-payout-for-hspba-members/
[^metoo]: Companion AI-research audit (external deep-research model), a **private working document — referenced, not republished**. Used only as a lead; every load-bearing claim it raised (LOA ubiquity, the 13.49% worked example, the exclusions, the 2025 NCI model and NBA-only carve-out) was independently verified against the primary LOA text cited above, and one exclusions-list error in it was corrected.
[^uvic]: UVic Bargaining, "PSEC": https://www.uvic.ca/bargaining/home/psec/index.php
[^academic]: Academic Matters, "Bargaining in the shadow of BC's Public Sector Employers' Council": https://academicmatters.ca/bargaining-in-the-shadow-of-bcs-public-sector-employers-council/
[^law]: Canadian Lawyer, "BC to increase general wages for public sector employees under 2022 Shared Recovery Mandate": https://www.canadianlawyermag.com/news/general/bc-to-increase-general-wages-for-public-sector-employees-under-2022-shared-recovery-mandate/372488
