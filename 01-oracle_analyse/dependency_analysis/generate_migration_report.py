"""
generate_migration_report.py

Generates a Markdown migration report for rebuilding Oracle database objects
as dbt models in GCP. Uses NetworkX for topological sorting and layer assignment.

Reads:
    output/parsed_objects.json       — node metadata
    output/dependency_edges.json     — directed edges
    output/centrality_analysis.json  — centrality measures

Output:
    output/migration_report.md       — complete migration report

Usage:
    python generate_migration_report.py
"""

import json
from collections import defaultdict
from pathlib import Path

import networkx as nx

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "output"
OBJECTS_FILE = OUTPUT_DIR / "parsed_objects.json"
EDGES_FILE = OUTPUT_DIR / "dependency_edges.json"
CENTRALITY_FILE = OUTPUT_DIR / "centrality_analysis.json"
REPORT_FILE = OUTPUT_DIR / "migration_report.md"


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_data() -> tuple[list[dict], list[dict], dict]:
    with OBJECTS_FILE.open(encoding="utf-8") as f:
        parsed = json.load(f)
    with EDGES_FILE.open(encoding="utf-8") as f:
        edges = json.load(f)
    with CENTRALITY_FILE.open(encoding="utf-8") as f:
        centrality = json.load(f)
    return parsed.get("objects", []), edges, centrality


# ---------------------------------------------------------------------------
# Analysis functions
# ---------------------------------------------------------------------------

def find_external_sources(objects: list[dict]) -> dict[str, list[str]]:
    """Find tables referenced as data_sources that are not analysed objects or target tables."""
    object_names = set(o["object_name"] for o in objects)

    all_targets = set()
    for o in objects:
        for t in o.get("target_tables", []):
            all_targets.add(t["table_name"])

    all_sources = set()
    for o in objects:
        all_sources.update(o.get("data_sources", []))

    external = all_sources - object_names - all_targets

    by_schema: dict[str, list[str]] = defaultdict(list)
    for s in sorted(external):
        schema = s.split(".")[0] if "." in s else "UNKNOWN"
        by_schema[schema].append(s)
    return dict(sorted(by_schema.items(), key=lambda x: -len(x[1])))


def build_graph_and_layers(objects: list[dict], edges: list[dict]) -> tuple[nx.DiGraph, list[list[str]], list[list[tuple]]]:
    """Build DiGraph, compute topological layers, detect cycles."""
    G = nx.DiGraph()
    for obj in objects:
        G.add_node(obj["object_name"], object_type=obj.get("object_type", "unknown"),
                    schema=obj.get("schema", ""))
    for edge in edges:
        G.add_edge(edge["source"], edge["target"], linked_table=edge.get("linked_table", ""))

    cycles: list[list[tuple]] = []
    while not nx.is_directed_acyclic_graph(G):
        try:
            cycle = nx.find_cycle(G)
            cycles.append(cycle)
            # Remove one edge from the cycle to break it
            u, v, *_ = cycle[0]
            if G.has_edge(u, v):
                G.remove_edge(u, v)
        except nx.NetworkXNoCycle:
            break

    layers: list[list[str]] = []
    for generation in nx.topological_generations(G):
        layers.append(sorted(generation))

    return G, layers, cycles


def cross_schema_matrix(edges: list[dict]) -> dict[str, dict[str, int]]:
    """Build a schema-to-schema edge count matrix."""
    schemas = set()
    counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for edge in edges:
        src_s = edge["source"].split(".")[0] if "." in edge["source"] else ""
        tgt_s = edge["target"].split(".")[0] if "." in edge["target"] else ""
        if src_s and tgt_s:
            schemas.add(src_s)
            schemas.add(tgt_s)
            counts[src_s][tgt_s] += 1
    return {s: dict(counts[s]) for s in sorted(schemas)}


def classify_nodes(G: nx.DiGraph) -> dict[str, list[str]]:
    """Classify nodes by their role in the graph."""
    isolated = sorted(n for n in G.nodes if G.in_degree(n) == 0 and G.out_degree(n) == 0)
    roots = sorted(n for n in G.nodes if G.in_degree(n) == 0 and G.out_degree(n) > 0)
    leaves = sorted(n for n in G.nodes if G.out_degree(n) == 0 and G.in_degree(n) > 0)
    intermediate = sorted(n for n in G.nodes if G.in_degree(n) > 0 and G.out_degree(n) > 0)
    return {"isolated": isolated, "roots": roots, "leaves": leaves, "intermediate": intermediate}


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(objects: list[dict], edges: list[dict], centrality: dict) -> str:
    obj_by_name = {o["object_name"]: o for o in objects}
    G, layers, cycles = build_graph_and_layers(objects, edges)
    external_sources = find_external_sources(objects)
    schema_matrix = cross_schema_matrix(edges)
    classification = classify_nodes(G)
    cent_data = centrality.get("centrality", {})
    summary = centrality.get("summary", {})
    components = centrality.get("components", [])
    top_nodes = centrality.get("top_nodes", {})

    lines: list[str] = []

    def h1(text: str) -> None:
        lines.append(f"\n# {text}\n")

    def h2(text: str) -> None:
        lines.append(f"\n## {text}\n")

    def h3(text: str) -> None:
        lines.append(f"\n### {text}\n")

    def p(text: str) -> None:
        lines.append(f"{text}\n")

    # ---- 1. Summary ----
    h1("Oracle → dbt Migrasjonsrapport")

    p("Denne rapporten er auto-generert fra avhengighetsanalysen av Oracle-databaseobjekter "
      "i skjemaene CCM, CLM_ADM, CLM_CCM og CRM_ANALYSE. Formålet er å gi utviklerteamet "
      "en konkret plan for å gjenskape disse objektene som dbt-modeller i GCP.")

    h2("1. Oppsummering")

    total_ext = sum(len(v) for v in external_sources.values())
    p(f"| Metrikk | Verdi |")
    p(f"|:--------|------:|")
    p(f"| Totalt analyserte objekter | {len(objects)} |")
    p(f"| Prosedyrer | {sum(1 for o in objects if o.get('object_type') == 'procedure')} |")
    p(f"| Views | {sum(1 for o in objects if o.get('object_type') == 'view')} |")
    p(f"| Avhengighetskanter | {len(edges)} |")
    p(f"| Kryss-skjema-kanter | {sum(1 for e in edges if e['source'].split('.')[0] != e['target'].split('.')[0])} |")
    p(f"| Tilkoblede komponenter (weakly) | {summary.get('weakly_connected_components', 'N/A')} |")
    p(f"| Største komponent | {summary.get('largest_component_size', 'N/A')} noder |")
    p(f"| Isolerte objekter (ingen avhengigheter) | {len(classification['isolated'])} |")
    p(f"| Eksterne kildetabeller (dbt sources) | {total_ext} |")
    p(f"| Graftetthet | {summary.get('density', 'N/A')} |")

    h3("Roller i grafen")
    p(f"| Rolle | Antall | Beskrivelse |")
    p(f"|:------|-------:|:------------|")
    p(f"| Root-noder | {len(classification['roots'])} | Kun utgående kanter — leser fra eksterne kilder, skriver til interne tabeller |")
    p(f"| Mellomliggende | {len(classification['intermediate'])} | Både inn- og utgående kanter — transformasjonsledd |")
    p(f"| Bladnoder (leaf) | {len(classification['leaves'])} | Kun innkommende kanter — sluttbrukere av data |")
    p(f"| Isolerte | {len(classification['isolated'])} | Ingen kanter i avhengighetsgrafen |")

    # ---- 2. External sources ----
    h2("2. Eksterne kildetabeller (dbt sources)")

    p(f"Totalt **{total_ext}** tabeller refereres som datakilder men finnes ikke blant de "
      f"analyserte objektene. Disse må defineres som `source()` i dbt.\n")

    p(f"| Skjema | Antall tabeller |")
    p(f"|:-------|----------------:|")
    for schema, tables in external_sources.items():
        p(f"| {schema} | {len(tables)} |")

    # Show details for top schemas
    for schema, tables in list(external_sources.items())[:10]:
        h3(f"{schema} ({len(tables)} tabeller)")
        for t in tables:
            p(f"- `{t}`")

    if len(external_sources) > 10:
        remaining = list(external_sources.items())[10:]
        h3(f"Øvrige skjemaer ({len(remaining)} stk)")
        for schema, tables in remaining:
            p(f"- **{schema}**: {', '.join(f'`{t}`' for t in tables)}")

    # ---- 3. Topological build order ----
    h2("3. Topologisk bygge-rekkefølge")

    if cycles:
        p("**Advarsel: Sykler ble funnet i avhengighetsgrafen.** "
          "Følgende sykliske kanter ble midlertidig fjernet for å muliggjøre topologisk sortering. "
          "Utviklerteamet må bestemme rekkefølge manuelt for disse.\n")
        for cycle in cycles:
            p("Syklus:")
            for u, v, *_ in cycle:
                p(f"  - `{u}` → `{v}`")
        p("")

    p(f"Grafen er delt inn i **{len(layers)} lag** (tiers). Lag 0 har ingen interne avhengigheter "
      f"og bør bygges først. Hvert påfølgende lag avhenger kun av foregående lag.\n")

    # Summary table per layer
    p(f"| Lag | Antall objekter | Prosedyrer | Views | Skjemaer |")
    p(f"|----:|----------------:|-----------:|------:|:---------|")
    for i, layer in enumerate(layers):
        procs = sum(1 for n in layer if obj_by_name.get(n, {}).get("object_type") == "procedure")
        views = sum(1 for n in layer if obj_by_name.get(n, {}).get("object_type") == "view")
        schemas = sorted(set(obj_by_name.get(n, {}).get("schema", "") for n in layer))
        p(f"| {i} | {len(layer)} | {procs} | {views} | {', '.join(schemas)} |")

    # Detailed listing for non-trivial layers (skip the massive isolated layer)
    connected_layers = [(i, layer) for i, layer in enumerate(layers)
                        if any(G.in_degree(n) > 0 or G.out_degree(n) > 0 for n in layer)]

    for i, layer in connected_layers:
        h3(f"Lag {i} ({len(layer)} objekter)")

        # Only show objects that have edges
        active = [n for n in layer if G.in_degree(n) > 0 or G.out_degree(n) > 0]
        if len(active) > 50:
            p(f"*{len(active)} tilkoblede objekter — viser topp 30 etter downstream-antall:*\n")
            active = sorted(active, key=lambda n: G.out_degree(n), reverse=True)[:30]

        p(f"| Objekt | Type | Skjema | Upstream | Downstream |")
        p(f"|:-------|:-----|:-------|--------:|-----------:|")
        for n in active:
            obj = obj_by_name.get(n, {})
            p(f"| `{n}` | {obj.get('object_type', '?')} | {obj.get('schema', '?')} "
              f"| {G.in_degree(n)} | {G.out_degree(n)} |")

    # ---- 4. Critical objects ----
    h2("4. Kritiske objekter — prioriteringsliste")

    p("Disse objektene bør prioriteres i migreringen fordi de er sentrale knutepunkter i avhengighetsgrafen.\n")

    h3("4.1 Broker-noder (betweenness centrality)")
    p("Noder som binder sammen de ulike delene av grafen. Hvis disse mangler, vil mange "
      "nedstrøms objekter bryte.\n")

    betweenness_top = top_nodes.get("betweenness", [])[:20]
    if betweenness_top:
        p(f"| # | Objekt | Betweenness | Type | Skjema |")
        p(f"|--:|:-------|------------:|:-----|:-------|")
        for rank, item in enumerate(betweenness_top, 1):
            p(f"| {rank} | `{item['object']}` | {item['value']:.6f} | {item['object_type']} | {item['schema']} |")

    h3("4.2 Fan-out-noder (out-degree centrality)")
    p("Noder med flest nedstrøms avhengigheter — mange andre objekter avhenger av disse.\n")

    out_degree_top = top_nodes.get("out_degree", [])[:20]
    if out_degree_top:
        p(f"| # | Objekt | Out-degree | Downstream | Type | Skjema |")
        p(f"|--:|:-------|----------:|----------:|:-----|:-------|")
        for rank, item in enumerate(out_degree_top, 1):
            node_data = cent_data.get(item["object"], {})
            downstream = G.out_degree(item["object"]) if item["object"] in G else 0
            p(f"| {rank} | `{item['object']}` | {item['value']:.6f} | {downstream} "
              f"| {item['object_type']} | {item['schema']} |")

    h3("4.3 PageRank — viktigste noder")
    p("Noder som er viktige basert på hvem som peker på dem (rekursivt).\n")

    pagerank_top = top_nodes.get("pagerank", [])[:20]
    if pagerank_top:
        p(f"| # | Objekt | PageRank | Type | Skjema |")
        p(f"|--:|:-------|--------:|:-----|:-------|")
        for rank, item in enumerate(pagerank_top, 1):
            p(f"| {rank} | `{item['object']}` | {item['value']:.6f} | {item['object_type']} | {item['schema']} |")

    # ---- 5. Objects to skip ----
    h2("5. Objekter som kan utelates fra migrering")

    p(f"**{len(classification['isolated'])}** objekter har ingen kjente avhengighets-kanter "
      f"i analysen. Disse kan potensielt utelates fra migreringen, men bør verifiseres "
      f"mot faktisk bruk (rapporter, applikasjoner, ad-hoc-spørringer).\n")

    h3("5.1 Isolerte objekter per skjema")

    iso_by_schema: dict[str, dict[str, int]] = defaultdict(lambda: {"procedures": 0, "views": 0})
    for n in classification["isolated"]:
        obj = obj_by_name.get(n, {})
        schema = obj.get("schema", "UNKNOWN")
        obj_type = obj.get("object_type", "unknown")
        if obj_type == "procedure":
            iso_by_schema[schema]["procedures"] += 1
        else:
            iso_by_schema[schema]["views"] += 1

    p(f"| Skjema | Isolerte prosedyrer | Isolerte views | Totalt |")
    p(f"|:-------|-------------------:|---------------:|-------:|")
    for schema in sorted(iso_by_schema):
        d = iso_by_schema[schema]
        p(f"| {schema} | {d['procedures']} | {d['views']} | {d['procedures'] + d['views']} |")

    h3("5.2 Bladnoder (leaf) — ingen leser fra disse")
    p(f"**{len(classification['leaves'])}** objekter har innkommende kanter men ingen utgående. "
      f"De er siste ledd i datakjeden — typisk rapporterings-views. De er nødvendige hvis de "
      f"brukes direkte, men bør deprioriteres i migrering.\n")

    leaf_by_schema: dict[str, int] = defaultdict(int)
    for n in classification["leaves"]:
        schema = obj_by_name.get(n, {}).get("schema", "UNKNOWN")
        leaf_by_schema[schema] += 1

    p(f"| Skjema | Antall bladnoder |")
    p(f"|:-------|----------------:|")
    for schema in sorted(leaf_by_schema):
        p(f"| {schema} | {leaf_by_schema[schema]} |")

    # ---- 6. Cross-schema dependencies ----
    h2("6. Kryss-skjema-avhengigheter")

    p("Avhengighetsmatrise — antall kanter fra rad-skjema til kolonne-skjema:\n")

    all_schemas = sorted(set(
        list(schema_matrix.keys()) +
        [s for d in schema_matrix.values() for s in d]
    ))

    header = "| Fra \\ Til | " + " | ".join(all_schemas) + " |"
    sep = "|:---------|" + "|".join("-" * (len(s) + 2) for s in all_schemas) + "|"
    p(header)
    p(sep)
    for src in all_schemas:
        row = f"| **{src}** |"
        for tgt in all_schemas:
            count = schema_matrix.get(src, {}).get(tgt, 0)
            row += f" {count if count > 0 else '-'} |"
        p(row)

    # ---- 7. Connected components ----
    h2("7. Tilkoblede komponenter")

    non_trivial = [c for c in components if c["size"] > 1]
    p(f"Totalt **{len(components)}** weakly connected components, hvorav "
      f"**{len(non_trivial)}** har mer enn 1 node.\n")

    h3("7.1 Hovedkomponenten")
    if components:
        main = components[0]
        p(f"Komponent 0 inneholder **{main['size']} noder** og spenner skjemaene "
          f"**{', '.join(main.get('schemas', []))}**. Denne er kjernen i avhengighetsgrafen "
          f"og må migreres samlet i riktig rekkefølge.\n")

    h3("7.2 Uavhengige komponenter")
    p("Disse komponentene kan migreres uavhengig av hverandre og av hovedkomponenten:\n")

    if len(non_trivial) > 1:
        p(f"| Komponent | Størrelse | Skjemaer |")
        p(f"|----------:|---------:|:---------|")
        for comp in non_trivial[1:]:
            schemas = ", ".join(comp.get("schemas", []))
            p(f"| {comp['id']} | {comp['size']} | {schemas} |")

    # ---- 8. Recommended migration phases ----
    h2("8. Anbefalt migreringsstrategi")

    p("Basert på analysen anbefales følgende faser:\n")

    p("### Fase 0: Oppsett")
    p(f"- Definer **{total_ext}** kildetabeller som `source()` i dbt")
    p(f"- Opprett dbt-prosjektstruktur med skjemamapping for {', '.join(all_schemas)}\n")

    p("### Fase 1: Root-noder (lag 0)")
    p(f"- Migrer **{len(classification['roots'])}** root-prosedyrer som kun leser fra eksterne kilder")
    p(f"- Disse har ingen interne avhengigheter og kan bygges umiddelbart\n")

    p("### Fase 2: Kritisk infrastruktur")
    p(f"- Migrer de **5 hub-prosedyrene** i CLM_ADM som til sammen har 88-116 nedstrøms avhengigheter")
    p("- Viktigst: `CLM_ADM.P_RDM_CUSTOMER_MAPPING`, `CLM_ADM.P_ADM_SUBSCRIPTION_MASTER_HIST`\n")

    p("### Fase 3: Mellomliggende lag")
    p(f"- Migrer lag 1–{len(layers)-1} sekvensielt")
    p("- Hvert lag kan internt bygges parallelt\n")

    p("### Fase 4: Bladnoder og rapporterings-views")
    p(f"- Migrer **{len(classification['leaves'])}** bladnoder etter behov")
    p("- Prioriter basert på faktisk bruk\n")

    p("### Valgfritt: Isolerte objekter")
    p(f"- **{len(classification['isolated'])}** isolerte objekter migreres kun hvis de har kjent bruk")
    p("- Krever manuell gjennomgang for å avgjøre om de er i aktiv bruk\n")

    # Add generation timestamp
    from datetime import datetime
    p(f"\n---\n*Rapport generert: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    for path, label in [
        (OBJECTS_FILE, "parsed_objects.json"),
        (EDGES_FILE, "dependency_edges.json"),
        (CENTRALITY_FILE, "centrality_analysis.json"),
    ]:
        if not path.exists():
            print(f"ERROR: {label} not found at {path}")
            raise SystemExit(1)

    objects, edges, centrality = load_data()
    print(f"Loaded {len(objects)} objects, {len(edges)} edges.")

    report = generate_report(objects, edges, centrality)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text(report, encoding="utf-8")
    print(f"Migration report written to: {REPORT_FILE}")
    print(f"Report size: {len(report):,} characters")


if __name__ == "__main__":
    main()
