# P_ADM_SUBSCRIPTION_HISTORY_I

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, P_ADM_SUBSCRIPTION_HISTORY_I, is designed to populate a monthly partition of the `ADM_SUBSCRIPTION_HISTORY_I` table. It first validates the availability of source data for the specified month (V_YYYYMM). If source data is sufficient, it either creates a new partition or checks an existing one in the target table. It then creates a temporary staging table named `TMP_SUBSCRIPTION_HISTORY_I`, populating it with transformed subscription history data, joined with customer mapping and master history details from various source tables. After applying `NOT NULL` constraints to specific columns in the temporary table, it efficiently moves this data into the corresponding monthly partition of the permanent `ADM_SUBSCRIPTION_HISTORY_I` table using an `ALTER TABLE ... EXCHANGE PARTITION` statement. The procedure also handles error logging and analysis of the newly populated partition.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HIST_KURT]]
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HIST_I_KURT]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]

## Target Tables (Outputs)
- → [[ADM_SUBSCRIPTION_HISTORY_I]]
- → [[TMP_SUBSCRIPTION_HISTORY_I]]

