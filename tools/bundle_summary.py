#!/usr/bin/env python3
"""Regenerate SUMMARY-FULL.md by bundling SUMMARY.md + every per-article file in
summaries/ into one document.

The bundle order is derived from the index links in SUMMARY.md (the lines that
look like `](summaries/<name>.md)`), so SUMMARY.md + the summaries/ files are the
single source of truth. Run after editing any of them:

    python tools/bundle_summary.py

By default it operates on the repository root (the directory containing
SUMMARY.md, summaries/, and SUMMARY-FULL.md). Pass a different directory as the
first argument to override. No third-party dependencies; standard library only.
"""
import re
import sys
from pathlib import Path

PREAMBLE = (
    "<!-- AUTO-GENERATED: this file bundles SUMMARY.md + every per-article summary in summaries/\n"
    "     into one shareable document. Regenerate after edits; do not hand-edit. -->\n"
    "\n"
    "# BCNU 2025–2029 Settlement — Full Gains/Losses Vote Guide (single document)\n"
    "\n"
    "*This one file combines the at-a-glance overview with the complete per-article/appendix/MOA\n"
    "breakdowns, for easy sharing. The overview comes first; every detailed summary follows below\n"
    "in the same order as the index.*\n"
    "\n"
    "---\n"
    "\n"
    "\n"
)

MIDSEP = (
    "\n\n\n---\n\n"
    "# Per-article / appendix / MOA detail — full breakdowns\n"
    "\n\n\n---\n\n"
)

ITEMSEP = "\n\n\n---\n\n"

LINK_RE = re.compile(r"\]\(summaries/([^)]+\.md)\)")


def main() -> int:
    base = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    summary_path = base / "SUMMARY.md"
    out_path = base / "SUMMARY-FULL.md"

    summary_text = summary_path.read_text(encoding="utf-8")

    # Derive bundle order from the index links, de-duplicated, order-preserving.
    order = []
    seen = set()
    for name in LINK_RE.findall(summary_text):
        if name not in seen:
            seen.add(name)
            order.append(name)

    missing = [n for n in order if not (base / "summaries" / n).exists()]
    if missing:
        print("ERROR: index references missing summary files:", missing, file=sys.stderr)
        return 1

    items = [
        (base / "summaries" / name).read_text(encoding="utf-8").rstrip("\n")
        for name in order
    ]

    parts = [PREAMBLE, summary_text.rstrip("\n"), MIDSEP, items[0]]
    for it in items[1:]:
        parts.append(ITEMSEP)
        parts.append(it)
    result = "".join(parts) + "\n"

    out_path.write_text(result, encoding="utf-8")
    print(f"Wrote {out_path} ({len(order)} sections bundled).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
