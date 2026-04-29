# TAB_INDEX_REBUILD

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Rebuilds all indexes, including partitioned and subpartitioned indexes, for a specified table. It dynamically constructs and executes ALTER INDEX REBUILD statements, incorporating parallel degree where specified in the index definition.

## Data Sources (Inputs)
- ← [[USER_INDEXES]]
| Column Name |
|---|
| INDEX_NAME |
| TABLE_NAME |
| DEGREE |
- ← [[USER_IND_PARTITIONS]]
| Column Name |
|---|
| INDEX_NAME |
| STATUS |
| PARTITION_NAME |
- ← [[USER_IND_SUBPARTITIONS]]
| Column Name |
|---|
| INDEX_NAME |
| PARTITION_NAME |
| STATUS |
| SUBPARTITION_NAME |

