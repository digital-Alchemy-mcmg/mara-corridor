# Codex Handoff — Spatial DNA B→B5 Entry Engine

## Objective

Take this package as the corrected structural baseline for the MARA pipeline from the Scout handoff through the B4 truth gate. Keep runtime code generic, remove target/candidate mock content, and stop execution at the B5 entry boundary.

## What was corrected from the supplied prototype

1. **Removed target hard-coding.** Runtime code contains no Andrea's Chop House organization/title/location/routing constants.
2. **Removed candidate mock vault.** No Christopher Flournoy, Bobcat Bonnie's, Twin Peaks, Panera, Patrice, Metro Concepts, or other candidate-specific runtime atoms remain.
3. **Removed static B4 answer map.** `CALIBRATION_SPEC` is not runtime authority. B4 now consumes a `TruthAuditor` adapter and validates its output against structural invariants.
4. **Removed B5 placeholder synthesis.** No static operating spines, contradiction strings, prohibited-claim lists, or coverage heuristics remain.
5. **Removed Boundary C.** No payload compiler, no `MARA_LAYOUT_PAYLOAD_v1`, and no post-B5 scoring exists in this package.
6. **Added B handoff boundary.** It validates Scout packet shape only.
7. **Separated B3 considered vs selected evidence.** Eligible-plane contents are no longer automatically treated as bound evidence.
8. **Made B3 target-node driven.** Plane routing, evidence selection, and proposition construction are explicit injected interfaces.
9. **Made B4 proposition-specific.** Only B3-selected atoms may be bound or excluded by B4.
10. **Enforced hard-gate semantics.** A mandatory target gate cannot be marked satisfied through a restricted-scope qualification.
11. **Added B5 entry ledger validation.** Every B2 node must have exactly one reconciled B4 record before exit.
12. **Removed the malformed inline runtime harness.** There is no `__main__` block containing duplicated/broken string literals.

## Current package boundary

`A1–A5 Scout (external) → B → B1 → B2 → B3 → B4 → B5 ENTRY STOP`

Do not implement Boundary C in this task.

## Required semantic adapters

The core engine deliberately does not pretend deterministic Python can perform semantic reasoning by itself. Implementations must be provided for:

- `TargetDecomposer`
- `PlaneRouter`
- `EvidenceSelector`
- `PropositionBuilder`
- `TruthAuditor`

They may be LLM-backed, model-service-backed, or deterministic where appropriate, but they must obey `ARCHITECTURE_LOCK.md`.

## Critical invariants Codex must preserve

- B and B1/B2 are candidate-blind.
- B2 addresses use lowercase letters/numbers only.
- B3 plane choice originates from the target node, not global candidate scoring.
- B3 is permissive discovery; B4 is strict truth adjudication.
- Candidate title or occupational convention may help discovery but cannot be proof in B4.
- Unknown remains unknown.
- B4 cannot reference evidence that B3 did not select.
- Hard gates cannot be qualified into satisfaction.
- Runtime contains no target-specific calibration answers.
- B5 is not implemented in this package; output status is `READY_FOR_B5_SEMANTIC_CORE`.

## Tests already passing

- execution terminates at B5 entry with B4 states preserved;
- B3 does not convert an entire eligible plane into bound evidence;
- B4 rejects an attempt to satisfy a hard gate by restricted-scope qualification.

## Codex next task

Inspect the package, preserve the architecture lock, and implement/plug in the real semantic adapters against the actual Scout packet and Candidate Spatial DNA interfaces. Add regression tests before changing stage contracts. Do not reintroduce Andrea/candidate calibration data into runtime code.
