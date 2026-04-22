# Prosjektminne (Project Memory)
Dette dokumentet fungerer som et felles minne for alle AI-agenter.

## Viktige Beslutninger & Lærdommer

- **Dato:** 2026-04-22
- **Beslutning:** Utviklet et Python-script (`generate_obsidian_files.py`) for å konvertere JSON-analyseresultater til et Obsidian-vault.
- **Kontekst:** For å kunne visualisere og navigere avhengigheter mellom Oracle-databaseobjekter (views, prosedyrer, tabeller) i et graf-verktøy som Obsidian. Scriptet genererer individuelle Markdown-filer for hvert objekt, inkludert metadata som skjema, type, og retningsbestemte linker (leser fra/skriver til) for avhengigheter.
- **Utført av:** Gemini/Claude

- **Dato:** 2026-04-13
- **Beslutning:** Lagt til Oracle dependency-analyse og NetworkX sentralitetsanalyse for dbt-migrering.
- **Kontekst:** Kartlegger avhengigheter mellom Oracle-systemer som grunnlag for migreringsrekkefølge.
- **Utført av:** Claude Code

- **Dato:** 2026-04-11
- **Beslutning:** Migrerte historisk AI-minne fra interne Claude-prosjekter til `docs/ai/`.
- **Kontekst:** Sikrer at alle modeller har tilgang til tidligere erfaringer direkte i prosjektmappen.
