# Spatial DNA — B through B5 Entry Architecture Lock

## Authoritative sequence

`Scout A1–A5 → B handoff → B1 Decouple → B2 Create Tree → B3 Bind → B4 The Gate → STOP at B5 entry`

This package intentionally does **not** implement B5 Semantic Core Reasoning and does **not** implement Boundary C.

## B handoff

B validates the Scout packet schema only. It does not decompose the target and does not inspect candidate evidence.

## B1 — Decouple

Candidate-blind target decomposition. B1 must:

- preserve source spans and source authority;
- capture target identification and application routing;
- classify only source-supported semantic force (`*`, `≈`, unmarked);
- preserve qualifiers and missing fields;
- determine malform state from origin/destination;
- remain candidate-blind.

B1 must not infer candidate fit, activate SDNA planes, or manufacture missing target requirements.

## B2 — Create Tree

B2 converts B1 requirements into a deterministic, addressable hierarchy.

- lowercase letters and numbers only in addresses;
- target-derived branch structure, no fixed domain taxonomy;
- exact source-span provenance retained;
- semantic class preserved exactly;
- many-to-many source-span↔target-address mappings permitted;
- tree frozen before B3.

## B3 — Bind

B3 is intentionally permissive discovery.

For each target node:

1. derive a satisfaction question;
2. determine eligible SDNA planes from the target node;
3. search only those planes;
4. distinguish atoms *considered* from atoms *selected*;
5. submit a proposition and binding rationale to B4.

B3 may surface direct, proximate, plausible, and transferable evidence. It may not declare proposition truth merely from title, occupational convention, or necessity.

## B4 — The Gate

B4 audits the exact B3 proposition.

Standard:

- zero title inference as proof;
- zero occupational convention as proof;
- zero necessity argument as proof;
- zero invented credentials;
- no semantic inflation;
- every non-PASS disposition requires a specific reason.

Resolution states:

- `PASS / FULLY SUPPORTED`
- `QUALIFIED / BOUND AT RESTRICTED SCOPE`
- `UNRESOLVED AT ATOMIC LEVEL`
- `CONTRADICTED`

Hard gates may not be converted into satisfaction merely by narrowing them. They must either be specifically established or remain unresolved/contradicted after re-search/correction.

## B5 entry boundary

This package terminates after B4 reconciliation. The B5 entry packet contains:

- frozen target tree;
- audited B4 ledger keyed by target address;
- PASS nodes;
- qualified nodes;
- unresolved nodes;
- contradicted nodes;
- routing/malform state;
- target identification.

No semantic-core synthesis, prism reasoning, advocacy, scoring, or payload compilation is performed here.
