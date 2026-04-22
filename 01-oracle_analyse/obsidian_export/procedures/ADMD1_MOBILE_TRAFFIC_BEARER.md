# ADMD1_MOBILE_TRAFFIC_BEARER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure processes mobile traffic bearer data for a specified date range. For each day in the range, it extracts raw call detail record (CDR) data from the `CDR.CDR_GENEVA` table, stores it into a temporary table named `TMP_MOBILE_TRAFFIC_BEARER_HIST`. It then joins this temporary data with subscription mapping information from `CCDW.SUBSCRIPTION_MAPPING` and inserts the unique records into a permanent, partitioned history table, `ADM_MOBILE_TRAFFIC_BEARER_HIST`. The procedure also manages indexes on the main history table (optionally dropping and recreating them for performance) and collects statistics on the newly loaded partitions. It includes dynamic date range determination and error handling for missing target tables or data.

## Data Sources (Inputs)
- ← [[CDR.CDR_GENEVA]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]

## Target Tables (Outputs)
- → [[ADM_MOBILE_TRAFFIC_BEARER_HIST]]
- → [[TMP_MOBILE_TRAFFIC_BEARER_HIST]]

