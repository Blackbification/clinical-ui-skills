---
name: patient-management
description: "Designs and audits operational healthcare frontends for patient search, registration, queues, appointments, wards, beds, lists, check-in, transfers and administrative workflows. Use when staff must find, sort, filter, route, schedule or act on many patients or operational objects quickly and safely."
license: MIT
compatibility: Codex, Claude Code, Cursor, and agents supporting Agent Skills-style SKILL.md instructions.
metadata:
  author: "Juan Mora Delgado"
  version: "0.1.0"
  project: clinical-ui-skills
---

# Patient Management

Design operational healthcare interfaces around **recognition, throughput, scope and exception handling**.

This is not a clinician dashboard and not a patient chart. The work object may be a patient, appointment, queue position, bed, encounter, referral, registration task or transfer.

## Start with the operational task

```text
Primary staff role:
Work object:
Repeated action:
Required scan fields:
Exception fields:
Scope/filter context:
Expected volume:
Device/environment:
Most dangerous plausible mix-up:
```

## Information model

Prefer stable aligned rows when users compare many objects. Keep the primary identity field visually stable. Put the fields that distinguish similar records adjacent to identity rather than hiding them in detail panels.

Possible concepts, only when supplied by the product:

- patient identity and identifiers;
- date of birth / age;
- location / ward / service;
- appointment or queue state;
- arrival / check-in time;
- assigned clinician/team;
- bed/room;
- referral status;
- operational flags;
- last update / freshness.

Do not invent required identifiers or institutional policies.

## Search and identity disambiguation

Patient search must reduce wrong-record selection, not merely return fast matches.

- show enough distinguishing information for the intended workflow;
- highlight matched text without hiding surrounding context;
- keep exact identifier search available when relevant;
- avoid visually identical result cards with only the name prominent;
- make duplicate/similar-name situations detectable;
- preserve the active scope/filter after returning from detail when useful.

Never imply that a name alone is a safe universal identity key.

## Lists, queues and worklists

Use columns/rows when comparison matters. Make sorting/filtering state visible. Distinguish priority from severity, waiting time from clinical urgency, assignment from ownership, current state from next action, and data unavailable from no data.

Avoid a card grid for a queue merely because cards are easy to generate.

## Appointments and schedules

Make date, time, timezone where relevant, location/modality, status and patient association clear. Preserve product-defined states. Do not rely on color alone to indicate cancellation or conflicts.

## Wards / beds / transfers

Spatial layouts are acceptable when spatial reasoning is the task. Otherwise use compact lists/tables. For bed or transfer actions, show source and destination explicitly, show the patient/object in scope, avoid ambiguous drag-only actions, provide keyboard/touch alternatives, confirm only when consequence justifies interruption and refresh visibly after state changes.

## Bulk actions

Bulk actions should show selected count, scope and consequence. Keep selection visible after scrolling. Avoid hidden select-all semantics and actions that silently apply beyond the current page/filter.

## Empty, stale and unavailable

Distinguish no matches for current filters, list successfully loaded but empty, data unavailable/error, partial data and stale data when freshness matters.

## Density

Professional operations surfaces may legitimately be dense. Use typography, alignment, grouping, column priority and progressive disclosure instead of oversized cards and whitespace.

## Anti-slop traps

- patient-as-card grid for high-volume lists;
- giant KPI strip before the actual queue;
- rounded icon tile for every operational state;
- colored pill for every cell;
- kanban by default when sorting/filtering is primary;
- map/floor-plan metaphor when spatial location is not the task;
- hover-only row actions;
- generic “active / inactive” labels replacing real workflow states;
- decorative avatar dominance;
- hidden scope after filtering.

## Finish gate

- [ ] work object dominates before aggregate analytics;
- [ ] identity/disambiguation supports the intended task;
- [ ] sorting/filter scope remains visible;
- [ ] current state and next action are distinguishable;
- [ ] list/queue works at realistic volume;
- [ ] bulk action scope is explicit;
- [ ] no-match ≠ load failure;
- [ ] touch/keyboard paths exist where required;
- [ ] destructive/reassignment actions state object + consequence;
- [ ] dense mode remains readable;
- [ ] anti-slop audit passed.

## Boundary

This skill does not define hospital policy, patient-identification requirements, triage severity, scheduling rules or workflow authority. Those must come from the product and organization.
