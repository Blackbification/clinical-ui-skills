---
name: clinical-data-viz
description: "Designs and audits clinical charts, trends, results views and quantitative displays with explicit units, time, missingness, provenance and task-appropriate chart choice. Use for labs, vitals, monitoring, outcomes, population dashboards and patient-facing health data visualizations."
license: MIT
compatibility: Codex, Claude Code, Cursor, and agents supporting Agent Skills-style SKILL.md instructions.
metadata:
  author: "Juan Mora Delgado"
  version: "0.1.0"
  project: clinical-ui-skills
---

# Clinical Data Visualization

Use visualization only when visual pattern recognition answers the user’s question faster or more safely than exact values alone.

## Define the question first

```text
User:
Question:
Decision/action supported:
Variables and units:
Time horizon/sampling:
Missingness:
Reference/target source:
Need exact values?:
Need comparison?:
```

If the user primarily needs an exact current value, a value/table may beat a chart.

## Choose encoding by task

- line for meaningful ordered trend;
- step for state changes where interpolation misleads;
- points for discrete observations;
- bars for category/bin comparison;
- scatter for quantitative relationships;
- distribution plots for population distribution;
- table for exact comparison, sparse data or heterogeneous fields;
- small multiples for repeated comparable trends.

Avoid donut, radial gauge and decorative area charts unless their encoding serves a real task.

## Integrity rules

- use an honest time axis;
- keep exact timestamps available where needed;
- never turn missing into zero;
- do not silently bridge unavailable periods;
- keep units attached to values/axes;
- avoid unjustified dual axes and visual distortion;
- distinguish reference interval, personal target, decision threshold and population benchmark;
- display ranges/targets only when supplied by trusted product logic/content;
- do not invent abnormality from visual position.

## Clinician views

Prefer compact values, aligned columns, exact values beside sparklines, small multiples and focus+context. Do not force every metric into a large card-chart pair.

## Patient-facing views

Lead with the supplied value/status/meaning and next action, then a simple trend when useful. Explain time/axis language and avoid unexplained professional jargon.

## Accessibility

Provide a non-visual equivalent for essential information. Do not hide essential values solely in hover tooltips or inaccessible canvas content.

## Anti-slop traps

- donut reflex;
- gauge theater;
- glowing gradient area under every line;
- 3D charts;
- connecting through missing data;
- chart where one number would do;
- KPI cards + generic chart regardless of question;
- dual axis by default;
- color-only abnormality;
- line spaghetti;
- decorative health-score rings.

## Finish gate

- [ ] chart answers a named question;
- [ ] exact values remain accessible when needed;
- [ ] units explicit;
- [ ] time spacing honest;
- [ ] missing data not interpolated/zeroed silently;
- [ ] reference/target semantics sourced and distinct;
- [ ] abnormal state not color-only;
- [ ] scale choices avoid distortion;
- [ ] accessible equivalent exists;
- [ ] simpler table/value considered;
- [ ] anti-slop audit passed.

## Boundary

This skill does not define clinical thresholds, normal ranges, outcome interpretation or statistical validity.
