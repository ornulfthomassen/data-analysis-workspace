# P_ADM_SUBS_USAGE_MOB_MONTH_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, P_ADM_SUBS_USAGE_MOB_MONTH_AGG, is designed to process and aggregate mobile subscription usage data on a monthly basis. It first prepares a detailed Key Performance Indicator (KPI) enriched temporary dataset from raw usage records. Then, it aggregates this KPI-enriched data into another temporary table, calculating various metrics for MMS, SMS, Voice calls, and Data usage (including domestic, roaming, and different data package types) per subscription and month. Finally, it loads this aggregated data into a specific monthly partition of a permanent administrative table (ADM_SUBS_USAGE_MOB_MONTH_AGG) using an 'exchange partition' operation. The procedure includes logic for data source validation, error handling, and gathering table statistics.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_SUBS_USAGE_MONTH_DET]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[GALAXY.CALL_TYPE_DIM]]
- ← [[GALAXY.ROAMING_COUNTRY_DIM_V]]
- ← [[GALAXY.DESTINATION_COUNTRY_DIM_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]

## Target Tables (Outputs)
- → [[TMP_SUBS_USAGE_MONTH_DET_KPI]]
- → [[TMP_SUBS_USAGE_MOB_MONTH_AGG]]
- → [[ADM_SUBS_USAGE_MOB_MONTH_AGG]]

