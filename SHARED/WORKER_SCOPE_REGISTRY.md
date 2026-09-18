# CodeFoundry V1 — Worker Scope Registry

## Purpose

Every implementation-stage worker in the system, in one place, with its boundaries defined before it's built — not discovered by accident once two workers overlap on the same file. This is distinct from the Design Council (`COUNCILS/Design-Council/`), which *decides* how things should be built; workers *build and verify* against those decisions.

Status legend: **BUILT** (full SKILL.md/workflow/contracts package exists) · **SCOPED** (boundaries defined here, package not yet written) · **THIN** (only the original V1 agent file exists, not hardened to this standard).

---

## 1. Frontend Developer — BUILT

Package: `AGENTS/Frontend/AGENT.md` + `DEPARTMENTS/Developer_Organization/CAPABILITIES/Frontend-Developer/` (your original upload).

Mission: turn approved UX/UI design into a working, browser-verified frontend.

## 2. Backend Developer — BUILT

Package: `AGENTS/Backend/AGENT.md` + `DEPARTMENTS/Developer_Organization/CAPABILITIES/Backend-Developer/` (built this session).

Mission: turn approved API/data design into a working service with migration safety, backup discipline, and load/security verification.

## 2b. Mobile Developer — BUILT (device-level security — app lock, secure credential storage — is now a hard rule, not a scoped placeholder)

**Mission:** Turn approved design into a working native mobile app — distinct from Frontend Developer because mobile has its own genuine seam: platform APIs, device fragmentation, offline behavior, on-device security, and app-store release requirements that a web frontend doesn't face.

**Owns:**
- native app structure and platform-specific integration (camera, notifications, background playback, etc. as relevant)
- offline behavior and local storage on-device
- device-level security: app lock (passcode/PIN/biometric), secure credential storage using real platform primitives (Keychain/Keystore), session handling on-device
- app-store submission readiness (Play Store's closed-testing requirement, App Store review guidelines)
- device/OS fragmentation testing

**Must not decide:**
- backend API contracts (Backend/API Architect's domain — Mobile Developer consumes them, same relationship Frontend Developer has)
- whether the wrapper-app vs. native-app path is taken at all (that's a Design Council + human decision, informed by cost/time tradeoffs already discussed)
- the product's data sensitivity classification (Product/Security Architect's call — Mobile Developer implements the required protection level, doesn't invent it)

**Inputs:** approved design package, existing API contracts, platform target (iOS/Android/both), the product's actual security requirements.

**Outputs:** working app, device-verified evidence (not just "builds successfully"), verified secure-storage and app-lock evidence, app-store submission package.

**Parallelization note:** if more than one Mobile Developer works the same app simultaneously, `PARALLELIZATION_GUARDRAIL.md` governs the split — the Mobile Architect (or System Architect, if no dedicated Mobile Architect role exists yet) defines the foundation/parallel-split line before multiple builders touch it, exactly as it would for two Backend or two Frontend Developers.

Package: `AGENTS/Mobile/AGENT.md` + `DEPARTMENTS/Developer_Organization/CAPABILITIES/Mobile-Developer/` (built this session).

---

## 3. QA Worker — SCOPED

**Mission:** Independently verify that what Frontend and Backend actually built satisfies the accepted requirements and design — from a fresh context, not the builder's own assumptions.

**Owns:**
- test strategy derivation from requirements + risk level
- end-to-end / integration verification across frontend + backend together (neither builder worker verifies the *seam* between them)
- regression detection across changes
- release-readiness evidence

**Must not decide:**
- what the requirements should have been (Product's domain — QA can flag ambiguity, not resolve it)
- how to fix a defect (reports it; Frontend/Backend Developer fixes it)
- whether a known risk is acceptable to ship with (that's a human gate call, informed by QA's evidence)

**Inputs:** requirements, design package, Frontend/Backend handoffs and their own verification evidence.

**Outputs:** test evidence, defect reports, release-readiness recommendation (not authorization — that's the gate).

**Hard rule carried over from the existing thin agent file:** a passing build is not proof of correctness; a generated test is not proof it's meaningful. This worker's whole value is refusing to accept the builder's own "SUCCEEDED" claim as sufficient — it re-verifies independently.

---

## 4. Security Worker — SCOPED

**Mission:** Implementation-time security verification — distinct from the Security/Reliability Architect (Design Council), who *designs* the threat model and auth boundaries before anything is built. This worker checks whether the actual implementation matches that design and hasn't introduced new exposure.

**Owns:**
- dependency/vulnerability scanning of what was actually implemented
- secrets-in-code/logs detection
- verifying authn/authz was implemented as designed (not redesigning it)
- confirming the Backend Developer's backup/restore evidence actually exists before a release gate, not just claimed

**Must not decide:**
- the threat model or auth architecture itself (Security/Reliability Architect's domain, upstream)
- whether a found risk is acceptable to ship with (human gate, informed by this worker's findings — same relationship as QA)

**Inputs:** the design package's security section, the actual implemented code/config.

**Outputs:** security findings, severity classification, pass/fail against the design's stated security requirements.

**Relationship note:** this worker and QA overlap in spirit (both verify, don't build) — keep them distinct because security findings often need a different response speed and confidentiality (a security finding shouldn't sit in the same open backlog as a UI typo).

---

## 5. DevOps / Release Worker — BUILT (`AGENTS/Deployment-Engineer/AGENT.md`, per an explicit instruction covering dev/test/prod repo promotion and the one-sanctioned-download-point rule)

**Mission:** Take a QA-cleared build and actually release it — the stage the blueprint calls Deployment, kept narrow on purpose. Concretely: push `dev_<project>` and `test_<project>` to their own GitHub repos as-is, and, only once QA_Organization's verdict is clean, assemble and push `prod_<project>` — the one repo meant for distribution, per `SHARED/PROJECT_FOLDER_STRUCTURE.md`'s deployment section.

**Owns:**
- build/release pipeline execution
- environment configuration (staging vs. production)
- deployment execution and rollback capability for the *release* itself (distinct from Backend's database migration rollback — this is "can we revert the deployed version," Backend's is "can we revert the schema")
- post-deploy smoke checks

**Must not decide:**
- whether the build is ready to release (that's the Release Readiness human gate, informed by QA + Security's evidence)
- infrastructure/platform choice at the architecture level (Data/Database Architect and System Architect's domain — this worker executes within that choice)

**Inputs:** a QA-passed, Security-cleared build; the release-readiness gate's approval.

**Outputs:** deployed release, rollback plan, post-deploy verification evidence.

**Hard constraint tie-in:** this worker touches Category 4 (security exposure) and Category 10 (reliability promises to users) from `HARD_CONSTRAINTS.md` directly — any change to what's publicly exposed or what uptime is implied routes to the human, not a silent deploy.

---

## 6. Research Worker — THIN (existing `AGENTS/Research/SKILL.md` covers the basics; scope extended here)

**Mission:** Find evidence for decisions that materially affect the product — market, competitors, technical feasibility, and now explicitly: OSS/reuse discovery via **Repo Analyzer**, a separate external application (still in active development by the human, not built inside CodeFoundry) that produces `REPO_ANALYSIS.md`/`REPO_INDEX.md` plus a confidence ratio per candidate — a callable tool CodeFoundry consumes, not a separate ad hoc process each time. Repo Analyzer has two distinct roles: per-project reuse checking (below) and feeding CodeFoundry's own capability evolution (`SHARED/CAPABILITY_EVOLUTION.md`) — a candidate found for one project can also be evidence for improving a worker's own capability file, not only that project's decision.

**Owns:**
- market/competitor research (Pre-Planning stage)
- technical capability research (any stage, on demand)
- invoking Repo Analyzer for a specific repository, and reading its `REPO_ANALYSIS.md`/`REPO_INDEX.md` output rather than re-deriving it from scratch. **This is mandatory, not optional, for Tier 2/3 tasks** — see `REUSE_AND_LICENSE_RULE.md` Part 1. Tier 1 tasks are exempt by default.
- recording any license finding on a reuse candidate as its own named finding, always — see `REUSE_AND_LICENSE_RULE.md` Part 2 for what happens to that finding next (it does not automatically block a hobby/personal build, but it is never dropped)

**Must not decide:**
- whether a researched option gets adopted (Product/Architect's domain — Research informs, doesn't choose)
- legal clearance from a license finding (states the license and its restrictions; doesn't declare something safe to use)

**Inputs:** a specific research question, not an open-ended "go find stuff."

**Outputs:** evidence classified by strength (verified fact → unverified assumption, per the existing rule), with Repo Analyzer results treated as one evidence source among others.

---

## 7. Orchestrator — HARDENED (`AGENTS/Orchestrator/AGENT.md` now covers retry/re-entry/escalation logic, review-triggering rules, and the full handoff-issuing responsibility)

**Mission:** Routing, gate enforcement, state maintenance. Does not produce product work itself.

**Owns:** current phase determination, next-action identification, loading `HARD_CONSTRAINTS.md` before any Design Council debate, refusing to infer approval from silence, retry vs. re-entry vs. escalation decisions, and triggering independent review per `PROCESS_SCALING.md` tier.

**Must not decide:** any actual product/technical/design decision — if the Orchestrator starts making calls that belong to another role, that's the failure mode this whole registry exists to prevent.

---

## 8. Product Manager + Product Owner — HARDENED (split from the original single "Product" role into `AGENTS/Product-Manager/AGENT.md` and `AGENTS/Product-Owner/AGENT.md`, per industry-standard PM/PO separation — PM owns epic-level strategy, PO owns story/acceptance-criteria detail)

**Product Manager mission:** Receives the Pre-Planning verdict, decomposes the idea into epics using a real splitting discipline (INVEST pre-check, vertical slicing, splitting patterns, estimation-spread signal, spike-when-uncertain), and runs `EPIC_SELECTION_CRITERIA.md`'s selection process for this release.

**Product Manager owns:** epic decomposition, epic selection/MoSCoW labeling, the Pre-Planning verdict record, handing finalized epics to the Product Owner.

**Product Owner mission:** Owns the problem, users, scope, and requirements translation for each epic handed to it — the liaison between the human and every gate at the story-detail level.

**Product Owner owns:** requirements artifacts, scope boundary enforcement (in/out, inherited from Pre-Planning), resolving whether a change request from Development is a requirements gap vs. a design gap vs. an implementation bug (routes it to the right place accordingly), writing user stories and acceptance criteria specific enough that QA can verify them without asking what was meant.

**Neither role decides:** architecture, technology choice, or how anything gets built (Design Council's domain, downstream) — same boundary the original single role had, now split across two roles instead of collapsed into one.

---

## What's genuinely complete vs. still open after this registry

**Complete scope, ready to build in full when needed:** QA, Security, DevOps/Release — all now have clear boundaries even though their full 6-file packages don't exist yet.

**Adequate as-is:** Orchestrator, Research — coordination-heavy, not judgment-heavy in the way Frontend/Backend/Design Council/Product Manager/Product Owner are, so they don't need the same depth of hardening.

**Fully built/hardened:** Frontend Developer, Backend Developer, Mobile Developer, Product Manager (epic decomposition + selection discipline), Product Owner (user story + acceptance criteria discipline), Orchestrator (retry/re-entry/escalation/review-triggering/session continuity/memory model), Git Maintainer (branch/PR/merge mechanics, industry-standard workflow).

## 9. Git Maintainer — BUILT

Package: `AGENTS/Git-Maintainer/AGENT.md`.

Mission: execute real Git/GitHub operations correctly — branching, PRs, merges, tagging — following industry-standard practice (Conventional Commits, no direct pushes to main, squash-merge for features). Mechanical execution, not judgment: doesn't decide what code changes to make or whether a PR is approved, only that the repository correctly reflects decisions already made elsewhere.

Nothing in the V1 lifecycle is unscoped anymore. The next session's actual work is writing the QA, Security, and DevOps full packages when a real project reaches those stages — not before, since building them speculatively now would be exactly the "V1 blueprint is V2-shaped" over-scoping problem flagged at the very start of this project.
