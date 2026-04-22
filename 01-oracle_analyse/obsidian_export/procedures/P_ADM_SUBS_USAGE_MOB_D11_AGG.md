# P_ADM_SUBS_USAGE_MOB_D11_AGG

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure P_ADM_SUBS_USAGE_MOB_D11_AGG calculates and aggregates mobile subscription usage data. It performs a multi-stage aggregation process: First, it creates a detailed temporary table, 'TMP_SUBS_USAGE_D11_DET_KPI', by joining various dimension tables with raw usage data and augmenting it with derived key performance indicators (KPIs) such as roaming zone classification, destination zone, traffic type (e.g., MMS, SMS, Voice, Data), and detailed data package categories. Second, it aggregates this detailed data from the first temporary table into a second temporary table, 'TMP_SUBS_USAGE_MOB_D11_AGG'. This final aggregation summarizes usage metrics like MMS/SMS event counts, voice call durations/event counts, data volume (categorized by various data package and shared bucket types), and net revenue, broken down by roaming, destination, and traffic types. Both intermediate temporary tables are explicitly created, used, and then dropped within the procedure's execution.

## Data Sources (Inputs)
- ← [[CCM.VYA_USAGE_DAY_RAW_FULL]]
- ← [[GALAXY.CALL_TYPE_DIM]]
- ← [[GALAXY.ROAMING_COUNTRY_DIM_V]]
- ← [[GALAXY.DESTINATION_COUNTRY_DIM_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]
- ← [[CLM_ADM.ADM_SUBS_USAGE_MONTH_DET]]

## Target Tables (Outputs)
- → [[TMP_SUBS_USAGE_D11_DET_KPI]]
- → [[TMP_SUBS_USAGE_MOB_D11_AGG]]

