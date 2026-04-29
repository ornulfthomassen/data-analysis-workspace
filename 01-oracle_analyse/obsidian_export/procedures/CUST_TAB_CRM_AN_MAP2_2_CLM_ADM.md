# CUST_TAB_CRM_AN_MAP2_2_CLM_ADM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure orchestrates a data migration process for specific time periods (YYYYMM range). It dynamically creates a target partitioned table if it doesn't exist, or adds partitions to it. For each period, it reads data from a source table (`P_TABLE_OLD`) in the `CRM_ANALYSE` schema, joins it with a customer mapping table (`ADM_CUSTOMER_MAPPING_YYYYMM`) in the `CLM_ADM` schema, and loads the combined data into a temporary staging table (`P_TMP_TABLE`). Finally, it performs a partition exchange, moving the data from the temporary table into the corresponding partition of the permanent target table (`P_TABLE_NEW`) in the `CLM_ADM` schema. The entire process, including start and end times and row counts, is logged in `ADM_MIGRATE_LOG`.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| RELATIVE_MONTH |
- ← [[ADM_MIGRATE_LOG]]
| Column Name |
|---|
| AML_ID |
- ← [[CRM_ANALYSE.<P_TABLE_OLD>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CU_KURT_ID_OWNER |
| EM_CLASSIFICATION |
| MAP_SEGMENT |
| RUN_DATE |
| P_MAP_SEGMENT1 |
| P_MAP_SEGMENT6 |
| P_MAP_SEGMENT5 |
| P_MAP_SEGMENT4 |
| P_MAP_SEGMENT3 |
| P_MAP_SEGMENT2 |
| EM_PROBABILITY |
| IND_MAP_SEGMENT6 |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_<PERIOD_MONTH_KEY>]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |

## Target Tables (Outputs)
- → [[CLM_ADM.<P_TABLE_NEW>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| MAP2_SEGMENT_ID |
| MAP2_SEGMENT_NAME |
| RUN_DATE |
| P_MAP_SEGMENT1 |
| P_MAP_SEGMENT6 |
| P_MAP_SEGMENT5 |
| P_MAP_SEGMENT4 |
| P_MAP_SEGMENT3 |
| P_MAP_SEGMENT2 |
| EM_PROBABILITY |
| IND_MAP_SEGMENT6 |
- → [[<P_TMP_TABLE>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| MAP2_SEGMENT_ID |
| MAP2_SEGMENT_NAME |
| RUN_DATE |
| P_MAP_SEGMENT1 |
| P_MAP_SEGMENT6 |
| P_MAP_SEGMENT5 |
| P_MAP_SEGMENT4 |
| P_MAP_SEGMENT3 |
| P_MAP_SEGMENT2 |
| EM_PROBABILITY |
| IND_MAP_SEGMENT6 |
- → [[ADM_MIGRATE_LOG]]
| Column Name |
|---|
| AML_ID |
| MIGRATE_DTTM_START |
| MIGRATE_DTTM_END |
| FROM_TABLE |
| TO_TABLE |
| FROM_NUM_COLUMNS |
| TO_NUM_COLUMNS |
| PERIOD_MONTH_KEY |
| FROM_NUM_ROWS |
| TO_NUM_ROWS |
| STATUS |
| ERROR_MESSAGE |

