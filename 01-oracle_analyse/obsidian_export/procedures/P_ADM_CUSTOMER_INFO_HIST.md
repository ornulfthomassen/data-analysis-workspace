# P_ADM_CUSTOMER_INFO_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The `P_ADM_CUSTOMER_INFO_HIST` procedure loads or updates historical customer and household information for a specified month (P_YYYYMM) into a partitioned table named `ADM_CUSTOMER_INFO_HIST`. It first validates the existence and status of required source data for the given month. If source data is valid, it manages partitions in the target table, ensuring the target partition exists. It then creates a temporary staging table (`TMP_CUSTOMER_INFO_HIST`) by selecting and transforming data from various customer and household dimension tables. Finally, it uses an `ALTER TABLE ... EXCHANGE PARTITION` statement to efficiently replace or load the data from the temporary staging table into the corresponding partition of `ADM_CUSTOMER_INFO_HIST`, followed by gathering statistics for performance optimization.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_KURT]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_HIST]]
- ← [[CLM_ADM.ADM_HOUSEHOLD_INFO_KURT]]
- ← [[CLM_ADM.ADM_HOUSEHOLD_MAPPING_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]

## Target Tables (Outputs)
- → [[ADM_CUSTOMER_INFO_HIST]]
- → [[TMP_CUSTOMER_INFO_HIST]]

