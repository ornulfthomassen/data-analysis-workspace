# P_ADD_PARTITION

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADD_PARTITION` is designed to dynamically add missing partitions (either monthly or daily, depending on the `P_PERIOD_KEY` parameter) to a specified partitioned table (`P_TABLE`). It iterates through the last 30 days, identifies any dates or months for which a partition does not yet exist on the target table, and then executes an `ALTER TABLE ... ADD PARTITION` command to create it. It includes an initial check to ensure the target table is already partitioned; otherwise, it raises an application error.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[GALAXY.DATE_DIM_MV]]

