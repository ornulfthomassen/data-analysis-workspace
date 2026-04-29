# GCP_ROLLOVER_HISTORY_MONTH

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts rollover history data, filtering by a dynamic period key (past few months), primarily for loading into Google Cloud Platform (GCP).

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_ROLLOVER_HIST]]
| Column Name |
|---|
| LOAD_DATE |
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| SUBSCR_ID |
| POID |
| BALANCE |
| O_ID |
| PURCHASE_SEQ |
- ← [[DUAL]]

