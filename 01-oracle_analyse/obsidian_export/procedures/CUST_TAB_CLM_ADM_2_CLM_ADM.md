# CUST_TAB_CLM_ADM_2_CLM_ADM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure serves as a generalized data migration and transformation utility. It moves and reshapes data from a source table (identified by parameter P_TABLE_OLD) to a new, partitioned target table (identified by parameter P_TABLE_NEW), typically within the CLM_ADM schema. For each month in a specified range, it dynamically constructs the target table (if it doesn't exist) based on the source's column definitions, adding customer key columns. It then reads data from the source, joins it with a month-specific customer mapping table (e.g., CLM_ADM.ADM_CUSTOMER_MAPPING_YYYYMM) to convert customer identifiers to customer keys, and loads the transformed data into a temporary table (P_TMP_TABLE). Finally, it performs a partition exchange, swapping the temporary table's segment into the corresponding partition in the target table. The procedure includes dynamic table and partition management, column introspection, and detailed logging of migration progress in ADM_MIGRATE_LOG.

## Data Sources (Inputs)
- ← [[ALL_TAB_COLS]]
- ← [[SYS.ALL_OBJECTS]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[P_TABLE_OLD]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_YYYYMM]]
- ← [[ADM_MIGRATE_LOG]]

## Target Tables (Outputs)
- → [[P_TABLE_NEW]]
- → [[P_TMP_TABLE]]

