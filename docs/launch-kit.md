# Launch Kit

## GitHub metadata

**Repository name:** `clinical-ui-skills`

**Description:**  
Open Agent Skills for healthcare frontends: reduce generic AI slop while improving task hierarchy, safety-oriented UI, accessibility and clinical design discipline. Includes 12 skills, 72 evals and ClinicalUIBench.

**Topics:**

```text
agent-skills healthcare healthtech clinical-informatics health-it frontend ui-ux
human-factors accessibility ai-agents anti-slop clinical-dashboard patient-portal
clinical-software codex claude-code cursor
```

**One-line pitch:**  
> Same model. Same healthcare task. Better design discipline.

**Repo rule:**  
> NO UNEXAMINED DEFAULTS.

## Best launch visual

Use [`../examples/demo-01-inpatient-worklist/comparison.png`](../examples/demo-01-inpatient-worklist/comparison.png) first. It shows the core idea better than a logo: generic dashboard grammar on the left, task-first clinical worklist on the right.

## LinkedIn — English

I kept asking coding agents for healthcare software and getting the same product back.

Sidebar.  
Four KPI cards.  
Rounded panels.  
Colored pills.  
A donut chart nobody asked for.  
Sparkles because “AI”.

That is annoying in generic SaaS.

In healthcare, the bigger problem is that the **same defaults can become the information architecture**.

So I built **Clinical UI Skills** and released it under MIT.

It is an open suite of Agent Skills for coding agents building clinician dashboards, patient charts, patient operations, forms, results/trends, patient apps and visible AI features.

The principle is simple:

**Healthcare UI quality ≠ visual novelty.**

The agent should reason first about:

user → task → consequence → patient/action scope → information hierarchy → semantic state → accessibility → representation → visual system.

Anti-slop itself is only **5/100** in the Clinical UI Score.

Because a screen can have zero purple gradients and still be terrible clinical software.

v0.1 ships with:

- **12 Agent Skills**;
- **72 synthetic evals** across 10 categories;
- Clinical Slop Catalog;
- Clinical UI Score + AI Slop Score;
- ClinicalUIBench protocol and scoring tooling;
- an installer and heuristic frontend linter;
- 3 reproducible before/after demos.

And one rule:

**NO UNEXAMINED DEFAULTS.**

I do not want the community to tell me the screenshots look nice.

I want the opposite: find the healthcare workflow where a rule fails, recreate it with synthetic data and submit it.

Same model. Same task. Vanilla vs Clinical UI Skills.

**#ClinicalUIChallenge**

Created by **Juan Mora Delgado**. MIT licensed.

## LinkedIn — Spanish

Llevaba tiempo pidiendo a agentes de código interfaces sanitarias y recibiendo el mismo producto.

Sidebar.  
Cuatro KPI cards.  
Paneles redondeados.  
Pills de colores.  
Un donut que nadie pidió.  
Sparkles porque “AI”.

El problema no es que sea feo o repetitivo.

El problema es que, en software sanitario, esos defaults pueden acabar convirtiéndose en la **arquitectura de información**.

Por eso he creado **Clinical UI Skills** y lo libero con licencia MIT.

Es una suite abierta de Agent Skills para agentes que construyen cuadros de mando clínicos, historias de paciente, gestión operativa, formularios, resultados, apps para pacientes y funciones visibles de IA.

La idea:

**la calidad de una UI clínica no es originalidad visual.**

Primero hay que razonar sobre:

usuario → tarea → consecuencia → contexto del paciente/acción → jerarquía → estados → accesibilidad → representación → sistema visual.

De hecho, el anti-slop sólo pesa **5/100** en el Clinical UI Score.

Porque puedes quitar todos los gradientes violetas y seguir teniendo una interfaz clínica pésima.

La v0.1 sale ya con:

- **12 skills**;
- **72 evals sintéticos**;
- Clinical Slop Catalog;
- Clinical UI Score + AI Slop Score;
- ClinicalUIBench;
- installer + linter;
- 3 before/after reproducibles.

Y una sola regla:

**NO UNEXAMINED DEFAULTS.**

No quiero que la comunidad me diga “qué bonito”.

Quiero que encuentre dónde falla, lo reproduzca con datos sintéticos y lo convierta en una nueva regla o eval.

Mismo modelo. Misma tarea. Vanilla vs Clinical UI Skills.

**#ClinicalUIChallenge**

Creado por **Juan Mora Delgado**. MIT.

## X / Bluesky thread

**1/** Coding agents have a healthcare UI default: sidebar + KPI cards + rounded panels + pills + decorative charts + sparkle AI. I open-sourced **Clinical UI Skills** to make the agent reason before it decorates.

**2/** It is not “never use cards”. The rule is **NO UNEXAMINED DEFAULTS.** Start with user → task → consequence → scope → hierarchy → state → accessibility → representation.

**3/** Anti-slop is only 5/100 in the score. Safety/error resistance, context, hierarchy, task efficiency and accessibility matter far more. A non-sloppy UI can still be bad clinical software.

**4/** v0.1: 12 Agent Skills + 72 synthetic evals + ClinicalUIBench + linter/installer + 3 reproducible before/after demos. MIT.

**5/** The test I want: same model + same task. Vanilla vs Clinical UI Skills. Publish both. Report regressions too. **#ClinicalUIChallenge**

**6/** Created by Juan Mora Delgado. If you build healthtech/EHR/patient apps, break it with synthetic cases and contribute the failure mode we missed.

## Show HN

**Title:**  
Show HN: Clinical UI Skills – 12 Agent Skills for less generic healthcare frontend generation

**Body:**

I built Clinical UI Skills after noticing that coding agents often interpret “clinical dashboard” as an aesthetic category instead of a workflow. They reach for KPI cards, card grids, pills and decorative charts before asking what the clinician is actually scanning, comparing or acting on.

The project is not a design system and does not ban those components. It changes the decision process: identify user/task/consequence/device, establish patient/action context, define semantic states before colors, choose representation by task, then audit the rendered result.

v0.1 includes 12 SKILL.md skills, 72 synthetic evals, a 100-point Clinical UI Score, separate AI Slop Score, a heuristic source linter, an install helper, three reproducible before/after demos and the ClinicalUIBench protocol/scoring tools.

Anti-slop is deliberately only 5/100. Safety/error resistance, hierarchy, task efficiency and accessibility dominate.

The demos are illustrative, not evidence of benchmark superiority. The next step is controlled same-model/same-task comparisons with blinded review. I would especially value counterexamples and regressions.

MIT licensed. Created by Juan Mora Delgado.

## Reddit / community post

**Title:** I open-sourced 12 Agent Skills for healthcare frontend generation — looking for failure modes, not compliments

I kept seeing coding agents solve “clinical dashboard” as a visual genre rather than a workflow. Clinical UI Skills tries to make the agent reason from task/context/state first.

v0.1 has 12 skills, 72 synthetic evals, ClinicalUIBench scoring/protocol, an installer/linter and three reproducible demos. MIT licensed.

The important constraint: anti-slop is only 5% of the score. A pretty non-generic interface can still be unsafe, inaccessible or terrible for clinical work.

I am looking for hard counterexamples: workflows where a rule pushes the UI in the wrong direction, missing states, accessibility regressions and generated patterns we should add to the catalog. Synthetic examples only — no PHI/confidential screenshots.

## Pinned GitHub Discussion

**Title:** What recurring AI-generated healthcare UI pattern should become the next eval?

Not “what design trend do you dislike?”

Describe:
1. primary user;
2. task;
3. generated pattern;
4. why it damages the task;
5. better direction;
6. a synthetic way to reproduce it.

The best submissions become: catalog entry → eval assertion → ClinicalUIBench case.

## Release-day sequence

1. Create public repo and push the release package.
2. Set description, topics and `assets/social-preview.png`.
3. Confirm Actions are green.
4. Create GitHub Release `v0.1.0` from `RELEASE_NOTES_v0.1.0.md`.
5. Enable Discussions and open the pinned prompt above.
6. Open 4–6 genuine starter issues from `initial-issues.md`.
7. LinkedIn: use inpatient worklist comparison image.
8. X/Bluesky: publish the thread with the same visual.
9. Show HN once the URL is stable and README images render correctly.
10. Ask specifically for counterexamples, benchmark runs and slop-pattern submissions.

## First-week growth loop

```text
AI-generated failure
        ↓
synthetic community reproduction
        ↓
Clinical Slop Catalog
        ↓
new eval/assertion
        ↓
ClinicalUIBench run
        ↓
shareable before/after + score
        ↓
more reproductions
```

A community that contributes **failures** is more valuable than launch-day likes.
