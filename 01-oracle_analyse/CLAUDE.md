# 01 — Oracle Analyse

Tre-stegs pipeline for analyse og kartlegging av Oracle-databaseobjekter:

1. **LLM-analyse** (`analyze_views.py`, `analyze_procedures.py`) — Gemini 2.5 Flash ekstraherer funksjonalitet, datakilder og måltabeller fra SQL-kildekode i BigQuery
2. **Dependency analysis** (`dependency_analysis/parse_analysis_files.py`, `build_dependency_graph.py`) — Bygger rettet avhengighetsgraf fra LLM-resultatene
3. **Spanner Graph** (`dependency_analysis/load_to_spanner.py`) — Laster grafen inn i Spanner for visualisering og GQL-spørringer

## Skjemaer som analyseres

| Skjema | Views | Prosedyrer |
|--------|-------|------------|
| CCM (Customer Contact Management) | 512 | 12 |
| CLM_ADM (CLM Admin/Analytics) | 81 | 235 |
| CLM_CCM (CLM Customer Contact Mgmt) | 253 | 26 |
| CRM_ANALYSE (CRM Analytics) | 253 | 22 |

## Status

- **Prosedyreanalyse**: Fullført for alle 295 prosedyrer
- **Viewanalyse**: Fullført for alle 1099 views
- **Dependency analysis**: Kjørt — 1389 noder, 1352 kanter (892 kryss-skjema)
- **Spanner Graph**: Data lastet inn i `s07601-p-tnn-consumer`

## Filer

- `config.py` — Delt konfigurasjon: skjemaregister, GCP-hjelpefunksjoner, checkpoint-logikk
- `analyze_views.py` — CLI-script for viewanalyse
- `analyze_procedures.py` — CLI-script for prosedyreanalyse
- `view_and_proc_oracle_agent_analysis.ipynb` — Opprinnelig notebok (referanse)
- `bkp/` — Tidligere analyseresultater (JSON-filer fra notebooken)
- `dependency_analysis/` — Dependency analysis + Spanner Graph-lasting

## Biblioteker

pandas, vertexai (Gemini), google-cloud-bigquery, google-cloud-spanner, tqdm (se `pyproject.toml`)

## Kjøring

Se `README.md` i denne mappen for fullstendige instruksjoner.

## Spanner-database

| Parameter | Verdi |
|-----------|-------|
| Prosjekt | `tnn-nova-spanner` |
| Instans | `nova-eu-west1-01` |
| Database | `s07601-p-tnn-consumer` |
| Graf | `OracleDependencyGraph` |
