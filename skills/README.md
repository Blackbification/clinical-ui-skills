# Skill Suite

Machine-readable suite metadata and install presets live in [`manifest.json`](manifest.json).

Recommended loading pattern: start with `clinical-ui` + `anti-slop-core`, add domain skills required by the task, add `clinical-safety-ui` and `clinical-accessibility` for consequential healthcare workflows, and finish with `clinical-ui-audit`.

Do not load every skill blindly when context budget is tight. The installer presets are convenience bundles, not mandatory runtime bundles.
