# Data Analysis Workspace

Dataanalyse-prosjekter for Telenor Norge Consumer — primært Oracle-avhengighetsanalyse for dbt-migrering.

## Prosjekter

| Mappe | Status | Beskrivelse |
|-------|--------|-------------|
| `01-oracle_analyse/` | **Aktiv** | Oracle-kodeanalyse med LLM + avhengighetsgraf visualisert i Obsidian |
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

### Visualisering

Avhengighetsgrafen visualiseres med **Obsidian** (ikke Spanner Graph — det ble droppet). Åpne mappen `01-oracle_analyse/obsidian_export/` i Obsidian for å se grafvisningen. Last ned Obsidian fra [obsidian.md](https://obsidian.md/download).

### Hva er gjort

- LLM-analyse av **295 prosedyrer** og **1099 views** fra 4 Oracle-skjemaer (CCM, CLM_ADM, CLM_CCM, CRM_ANALYSE)
- Avhengighetsgraf: **1389 noder, 1352 kanter** (892 kryss-skjema)
- Obsidian-vault med alle objekter, retningspiler og skjema-metadata
- Kolonne-lineage lagt til i promptene (runde 2 klar til kjøring)

### Hva gjenstår

- Kjøre runde 2 med kolonne-lineage for alle objekter
- Verifisere migreringsrapportens anbefalte rekkefølge
- Definere første batch for dbt-migrering basert på sentralitetsanalyse
