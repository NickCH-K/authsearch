# Project Goal

## Objective

Compile a list — **as comprehensive as possible** — of **many-analyst studies**,
and for each one collect contact information for the project's **organizing
author(s)**.

## What counts as a "many-analyst study"

A study in which **the same research task is completed multiple times by
multiple independent teams of analysts**. The teams all attack the *same*
question/data, and the study compares how their results differ.

Canonical examples: Silberzahn et al. (2018) "Many Analysts, One Data Set";
Botvinik-Nezer et al. (2020) NARPS neuroimaging; Huntington-Klein et al. (2021)
hidden researcher decisions in economics; Menkveld et al. (2024) "Nonstandard
Errors" in finance.

## What does NOT count (exclude these)

- **Multiverse / specification-curve studies**: a *single* author/team tries
  many different analytic approaches themselves (e.g. "I Just Ran Four Million
  Regressions", forking-paths papers). Distinct because it is one team, not many.
- **Replication projects**: many teams each replicate a *different* single study
  (e.g. Many Labs, Camerer et al. reproducibility projects, mass-reproducibility).
  Distinct because the teams do *different* tasks, not the *same* one.
  (Borderline: a project where many teams all reproduce the *same* observational
  study — e.g. Ostropolets et al. 2023 — counts, because the task is shared.)
- **Commentary / re-analysis** of an existing many-analyst dataset (e.g. Auspurg
  & Brüderl re-analyzing the Silberzahn data) — note the *underlying* study, but
  the commentary itself is not a new many-analyst study.
- **Methodology papers** about how to run many-analyst studies (unless they also
  contain an original many-analyst study).

When in doubt, the test is: **Did many independent teams each perform the SAME
task on (broadly) the SAME data?** If yes → include.

## Who we want contact info for

Only the **main organizing author(s)** of the project — the people who designed
and ran it. **NOT** the full roster of participating analysts (many of these
papers list dozens-to-hundreds of contributing analysts as co-authors; we do not
want those).

Most studies have ONE organizer → one row. Some have several (e.g.
Huntington-Klein & Pörtner) → one row per organizer.

## Output

`Contact Info.xlsx` with columns:

| Study Name | Link (DOI preferred) | Organizer Name | Organizer Email | Organizer Phone | Organizer Affiliation | Notes |

- One row per organizer.
- If a study is a good fit but no contact can be found for an organizer, still
  add the row with `FAILED TO FIND` in the email column.

## The process (loop)

Maintained as a work queue in `Papers to Check.txt`. For each entry:

1. Look it up online; confirm it's a many-analyst study. If not → move to
   `Studies Checked but Inappropriate.txt` with a reason.
2. If yes → find organizer(s) + contact info → add row(s) to `Contact Info.xlsx`.
3. Mine (a) the study's own reference list and (b) Google Scholar "cited by"
   for further many-analyst studies (be fairly confident before adding). Append
   any genuinely new ones to `Papers to Check.txt`.
4. Remove the finished entry from `Papers to Check.txt`.

Iterate until `Papers to Check.txt` is empty. Then do fresh Google Scholar
searches for more many-analyst studies, add new finds to the queue, and repeat
until the queue is empty again.

## Seed material

Two example PDFs are in the repo root:
- `Huntington-Klein et al 2021 The Influence of Hidden Researcher Decisions.pdf`
- `2026-06-jel-resubmission-2nd.pdf` (Huntington-Klein & Pörtner, "The Sources of
  Researcher Variation in Economics", a review that cites many of these studies)

The initial `Papers to Check.txt` was seeded from the many-analyst studies these
two papers cite.
