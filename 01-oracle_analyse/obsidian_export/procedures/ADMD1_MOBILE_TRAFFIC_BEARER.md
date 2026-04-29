# ADMD1_MOBILE_TRAFFIC_BEARER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure processes daily mobile traffic bearer data. For a given date range, it extracts raw traffic records from `CDR.CDR_GENEVA`, aggregates them into a temporary table, then joins with `CCDW.SUBSCRIPTION_MAPPING` to enrich the data, and finally inserts the unique aggregated results into the partitioned historical table `ADM_MOBILE_TRAFFIC_BEARER_HIST`. It includes logic for managing table partitions, dropping/creating indexes, and handling missing data scenarios.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DATE_KEY |
- ← [[CDR.CDR_GENEVA]]
| Column Name |
|---|
| LOAD_DATE |
| SUBSCR_ID |
| GENEVA_CALL_TYPE |
| BEARER |
| EVENT_START_DATE_TIME |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
- ← [[ADM_MOBILE_TRAFFIC_BEARER_HIST]]
| Column Name |
|---|
| PERIOD_DATE_KEY |
| SUBSCRIPTION_ID |
| BEARER |
- ← [[TMP_MOBILE_TRAFFIC_BEARER_HIST]]
| Column Name |
|---|
| EVENT_DATE |
| SUBSCR_ID |
| GENEVA_CALL_TYPE |
| BEARER |

## Target Tables (Outputs)
- → [[TMP_MOBILE_TRAFFIC_BEARER_HIST]]
| Column Name |
|---|
| SUBSCR_ID |
| GENEVA_CALL_TYPE |
| BEARER |
| EVENT_DATE |
- → [[ADM_MOBILE_TRAFFIC_BEARER_HIST]]
| Column Name |
|---|
| PERIOD_DATE_KEY |
| SUBSCRIPTION_ID |
| EVENT_DATE |
| GENEVA_CALL_TYPE |
| BEARER |

