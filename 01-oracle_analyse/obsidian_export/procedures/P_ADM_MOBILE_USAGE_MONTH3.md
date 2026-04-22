# P_ADM_MOBILE_USAGE_MONTH3

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Aggregates detailed mobile usage statistics, including event counts (MMS, SMS, TALE), call duration (TALE), data volume (MB_DATA), and associated net revenues, for a specified month (P_YYYYMM). It breaks down these metrics by domestic, international, and roaming usage, as well as by various product and traffic type categories. The aggregated data is first stored in a temporary staging table, and then moved into a monthly partition of a permanent, partitioned usage summary table. The procedure ensures the target partition exists and computes statistics after the data load.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_SUBS_USAGE_MONTH_DET]]
- ← [[GALAXY.CALL_TYPE_DIM]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]

## Target Tables (Outputs)
- → [[TMP_MOBILE_USAGE_MONTH]]
- → [[ADM_MOBILE_USAGE_MONTH_NEW]]

