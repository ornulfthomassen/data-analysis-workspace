# STOCK_FTV_HISTORY_MONTH

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `STOCK_FTV_HISTORY_MONTH` automates the monthly archiving and partitioning of detailed and aggregated stock history data. It iterates through a specified month range. For each month, it first ensures that corresponding partitions exist in the permanent historical tables (`STOCK_FTV_HISTORY_MONTH_DET` and `STOCK_FTV_HISTORY_MONTH_AGG`), dropping and recreating them if necessary. It then calls another procedure (`CLM_ADM.STOCK_FTV_HISTORY`) to populate intermediate staging tables (`STOCK_FTV_HISTORY_DET` and `STOCK_FTV_HISTORY_AGG`) with data for the month. Finally, it uses `ALTER TABLE ... EXCHANGE PARTITION` to efficiently move the data from these staging tables into the dedicated monthly partitions of the permanent historical tables, thereby maintaining a structured, monthly-partitioned archive of stock details and aggregates.

## Data Sources (Inputs)
- ← [[DUAL]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[STOCK_FTV_HISTORY_DET]]
- ← [[STOCK_FTV_HISTORY_AGG]]

## Target Tables (Outputs)
- → [[STOCK_FTV_HISTORY_MONTH_DET]]
- → [[STOCK_FTV_HISTORY_MONTH_AGG]]

