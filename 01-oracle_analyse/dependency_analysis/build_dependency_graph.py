"""
build_dependency_graph.py

Reads parsed_objects.json (produced by parse_analysis_files.py) and builds a
complete dependency graph showing how procedures and views are interconnected.

An edge A → B is created when:
  - Object A writes to table X  (A has table X in its target_tables)
  - Object B reads from table X (B has table X in its data_sources)

Usage:
    python build_dependency_graph.py [--include-temp]

Options:
    --include-temp   Include temporary tables when building edges.
                     By default, temporary tables are skipped because
                     they are internal to a single procedure.

Output (in output/):
    dependency_edges.json    — flat list of directed edges
    dependency_graph.json    — adjacency list (upstream/downstream per object)
    dependency_summary.json  — high-level statistics
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "output"
INPUT_FILE = OUTPUT_DIR / "parsed_objects.json"


# ---------------------------------------------------------------------------
# Graph builder
# ---------------------------------------------------------------------------

def build_graph(objects: list[dict], include_temp: bool = False) -> tuple[list[dict], dict]:
    """
    Build dependency edges from the parsed objects.

    Returns:
        edges   — list of edge dicts
        graph   — adjacency dict  {object_name: {upstream, downstream, type, schema}}
    """
    # Index objects by name for quick lookup
    obj_by_name: dict[str, dict] = {o["object_name"]: o for o in objects}

    # Map: table_name -> list of objects that WRITE to it (producers)
    producers: dict[str, list[str]] = defaultdict(list)
    for obj in objects:
        for t in obj.get("target_tables", []):
            if not include_temp and t.get("is_temporary"):
                continue
            producers[t["table_name"]].append(obj["object_name"])

    # Map: table_name -> list of objects that READ from it (consumers)
    consumers: dict[str, list[str]] = defaultdict(list)
    for obj in objects:
        for src in obj.get("data_sources", []):
            consumers[src].append(obj["object_name"])

    # Build edges: for each table that has at least one producer AND one consumer,
    # create an edge for every (producer, consumer) pair.
    edges: list[dict] = []
    seen_edges: set[tuple[str, str, str]] = set()

    for table_name, producer_list in producers.items():
        consumer_list = consumers.get(table_name, [])
        for producer in producer_list:
            for consumer in consumer_list:
                if producer == consumer:
                    # Self-loop (procedure reads from its own target table) — skip
                    continue
                key = (producer, consumer, table_name)
                if key in seen_edges:
                    continue
                seen_edges.add(key)

                producer_obj = obj_by_name.get(producer, {})
                consumer_obj = obj_by_name.get(consumer, {})

                edges.append({
                    "source": producer,
                    "target": consumer,
                    "linked_table": table_name,
                    "source_type": producer_obj.get("object_type", "unknown"),
                    "target_type": consumer_obj.get("object_type", "unknown"),
                })

    # Build adjacency list
    graph: dict[str, dict] = {}
    for obj in objects:
        graph[obj["object_name"]] = {
            "upstream": [],
            "downstream": [],
            "type": obj.get("object_type", "unknown"),
            "schema": obj.get("schema", ""),
        }

    for edge in edges:
        src = edge["source"]
        tgt = edge["target"]
        table = edge["linked_table"]
        if src in graph:
            graph[src]["downstream"].append({"object": tgt, "via_table": table})
        if tgt in graph:
            graph[tgt]["upstream"].append({"object": src, "via_table": table})

    return edges, graph


def build_summary(objects: list[dict], edges: list[dict], graph: dict) -> dict:
    """Compute high-level statistics about the dependency graph."""

    total_objects = len(objects)
    total_edges = len(edges)

    # Cross-schema edges: source schema != target schema
    cross_schema = 0
    for edge in edges:
        src_schema = edge["source"].split(".")[0] if "." in edge["source"] else ""
        tgt_schema = edge["target"].split(".")[0] if "." in edge["target"] else ""
        if src_schema and tgt_schema and src_schema != tgt_schema:
            cross_schema += 1

    # Isolated objects: no upstream and no downstream
    isolated = [
        name for name, data in graph.items()
        if not data["upstream"] and not data["downstream"]
    ]

    # Degree = number of unique upstream + downstream objects
    degree: dict[str, int] = {}
    for name, data in graph.items():
        up = len(set(e["object"] for e in data["upstream"]))
        down = len(set(e["object"] for e in data["downstream"]))
        degree[name] = up + down

    top_10 = sorted(degree.items(), key=lambda x: x[1], reverse=True)[:10]
    most_connected = [
        {
            "object": name,
            "degree": deg,
            "upstream_count": len(set(e["object"] for e in graph[name]["upstream"])),
            "downstream_count": len(set(e["object"] for e in graph[name]["downstream"])),
            "type": graph[name]["type"],
            "schema": graph[name]["schema"],
        }
        for name, deg in top_10
        if deg > 0
    ]

    # Type breakdown
    proc_count = sum(1 for o in objects if o.get("object_type") == "procedure")
    view_count = sum(1 for o in objects if o.get("object_type") == "view")

    # Schema breakdown
    schema_counts: dict[str, dict[str, int]] = defaultdict(lambda: {"procedures": 0, "views": 0})
    for obj in objects:
        schema = obj.get("schema", "UNKNOWN")
        obj_type = obj.get("object_type", "unknown")
        if obj_type == "procedure":
            schema_counts[schema]["procedures"] += 1
        elif obj_type == "view":
            schema_counts[schema]["views"] += 1

    return {
        "total_objects": total_objects,
        "procedures": proc_count,
        "views": view_count,
        "total_edges": total_edges,
        "cross_schema_edges": cross_schema,
        "isolated_objects_count": len(isolated),
        "isolated_objects": sorted(isolated),
        "most_connected_objects": most_connected,
        "objects_per_schema": {k: dict(v) for k, v in sorted(schema_counts.items())},
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    include_temp = "--include-temp" in sys.argv

    if not INPUT_FILE.exists():
        print(f"ERROR: Input file not found: {INPUT_FILE}")
        print("Run parse_analysis_files.py first.")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with INPUT_FILE.open(encoding="utf-8") as f:
        parsed = json.load(f)

    objects: list[dict] = parsed.get("objects", [])
    failed: list[dict] = parsed.get("failed", [])

    print(f"\nLoaded {len(objects)} successfully parsed objects "
          f"({len(failed)} skipped due to errors).")
    print(f"Temporary table edges: {'INCLUDED' if include_temp else 'EXCLUDED'} "
          f"(use --include-temp to change)\n")

    edges, graph = build_graph(objects, include_temp=include_temp)
    summary = build_summary(objects, edges, graph)

    # Write output files
    edges_path = OUTPUT_DIR / "dependency_edges.json"
    graph_path = OUTPUT_DIR / "dependency_graph.json"
    summary_path = OUTPUT_DIR / "dependency_summary.json"

    with edges_path.open("w", encoding="utf-8") as f:
        json.dump(edges, f, indent=2, ensure_ascii=False)

    with graph_path.open("w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)

    with summary_path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    # Print summary
    print(f"{'=' * 60}")
    print(f"  Dependency Graph — Summary")
    print(f"{'=' * 60}")
    print(f"  Total objects          : {summary['total_objects']}")
    print(f"    Procedures           : {summary['procedures']}")
    print(f"    Views                : {summary['views']}")
    print(f"  Total edges            : {summary['total_edges']}")
    print(f"  Cross-schema edges     : {summary['cross_schema_edges']}")
    print(f"  Isolated objects       : {summary['isolated_objects_count']}")
    print(f"{'-' * 60}")
    print(f"  Objects per schema:")
    for schema, counts in summary["objects_per_schema"].items():
        print(f"    {schema:<20} procedures={counts['procedures']}, views={counts['views']}")
    print(f"{'-' * 60}")
    if summary["most_connected_objects"]:
        print(f"  Top 10 most connected objects (by degree):")
        for item in summary["most_connected_objects"]:
            print(
                f"    {item['object']:<50} "
                f"degree={item['degree']:>3}  "
                f"(↑{item['upstream_count']} ↓{item['downstream_count']})  "
                f"[{item['type']}]"
            )
    print(f"{'=' * 60}")
    print(f"\nOutput files written to: {OUTPUT_DIR}")
    print(f"  {edges_path.name}")
    print(f"  {graph_path.name}")
    print(f"  {summary_path.name}\n")


if __name__ == "__main__":
    main()
