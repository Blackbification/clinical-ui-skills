---
name: patient-facing-ui
description: "Designs and audits patient portals and patient-facing healthcare apps using plain language, focused tasks, appropriate information density, clear next actions, privacy-aware presentation, accessible interaction and restrained health/AI aesthetics."
license: MIT
compatibility: Codex, Claude Code, Cursor, and agents supporting Agent Skills-style SKILL.md instructions.
metadata:
  author: "Juan Mora Delgado"
  version: "0.1.0"
  project: clinical-ui-skills
---

# Patient-Facing UI

Design for people managing health tasks, not for clinicians using a simplified EHR.

## Start with the patient task

Examples: understand a result, prepare for an appointment, record a measurement, complete a questionnaire, view a care plan, send a message, schedule, understand what happens next, or find product-supplied help information.

Do not start from “show all available record data.”

## Information order

A useful focused sequence is:

1. what this is;
2. current status/result;
3. what it means when interpretation is supplied by the product;
4. what to do next;
5. when to seek help when supplied by approved product content;
6. supporting detail;
7. history/source.

Do not invent clinical interpretation, reassurance, escalation advice or thresholds.

## Language and density

Prefer everyday terms, short sentences, active voice and explicit next actions. Default to lower density than clinician workspaces without exaggerated whitespace. Use progressive disclosure rather than deleting source detail.

## Results

Show value, unit and time as relevant; use supplied status/interpretation only; show a useful trend when it helps; keep the next action clear. Do not infer “normal” from absence of a flag.

## Mobile and forms

Use practical targets, visible labels, appropriate keyboard types, no hover-only core content and responsive reflow. Keep units/formats explicit, preserve input after recoverable failures and never convert unknown into negative.

## Privacy-aware presentation

Consider shared devices and notification previews. Avoid exposing unnecessary sensitive detail by default. This skill does not define privacy law.

## Warnings

When warning/help-seeking content is supplied, use a clear heading, concise specific text, explicit action and non-color cues. Do not invent medical advice.

## Tone

Use calm, precise language. Avoid gamified celebration for serious states, infantilizing copy, cute mascots around warnings and generic wellness decoration that competes with instructions.

## AI

Label generated content, describe capability concretely, keep source record distinguishable, preserve human-contact paths when supplied, and do not use sparkle/glow as evidence of trust.

## Anti-slop traps

- wellness gradients everywhere;
- giant greeting/avatar;
- invented health score;
- arbitrary activity rings;
- card dashboard for every record category;
- sparkles next to explanations;
- illustration before important information;
- raw EHR dump;
- badges for every status;
- hidden next action.

## Finish gate

- [ ] primary patient task obvious;
- [ ] next action clear;
- [ ] interpretation/advice not invented;
- [ ] language understandable;
- [ ] mobile/touch practical;
- [ ] warnings specific and non-color-only;
- [ ] source and generated content distinguishable;
- [ ] privacy exposure considered;
- [ ] anti-slop audit passed.

## Boundary

This skill does not provide medical advice, determine clinical interpretation, define escalation thresholds or establish privacy/legal compliance.
