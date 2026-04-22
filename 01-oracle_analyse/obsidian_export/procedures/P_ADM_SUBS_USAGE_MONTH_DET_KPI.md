# P_ADM_SUBS_USAGE_MONTH_DET_KPI

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure calculates and enriches subscription usage data by deriving various Key Performance Indicators (KPIs) related to roaming zones, destination zones, traffic types, data package classifications, and shared bucket types. It processes monthly detailed usage records, joins them with several dimension tables (month, call type, roaming country, destination country, product, traffic type), and stores the results in a temporary table.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_SUBS_USAGE_MONTH_DET]]
- ← [[GALAXY.CALL_TYPE_DIM]]
- ← [[GALAXY.ROAMING_COUNTRY_DIM_V]]
- ← [[GALAXY.DESTINATION_COUNTRY_DIM_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]

## Target Tables (Outputs)
- → [[TMP_SUBS_USAGE_MONTH_DET_KPI]]

