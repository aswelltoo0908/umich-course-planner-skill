---
name: umich-course-planner
description: Plan University of Michigan Ann Arbor course registration using current official requirements, live section data, Atlas and public instructor reviews. Use for course selection, professor comparison, schedule optimization, prerequisite checks, waitlists, credit-load decisions, and semester roadmaps; anonymize all student data in reusable outputs.
---

# UMich Course Planner

Produce an evidence-based registration plan rather than a generic course list. Separate verified facts from recommendations and label data timestamps because seats, instructors, and meeting times change.

## Privacy boundary

- Treat UMID, uniqname, email, phone, exact student identity, login/session data, unofficial transcripts, grades, and private degree-audit details as sensitive.
- Use private data only to answer the student's request. Never copy it into reusable skills, public documents, brochure material, logs, examples, or promotional copy.
- Replace identity with `Student`; replace account identifiers with `[REDACTED]`; generalize private grades to requirement status such as `completed`, `in progress`, or `planned` unless the student explicitly needs the exact grade in a private answer.
- Preserve course codes, section numbers, instructor names, public meeting times, public evaluation aggregates, and official requirement names: these are course facts, not student identity.
- Before exporting or sharing a planning artifact, run `scripts/redact_course_planning.py` and review the result manually.

## Workflow

1. Establish the target term, school/college, intended program, completed/in-progress prerequisites, credit target, workload preference, and schedule constraints. Infer only when prior trusted context is clear; otherwise mark unknowns.
2. Verify degree requirements on the current official LSA, College of Engineering, department, or Registrar page. Distinguish declaration prerequisites, major core, category electives, distribution/skills requirements, and credits that merely count toward the degree.
3. Read live offerings from the LSA Course Guide, Wolverine Access, or Atlas. Record lecture/lab/discussion dependencies, reserved seats, open seats, waitlist status, prerequisites, locations, and dates.
4. Compare every instructor actually offered in the target term. Prefer Atlas evaluation aggregates and course-specific history; use Rate My Professors only as a noisy secondary signal. Note sample size and missing data. Never invent a ranking for an instructor without evidence.
5. Build conflict-free schedules using actual components and realistic campus travel. A zero-minute transition between Central and North Campus is a conflict even if the time grid does not flag it.
6. Score schedules on program progress, instructor evidence, expected workload, grade risk, commute, credit count, and the student's preferences. Do not equate a high historical median grade with low effort.
7. Return one primary plan and up to two backups. Include exact sections, component pairings, weekly grid, total credits, requirement progress, conflicts/commute warnings, seat timestamp, and next registration actions.

## Evidence rules

- Use the official program page for requirement placement and prerequisites.
- Use the official course guide or Wolverine Access for current sections and seats.
- Use Atlas for median grades, evaluation aggregates, historical offerings, and instructor profiles.
- Use public reviews only to interpret teaching style; do not treat them as authoritative grade data.
- For a new or sparsely reviewed instructor, say `insufficient public evidence` and optimize around section time or provide a backup.
- Recheck live data immediately before registration. Never enroll, drop, swap, join a waitlist, or send messages without the student's explicit authorization for that action.

## Output contract

Use the compact schema in [references/output-schema.md](references/output-schema.md). For source priorities, enrollment edge cases, and definitions, read [references/sources-and-rules.md](references/sources-and-rules.md).
