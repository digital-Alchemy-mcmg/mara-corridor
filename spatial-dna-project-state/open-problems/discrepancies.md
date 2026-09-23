# Open questions and conflicts, preserved without correction

| Topic | Evidence and actual state | Dependency before implementation |
|---|---|---|
| Graph existence | Reports describe 44 populated nodes and 11 edges. `DNA` branch-tip `nodes.jsonl` and `edges.jsonl` are zero bytes. | Obtain actual populated graph or authoritative reconstruction with source provenance. |
| Renderer and code | Reports name `ThreeSpatialStage.tsx`, a Binding Gate, projection, and payload producers. These named code files are absent from the inspected `main`, `DNA`, and `ENGine` trees. | Locate/source executable implementation; do not replace descriptions with invented code. |
| Notebook and ZIP | Reports refer to an SPDNA Notebook collection and uploaded project ZIP. Neither was transferred as a separate source file into this workspace. | Provide exact files if they are to be preserved or implemented. |
| Radius | One description states `R = sqrt(X² + Z²)` and another `R = 11 - 7 × match strength`; some entries at X=Z=0 report a nonzero R. | Resolve which fields are derived versus display metadata and supply the executable projection contract. |
| Precision and angle | A sample called exact/unrounded contains two-decimal values. `arctan(X/Z)` alone does not specify zero and quadrant handling. | Obtain original precision and angular rule; preserve current sample verbatim. |
| Bounds | Most sources give X,Z in [-10,10], Y in [-5,5]; the UI blueprint depicts X [-10.5,10.5]. | Specify which bound governs validation. |
| Plane placement | Six evidence planes are described, with four lateral and two center-axis roles in one sample. | Obtain plane selection and center-axis placement rules. |
| JOB-002 identity | Textual sources describe a Detroit Method Hospitality AGM role; the UI slides show differing example job/location text. | Identify canonical fixture row and mark slide placeholder status. |
| SCOUT scope | Wiring analysis requests autonomous SCOUT wiring; test UI and standby instructions restrict that upper layer. | Future execution directive must determine scope. This preservation pass implements none of it. |
| Payload completeness | Reports flag missing angular azimuth, multiple receptor bindings, edge illumination weights, and the rule behind negative-space suppression. | Obtain source contract and producer output; do not fill by inference. |
| Run receipts | Reports label parts “proven by artifact” or “proven by execution,” without corresponding complete source and replay receipts in the inspected repository. | Independently reproduce against available original code and inputs when supplied. |
| Training workbook variants | Supplied `spatial dna training.xlsx` and committed `spatial dna training (1).xlsx` have different binary sizes and hashes. | Compare content and select version for implementation explicitly; preserve both here. |
| ENGine fragment | `ENGine` holds one 8,000-byte base64 fragment, not an established complete archive. | Locate all parts and validate archive before treating as engine. |

Source values and descriptions are not silently changed in this package. These are open questions, not repaired contracts.
