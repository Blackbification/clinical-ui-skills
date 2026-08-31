# ClinicalUIBench

ClinicalUIBench is the evaluation layer of Clinical UI Skills. It compares frontend outputs under controlled prompts and scores **task fit, hierarchy, efficiency, safety-oriented UI behavior, accessibility, data clarity, visual intentionality and anti-slop discipline**.

It is not a clinical-validation, regulatory-compliance or medical-device benchmark.

## Conditions

Recommended three-condition comparison:

1. `vanilla` — model/agent without design skill;
2. `generic-anti-slop` — same model/agent with a non-healthcare anti-slop skill;
3. `clinical-ui-skills` — same model/agent with the relevant skills from this repository.

Keep model, prompt, tool access, framework and iteration budget as comparable as practical. Record deviations.

## What is scored

A human or evaluation agent supplies dimension scores using `rubric.json`. `scripts/score_submission.py` applies weights/caps and emits the final 0–100 Clinical UI Score plus the separate 0–10 AI Slop Score.

## Files

- `rubric.json` — machine-readable dimensions and caps;
- `submission.schema.json` — documented submission shape;
- `sample-submission.json` — synthetic example;
- `leaderboard-template.csv` — public leaderboard columns;
- `protocol.md` — reproducibility protocol;
- `blinding.md` — recommended blinded review;
- `adjudication.md` — handling reviewer disagreement.

## Commands

```bash
python scripts/validate_submission.py benchmarks/sample-submission.json
python scripts/score_submission.py benchmarks/sample-submission.json
python scripts/build_leaderboard.py benchmarks/submissions --out benchmarks/leaderboard.csv
```

Do not publish PHI/PII, confidential product screens or proprietary clinical datasets.
