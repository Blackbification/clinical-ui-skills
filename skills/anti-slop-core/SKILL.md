---
name: anti-slop-core
description: "Prevents generic AI-generated frontend aesthetics by forcing product-specific visual decisions, appropriate density, purposeful components and a rendered anti-slop review. Use for generating or reviewing healthcare UI and other product interfaces where generic vibe-coded patterns should be avoided."
license: MIT
compatibility: Codex, Claude Code, Cursor, and agents supporting Agent Skills-style SKILL.md instructions.
metadata:
  author: "Juan Mora Delgado"
  version: "0.1.0"
  project: clinical-ui-skills
---

# Anti-Slop Core

Prevent generic AI frontend defaults without turning “anti-slop” into another rigid visual style.

## Core principle

**No unexamined defaults.**

Do not ban a component merely because AI often uses it. Ask whether it earns its place for this product, user and task.

In healthcare, safety, accessibility and task efficiency override distinctiveness.

## Common tells — inspect, do not auto-ban

### Layout

- sidebar + header + equal card grid regardless of task;
- bento for data needing alignment/comparison;
- excessive centered composition in work surfaces;
- one visual container per concept;
- nested card-on-card hierarchy;
- large empty gutters reducing professional scan density;
- identical spacing/border/radius for every section.

### Components

- icon inside colored rounded square for every section;
- pill/badge for every state/category/date;
- stat cards for values that do not drive decisions;
- progress rings/gauges without a meaningful bounded target;
- giant search/command surfaces used decoratively.

### Visuals

- default purple/blue gradients;
- decorative glass/backdrop blur;
- colored glow/shadow;
- excessive large radii;
- generic blue/teal chosen only because product is healthcare;
- indiscriminate pastel severity colors.

### Typography

- undifferentiated scale;
- huge display headings inside operational software;
- labels too faint to scan;
- tiny metadata everywhere to look “premium”.

### Motion

- entrance animation on every card;
- hover-scale on routine controls;
- pulsing after loading is complete;
- motion competing with warnings/monitoring.

### Data visualization

- donut because value is a percentage;
- area gradient because a line looked plain;
- KPI cards before the worklist;
- charts for single values;
- axes/units hidden for minimalism;
- chart + number + progress ring duplicating the same fact.

### AI surfaces

- sparkle icon as universal AI identifier;
- purple “Ask AI” pill floating over product;
- orb/glow/avatar with no interaction reason;
- chat chosen where structured UI would be faster;
- vague “AI-powered insights” cards;
- generated summary placed above source data regardless of task.

## Generation workflow

### 1. State visual intent

```text
Visual intent:
Density:
Layout strategy:
Type strategy:
Color strategy:
Component strategy:
Motion policy:
What must NOT look generic here:
```

### 2. Commit to a small token system

Define background/surface, text, border/divider, semantic state, focus, spacing, radius, elevation, type and motion. Avoid decorative token proliferation.

### 3. Earn every container

Before a card: does the boundary communicate grouping, interaction or useful separation? Would alignment/spacing alone be clearer?

### 4. Earn every chart

What question does it answer? Would a number/table/compact trend answer faster? Are units, time and missing data explicit?

### 5. Earn every accent

Accent should support hierarchy, interaction, semantics or brand identity — not act as wallpaper.

### 6. Render

Anti-slop review should inspect rendered output, not source alone.

## Review mode

1. identify primary task;
2. list generic tells;
3. separate aesthetic clichés from usability problems;
4. prioritize fixes that improve task performance first;
5. propose coherent visual direction;
6. give AI Slop Score;
7. preserve familiar patterns when familiarity benefits task.

## AI Slop Score 0–10

- `0–1`: highly intentional;
- `2–3`: minor defaults;
- `4–5`: recognizable template tendencies;
- `6–7`: several dominant AI patterns;
- `8–9`: strongly vibe-coded;
- `10`: nearly every major decision appears unexamined.

Novelty is not evidence of quality.

## Healthcare override

Do not remove density just to create whitespace; hide familiar controls for minimalism; replace useful tables with novel layouts; mute warning contrast for palette harmony; invent creative severity encodings; obscure units/timestamps/patient context; or turn critical text into icons to reduce clutter.

## Better directions

- Equal KPI cards → integrate useful counts into filters/tabs/headers or put work object first.
- Status-pill soup → aligned text/columns/compact semantic indicators.
- Card soup → regions, dividers, headings, aligned rows.
- Decorative charts → number, delta, sparkline, table or no chart.
- Generic AI insight → source-linked structured output close to the task.
- Huge whitespace → density tuned to expertise and frequency.

## Finish gate

- [ ] visual direction explicit;
- [ ] density justified;
- [ ] layout matches task;
- [ ] repeated cards justified;
- [ ] every chart answers a question;
- [ ] semantic colors coherent;
- [ ] motion functional;
- [ ] generic AI ornament does not compete with content;
- [ ] accessibility/safety preserved;
- [ ] rendered UI reviewed;
- [ ] AI Slop Score has rationale.

## Boundaries

Do not copy a reference product's visual identity, infer one style is universally premium, force novelty, claim a slop heuristic proves usability, or violate accessible patterns for originality.
