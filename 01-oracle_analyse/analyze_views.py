"""CLI-script for analyse av Oracle-views med Gemini."""

import argparse
import json
import os
import sys
import time

import pandas as pd
from tqdm import tqdm

from config import (
    SCHEMAS,
    call_llm_with_retry,
    check_gcp_auth,
    cleanup_checkpoint,
    fetch_bigquery_data,
    get_checkpoint_filename,
    get_full_table_id,
    get_output_filename,
    init_vertex_ai,
    load_checkpoint,
    parse_llm_response,
    save_checkpoint,
)

PROMPT_TEMPLATE = """
Analyze the following Oracle SQL view script. Extract its main functionality and, for every table or view it reads from, provide column-level lineage.

Specifically, identify:
1.  **functionality**: A string describing the view's main purpose.
2.  **data_sources**: A list of objects for each table or view the script READS FROM. Each object must include `table_name` and a `columns` list of specific columns read.

If column-level details cannot be determined (e.g., `SELECT *`), provide an empty list for `columns`.

JSON output format:
{{
  "functionality": "Creates a unified view of customer data by joining customer and address tables.",
  "data_sources": [
    {{
      "table_name": "CUSTOMERS",
      "columns": ["customer_id", "first_name", "last_name", "address_id"]
    }},
    {{
      "table_name": "ADDRESSES",
      "columns": ["address_id", "street", "city", "zip_code"]
    }}
  ]
}}

SQL Script:
---
{sql_script}
---
"""


def analyze_views(schema: str, model, output_dir: str, checkpoint_interval: int, dry_run: bool, max_items: int = None):
    """Analyserer views for ett skjema."""
    table_id = get_full_table_id(schema, "views")
    output_file = get_output_filename(schema, "views", output_dir)
    checkpoint_file = get_checkpoint_filename(schema, "views", output_dir)

    print("\n" + "=" * 60)
    print("Skjema: " + schema + " — " + table_id)
    print("=" * 60)

    # Hent data fra BigQuery
    df = fetch_bigquery_data(table_id)

    if max_items:
        df = df.head(max_items)
        print(f"Begrenser til {max_items} views for testing.")

    if dry_run:
        print(f"[DRY RUN] {len(df)} views funnet. Avbryter.")
        return

    # Last checkpoint
    completed, results = load_checkpoint(checkpoint_file)
    remaining = len(df) - len(completed)
    print(f"Analyserer {remaining} gjenstående views...")

    run_start = time.perf_counter()

    for _, row in tqdm(df.iterrows(), total=len(df), desc=f"Views ({schema})"):
        view_name = row["view_name"]

        if view_name in completed:
            continue

        sql_script = row["text_long"] if pd.notna(row.get("text_long")) else row.get("text_vc", "")
        prompt = PROMPT_TEMPLATE.format(sql_script=sql_script)

        try:
            response_text = call_llm_with_retry(model, prompt)
            parsed = parse_llm_response(response_text)
            results.append({
                "view_name": view_name,
                "functionality": parsed.get("functionality", "N/A"),
                "data_sources": parsed.get("data_sources", []),
            })
        except Exception as e:
            results.append({
                "view_name": view_name,
                "functionality": "Error during analysis",
                "data_sources": [],
                "error": str(e),
            })

        completed.add(view_name)

        if len(completed) % checkpoint_interval == 0:
            save_checkpoint(checkpoint_file, completed, results)
            elapsed = time.perf_counter() - run_start
            avg = elapsed / len(completed)
            print(f"  [CHECKPOINT] {len(completed)}/{len(df)} (snitt {avg:.1f}s per view)")

    # Lagre endelig resultat
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)
    print(f"Resultat lagret: {output_file}")

    cleanup_checkpoint(checkpoint_file)


def main():
    parser = argparse.ArgumentParser(description="Analyser Oracle-views med Gemini")
    parser.add_argument(
        "--schema", "-s",
        nargs="+",
        required=True,
        help=f"Skjema(er) å analysere, eller 'all'. Gyldige: {', '.join(SCHEMAS.keys())}",
    )
    parser.add_argument("--output-dir", "-o", default=".", help="Mappe for output-filer")
    parser.add_argument("--checkpoint-interval", "-c", type=int, default=5, help="Lagre checkpoint hvert N. view")
    parser.add_argument("--dry-run", action="store_true", help="Bare hent data, vis antall")
    parser.add_argument("--max-items", type=int, default=None, help="Maks antall elementer å behandle (for testing)")

    args = parser.parse_args()

    # Bestem skjemaer
    if args.schema == ["all"]:
        schemas = list(SCHEMAS.keys())
    else:
        for s in args.schema:
            if s not in SCHEMAS:
                print(f"Ukjent skjema: {s}. Gyldige: {', '.join(SCHEMAS.keys())}")
                sys.exit(1)
        schemas = args.schema

    os.makedirs(args.output_dir, exist_ok=True)

    check_gcp_auth()
    model = init_vertex_ai()

    for schema in schemas:
        analyze_views(schema, model, args.output_dir, args.checkpoint_interval, args.dry_run, args.max_items)

    print("\nFerdig! " + str(len(schemas)) + " skjema(er) behandlet.")


if __name__ == "__main__":
    main()
