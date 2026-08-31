.PHONY: check validate test evals lint-demo
check: validate test
validate:
	python scripts/validate_skills.py
	python scripts/validate_evals.py
	python scripts/validate_submission.py benchmarks/sample-submission.json
test:
	python -m unittest discover -s tests -v
evals:
	python scripts/run_evals.py
lint-demo:
	python scripts/clinical_ui_lint.py examples
