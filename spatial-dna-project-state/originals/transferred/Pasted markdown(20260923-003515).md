# Forensic Data Reconstruction: Spatial DNA Project Corpus

## 1. Executive Summary of Recoverable Material

The Spatial DNA Project represents a critical architectural shift in candidate modeling, moving away from the decay of linear, chronological resumes toward a deterministic 3D atemporal topology. This forensic reconstruction serves as the essential baseline for future engineering efforts, ensuring that any system re-development is grounded in established "ground truth" rather than subject to architectural drift. By preserving the exact state of the candidate evidence substrate—including verified conflicts and mathematical coordinate derivations—we establish a stable foundation for the MARA traversal and projection engine.

The reliability of this reconstruction is governed by a hierarchy of evidentiary standards. The following table evaluates the "Evidence Tiers" identified within the corpus and their subsequent impact on system reliability:

|   |
| - |

Evidence Tier

|   |
| - |

Criteria & Meaning

|   |
| - |

Impact on Reconstruction Reliability

|   |
| - |

**PROVEN BY ARTIFACT**

|   |
| - |

Physical, inspectable machine code, JSON, JSONL, or workbook files committed or staged.

|   |
| - |

**Highest:** These files provide the immutable source of truth for schemas and data values.

|   |
| - |

**PROVEN BY EXECUTION**

|   |
| - |

Operations that have been run, mathematically verified, and produced reproducible output.

|   |
| - |

**High:** Confirms the logic of the transformation scripts and mathematical formulas is functional.

|   |
| - |

**REPORTED / EXPERIMENTAL**

|   |
| - |

Findings observed during interactive prototyping but not yet chained in CI/CD.

|   |
| - |

**Moderate:** Useful for understanding intent, but requires manual verification during engineering.

|   |
| - |

**CLAIMED BUT NOT VERIFIED**

|   |
| - |

Features or linkages in design specs not yet executed autonomously.

|   |
| - |

**Low:** These represent theoretical capabilities that require new engineering to realize.

|   |
| - |

**SOURCE-REPORTED / ARTIFACT NOT AVAILABLE**

|   |
| - |

Concepts referenced in documentation without an exported raw artifact.

|   |
| - |

**Minimal:** Serves as a conceptual placeholder only; cannot be used for direct reconstruction.

The reconstruction is governed by a set of "Key Invariants" and "Non-Negotiables" that must remain immutable:

- **Atomic Immutability:** The 44 atoms and their designated plane assignments are frozen by contract.
- **Coordinate Boundaries:** Operations must remain within the strictly bounded 3D Cartesian space ([-10..10] \times [-5..5] \times [-10..10]).
- **Zero-Drift Mandate:** Historical conflicts (e.g., timeline disputes) must not be reconciled or "smoothed"; they must remain quarantined.
- **Zero Physics Rule:** The rendering environment must not apply gravity, forces, or spring-mass simulations; placement is strictly deterministic.
- **Join Key Integrity:** The `atom_id` serves as the immutable primary key linking semantic blurbs to spatial coordinates.

The following sections provide a detailed inventory of the artifacts and technical specifications required to maintain this state.

## 2. Source Inventory and Artifact Catalog

The "Master Artifact Provenance Directory" is the primary ledger used to distinguish between data that is physically present and capabilities that are merely described in prose. For the engineering handoff, this distinction is critical: an engineer can build upon an artifact, but they must design from scratch for a "claimed" capability.

### Artifact Record Index

- **SOURCE NAME:** Candidate Evidence Graph (Nodes)
  - **ARTIFACT / DATA IDENTIFIER:** `nodes.jsonl`
  - **TYPE:** JSONL
  - **EVIDENCE STATUS:** PROVEN BY ARTIFACT
  - **DESCRIPTION OF ACTUAL CONTENT:** Contains 44 discrete atomic nodes representing candidate evidence across 6 origin planes (Identity, Work History, Education, Creative, Psychometric, References).
- **SOURCE NAME:** Candidate Evidence Graph (Edges)
  - **ARTIFACT / DATA IDENTIFIER:** `edges.jsonl`
  - **TYPE:** JSONL
  - **EVIDENCE STATUS:** PROVEN BY ARTIFACT
  - **DESCRIPTION OF ACTUAL CONTENT:** Contains 11 relational structural edges (E01–E11) defining connections such as `CORROBORATED_BY`, `EXTENDS`, and `IMPLEMENTS`.
- **SOURCE NAME:** Target Test Frame
  - **ARTIFACT / DATA IDENTIFIER:** `spatial dna training (1).xlsx`
  - **TYPE:** XLSX
  - **EVIDENCE STATUS:** PROVEN BY ARTIFACT
  - **DESCRIPTION OF ACTUAL CONTENT:** A workbook documenting the Michigan labor market. Contains 127 jobs, with an average salary benchmark of $74,030.87 and a top benchmark of $250,000.00. Records 87 unique locations across 5 primary clusters (Hospitality, Operations, Branch Management, Sales/Commission, and Technical).
- **SOURCE NAME:** Target Calibration Payload (JOB-002)
  - **ARTIFACT / DATA IDENTIFIER:** `MARA_JOB_002_PROJECTION_PAYLOAD.json` / `spatial-dna-test-001-result.json`
  - **TYPE:** JSON
  - **EVIDENCE STATUS:** PROVEN BY EXECUTION
  - **DESCRIPTION OF ACTUAL CONTENT:** Deterministic mapping of candidate atoms to the Method Hospitality "Restaurant Assistant General Manager" role, including binding types and radial distances.
- **SOURCE NAME:** Exact 25-Coordinate Sample
  - **ARTIFACT / DATA IDENTIFIER:** `EXACT_SPATIAL_COORDINATES_25.json`
  - **TYPE:** JSON
  - **EVIDENCE STATUS:** PROVEN BY ARTIFACT
  - **DESCRIPTION OF ACTUAL CONTENT:** A verification dataset (Sequences 01–25) containing fixed, unrounded X, Y, Z, R coordinates and polarity designations.
- **SOURCE NAME:** Static Canvas Component
  - **ARTIFACT / DATA IDENTIFIER:** `ThreeSpatialStage.tsx` / `SPATIAL_DNA_STAGE_v1`
  - **TYPE:** TSX (React/Three.js)
  - **EVIDENCE STATUS:** PROVEN BY ARTIFACT
  - **DESCRIPTION OF ACTUAL CONTENT:** Source code for the WebGL rendering stage, implementing the bounding box and "Zero Physics" enforcement rules.
- **SOURCE NAME:** SCOUT Receptor Extraction
  - **ARTIFACT / DATA IDENTIFIER:** SCOUT Runner Contract
  - **TYPE:** Programmatic Design
  - **EVIDENCE STATUS:** CLAIMED BUT NOT VERIFIED
  - **DESCRIPTION OF ACTUAL CONTENT:** Underlying artifact for autonomous end-to-end URL extraction of arbitrary postings is not present in the source material.
- **SOURCE NAME:** Automated Wiring Harness
  - **ARTIFACT / DATA IDENTIFIER:** Autonomous Daemon Script
  - **TYPE:** Script / Automation
  - **EVIDENCE STATUS:** CLAIMED BUT NOT VERIFIED
  - **DESCRIPTION OF ACTUAL CONTENT:** Underlying artifact for chaining Stage 1 (Demand) through Stage 3 (Coordinates) without human coordination is not present in the source material.

### Duplicate Representations

Forensic analysis confirms that the **25-Atom Verification Sample** in Section 6 is a deterministic subset of the data within the **MARA_LAYOUT_PAYLOAD_v1**. The Payload version extends this coordinate data with UI-bound metadata (Header, Pitch, Bullets) and trace IDs for use in document compilation.

## 3. Technical Schemas and Data Contracts

Structural normalization is the primary defense against "spark drift" and hallucination. By enforcing strict data contracts across the causal flow, the system ensures that demand receptors and candidate atoms interact in a predictable, auditable environment.

### Core Schema Definitions

#### SCOUT_TARGET_OBSERVATION_v1

```json
{
  "contract_version": "SCOUT_TARGET_OBSERVATION_v1",
  "observation_id": "string",
  "provenance": {
    "collection_date": "ISO-8601",
    "vendor": "string",
    "source_url": "string",
    "disk_cartridge_hash": "sha256"
  },
  "entity_metadata": {
    "employer": "string",
    "job_title": "string",
    "location": { 
      "city": "string", 
      "state": "string", 
      "postal_code": "string",
      "workplace_type": "ON_SITE | HYBRID | REMOTE" 
    },
    "employment_type": "FULL_TIME | PART_TIME | CONTRACT",
    "compensation": { 
      "raw": "string",
      "currency": "USD",
      "interval": "ANNUAL | HOURLY",
      "min": 0, 
      "max": 0 
    },
    "industry": "string"
  },
  "demand_envelope": {
    "verbatim_clauses": [ { "clause_id": "string", "section": "string", "text": "string" } ],
    "negative_space_constraints": [ "string" ]
  }
}

```

#### JOB-002 Method Hospitality Metadata

```json
{
  "observation_id": "OBS-JOB-002-METHOD-HOSP",
  "employer": "Method Hospitality",
  "job_title": "Restaurant Assistant General Manager",
  "location": "Detroit, MI 48226",
  "compensation": { 
    "min_salary": 70000, 
    "max_salary": 75000, 
    "avg_salary": 72500,
    "pay_type": "Salary",
    "employment_type": "Full-time"
  },
  "schedule": "Monday to Friday (+7)",
  "benefits": ["401(k)", "Health insurance", "Paid time off", "Vision", "Dental", "Life insurance"]
}

```

#### D_01 - D_05 Demand Receptors

```json
{
  "job_id": "JOB-002",
  "receptors": [
    { "receptor_id": "D_01", "category": "Operational & Shift Leadership", "weight": 5 },
    { "receptor_id": "D_02", "category": "Financial & P&L Discipline", "weight": 5 },
    { "receptor_id": "D_03", "category": "Workforce Training & Team Development", "weight": 4 },
    { "receptor_id": "D_04", "category": "Compliance, Health & Safety Standards", "weight": 4 },
    { "receptor_id": "D_05", "category": "Cross-Functional Systems & Guest Retention", "weight": 3 }
  ]
}

```

#### MARA_LAYOUT_PAYLOAD_v1

```json
{
  "contract_version": "MARA_LAYOUT_PAYLOAD_v1",
  "metadata": { "target_job_id": "string", "target_title": "string" },
  "spatial_configuration": {
    "active_lateral_planes": [ { "plane_id": "string", "domain_alignment_score": 0 } ],
    "counts": { "total_atoms_evaluated": 44, "direct_bind_count": 0 }
  },
  "dynamic_layout_elements": {
    "layout_containers": [ { "container_id": "string", "content": "string", "bound_atoms": [] } ]
  }
}

```

#### CANVAS_RENDERING_SPECIFICATION

```json
{
  "contract_type": "CANVAS_RENDERING_SPECIFICATION",
  "version": "1.0.0",
  "static_environment": {
    "viewport": { "fov": 45, "initial_camera_position": {"x": 18.0, "y": 12.0, "z": 18.0} },
    "bounding_box": { "ranges": { "x": [-10.0, 10.0], "y": [-5.0, 5.0], "z": [-10.0, 10.0] } },
    "planes": { "ceiling": {"y": 5.0}, "baseline": {"y": 0.0}, "floor": {"y": -5.0} }
  }
}

```

### Dependency Map: System Causal Execution Chain

The execution flow is a deterministic, 9-step chain. Any failure in an upstream stage invalidates the downstream reconstruction:

1. **Job Inception:** Raw posting ingest from `spatial dna training (1).xlsx`.
2. **Normalization & Extraction:** Generation of `SCOUT_TARGET_OBSERVATION_v1`.
3. **Demand Receptors (D_k):** Partitioning into verbatim machine-addressable receptors.
4. **Candidate Evidence Atoms:** Mapping the 44 immutable atoms from the Knowledge Graph.
5. **Binding Gate:** Evaluation of Atoms against D_k (Direct, Transferable, Non-Bind).
6. **Spatial Projection (X, Y, Z, R):** Computation of Cartesian coordinates and vertical polarity.
7. **Spatial & Layout Payload:** Assembly of the `MARA_LAYOUT_PAYLOAD_v1` JSON.
8. **Dynamic Layout Containers:** Allocation of atoms to UI containers (Header, Pitch, etc.).
9. **Gemini Canvas:** Final rendering in the Three.js 3D stage.

## 4. The Candidate Evidence Substrate: Atoms and Edges

"Atomization" fractures monolithic resumes into discrete evidence units. This decouples capability from linear chronology, allowing evidence from any time period to be projected as spatially relevant if it meets a specific demand receptor.

### The 6 Origin Spatial DNA Planes

|   |
| - |

Plane ID

|   |
| - |

Domain Focus

|   |
| - |

Atom Count

|   |
| - |

Key Branches & Entities

|   |
| - |

**plane_01**

|   |
| - |

Identity

|   |
| - |

3

|   |
| - |

Core Demographics, Residential History (Novi/Wixom), Dual Professional Archetype

|   |
| - |

**plane_02**

|   |
| - |

Work History

|   |
| - |

17

|   |
| - |

Twin Peaks, Bobcat Bonnie’s, Metro Concepts, Panera, Patrice & Associates, Applebee’s, Walled Lake Tavern, Staples, Gatsby’s, Pinnacle, Automotive Finance

|   |
| - |

**plane_03**

|   |
| - |

Education & Tech

|   |
| - |

5

|   |
| - |

Oakland University, Oakland Community College, ServSafe/TIPS, POS Systems, Deterministic Multi-Agent Systems

|   |
| - |

**plane_04**

|   |
| - |

Creative & Projects

|   |
| - |

11

|   |
| - |

MARA, Spatial DNA, DARCH, The Tribunal, POLICY, Political Atlas, Ashante, Serializer, Relax

|   |
| - |

**plane_05**

|   |
| - |

Psychometric

|   |
| - |

4

|   |
| - |

16Personalities (ENTJ-A), DISC (41/23/16/20), Holland Investigative, ChatGPT Cognitive Cartography

|   |
| - |

**plane_06**

|   |
| - |

References

|   |
| - |

4

|   |
| - |

Twin Peaks Corporate, Panera MTC Selection, Operator’s Playbook Corroboration, Direct Reference Gap Ledger

### 11 Relational Graph Edges (`edges.jsonl`)

|   |
| - |

ID

|   |
| - |

Source

|   |
| - |

Target

|   |
| - |

Relation

|   |
| - |

Description

|   |
| - |

E01

|   |
| - |

WH-TWIN-001

|   |
| - |

RF-TWIN-001

|   |
| - |

CORROBORATED_BY

|   |
| - |

AGM role corroborated by corporate entrustment.

|   |
| - |

E02

|   |
| - |

WH-TWIN-003

|   |
| - |

WH-TWIN-004

|   |
| - |

EXTENDS

|   |
| - |

NSO leadership built upon frontline training pipelines.

|   |
| - |

E03

|   |
| - |

WH-BOBC-001

|   |
| - |

WH-BOBC-002

|   |
| - |

PRODUCES_METRIC

|   |
| - |

GM tenure produced 18% food cost variance reduction.

|   |
| - |

E04

|   |
| - |

WH-BOBC-001

|   |
| - |

WH-BOBC-003

|   |
| - |

ENFORCES

|   |
| - |

GM ownership enforced 100% audit readiness.

|   |
| - |

E05

|   |
| - |

WH-BOBC-002

|   |
| - |

PR-BOBC-001

|   |
| - |

FORMALIZED_AS

|   |
| - |

Optimization formalized as P&L Framework.

|   |
| - |

E06

|   |
| - |

TC-DEV-001

|   |
| - |

PR-SDNA-001

|   |
| - |

IMPLEMENTS

|   |
| - |

TypeScript/Three.js competence implements Spatial DNA.

|   |
| - |

E07

|   |
| - |

TC-DEV-001

|   |
| - |

PR-DRCH-001

|   |
| - |

IMPLEMENTS

|   |
| - |

Deterministic systems competence implements DARCH.

|   |
| - |

E08

|   |
| - |

ID-003

|   |
| - |

WH-TWIN-001

|   |
| - |

EXEMPLIFIED_BY

|   |
| - |

Leadership archetype exemplified by Twin Peaks AGM.

|   |
| - |

E09

|   |
| - |

ID-003

|   |
| - |

PR-PLCY-001

|   |
| - |

EXEMPLIFIED_BY

|   |
| - |

Systems archetype exemplified by POLICY engine.

|   |
| - |

E10

|   |
| - |

TC-CERT-001

|   |
| - |

WH-BOBC-003

|   |
| - |

ENABLES

|   |
| - |

ServSafe/TIPS enable zero-violation audits.

|   |
| - |

E11

|   |
| - |

RF-PAN-001

|   |
| - |

WH-TWIN-004

|   |
| - |

PRECURSOR_TO

|   |
| - |

Panera trainer role was precursor to Twin Peaks training.

### Machine Payload Gaps

The following attributes are calculated during traversal but are omitted from exported payloads:

1. **Angular Azimuth (\theta):** Omitted; consumers must back-calculate via \arctan(X/Z).
2. **Receptor Multi-Binding Vectors:** Exported as single strings rather than required arrays.
3. **Relational Edge Illumination Weights:** Coordinates exported without dynamic inter-plane weights.
4. **Negative Space Suppression Signature:** Atoms marked `NON_BIND` lack the specific constraint ID triggered.

## 5. The Forensic Ledger of Historical Conflicts

The "Zero-Drift Mandate" preserves semantic contradictions as a strategic choice. Discrepancies are not "smoothed"; they are isolated to ensure the system remains auditable by human or machine agents.

### Preserved Historical Conflict Registers

|   |
| - |

CONFLICT ID

|   |
| - |

ATOM ID

|   |
| - |

TYPE & DOMAIN

|   |
| - |

NARRATIVE DISCREPANCY & QUARANTINE COORDINATES

|   |
| - |

**CONF-01**

|   |
| - |

WH-BOBC-001

|   |
| - |

Timeline Dispute (Work History)

|   |
| - |

Bobcat Bonnie’s GM tenure end-date conflicts (2023 vs 2024). **Quarantine:** Floor Zone (Y = -2.80).

|   |
| - |

**CONF-02**

|   |
| - |

WH-APPL-001

|   |
| - |

Title Discrepancy (Work History)

|   |
| - |

Applebee's title recorded as Senior Assistant Manager (Payroll) vs General Manager (Summary). **Quarantine:** Restricted to verified payroll role; Floor Zone (Y = -2.80).

|   |
| - |

**CONF-03**

|   |
| - |

WH-MTR-001

|   |
| - |

Onset Overlap (Work History)

|   |
| - |

Metro Concepts operational management onset dates overlap across 2023 and 2024. **Quarantine:** Flagged as CONFLICTED in ledger.

|   |
| - |

**CONF-04**

|   |
| - |

WH-WLT-001

|   |
| - |

Separation Documentation (Work History)

|   |
| - |

Walled Lake Tavern documentation includes formal wage reconciliation notice (Oct 13, 2025). **Quarantine:** Floor Zone (Y ≤ -2.0).

|   |
| - |

**CONF-05**

|   |
| - |

ED-OU-001

|   |
| - |

Credential Status (Education)

|   |
| - |

OCC coursework completed vs OU technology degree in progress. **Quarantine:** Degree claims blocked; verified coursework in Floor.

**Rendering Constraint:** These five records must remain in the "Floor Zone" (Y ≤ -2.0) to distinguish them visually from verified evidence.

## 6. Spatial Coordinate Engine and Calibration Samples

The spatial coordinate engine transforms semantic evidence into a deterministic 3D space. Positions relative to the origin (0,0,0)—the Target Demand Centroid—determine an atom's relevance to the job.

### Exact 25-Atom Verification Sample

|   |
| - |

Sequence

|   |
| - |

Atom ID

|   |
| - |

X

|   |
| - |

Y

|   |
| - |

Z

|   |
| - |

R

|   |
| - |

Plane

|   |
| - |

Polarity

|   |
| - |

1

|   |
| - |

ID-001

|   |
| - |

9.69

|   |
| - |

-0.8

|   |
| - |

2.24

|   |
| - |

9.95

|   |
| - |

plane_01

|   |
| - |

BASELINE

|   |
| - |

2

|   |
| - |

ID-002

|   |
| - |

9.9

|   |
| - |

-0.8

|   |
| - |

-1.04

|   |
| - |

9.95

|   |
| - |

plane_01

|   |
| - |

BASELINE

|   |
| - |

3

|   |
| - |

ID-003

|   |
| - |

4.35

|   |
| - |

4.1

|   |
| - |

-0.08

|   |
| - |

4.35

|   |
| - |

plane_01

|   |
| - |

CEILING

|   |
| - |

4

|   |
| - |

WH-TWIN-003

|   |
| - |

0.83

|   |
| - |

4.1

|   |
| - |

4.27

|   |
| - |

4.35

|   |
| - |

plane_02

|   |
| - |

CEILING

|   |
| - |

5

|   |
| - |

WH-TWIN-004

|   |
| - |

-0.75

|   |
| - |

0.84

|   |
| - |

7.11

|   |
| - |

7.15

|   |
| - |

plane_02

|   |
| - |

BASELINE

|   |
| - |

6

|   |
| - |

WH-BOBC-001

|   |
| - |

-1.12

|   |
| - |

-2.8

|   |
| - |

7.06

|   |
| - |

7.15

|   |
| - |

plane_02

|   |
| - |

FLOOR

|   |
| - |

7

|   |
| - |

WH-BOBC-002

|   |
| - |

0.0

|   |
| - |

0.84

|   |
| - |

7.15

|   |
| - |

7.15

|   |
| - |

plane_02

|   |
| - |

BASELINE

|   |
| - |

8

|   |
| - |

WH-PAT-001

|   |
| - |

0.3

|   |
| - |

-2.8

|   |
| - |

5.74

|   |
| - |

5.75

|   |
| - |

plane_02

|   |
| - |

FLOOR

|   |
| - |

9

|   |
| - |

WH-APPL-001

|   |
| - |

-1.0

|   |
| - |

-2.8

|   |
| - |

7.08

|   |
| - |

7.15

|   |
| - |

plane_02

|   |
| - |

FLOOR

|   |
| - |

10

|   |
| - |

WH-WLT-001

|   |
| - |

0.25

|   |
| - |

-2.8

|   |
| - |

7.15

|   |
| - |

7.15

|   |
| - |

plane_02

|   |
| - |

FLOOR

|   |
| - |

11

|   |
| - |

WH-STAP-001

|   |
| - |

0.98

|   |
| - |

4.1

|   |
| - |

4.24

|   |
| - |

4.35

|   |
| - |

plane_02

|   |
| - |

CEILING

|   |
| - |

12

|   |
| - |

WH-GATS-001

|   |
| - |

-0.76

|   |
| - |

4.1

|   |
| - |

4.28

|   |
| - |

4.35

|   |
| - |

plane_02

|   |
| - |

CEILING

|   |
| - |

13

|   |
| - |

WH-FIN-001

|   |
| - |

0.37

|   |
| - |

-2.8

|   |
| - |

7.14

|   |
| - |

7.15

|   |
| - |

plane_02

|   |
| - |

FLOOR

|   |
| - |

14

|   |
| - |

ED-OU-001

|   |
| - |

0.0

|   |
| - |

-2.8

|   |
| - |

0.0

|   |
| - |

9.95

|   |
| - |

plane_03

|   |
| - |

FLOOR

|   |
| - |

15

|   |
| - |

TC-CERT-001

|   |
| - |

0.0

|   |
| - |

1.0

|   |
| - |

0.0

|   |
| - |

5.75

|   |
| - |

plane_03

|   |
| - |

BASELINE

|   |
| - |

16

|   |
| - |

TC-DEV-001

|   |
| - |

0.0

|   |
| - |

4.1

|   |
| - |

0.0

|   |
| - |

4.35

|   |
| - |

plane_03

|   |
| - |

CEILING

|   |
| - |

17

|   |
| - |

PR-PLCY-001

|   |
| - |

0.0

|   |
| - |

-0.8

|   |
| - |

0.0

|   |
| - |

9.95

|   |
| - |

plane_04

|   |
| - |

BASELINE

|   |
| - |

18

|   |
| - |

PR-DRCH-001

|   |
| - |

0.0

|   |
| - |

-0.8

|   |
| - |

0.0

|   |
| - |

9.95

|   |
| - |

plane_04

|   |
| - |

BASELINE

|   |
| - |

19

|   |
| - |

PR-SERL-001

|   |
| - |

0.0

|   |
| - |

-0.8

|   |
| - |

0.0

|   |
| - |

9.95

|   |
| - |

plane_04

|   |
| - |

BASELINE

|   |
| - |

20

|   |
| - |

PR-BOBC-001

|   |
| - |

0.0

|   |
| - |

4.1

|   |
| - |

0.0

|   |
| - |

4.35

|   |
| - |

plane_04

|   |
| - |

CEILING

|   |
| - |

21

|   |
| - |

PS-MBTI-001

|   |
| - |

-5.71

|   |
| - |

1.0

|   |
| - |

-0.7

|   |
| - |

5.75

|   |
| - |

plane_05

|   |
| - |

BASELINE

|   |
| - |

22

|   |
| - |

RF-TWIN-001

|   |
| - |

-0.4

|   |
| - |

1.0

|   |
| - |

-5.74

|   |
| - |

5.75

|   |
| - |

plane_06

|   |
| - |

BASELINE

|   |
| - |

23

|   |
| - |

RF-PAN-001

|   |
| - |

-0.6

|   |
| - |

1.0

|   |
| - |

-5.72

|   |
| - |

5.75

|   |
| - |

plane_06

|   |
| - |

BASELINE

|   |
| - |

24

|   |
| - |

RF-PLAY-001

|   |
| - |

0.68

|   |
| - |

4.1

|   |
| - |

-4.3

|   |
| - |

4.35

|   |
| - |

plane_06

|   |
| - |

CEILING

|   |
| - |

25

|   |
| - |

RF-UNPOP-001

|   |
| - |

-1.9

|   |
| - |

-2.8

|   |
| - |

-9.77

|   |
| - |

9.95

|   |
| - |

plane_06

|   |
| - |

FLOOR

### Logic and Calibration Formulas

- **Radial Distance (R):** R = 11.0 - (\text{match\\\_strength} \times 7.0), bounded [3.0, 10.0].
- **Cardinal Azimuth Anchors:**
  - **North (+Z, 0°):** plane_02 (Work History)
  - **East (+X, 90°):** plane_01 (Identity)
  - **South (-Z, 180°):** plane_06 (References)
  - **West (-X, 270°):** plane_05 (Psychometric)
- **Vertical Polarity (Y):** Ceiling (Y \ge +2.0), Baseline (Between -2.0 and +2.0), Floor (Y \le -2.0).
- **Zero Physics Rule:** No layout solvers or gravity.
- **Binding Ray Rule:** `DIRECT_BIND` = solid ray to origin; `TRANSFERABLE_BIND` = dashed ray; `NON_BIND` = no ray.

## 7. Evidence Status and Engineering Gap Analysis

This forensic postmortem reveals a system that is data-rich but functionally fragmented. While the schemas and coordinate math are proven, the automation connecting these stages remains a design assertion rather than a demonstrated capability.

### Demonstrated Artifacts vs. Asserted Capabilities

|   |
| - |

Item

|   |
| - |

Forensic Status

|   |
| - |

**44-Node Atom Extraction**

|   |
| - |

PROVEN BY ARTIFACT (`nodes.jsonl`)

|   |
| - |

**11-Edge Relational Graph**

|   |
| - |

PROVEN BY ARTIFACT (`edges.jsonl`)

|   |
| - |

**Spatial Coordinate Logic**

|   |
| - |

PROVEN BY EXECUTION (Verified via Stage 3 Sample)

|   |
| - |

**Three.js Visual Stage**

|   |
| - |

PROVEN BY ARTIFACT (`ThreeSpatialStage.tsx`)

|   |
| - |

**Automated Wiring Harness**

|   |
| - |

NOT VERIFIED - PROMPT COORDINATION REQUIRED

|   |
| - |

**SCOUT Autonomous Extraction**

|   |
| - |

NOT VERIFIED - CLAIMED DESIGN ONLY

|   |
| - |

**Standalone Gemini Canvas**

|   |
| - |

NOT VERIFIED - EXPERIMENTAL ONLY

### Final State Summary

A future engineer possesses the necessary ground-truth data to render the Spatial DNA for Candidate JOB-002 using the verified coordinate sample and Three.js stage. However, the system is not yet "autonomous." You can verify coordinates and render static payloads, but you cannot execute a direct URL-to-3D-Projection pipeline without human intervention. Future development must focus on bridging the "Machine Payload Gaps" and the "Automated Wiring Harness" while strictly adhering to the frozen 44-atom substrate.