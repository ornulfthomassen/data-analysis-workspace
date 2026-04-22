# CUST_TAB_CRM_ANALYSE_2_CLM_ADM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure serves to migrate and transform customer-related data on a monthly basis. It takes a source table (defined by `P_TABLE_OLD` in the `CRM_ANALYSE` schema) and processes its data into a new, partitioned target table (defined by `P_TABLE_NEW` in the `CLM_ADM` schema). The process dynamically identifies source table columns, creates the target table with a specific structure and partitioning scheme, and then iterates through a range of `PERIOD_MONTH_KEY` values. For each month, it creates a temporary staging table (`P_TMP_TABLE`), populates it with transformed data (including customer key mapping), and then efficiently moves this data into the permanent target table using an `EXCHANGE PARTITION` operation. The procedure also handles logging of migration progress and status in `ADM_MIGRATE_LOG`, manages table statistics, and grants select privileges on the newly created table.

## Data Sources (Inputs)
- ← [[ALL_TAB_COLS]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[SYS.ALL_OBJECTS]]
- ← [[CRM_ANALYSE.<P_TABLE_OLD>]]
- ← [[ADM_MIGRATE_LOG]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_<PERIOD_MONTH_KEY>]]
- ← [[ADM_CUSTOMER_USE]]

## Target Tables (Outputs)
- → [[CLM_ADM.<P_TABLE_NEW>]]
- → [[ADM_MIGRATE_LOG]]
- → [[CLM_ADM.<P_TMP_TABLE>]]

