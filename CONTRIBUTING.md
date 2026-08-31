# Contributing

Clinical UI Skills should remain useful to clinicians, designers, frontend engineers, clinical informaticians, accessibility specialists, human-factors practitioners and coding-agent builders.

The project values **counterexamples and reproducible failure modes** more than aesthetic agreement.

## High-value contributions

1. A recurring AI-generated healthcare UI failure with a synthetic reproduction.
2. A conditional design rule tied to a real task or risk.
3. A new eval with explicit assertions.
4. A #ClinicalUIChallenge before/after submission.
5. Evidence that strengthens, narrows or disproves a project heuristic.
6. A reproducible accessibility or responsive failure.
7. A workflow the current task model handles badly.

## Contribution principles

A rule belongs here when it is:

- tied to a recognizable task, risk, accessibility need, usability problem or repeatable AI-generation failure;
- specific enough for an agent to act on;
- conditional rather than taste-only;
- testable through an eval, screenshot/code review or user research when possible.

Avoid universal taste rules such as “never use cards” or “always use dense tables.” Prefer conditional guidance such as:

> Use a table when the primary task requires scanning and comparing many records across stable attributes. Do not replace the table with equal-weight cards merely to make the interface feel modern.

## Evidence tiers

1. Normative accessibility or regulatory material.
2. Public human-factors / usability guidance.
3. Healthcare design systems and mature open clinical software.
4. Peer-reviewed research.
5. Reproducible project evals.
6. Expert heuristic / design hypothesis.

Label tier 6 clearly. Do not present project preference as established evidence.

## Clinical claims

Do not add clinical thresholds, diagnostic rules, drug dosing, treatment recommendations or disease-management algorithms merely to make examples realistic.

## Patient and confidential data

No real PHI/PII in screenshots, fixtures, issues, PRs, demos, benchmark submissions or test recordings. Do not submit confidential screenshots from employers, customers, hospitals or commercial products. Recreate the pattern with synthetic content.

## Adding a slop pattern

A proposed pattern should include:

```text
Name:
Surface/user:
Signal:
Why it fails:
When it may actually be appropriate:
Better direction:
Evidence tier:
Eval that could detect it:
```

The “when it may actually be appropriate” field is important. Anti-slop rules should not become dogma.

## Adding an eval

Every eval must:

- use synthetic data;
- define user, task and surface;
- avoid unnecessary disease-specific treatment logic;
- have at least five assertions;
- include at least one failure mode the scenario is intended to expose;
- be reproducible without private infrastructure.

## Pull request checklist

- [ ] Skill frontmatter validates.
- [ ] `license: MIT` remains intact.
- [ ] Rules are conditional rather than taste-only.
- [ ] New behavior has an eval, evidence or explicit heuristic rationale.
- [ ] No real patient/confidential data.
- [ ] Accessibility considered.
- [ ] Safety implications considered.
- [ ] Sources added to `references/evidence-map.md` when applicable.
- [ ] `python scripts/validate_skills.py` passes.
- [ ] `python -m unittest discover -s tests -v` passes.
- [ ] README/docs updated if public behavior changed.

## Attribution

By contributing, you agree that your contribution is licensed under the repository's MIT License. Git history is the canonical contributor record. Significant contributors may be added to `CREDITS.md` with consent.
