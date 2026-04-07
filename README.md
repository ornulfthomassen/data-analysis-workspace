# Data Analysis Workspace

Monorepo for dataanalyse-prosjekter hos Telenor Norge Consumer.

## Prosjekter

| Mappe | Beskrivelse | Status |
|-------|-------------|--------|
| `01-oracle_analyse/` | Oracle-kodeanalyse med LLM (Gemini 2.5 Flash) | Prosedyrer ferdig, views må kjøres på nytt |

## Oppsett

```bash
# Python 3.13.7
python3 -m venv .venv
source .venv/bin/activate

# GCP-autentisering
gcloud auth application-default login
```

## 01 — Oracle Analyse

Automatisert analyse av Oracle-databaseobjekter (views og prosedyrer) fra fire skjemaer (CCM, CLM_ADM, CLM_CCM, CRM_ANALYSE). SQL-kildekoden hentes fra BigQuery og sendes til Gemini for å ekstrahere funksjonalitet, datakilder og måltabeller.

- **295 prosedyrer** analysert (ferdig)
- **1099 views** må kjøres på nytt (feilet pga. utløpt autentisering)

Se `01-oracle_analyse/view_and_proc_oracle_agent_analysis.ipynb` for å komme i gang.

## Konvensjoner

- Delprosjekter nummereres sekvensielt (`01-`, `02-`, ...)
- Hvert delprosjekt har egne avhengigheter
- GCP Application Default Credentials for autentisering
- Gemini (Vertex AI) som LLM for analyseoppgaver
