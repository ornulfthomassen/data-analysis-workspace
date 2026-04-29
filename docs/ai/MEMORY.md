# Data Analysis Workspace — Project Memory

## Overview
Monorepo for Telenor Norge Consumer data analysis projects at `/Users/t736135/git_projects/data-analysis-workspace`.

## Sub-projects
- `01-oracle_analyse/` — LLM-based Oracle DB code analysis + dependency graph in Spanner Graph
- `02-telenorbutikken/` — SMS pilot campaign analysis with discount coupons

## Documentation structure
- Top-level README.md + CLAUDE.md: short overview only
- Each sub-project has its own README.md + CLAUDE.md with full details
- No sub-sub-project READMEs (e.g. dependency_analysis/ has no README)

## Key details
- Python 3.13.7 in `.venv/`
- GCP projects: `tnn-consumer-common-nx` (BQ), `tnn-pnx-consumer-common-ai` (Vertex AI), `tnn-nova-spanner` (Spanner)
- gcloud auth is machine-global (not per VS Code session!)
- Remote: https://github.com/ornulfthomassen/data-analysis-workspace
- User prefers Norwegian for documentation/CLAUDE.md files

## 01-oracle_analyse
- 3-step pipeline: LLM analysis → dependency graph → Spanner Graph
- Spanner: project `tnn-nova-spanner`, instance `nova-eu-west1-01`, DB `s07601-p-tnn-consumer`
- Edge table uses `object_name` (not `source_object`) due to Spanner INTERLEAVE requirement
- GQL queries need column aliases to avoid ambiguity (object_name exists in both tables)
- User has Spanner instance access but not gcloud project-level access — uses Spanner Studio for DDL

## 02-telenorbutikken
- SMS pilot with discount coupons in a geographic area
- BQ tables: `tnn-consumer-common-nx-gold.Engagement.hightouch_engagement_reporting_deep_v` (campaign), `tnn-consumer-common-nx-gold.customer_360.customer_360` (customer profile)
- Campaign Model_id: '4210310'
- PowerPoint with details to be uploaded to docs/
