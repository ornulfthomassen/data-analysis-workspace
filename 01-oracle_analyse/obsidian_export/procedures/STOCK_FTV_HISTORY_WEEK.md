# STOCK_FTV_HISTORY_WEEK

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure processes historical stock (FTV) data on a weekly basis. It iterates through a specified range of weeks, typically from a past week up to the previous week (excluding the current week). For each week, it dynamically manages partitions within two permanent target tables: `STOCK_FTV_HISTORY_WEEK_DET` (for detailed data) and `STOCK_FTV_HISTORY_WEEK_AGG` (for aggregated data). It drops and then re-adds a partition for the current processing week in both target tables. It then calls an external procedure `CLM_ADM.STOCK_FTV_HISTORY` (which is assumed to populate staging tables) and subsequently uses `ALTER TABLE ... EXCHANGE PARTITION` to efficiently move the detailed and aggregated stock data from these staging tables (`STOCK_FTV_HISTORY_DET` and `STOCK_FTV_HISTORY_AGG`) into the newly created partitions of the respective weekly history tables. Finally, it commits the changes and gathers statistics on the updated partitions.

## Data Sources (Inputs)
- ← [[DUAL]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[SYS.ALL_OBJECTS]]
- ← [[STOCK_FTV_HISTORY_DET]]
- ← [[STOCK_FTV_HISTORY_AGG]]

## Target Tables (Outputs)
- → [[STOCK_FTV_HISTORY_WEEK_DET]]
- → [[STOCK_FTV_HISTORY_WEEK_AGG]]
- → [[STOCK_FTV_HISTORY_DET]]
- → [[STOCK_FTV_HISTORY_AGG]]

