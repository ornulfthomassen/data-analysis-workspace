"""
generate_triage_table.py

Generates an interactive HTML table for developers to triage Oracle database
objects — identifying which should be migrated to dbt, evaluated, or skipped.

Reads:
    output/parsed_objects.json       — node metadata
    output/dependency_edges.json     — directed edges
    output/centrality_analysis.json  — centrality measures

Output:
    output/triage_table.html         — interactive filterable HTML table

Usage:
    python generate_triage_table.py
"""

import json
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
HTML_FILE = OUTPUT_DIR / "triage_table.html"


# ---------------------------------------------------------------------------
# Data loading & analysis
# ---------------------------------------------------------------------------

def load_and_analyse() -> list[dict]:
    with OBJECTS_FILE.open(encoding="utf-8") as f:
        objects = json.load(f).get("objects", [])
    with EDGES_FILE.open(encoding="utf-8") as f:
        edges = json.load(f)
    with CENTRALITY_FILE.open(encoding="utf-8") as f:
        centrality = json.load(f)

    cent_data = centrality.get("centrality", {})

    # Build graph for topology
    G = nx.DiGraph()
    for obj in objects:
        G.add_node(obj["object_name"])
    for edge in edges:
        G.add_edge(edge["source"], edge["target"])

    # Break cycles for layer computation
    while not nx.is_directed_acyclic_graph(G):
        try:
            cycle = nx.find_cycle(G)
            u, v, *_ = cycle[0]
            if G.has_edge(u, v):
                G.remove_edge(u, v)
        except nx.NetworkXNoCycle:
            break

    # Compute layers
    node_layer: dict[str, int] = {}
    for layer_num, generation in enumerate(nx.topological_generations(G)):
        for node in generation:
            node_layer[node] = layer_num

    # Build rows
    rows = []
    for obj in objects:
        name = obj["object_name"]
        in_deg = G.in_degree(name) if name in G else 0
        out_deg = G.out_degree(name) if name in G else 0
        cd = cent_data.get(name, {})

        # Classification
        if in_deg == 0 and out_deg == 0:
            role = "Isolert"
            recommendation = "SKIP"
        elif in_deg == 0 and out_deg > 0:
            role = "Root"
            recommendation = "MIGRATE"
        elif out_deg == 0 and in_deg > 0:
            role = "Leaf"
            recommendation = "EVALUATE"
        else:
            role = "Intermediate"
            recommendation = "MIGRATE"

        rows.append({
            "object_name": name,
            "object_type": obj.get("object_type", ""),
            "schema": obj.get("schema", ""),
            "role": role,
            "recommendation": recommendation,
            "upstream": in_deg,
            "downstream": out_deg,
            "layer": node_layer.get(name, -1),
            "component": cd.get("component_id", -1),
            "betweenness": cd.get("betweenness", 0),
            "pagerank": cd.get("pagerank", 0),
            "functionality": obj.get("functionality", "").replace('"', "&quot;").replace("<", "&lt;"),
        })

    # Sort: MIGRATE first, then EVALUATE, then SKIP; within each by downstream desc
    order = {"MIGRATE": 0, "EVALUATE": 1, "SKIP": 2}
    rows.sort(key=lambda r: (order.get(r["recommendation"], 9), -r["downstream"], r["object_name"]))
    return rows


# ---------------------------------------------------------------------------
# HTML generation
# ---------------------------------------------------------------------------

def generate_html(rows: list[dict]) -> str:
    counts = {"MIGRATE": 0, "EVALUATE": 0, "SKIP": 0}
    for r in rows:
        counts[r["recommendation"]] = counts.get(r["recommendation"], 0) + 1

    rows_json = json.dumps(rows, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="no">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Oracle → dbt Triage</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
         background: #f8f9fa; color: #1a1a2e; padding: 20px; }}
  h1 {{ font-size: 1.5rem; margin-bottom: 4px; }}
  .subtitle {{ color: #666; font-size: 0.9rem; margin-bottom: 16px; }}
  .controls {{ display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 16px; align-items: center; }}
  .controls input, .controls select {{
    padding: 6px 10px; border: 1px solid #ccc; border-radius: 6px; font-size: 0.85rem;
  }}
  .controls input {{ width: 260px; }}
  .badge {{ display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 0.75rem;
            font-weight: 600; text-transform: uppercase; letter-spacing: 0.03em; }}
  .badge-migrate {{ background: #d4edda; color: #155724; }}
  .badge-evaluate {{ background: #fff3cd; color: #856404; }}
  .badge-skip {{ background: #f8d7da; color: #721c24; }}
  .summary {{ display: flex; gap: 12px; margin-bottom: 16px; flex-wrap: wrap; }}
  .summary-card {{ background: #fff; border-radius: 8px; padding: 12px 18px; box-shadow: 0 1px 3px rgba(0,0,0,.08);
                   min-width: 140px; }}
  .summary-card .num {{ font-size: 1.6rem; font-weight: 700; }}
  .summary-card .label {{ font-size: 0.8rem; color: #666; }}
  table {{ width: 100%; border-collapse: collapse; background: #fff; border-radius: 8px;
           overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,.08); font-size: 0.82rem; }}
  thead {{ position: sticky; top: 0; z-index: 1; }}
  th {{ background: #16213e; color: #fff; text-align: left; padding: 10px 8px; cursor: pointer;
       user-select: none; white-space: nowrap; }}
  th:hover {{ background: #1a1a4e; }}
  th .arrow {{ font-size: 0.7rem; margin-left: 4px; }}
  td {{ padding: 7px 8px; border-bottom: 1px solid #eee; vertical-align: top; }}
  tr:hover {{ background: #f0f4ff; }}
  .func-cell {{ max-width: 350px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
                cursor: pointer; }}
  .func-cell.expanded {{ white-space: normal; }}
  .num-cell {{ text-align: right; font-variant-numeric: tabular-nums; }}
  .count-label {{ font-size: 0.8rem; color: #666; margin-left: 6px; }}
  .export-btn {{ padding: 6px 14px; background: #16213e; color: #fff; border: none;
                 border-radius: 6px; cursor: pointer; font-size: 0.85rem; }}
  .export-btn:hover {{ background: #1a1a4e; }}
</style>
</head>
<body>

<h1>Oracle → dbt Triage</h1>
<p class="subtitle">Interaktiv oversikt for å avgjøre hvilke objekter som skal migreres til dbt. Klikk på rader for å utvide beskrivelsen.</p>

<div class="summary">
  <div class="summary-card"><div class="num">{len(rows)}</div><div class="label">Totalt</div></div>
  <div class="summary-card"><div class="num" style="color:#155724">{counts["MIGRATE"]}</div><div class="label">Migrate</div></div>
  <div class="summary-card"><div class="num" style="color:#856404">{counts["EVALUATE"]}</div><div class="label">Evaluate</div></div>
  <div class="summary-card"><div class="num" style="color:#721c24">{counts["SKIP"]}</div><div class="label">Skip</div></div>
</div>

<div class="controls">
  <input type="text" id="search" placeholder="Sok (objektnavn, skjema, beskrivelse)...">
  <select id="filterRec">
    <option value="">Alle anbefalinger</option>
    <option value="MIGRATE">MIGRATE</option>
    <option value="EVALUATE">EVALUATE</option>
    <option value="SKIP">SKIP</option>
  </select>
  <select id="filterSchema">
    <option value="">Alle skjemaer</option>
    <option value="CCM">CCM</option>
    <option value="CLM_ADM">CLM_ADM</option>
    <option value="CLM_CCM">CLM_CCM</option>
    <option value="CRM_ANALYSE">CRM_ANALYSE</option>
  </select>
  <select id="filterType">
    <option value="">Alle typer</option>
    <option value="procedure">Prosedyre</option>
    <option value="view">View</option>
  </select>
  <select id="filterRole">
    <option value="">Alle roller</option>
    <option value="Root">Root</option>
    <option value="Intermediate">Intermediate</option>
    <option value="Leaf">Leaf</option>
    <option value="Isolert">Isolert</option>
  </select>
  <button class="export-btn" onclick="exportCSV()">Eksporter CSV</button>
  <span id="rowCount" class="count-label"></span>
</div>

<table>
<thead>
<tr>
  <th data-col="object_name">Objekt <span class="arrow"></span></th>
  <th data-col="object_type">Type <span class="arrow"></span></th>
  <th data-col="schema">Skjema <span class="arrow"></span></th>
  <th data-col="role">Rolle <span class="arrow"></span></th>
  <th data-col="recommendation">Anbefaling <span class="arrow"></span></th>
  <th data-col="upstream">Upstream <span class="arrow"></span></th>
  <th data-col="downstream">Downstream <span class="arrow"></span></th>
  <th data-col="layer">Lag <span class="arrow"></span></th>
  <th data-col="betweenness">Betweenness <span class="arrow"></span></th>
  <th data-col="pagerank">PageRank <span class="arrow"></span></th>
  <th data-col="functionality">Beskrivelse <span class="arrow"></span></th>
</tr>
</thead>
<tbody id="tbody"></tbody>
</table>

<script>
const allRows = {rows_json};
let sortCol = null, sortAsc = true;

function badgeClass(rec) {{
  return rec === 'MIGRATE' ? 'badge-migrate' : rec === 'EVALUATE' ? 'badge-evaluate' : 'badge-skip';
}}

function render(data) {{
  const tbody = document.getElementById('tbody');
  tbody.innerHTML = data.map(r => `<tr>
    <td><strong>${{r.object_name}}</strong></td>
    <td>${{r.object_type}}</td>
    <td>${{r.schema}}</td>
    <td>${{r.role}}</td>
    <td><span class="badge ${{badgeClass(r.recommendation)}}">${{r.recommendation}}</span></td>
    <td class="num-cell">${{r.upstream}}</td>
    <td class="num-cell">${{r.downstream}}</td>
    <td class="num-cell">${{r.layer === -1 ? '-' : r.layer}}</td>
    <td class="num-cell">${{r.betweenness > 0 ? r.betweenness.toFixed(6) : '-'}}</td>
    <td class="num-cell">${{r.pagerank.toFixed(6)}}</td>
    <td class="func-cell" onclick="this.classList.toggle('expanded')">${{r.functionality || '-'}}</td>
  </tr>`).join('');
  document.getElementById('rowCount').textContent = `${{data.length}} av ${{allRows.length}} objekter`;
}}

function getFiltered() {{
  const q = document.getElementById('search').value.toLowerCase();
  const rec = document.getElementById('filterRec').value;
  const schema = document.getElementById('filterSchema').value;
  const type = document.getElementById('filterType').value;
  const role = document.getElementById('filterRole').value;
  let data = allRows.filter(r => {{
    if (rec && r.recommendation !== rec) return false;
    if (schema && r.schema !== schema) return false;
    if (type && r.object_type !== type) return false;
    if (role && r.role !== role) return false;
    if (q && !r.object_name.toLowerCase().includes(q)
          && !r.schema.toLowerCase().includes(q)
          && !r.functionality.toLowerCase().includes(q)) return false;
    return true;
  }});
  if (sortCol) {{
    data.sort((a, b) => {{
      let va = a[sortCol], vb = b[sortCol];
      if (typeof va === 'number') return sortAsc ? va - vb : vb - va;
      return sortAsc ? String(va).localeCompare(String(vb)) : String(vb).localeCompare(String(va));
    }});
  }}
  return data;
}}

function refresh() {{ render(getFiltered()); }}

document.getElementById('search').addEventListener('input', refresh);
document.getElementById('filterRec').addEventListener('change', refresh);
document.getElementById('filterSchema').addEventListener('change', refresh);
document.getElementById('filterType').addEventListener('change', refresh);
document.getElementById('filterRole').addEventListener('change', refresh);

document.querySelectorAll('th[data-col]').forEach(th => {{
  th.addEventListener('click', () => {{
    const col = th.dataset.col;
    if (sortCol === col) sortAsc = !sortAsc;
    else {{ sortCol = col; sortAsc = true; }}
    document.querySelectorAll('th .arrow').forEach(a => a.textContent = '');
    th.querySelector('.arrow').textContent = sortAsc ? ' ▲' : ' ▼';
    refresh();
  }});
}});

function exportCSV() {{
  const data = getFiltered();
  const cols = ['object_name','object_type','schema','role','recommendation','upstream','downstream','layer','betweenness','pagerank','functionality'];
  const header = cols.join(';');
  const csvRows = data.map(r => cols.map(c => {{
    let v = r[c];
    if (typeof v === 'string' && (v.includes(';') || v.includes('"') || v.includes('\\n')))
      v = '"' + v.replace(/"/g, '""') + '"';
    return v;
  }}).join(';'));
  const csv = '\\uFEFF' + [header, ...csvRows].join('\\n');
  const blob = new Blob([csv], {{type: 'text/csv;charset=utf-8;'}});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'oracle_triage.csv';
  a.click();
}}

refresh();
</script>
</body>
</html>"""


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

    rows = load_and_analyse()
    html = generate_html(rows)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    HTML_FILE.write_text(html, encoding="utf-8")
    print(f"Triage table written to: {HTML_FILE}")
    print(f"  MIGRATE: {sum(1 for r in rows if r['recommendation'] == 'MIGRATE')}")
    print(f"  EVALUATE: {sum(1 for r in rows if r['recommendation'] == 'EVALUATE')}")
    print(f"  SKIP: {sum(1 for r in rows if r['recommendation'] == 'SKIP')}")


if __name__ == "__main__":
    main()
