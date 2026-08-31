# Evals

`index.json` + `scenarios/*.json` contains **72 synthetic scenarios** covering dashboards, patient charts, patient management, forms, clinical data visualization, patient-facing UI, accessibility, safety, AI surfaces and responsive behavior.

Each eval includes `id`, `category`, `risk`, `title`, `prompt`, `expected_output`, optional `files` and explicit behavioral assertions.

```bash
python scripts/validate_evals.py
python scripts/run_evals.py
python scripts/run_evals.py --category patient-management
python scripts/run_evals.py --id ai-03
```

The runner does not call a model. It is a reproducible feed for an agent or evaluation harness.

All public eval data and screenshots must be synthetic.
