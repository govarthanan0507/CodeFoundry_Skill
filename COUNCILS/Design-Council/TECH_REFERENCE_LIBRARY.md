# Backend / Infrastructure Reference Library — V1

## Purpose

Same reasoning as `REFERENCE_LIBRARY.md`, one layer down the stack:
the Data/Database Architect and the System/Backend Architect need a
pre-loaded set of real options with real costs to recommend from, so a
technology choice is never just a conclusion — it's a short list of
what was actually considered, what each costs, and why one was picked
over the others. This is not a new rule — `COUNCIL.md`'s design output
already requires "tradeoffs and rejected alternatives" for every
architecture decision — this file is what makes that requirement
answerable with real numbers instead of an invented-on-the-spot
comparison each time.

## The required output shape for ANY technology recommendation

Applies to every Design Council role recommending a tool, service, or
platform — database, hosting, or otherwise — not just the two
categories catalogued below:

```text
OPTIONS CONSIDERED: <the real, named alternatives — not a strawman
   list where only the recommended one looks reasonable>
COST (per option): <actual pricing model — free tier limits, what
   triggers a paid tier, and the paid cost — checked against
   HARD_CONSTRAINTS.md category 1 (money/budget: zero-cost default
   unless explicitly approved)>
ADVANTAGE / TRADEOFF (per option): <what it's genuinely good at,
   what it costs you in return — vendor lock-in per HARD_CONSTRAINTS
   category 6 included here, not treated as separate from cost>
RECOMMENDATION: <the pick>
WHY: <specifically why this project's actual constraints (scale,
   budget, data shape, team size) favor this one — never "it's the
   most popular" alone>
```

A recommendation with no `OPTIONS CONSIDERED` or no `WHY` is treated
the same as a Design Council decision missing its rejected
alternatives — incomplete, not just terse.

## Database options (Data/Database Architect)

```text
POSTGRESQL
  Cost: free/open-source self-hosted; managed cloud tiers from most
        major providers, small pricing differences that accumulate
        at real scale.
  Advantage: became the most widely used database among professional
        developers as of 2025 — handles relational data, JSON
        documents, full-text search, geospatial and time-series in
        one engine. The safe general default.
  Tradeoff: more setup/operational surface than SQLite; managed
        hosting cost if not self-hosting.
  Fits: financial data, inventory, anything where relationships and
        consistency matter — the default recommendation absent a
        specific reason to pick something else.

SQLITE
  Cost: free, public domain, zero infrastructure.
  Advantage: extraordinary read performance from a single file
        (100,000+ queries/sec reported for read-heavy loads); zero
        configuration.
  Tradeoff: not built for high-concurrency multi-writer workloads or
        a networked multi-server deployment.
  Fits: a personal/hobby project, a local-first tool, low-write
        single-instance apps — matches this project's own
        Base_Memory_OS case study's actual choice.

SUPABASE
  Cost: free tier — 500MB database storage, 1GB file storage, 5GB
        egress, 50,000 monthly active users for auth, 500,000 edge
        function invocations, up to 2 active projects. Free projects
        pause after a week of inactivity; no backups, no SLA on free.
  Advantage: bundles Postgres (real Postgres, not a proprietary
        variant) with auth, file storage, and realtime in one
        platform — meaningfully reduces separate-service setup for a
        small project compared to wiring Postgres + auth + storage
        together by hand.
  Tradeoff: the free tier's pause-after-inactivity and no-backups
        terms matter the moment a project has any real users, not
        just during a hobby/prototype phase — this is exactly the
        kind of finding that should resurface at a Pre-Planning
        intent-change re-entry, same as a license finding.
  Fits: a small-to-medium project wanting Postgres plus auth/storage
        without assembling them separately, especially early-stage or
        prototype work.

MONGODB
  Cost: Atlas free tier at 512MB shared resources; dedicated clusters
        from roughly $57/month up.
  Advantage: dominant for unstructured/semi-structured, document-
        shaped data.
  Tradeoff: weaker for workloads that are genuinely relational —
        picking it for relational data because it's popular is a
        named anti-pattern, not a neutral choice.
  Fits: content with a genuinely variable/nested shape (a CMS, event
        logs) — not the default; a deliberate pick for document-shaped
        data specifically.
```

Default recommendation absent a stated reason otherwise: PostgreSQL
for anything with real relationships and multi-writer needs; SQLite
for a genuinely single-instance/personal-scale project; Supabase when
Postgres plus bundled auth/storage saves real setup for a small/early
project (with the free-tier limits above named, not assumed away);
MongoDB only when the data is actually document-shaped, stated
explicitly as the reason, not picked by default.

## Hosting / deployment platform (System/Backend Architect)

```text
VERCEL
  Cost: Hobby plan free — 100GB bandwidth, 1M serverless invocations
        — but the free tier explicitly bans commercial use.
  Advantage: best-in-class for Next.js and frontend-first projects.
  Tradeoff: commercial-use ban on the free tier is a Hard Constraint
        trigger (category 1) the moment a hobby project's intent
        changes to commercial — ties directly into this system's
        intent-change re-entry rule.
  Fits: frontend-heavy apps, personal/non-commercial projects.

NETLIFY
  Cost: credit-based free tier (300 credits/month), 100GB bandwidth,
        300 build minutes.
  Advantage: best for Jamstack/static sites.
  Tradeoff: credit model means usage growth converts to cost sooner
        than a flat free tier would.
  Fits: static sites, frontend-first, similar niche to Vercel.

RENDER
  Cost: free web service tier (512MB RAM), free PostgreSQL included,
        custom domains supported free.
  Advantage: "deploy the app and the database" in one place — good
        default when both a backend service and a database are
        needed together.
  Tradeoff: free tier resource ceiling (512MB) is real — a genuinely
        resource-heavy backend outgrows it quickly.
  Fits: small full-stack projects wanting one platform for app +
        database, at zero cost initially.

RAILWAY
  Cost: trial/usage-based credit, not an unlimited always-free tier
        (a real shift from its earlier reputation) — a typical
        moderate-traffic app runs roughly $8-15/month.
  Advantage: cheaper than Render at real (non-trivial) traffic once
        past the free trial.
  Tradeoff: not free long-term — budget this as a real recurring cost
        against HARD_CONSTRAINTS category 1, not assumed free.
  Fits: once a project has outgrown Render's free ceiling but doesn't
        yet need full cloud-provider (AWS/GCP/Azure) complexity.
```

Default recommendation absent a stated reason otherwise: Render for a
small full-stack project needing both app and database at zero cost;
Vercel/Netlify for a frontend-only or static project; Railway only
once real traffic has outgrown Render's free ceiling, stated
explicitly as the reason for the added cost.

## Mobile platform / language (System Architect, until a dedicated Mobile Architect role exists — per `SHARED/WORKER_SCOPE_REGISTRY.md`'s existing note)

```text
KOTLIN (Android native)
  Advantage: best Android-specific performance and platform-API access
        — outperforms cross-platform options by roughly 5-10% on
        Android-specific benchmarks; full, immediate access to new
        Android OS features.
  Tradeoff: Android-only — a separate iOS codebase (Swift) is needed
        for that platform.
  Fits: Android-only apps, or a deliberate two-native-codebases
        strategy where per-platform performance/features matter more
        than shared code.

SWIFT (iOS native)
  Advantage: best iOS-specific performance and immediate access to new
        iOS platform features; ~60fps rendering, sub-millisecond frame
        times.
  Tradeoff: iOS-only — a separate Android codebase (Kotlin) is needed.
  Fits: iOS-only apps, or the iOS half of a deliberate two-native-
        codebases strategy.

KOTLIN MULTIPLATFORM (KMP)
  Advantage: shares business logic, networking, and data models across
        iOS/Android/web/desktop while keeping the UI fully native per
        platform (compiles to native code on each) — avoids the
        "cross-platform UI feels off" tradeoff other options carry.
  Tradeoff: still writes native UI per platform (less shared code than
        Flutter/React Native); KMP developers are harder to find,
        though the role commands a lower average cost than React
        Native's.
  Fits: enterprise apps that cannot compromise on native UI feel/
        performance but still want shared business logic — a
        deliberate middle ground, not a default.

FLUTTER
  Advantage: single codebase compiled to native ARM code for both
        platforms; largest cross-platform market share (roughly 46%
        as of 2026); near-native rendering performance.
  Tradeoff: UI is Flutter's own rendering engine, not each platform's
        native widget set — a deliberate tradeoff, not a defect, but
        worth naming when pixel-perfect native platform feel matters.
  Fits: the general default for a single team shipping both platforms
        from one codebase, absent a specific reason (bleeding-edge OS
        feature, AR/VR, maximum native performance) to go native.

REACT NATIVE
  Advantage: single JS/TS codebase for both platforms; large existing
        talent pool if the team already knows React; second-largest
        cross-platform share (roughly 35-38%); its Fabric architecture
        narrows the performance gap with native for standard business
        apps.
  Tradeoff: highest average developer cost of the options listed here;
        bridge-based architecture (pre-Fabric) historically weaker than
        Flutter for animation-heavy UI, though Fabric closes much of
        that gap.
  Fits: a team that already has strong React/JS expertise and wants to
        reuse that skill set directly, or a codebase that benefits from
        sharing logic with an existing React web app.
```

Default recommendation absent a stated reason otherwise: Flutter for a
new cross-platform app with no existing team-skill constraint (largest
share, native-compiled performance); React Native when the team
already has strong React expertise to reuse; native (Kotlin + Swift,
two codebases) only when a stated reason exists (bleeding-edge OS
feature, AR/VR, maximum performance headroom) — not by default; KMP as
a deliberate middle ground when native UI feel is non-negotiable but
duplicate business logic isn't acceptable either.

**Testing/verification depth for mobile is explicitly out of scope
here and in `CAPABILITIES/Mobile-Developer/`'s own build discipline** —
per this project's Development/QA separation
(`DEPARTMENTS/Developer_Organization/CONSTITUTION.md` principle 5,
"self-checks are not QA"), device/OS-fragmentation testing and deep
verification are `QA_Organization`'s job, not something this reference
library or the Mobile Developer capability duplicates.

## Growing this file

Same rule as `REFERENCE_LIBRARY.md`: a real comparison a role had to
research live gets folded back in here afterward, so the next Design
Council pass on the same category doesn't pay for the same research
again. Costs and free-tier terms change — this file should be
re-checked against current pricing at adoption time, not assumed
permanently accurate; a stale figure found during a real recommendation
is itself a reason to update this file, not just work around it once.

## On the "separate trained model" question, restated here

Same answer as `REFERENCE_LIBRARY.md` gives for UI patterns: this
static file solves the actual problem (not re-researching the same
comparisons every time) without new infrastructure. Reconsider only
with evidence this approach is hitting a real wall, not preemptively.
