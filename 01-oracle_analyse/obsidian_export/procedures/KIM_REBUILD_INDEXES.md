# KIM_REBUILD_INDEXES

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Identifies invalid or unusable indexes associated with tables whose names start with 'KIM_' for the current user. For each identified invalid index (whether unpartitioned, partitioned, or subpartitioned), it performs an 'ALTER INDEX REBUILD' operation to make it usable, logging the process and summary.

## Data Sources (Inputs)
- ← [[USER_INDEXES]]
| Column Name |
|---|
| TABLE_NAME |
| INDEX_NAME |
| STATUS |
| INDEX_TYPE |
| UNIQUENESS |
| NUM_ROWS |
| DEGREE |
| PARTITIONED |
| TABLESPACE_NAME |
- ← [[USER_IND_PARTITIONS]]
| Column Name |
|---|
| INDEX_NAME |
| PARTITION_NAME |
| STATUS |
| NUM_ROWS |
| TABLESPACE_NAME |
- ← [[USER_IND_SUBPARTITIONS]]
| Column Name |
|---|
| INDEX_NAME |
| SUBPARTITION_NAME |
| STATUS |
| NUM_ROWS |
| TABLESPACE_NAME |

