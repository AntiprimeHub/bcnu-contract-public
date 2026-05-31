# How this guide was made

This page is the honest account of how the summaries in this repository were
produced — what was automated, what AI did, what a human did, and where the
limits are. It's here so you can judge how much to trust the guide and (most
importantly) verify the parts that matter to you against the official documents.

## The two source documents

1. **The in-force 2022–2025 Provincial Collective Agreement** — the contract
   currently in effect. Its PDF contains real, selectable text.
2. **The 2025–2029 Terms of Settlement booklet** — the deal being voted on. The
   pages that show contract language are **scanned/pasted images** with tracked
   changes: **underlined = newly added**, **struck through = deleted**.

The whole guide is essentially a careful diff between these two documents.

## Step 1 — The baseline (automated text extraction)

The in-force 2022–2025 agreement was converted from PDF to Markdown with a small
text-extraction script (`pdf_to_markdown.py`, part of a separate working corpus,
**not included here** — it only handles text-based PDFs). That produced the
**baseline**: "what the contract says today," which every change is measured
against.

## Step 2 — The changes (AI vision transcription of the image pages)

The settlement booklet's tracked-change pages are **images**, not text. Ordinary
OCR can read the words but **cannot tell underline from strikethrough** — and that
distinction (new vs. deleted) is the entire signal. So those pages were
transcribed **at scale using an AI vision model (Anthropic's Claude)**: each page
image was read and re-recorded with the markup preserved — underline → new text,
strikethrough → deletion — page by page across the booklet.

**This is stated plainly because it matters: AI transcription can make mistakes** —
misreading a number, missing a strike, mis-classifying a line. The next two steps
exist specifically to catch them.

## Step 3 — Cross-check against the baseline

A change can also be slipped in *without* being marked — text that looks like
unchanged "context" but actually differs from the in-force agreement. To catch
that, each amended provision's "before" text was diffed against the Step-1
baseline. This is how the unmarked / "silent" edits flagged in the guide were
found.

## Step 4 — Plain-language summaries + a line-by-line reference audit

Each article, appendix, and MOA was summarized into **gains / losses / neutral /
watch-outs** with clause and page citations. Those summaries were then put through
a **line-by-line reference audit**: every dollar figure, date, count, and
gain/loss classification was re-checked against the transcription and the
baseline. Corrections from that audit are in this repository's commit history —
for example, a benefit that was already in the old contract being mislabeled as a
new "gain," and a community-list miscount, were both caught and fixed.

Both the transcription and the verification were **AI-assisted and
human-directed**: a person set up the process, reviewed the findings, and
spot-checked specific items directly against the source page images.

## Honest limitations

- **It's a diff of a booklet, not the executed contract.** Where the booklet and
  the final signed agreement differ, the signed agreement governs.
- **AI was used heavily** — for both the image transcription and the verification.
  Despite the cross-check and audit, errors are possible. Treat every figure as
  "verify before you rely on it."
- **The working corpus isn't published here.** The `Source:` / `Baseline:` lines
  at the top of each summary point to that private corpus (the transcriptions and
  the baseline), so those paths won't resolve in this repository.

## Reproduce / check this repository

The combined [`SUMMARY-FULL.md`](SUMMARY-FULL.md) is **generated, not
hand-written** — it is [`SUMMARY.md`](SUMMARY.md) plus every file in
[`summaries/`](summaries/), bundled in index order. You can regenerate it and
confirm it matches what's published (Python 3, standard library only — no
dependencies):

```
python tools/bundle_summary.py
git diff SUMMARY-FULL.md      # should show no changes
```

## A different kind of document: the EFNBT deep-dive

[EFNBT-BENEFITS-TRUST-ANALYSIS.md](EFNBT-BENEFITS-TRUST-ANALYSIS.md) was **not**
built the way the summaries above were. It is not a transcription diff — it is a
researched analysis that combines two things: (a) the settlement's own
benefit-trust documents (the EFNBT funding formula and the health-and-welfare
MOAs), and (b) **external, publicly-citable evidence** on how jointly-trusteed and
multiemployer benefit trusts have performed elsewhere (US Taft-Hartley health
funds, the multiemployer pension solvency crisis, BC's existing Joint Benefits
Trusts, and others).

Every external claim was put through an **adversarial multi-agent verification
pass** — a claim was dropped unless it survived independent attempts to refute it
— and the most load-bearing sources were re-fetched and checked against their
quoted text. Its full methodology, complete source list (with working links), and
honesty caveats are documented **inline** at the top and bottom of that file. As
with everything here, it is **AI-assisted and human-directed**, independent and
unofficial, and where it disagrees with the official documents, the official
documents govern.

## Verify against the official source

This guide is a reading aid, not the contract. Before you vote, get the
**official 2025–2029 Terms of Settlement** from your union and check anything that
affects you against it. **Where this guide and the official documents disagree,
the official documents win.**
