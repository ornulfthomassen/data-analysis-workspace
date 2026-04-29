# Current Focus — Data Analysis Workspace
> Sist oppdatert: 2026-04-29 — Overlevering fra Ørnulf

## Status: Overlevert

Prosjektet er overlevert fra Ørnulf Thomassen. Videre arbeid drives av Harald/Noman/Amanda.

## Fullført arbeid (runde 1)
- LLM-analyse av **295 prosedyrer** og **1099 views** fra 4 Oracle-skjemaer
- Avhengighetsgraf: 1389 noder, 1352 kanter (892 kryss-skjema)
- Data lastet i Spanner Graph (`tnn-nova-spanner`)
- NetworkX sentralitetsanalyse og migreringsrapport
- Obsidian-vault for grafvisualisering
- Kolonne-lineage lagt til i LLM-promptene

## Neste steg (for ny eier)
- [ ] Kjøre runde 2: full re-analyse med kolonne-lineage (`--schema all`)
- [ ] Verifisere migreringsrapport mot faktiske Oracle-avhengigheter
- [ ] Definere første batch for dbt-migrering
- [ ] Koble funn til Telenor data platform roadmap

## Kontekst
- Hovedmappe: `01-oracle_analyse/`
- Se `01-oracle_analyse/README.md` for pipeline-dokumentasjon
- GCP gcloud config: `jobb`
- Branch: main
