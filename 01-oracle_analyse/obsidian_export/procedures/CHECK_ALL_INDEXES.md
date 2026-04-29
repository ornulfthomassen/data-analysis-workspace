# CHECK_ALL_INDEXES

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Identifies and rebuilds unusable indexes, including their partitions and subpartitions, for a specified table owner and table name.

## Data Sources (Inputs)
- ← [[ALL_IND_PARTITIONS]]
| Column Name |
|---|
| index_owner |
| index_name |
| partition_name |
| status |
- ← [[ALL_IND_SUBPARTITIONS]]
| Column Name |
|---|
| index_owner |
| index_name |
| subpartition_name |
| status |
- ← [[ALL_INDEXES]]
| Column Name |
|---|
| owner |
| index_name |
| table_owner |
| table_name |
| status |

