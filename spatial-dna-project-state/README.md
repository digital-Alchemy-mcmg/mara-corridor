# Spatial DNA transferred project state

## Scope and reading order

This package preserves what was available for the September 2026 transfer, and records the difference between source claims and inspected repository facts. It does not establish a working end-to-end application. Read `manifests/files.json` to locate all files and confirm hashes, `provenance/transfer-index.md` to trace sources, `handoff/state-audit.md` for the qualified state, and `open-problems/discrepancies.md` before using example values as a contract.

The 14 files under `originals/transferred/` are the byte-identical supplied sources. `extracted/` contains searchable DOCX paragraph and table text, CSV tables and workbook sheets, page-by-page PDF OCR, Markdown copies, and embedded OOXML media. The PDFs and images remain the visual authority for their own content; OCR can be inaccurate. `03-spatial-projection-coordinates/` and `04-spatial-and-layout-payload/` expose two parsed examples without correction. `history/branch-snapshots/` preserves files from `DNA` and `ENGine` at their inspected tips. The repository's `main` workbook is separately copied into `history/branch-snapshots/main/`.

## Five stages

1. `01-job-inception-normalization-demand/`: job source and normalization, observations, and demand receptors. The transferred training workbook is an input and calibration resource. General extraction logic is not established as executable.
2. `02-candidate-evidence-spatial-dna-binding/`: candidate atoms in six planes, edges, traversal, binding, and conflict quarantine. The 44 atoms and 11 edges are reported; the inspected `DNA` branch machine graph files are empty.
3. `03-spatial-projection-coordinates/`: 25 coordinate records parsed directly from the supplied DOCX. Their field labels and `VERIFIED` values are source labels, not this preservation pass's independent verification of geometry.
4. `04-spatial-and-layout-payload/`: JOB-002 layout example parsed directly from the supplied DOCX. It preserves source contents; its production path is not demonstrated.
5. `05-test-canvas-validation-observability/`: the test harness and canvas are described in the original PDFs and wiring analysis. No executable canvas is in the inspected branch trees.

Most source documents cover several stages and remain intact in `originals/` and searchable under `extracted/`; folders for stages without independently supplied executable artifacts contain pointers, not invented schemas or code.

## Recovery checks

From this branch, a fresh reader can recover the supplied originals, extracted values, prior branch-tip files, preservation audit, and open questions. The SPDNA Notebook collection, uploaded project ZIP, claimed populated graph/code and independently reproducible runs were not supplied to this workspace. The presence of descriptions does not change those access facts. See `handoff/recovery.md`.
