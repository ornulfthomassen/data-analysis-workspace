# STOCK_MOBILE_HISTORY_MONTH

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure processes historical stock mobile data on a monthly basis. It first determines the processing month(s), typically the previous month. For each identified month, it performs maintenance on two partitioned target tables: `STOCK_MOBILE_HISTORY_MONTH_DET` and `STOCK_MOBILE_HISTORY_MONTH_AGG`, by dropping and then recreating the partition corresponding to that month. It then calls an external procedure (`CLM_ADM.STOCK_MOBILE_HISTORY`) to populate temporary/staging tables (`STOCK_MOBILE_HISTORY_DET` and `STOCK_MOBILE_HISTORY_AGG`) with the relevant stock data for the period. Finally, it uses `ALTER TABLE ... EXCHANGE PARTITION` to efficiently move the data from these staging tables into the newly created monthly partitions of the respective target tables. It also gathers statistics on the updated partitions and logs the load activity using another external procedure (`CRM_ANALYSE.P_ADM_LOAD_HISTORY`).

## Data Sources (Inputs)
- ← [[DUAL]]
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| DATE_KEY |
| YEAR_MONTH_NUMBER |
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_DET]]
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_AGG]]

## Target Tables (Outputs)
- → [[CLM_ADM.STOCK_MOBILE_HISTORY_MONTH_DET]]
- → [[CLM_ADM.STOCK_MOBILE_HISTORY_MONTH_AGG]]

