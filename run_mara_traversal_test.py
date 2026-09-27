#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NODES = ROOT / "candidate-spatial-dna-kg" / "graph" / "nodes.jsonl"
EDGES = ROOT / "candidate-spatial-dna-kg" / "graph" / "edges.jsonl"
PROJECTION = ROOT / "spatial-dna-tests" / "job_002_projection_current.json"
LAYOUT = ROOT / "spatial-dna-tests" / "job_002_layout_current.json"
FIXTURE = ROOT / "contracts" / "TEST_FIXTURE_METHOD_HOSPITALITY.json"
AUTHORITY = ROOT / "contracts" / "AUTHORITY_MAP.json"
BINDING_MATRIX = ROOT / "contracts" / "JOB_002_BINDING_MATRIX.json"

CANONICAL_CONFLICTS = {
    "WH-BOBC-001",
    "WH-APPL-001",
    "WH-MCMG-001",
    "WH-WLT-001",
    "ED-OU-001",
}

def read_jsonl(path):
    out = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            out.append(json.loads(raw))
        except json.JSONDecodeError as exc:
            raise SystemExit(json.dumps({
                "status": "ERROR",
                "error_code": "LINEAGE_ERROR",
                "stage": "GRAPH_LOAD",
                "details": f"{path}:{lineno}: {exc}",
            }, indent=2))
    return out

def emit_error(errors, facts):
    print(json.dumps({
        "status": "ERROR",
        "error_code": "HARNESS_VALIDATION_ERROR",
        "stage": "SPATIAL_DNA_LINEAGE_GATE",
        "facts": facts,
        "errors": errors,
    }, indent=2))
    return 1

def main():
    nodes = read_jsonl(NODES)
    edges = read_jsonl(EDGES)
    projection_doc = json.loads(PROJECTION.read_text(encoding="utf-8"))
    projection = projection_doc["rows"]
    layout_doc = json.loads(LAYOUT.read_text(encoding="utf-8"))
    layout = layout_doc["rows"]
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    authority = json.loads(AUTHORITY.read_text(encoding="utf-8"))

    errors = []
    ids = [n["atom_id"] for n in nodes]
    id_set = set(ids)
    acceptance = fixture["acceptance"]

    if len(nodes) != acceptance["total_atoms"]:
        errors.append(f"Expected {acceptance['total_atoms']} atoms, found {len(nodes)}.")
    if len(id_set) != len(ids):
        errors.append("Duplicate atom_id values exist.")
    if len(edges) != 11:
        errors.append(f"Expected 11 edges, found {len(edges)}.")

    graph_conflicts = {n["atom_id"] for n in nodes if n.get("evidence_state") == "CONFLICTED"}
    missing_conflicts = sorted(CANONICAL_CONFLICTS - graph_conflicts)
    if missing_conflicts:
        errors.append(f"Canonical conflicts missing from graph: {missing_conflicts}")

    for edge in edges:
        for side in ("source", "target"):
            if edge[side] not in id_set:
                errors.append(f"{edge['edge_id']} {side} references missing atom {edge[side]}.")

    projection_ids = [r.get("Atom_ID","") for r in projection if r.get("Atom_ID")]
    orphan_projection_ids = sorted(set(projection_ids) - id_set)
    if orphan_projection_ids:
        errors.append(
            "Current repaired JOB-002 projection still references IDs absent from the 44-atom substrate: "
            + ", ".join(orphan_projection_ids)
        )
    quarantined_legacy_ids = sorted(
        {r.get("Atom_ID") for r in projection_doc.get("quarantined_legacy_rows", []) if r.get("Atom_ID")}
    )

    for row in projection:
        atom_id = row.get("Atom_ID")
        if not atom_id or atom_id not in id_set:
            continue
        atom = next(n for n in nodes if n["atom_id"] == atom_id)
        if atom.get("evidence_state") == "CONFLICTED":
            y = float(row.get("Coord_Y", 0) or 0)
            zone = row.get("Polarity_Zone","")
            if y > -2.0 or "FLOOR" not in zone:
                errors.append(f"QUARANTINE_VIOLATION: {atom_id} is conflicted but projected outside Floor.")

    year_range = re.compile(r"\b(19|20)\d{2}\s*[-–]\s*(19|20)\d{2}\b")
    for row in layout:
        traces = [x for x in str(row.get("Bound_Atom_Trace","")).split(";") if x]
        conflicted = [t for t in traces if t in graph_conflicts]
        if conflicted and row.get("Element_Type") == "role_header":
            text = str(row.get("Content_Payload",""))
            if year_range.search(text) and not re.search(r"unresolved|conflict|2023/2024|2023\s*or\s*2024", text, re.I):
                errors.append(
                    "LINEAGE_ERROR: role header bound to conflicted atom(s) "
                    + ", ".join(conflicted)
                    + f" collapses unresolved chronology: {text}"
                )

    binding_counts = None
    missing_binding_matrix = not BINDING_MATRIX.exists()
    if missing_binding_matrix:
        errors.append(
            "CURRENT_AUTHORITY_GAP: acceptance requires 12 DIRECT_BIND / 16 TRANSFERABLE_BIND / "
            "16 NON_BIND across all 44 atoms, but current authority does not enumerate the complete "
            "44-row membership map. Null-by-default governance forbids manufacturing it."
        )
    else:
        matrix = json.loads(BINDING_MATRIX.read_text(encoding="utf-8"))
        rows = matrix.get("bindings", [])
        matrix_ids = [r.get("atom_id") for r in rows]
        if len(rows) != len(nodes) or set(matrix_ids) != id_set:
            errors.append("JOB_002_BINDING_MATRIX.json must contain exactly one classification for each current atom_id.")
        classes = [r.get("binding_class") for r in rows]
        binding_counts = {
            "DIRECT_BIND": classes.count("DIRECT_BIND"),
            "TRANSFERABLE_BIND": classes.count("TRANSFERABLE_BIND"),
            "NON_BIND": classes.count("NON_BIND"),
        }
        expected = {
            "DIRECT_BIND": acceptance["direct_bind_count"],
            "TRANSFERABLE_BIND": acceptance["transferable_bind_count"],
            "NON_BIND": acceptance["non_bind_count"],
        }
        if binding_counts != expected:
            errors.append(f"Binding counts {binding_counts} do not match current acceptance {expected}.")

    facts = {
        "authority_version": authority["authority_map_version"],
        "node_count": len(nodes),
        "edge_count": len(edges),
        "conflicted_atom_ids": sorted(graph_conflicts),
        "job_002_projection_rows": len(projection),
        "job_002_layout_rows": len(layout),
        "orphan_projection_ids": orphan_projection_ids,
        "quarantined_legacy_ids": quarantined_legacy_ids,
        "binding_matrix_present": not missing_binding_matrix,
        "binding_counts": binding_counts,
        "acceptance": acceptance,
    }

    if errors:
        return emit_error(errors, facts)

    print(json.dumps({
        "status": "PASS",
        "stage": "SPATIAL_DNA_LINEAGE_GATE",
        "facts": facts,
    }, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
