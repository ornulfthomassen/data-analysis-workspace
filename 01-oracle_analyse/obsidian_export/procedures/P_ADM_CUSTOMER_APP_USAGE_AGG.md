# P_ADM_CUSTOMER_APP_USAGE_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure aggregates customer application usage data for a specified month (P_YYYYMM). It first performs status checks on source data. If sources are valid, it creates or ensures the existence of a partition in the main target table, `ADM_CUSTOMER_APP_USAGE_AGG`, for the given month. It then populates a temporary staging table, `TMP_CUSTOMER_APP_USAGE_AGG`, with aggregated data by joining several source tables. Finally, it uses an `EXCHANGE PARTITION` operation to efficiently swap the contents of the temporary table into the corresponding partition of the permanent `ADM_CUSTOMER_APP_USAGE_AGG` table, effectively loading the aggregated data.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[CCDW_CUSTOMER_EVENT.CUSTOMER_EVENT_DETAIL]]
- ← [[CCDW_CUSTOMER_EVENT.EVENT_MEDIUM]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[ADM_CUSTOMER_APP_USAGE_AGG]]
- → [[TMP_CUSTOMER_APP_USAGE_AGG]]

