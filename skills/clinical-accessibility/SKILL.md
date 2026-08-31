---
name: clinical-accessibility
description: "Designs and audits accessible healthcare frontends using WCAG 2.2 AA as the default web baseline while accounting for clinical tables, warnings, patient identity, units, data visualizations, touch, zoom, keyboard and assistive-technology use."
license: MIT
compatibility: Codex, Claude Code, Cursor, and agents supporting Agent Skills-style SKILL.md instructions.
metadata:
  author: "Juan Mora Delgado"
  version: "0.1.0"
  project: clinical-ui-skills
---

# Clinical Accessibility

Treat accessibility as task performance, not a final polish pass. Default web target: **WCAG 2.2 AA**. This skill does not itself establish conformance.

## Core checks

- semantic landmarks, headings, tables and controls;
- real buttons for actions and links for navigation;
- keyboard-operable primary tasks;
- visible focus and sensible focus order;
- programmatic and persistent form labels;
- adequate contrast;
- important state not color-only;
- practical touch targets;
- no essential hover-only information;
- zoom/reflow without loss of identity, units or primary actions;
- errors specific, associated and recoverable;
- alternatives to drag-only interaction;
- accessible authentication patterns.

## Healthcare-specific checks

Patient identity must remain perceivable with assistive technology. Units should stay with values in reading order. Warning meaning must survive without icon/color. Row actions need specific accessible names. Dense tables need correct header associations and a usable keyboard strategy.

## Data visualization

Provide an accessible table/list/summary for essential information; expose exact values outside hover; ensure interactive exploration is keyboard accessible when required.

## Responsive conditions

Consider shared workstations, tablets, one-handed mobile use, gloves, bright/dim environments, large text, 200% zoom and screen readers without assuming one environment applies everywhere.

## Anti-slop traps

- tiny low-contrast metadata;
- icon-only actions with vague names;
- `outline-none` without replacement focus styling;
- div/span as button;
- placeholder-only input labels;
- color-only red/green status;
- hover-only units or values;
- fixed-height cards that clip large text;
- drag-only transfers;
- decorative motion competing with warnings.

## Finish gate

- [ ] primary task keyboard/touch operable;
- [ ] focus visible;
- [ ] semantics appropriate;
- [ ] labels accessible;
- [ ] important state not color-only;
- [ ] identity/units survive reading order;
- [ ] zoom/reflow checked;
- [ ] charts have accessible equivalent;
- [ ] errors recoverable;
- [ ] no conformance claim exceeds evidence.

## Boundary

Passing these checks is not proof of WCAG conformance or clinical usability. Validate with appropriate automated and manual testing and representative users.
