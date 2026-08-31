---
name: clinical-forms
description: "Designs and audits healthcare forms, documentation, data-entry and order-entry interfaces with explicit units, formats, defaults, missingness, validation, conditional logic, recovery and repeated-entry ergonomics. Use for clinician documentation, medication/order forms, patient questionnaires, measurements and structured clinical data entry."
license: MIT
compatibility: Codex, Claude Code, Cursor, and agents supporting Agent Skills-style SKILL.md instructions.
metadata:
  author: "Juan Mora Delgado"
  version: "0.1.0"
  project: clinical-ui-skills
---

# Clinical Forms

Treat data entry as a **stateful safety-critical interaction**, not as a stack of generic inputs.

## Define the entry model first

```text
Primary user:
Data being entered:
Source of truth:
Required vs optional:
Units/formats:
Allowed unknown/not-applicable states:
Defaults and their provenance:
Conditional fields:
Validation timing:
Save/submission model:
Most consequential entry error:
```

## Labels and instructions

Use persistent labels. Place short instructions next to the field they affect. Do not use placeholder text as the only label.

## Units and formats

Keep units visually attached to the value and programmatically understandable. Make expected formats explicit for dates, time, durations, decimal precision and identifiers. Do not silently switch units or infer units from context when ambiguity is plausible.

## Unknown, negative and not applicable

Model these as different states when the product distinguishes them: `unknown ≠ no`, `not assessed ≠ no`, `not applicable ≠ no`, `not recorded ≠ no`.

Never turn an untouched checkbox, blank select or failed load into a clinical negative.

## Defaults

Every default must have a reason. Ask whether it is a safe, stable product default, derived from current context, could create a consequential error if accepted inattentively, or should be explicitly confirmed. Do not prefill clinically meaningful answers merely to reduce clicks.

## Validation

Prefer validation close to the field and preserve entered data after recoverable errors. Use clear error summaries for long forms when helpful. State what is wrong and how to fix it. Do not use only red borders/icons.

## Conditional logic

Reveal conditional fields predictably. When changing a parent answer would discard hidden child data, warn or preserve according to product policy.

## Repeated entry

Optimize keyboard/touch sequence, tab order, scanning and carry-forward only when safe and intentional.

## Choice controls

Use radios for a small mutually exclusive set, checkboxes for independent choices, autocomplete/search for large vocabularies, and free text only when structured choice is not appropriate. Do not turn every binary clinical concept into a stylized toggle.

## Date and time

Make date/time context clear. Avoid ambiguous numeric dates where locale may vary. Show timezone when cross-zone interpretation matters. Distinguish event time from entry time if both exist.

## Submission and recovery

Communicate draft/saved/submitting/success/failure states. Prevent duplicate submissions. Offer undo or reversal when appropriate. Do not clear the form after a failed submission.

## Patient-facing forms

Reduce jargon and cognitive burden, preserve answers across errors/navigation, and use progressive steps only when they reduce complexity.

## Order-entry / high-consequence forms

Keep patient/object scope visible. Show critical supplied parameters together. Confirm only when consequence justifies it. Do not invent clinical defaults or dosing logic.

## Anti-slop traps

- floating labels everywhere;
- giant rounded inputs with excessive vertical space;
- default values added for visual completeness;
- placeholder-only labels;
- one generic confirmation modal for every action;
- binary toggles replacing nuanced states;
- hiding units inside placeholders;
- multi-step wizard for a short repeated professional task;
- success confetti for routine documentation.

## Finish gate

- [ ] every control has a persistent/programmatic label;
- [ ] units/formats are explicit;
- [ ] unknown/negative/not-applicable are not collapsed accidentally;
- [ ] defaults are justified;
- [ ] validation is specific and recoverable;
- [ ] errors are not color-only;
- [ ] user input survives recoverable failure;
- [ ] conditional fields do not silently discard data;
- [ ] keyboard/touch sequence fits repeated use;
- [ ] submission state is visible;
- [ ] patient/action scope remains clear when consequential;
- [ ] anti-slop audit passed.

## Boundary

This skill does not determine which clinical fields are required, which answers are correct, or which defaults are medically appropriate.
