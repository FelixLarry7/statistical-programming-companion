# Stage 8 technical and editorial review

19 November 2026

This record documents an AI-assisted technical and editorial assessment
against the master blueprint. It covers all forty chapter sources, ten
part openers, twenty-one appendices, the shared reference and notation
files, the twelve project packs and the stated instructor-solution scope.
The work is not an independent human review and carries no Wiley or
Routledge affiliation, appointment, acceptance or certification.

## Completed work

The edited source includes the P03 three-point decision threshold,
Chapter 33 support clarification, Chapter 19 sharp and fuzzy distinction,
Chapter 30 age-window SQL correction, consistent exercise headings and
revised review provenance. The detailed before-and-after register and
unified source diff make the applied changes reviewable.

The dated fresh execution evidence is in verification/stage8. All ten
parts ran in Python, R and DuckDB; Stata used the matched original
licensed local execution evidence. The frozen and edited-source audits
passed 81,910 primary comparisons, 123 printed cells, 90 formula anchors
and 24 stream checks. The optional causal forest retains archived
execution evidence and was not freshly rerun during Stage 8.

The teaching directory contains all 892 chapter questions, 80 selected
worked chapter answers, five worked sample examination answers and
twelve project marking notes. Forty-nine numerical solution anchors
passed the additional calculation checks. The remaining 812 questions
do not yet have complete worked solution guides in this release.

## Records

- chapter_review.csv and chapter_review.json identify every chapter and focus.
- copyedit_changes.csv records the 60 initial edit operations.
- edited_files.json and manuscript_edits.diff record the final changed source.
- findings.csv and findings.json show the disposition and remaining gates.
- editorial_audit.json checks structure, references, citations and image descriptions.
- solution_verification.json records calculation checks and their tolerance.
- exercise_index.csv indexes every chapter question.

## Required separate sign off

A qualified academic reviewer should assess methodological and pedagogical
soundness, inspect the selected solutions and independently rerun selected
public and licensed projects. A separate editor should assess language,
consistency and scholarly apparatus. Record reviewer identity,
qualifications, conflicts, files and hashes reviewed, dates, findings,
author responses and acceptance. Blank sign-off fields are supplied in
external_review_handoff.md. They are not a completed certification.

The companion archive was published on Zenodo on 19 November 2026. [View the archived release](https://zenodo.org/records/24382209).
