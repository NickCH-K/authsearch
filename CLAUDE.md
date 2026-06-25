# CLAUDE.md — Instructions for resuming this project

This is a **long-running research task** that may be interrupted (e.g. running
out of tokens) and resumed in a fresh session. Everything needed to pick the work
back up lives in this repo. Read this file first, then `PROGRESS.md`.

## What this project is

See `GOAL.md` for the full goal and the precise definition of a "many-analyst
study". In one line: build the most comprehensive possible list of many-analyst
studies and collect contact info for each study's *organizing* author(s).

## How to resume (do this on every restart)

1. Read `GOAL.md` (definition + inclusion/exclusion rules) and this file.
2. Read `PROGRESS.md` — it records exactly where the last session stopped, the
   running tallies, and any in-flight notes.
3. Look at the three live data files:
   - `Papers to Check.txt`   — the work queue (candidates not yet processed).
   - `Contact Info.xlsx`     — confirmed studies + organizer contacts (the deliverable).
   - `Studies Checked but Inappropriate.txt` — rejected candidates (don't recheck).
4. Continue the loop below from wherever the queue stands.

## The loop (per entry in `Papers to Check.txt`)

For the **top entry** in the queue:

1. **Verify** via web search/fetch that it is a genuine many-analyst study
   (same task, many independent teams). Use the exclusion rules in `GOAL.md`.
   - If NOT → append it to `Studies Checked but Inappropriate.txt` with a REASON,
     remove it from the queue, and move on.
2. **Find organizer(s) + contact info.** The organizers are usually the first
   1-3 listed/corresponding authors, NOT the big roster of participating analysts.
   Look at: the paper's title page / corresponding-author footnote, the project
   website / OSF page, and author faculty pages for email/phone/affiliation.
   Add one row **per organizer** with `scripts/contacts.py add`. Prefer a DOI link.
   - If a good study but no contact found for an organizer → still add the row,
     put `FAILED TO FIND` in the email field.
3. **Expand the frontier.** (a) Scan the study's reference list for other
   many-analyst studies; (b) check Google Scholar "cited by" for papers that are
   clearly many-analyst. Be *fairly confident* before adding (the search space
   explodes otherwise). Append genuinely new candidates (not already in any of
   the three files) to `Papers to Check.txt`.
4. **Remove** the finished entry from `Papers to Check.txt`.
5. Update `PROGRESS.md` (tallies + last action) periodically — at least every
   few entries and before stopping.

When the queue empties: run fresh Google Scholar / web searches for more
many-analyst studies (search terms in `PROGRESS.md`), enqueue new finds, repeat
until empty again.

## Tools & conventions

- **Add a contact:** `python3 scripts/contacts.py add --study "..." --link "..."
  --organizer "..." --email "..." --phone "..." --affiliation "..." --notes "..."`
  (idempotent on study+organizer, so safe to re-run.)
- **Inspect output:** `python3 scripts/contacts.py list` / `... studies`.
- **Extract a PDF:** `python3 scripts/extract_pdf.py file.pdf` → `scratch/`.
- `scratch/` holds throwaway extracted text; not part of the deliverable.
- Dedupe every new candidate against all three files before enqueuing.
- Keep `PROGRESS.md` honest and current — it is the single source of truth for
  "where are we". A resuming session trusts it.

## Environment notes

- `pypdf`, `openpyxl`, `cffi` are pip-installed (rebuild with
  `pip3 install pypdf openpyxl cffi` if a fresh container loses them).
- PDF page-image rendering is unavailable; use `scripts/extract_pdf.py` for text.
- Web access is via `WebSearch` / `WebFetch` tools.
