---
name: patient-chart
description: "Designs and audits single-patient clinical charts and longitudinal record views with persistent patient context, temporal integrity, clear current-versus-historical state, and safe review/action patterns."
license: MIT
compatibility: Codex, Claude Code, Cursor, and agents supporting Agent Skills-style SKILL.md instructions.
metadata:
  author: "Juan Mora Delgado"
  version: "0.1.0"
  project: clinical-ui-skills
---

# Patient Chart

Design a single-patient clinical workspace where the user can understand **who**, **when**, **what is current**, **what changed**, and **what action affects which record**.

Do not turn the chart into unrelated equal-weight dashboard cards.

## Chart model

A chart may contain patient identity, encounters, allergies, conditions/problems, medications, orders, results/tests, vitals, procedures, notes, immunizations, tasks, forms, attachments and flags. Include only what is relevant.

## Patient context

Patient context is L0 information. Keep organization-required identity visible enough for the workflow; preserve identity through workspaces/overlays where feasible; make patient switching explicit; make action scope obvious.

Do not invent identifier policy.

## Review versus entry

Reviewing and entering information impose different cognitive demands. For complex workflows, prefer a deliberate workspace for adding/editing/ordering/reconciling/documenting while preserving patient context. Avoid in-place editing everywhere merely because it is technically easy.

## Current versus historical

Make relevant lifecycle/temporal state understandable: active/inactive, current/historical, ordered/pending/resulted, draft/signed/amended, ongoing/completed, cancelled, entered in error, unknown.

Do not rely on faded text alone to mean historical.

## Timeline integrity

When chronology matters:

- use explicit dates/times;
- keep ordering consistent;
- expose author/source when provenance matters;
- distinguish event time from entry/update time if product exposes both;
- do not visually interpolate across missing periods.

Relative time can support scanning but should not erase exact time when exact timing matters.

## Section hierarchy

Do not give allergies, medications, routine notes and administrative metadata identical visual weight. Prioritize according to task.

- **L0:** patient identity/scope.
- **L1:** action-driving current information.
- **L2:** supporting current/historical information.
- **L3:** metadata/detail on demand.

## Patient banner

Keep it compact. Potential elements only if required: name, age/DOB, identifier(s), sex/gender fields as defined by product, location/encounter and major flags. Avoid a consumer profile hero.

## Results

Preserve test name, value, unit, time, supplied reference context, supplied abnormal/critical status, useful trend and missing/pending/cancelled state.

Do not invent reference ranges/severity. Avoid unit-on-hover, color-only abnormality, or sparklines that hide exact values.

## Medication

When supplied, visually distinguish states such as active, stopped, planned, completed and historical. Keep dose/route/frequency readable when present. Do not infer correctness.

## Allergies / high-salience flags

Use strong but controlled salience. Avoid making the whole chart red, stacking duplicate warnings, or using icon-only allergy communication.

## Notes

Optimize author/time/type/status, scan preview, full reading, chronology and search. Do not render every note as a tall card if a compact list/timeline is better.

## Navigation

Choose anchored sections, tabs, side navigation, search/filter, timeline or overview+detail based on chart size. Keep location within the patient chart obvious.

## Loading and empty states

Mandatory distinction: “no recorded allergies” ≠ “allergies not loaded”; “no results in selected period” ≠ “result service unavailable”; “unknown” ≠ “no”.

Never substitute visual emptiness for a clinical negative.

## Responsive behavior

On smaller screens preserve patient context and highest-value current information, use disclosure for detail, keep frequent actions reachable and avoid giant stacked-card conversions.

## Anti-slop traps

- profile hero banner;
- domain card wall;
- rounded colored icon for every clinical domain;
- equal visual weight across modules;
- pastel status chips everywhere;
- decorative health score;
- “record completeness” donut;
- AI summary dominating first viewport;
- excessive spacing causing scroll marathon.

## AI summary surfaces

If an AI-generated summary exists, label it, keep source data accessible, show provenance/links when supported, distinguish generated content from source record and avoid styling generated inference like authoritative chart data.

## Required design contract

```text
Primary chart task:
Persistent patient context:
L1 current/action-driving data:
Historical data representation:
Temporal model:
Primary actions:
Loading/empty/error distinctions:
Device:
Anti-slop risks:
```

## Finish gate

- [ ] patient context persists;
- [ ] current/historical distinguishable;
- [ ] timestamps/units explicit where needed;
- [ ] no-data ≠ not-loaded;
- [ ] action scope clear;
- [ ] high-salience information not diluted by card soup;
- [ ] chronology coherent;
- [ ] navigation understandable;
- [ ] responsive behavior preserves task-critical information;
- [ ] AI output, if present, distinct from source data;
- [ ] anti-slop audit passed.

## Boundary

This skill defines interface behavior/hierarchy. It does not determine diagnoses, clinical relevance, abnormal ranges, medication safety or treatment.
