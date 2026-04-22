# P_ADM_HOUSEHOLD_INFO_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_HOUSEHOLD_INFO_HIST`, is designed to load or refresh monthly historical household information into a partitioned table `ADM_HOUSEHOLD_INFO_HIST`. It first performs checks to ensure the availability of source data for the specified month (`P_YYYYMM`). It then manages partitions in the `ADM_HOUSEHOLD_INFO_HIST` table, adding a new partition if it doesn't exist. The core functionality involves creating a temporary table (`TMP_HOUSEHOLD_INFO_HIST`), populating it with processed data derived from other household information tables, and finally exchanging this temporary table with the corresponding partition in the permanent `ADM_HOUSEHOLD_INFO_HIST` table. It also gathers statistics on the newly loaded partition and includes robust error handling and logging.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_HOUSEHOLD_INFO_KURT]]
- ← [[CLM_ADM.ADM_HOUSEHOLD_MAPPING_HIST]]
- ← [[ADM_HOUSEHOLD_INFO_HIST]]

## Target Tables (Outputs)
- → [[ADM_HOUSEHOLD_INFO_HIST]]
- → [[TMP_HOUSEHOLD_INFO_HIST]]

