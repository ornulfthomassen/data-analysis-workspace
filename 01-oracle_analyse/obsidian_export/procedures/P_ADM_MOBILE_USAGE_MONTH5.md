# P_ADM_MOBILE_USAGE_MONTH5

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, P_ADM_MOBILE_USAGE_MONTH5, calculates and aggregates detailed mobile usage statistics (including MMS, SMS, voice calls, and data volumes with associated revenues) for a specific month. It processes various KPIs related to traffic type, destination zone, roaming zone, and data packages. The aggregated results are then loaded into a monthly partition of a permanent analytical table, ADM_MOBILE_USAGE_MONTH_NEW3, replacing any existing data for that month's partition. It uses a temporary table for intermediate data storage during the aggregation process.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
- ← [[CLM_ADM.TMP_SUBS_USAGE_MONTH_DET_KPI]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_MOBILE_USAGE_MONTH_NEW3]]
- → [[CLM_ADM.TMP_MOBILE_USAGE_MONTH]]

