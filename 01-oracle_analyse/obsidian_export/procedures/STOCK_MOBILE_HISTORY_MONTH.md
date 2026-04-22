# STOCK_MOBILE_HISTORY_MONTH

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `STOCK_MOBILE_HISTORY_MONTH`, processes and manages historical stock mobile data on a monthly basis. For a specified range of months, it dynamically creates and updates partitions in two permanent historical tables: `STOCK_MOBILE_HISTORY_MONTH_DET` (detailed) and `STOCK_MOBILE_HISTORY_MONTH_AGG` (aggregated). It achieves this by first calling an external procedure (`CLM_ADM.STOCK_MOBILE_HISTORY`) which is presumed to generate the current month's detailed and aggregated stock data into temporary staging tables (`STOCK_MOBILE_HISTORY_DET` and `STOCK_MOBILE_HISTORY_AGG`). Subsequently, it performs an `EXCHANGE PARTITION` operation, swapping the newly generated data from these staging tables directly into the corresponding monthly partitions of the permanent historical tables. The procedure also handles dropping existing monthly partitions before adding new ones and gathers statistics for the newly updated partitions.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[SYS.ALL_OBJECTS]]
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_DET]]
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_AGG]]

## Target Tables (Outputs)
- → [[CLM_ADM.STOCK_MOBILE_HISTORY_MONTH_DET]]
- → [[CLM_ADM.STOCK_MOBILE_HISTORY_MONTH_AGG]]

