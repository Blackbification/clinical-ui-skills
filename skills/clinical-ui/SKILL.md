---
name: clinical-ui
description: "Orchestrates design and review of healthcare frontends by classifying user, clinical task, risk, information density, device and use environment before choosing UI patterns. Use for clinician dashboards, patient charts, patient portals, clinical workflows, monitoring views and other visible healthcare software."
license: MIT
compatibility: Codex, Claude Code, Cursor, and agents supporting Agent Skills-style SKILL.md instructions.
metadata:
  author: "Juan Mora Delgado"
  version: "0.1.0"
  project: clinical-ui-skills
---

# Clinical UI

Design healthcare interfaces from **task and context**, not from generic SaaS patterns.

Use specialized skills by context rather than loading everything blindly:

- `anti-slop-core` — generic frontend anti-default discipline;
- `clinician-dashboard` — multi-patient scan/compare/act surfaces;
- `patient-chart` — single-patient longitudinal record;
- `patient-management` — search, queues, appointments, wards, beds and operations;
- `clinical-forms` — documentation and structured entry;
- `clinical-safety-ui` — scope, warnings, critical states, errors and confirmations;
- `clinical-data-viz` — results, trends and quantitative displays;
- `patient-facing-ui` — portals and patient apps;
- `clinical-accessibility` — WCAG-oriented and healthcare-specific accessibility;
- `clinical-ai-ui` — summaries, assistants, extraction review and agent actions;
- `clinical-ui-audit` — final cross-cutting audit and scoring.

## Priority order

When rules conflict:

1. patient/user safety and avoidance of dangerous ambiguity;
2. task effectiveness;
3. accessibility;
4. information hierarchy and clarity;
5. workflow efficiency;
6. visual consistency;
7. distinctiveness / anti-slop;
8. decoration.

Never sacrifice a safer or faster clinical interaction merely to make an interface look more original.

## Skill routing matrix

Load `clinical-ui` + `anti-slop-core` by default, then add only what the task needs:

| Surface/task | Add |
|---|---|
| multi-patient dashboard/worklist | `clinician-dashboard`, `clinical-safety-ui`, `clinical-accessibility` |
| single-patient chart | `patient-chart`, `clinical-safety-ui`, `clinical-accessibility` |
| search/queue/appointments/wards/beds | `patient-management`, `clinical-safety-ui`, `clinical-accessibility` |
| form/documentation/order entry | `clinical-forms`, `clinical-safety-ui`, `clinical-accessibility` |
| chart/trend/results visualization | `clinical-data-viz`, `clinical-accessibility` |
| patient portal/mobile | `patient-facing-ui`, `clinical-accessibility`; add `clinical-forms`/`clinical-data-viz` as needed |
| visible AI feature | `clinical-ai-ui`, `clinical-safety-ui`, `clinical-accessibility` |
| final review | `clinical-ui-audit` |

For high-consequence interactions, do not omit `clinical-safety-ui` simply to save context.

## 1 — Classify the context

Before creating layout or components, determine:

### Primary user

- physician;
- nurse;
- pharmacist;
- allied health professional;
- administrative / operational staff;
- patient;
- carer / family;
- mixed / shared.

If multiple roles use the surface, identify the **primary task owner**.

### Surface

- multi-patient dashboard / worklist;
- single-patient chart;
- patient search / registry;
- queue / ward / bed / appointment view;
- order or medication workflow;
- form / documentation;
- results review;
- monitoring / trend view;
- patient portal;
- patient mobile app;
- communication / messaging;
- AI-assisted surface;
- other.

### Primary task

Use task verbs: detect, review, compare, prioritize, decide, enter, reconcile, acknowledge, schedule, communicate, monitor, escalate, complete, hand off.

Do not start from “what dashboard components should I use?”

### Consequence / risk

Classify the UI interaction, not the disease:

- `low`: inconvenience or recoverable workflow friction;
- `moderate`: error may delay work, misroute information or create meaningful rework;
- `high`: misunderstanding/use error could plausibly contribute to patient harm or major care-process failure.

When uncertain, do not invent a regulatory classification. State the uncertainty and design cautiously.

### Density

- `low`: occasional user, focused task, patient-facing;
- `medium`: mixed review/action workflow;
- `high`: professional scanning, comparison, queues, multi-patient work.

Density is a task property, not a style preference.

### Device / environment

Consider desktop, tablet, mobile or shared workstation and relevant conditions such as interruptions, gloves, bright/dim lighting, one-handed use, time pressure and shared screens.

## 2 — Define the task model

Before implementation:

```text
Primary user:
Primary task:
Top decisions/actions:
Information required immediately:
Information required on inspection:
Information available on demand:
Most dangerous plausible UI misunderstanding:
Expected device/environment:
```

## 3 — Establish context anchors

For patient-specific surfaces:

- keep patient context persistent enough for the workflow;
- display organization-required identity attributes consistently;
- make patient/context switching visible;
- make the scope of actions obvious;
- avoid overlays that obscure which patient an action affects.

Do not invent a universal identifier policy.

## 4 — Define semantic states before colors

List states the UI must distinguish, such as current, historical, new, reviewed, pending, completed, cancelled, unavailable, unknown, entered in error, routine, important, urgent and critical.

Then encode state through a combination of text, position, typography, shape/border, icon and color.

**Do not use color as the sole carrier of clinically meaningful state.**

Do not invent clinical severity thresholds. Severity must come from product logic or supplied rules.

## 5 — Build hierarchy

Use four levels:

- **L0 — persistent context:** identity, scope, encounter/location and information preventing wrong-context action.
- **L1 — action-driving information:** information that can change what the user does now.
- **L2 — supporting information:** useful for interpretation/comparison.
- **L3 — detail on demand:** metadata, long history, provenance detail, secondary notes.

Do not give all levels equal visual weight.

## 6 — Choose representation by task

Prefer a **table/aligned rows** for scanning/comparison/sort/filter/repeated actions; a **timeline** when sequence dominates; a **list** for variable-length objects; a **card** for coherent objects where cross-object comparison is weak; and a **chart** only when visual shape/trend/distribution answers a real question faster than exact values.

Do not convert every domain concept into a card.

## 7 — Design interaction states

Every important surface must consider:

- loading;
- partial loading;
- empty;
- no permission;
- unavailable;
- stale data if applicable;
- validation error;
- network/server error;
- success;
- destructive action;
- interrupted/incomplete task.

Never render an empty panel in a way that can be confused with “no clinical finding” when data has not loaded.

## 8 — Accessibility gate

Default target for web UI: WCAG 2.2 AA.

At minimum: semantic controls, keyboard access, visible focus, programmatic labels, sensible reading/focus order, adequate contrast, non-color semantic cues, appropriate target sizes, error identification, no critical hover-only information, and zoom/reflow checks.

## 9 — Anti-slop gate

Use `anti-slop-core` and ask:

- Did we default to sidebar + equal cards because it is common?
- Are KPI tiles answering decisions?
- Is whitespace reducing scan speed?
- Is a chart decorative?
- Are status pills overused?
- Are rounded icon tiles serving information?
- Are gradients/glass/shadows/animation functional?
- Does every section have identical visual treatment?
- Did we mistake “healthcare” for generic blue/teal styling?

A restrained conventional choice is acceptable when justified.

## 10 — Render and inspect

When browser/render tools are available:

1. render at target viewport;
2. inspect screenshot;
3. inspect compact and data-heavy states;
4. inspect keyboard focus;
5. inspect loading/error/empty states;
6. inspect responsive behavior;
7. run `clinical-ui-audit`;
8. revise.

## Required generation contract

Before code, output briefly:

```text
Context
- user:
- surface:
- task:
- risk:
- density:
- device/environment:

Hierarchy
- L0:
- L1:
- L2:
- L3:

Representation choices:
Safety/accessibility decisions:
Anti-slop risks to avoid:
```

## Finish gate

- [ ] primary user/task explicit;
- [ ] patient/action scope clear where relevant;
- [ ] L0/L1 dominate decoration;
- [ ] temporal state explicit where relevant;
- [ ] missing/unavailable cannot masquerade as normal/negative;
- [ ] units visible where needed;
- [ ] critical state not color-only;
- [ ] loading/empty/error states designed;
- [ ] keyboard/focus considered;
- [ ] responsive behavior fits intended device;
- [ ] anti-slop review complete;
- [ ] no decoration competes with action-driving information.

## Boundaries

This skill does not invent medical logic, validate clinical safety, determine regulatory classification, replace usability testing, authorize real patient data in fixtures, or guarantee WCAG/regulatory compliance.
