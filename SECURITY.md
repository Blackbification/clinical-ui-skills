# Security and safety reporting

Clinical UI Skills contains prompts/instructions, evaluation fixtures and heuristic tooling. It is not a clinical decision engine, but defects in this repository can still encourage unsafe interface behavior.

## Security vulnerabilities

If the repository has GitHub Private Vulnerability Reporting enabled, use it for security-sensitive reports. Do not publish exploit details in a public issue before maintainers have had an opportunity to review them.

## Clinical UI safety concerns

For a rule, example or eval that could plausibly encourage wrong-patient action, misleading clinical state, inaccessible critical information or another high-consequence use error, open a `Clinical UI safety concern` issue unless the report itself contains sensitive security information.

## Never submit patient data

Do not include PHI/PII, screenshots of real patient records, credentials, private endpoints, secrets, confidential customer material or lightly de-identified clinical records in any report. Reproduce the issue with synthetic data.

## Scope

A report against this repository is not a substitute for reporting a vulnerability or safety event to the affected healthcare product, institution, manufacturer or relevant authority.
