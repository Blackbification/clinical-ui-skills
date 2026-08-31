# AGENTS.md

Instructions for coding agents modifying this repository.

1. Preserve the project's scope: **frontend/UI/visual interaction for healthcare software**.
2. Public examples, screenshots, fixtures and evals use **synthetic data only**. Never add PHI/PII or lightly de-identified real records.
3. Do not invent clinical thresholds, treatment recommendations, dosing, diagnostic logic or regulatory claims to make a demo realistic.
4. Keep Agent Skills compatible with the open `SKILL.md` specification; skill names must match their directory names and `SKILL.md` should remain under 500 lines.
5. Every skill remains MIT licensed and retains `metadata.author: "Juan Mora Delgado"` unless the project owner intentionally changes attribution policy.
6. A design rule should be conditional and task-based. Avoid taste-only bans such as “never use cards”.
7. Safety/accessibility claims must stay within available evidence. The project is not a compliance or clinical-validation framework.
8. New evals require synthetic data and at least 6 explicit assertions.
9. Run `make check` before proposing changes.
10. When a rule changes public behavior, update the relevant docs/evals/changelog.
