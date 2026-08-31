# Methodology

Clinical UI Skills uses a layered method:

1. Context classification — user, task, risk, density, device, environment.
2. Task model — repeated decisions/actions and required information.
3. Semantic model — identity, temporal, availability and priority state before styling.
4. Information hierarchy — L0 through L3.
5. Representation — table/list/timeline/card/chart by task.
6. Visual system — restrained tokens and intentional components.
7. State completion — loading, empty, error, stale, permission, destructive.
8. Accessibility — WCAG 2.2 AA baseline.
9. Anti-slop review — remove generic defaults that do not serve task.
10. Rendered audit — inspect pixels/interaction and revise.

## Why anti-slop is late

If anti-slop runs first, an agent may replace useful tables with novel layouts, reduce necessary density, create unfamiliar severity encodings, or hide controls for minimalism. Anti-slop therefore weighs only 5/100 in the Clinical UI Score.

## Eval philosophy

An eval should test a failure mode, not a taste preference.

Good assertion: “The multi-patient view uses an aligned list/table or gives a task-based reason for another representation.”

Weak assertion: “The UI does not use 12px border-radius.”

## Evidence versus heuristic

Classify rules as normative, public guidance, mature healthcare pattern or project heuristic. Project heuristics should be removable if evals/user research contradict them.

## Future human review

ClinicalUIBench should use blinded mixed raters: clinicians, nurses/allied professionals as relevant, UX/human factors, accessibility and frontend/product design. Raters should judge task scenarios, not screenshot preference alone.
