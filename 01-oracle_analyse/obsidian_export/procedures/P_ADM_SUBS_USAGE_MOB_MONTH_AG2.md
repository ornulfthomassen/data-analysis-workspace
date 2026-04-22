# P_ADM_SUBS_USAGE_MOB_MONTH_AG2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure aggregates mobile subscription usage data on a monthly basis. It calculates various Key Performance Indicators (KPIs) related to MMS, SMS, Voice, and Data usage, classifying them by roaming zone, destination zone, traffic type, data package type, and shared bucket type. The final aggregated data for a specific month is then loaded into a permanent, partitioned administrative table by exchanging a newly created partition with a temporary table containing the processed data.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_SUBS_USAGE_MONTH_DET2]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[GALAXY.CALL_TYPE_DIM]]
- ← [[GALAXY.ROAMING_COUNTRY_DIM_V]]
- ← [[GALAXY.DESTINATION_COUNTRY_DIM_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]

## Target Tables (Outputs)
- → [[TMP_SUBS_USAGE_MONTH_DET_KPI]]
- → [[TMP_SUBS_USAGE_MOB_MONTH_AGG]]
- → [[ADM_SUBS_USAGE_MOB_MONTH_AGG2]]

