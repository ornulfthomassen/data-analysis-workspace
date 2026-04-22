# Oracle Analyse

Automatisert analyse og avhengighetskartlegging av Oracle-databaseobjekter (views og prosedyrer) fra fire skjemaer. Fire-stegs pipeline:

## Steg 1: LLM-analyse av SQL-kildekode

SQL-kildekoden hentes fra BigQuery og sendes til Gemini 2.5 Flash for å ekstrahere strukturert metadata: funksjonalitet, datakilder og måltabeller.

| Skjema | Views | Prosedyrer |
|--------|-------|------------|
| CCM | 512 | 12 |
| CLM_ADM | 81 | 235 |
| CLM_CCM | 253 | 26 |
| CRM_ANALYSE | 253 | 22 |

```bash
# Views — ett skjema, flere, eller alle
python analyze_views.py --schema ccm
python analyze_views.py --schema all

# Prosedyrer
python analyze_procedures.py --schema clm_adm
python analyze_procedures.py --schema all

# Dry run (bare vis antall, ingen LLM-kall)
python analyze_views.py --schema all --dry-run
```

Checkpoint/resume er innebygd — avbryt og kjør på nytt for å gjenoppta.

**Status:** Prosedyrer ferdig (295 stk). Views ferdig (1099 stk).

## Steg 2: Dependency analysis

Parser JSON-resultater fra steg 1 og bygger en rettet avhengighetsgraf: hvis prosedyre A skriver til tabell X og objekt B leser fra tabell X, opprettes en kant A→B.

```bash
cd dependency_analysis

# Parse alle JSON-filer til enhetlig format
python parse_analysis_files.py

# Bygg avhengighetsgraf
python build_dependency_graph.py

# Inkluder midlertidige tabeller
python build_dependency_graph.py --include-temp
```

**Resultat:** 1389 noder, 1352 kanter (892 kryss-skjema).

## Steg 3: Spanner Graph (visualisering)

Avhengighetsgrafen lastes inn i Google Cloud Spanner Graph for interaktiv visualisering og GQL-spørringer.

| Parameter | Verdi |
|-----------|-------|
| Prosjekt | `tnn-nova-spanner` |
| Instans | `nova-eu-west1-01` |
| Database | `s07601-p-tnn-consumer` |

```bash
cd dependency_analysis

# Opprett tabeller: kjør spanner_ddl.sql i Spanner Studio (3 statements i rekkefølge)

# Last data inn i Spanner
python load_to_spanner.py

# Ved re-kjøring: slett eksisterende data først
python load_to_spanner.py --clear
```

GQL-eksempler for Spanner Studio:

```sql
-- Grafvisualisering for én prosedyre
GRAPH OracleDependencyGraph
MATCH (src:OracleObject {object_name: 'CLM_ADM.P_ADM_MONTH_DIM'})-[d:DependsOn]->(dst:OracleObject)
RETURN TO_JSON(src) AS source, TO_JSON(d) AS edge, TO_JSON(dst) AS target;

-- Kryss-skjema-avhengigheter
GRAPH OracleDependencyGraph
MATCH (src:OracleObject)-[d:DependsOn]->(dst:OracleObject)
WHERE src.schema_name != dst.schema_name
RETURN src.schema_name AS src_schema, src.object_name AS src_object,
       dst.schema_name AS dst_schema, dst.object_name AS dst_object,
       d.linked_table AS via_table;
```

## Steg 4: Generer Obsidian-filer (Visualisering)

Etter at JSON-analysene er fullført, kan du generere et komplett Obsidian-vault for å visualisere avhengighetene som en graf.

```bash
python generate_obsidian_files.py
```

Dette scriptet gjør følgende:
1.  Oppretter en `obsidian_export`-mappe.
2.  Genererer en Markdown-fil for hver prosedyre og hvert view.
3.  Genererer "stub"-filer for alle eksterne avhengigheter (tabeller etc.).
4.  Linker avhengigheter med piler (`←` for lesing, `→` for skriving) for tydelig retning.
5.  Inkluderer metadata som `Schema` og `Type` i hver fil.

Åpne `obsidian_export`-mappen i Obsidian for å se grafen.
Obsidian er en kraftig kunnskapsbase som lar deg organisere notater og visualisere sammenhenger mellom dem ved hjelp av en grafvisning. Du kan laste ned Obsidian her: [https://obsidian.md/download](https://obsidian.md/download)

## Filstruktur

```
config.py                     # Delt konfig: skjemaregister, GCP-hjelpefunksjoner
analyze_views.py              # CLI for viewanalyse (steg 1)
analyze_procedures.py         # CLI for prosedyreanalyse (steg 1)
generate_obsidian_files.py    # CLI for Obsidian-generering (steg 4)
pyproject.toml                # Avhengigheter
view_and_proc_oracle_agent_analysis.ipynb  # Opprinnelig notebok (referanse)
bkp/                          # Tidligere analyseresultater
dependency_analysis/
├── parse_analysis_files.py   # Steg 2: Parse JSON til enhetlig format
├── build_dependency_graph.py # Steg 2: Bygg avhengighetsgraf
├── spanner_ddl.sql           # Steg 3: DDL for Spanner-tabeller + property graph
├── load_to_spanner.py        # Steg 3: Last data inn i Spanner
└── output/                   # Genererte JSON-filer
obsidian_export/              # Genererte markdown-filer for Obsidian
```
