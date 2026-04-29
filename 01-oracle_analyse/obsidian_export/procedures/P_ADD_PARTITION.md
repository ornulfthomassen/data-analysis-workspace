# P_ADD_PARTITION

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure is designed to dynamically add missing partitions to a specified partitioned table (`P_TABLE`) within the current schema. It identifies gaps in partitioning for the last 30 days (either by month or day, determined by `P_PERIOD_KEY`) by comparing entries in `GALAXY.DATE_DIM_MV` against existing partitions listed in `SYS.ALL_OBJECTS`. If missing partitions are found, it executes an `ALTER TABLE ... ADD PARTITION` statement to create them.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| SUBOBJECT_NAME |
| OWNER |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DATE_KEY |
| DAY |

## Target Tables (Outputs)
- → [[[Dynamic Table from P_TABLE parameter]]]
| Column Name |
|---|
| [partitioning_key_column] |

