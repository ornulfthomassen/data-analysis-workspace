# GCP_ROLLOVER_HISTORY_MONTH

**Schema:** `CCM` | **Type:** `View`

## Description
Prepares and extracts rollover history data for loading into Google Cloud Platform (GCP). It selects rollover-related attributes like load date, period month key, subscription IDs, balance, and purchase sequence from an administrative rollover history table, filtering for recent months.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_ROLLOVER_HIST]]

