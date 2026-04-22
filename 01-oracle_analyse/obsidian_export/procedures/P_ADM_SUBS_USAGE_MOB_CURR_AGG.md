# P_ADM_SUBS_USAGE_MOB_CURR_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, P_ADM_SUBS_USAGE_MOB_CURR_AGG, calculates and aggregates detailed mobile subscription usage data for a specific month. It first processes raw usage details and various dimension data to derive key performance indicators (KPIs) related to roaming, destination, traffic type (MMS, SMS, Voice, Data), data package types, and shared bucket types. These detailed KPIs are stored in a temporary table (TMP_SUBS_USAGE_CURR_DET_KPI). Subsequently, it aggregates this data into another temporary table (TMP_SUBS_USAGE_MOB_CURR_AGG), summarizing usage counts, durations, data volumes (MB), and net revenues by subscription ID, sub_number, and the derived KPIs. Finally, the aggregated data from the second temporary table is loaded into a permanent, partitioned administrative table (ADM_SUBS_USAGE_MOB_MONTH_AGG) by performing an EXCHANGE PARTITION operation for the processed month.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBS_USAGE_MONTH_DET]]
- ← [[GALAXY.CALL_TYPE_DIM]]
- ← [[GALAXY.ROAMING_COUNTRY_DIM_V]]
- ← [[GALAXY.DESTINATION_COUNTRY_DIM_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]

## Target Tables (Outputs)
- → [[TMP_SUBS_USAGE_CURR_DET_KPI]]
- → [[TMP_SUBS_USAGE_MOB_CURR_AGG]]
- → [[ADM_SUBS_USAGE_MOB_MONTH_AGG]]

