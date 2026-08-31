---
name: clinical-ui-audit
description: "Audits healthcare frontend code and rendered UI for clinical context fit, information hierarchy, task efficiency, safety/error resistance, accessibility, data clarity, visual intentionality and generic AI slop. Returns prioritized findings plus Clinical UI Score and AI Slop Score."
license: MIT
compatibility: Codex, Claude Code, Cursor, and agents supporting Agent Skills-style SKILL.md instructions.
metadata:
  author: "Juan Mora Delgado"
  version: "0.1.0"
  project: clinical-ui-skills
---

# Clinical UI Audit

Audit rendered healthcare UI and frontend implementation as a task/safety system, not a beauty contest.

Prefer evidence from: rendered screenshots, actual interaction, frontend source, then design description. When evidence is limited, state the limitation.

## 1 — Establish context

```text
Primary user:
Primary task:
Surface:
Risk:
Expected device:
Use environment:
Available evidence:
```

If unknown, make the narrowest reasonable assumption and label it.

## 2 — Blocker screen

A `BLOCKER` is a plausible interface defect that should be resolved before treating the surface as ready for serious use.

Potential blocker classes:

- patient/action scope cannot be determined;
- loading/failure visually indistinguishable from meaningful clinical “none”;
- high-consequence state conveyed only by color;
- primary action can easily apply to wrong patient/object;
- essential control inoperable with intended input mode;
- essential value detached from unit/context;
- destructive workflow has dangerously ambiguous scope;
- generated AI content indistinguishable from source record where provenance matters.

Do not label ugliness/generic styling a BLOCKER.

## 3 — Score eight dimensions

Use `references/clinical-ui-score.md`.

### A. Clinical context fit — 15

User role, task, risk, density, device and environment.

### B. Information hierarchy — 15

Context vs action-driving vs supporting vs detail.

### C. Task efficiency — 15

Scan path, comparison, interaction burden, filters and action placement.

### D. Safety & error resistance — 20

Identity/scope, semantic states, temporal clarity, missing/loading/error, destructive actions, warning salience and use-error traps.

### E. Accessibility — 15

Semantics, keyboard, focus, contrast, labels, non-color cues, targets, error identification and reflow. Do not claim full WCAG conformance from a screenshot.

### F. Data clarity — 10

Units, timestamps, alignment, visualization choice, missing data and provenance/context where applicable.

### G. Visual intentionality — 5

Coherent system, typography, spacing, component anatomy, restraint and product fit.

### H. Anti-slop discipline — 5

Whether generic AI defaults dominate.

## 4 — AI Slop Score

Separate 0–10 score. Inspect KPI/card soup, bento regardless of task, generic gradients/glass, rounded icon tiles, pill overload, decorative charts, huge whitespace in dense tasks, repetitive radii/shadows, generic AI motifs and meaningless animation.

Do not reward novelty for novelty's sake.

## 5 — Finding severity

### BLOCKER
Plausible high-consequence use problem/fundamental context ambiguity.

### HIGH
Major task, accessibility, hierarchy or safety weakness.

### MEDIUM
Meaningful friction/confusion or generic-pattern issue with limited consequence.

### LOW
Polish, consistency or minor slop.

Every finding must include:

```text
Severity:
Evidence:
Why it matters:
Concrete fix:
Verification:
```

Avoid “improve hierarchy” without specifics.

## 6 — Score caps

Project heuristics:

- unresolved BLOCKER → overall max `49/100`;
- 2+ unresolved HIGH safety findings → safety max `8/20`;
- inaccessible primary task → accessibility max `7/15`.

These are not regulatory rules.

## Required output

```text
CLINICAL UI AUDIT

Context
...

Scores
Clinical context fit ..... __/15
Information hierarchy .... __/15
Task efficiency .......... __/15
Safety/error resistance .. __/20
Accessibility ............ __/15
Data clarity ............. __/10
Visual intentionality .... __/5
Anti-slop discipline ..... __/5
TOTAL .................... __/100

AI Slop Score ............ __/10

BLOCKERS
...
HIGH
...
MEDIUM
...
LOW
...

Top 3 fixes
1.
2.
3.

Verification plan
...
```

## Surface-specific review

### Clinician dashboard

Is the work object visible before analytics? Can users scan/compare? Is patient association stable? Are priority/severity/newness distinct? Are filters/scope visible? Does density remain readable?

### Patient chart

Is patient context persistent? Current/historical clear? Chronology coherent? Units/time/source available? No-data ≠ not-loaded? Actions scoped?

### Patient-facing

Is task clear? Language understandable? Next action prominent? Interpretation sourced? Mobile/touch practical? Warnings calm, specific and accessible?

## Code review heuristics

Inspect non-semantic clickable elements, missing labels, hidden focus, color-only state, placeholder-only forms, repeated radius/shadow/gradient utilities, icon-only buttons without accessible names, chart content inaccessible outside hover/canvas, unassociated errors, loading skeletons that could resemble data, and responsive stacking that destroys comparison.

Use the repository-root linter at `../../scripts/clinical_ui_lint.py` as supporting evidence.

## Audit finish gate

- [ ] context assumptions stated;
- [ ] rendered UI inspected when available;
- [ ] blocker screen complete;
- [ ] eight dimensions scored;
- [ ] AI Slop Score separate;
- [ ] each finding evidence + concrete fix;
- [ ] accessibility claims within evidence;
- [ ] no clinical correctness claims invented;
- [ ] verification plan provided.
