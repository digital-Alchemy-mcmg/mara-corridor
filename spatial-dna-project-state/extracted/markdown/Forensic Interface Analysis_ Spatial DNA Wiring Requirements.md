### Forensic Interface Analysis: Spatial DNA Wiring Requirements

#### 1\. The Entry Boundary: JOB → DEMAND → RECEPTORS

The Job Inception stage is the strategic foundation of the Spatial DNA architecture. By transitioning from unstructured market data to normalized receptors, the system establishes a "Target Demand Centroid." This centroid acts as the mathematical origin  $(0, 0, 0)$  for all subsequent spatial calculations, ensuring that candidate evidence is evaluated against a fixed, objective standard. Failure to lock this centroid at the inception stage leads to "Spark Drift," where the evaluative criteria oscillate during the matching process, compromising the integrity of the entire 3D topology.The handoff between raw job postings and the structured SCOUT\_TARGET\_OBSERVATION\_v1 envelope ensures that environmental noise is filtered out before reaching the evaluative engine. This is achieved through deterministic string extraction and structural section tagging, a "minimum reasoning push" that prevents the system from performing narrative smoothing or hallucinating requirements not present in the source text.| Input (Raw/Upstream) | Metadata/Source Field | Structured Output (SCOUT\_v1 Key) || \------ | \------ | \------ || **Raw Job Posting URL** | source\_url | provenance.source\_url || **Workbook Row (JOB-002)** | row\_id | observation\_id || **Collection Evidence** | disk\_cartridge\_hash | provenance.disk\_cartridge\_hash || **Employer Context** | compensation.min | entity\_metadata.compensation.min || **Requirement Clauses** | verbatim\_clauses | demand\_envelope.verbatim\_clauses || **Negative Constraints** | negative\_space | demand\_envelope.negative\_space\_constraints |

The transformation of these clauses into  $D\_k$  receptors is the primary point of normalization. Using identifiers like receptor\_id and job\_id, the system maps verbatim text to categorical receptors (e.g.,  $D\_{01}$  Operational Leadership,  $D\_{02}$  Financial Discipline). This step is strictly limited to structural tagging; the system must not "soften" the employer's requirements at this boundary. These receptors serve as the primary gravitational pull for the evidence substrate, transitioning the data into the Binding Gate.

#### 2\. The Core Evaluative Boundary: RECEPTORS → SPATIAL DNA → TRAVERSAL / BINDING

The "Binding Gate" is a strategic necessity designed to decouple candidate evidence from chronological decay. By classifying capability strength regardless of the candidate's linear timeline, the architecture treats human experience as a set of atemporal assets. This boundary ensures that an atom of evidence—whether generated yesterday or a decade ago—is projected based on its semantic proximity to the  $D\_k$  receptors rather than its date of origin.The data flow maps the  $D\_{01}..D\_n$  receptors against the candidate substrate, consisting of 44 immutable atoms and 11 relational edges. The transformation logic utilizes a three-tier binding classification:

* **DIRECT\_BIND:**  Empirical, verified evidence fulfilling primary operational demands.  
* **TRANSFERABLE\_BIND:**  Foundational or analogous capability supporting the role.  
* **NON\_BIND:**  Evidence outside the target envelope, relegated to a dormant state.This stage requires specific payloads from the candidate\_spatial\_dna\_nodes.jsonl and edges.jsonl files to maintain the graph's structural integrity. A forensic requirement of this boundary is "Conflict Preservation." Historical discrepancies are not smoothed; they are explicitly categorized into five registers—TIMELINE\_DISPUTE, TITLE\_DISCREPANCY, ONSET\_OVERLAP, SEPARATION\_DOCUMENTATION, and CREDENTIAL\_STATUS. These conflicted atoms are assigned to the Floor zone ( $Y \\le \-2.0$ ) and flagged with quarantine\_action to prevent them from inflating the candidate's match strength. Once classified, the atoms are prepared for geometric translation in the Coordinate Engine.

#### 3\. The Geometric Boundary: BINDING → SPATIAL PROJECTION → COORDINATES

Deterministic projection is critical for converting semantic "match strength" into an observable, non-hallucinatory topology. By calculating coordinates  $(X, Y, Z, R)$ , the system moves from subjective interpretation to a 3D Cartesian space where proximity to the origin represents objective suitability.The mathematical handoff from the Binding Gate to the Coordinate Engine utilizes the following deterministic formulas to ensure "Zero Drift":

* **Radial Distance (**  **$R**$  **):**  Calculated as  $R \= 11.0 \- (match\\\_strength \\times 7.0)$ , bounded strictly between  $3.0, 10.0$ .  
* **Planar Azimuth (**  **$\\theta**$  **):**  Computed as  $\\arctan(X/Z)$  to determine the angular position relative to the domain plane.  
* **Vertical Polarity (**  **$Y**$  **):**  Designated as Ceiling ( $Y \\ge \+2.0$ ), Baseline ( $-2.0 \< Y \< \+2.0$ ), or Floor ( $Y \\le \-2.0$ ).Orchestration at this boundary involves selecting the top 4 active lateral planes (drawn from the 6 origin planes: Identity, Work History, Education/Tech, Creative, Psychometric, and References) to surround the vertical Y-axis. During this handoff, the "Zero Physics Rule" must be enforced as a validation constraint. The system is prohibited from applying simulated forces, such as gravity or spring-loaded layout logic, to "clean up" the visual representation; the coordinates must remain exactly where the math places them. These verified coordinates are then packaged for downstream consumption by layout engines.

#### 4\. The Structural Handoff: COORDINATES → SPATIAL PAYLOAD → LAYOUT PAYLOAD

The MARA\_LAYOUT\_PAYLOAD\_v1 serves as the durable packet bridging pure spatial data and human-readable document architecture. It ensures that the high-dimensional coordinate graph is translated into a format that a layout engine can use to construct a professional summary, while maintaining a direct trace to the underlying evidence.The transition from raw coordinates to dynamic\_layout\_elements is governed by the "Surface Transducer" rules (specifically PIN 18–21). These rules function as a density filter, translating the  $(X, Y, Z)$  coordinates into specific UI containers. For example, atoms with a high  $Y$ \-polarity and low  $R$  (match strength) are mapped to the "Executive Pitch" or "Header," while lower-priority atoms are directed to "Bullets" or the "Competency Matrix."To maintain total provenance, the following identifiers must survive this stage:

* **atom\_id**  **:**  The immutable primary key linking evidence blurbs to coordinates.  
* **disk\_cartridge\_hash**  **and**  **source\_url**  **:**  Verification of the data's Stage 1 origin.  
* **layout\_containers**  **:**  The structured JSON elements (Header, Experience, Bullets) that organize the bound atoms for the visual renderer.This payload serves as the final instruction set for the visual renderer, ensuring that every claim in the final document is anchored to a specific point in the 3D topology.

#### 5\. The Visual Boundary: LAYOUT PAYLOAD → CANVAS

The "Passive Observer" model is the strategic mandate for the Visual Boundary. The Canvas must be strictly decoupled from calculation to ensure round-trip validation integrity. If the Canvas were allowed to adjust coordinates for "aesthetic" reasons, it would break the forensic link between the evidence and the math.The rendering harness ingests the CANVAS\_RENDERING\_SPECIFICATION and enforces two critical rules:

* **Color Mapping Rule:**  Plane-specific hex codes must be applied (e.g., plane\_02/Work History \= Amber \#F59E0B; plane\_01/Identity \= Blue \#3B82F6).  
* **Binding Ray Rule:**  DIRECT\_BIND atoms must render a solid ray to the origin  $(0, 0, 0)$ , while TRANSFERABLE\_BIND atoms render a dashed ray. NON\_BIND atoms receive no ray.The harness must also execute "Round-Trip Verification" by performing "Boundary Tamper Tests." If an atom is passed with a coordinate outside the legal volume (e.g.,  $X \> 10.0$  or  $Y \< \-5.0$ ), the system must trigger an OUT\_OF\_BOUNDS\_ERROR and halt the render immediately. This prevents the display of distorted data and ensures that the final state—a visual 3D topology—is a faithful representation of the evidentiary substrate.

#### 6\. Identification of System Disconnections & Data Gaps

The primary strategic risk currently facing the system is "Spark Drift" caused by unautomated links between the 5 stages. Forensic analysis of the current "Not Yet Proven" ledger identifies the following gaps:

* **Daemon Absence:**  There is no autonomous daemon or script to chain raw SCOUT observations directly to the Binding Gate, necessitating manual handoffs.  
* **Receptor Compilation:**  The SCOUT runner does not yet autonomously compile text into  $D\_n$  demand receptors; this currently requires external coordination.  
* **Attribute Omissions:**  The exported atom objects currently omit Angular Azimuth ( $\\theta$ ) and Multi-Binding Vectors (array of bound\_receptors), forcing downstream consumers to back-calculate these values.  
* **Suppression Context:**  The current payload lacks a "Negative Space Suppression Signature," meaning NON\_BIND atoms are excluded without a record of which negative constraint triggered the suppression.

#### 7\. THE HARNESS MUST BE ABLE TO:

The wiring harness for the Spatial DNA system must fulfill the following functional requirements to maintain system integrity:

1. **Orchestrate the 5-Stage Causal Flow:**  Manage the deterministic transition of data from Job Inception through to the final Canvas rendering without manual intervention.  
2. **Enforce "Zero Physics" and "Zero Drift" Mandates:**  Prevent any layout engines or renderers from applying simulated forces or "smoothing" logic to the coordinates.  
3. **Maintain the**  **atom\_id**  **Join Key:**  Ensure this immutable primary key persists across all boundaries for perfect forensic traceability.  
4. **Calculate and Inject Missing Attributes:**  Compute and inject Angular Azimuth ( $\\theta$ ) and multi-binding vectors into the exported atom objects to eliminate back-calculation at the Canvas.  
5. **Quarantine Management:**  Effectively isolate and project the five historical conflict registers into the Floor zone ( $Y \\le \-2.0$ ) with appropriate quarantine\_action metadata.  
6. **Execute Round-Trip Verification:**  Perform automated "Boundary Tamper Tests" to ensure the renderer is not misrepresenting the spatial payload.  
7. **Preserve Provenance Hashes:**  Ensure that disk\_cartridge\_hash and source\_url from Stage 1 are preserved through the final MARA\_LAYOUT\_PAYLOAD\_v1 for auditability.

&nbsp;