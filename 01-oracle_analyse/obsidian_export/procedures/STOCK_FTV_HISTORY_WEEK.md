# STOCK_FTV_HISTORY_WEEK

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Generates weekly historical stock data by processing a specified or default range of weeks. For each week, it performs housekeeping on partitioned target tables (`CLM_ADM.STOCK_FTV_HISTORY_WEEK_DET`, `CLM_ADM.STOCK_FTV_HISTORY_WEEK_AGG`) by dropping and recreating the corresponding weekly partitions. It then calls an external procedure (`CLM_ADM.STOCK_FTV_HISTORY`) to populate temporary 'source' tables (`CLM_ADM.STOCK_FTV_HISTORY_DET`, `CLM_ADM.STOCK_FTV_HISTORY_AGG`) for the current week. Finally, it uses `ALTER TABLE ... EXCHANGE PARTITION` to effectively move the data from these temporary source tables into the newly created weekly partitions of the target historical tables, and gathers statistics on the updated partitions.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[DUAL]]
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| DATE_KEY |
| YEAR_WEEK_NUMBER |
- ← [[ALL_TAB_PARTITIONS]]
| Column Name |
|---|
| TABLE_NAME |
| PARTITION_NAME |
- ← [[CLM_ADM.STOCK_FTV_HISTORY_DET]]
- ← [[CLM_ADM.STOCK_FTV_HISTORY_AGG]]

## Target Tables (Outputs)
- → [[CLM_ADM.STOCK_FTV_HISTORY_WEEK_DET]]
- → [[CLM_ADM.STOCK_FTV_HISTORY_WEEK_AGG]]

