# Discovery Reference Library — V1

## Purpose

Discovery's fallback sequence (`DISCOVERY_PROTOCOL.md`'s "when the
user doesn't know" rule) needs to show concrete options and propose
industry-standard defaults *inside the conversation*, not by pausing
to search the internet every time a button, calendar, or color
question comes up. This file is that pre-loaded reference — common UI
pattern defaults, cited once, reused every Discovery session. A role
consults this file first; it only reaches for a live search when this
file genuinely doesn't cover the pattern in question.

## How this is used

```text
Discovery needs to show 2-3 concrete options, or propose a default
        ↓
Pattern covered below?
    ├── YES → use it directly, no search, no added tokens
    └── NO  → this file doesn't cover it; a live lookup is warranted
              (and is itself a signal this file should grow — see
              "Growing this file" below)
```

## Buttons — states and defaults

Essential states, each needing a visually distinct treatment (never
color alone — pair with icon, border weight, or underline so a
colorblind user or a low-contrast screen still reads the change):

```text
Default   — resting state
Hover     — pointer over it (desktop only; no hover state on touch)
Active/Pressed — the moment of click; color or depth shift
Focus     — keyboard (Tab) navigation; must have a clearly visible
            focus indicator — required for accessibility, not optional
Disabled  — visibly non-interactive, still readable
Loading   — in-flight action, distinct from disabled
Selected  — toggled on and stays on (filters, segmented controls,
            toggle buttons) — different from Active/Pressed, which is
            momentary
```

Default when the user has no preference: primary action = solid
filled button; secondary/cancel = outline or ghost; destructive
action = the platform's warning color, always with a confirming step
(never a silent instant delete) unless the user's own Discovery input
said otherwise. Contrast ratio at least 4.5:1 (button text vs.
background) — this is an accessibility floor, not a style choice, so
it's never traded away for a "cleaner" look.

## Calendar / date picker

Two different patterns, not one — the default depends on the task:

```text
CALENDAR (full grid, browse-by-month) — better for open-ended
  browsing, seeing available days/patterns at a glance (booking,
  scheduling multiple things).
DATE PICKER (compact input + popup) — better for a single, known
  date entry where the user isn't browsing (birthdate, a deadline).
```

Default when unspecified: a date picker for a single date field, a
full calendar when the task is genuinely about browsing availability.
Required states for the day cell itself: Active/selectable, Inactive
(out of range/disabled), Today (visually distinguished from the
selection — the two must never look identical, a named common
mistake), Range Start, Range End (for a date-range field). Always show
today's date as a reference point, and default the initial view to
today or the most likely relevant date (not January of some arbitrary
year).

## Color

```text
A DEFAULT PALETTE SHAPE, when the user has no preference and Phase 1's
reference-first step (DISCOVERY_PROTOCOL.md) came up empty:
  - 1-3 typefaces: a distinctive display face over a refined body face
  - a toned neutral ground (not stark white/black)
  - 0-2 accent colors sharing chroma and lightness, used consistently
    for the same meaning across the product (one color = one meaning,
    not reused arbitrarily)
  - status colors kept semantically distinct from the accent (a brand
    accent color should not double as an error/success color, or the
    two meanings collide)
```

Accessibility floor, non-negotiable regardless of aesthetic
preference: 4.5:1 contrast for body text (3:1 acceptable only at 24px+
bold), and never the only signal for a state change (see Buttons,
above) — this rule already exists in `artifact-design`-adjacent craft
guidance and is restated here because Discovery is where a color
preference gets captured, so the floor has to be enforced at capture
time, not caught later.

## Navigation / information architecture

Default when unspecified: top nav or a left sidebar for a small number
of top-level sections (roughly 5-7); a tab bar for mobile with 3-5
primary destinations; a hamburger/overflow menu only once options
exceed what fits comfortably, never as the default for a small option
count (hiding navigation behind an extra tap when it didn't need to
be hidden is a named anti-pattern, not a neutral choice).

## Forms

Default state coverage required for every input, per the Frontend
Developer worker's own existing rule
(`DEPARTMENTS/Developer_Organization/CAPABILITIES/Frontend-Developer/CAPABILITY.md`) — this library exists so
Discovery captures intent for these same states up front rather than
Development inventing them later: empty, filled, focus, error
(with the specific message inline, not just a red border), disabled,
success/confirmation.

## Growing this file

A live search that Discovery had to run because this file didn't
cover the pattern is itself a signal — the finding should be folded
back into this file afterward (a new section or an addition to an
existing one), so the same gap doesn't cost a live search a second
time. This file is meant to grow from real Discovery sessions, not be
front-loaded speculatively into covering every conceivable UI pattern
before any real session has needed it — the same "don't build the
50-category map before proving it's needed" discipline already applied
elsewhere in this system (`SHARED/EPIC_SELECTION_CRITERIA.md`'s
reasoning, and `QA_Organization`'s capability-pool history).

## On the "separate trained model just for this" idea

Worth naming directly rather than building past it: a static reference
file (this one) accomplishes the actual goal — not re-searching the
same common patterns every session — at effectively zero cost and zero
new infrastructure. A separate fine-tuned/specialized model adds real
cost (training, hosting, keeping it in sync with this file as it
grows, a second thing that can drift out of date) to solve a problem
this file already solves. Per this project's own recurring lesson
(building impressive infrastructure instead of doing the actual work),
that's not warranted yet — it would only become worth reconsidering
with real evidence that this file's approach is hitting an actual wall
(e.g. token cost from *this file itself* becoming large enough to
matter, not from the searches it's replacing), not as a preemptive
optimization.
