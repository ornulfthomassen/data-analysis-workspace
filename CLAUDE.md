# Data Analysis Workspace

Monorepo for dataanalyse-prosjekter hos Telenor Norge Consumer. Hvert delprosjekt ligger i en nummerert mappe og er selvforsynt med egne avhengigheter.

## Prosjektstruktur

```
01-oracle_analyse/    Oracle-kodeanalyse med LLM (Gemini)
```

## Miljø

- **Python**: 3.13.7 (`.venv/` i rot)
- **GCP-prosjekter**: `tnn-consumer-common-nx` (BigQuery), `tnn-pnx-consumer-common-ai` (Vertex AI)
- **Autentisering**: `gcloud auth application-default login`

## 01 — Oracle Analyse

Automatisert analyse av Oracle-databaseobjekter (views og prosedyrer) ved hjelp av Gemini 2.5 Flash på Vertex AI. SQL-kildekoden ligger i BigQuery-tabeller og sendes til LLM for å ekstrahere strukturert metadata: funksjonalitet, datakilder og måltabeller.

### Skjemaer som analyseres

| Skjema | Views | Prosedyrer |
|--------|-------|------------|
| CCM (Customer Contact Management) | 512 | 12 |
| CLM_ADM (CLM Admin/Analytics) | 81 | 235 |
| CLM_CCM (CLM Customer Contact Mgmt) | 253 | 26 |
| CRM_ANALYSE (CRM Analytics) | 253 | 22 |

### Status

- **Prosedyreanalyse**: Fullført for alle 295 prosedyrer (JSON-filer med funksjonalitet, datakilder, måltabeller)
- **Viewanalyse**: Feilet for alle 1099 views pga. utløpt autentisering (503-feil). Må kjøres på nytt.

### Filer

- `view_and_proc_oracle_agent_analysis.ipynb` — Hovednotebok (data-prep + LLM-analyse)
- `*_procedures_analysis.json` — Ferdig prosedyreanalyse (4 filer)
- `*_views_analysis.json` — Feilet viewanalyse (4 filer, må kjøres på nytt)

### Biblioteker

pandas, vertexai (Gemini), tqdm, Google Cloud CLI (`bq`, `gcloud`)

### Kjøring

1. Autentiser: `gcloud auth application-default login`
2. Kjør notebook-cellene sekvensielt. Celler med LLM-kall har checkpoint/resume-logikk.

## Konvensjoner

- Delprosjekter nummereres sekvensielt (`01-`, `02-`, ...)
- Hvert delprosjekt har egen `pyproject.toml` / avhengigheter
- Mellomlagring av data i parquet-filer for debugging
- GCP Application Default Credentials for autentisering
- Gemini (Vertex AI) som LLM for analyseoppgaver
