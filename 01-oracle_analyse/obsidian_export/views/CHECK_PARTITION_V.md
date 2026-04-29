# CHECK_PARTITION_V

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies the latest partition key (formatted as YYYYMM) for specific partitioned tables owned by 'CLM_ADM'. It filters for tables that use 'PERIOD_MONTH_KEY' as a partition column and have partition keys greater than '202511'.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_NAME |
| SUBOBJECT_NAME |
| OWNER |
| OBJECT_TYPE |
- ← [[SYS.ALL_PART_KEY_COLUMNS]]
| Column Name |
|---|
| NAME |
| OWNER |
| COLUMN_NAME |

