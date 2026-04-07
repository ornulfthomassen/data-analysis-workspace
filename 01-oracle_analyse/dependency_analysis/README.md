# Oracle Dependency Analysis

Standalone Python scripts that parse the Gemini-generated Oracle database
object analysis and build a complete dependency graph showing how procedures
and views are interconnected.

## Prerequisites

- Python 3.13+
- No external packages required (standard library only)

## Usage

Run the scripts in order from this directory:

```bash
# Step 1 — Parse all analysis JSON files and produce a unified output
python parse_analysis_files.py

# Step 2 — Build the dependency graph from the parsed data
python build_dependency_graph.py

# Optional: include temporary tables when building edges
python build_dependency_graph.py --include-temp
```

## Scripts

### `parse_analysis_files.py`

- Auto-discovers all `*_procedures_analysis.json` and `*_views_analysis.json`
  files in the parent `01-oracle_analyse/` directory
- Extracts the schema name from each filename
  (e.g. `..._temp_ccm_user_...` → schema `CCM`)
- Normalizes table names: if a table name already has a schema prefix
  (e.g. `CLM_ADM.SOME_TABLE`), it is kept as-is; otherwise the owning
  schema is prepended
- Skips objects with a non-null `error` field but records them separately
  for reporting
- Prints a per-schema summary to stdout

**Output:** `output/parsed_objects.json`

### `build_dependency_graph.py`

- Reads `output/parsed_objects.json`
- Builds directed edges: if procedure A writes to table X and procedure B
  reads from table X, an edge A → B is created
- Temporary tables (`is_temporary: true`) are **excluded** from edge-building
  by default (use `--include-temp` to include them)
- Handles cross-schema dependencies
- Prints a summary with the top 10 most connected objects

**Output:**

| File | Description |
|------|-------------|
| `output/dependency_edges.json` | Flat list of directed edges with `source`, `target`, `linked_table`, `source_type`, `target_type` |
| `output/dependency_graph.json` | Adjacency list per object: `upstream`, `downstream`, `type`, `schema` |
| `output/dependency_summary.json` | High-level stats: total objects/edges, cross-schema edge count, isolated objects, top 10 most connected |

## Notes

- If view analysis files are incomplete or contain errors, re-run the
  upstream analysis scripts and then re-run these scripts to include view
  dependencies.
- Output files are written to `output/` (created automatically if absent).
