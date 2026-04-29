# TAB_INDEX_UNUSABLE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Sets all indexes (including partitioned and subpartitioned indexes) belonging to a specified table to an unusable state. It iterates through all indexes associated with the input table name and executes an 'ALTER INDEX ... UNUSABLE' command for each, gracefully handling any errors.

## Data Sources (Inputs)
- ← [[USER_INDEXES]]
| Column Name |
|---|
| INDEX_NAME |
| TABLE_NAME |
- ← [[USER_IND_PARTITIONS]]
| Column Name |
|---|
| INDEX_NAME |
| PARTITION_NAME |
| STATUS |
- ← [[USER_IND_SUBPARTITIONS]]
| Column Name |
|---|
| INDEX_NAME |
| PARTITION_NAME |
| SUBPARTITION_NAME |
| STATUS |

