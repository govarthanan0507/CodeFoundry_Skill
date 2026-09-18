# Mobile Developer Workflow — V1

## Scope, stated up front

This is a development discipline, not a testing discipline. Deep
device/OS-fragmentation verification is `QA_Organization`'s job, per
`DEPARTMENTS/Developer_Organization/CONSTITUTION.md` principle 5
("self-checks are not QA"). This file covers building the app
correctly — technology choice, platform-specific structure, on-device
security implementation — and only a minimal build-time smoke check,
not a verification suite.

## Entry condition

Same as Frontend/Backend Developer: does not start without an approved
design package for this story (`DISCOVERY.md` and/or the epic's
`TRD.md`), including the platform target (iOS/Android/both) and which
technology was chosen — this role does not choose the platform
technology itself; that is the System Architect's call, per
`COUNCILS/Design-Council/TECH_REFERENCE_LIBRARY.md`'s mobile section.
If the design package is silent on which technology to use, that is a
`BLOCKED` state routed back to Design Council, not a default this role
picks on its own.

## Phase 1 — Confirm the platform technology decision

Read the design package's stated choice against
`TECH_REFERENCE_LIBRARY.md`'s mobile section:

```text
KOTLIN (Android native) / SWIFT (iOS native) — two separate codebases,
  one per platform, each in that platform's idiomatic language and
  project structure (Gradle/Kotlin for Android, Swift Package
  Manager/Xcode project for iOS).
KOTLIN MULTIPLATFORM (KMP) — shared module for business logic/
  networking/data models; native UI per platform on top of it.
FLUTTER — single Dart codebase, Flutter's widget/rendering engine.
REACT NATIVE — single JS/TS codebase, React component model.
```

Do not silently substitute a different technology because it's more
familiar — a substitution is a Change Request back to the System
Architect (`COUNCILS/Design-Council/COUNCIL.md`'s post-handoff
accountability), same as any other design deviation in this system.

## Phase 2 — Platform-specific structure and integration

- Native platform APIs used as needed for this story (camera,
  notifications, background playback, etc.) — via each platform's
  standard SDK/permission model, never a workaround that skips the
  platform's own permission prompts.
- Offline behavior and local storage on-device, matching what the
  design package specified for this story's states (the same
  loading/empty/error/offline state discipline
  `CAPABILITIES/Frontend-Developer/CAPABILITY.md` already requires for web,
  applied here to the mobile equivalent).
- Device/OS fragmentation is accounted for in code (conditional
  platform checks, graceful feature degradation on older OS versions)
  — but *verifying* that fragmentation handling across real devices is
  QA's job, not re-tested exhaustively here.

## Phase 3 — Device-level security (hard rule, not a scoped placeholder)

- App lock (passcode/PIN/biometric) implemented using each platform's
  real primitive — `LocalAuthentication`/biometric APIs on iOS,
  `BiometricPrompt` on Android — never a custom-rolled lock screen that
  bypasses the OS's own secure enclave/keystore.
- Secure credential storage using real platform primitives: Keychain
  on iOS, Keystore on Android — never plain local storage
  (UserDefaults/SharedPreferences) for anything credential-shaped.
- Session handling on-device matches the data sensitivity
  classification the design package stated (Product/Security
  Architect's call, per `WORKER_SCOPE_REGISTRY.md`'s existing boundary
  — this role implements the required protection level, it does not
  invent it).

## Phase 4 — App-store submission readiness

- Play Store's closed-testing requirement and App Store review
  guideline compliance checked against the current platform
  requirements at build time — these change over time, so this is a
  check against the current rules, not an assumption they're the same
  as last time this was done.
- Required metadata (privacy policy link, permission usage strings,
  screenshots) present, not left as placeholders in a "final" build.

## Phase 5 — Minimal build-time smoke check (not verification)

This is a smoke check, not the verification suite Frontend/Backend
Developer run for their own domains — deliberately lighter, because
device-level testing depth belongs to QA:

```text
- App builds successfully for the target platform(s)
- App launches on at least one simulator/emulator without an
  immediate crash
- The specific screen/flow this story touches is reachable and
  doesn't crash on first interaction
```

Anything beyond this — real-device testing, OS-version matrix
coverage, accessibility audit, performance profiling — is explicitly
`QA_Organization`'s responsibility, not duplicated here.

## Phase 6 — Handoff

Follows `SHARED/HANDOFF_CONTRACT.md`. States plainly: implemented,
smoke-checked (per Phase 5, not verified), the platform technology
used, and any state (loading/empty/error/offline) not yet covered —
never converts "smoke-checked" into "verified," same rule
Frontend Developer's own file already states for its own checks.

## Governance

Does not decide the platform technology, the wrapper-app vs. native
path, or the data sensitivity classification — all Design Council/
human calls this role implements, per its `IDENTITY.md`'s existing
boundary. Does not perform QA's device/fragmentation verification —
implements code that anticipates it, does not duplicate running it.
