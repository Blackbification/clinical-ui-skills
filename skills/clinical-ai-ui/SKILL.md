---
name: clinical-ai-ui
description: "Designs and audits visible AI features in healthcare frontends, including generated summaries, extraction review, assistants and agent actions, with explicit provenance, uncertainty, human review, action scope and failure states."
license: MIT
compatibility: Codex, Claude Code, Cursor, and agents supporting Agent Skills-style SKILL.md instructions.
metadata:
  author: "Juan Mora Delgado"
  version: "0.1.0"
  project: clinical-ui-skills
---

# Clinical AI UI

Design the UI around the **job the AI performs**, not around the fact that AI exists.

## Choose interaction by job

- generated summary → source-linked summary;
- extraction → source/value review table;
- candidate issues → ranked/filtered review list;
- drafted message/note → editable draft with source context;
- agent action → explicit proposed action + scope + confirmation when consequence justifies it;
- open-ended exploration → chat may be appropriate.

Chat is one pattern, not the default container for AI.

## Source versus generated

Keep source fact, product-computed state, AI extraction, AI summary/inference and human-authored/signed content visually distinguishable. Do not imply that a sparkle icon communicates provenance.

## Provenance

When supported and verification matters, expose source anchors/snippets close to generated claims. Never fabricate citations.

## Uncertainty

Represent uncertainty only when the system provides a meaningful signal. Do not invent confidence percentages or vague pseudo-precision.

## Human review

Make accepted/rejected/edited states explicit. For bulk review, support structured comparison and exceptions rather than one modal per suggestion.

## AI actions

Show proposed action, target patient/object, critical parameters, preview versus executed state, confirmation when warranted, and clear success/failure. Never silently broaden scope.

## Patient-facing AI

Use plain language, preserve supplied human-contact/escalation paths, and avoid anthropomorphic/glowing trust cues.

## Streaming and failure

Incomplete streamed output must not look final. State generating/complete/failed/stale. On failure, say what failed, what scope was affected, whether anything changed and what can happen next.

## Anti-slop traps

- sparkle = trustworthy AI;
- purple gradient/glow as AI identity;
- vague “Ask AI” pill;
- assistant orb covering content;
- chat for deterministic structured tasks;
- AI summary dominating chart first viewport;
- invented confidence percentage;
- generated content visually identical to source record;
- magical insight cards with no provenance;
- agent actions buried in prose.

## Required contract

```text
User task:
AI job:
Source data:
Generated content:
Source/generated distinction:
Provenance strategy:
Uncertainty strategy:
Review model:
Action scope/reversibility:
Failure states:
Why chat is/is not appropriate:
```

## Finish gate

- [ ] AI job explicit;
- [ ] interaction matches task;
- [ ] generated content distinguishable from source;
- [ ] provenance available when supported/needed;
- [ ] uncertainty not fabricated;
- [ ] review state explicit;
- [ ] proposed vs executed actions distinct;
- [ ] action scope visible;
- [ ] incomplete output cannot masquerade as final;
- [ ] failure state specific;
- [ ] no decorative trust signals;
- [ ] anti-slop audit passed.

## Boundary

This skill does not determine whether an AI model is clinically valid, safe, compliant or appropriate for a medical purpose.
