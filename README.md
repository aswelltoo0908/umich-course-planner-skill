# UMich Course Planner Skill

An open-source Codex skill for evidence-based University of Michigan Ann Arbor course planning.

## What it does

- Verifies prerequisites, major requirements, electives, and distribution rules against official sources.
- Checks current lectures, labs, discussions, reserved seats, open seats, and waitlists.
- Compares instructors using Atlas and public review signals while reporting evidence quality.
- Detects timetable conflicts, linked-component requirements, evening exams, and Central/North Campus travel issues.
- Produces a primary schedule, backups, requirement mapping, credit totals, and registration actions.
- Redacts common student identifiers before planning material is shared or published.

## Install

Copy the folder into your Codex skills directory:

```bash
git clone https://github.com/aswelltoo0908/umich-course-planner-skill.git
cp -R umich-course-planner-skill ~/.codex/skills/umich-course-planner
```

Restart or refresh Codex so the skill index is reloaded.

## Use

Ask Codex to plan a UMich semester, compare professors, check prerequisites, evaluate waitlists, or optimize a schedule. The skill is discoverable automatically, or can be invoked as `$umich-course-planner`.

## Privacy

Do not publish student names, UMIDs, uniqnames, contact information, login/session data, private transcripts, raw degree-audit exports, or exact private grades. Before sharing a text artifact, run:

```bash
python3 scripts/redact_course_planning.py input.md -o output.redacted.md
```

Automated redaction is only a first pass; review the result manually.

## Sources

The workflow prioritizes official UMich program pages, the LSA Course Guide, Wolverine Access, Atlas, and Registrar policies. Public professor reviews are treated only as secondary qualitative evidence.

## License

MIT
