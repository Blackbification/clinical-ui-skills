---
name: clinical-safety-ui
description: "Designs and audits safety-oriented visual states for healthcare frontends: patient/action scope, alerts, critical results, warnings, errors, destructive actions, missingness, freshness, confirmations and state transitions. Use when UI ambiguity or misuse could plausibly contribute to patient or care-process harm."
license: MIT
compatibility: Codex, Claude Code, Cursor, and agents supporting Agent Skills-style SKILL.md instructions.
metadata:
  author: "Juan Mora Delgado"
  version: "0.1.0"
  project: clinical-ui-skills
---

# Clinical Safety UI

Design the interface so consequential state is **hard to misread, hard to mis-scope and recoverable when possible**.

This skill is a UI reasoning aid, not a safety certification or risk-management process.

## Start with use-error hypotheses

```text
User:
Task/action:
Object/patient in scope:
Potentially consequential misunderstanding:
Required state distinctions:
Reversibility:
Freshness/completeness requirements:
Environment/interruptions:
```

## Patient and action scope

For consequential actions, the UI should make it possible to answer which patient/object is in scope, what action will happen, which parameters are in scope, whether information is current/complete enough, and whether the action can be reversed.

## Semantic state before visual state

Model state dimensions before assigning color: lifecycle, review, availability, priority and action. Do not merge dimensions merely because a single badge is convenient.

## Alert hierarchy

Every warning/alert should have a reason for its salience. Ask whether the user must know now, whether action is required, what happens if ignored, whether blocking is justified, whether it can be contextual and whether the same signal is duplicated elsewhere.

Avoid alert stacks where everything looks equally urgent.

## Color and redundancy

Color may reinforce meaning but must not be the only meaningful cue. Combine with explicit language and, where useful, iconography, border/shape, placement and typography. Never invent red/amber/green clinical thresholds.

## Critical results and abnormal values

When product logic supplies critical/abnormal status, preserve analyte/result identity, exact value, unit, time, supplied status, patient association and required acknowledgement/action state when present. Do not hide exact values in hover interactions or reduce them to a colored dot.

## Confirmations

When confirmation is justified, state object/patient, action, consequence, primary confirm action and safe cancel/back action. Avoid confirmation fatigue for trivially reversible actions.

## Destructive / irreversible actions

Use explicit verbs, object names and scope. Prefer undo for safely reversible actions. Avoid ambiguous icon-only destructive controls in dense lists.

## Missing, partial, stale and unavailable

These states must never be conflated with a meaningful clinical negative. Show freshness when stale information could plausibly mislead the user.

## Switching context

When patient/object context changes, update persistent identity immediately, clear stale pending action state, close or re-scope panels that could apply to the previous object, make the transition perceptible, and avoid retaining old values during loading without an explicit stale state.

## Failure and retry

Expose failure clearly, preserve safe user input, provide contextual retry, and avoid silent optimistic success for consequential changes.

## Anti-slop traps

- red everywhere;
- identical pill treatment for severity, status and ownership;
- global warning banner for contextual issues;
- icon-only critical state;
- decorative pulse animation as urgency;
- confirmation modal reflex;
- generic “Something went wrong” after consequential action;
- green meaning “safe” without product semantics;
- skeleton UI that looks like actual clinical values;
- all warnings competing at equal visual weight.

## Finish gate

- [ ] consequential patient/object scope is visible;
- [ ] state dimensions are not conflated;
- [ ] high-consequence state is not color-only;
- [ ] missing/partial/stale/unavailable are explicit when relevant;
- [ ] alert salience matches action need;
- [ ] critical values retain value + unit + time + association;
- [ ] confirmation states object + action + consequence;
- [ ] context switching cannot leave stale actionable state;
- [ ] failures are visible and recoverable where possible;
- [ ] no invented clinical thresholds;
- [ ] anti-slop audit passed.

## Boundary

This skill does not replace clinical safety cases, hazard analysis, usability validation, quality management, regulatory review or organization-specific policy.
