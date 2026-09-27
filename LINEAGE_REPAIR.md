# Spatial DNA lineage repair branch

This branch converts the September 23 preservation state into an executable lineage-gated recovery surface.

## What was restored
- Authoritative 44-atom candidate graph from Google Drive.
- Authoritative 11-edge v2 relationship ledger from Google Drive.
- JOB-002 demand, projection, and layout source tables from the connected Google Sheet.
- Exact 25-coordinate source fixture from Google Drive.
- A runnable lineage validator at `run_mara_traversal_test.py`.

## Current gate
Run:

`python run_mara_traversal_test.py`

The gate intentionally fails while JOB-002 references atom IDs that do not exist in the recovered 44-atom graph or while conflicted chronology is silently collapsed. This is not treated as a successful traversal until those source-level defects are repaired with authority.

See `governance/lineage-corrections.json`.
