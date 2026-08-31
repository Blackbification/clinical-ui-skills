---
name: clinician-dashboard
description: "Designs and audits dense, scannable clinician dashboards, worklists and multi-patient monitoring views. Use when clinicians or care teams must review, compare, prioritize or act across multiple patients, tasks, results or clinical exceptions."
license: MIT
compatibility: Codex, Claude Code, Cursor, and agents supporting Agent Skills-style SKILL.md instructions.
metadata:
  author: "Juan Mora Delgado"
  version: "0.1.0"
  project: clinical-ui-skills
---

# Clinician Dashboard

Build work surfaces for clinical professionals who need to **scan, compare, detect exceptions, prioritize and act**. Do not default to an executive analytics dashboard.

## First question

What decision/action must the clinician make repeatedly?

Examples: which patient needs attention first; which result is new and important; what is pending; what changed since prior review; which task is overdue; who is ready for the next workflow step.

The work object usually deserves more prominence than aggregate vanity metrics.

## Dashboard modes

### Multi-patient worklist
Primary object = patient row/item. Optimize identity, stable columns, scanning, sorting, filtering, exceptions and repeated row actions.

### Exception queue
Primary object = problem/task/result requiring review. Optimize priority, freshness, assignment, status, acknowledgement/completion and source patient context.

### Monitoring dashboard
Primary object = evolving state. Optimize temporal change, current state, trajectory, explicit freshness, product-supplied thresholds and actionable exceptions.

### Operational clinical dashboard
Primary object = care-process state. Optimize queue, location, assignment, dependencies, bottlenecks and next action.

Do not merge every mode into one screen merely because data exists.

## Information architecture

Use a compact top context for team/service/location/date, active filters, freshness and scope. Do not spend the first 30% of the viewport on greetings and metric cards.

Put the patient/result/task work object early. Counts and aggregates can support navigation/filtering/workload overview, but should not displace the work object unless aggregation is the primary task.

## Table versus card

Prefer table/aligned rows when many similar entities share stable fields, sorting matters, column comparison matters or repeated actions are common.

Cards are acceptable when each entity has materially different content structure and cross-entity comparison is weak.

Do not choose cards because they look friendlier.

## Multi-patient safety

For every row/item:

- patient association remains visually stable;
- row actions clearly affect that row;
- expanded detail preserves patient identity;
- selection state is explicit;
- bulk actions clearly expose scope;
- transition into a patient chart is obvious.

Implement the identifiers supplied by the system/policy; do not invent universal identification requirements.

## Scannability

Prefer aligned numeric columns, consistent units, stable column order, short labels, meaningful whitespace, compact semantic indicators and fixed positions for frequent signals.

Avoid center-aligned clinical tables, variable signal positions, paragraph-length row content, and many competing colored row backgrounds.

## Priority and severity

Keep workflow priority, clinical severity, new/unreviewed status and overdue status as distinct semantic dimensions. Do not collapse everything into “red = bad.”

If severity comes from backend/product logic, display it faithfully. Do not create thresholds.

## Time / freshness

Make relevant time semantics explicit: observed, resulted, ordered, last updated, due, overdue, since last review.

If data can be stale, distinguish stale from missing and never imply live monitoring when refresh is periodic.

## Filters

Professional filters should expose current scope, be easy to reset, keyboard usable and persistent enough to prevent population confusion. Do not hide essential active filters inside “More.”

## Actions

Place frequent actions near their object. Be cautious with primary actions hidden in menus, ambiguous icon-only actions, destructive actions next to routine actions, and row-click plus nested controls with unclear targets.

## Alerts

Do not convert every exception into an alert banner. Use salience proportional to urgency, consequence, novelty and need for interruption. Prefer prioritization/filtering for routine exceptions.

## Density

High density is often appropriate for frequent expert work. Reduce it when expertise is low, tasks are infrequent, touch accuracy matters, or content becomes visually indistinguishable.

Do not import consumer-app spacing into a high-frequency desktop worklist by default.

## Responsive behavior

Do not mechanically stack every desktop cell into giant mobile cards. Identify the tasks expected on smaller screens, preserve identity/action-driving fields, allow secondary detail, remove low-value columns and retain practical targets.

A mobile surface may need a different task scope.

## Empty/failure states

Differentiate no matching records, no recorded data, not loaded, permission denied, service unavailable and filter-zero. These meanings are not interchangeable.

## Anti-slop traps

- four KPI cards before the patient list;
- workload donut;
- “Good morning, Doctor” hero;
- card per patient;
- badge for every field;
- rainbow status table;
- massive whitespace;
- decorative sparklines on every row;
- floating AI button covering work.

## Required design contract

```text
Dashboard mode:
Primary user:
Repeated decision/action:
Primary work object:
Scan fields:
Exception fields:
Primary actions:
Time/freshness semantics:
Density:
Device:
Most dangerous UI ambiguity:
```

## Finish gate

- [ ] work object before decorative analytics;
- [ ] patient association stable;
- [ ] rows/items easy to scan;
- [ ] comparable values align;
- [ ] units/timestamps clear where needed;
- [ ] priority/severity/newness not conflated;
- [ ] active filter scope visible;
- [ ] actions clearly scoped;
- [ ] stale/missing/loading differ;
- [ ] keyboard/touch fits device;
- [ ] aggregate metrics earn their space;
- [ ] anti-slop audit passed.

## Boundary

This skill does not determine clinical priority rules, abnormal ranges, treatment thresholds or local workflow policy.
