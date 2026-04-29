"""
load_to_spanner.py

Leser dependency analysis-output (parsed_objects.json, dependency_edges.json)
og laster noder og kanter inn i Spanner-tabellene OracleObjects og Dependencies.

Forutsetter at tabellene allerede er opprettet (se spanner_ddl.sql).

Usage:
    python load_to_spanner.py [--clear]

Options:
    --clear   Slett eksisterende data før lasting (DELETE FROM Dependencies, DELETE FROM OracleObjects)
"""

import json
import sys
from pathlib import Path

from google.cloud import spanner

# ---------------------------------------------------------------------------
# Spanner-konfigurasjon
# ---------------------------------------------------------------------------
SPANNER_PROJECT = "tnn-nova-spanner"
SPANNER_INSTANCE = "nova-eu-west1-01"
SPANNER_DATABASE = "s07601-p-tnn-consumer"

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "output"
PARSED_OBJECTS_FILE = OUTPUT_DIR / "parsed_objects.json"
EDGES_FILE = OUTPUT_DIR / "dependency_edges.json"

# Spanner batch insert limit
BATCH_SIZE = 500


def load_data():
    """Last parsed objects og edges fra JSON-filer."""
    with PARSED_OBJECTS_FILE.open(encoding="utf-8") as f:
        parsed = json.load(f)
    objects = parsed.get("objects", [])

    with EDGES_FILE.open(encoding="utf-8") as f:
        edges = json.load(f)

    return objects, edges


def clear_tables(database):
    """Slett alle rader (edges først pga. interleaving)."""
    def delete_all(transaction):
        transaction.execute_update("DELETE FROM Dependencies WHERE true")
        transaction.execute_update("DELETE FROM OracleObjects WHERE true")

    database.run_in_transaction(delete_all)
    print("Eksisterende data slettet.")


def insert_objects(database, objects):
    """Sett inn noder (OracleObjects) i batches."""
    rows = []
    for obj in objects:
        rows.append((
            obj["object_name"],
            obj.get("object_type", ""),
            obj.get("schema", ""),
            obj.get("functionality", ""),
        ))

    columns = ("object_name", "object_type", "schema_name", "functionality")
    total = len(rows)
    inserted = 0

    for i in range(0, total, BATCH_SIZE):
        batch = rows[i:i + BATCH_SIZE]
        with database.batch() as batcher:
            batcher.insert(
                table="OracleObjects",
                columns=columns,
                values=batch,
            )
        inserted += len(batch)
        print(f"  OracleObjects: {inserted}/{total}")

    print(f"  {total} noder lastet inn.")


def insert_edges(database, edges):
    """Sett inn kanter (Dependencies) i batches."""
    rows = []
    for edge in edges:
        rows.append((
            edge["source"],
            edge["target"],
            edge["linked_table"],
            edge.get("source_type", ""),
            edge.get("target_type", ""),
        ))

    columns = ("object_name", "target_object", "linked_table", "source_type", "target_type")
    total = len(rows)
    inserted = 0

    for i in range(0, total, BATCH_SIZE):
        batch = rows[i:i + BATCH_SIZE]
        with database.batch() as batcher:
            batcher.insert(
                table="Dependencies",
                columns=columns,
                values=batch,
            )
        inserted += len(batch)
        print(f"  Dependencies: {inserted}/{total}")

    print(f"  {total} kanter lastet inn.")


def main():
    clear_first = "--clear" in sys.argv

    if not PARSED_OBJECTS_FILE.exists() or not EDGES_FILE.exists():
        print("ERROR: Kjør parse_analysis_files.py og build_dependency_graph.py først.")
        sys.exit(1)

    objects, edges = load_data()
    print(f"Lastet {len(objects)} noder og {len(edges)} kanter fra JSON.")

    client = spanner.Client(project=SPANNER_PROJECT)
    instance = client.instance(SPANNER_INSTANCE)
    database = instance.database(SPANNER_DATABASE)

    if clear_first:
        clear_tables(database)

    print("\nLaster noder...")
    insert_objects(database, objects)

    print("\nLaster kanter...")
    insert_edges(database, edges)

    print(f"\nFerdig! Data lastet inn i {SPANNER_DATABASE}.")
    print("Åpne Spanner Studio og kjør GQL-spørringer for å visualisere grafen.")


if __name__ == "__main__":
    main()
