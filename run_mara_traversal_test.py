#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NODES = ROOT / "candidate-spatial-dna-kg" / "graph" / "nodes.jsonl"
EDGES = ROOT / "candidate-spatial-dna-kg" / "graph" / "edges.jsonl"
PROJECTION = ROOT / "spatial-dna-tests" / "job_002_projection_source.json"
LAYOUT = ROOT / "spatial-dna-tests" / "job_002_layout_source.json"

EXPECTED_NODE_COUNT = 44
EXPECTED_EDGE_COUNT = 11
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

def fail(errors, facts):
    print(json.dumps({
        "status": "ERROR",
        "error_code": "LINEAGE_ERROR",
        "stage": "SPATIAL_DNA_LINEAGE_GATE",
        "facts": facts,
        "errors": errors,
    }, indent=2))
    return 1

def main():
    nodes = read_jsonl(NODES)
    edges = read_jsonl(EDGES)
    projection = json.loads(PROJECTION.read_text(encoding="utf-8"))
    layout = json.loads(LAYOUT.read_text(encoding="utf-8"))

    errors = []
    ids = [n["atom_id"] for n in nodes]
    id_set = set(ids)

    if len(nodes) != EXPECTED_NODE_COUNT:
        errors.append(f"Expected {EXPECTED_NODE_COUNT} atoms, found {len(nodes)}.")
    if len(id_set) != len(ids):
        errors.append("Duplicate atom_id values exist.")
    if len(edges) != EXPECTED_EDGE_COUNT:
        errors.append(f"Expected {EXPECTED_EDGE_COUNT} edges, found {len(edges)}.")

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
            "JOB-002 projection references atom IDs absent from the 44-atom graph: "
            + ", ".join(orphan_projection_ids)
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
            content = str(row.get("Content_Payload",""))
            if year_range.search(content) and not re.search(r"unresolved|conflict|2023/2024|2023\s*or\s*2024", content, re.I):
                errors.append(
                    "Chronology smoothing detected: role_header bound to conflicted atom(s) "
                    + ", ".join(conflicted)
                    + f" collapses unresolved chronology: {content}"
                )

    facts = {
        "node_count": len(nodes),
        "edge_count": len(edges),
        "conflicted_atom_ids": sorted(graph_conflicts),
        "job_002_projection_rows": len(projection),
        "job_002_layout_rows": len(layout),
        "orphan_projection_ids": orphan_projection_ids,
    }

    if errors:
        return fail(errors, facts)

    print(json.dumps({
        "status": "PASS",
        "stage": "SPATIAL_DNA_LINEAGE_GATE",
        "facts": facts,
    }, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
