# ADM_MOBILE_WIFI_TRAFFIC_DAILY2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure processes daily mobile WiFi traffic data for a specified date range. It dynamically creates and manages a partitioned historical table named `ADM_MOBILE_WIFI_TRAFFIC_HIST` in the `CLM_ADM` schema. For each day in the range, it extracts, aggregates, and transforms data from `CDR.CDR_GENEVA`, stores it temporarily in `TMP_MOBILE_WIFI_TRAFFIC_HIST`, and then inserts distinct records into the appropriate daily partition of the main historical table, joining with `CCDW.SUBSCRIPTION_MAPPING` and avoiding duplicates based on `EVENT_DATE_KEY`, `SUBSCRIPTION_ID`, `BEARER`, and `TIERID_3`.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| SUBOBJECT_NAME |
| OWNER |
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
- ← [[CLM_ADM.TMP_MOBILE_WIFI_TRAFFIC_HIST]]
| Column Name |
|---|
| EVENT_DATE |
| MAIN_NUMBER |
| SUBSCR_ID |
| GENEVA_CALL_TYPE |
| TIERID_3 |
| BEARER |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
| SUBSCRIPTION_ID |
- ← [[CLM_ADM.ADM_MOBILE_WIFI_TRAFFIC_HIST]]
| Column Name |
|---|
| EVENT_DATE_KEY |
| SUBSCRIPTION_ID |
| BEARER |
| TIERID_3 |

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_MOBILE_WIFI_TRAFFIC_HIST]]
| Column Name |
|---|
| EVENT_DATE_KEY |
| EVENT_DATE |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| GENEVA_CALL_TYPE |
| TIERID_3 |
| BEARER |
- → [[CLM_ADM.TMP_MOBILE_WIFI_TRAFFIC_HIST]]
| Column Name |
|---|
| MAIN_NUMBER |
| SUBSCR_ID |
| GENEVA_CALL_TYPE |
| TIERID_3 |
| BEARER |
| EVENT_DATE |

