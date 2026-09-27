B5 SCAFFOLD — CODEX WORKING INSTRUCTIONS

PROJECT
Spatial DNA

ASSIGNMENT
B5 Prism Orchestration + Consolidation Scaffold

OBJECTIVE

Build the structural B5 execution station.

This assignment is NOT to implement Scout, B, B1, B2, B3, B4, Resume Factory, or the unresolved Traveling Envelope handoff.

B5 must be independently runnable against a synthetic sealed B4-cleared package so its internal workflow can be built and tested now.

B5 receives B4-audited evidence and owns projection posture only.

B4 owns truth.
B5 owns projection posture.
Resume Factory owns expression and physical layout.

B5 must never turn projection, inference, psychometric observation, occupational convention, or narrative interpretation into fact.

--------------------------------------------------
1. AUTHORITY
--------------------------------------------------

Primary semantic authority:

B5 — Semantic Core Reasoning Architecture Lock

Execution/workbench authority:

B5 Semantic Core — Engine Build Brief

Do not redesign the five-prism theory.
Do not invent a replacement scoring ontology.
Do not request hidden prism weights or a prewritten formula.

The scaffold must operationalize the existing theory while leaving the semantic reasoning implementation replaceable/testable.

--------------------------------------------------
2. INPUT BOUNDARY
--------------------------------------------------

Create an abstract B4ClearedPackage interface.

This is a temporary execution boundary used so B5 can be developed independently of the unresolved upstream Traveling Envelope contract.

The B4ClearedPackage must be treated as:

SEALED
READ-ONLY
ALREADY AUDITED
SOURCE OF TRUTH FOR B5

B5 must not:

query B4
query B3
query Spatial DNA
query candidate source files
query external sources
repair missing evidence
retrieve additional evidence
reinterpret rejected evidence
change B4 truth status

If package integrity fails, stop that package before semantic reasoning.

Do not silently repair it.

--------------------------------------------------
3. B5 EXECUTION PIPELINE
--------------------------------------------------

Implement this structural sequence:

B4ClearedPackage
    ->
Admission / integrity verification
    ->
Evidence access layer
    ->
Five independent Prism executions
    ->
Prism result validation
    ->
Consolidation
    ->
Normalized five-prism distribution
    ->
Owner prism selection
    ->
Semantic priority derivation
    ->
Writing-boundary derivation
    ->
Presentation-geometry derivation
    ->
B5 payload construction
    ->
Receipt / verification evidence
    ->
STOP

No Resume Factory execution.

--------------------------------------------------
4. FIVE REQUIRED PRISM SKILLS
--------------------------------------------------

All five must execute for every admitted package.

1. SALES HEADHUNTER

Purpose:
Find the strongest immediately legible proof.

Typical evidence shape:
metric
accomplishment
tenure
output
result
undeniable production

This prism asks:
What evidence can carry the candidate immediately because it is concrete and difficult to dispute?

2. SPORTS AGENT

Purpose:
Present established value rather than an applicant auditioning for approval.

Typical evidence shape:
demonstrated performance
chronology
sustained responsibility
proven value
career continuity

This prism asks:
What evidence allows the candidate to be framed as an established asset within what has already been earned?

3. DISCOVERY SCOUT

Purpose:
Surface transferable signal that may not be obvious from conventional role matching.

Typical evidence shape:
projects
unusual accomplishments
adjacent experience
cross-domain capability
non-obvious target relevance

This prism asks:
What valid capability is present that a conventional reading might miss?

4. INDEPENDENT STAFFING-FIRM OWNER

Purpose:
Determine how legibly the candidate already belongs in the target industry or operating environment.

Typical evidence shape:
industry fluency
industry-native concepts
operating familiarity
direct domain evidence
role-adjacent fluency

This prism asks:
How much industry-native positioning has the evidence actually earned?

Never exceed demonstrated fluency.

5. CASTING DIRECTOR

Purpose:
Construct the strongest defensible interpretation of the whole candidate.

Typical evidence shape:
broad corpus pattern
chronology
recurring behavior
unconventional learning
references
bounded contextual evidence
whole-person pattern

This prism asks:
What larger interpretation is defensible when the evidence is viewed together without converting projection into fact?

--------------------------------------------------
5. PRISM ISOLATION RULE
--------------------------------------------------

Each prism executes against the SAME admitted B4-cleared package.

Each prism produces its own result independently.

No prism may use another prism's output as evidence.

Use a fixed invocation order for deterministic orchestration if useful, but that order MUST NOT imply semantic precedence.

Canonical execution order may be:

Sales Headhunter
Sports Agent
Discovery Scout
Independent Staffing-Firm Owner
Casting Director

Only the Consolidator may inspect all five prism outputs together.

--------------------------------------------------
6. PRISM RESULT CONTRACT
--------------------------------------------------

Define one common PrismResult contract.

Each PrismResult must contain enough structure to support consolidation, including:

prism_id
prism_name
candidate_target_interpretation
evidence_anchor_ids
evidence_rationale
projection_signal
limitations
prohibited_overreach
execution_status

Do not permit free-floating claims.

Every meaningful prism finding must trace to one or more B4-cleared evidence anchors.

A prism with weak supporting evidence still remains present.

Do not drop a prism merely because its contribution is small.

--------------------------------------------------
7. CONSOLIDATION
--------------------------------------------------

After all five valid PrismResults exist, execute one Consolidator.

The Consolidator owns comparison between prisms.

Its job is to determine:

rank order of all five prisms
relative projection emphasis
owner prism
supporting prism relationships
foreground priorities
reinforcement priorities
background priorities
suppression priorities
writing assertiveness ceiling
language-intensity guidance
prohibited implications
presentation geometry

All five prisms MUST remain represented.

Projection emphasis MUST normalize to exactly 100%.

The percentages mean:

relative projection emphasis

They DO NOT mean:

truth score
confidence score
candidate fit score
success probability
qualification percentage
evidence reliability

The highest-ranked prism becomes the OWNER PRISM.

Do not create a hidden universal weighting formula merely for convenience.

The distribution must respond to the geometry of the B4-cleared evidence for that specific candidate-target relationship.

--------------------------------------------------
8. EVIDENCE GEOMETRY
--------------------------------------------------

The Consolidator must be capable of recognizing at least these structural outcomes:

SINGLE DOMINANT

One prism materially dominates.

Output meaning:
one major semantic presentation center
other prisms subordinate

DUAL DOMINANT

Two prisms jointly dominate.

Output meaning:
two meaningful presentation centers
do not artificially subordinate one

DOMINANT PLUS SECONDARY

One clear owner exists with one substantial secondary posture.

Output meaning:
preserve hierarchy
give secondary posture meaningful weight

DISTRIBUTED

Several prisms are close.

Output meaning:
do not manufacture a false dramatic center
preserve several comparable dimensions

Important:

Prism percentages are semantic priority.

They are NOT literal page-area percentages.

B5 describes presentation geometry.
Resume Factory later converts that geometry into physical layout.

--------------------------------------------------
9. REQUIRED B5 OUTPUT
--------------------------------------------------

Define a B5Payload contract containing at minimum:

ranked_prisms

For each prism:
    prism_id
    rank
    projection_emphasis_percentage
    evidence_anchor_ids
    rationale
    limitations

owner_prism

semantic_priorities:
    foreground
    reinforcement
    background
    suppression

writing_boundaries:
    permitted_assertiveness
    language_intensity_guidance
    prohibited_implications
    evidence_ceilings

presentation_geometry:
    geometry_type
    dominant_centers
    supporting_relationships
    geometry_rationale

traceability:
    B4 package identity
    B4 evidence anchors consumed
    prism execution identifiers
    consolidation execution identifier

Do not put resume sentences in B5Payload.

Do not put template names in B5Payload.

Do not put typography, coordinates, columns, boxes, or visual styling instructions in B5Payload.

--------------------------------------------------
10. PAYLOAD OWNERSHIP
--------------------------------------------------

For eventual Traveling Envelope integration:

B5 may WRITE ONLY payload.b5.

B5 may READ the B4-cleared input permitted to it.

B5 must not modify:

persistent identity
target source
Scout payload
B payload
B1 payload
B2 payload
B3 payload
B4 payload

For this scaffold, isolate B5 behind an adapter so the real Traveling Envelope can be connected later without rewriting B5 internals.

Expected pattern:

TravelingEnvelopeB4Adapter
        ->
B4ClearedPackage
        ->
B5Engine
        ->
B5Payload
        ->
TravelingEnvelopeB5Appender

The adapter/appender may be interfaces or stubs until the shared envelope contract is resolved.

--------------------------------------------------
11. BATCH BEHAVIOR
--------------------------------------------------

Do not build B5 only as a one-record demo.

Support a batch of at least 10 sealed B4ClearedPackages.

15-package support is preferred.

Every package is an independent B5 execution.

No candidate/package may contaminate another candidate/package.

Each package receives:

its own five prism executions
its own consolidation
its own B5 payload
its own receipt/status

A failure in one package must not corrupt successful packages in the same batch.

--------------------------------------------------
12. SYNTHETIC FIXTURES
--------------------------------------------------

Because B4 is not yet integrated, create synthetic B4-cleared fixtures strictly for B5 testing.

Fixtures must represent DIFFERENT evidence geometries.

At minimum create:

Fixture A — strong measurable production
Expected structural pressure toward Sales Headhunter

Fixture B — sustained chronology / established operating value
Expected structural pressure toward Sports Agent

Fixture C — unusual transferable/project evidence
Expected structural pressure toward Discovery Scout

Fixture D — strong direct industry fluency
Expected structural pressure toward Independent Staffing-Firm Owner

Fixture E — broad whole-person evidence with no single obvious anchor
Expected structural pressure toward Casting Director

Fixture F — dual-dominant evidence geometry

Fixture G — distributed evidence geometry

These expected pressures are test-fixture design conditions, NOT hard-coded output answers.

Do not hard-code prism percentages into the engine.

--------------------------------------------------
13. TESTS
--------------------------------------------------

Build automated tests covering:

all five prisms always execute

all five prisms survive consolidation

percentages normalize to exactly 100%

highest-ranked prism == owner_prism

every meaningful prism allocation has B4 evidence anchors

no evidence ID appears that was not in the admitted B4 package

B4 package remains unchanged after B5 execution

one prism cannot read another prism's result before consolidation

B5 payload contains no resume sentences

B5 payload contains no named template

B5 payload contains no physical layout coordinates

failed admission prevents prism execution

batch package isolation

one failed batch item does not invalidate other successful items

B5 writes only its owned output object

same deterministic fixture/input configuration produces structurally repeatable output where deterministic behavior is expected

--------------------------------------------------
14. WORKBENCH
--------------------------------------------------

Create a small runnable B5 workbench.

Required capabilities:

load one synthetic B4 package
load fixture batch
inspect package admission
run five prisms
inspect each PrismResult independently
run consolidation
inspect normalized distribution
inspect owner prism
inspect evidence anchors
inspect semantic priorities
inspect writing boundaries
inspect presentation geometry
export B5Payload
export execution receipt

The workbench is an inspection surface.

Do not spend time designing a polished Resume Factory UI.

--------------------------------------------------
15. RECEIPT
--------------------------------------------------

Every B5 execution must emit a receipt containing at minimum:

execution_id
package_id
admission_status
five prism execution statuses
consolidation_status
percentage_total
owner_prism
evidence_anchor_validation_status
boundary_validation_status
B5 payload location / identifier
timestamp

Batch mode also emits a batch manifest.

--------------------------------------------------
16. FORBIDDEN SCOPE
--------------------------------------------------

DO NOT implement:

Scout
Scout Disk
B
B1
B2
B3
B4 reasoning
Resume Factory
resume writing
candidate-job fit scoring
ATS optimization
job retrieval
source retrieval
candidate evidence retrieval
automatic repair of B4 evidence
new prism ontology
sixth prism
hidden universal prism weights
template selection
visual resume layout

DO NOT modify upstream architecture to make B5 easier.

--------------------------------------------------
17. DELIVERABLE
--------------------------------------------------

Return:

1. exact local project root used

2. files/modules created or changed

3. B5 module structure

4. B4ClearedPackage interface/schema

5. PrismSkill interface

6. five prism module boundaries

7. PrismResult interface/schema

8. Consolidator interface/module

9. B5Payload interface/schema

10. synthetic fixture set

11. automated tests and results

12. runnable B5 workbench command

13. sample single-package receipt

14. sample batch receipt

15. blockers or unresolved implementation questions

16. Git status / branch / HEAD if operating inside a repository

--------------------------------------------------
18. VERIFICATION STANDARD
--------------------------------------------------

Do not report B5 scaffold complete merely because files exist.

Completion requires executable evidence that:

a sealed B4-shaped package can enter

all five prisms execute independently

consolidation receives all five

a valid normalized five-prism distribution is emitted

the owner is selected

traceability to B4 evidence remains intact

semantic priorities and writing boundaries are produced

presentation geometry is produced

no Resume Factory work occurs

the upstream package remains unchanged

batch isolation works

--------------------------------------------------
19. STOP CONDITION
--------------------------------------------------

STOP when B5 emits a valid, inspectable, traceable B5 posture package and receipt from synthetic B4-cleared inputs.

Do not continue into Resume Factory.

Do not attempt to integrate with the unresolved Scout -> B -> B1 -> B2 -> B3 -> B4 Traveling Envelope unless separately authorized.