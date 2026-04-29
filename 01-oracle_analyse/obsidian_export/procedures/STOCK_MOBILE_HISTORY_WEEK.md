# STOCK_MOBILE_HISTORY_WEEK

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Manages weekly mobile stock history data. For a specified range of weeks, it first determines the weeks to process (defaulting to the previous week if not provided or if current/future weeks are specified). For each week, it dynamically drops and re-adds a partition in the permanent weekly detailed and aggregated history tables (`STOCK_MOBILE_HISTORY_WEEK_DET` and `STOCK_MOBILE_HISTORY_WEEK_AGG`). It then calls an external procedure (`CLM_ADM.STOCK_MOBILE_HISTORY`) to generate temporary stock data, which is written to `STOCK_MOBILE_HISTORY_DET` and `STOCK_MOBILE_HISTORY_AGG`. Finally, it uses an `ALTER TABLE ... EXCHANGE PARTITION` statement to atomically move the data from these temporary tables into the newly created weekly partitions of the permanent history tables, effectively emptying the temporary source tables. The procedure also logs the load status to `CRM_ANALYSE.ADM_LOAD_HISTORY` and gathers table statistics for the new partitions.

## Data Sources (Inputs)
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
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_DET]]
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_AGG]]

## Target Tables (Outputs)
- → [[CLM_ADM.STOCK_MOBILE_HISTORY_WEEK_DET]]
- → [[CLM_ADM.STOCK_MOBILE_HISTORY_WEEK_AGG]]
- → [[CLM_ADM.STOCK_MOBILE_HISTORY_DET]]
- → [[CLM_ADM.STOCK_MOBILE_HISTORY_AGG]]
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| PERIOD_KEY |
| STATUS_MESSAGE |
| DESCRIPTION |
| WARNING |

