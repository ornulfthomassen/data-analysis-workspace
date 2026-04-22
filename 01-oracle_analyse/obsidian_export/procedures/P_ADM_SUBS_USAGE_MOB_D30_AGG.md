# P_ADM_SUBS_USAGE_MOB_D30_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Aggregates detailed mobile subscription usage data (MMS, SMS, voice calls, data volumes, and associated revenues) from a monthly detail table and various dimension tables. It enriches and categorizes usage records by roaming zone, destination zone, traffic type, data package type, and shared bucket type. The procedure uses two intermediate temporary tables for detailed and aggregated results before loading the final aggregated data into a monthly partition of a permanent administrative table, ADM_SUBS_USAGE_MOB_MONTH_AGG.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBS_USAGE_MONTH_DET]]
- ← [[GALAXY.CALL_TYPE_DIM]]
- ← [[GALAXY.ROAMING_COUNTRY_DIM_V]]
- ← [[GALAXY.DESTINATION_COUNTRY_DIM_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]

## Target Tables (Outputs)
- → [[TMP_SUBS_USAGE_D30_DET_KPI]]
- → [[TMP_SUBS_USAGE_MOB_D30_AGG]]
- → [[ADM_SUBS_USAGE_MOB_MONTH_AGG]]

