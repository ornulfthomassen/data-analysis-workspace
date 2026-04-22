# GCP_ODS_OTT_MIN_SKY_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
Extracts and transforms historical usage data for the 'Min Sky' Over-The-Top (OTT) service, combining user activity metrics with customer identification. It calculates daily activity flags (KPI_FOREGROUND, KPI_CONNECTION) and aggregates usage statistics (quota, media file count) for reporting or loading into a data warehousing system (implied by 'Mjøsa').

## Data Sources (Inputs)
- ← [[CLM_ADM.SCD2_MIN_SKY_MAIN]]
- ← [[ODS.CONNECT_ID_LINK]]

