# ADM_MOBILE_WIFI_TRAFFIC_DAILY2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `ADM_MOBILE_WIFI_TRAFFIC_DAILY2` processes daily mobile and WiFi traffic data. For a specified range of dates (or determined dynamically from the latest `CDR.CDR_GENEVA` load date), it performs the following steps for each day: 
1. Ensures the existence and proper partitioning of the main historical table `ADM_MOBILE_WIFI_TRAFFIC_HIST`.
2. Creates a temporary staging table (`TMP_MOBILE_WIFI_TRAFFIC_HIST`) by selecting raw traffic data from `CDR.CDR_GENEVA`.
3. Enriches this staged data by joining with `CCDW.SUBSCRIPTION_MAPPING`.
4. Inserts unique records from the temporary table into the main `ADM_MOBILE_WIFI_TRAFFIC_HIST` table, avoiding duplicates.
It also handles the creation, optional dropping, and recreation of indexes on the historical table for performance optimization.

## Data Sources (Inputs)
- ← [[CDR.CDR_GENEVA]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]

## Target Tables (Outputs)
- → [[ADM_MOBILE_WIFI_TRAFFIC_HIST]]
- → [[TMP_MOBILE_WIFI_TRAFFIC_HIST]]

