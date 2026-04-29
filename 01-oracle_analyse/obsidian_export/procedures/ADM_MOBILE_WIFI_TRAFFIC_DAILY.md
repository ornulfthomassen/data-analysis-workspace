# ADM_MOBILE_WIFI_TRAFFIC_DAILY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure processes daily mobile traffic data to populate a permanent, partitioned history table (ADM_MOBILE_TRAFFIC_BEARER_HIST). It identifies processing dates based on system metadata and CDR load dates. For each day, it extracts aggregated traffic details from CDR records and subscription information, stores them temporarily in TMP_MOBILE_TRAFFIC_BEARER_HIST, and then inserts them into the permanent history table, handling partition creation and managing indexes as needed. It also performs checks for missing source data.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DATE_KEY |
- ← [[CDR.CDR_GENEVA]]
| Column Name |
|---|
| LOAD_DATE |
| CALLING_MAIN_DIRECTORY_NUMBER |
| SUBSCR_ID |
| GENEVA_CALL_TYPE |
| TIERID_3 |
| BEARER |
| EVENT_START_DATE_TIME |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |

## Target Tables (Outputs)
- → [[ADM_MOBILE_TRAFFIC_BEARER_HIST]]
| Column Name |
|---|
| EVENT_DATE_KEY |
| EVENT_DATE |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| GENEVA_CALL_TYPE |
| TIERID_3 |
| BEARER |
- → [[TMP_MOBILE_TRAFFIC_BEARER_HIST]]
| Column Name |
|---|
| MAIN_NUMBER |
| SUBSCR_ID |
| GENEVA_CALL_TYPE |
| TIERID_3 |
| BEARER |
| EVENT_DATE |

