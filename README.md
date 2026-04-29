# Data Analysis Workspace

Dataanalyse-prosjekter for Telenor Norge Consumer — primært Oracle-avhengighetsanalyse for dbt-migrering.

## Prosjekter

| Mappe | Status | Beskrivelse |
|-------|--------|-------------|
| `01-oracle_analyse/` | **Aktiv** | Oracle-kodeanalyse med LLM + avhengighetsgraf i Spanner Graph |
| `02-telenorbutikken/` | Ikke startet | SMS-pilot (kun en PowerPoint-fil) |
| `03-customer-360/` | Ikke startet | Customer 360-spørring (kun en SQL-fil) |

**Kun `01-oracle_analyse/` har reelt innhold.** Se [01-oracle_analyse/README.md](01-oracle_analyse/README.md) for full dokumentasjon.

## Overlevering

Prosjektet er overlevert fra Ørnulf Thomassen (april 2026). Kontaktpersoner for videre arbeid: Harald, Noman, Amanda.

### Kom i gang

```bash
cd 01-oracle_analyse
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
gcloud auth application-default login
```

### GCP-ressurser

| Ressurs | Prosjekt |
|---------|----------|
| BigQuery (kildekode) | `tnn-consumer-common-nx` |
| Vertex AI (Gemini) | `tnn-pnx-consumer-common-ai` |
| Spanner Graph | `tnn-nova-spanner` (instans: `nova-eu-west1-01`, DB: `s07601-p-tnn-consumer`) |

### Hva er gjort

- LLM-analyse av **295 prosedyrer** og **1099 views** fra 4 Oracle-skjemaer (CCM, CLM_ADM, CLM_CCM, CRM_ANALYSE)
- Avhengighetsgraf: **1389 noder, 1352 kanter** (892 kryss-skjema)
- Data lastet inn i Spanner Graph for visualisering
- Obsidian-vault generert for grafnavigering
- Kolonne-lineage lagt til i promptene (runde 2 klar til kjøring)

### Hva gjenstår

- Kjøre runde 2 med kolonne-lineage for alle objekter
- Verifisere migreringsrapportens anbefalte rekkefølge
- Definere første batch for dbt-migrering basert på sentralitetsanalyse
