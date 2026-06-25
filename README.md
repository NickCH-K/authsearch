# Many-Analyst Studies — Contact Compilation

A research project to compile the most comprehensive possible list of
**many-analyst studies** (studies where the same research task is completed
independently by many teams of analysts) and to collect contact information for
each study's **organizing author(s)**.

## Repository layout

| Path | What it is |
|------|------------|
| `GOAL.md` | The goal, the precise definition of a many-analyst study, and the inclusion/exclusion rules. **Read this first.** |
| `CLAUDE.md` | How to resume the project in a fresh session (this is a long-running, resumable task). |
| `PROGRESS.md` | Live status log: where the last session stopped, running tallies, search terms tried. |
| `Papers to Check.txt` | The work queue — candidate studies not yet processed. |
| `Contact Info.xlsx` | **The deliverable** — confirmed studies + organizer contacts, one row per organizer. |
| `Studies Checked but Inappropriate.txt` | Candidates that were checked and rejected (with reasons), so they're never rechecked. |
| `scripts/contacts.py` | CLI helper to add/list rows in `Contact Info.xlsx`. |
| `scripts/extract_pdf.py` | Extract text from a PDF into `scratch/`. |
| `*.pdf` | The two seed papers the project started from. |
| `scratch/` | Throwaway extracted text; not part of the deliverable. |

## Contact Info.xlsx columns

`Study Name | Link (DOI preferred) | Organizer Name | Organizer Email | Organizer Phone | Organizer Affiliation | Notes`

## The workflow in brief

1. Take a candidate from `Papers to Check.txt`.
2. Confirm it's a many-analyst study (else file it under inappropriate).
3. Record the organizer(s) and their contact info in `Contact Info.xlsx`.
4. Mine its references and citations for more many-analyst studies → back to the queue.
5. Remove it from the queue. Repeat until empty, then search for more.

See `GOAL.md` and `CLAUDE.md` for full detail.

## Setup

```bash
pip3 install pypdf openpyxl cffi
```
