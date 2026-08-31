# ClinicalUIBench Protocol

## Goal

Test whether a design-skill condition changes the quality of generated healthcare frontend outputs under a controlled task.

## Reproducibility contract

Record:

- eval ID and exact prompt;
- model and version/date if available;
- coding agent/client;
- skill condition;
- frontend framework / starter template;
- tool/browser access;
- iteration budget and whether screenshots were available to the model;
- viewport(s);
- generated source and screenshots;
- deviations from the base prompt.

## Generation

Use synthetic fixture data only. Do not manually redesign one condition after generation unless the same intervention is permitted for all conditions and recorded.

## Review

Prefer at least two independent reviewers for public comparative claims. Reviewers score the eight dimensions and record findings with evidence. For strong claims, blind condition identity when feasible.

## Interpretation

The benchmark measures the project rubric, not clinical correctness or regulatory compliance. Avoid generalizing from a small number of scenarios/models.
