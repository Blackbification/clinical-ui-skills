# Clinical Slop Catalog

Recurring AI-generated frontend failure modes. These are **signals to inspect**, not absolute bans.

Format: **Signal → why it fails → better direction**.

## A. Generic interface slop

### A01 Card soup
Nearly every section is inside a rounded card → hierarchy becomes container-driven and dense clinical surfaces become scroll-heavy → use regions, alignment, headings, dividers and whitespace; reserve cards for meaningful object/group boundaries.

### A02 Nested card soup
Cards contain subcards/tiles/badges → multiple boundaries compete with content → flatten hierarchy.

### A03 KPI preamble
3–6 metric cards consume first viewport → aggregate numbers displace actionable work → integrate useful counts into filters/tabs/headers unless metrics are the task.

### A04 Bento by default
Modular blocks regardless of comparison needs → data loses alignment and stable scan paths → choose table/list/timeline by task.

### A05 Healthcare-blue autopilot
Blue/teal chosen only because product is medical → generic identity and muddled semantics → separate brand color from clinical semantic color.

### A06 Purple AI accent
Purple/indigo gradient around AI controls → cliché becomes stronger than capability → use descriptive labels integrated into product hierarchy.

### A07 Glass for depth
Backdrop blur/frosted panels in operational UI → contrast/noise cost with weak task value → solid surfaces unless translucency communicates a real layer.

### A08 Radius inflation
Large radius on nearly everything → all components gain equal personality and density falls → small radius scale tied to anatomy.

### A09 Shadow wallpaper
Shadow on every container → meaningful elevation loses signal → border/surface/spacing for static grouping.

### A10 Gradient as content substitute
Gradient header/background makes sparse UI feel designed → visual weight without information → fix hierarchy and typography first.

### A11 Icon-tile taxonomy
Every heading gets a rounded colored icon box → decoration dominates scanning → text headings; icons only when recognition/action benefits.

### A12 Pill soup
Metadata/state/category/date/action all become pills → semantic distinction collapses → aligned text/columns/subtle markers; reserve strong badges.

### A13 Hero inside software
Greeting/illustration/huge title dominates operational app → steals first viewport from work → compact context header.

### A14 Empty-space prestige
Huge gaps on expert desktop screens → more eye travel/scrolling → task-appropriate density.

### A15 Identical section weight
All modules same size/border/title/icon/spacing → no semantic hierarchy → vary emphasis by task/consequence.

## B. Clinician-dashboard slop

### B01 Executive dashboard masquerading as worklist
Charts/totals before patients/tasks → action objects hidden → worklist first.

### B02 Patient-as-card grid
One large card per patient → poor comparison and low density → aligned rows/table when scanning many patients.

### B03 Rainbow row
Many independently colored status badges → competing salience → small state vocabulary + text/alignment.

### B04 Decorative sparkline everywhere
Every row gets a trend → visual noise and weak exact-value access → trend only where trajectory matters.

### B05 Hidden active filters
Population changes but scope only visible inside closed menu → population can be misread → expose active scope/reset.

### B06 Priority-severity conflation
One traffic-light status mixes urgency, disease severity and workflow state → ambiguous meaning → separate dimensions.

### B07 Ambiguous row action
Icon-only action weakly associated with patient row → wrong-object risk → accessible label + stable scope.

### B08 Metric duplication
Same count in card/donut/table header → visual inflation → one representation near decision.

## C. Patient-chart slop

### C01 Profile hero
Avatar/name/age as consumer-profile hero → consumes space and underplays clinical context → compact banner.

### C02 Domain card wall
Allergies/meds/problems/labs/notes equal cards → current/high-consequence data flattened → task-led hierarchy.

### C03 Historical fade
Old/inactive only lighter gray → weak for low vision and ambiguous → explicit status + placement/type.

### C04 Empty means none
Blank area represents no data, no finding and load failure → dangerous ambiguity → explicit state text.

### C05 Unit on hover
Unit/reference only in tooltip → hidden/inaccessible on touch → unit with value.

### C06 AI summary takeover
Generated summary dominates first viewport → abstraction overshadows source/provenance → secondary, source-linked layer.

### C07 Timeline without event semantics
All dates placed on one pretty timeline → order/result/entry/encounter time confused → define temporal semantics.

### C08 Scroll marathon
Every module fully expanded → high navigation cost → overview, anchors, filters, progressive detail.

## D. Forms/documentation slop

### D01 Placeholder label
Placeholder without persistent label → disappears during entry / accessibility problem → visible programmatic label.

### D02 Unit ambiguity
Numeric field has no nearby unit → interpretation/entry risk → expected unit explicit.

### D03 Default-as-answer
Meaningful option preselected merely for speed → may pass unnoticed → defaults only when justified by product/risk analysis.

### D04 Unknown collapsed into No
Binary control cannot represent unknown/not assessed → absence of knowledge becomes negative fact → model semantic states.

### D05 Validation after submit only
Long form gets generic top error → high correction burden → field-linked errors + summary if useful.

### D06 Destructive clear
Reset looks like save/continue → data-loss risk → de-emphasize and support recovery/confirmation appropriately.

## E. Alert/safety slop

### E01 Red means everything
Allergy, overdue task, validation error and critical result share red banner → no hierarchy, alert fatigue → distinguish interruption levels/states.

### E02 Color-only warning
Red/amber/green alone → inaccessible/ambiguous → text label + visual treatment.

### E03 Banner stack
Many warnings at top → habituation and displaced content → deduplicate/prioritize/contextualize.

### E04 Modal reflex
Every warning blocks → interruption loses meaning → choose inline/callout/confirmation/blocking by consequence.

### E05 Generic warning copy
“Warning: please check” → no reason/action → state problem, scope and required action.

### E06 Icon-alone criticality
Triangle/exclamation carries warning → inconsistent interpretation → concise specific text + accessible cue.

## F. Data-viz slop

### F01 Donut reflex
Any percentage becomes donut → poor exact comparison/space efficiency → number/bar/table based on question.

### F02 Gauge theater
Speedometer for bounded metric without decision value → high ink/low information → value + target/context.

### F03 Gradient area trend
Dramatic filled line chart → may exaggerate magnitude → restrained line/points + axes.

### F04 Hidden axes
Labels removed for minimalism → shape loses scale/time → show necessary context.

### F05 Missing-data interpolation
Continuous line bridges absent measurements → implies observations → gaps/markers/explicit missingness.

### F06 Tooltip-only value
Exact data only on hover → touch/keyboard accessibility and comparison cost → expose key values/access alternative.

### F07 Dual-axis convenience
Unrelated measures combined to fit one chart → misleading apparent correlation → separate or clearly justified views.

## G. Patient-facing slop

### G01 EHR miniaturization
Portal mirrors clinician chart → language/hierarchy mismatch → patient-task-first layers.

### G02 Wellness wallpaper
Pastel gradients/blobs/illustration around medical info → competes with serious content → restrained brand expression.

### G03 Invented health score
Arbitrary 0–100 simplification → false precision → validated product metrics only.

### G04 Celebration misuse
Confetti/streaks for serious adherence/results → trivializes context → restrained feedback matched to task.

### G05 Next action buried
Education before what user must do → action hard to find → next step first, explanation after.

### G06 Jargon dump
Direct EHR vocabulary → comprehension burden → plain language with source detail available.

### G07 False reassurance
“You’re all good!” from incomplete state → overstates interpretation → precise approved wording.

## H. AI-surface slop

### H01 Sparkle-as-trust
Sparkle/gradient is AI affordance → says nothing about capability/limits → descriptive action labels.

### H02 Chat for everything
Structured workflow replaced by open chat → slower, less predictable, harder to validate → structured UI + optional conversation.

### H03 AI result-card island
Generated answer floats apart from source → weak provenance/action integration → attach output to task/source.

### H04 Vague insight
“AI Insight” with generic advice → unclear operation/authority → label summarize/extract/compare/draft/explain.

### H05 Generated/source blur
Model output styled like official chart data → provenance ambiguity → explicit generated label and source links.

### H06 AI always-on dominance
Persistent orb/button on every screen → product becomes AI-centric → assistance at high-value moments only.

## I. Patient-management / operations slop

### I01 Name-only search result
Name/avatar dominates patient search → similar records are hard to distinguish → show task-appropriate disambiguation fields adjacent to identity.

### I02 Hidden selection scope
Bulk selection persists while filters/pages change → action scope becomes unclear → show selected count/scope and define select-all semantics explicitly.

### I03 Bulk-action ambiguity
“Assign” or “Move” appears without target/object summary → wrong-scope action risk → state selected objects, destination/owner and consequence.

### I04 Drag-only transfer
Bed/queue transfer only works by drag-and-drop → inaccessible and error-prone under touch/precision constraints → provide explicit move action and keyboard/touch alternative.

### I05 Operational-clinical status merge
Waiting/assigned/overdue is styled as if it were clinical severity → users infer the wrong meaning → keep workflow priority and clinical state separate.

### I06 No-match/load-failure collapse
Empty search/queue represents both no records and failed retrieval → users trust an incomplete population → explicit no-match, empty, partial and unavailable states.

## J. Accessibility / responsive slop

### J01 Mobile cardification
Every desktop table row becomes a tall mobile card → comparison and scan relationships disappear → prioritize columns, compact rows and accessible detail disclosure.

### J02 Focus erasure
Outline removed to create a cleaner UI → keyboard users lose location → preserve a strong visible focus indicator.

### J03 Icon-only action soup
Dense rows contain multiple ambiguous icon buttons → recognition/accessibility cost and wrong-action risk → visible labels where feasible and object-specific accessible names.

### J04 Hover-essential data
Units, exact values or warnings exist only on hover → touch/keyboard/screen-reader users lose meaning → persist essential content or provide an accessible interaction alternative.

### J05 Canvas-only chart
Chart carries essential information with no structured alternative → non-visual access fails → provide a table/summary or equivalent accessible data view.

### J06 Truncated identity/context
Responsive/zoom behavior ellipsizes patient identifiers or action scope first → wrong-context risk → prioritize identity/scope over decorative/secondary columns.

### J07 Motion-as-urgency
Pulse/blink animation is the main indicator of urgent state → motion sensitivity and semantic ambiguity → explicit status text + static salience; respect reduced motion.
