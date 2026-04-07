"""
parse_analysis_files.py

Loads all procedure and view analysis JSON files from the parent
01-oracle_analyse/ directory, normalizes table names with schema prefixes,
and writes a unified parsed_objects.json to the output/ folder.

Usage:
    python parse_analysis_files.py

Output:
    output/parsed_objects.json
"""

import json
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent
SOURCE_DIR = SCRIPT_DIR.parent          # 01-oracle_analyse/
OUTPUT_DIR = SCRIPT_DIR / "output"


# ---------------------------------------------------------------------------
# Schema extraction
# ---------------------------------------------------------------------------

def extract_schema_from_filename(filename: str) -> str | None:
    """
    Extract the schema name from a JSON filename.

    Pattern: *_temp_<schema>_user_* (e.g. tnn-..._temp_ccm_user_source_...)
    Returns the schema in uppercase, e.g. 'CCM', 'CLM_ADM', 'CLM_CCM',
    'CRM_ANALYSE'.
    """
    match = re.search(r"_temp_(.+?)_user_", filename, re.IGNORECASE)
    if match:
        return match.group(1).upper()
    return None


# ---------------------------------------------------------------------------
# Table-name normalisation
# ---------------------------------------------------------------------------

def normalize_table_name(name: str, owning_schema: str) -> str:
    """
    Qualify a table name with a schema prefix if it doesn't already have one.

    If the name already contains a dot (e.g. 'CLM_ADM.SOME_TABLE'), keep it
    as-is. Otherwise, prepend the owning schema.
    """
    name = name.strip()
    if "." in name:
        return name.upper()
    return f"{owning_schema}.{name}".upper()


# ---------------------------------------------------------------------------
# JSON loaders
# ---------------------------------------------------------------------------

def load_procedures_file(path: Path, schema: str) -> tuple[list[dict], list[dict]]:
    """
    Parse a procedures analysis JSON file.

    Returns:
        (successful, failed) — lists of parsed procedure dicts.
    """
    with path.open(encoding="utf-8") as f:
        raw = json.load(f)

    successful: list[dict] = []
    failed: list[dict] = []

    for item in raw:
        procedure_name = item.get("procedure_name", "").strip().upper()
        error = item.get("error") or None

        if error:
            failed.append({
                "object_name": f"{schema}.{procedure_name}",
                "object_type": "procedure",
                "schema": schema,
                "error": error,
            })
            continue

        data_sources = [
            normalize_table_name(s, schema)
            for s in item.get("data_sources", [])
            if s and s.strip()
        ]

        raw_targets = item.get("target_tables", [])
        target_tables = []
        for t in raw_targets:
            table_name = normalize_table_name(t.get("table_name", ""), schema)
            is_temporary = bool(t.get("is_temporary", False))
            target_tables.append({"table_name": table_name, "is_temporary": is_temporary})

        successful.append({
            "object_name": f"{schema}.{procedure_name}",
            "object_type": "procedure",
            "schema": schema,
            "functionality": item.get("functionality", ""),
            "data_sources": data_sources,
            "target_tables": target_tables,
            "error": None,
        })

    return successful, failed


def load_views_file(path: Path, schema: str) -> tuple[list[dict], list[dict]]:
    """
    Parse a views analysis JSON file.

    Returns:
        (successful, failed) — lists of parsed view dicts.
    """
    with path.open(encoding="utf-8") as f:
        raw = json.load(f)

    successful: list[dict] = []
    failed: list[dict] = []

    for item in raw:
        view_name = item.get("view_name", "").strip().upper()
        error = item.get("error") or None

        if error:
            failed.append({
                "object_name": f"{schema}.{view_name}",
                "object_type": "view",
                "schema": schema,
                "error": error,
            })
            continue

        data_sources = [
            normalize_table_name(s, schema)
            for s in item.get("data_sources", [])
            if s and s.strip()
        ]

        successful.append({
            "object_name": f"{schema}.{view_name}",
            "object_type": "view",
            "schema": schema,
            "functionality": item.get("functionality", ""),
            "data_sources": data_sources,
            "target_tables": [],   # views do not write to target tables
            "error": None,
        })

    return successful, failed


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    all_objects: list[dict] = []
    all_failed: list[dict] = []

    # Counters for the summary
    schema_stats: dict[str, dict[str, int]] = {}

    # --- Procedures ---------------------------------------------------------
    proc_files = sorted(SOURCE_DIR.glob("*_procedures_analysis.json"))
    if not proc_files:
        print("WARNING: No procedure analysis files found.")

    for path in proc_files:
        schema = extract_schema_from_filename(path.name)
        if schema is None:
            print(f"WARNING: Could not extract schema from '{path.name}', skipping.")
            continue

        successful, failed = load_procedures_file(path, schema)

        stats = schema_stats.setdefault(schema, {"proc_ok": 0, "proc_fail": 0, "view_ok": 0, "view_fail": 0})
        stats["proc_ok"] += len(successful)
        stats["proc_fail"] += len(failed)

        all_objects.extend(successful)
        all_failed.extend(failed)

    # --- Views --------------------------------------------------------------
    view_files = sorted(SOURCE_DIR.glob("*_views_analysis.json"))
    if not view_files:
        print("WARNING: No view analysis files found.")

    for path in view_files:
        schema = extract_schema_from_filename(path.name)
        if schema is None:
            print(f"WARNING: Could not extract schema from '{path.name}', skipping.")
            continue

        successful, failed = load_views_file(path, schema)

        stats = schema_stats.setdefault(schema, {"proc_ok": 0, "proc_fail": 0, "view_ok": 0, "view_fail": 0})
        stats["view_ok"] += len(successful)
        stats["view_fail"] += len(failed)

        all_objects.extend(successful)
        all_failed.extend(failed)

    # --- Write output -------------------------------------------------------
    output = {
        "objects": all_objects,
        "failed": all_failed,
    }
    out_path = OUTPUT_DIR / "parsed_objects.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    # --- Print summary ------------------------------------------------------
    total_ok = len(all_objects)
    total_fail = len(all_failed)
    total = total_ok + total_fail

    print(f"\n{'=' * 60}")
    print(f"  Oracle Analysis Parser — Summary")
    print(f"{'=' * 60}")
    print(f"  Total objects processed : {total}")
    print(f"  Successfully parsed     : {total_ok}")
    print(f"  Failed (with errors)    : {total_fail}")
    print(f"{'-' * 60}")
    print(f"  {'Schema':<20} {'Proc OK':>8} {'Proc Err':>9} {'View OK':>8} {'View Err':>9}")
    print(f"  {'-'*20} {'-'*8} {'-'*9} {'-'*8} {'-'*9}")
    for schema in sorted(schema_stats):
        s = schema_stats[schema]
        print(
            f"  {schema:<20} {s['proc_ok']:>8} {s['proc_fail']:>9} "
            f"{s['view_ok']:>8} {s['view_fail']:>9}"
        )
    print(f"{'=' * 60}")
    print(f"\nOutput written to: {out_path}\n")


if __name__ == "__main__":
    main()
