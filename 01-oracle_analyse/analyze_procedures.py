"""CLI-script for analyse av Oracle-prosedyrer med Gemini."""

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
Analyze the following Oracle SQL procedure script. Extract its main functionality, and for every table or view it interacts with, provide column-level lineage.

Specifically, identify:
1.  **functionality**: A string describing the procedure's main purpose.
2.  **data_sources**: A list of objects for each table or view the script READS FROM. Each object must include `table_name` and a `columns` list of specific columns read.
3.  **target_tables**: A list of objects for each table the script WRITES TO (INSERT, UPDATE, DELETE). Each object must include `table_name`, `is_temporary` (boolean), and a `columns` list of specific columns written to.

If column-level details cannot be determined (e.g., `SELECT *`), provide an empty list for `columns`.

JSON output format:
{{
  "functionality": "Processes daily sales data, inserting aggregated results into a permanent sales summary table.",
  "data_sources": [
    {{
      "table_name": "SALES_TRANSACTIONS",
      "columns": ["product_id", "sale_date", "amount"]
    }},
    {{
      "table_name": "PRODUCTS",
      "columns": ["product_id", "product_name"]
    }}
  ],
  "target_tables": [
    {{
      "table_name": "DAILY_SALES_SUMMARY",
      "is_temporary": false,
      "columns": ["sale_date", "total_sales"]
    }}
  ]
}}

SQL Script:
---
{sql_script}
---
"""


def analyze_procedures(schema: str, model, output_dir: str, checkpoint_interval: int, dry_run: bool, max_items: int = None):
    """Analyserer prosedyrer for ett skjema."""
    table_id = get_full_table_id(schema, "procedures")
    output_file = get_output_filename(schema, "procedures", output_dir)
    checkpoint_file = get_checkpoint_filename(schema, "procedures", output_dir)

    print("\n" + "=" * 60)
    print("Skjema: " + schema + " — " + table_id)
    print("=" * 60)

    # Hent data fra BigQuery
    df = fetch_bigquery_data(table_id)

    # Grupper linjer per prosedyre: sorter etter (name, line), konkatener tekst
    df_procedures = (
        df.sort_values(by=["name", "line"])
        .groupby("name")["text"]
        .apply(lambda x: "\n".join(x))
        .reset_index()
    )
    df_procedures.rename(columns={"name": "procedure_name", "text": "sql_script"}, inplace=True)
    
    if max_items:
        df_procedures = df_procedures.head(max_items)
        print(f"Begrenser til {max_items} prosedyrer for testing.")

    print(f"{len(df_procedures)} prosedyrer funnet.")

    if dry_run:
        print(f"[DRY RUN] Avbryter.")
        return

    # Last checkpoint
    completed, results = load_checkpoint(checkpoint_file)
    remaining = len(df_procedures) - len(completed)
    print(f"Analyserer {remaining} gjenstående prosedyrer...")

    run_start = time.perf_counter()

    for _, row in tqdm(df_procedures.iterrows(), total=len(df_procedures), desc=f"Prosedyrer ({schema})"):
        procedure_name = row["procedure_name"]

        if procedure_name in completed:
            continue

        prompt = PROMPT_TEMPLATE.format(sql_script=row["sql_script"])

        try:
            response_text = call_llm_with_retry(model, prompt)
            parsed = parse_llm_response(response_text)
            results.append({
                "procedure_name": procedure_name,
                "functionality": parsed.get("functionality", "N/A"),
                "data_sources": parsed.get("data_sources", []),
                "target_tables": parsed.get("target_tables", []),
            })
        except Exception as e:
            results.append({
                "procedure_name": procedure_name,
                "functionality": "Error during analysis",
                "data_sources": [],
                "target_tables": [],
                "error": str(e),
            })

        completed.add(procedure_name)

        if len(completed) % checkpoint_interval == 0:
            save_checkpoint(checkpoint_file, completed, results)
            elapsed = time.perf_counter() - run_start
            avg = elapsed / len(completed)
            print(f"  [CHECKPOINT] {len(completed)}/{len(df_procedures)} (snitt {avg:.1f}s per prosedyre)")

    # Lagre endelig resultat
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)
    print(f"Resultat lagret: {output_file}")

    cleanup_checkpoint(checkpoint_file)


def main():
    parser = argparse.ArgumentParser(description="Analyser Oracle-prosedyrer med Gemini")
    parser.add_argument(
        "--schema", "-s",
        nargs="+",
        required=True,
        help=f"Skjema(er) å analysere, eller 'all'. Gyldige: {', '.join(SCHEMAS.keys())}",
    )
    parser.add_argument("--output-dir", "-o", default=".", help="Mappe for output-filer")
    parser.add_argument("--checkpoint-interval", "-c", type=int, default=5, help="Lagre checkpoint hvert N. prosedyre")
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
        analyze_procedures(schema, model, args.output_dir, args.checkpoint_interval, args.dry_run, args.max_items)

    print("\nFerdig! " + str(len(schemas)) + " skjema(er) behandlet.")


if __name__ == "__main__":
    main()
