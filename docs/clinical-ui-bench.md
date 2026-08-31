# ClinicalUIBench

ClinicalUIBench is the reproducible evaluation layer for Clinical UI Skills.

## Research question

For comparable healthcare frontend tasks, does a healthcare-specific Agent Skills condition change task-oriented UI quality relative to vanilla generation or generic anti-slop guidance?

## Conditions

- **A — Vanilla:** coding agent without project skills.
- **B — Generic anti-slop:** same/comparable agent with non-healthcare anti-slop guidance.
- **C — Clinical UI Skills:** same/comparable agent with relevant skills from this repository.

## v0.1 corpus

The repository ships **72 synthetic evals across 10 categories**, each with explicit assertions. It also ships a machine-readable rubric, submission validator, score calculator, leaderboard builder, and guidance for reproducibility, blinding and reviewer adjudication in [`../benchmarks/`](../benchmarks/).

## Outcomes

- Clinical context fit.
- Information hierarchy.
- Task efficiency.
- Safety/error resistance.
- Accessibility.
- Data clarity.
- Visual intentionality.
- Anti-slop discipline.
- Separate AI Slop Score.

## Guardrails

- synthetic data only;
- record exact eval prompt/version;
- comparable model/tooling/iteration budget across conditions;
- same target viewport/states where possible;
- blinded review where feasible;
- preserve reviewer disagreement;
- report regressions and null findings;
- do not turn a project rubric into a clinical-validation claim.

## Current claim boundary

v0.1 provides a benchmark **protocol and corpus**, not a published multi-model result proving superiority. The included demos are illustrative and deliberately labeled as such. Public benchmark claims should follow the protocol and identify the release/tag used.
