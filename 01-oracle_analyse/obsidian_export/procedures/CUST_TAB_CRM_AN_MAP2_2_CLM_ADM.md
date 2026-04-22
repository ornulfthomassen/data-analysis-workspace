# CUST_TAB_CRM_AN_MAP2_2_CLM_ADM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The Oracle SQL procedure `CUST_TAB_CRM_AN_MAP2_2_CLM_ADM` is designed to migrate and transform customer segmentation (MAP2_SEGMENT) data for a specified range of months. It takes source data from a table in the `CRM_ANALYSE` schema (identified by `P_TABLE_OLD`) and populates a partitioned target table in the `CLM_ADM` schema (identified by `P_TABLE_NEW`). For each month within the defined range, the procedure: checks for or creates a partition in the target table; creates a temporary staging table (`P_TMP_TABLE`); populates this temporary table by joining the source data with a customer mapping table (`ADM_CUSTOMER_MAPPING_YYYYMM`) and performing data transformations; and then exchanges the populated temporary table with the corresponding partition in the permanent target table. It also logs the migration process (start/end times, row counts, status) into the `ADM_MIGRATE_LOG` table, analyzes statistics for the new partition, and grants SELECT privileges on the target table. Error handling is included for missing source/target tables or other runtime exceptions.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CRM_ANALYSE.<P_TABLE_OLD>]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_<PERIOD_MONTH_KEY>]]
- ← [[ADM_MIGRATE_LOG]]

## Target Tables (Outputs)
- → [[CLM_ADM.<P_TABLE_NEW>]]
- → [[ADM_MIGRATE_LOG]]
- → [[CLM_ADM.<P_TMP_TABLE>]]

