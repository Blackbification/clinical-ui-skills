# Healthcare UI State Model

| Dimension | Example states |
|---|---|
| availability | loading, loaded, partial, unavailable, stale, unknown |
| lifecycle | draft, active, completed, stopped, cancelled, entered in error |
| review | new, unreviewed, reviewed, acknowledged |
| workflow | unassigned, assigned, in progress, waiting, blocked, done |
| priority | routine, important, urgent, critical |
| provenance | source record, product-computed, AI-extracted, AI-generated, human-authored |
| action | idle, proposed, submitting, succeeded, failed, reversible |

Required distinctions when relevant: unknown ≠ negative; not recorded ≠ no; unavailable ≠ empty; loading ≠ none; pending ≠ negative; historical ≠ current; review status ≠ severity; priority ≠ severity; AI-generated ≠ source record; proposed action ≠ executed action.
