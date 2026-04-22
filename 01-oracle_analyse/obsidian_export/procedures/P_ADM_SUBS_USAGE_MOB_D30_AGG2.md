# P_ADM_SUBS_USAGE_MOB_D30_AGG2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure aggregates mobile subscription usage data by calculating various key performance indicators (KPIs) related to MMS, SMS, Voice calls, and Data usage. It categorizes usage by roaming zone, destination zone, traffic type, and data package details. The procedure first creates an intermediate temporary table (`TMP_SUBS_USAGE_D30_DET_KPI`) to derive detailed KPIs from raw usage data, then uses this to populate a second temporary table (`TMP_SUBS_USAGE_MOB_D30_AGG`) with aggregated monthly metrics. Finally, it stores these aggregated metrics into a permanent, partitioned administrative table (`ADM_SUBS_USAGE_MOB_MONTH_AGG2`), handling partition creation and indexing.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBS_USAGE_MONTH_DET2]]
- ← [[GALAXY.CALL_TYPE_DIM]]
- ← [[GALAXY.ROAMING_COUNTRY_DIM_V]]
- ← [[GALAXY.DESTINATION_COUNTRY_DIM_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]

## Target Tables (Outputs)
- → [[TMP_SUBS_USAGE_D30_DET_KPI]]
- → [[TMP_SUBS_USAGE_MOB_D30_AGG]]
- → [[ADM_SUBS_USAGE_MOB_MONTH_AGG2]]

