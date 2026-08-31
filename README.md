# Clinical UI Skills

**Stop coding agents from turning healthcare software into generic AI SaaS.**

[![License: MIT](https://img.shields.io/badge/License-MIT-111827.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-111827.svg)](https://agentskills.io)
[![Clinical UI Score](https://img.shields.io/badge/Clinical%20UI%20Score-100-111827.svg)](references/clinical-ui-score.md)
[![Skills](https://img.shields.io/badge/skills-12-111827.svg)](skills/manifest.json)
[![Evals](https://img.shields.io/badge/evals-72-111827.svg)](evals/index.json)

**Created by Juan Mora Delgado.** Open source under the MIT License.

Clinical UI Skills is an open set of Agent Skills for coding agents building healthcare frontends: clinician dashboards, patient charts, patient portals, patient mobile apps, results review, worklists, monitoring surfaces and clinical operations software.

The project is deliberately **not another healthcare design system**. It does not prescribe one palette, one component library or one aesthetic. It gives an agent a better decision process: start with the user, task, risk, information hierarchy, device and environment — then design.

> **Healthcare UI quality ≠ visual novelty.** The right user should see the right information, in the right hierarchy, at the right moment, and be able to perform the right action with minimal ambiguity.

## The problem

Ask a coding agent for a healthcare dashboard and it will often reach for the same statistically comfortable defaults:

`sidebar → KPI cards → rounded panels → colored pills → decorative chart → huge whitespace → sparkle/AI affordance`

That may be harmless on a landing page. In clinical software it can hide the work object, flatten urgency, separate values from units, blur current vs historical state, make loading look like “none”, or turn a dense scanning task into a collection of decorative cards.

**Clinical UI Skills attacks the reasoning failure behind the aesthetic tell.**

Not: “never use cards.”  
Instead: “justify the representation against the task.”

Not: “never use blue.”  
Instead: “do not mistake healthcare for a generic palette.”

Not: “make it unique.”  
Instead: “make every important visual decision intentional.”

## The one rule

```text
NO UNEXAMINED DEFAULTS.
```

If the answer to “why this card / chart / color / interaction / density?” is only “because it looks modern”, redesign it.

## What ships in v0.1

| Skill | What it changes |
|---|---|
| `clinical-ui` | Routes by user, surface, risk, density, device and environment before layout decisions. |
| `anti-slop-core` | Removes generic AI frontend defaults without replacing them with novelty theater. |
| `clinician-dashboard` | Optimizes multi-patient views and worklists for scan, compare, detect, prioritize and act. |
| `patient-chart` | Protects patient context, temporal integrity, provenance and longitudinal navigation. |
| `patient-management` | Covers search, queues, appointments, wards, beds and operational workflows. |
| `clinical-forms` | Makes clinical/patient data entry explicit about units, unknowns, defaults, errors and recovery. |
| `clinical-safety-ui` | Handles patient scope, warnings, critical states, missingness, confirmations and destructive actions. |
| `clinical-data-viz` | Keeps results, trends, ranges, timestamps and missing data interpretable. |
| `patient-facing-ui` | Prevents “EHR miniaturization”; favors comprehension, next action and progressive disclosure. |
| `clinical-accessibility` | Applies accessibility to real healthcare interaction conditions, not as an end-stage checklist. |
| `clinical-ai-ui` | Governs visible AI surfaces, provenance, uncertainty, review and action boundaries. |
| `clinical-ui-audit` | Scores rendered/code evidence and returns blockers, prioritized fixes and a verification plan. |

The suite is modular. Install all 12 skills or use the `clinician`, `patient`, `operations` or `ai` presets. Safety and accessibility remain cross-cutting rather than optional.

## Use it in 60 seconds

The repository follows the open Agent Skills `SKILL.md` convention.

Clone or download this repository and use the stdlib-only installer, or copy the skill folders directly.

```bash
# See available presets
python scripts/install_skills.py --help

# Install the complete suite
python scripts/install_skills.py --preset all --target .agents/skills

# Smaller task-oriented presets
python scripts/install_skills.py --preset clinician --target .agents/skills
python scripts/install_skills.py --preset patient --target .agents/skills
python scripts/install_skills.py --preset operations --target .agents/skills
python scripts/install_skills.py --preset ai --target .agents/skills
```

For Claude Code or Cursor, change `--target` to `.claude/skills` or `.cursor/skills`.

Then prompt normally:

```text
Build a desktop worklist for an internal-medicine team reviewing 24 hospitalized patients.
Use clinical-ui, anti-slop-core and clinician-dashboard.
Prioritize patient identity, what changed, pending work and next actions.
```

Or audit an existing implementation:

```text
Audit this healthcare frontend using clinical-ui-audit.
Return the Clinical UI Score, AI Slop Score, blockers, top fixes and verification plan.
```

## Same model. Same prompt. Different design discipline.

The project is built around a simple benchmarkable idea:

```text
CONDITION A                  CONDITION B                  CONDITION C
Vanilla coding agent   vs   Generic anti-slop      vs   Clinical UI Skills
```

The goal is not to prove that one screenshot is prettier. The goal is to measure whether the output is better at the work healthcare software actually needs to support.

## Three synthetic before/after demos

The repository ships rendered examples so the project can be judged visually before anyone installs it. These are illustrative demos using synthetic data — not claims from a controlled benchmark run.

### Inpatient worklist

![Vanilla agent vs Clinical UI Skills — inpatient worklist](examples/demo-01-inpatient-worklist/comparison.png)

### Longitudinal patient chart

![Vanilla agent vs Clinical UI Skills — patient chart](examples/demo-02-patient-chart/comparison.png)

### Patient-facing app

![Vanilla agent vs Clinical UI Skills — patient app](examples/demo-03-patient-app/comparison.png)

The HTML sources and individual screenshots are committed under [`examples/`](examples/), and can be regenerated with `python scripts/render_demos.py`.

## Clinical UI Score

Anti-slop is intentionally only **5 points out of 100**.

| Dimension | Weight |
|---|---:|
| Clinical context fit | 15 |
| Information hierarchy | 15 |
| Task efficiency | 15 |
| Safety & error resistance | **20** |
| Accessibility | 15 |
| Data clarity | 10 |
| Visual intentionality | 5 |
| Anti-slop discipline | **5** |
| **Total** | **100** |

A screen can have **zero AI slop and still be a bad clinical interface**. That is why safety, hierarchy, task performance and accessibility dominate the score.

The separate **AI Slop Score** runs from `0` (no meaningful generic tells) to `10` (heavily templated/generic). See [`references/clinical-ui-score.md`](references/clinical-ui-score.md).

## Clinical Slop Catalog

The repository includes a growing taxonomy of patterns such as:

- `KPI preamble`
- `card soup`
- `healthcare-blue autopilot`
- `priority-severity conflation`
- `historical fade`
- `empty means none`
- `unit on hover`
- `default-as-answer`
- `red means everything`
- `banner stack`
- `donut reflex`
- `gauge theater`
- `missing-data interpolation`
- `EHR miniaturization`
- `AI summary takeover`
- `sparkle-as-trust`
- `chat for everything`

Each pattern is documented as **signal → why it fails → better direction**, not as a taste-only prohibition. See [`references/clinical-slop-catalog.md`](references/clinical-slop-catalog.md).

## ClinicalUIBench starts here

`evals/index.json` includes **72 synthetic v0.1 scenarios across 10 categories**, including:

- inpatient worklists;
- anticoagulation review;
- tablet ward rounds;
- results review;
- medication reconciliation;
- longitudinal patient charts;
- patient-facing blood-pressure entry;
- lab-result explanation;
- medication schedules;
- loading / empty / unavailable state integrity;
- responsive degradation;
- accessibility failures;
- AI-generated patient summaries;
- generic healthcare SaaS redesigns.

Each eval has explicit assertions. The repository already includes the **ClinicalUIBench** protocol, rubric, submission schema, scorer, blinding/adjudication guidance and leaderboard builder under [`benchmarks/`](benchmarks/). Public leaderboard claims should be based on controlled, reviewable submissions — not the illustrative demos above.

## Run the project checks

```bash
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

Run the heuristic source linter against a frontend:

```bash
python scripts/clinical_ui_lint.py ./src
python scripts/clinical_ui_lint.py ./src --json
python scripts/clinical_ui_lint.py ./src --fail-on HIGH
```

The linter is intentionally conservative: **a warning is evidence to inspect, not a safety or design verdict.**

## The #ClinicalUIChallenge

This is the fastest way to show whether the project matters.

1. Pick one eval prompt.
2. Generate it once with a vanilla coding agent.
3. Generate it again with Clinical UI Skills.
4. Use synthetic data only.
5. Score both with `clinical-ui-audit`.
6. Submit the before/after through the challenge template.

The constraint is the point: **same task, comparable model, visible difference**.

See [`docs/clinical-ui-challenge.md`](docs/clinical-ui-challenge.md).

## Help build the Wall of Clinical Slop

Found a recurring AI-generated healthcare UI failure? Open a **“Show us the slop”** issue.

Good submissions are patterns, not screenshots of real systems. Recreate the problem with synthetic data, explain the task it damages, and suggest the better direction. Never upload PHI/PII or confidential product material.

The best patterns can graduate into the Clinical Slop Catalog and new benchmark assertions.

## Evidence, not aesthetic dogma

The project is informed by public human-factors, health-IT, accessibility and open healthcare software sources including FDA human-factors guidance, NIST health-IT usability work, ONC SAFER Guides, WCAG 2.2, NHS service patterns and OpenMRS frontend modules.

See [`EVIDENCE.md`](EVIDENCE.md) and [`references/evidence-map.md`](references/evidence-map.md).

Rules are separated by evidence strength. A project heuristic must not masquerade as a regulatory requirement.

## What this project is not

Clinical UI Skills is **not**:

- medical-device certification;
- proof of regulatory compliance;
- a substitute for human-factors/usability validation;
- a source of clinical thresholds, diagnostic logic or treatment decisions;
- a guarantee of WCAG conformance;
- permission to use real patient data in examples or evals.

For safety-critical or regulated products, validate with representative users in the intended environment and follow applicable regulatory, quality, security, privacy and risk-management requirements.

## Data rule

**Synthetic data only** in public examples, fixtures, screenshots, issues, benchmark submissions and demos. Synthetic records must not be lightly altered copies of real patient records.

## Contribute

The highest-value contributions are:

- a repeatable clinical UI failure pattern;
- a better conditional rule;
- a new synthetic eval with clear assertions;
- a before/after challenge submission;
- evidence that strengthens, narrows or disproves a heuristic;
- a reproducible accessibility or interaction failure;
- a clinical workflow the current skills model badly.

Read [`CONTRIBUTING.md`](CONTRIBUTING.md). The repository includes structured issue forms and a pull-request template.

## Roadmap

**v0.2** — browser/screenshot audit harness, accessibility adapters, component-library integration examples, machine-readable audit output and broader workflow coverage.  
**v0.3** — controlled multi-model benchmark runs, blinded multi-reviewer scoring, inter-rater reliability and regression tracking.  
**v1.0** — stable skill contracts and a versioned methodology after real public use and contributor feedback.

See [`docs/roadmap.md`](docs/roadmap.md).

## Credits

**Created and directed by Juan Mora Delgado.**

See [`CREDITS.md`](CREDITS.md) for project acknowledgements and source-project attribution notes. References to external projects or institutions do not imply endorsement.

## License

MIT License — Copyright © 2026 Juan Mora Delgado. See [`LICENSE`](LICENSE).

---

If this repository saves one healthcare product from becoming another **rounded-card + donut-chart + sparkle-AI dashboard**, star it, run the **#ClinicalUIChallenge**, and contribute the failure pattern your team keeps seeing.
