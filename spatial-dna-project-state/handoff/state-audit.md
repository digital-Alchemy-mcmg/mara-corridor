# Pre-implementation state audit, 23 September 2026 UTC

## What the supplied sources describe

The reported target is a job demand evaluated against atemporal candidate evidence and rendered as a visible spatial result. The documented path is JOB → DEMAND OBSERVATION → DEMAND RECEPTORS → CANDIDATE EVIDENCE / SPATIAL DNA → TRAVERSAL AND BINDING → SPATIAL PROJECTION → X/Y/Z → SPATIAL PAYLOAD → LAYOUT PAYLOAD → TEST CANVAS. These are documented handoffs. The inspected repository does not contain an executable end-to-end chain.

The sources describe six origin planes (Identity, Work History, Education, Creative Works, Psychometric/Cognitive, References/Testimony), 44 atoms, 11 edges, five historical conflicts, immutable `atom_id` linkage, binding states `DIRECT_BIND`, `TRANSFERABLE_BIND`, and `NON_BIND`, and deterministic coordinates in a bounded space. Some stages are represented only by descriptions and examples. Keep chronology as a lens where the sources specify it and preserve conflicting evidence instead of converting it into uncontested claims.

| Stage | Described role | Present evidence | Status |
|---|---|---|---|
| Job and demand | Preserve posting text, source and constraints; identify weighted receptors | Training workbook, JOB-002 textual examples, reports | Source data and documentation; general extractor unverified |
| Candidate graph and binding | Compare receptors to atoms across planes; traverse edges; quarantine conflict | Textual atom/edge descriptions; branch skeleton with empty graph files | Reported model; executable graph and gate unverified |
| Projection | Place bound atoms with plane, polarity, match and angular rules | Parsed 25-coordinate example | Sample data; derivation and round-trip unverified |
| Spatial and layout payloads | Carry identities, geometry, provenance and traceable layout claims | Parsed `MARA_LAYOUT_PAYLOAD_v1` example and documentation | Example; machine production path unverified |
| Canvas and validation | Observe supplied coordinates and binding rays; expose violations | UI blueprint, slides, wiring analysis | Specification; runnable canvas and tests unverified |

## Repository facts at audit

The default branch was `main` at `a5822a1694d642ba5148832786fc0b12975d40b2`, with one training workbook. `DNA` was `e856cb6e8db440932b2561b4dde6482460c25242`, holding the candidate-spatial-dna-kg skeleton and a structure DOCX. Its graph, schema, demographics and governance placeholders were empty. `ENGine` was `1cbb5ffb3db9c1e82ca787dec21c040579b8b913`, holding `.branch-seed` and `.materialize/part01.b64`. The latter is a fragment, not an established complete engine. This preservation branch is based on `main` and separately snapshots the two other branch tips; it does not merge them or promote their placeholders to implementation.

## Authority and evidence status

Actual bytes and repository trees establish what was supplied or committed. The 14 transferred originals and their extracts establish what their authors reported. The UI blueprint supports a passive inspector role. Reports are evidence of documented intent, not evidence of execution simply because they say “proven.” The parsed coordinates and layout example are source data. All extracted material retains an original source path in `manifests/files.json`.

## Visible integration boundaries

The documents expose job source → observation → receptors; receptors and candidate graph → binding; binding → coordinates; coordinates and trace IDs → spatial payload; spatial payload → layout payload; and payloads → passive canvas/validation. Identity, provenance, quarantine and failure status need to remain visible across these boundaries. This records the interfaces the sources discuss; it is not a new harness design.

## UI observation requirements in sources

The blueprint specifies read-only job and demand views, receptors and weights, atoms/planes/edges, binding and quarantine, X/Y/Z/R telemetry, spatial and layout payloads, trace IDs, provenance and evidence status, and a passive 3D view with explicit validation failures. A test fixture and canvas round-trip are described but have not been run here.

## Preservation boundary

This repository package includes all 14 source files supplied to the workspace, their useful read-access extractions, branch snapshots, and this qualified context. It does not include the unspecified SPDNA Notebook collection or uploaded project ZIP as independently supplied files. It cannot certify that content only described by the reports was ever received. No implementation or execution was performed as part of preservation.
