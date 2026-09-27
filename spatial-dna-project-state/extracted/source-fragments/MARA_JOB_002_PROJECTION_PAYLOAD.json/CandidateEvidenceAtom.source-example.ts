export interface CandidateEvidenceAtom {
  atom_id: string;               // e.g. "WH-TWIN-001"
  domain: DomainType;            // "Work History", "Creative Works", etc.
  plane_assignment: string;      // "plane_01" through "plane_06"
  claim: string;                 // The factual proposition
  evidence_state: EvidenceState; // "VERIFIED" | "SUPPORTED" | "CONFLICTED" | "CANDIDATE-REPORTED"
  provenance: {
    branch: string;              // "Twin Peaks"
    source_ref: string;          // "SRC-RESUME-001"
  };
  temporal_semantics: {
    durability_class: "DURABLE_CAPABILITY" | "TIME_SENSITIVE" | "HISTORICAL_TRAJECTORY";
    decay_rule: string;
  };
  edges: string[];               // Connected atom IDs from edges.jsonl
}
