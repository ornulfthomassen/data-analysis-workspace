# ADM_MOBILE_WIFI_TRAFFIC_DAILY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `ADM_MOBILE_WIFI_TRAFFIC_DAILY` processes daily mobile Wi-Fi traffic data. It manages the creation and partitioning of a historical data table, `ADM_MOBILE_TRAFFIC_BEARER_HIST`. For each processing date, it extracts and aggregates raw traffic data from `CDR.CDR_GENEVA` into a temporary staging table, `TMP_MOBILE_TRAFFIC_BEARER_HIST`. Subsequently, it inserts the processed data from this temporary table into the main `ADM_MOBILE_TRAFFIC_BEARER_HIST` table, enriching it with subscription information from `CCDW.SUBSCRIPTION_MAPPING` and preventing duplicate entries. The procedure also handles index creation/rebuilding and statistics gathering on the historical table and its partitions.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CDR.CDR_GENEVA]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]

## Target Tables (Outputs)
- → [[ADM_MOBILE_TRAFFIC_BEARER_HIST]]
- → [[TMP_MOBILE_TRAFFIC_BEARER_HIST]]

