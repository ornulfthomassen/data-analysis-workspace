"""
analyze_centrality.py

Builds a NetworkX directed graph from the dependency data and computes
graph-theory centrality measures to identify the most important Oracle
database objects.

Reads:
    output/dependency_edges.json   — directed edges (source → target)
    output/parsed_objects.json     — node metadata (type, schema)

Output (in output/):
    centrality_analysis.json       — full centrality results

Usage:
    python analyze_centrality.py
"""

import json
from pathlib import Path

import networkx as nx

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "output"
EDGES_FILE = OUTPUT_DIR / "dependency_edges.json"
OBJECTS_FILE = OUTPUT_DIR / "parsed_objects.json"


# ---------------------------------------------------------------------------
# Graph construction
# ---------------------------------------------------------------------------

def build_nx_graph(objects: list[dict], edges: list[dict]) -> nx.DiGraph:
    """Build a NetworkX DiGraph from parsed objects and dependency edges."""
    G = nx.DiGraph()

    for obj in objects:
        G.add_node(
            obj["object_name"],
            object_type=obj.get("object_type", "unknown"),
            schema=obj.get("schema", ""),
        )

    for edge in edges:
        G.add_edge(
            edge["source"],
            edge["target"],
            linked_table=edge.get("linked_table", ""),
        )

    return G


# ---------------------------------------------------------------------------
# Centrality computation
# ---------------------------------------------------------------------------

def compute_centrality(G: nx.DiGraph) -> dict:
    """Compute all centrality measures and connected components."""

    in_deg = nx.in_degree_centrality(G)
    out_deg = nx.out_degree_centrality(G)
    betweenness = nx.betweenness_centrality(G)
    pagerank = nx.pagerank(G)

    # Eigenvector centrality on the undirected version (directed can fail to converge)
    G_undirected = G.to_undirected()
    try:
        eigenvector = nx.eigenvector_centrality(G_undirected, max_iter=1000)
    except nx.PowerIterationFailedConvergence:
        # Fall back to numpy-based method
        eigenvector = nx.eigenvector_centrality_numpy(G_undirected)

    # Weakly connected components
    components = sorted(nx.weakly_connected_components(G), key=len, reverse=True)

    # Map each node to its component id
    node_component: dict[str, int] = {}
    for comp_id, comp_nodes in enumerate(components):
        for node in comp_nodes:
            node_component[node] = comp_id

    # Build per-node centrality dict
    centrality: dict[str, dict] = {}
    for node in G.nodes:
        centrality[node] = {
            "in_degree": round(in_deg[node], 6),
            "out_degree": round(out_deg[node], 6),
            "betweenness": round(betweenness[node], 6),
            "pagerank": round(pagerank[node], 6),
            "eigenvector": round(eigenvector.get(node, 0.0), 6),
            "object_type": G.nodes[node].get("object_type", "unknown"),
            "schema": G.nodes[node].get("schema", ""),
            "component_id": node_component.get(node, -1),
        }

    # Top nodes per measure
    measures = ["in_degree", "out_degree", "betweenness", "pagerank", "eigenvector"]
    top_nodes: dict[str, list[dict]] = {}
    for measure in measures:
        ranked = sorted(centrality.items(), key=lambda x: x[1][measure], reverse=True)[:15]
        top_nodes[measure] = [
            {"object": name, "value": round(data[measure], 6),
             "object_type": data["object_type"], "schema": data["schema"]}
            for name, data in ranked
            if data[measure] > 0
        ]

    # Component summary
    component_list = [
        {"id": i, "size": len(comp), "schemas": sorted(set(
            G.nodes[n].get("schema", "") for n in comp
        ))}
        for i, comp in enumerate(components)
    ]

    summary = {
        "total_nodes": G.number_of_nodes(),
        "total_edges": G.number_of_edges(),
        "density": round(nx.density(G), 6),
        "weakly_connected_components": len(components),
        "largest_component_size": len(components[0]) if components else 0,
        "isolated_nodes": sum(1 for c in components if len(c) == 1),
    }

    return {
        "summary": summary,
        "components": component_list,
        "centrality": centrality,
        "top_nodes": top_nodes,
    }


# ---------------------------------------------------------------------------
# Terminal report
# ---------------------------------------------------------------------------

def print_report(result: dict) -> None:
    """Print a human-readable summary to the terminal."""
    s = result["summary"]

    print(f"\n{'=' * 70}")
    print(f"  NetworkX Centrality Analysis")
    print(f"{'=' * 70}")
    print(f"  Nodes                       : {s['total_nodes']}")
    print(f"  Edges                       : {s['total_edges']}")
    print(f"  Density                     : {s['density']}")
    print(f"  Weakly connected components : {s['weakly_connected_components']}")
    print(f"  Largest component           : {s['largest_component_size']} nodes")
    print(f"  Isolated nodes              : {s['isolated_nodes']}")

    # Per-schema summary
    schema_stats: dict[str, dict[str, float]] = {}
    for name, data in result["centrality"].items():
        schema = data["schema"]
        if schema not in schema_stats:
            schema_stats[schema] = {"count": 0, "pagerank_sum": 0.0, "betweenness_sum": 0.0}
        schema_stats[schema]["count"] += 1
        schema_stats[schema]["pagerank_sum"] += data["pagerank"]
        schema_stats[schema]["betweenness_sum"] += data["betweenness"]

    print(f"\n{'-' * 70}")
    print(f"  Per-schema aggregation:")
    print(f"  {'Schema':<20} {'Nodes':>6} {'PageRank sum':>14} {'Betweenness sum':>16}")
    print(f"  {'-'*20} {'-'*6} {'-'*14} {'-'*16}")
    for schema in sorted(schema_stats):
        ss = schema_stats[schema]
        print(f"  {schema:<20} {ss['count']:>6} {ss['pagerank_sum']:>14.4f} {ss['betweenness_sum']:>16.4f}")

    # Top nodes per measure
    measures = [
        ("in_degree", "Top 15 — In-Degree Centrality (most depended upon)"),
        ("out_degree", "Top 15 — Out-Degree Centrality (most dependencies)"),
        ("betweenness", "Top 15 — Betweenness Centrality (bridge/broker nodes)"),
        ("pagerank", "Top 15 — PageRank (importance by incoming links)"),
        ("eigenvector", "Top 15 — Eigenvector Centrality (connected to important nodes)"),
    ]

    for measure, title in measures:
        top = result["top_nodes"].get(measure, [])
        if not top:
            continue
        print(f"\n{'-' * 70}")
        print(f"  {title}")
        print(f"  {'Object':<50} {'Value':>10} {'Type':<12} {'Schema'}")
        print(f"  {'-'*50} {'-'*10} {'-'*12} {'-'*15}")
        for item in top:
            print(
                f"  {item['object']:<50} {item['value']:>10.6f} "
                f"{item['object_type']:<12} {item['schema']}"
            )

    # Largest components
    components = result["components"]
    non_trivial = [c for c in components if c["size"] > 1]
    print(f"\n{'-' * 70}")
    print(f"  Largest connected components (size > 1): {len(non_trivial)}")
    for comp in non_trivial[:10]:
        schemas = ", ".join(comp["schemas"])
        print(f"    Component {comp['id']}: {comp['size']} nodes  [{schemas}]")
    if len(non_trivial) > 10:
        print(f"    ... and {len(non_trivial) - 10} more")

    print(f"\n{'=' * 70}\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    for path, label in [(EDGES_FILE, "dependency_edges.json"), (OBJECTS_FILE, "parsed_objects.json")]:
        if not path.exists():
            print(f"ERROR: {label} not found at {path}")
            print("Run parse_analysis_files.py and build_dependency_graph.py first.")
            raise SystemExit(1)

    with EDGES_FILE.open(encoding="utf-8") as f:
        edges = json.load(f)

    with OBJECTS_FILE.open(encoding="utf-8") as f:
        parsed = json.load(f)

    objects = parsed.get("objects", [])
    print(f"Loaded {len(objects)} objects and {len(edges)} edges.")

    G = build_nx_graph(objects, edges)
    result = compute_centrality(G)

    # Write output
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / "centrality_analysis.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"Output written to: {out_path}")

    print_report(result)


if __name__ == "__main__":
    main()
