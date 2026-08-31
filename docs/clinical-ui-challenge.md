# #ClinicalUIChallenge

A public, reproducible before/after challenge for healthcare frontend generation.

## Purpose

The challenge is designed to answer a narrow question:

> Does adding Clinical UI Skills materially improve the frontend produced for the same healthcare UI task?

It is not a clinical validation study and should not be presented as one.

## Protocol

1. Choose an eval from `evals/index.json`, or propose a new synthetic scenario.
2. Record the model/tool and relevant version when known.
3. Run **Condition A — Vanilla** with no Clinical UI Skills.
4. Run **Condition B — Clinical UI Skills** with the same task and comparable generation settings.
5. Do not manually redesign one condition more than the other.
6. Use only synthetic data.
7. Capture the same viewport and state for both outputs.
8. Audit both outputs using `clinical-ui-audit`.
9. Publish the prompt, screenshots, score, major differences and limitations.

Optional third condition:

- **Condition C — Generic anti-slop skill**, to separate generic visual cleanup from healthcare-specific UI reasoning.

## Submission structure

```text
Challenge ID:
Model/tool:
Date:
Eval/prompt:
Viewport:

Vanilla output:
Clinical UI Skills output:

Vanilla Clinical UI Score:
Skills Clinical UI Score:
Vanilla AI Slop Score:
Skills AI Slop Score:

Largest improvement:
Largest regression:
Unexpected result:
Limitations:
```

## Rules

- Synthetic data only.
- No screenshots of real EHRs or patient records.
- No confidential product screenshots.
- Do not cherry-pick only flattering cases when reporting aggregate results.
- Aesthetic preference alone is not a benchmark assertion.
- Report regressions. They are useful.

## What makes a strong submission

A strong challenge demonstrates a task-level difference: faster scan path, clearer patient scope, better current-vs-historical state, more appropriate density, better responsive behavior, less warning noise, better units/timestamps, or fewer accessibility traps.

A weak submission is simply “the second one looks nicer.”
