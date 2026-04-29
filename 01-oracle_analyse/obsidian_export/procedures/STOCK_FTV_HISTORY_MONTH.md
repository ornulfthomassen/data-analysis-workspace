# STOCK_FTV_HISTORY_MONTH

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure automates the monthly archiving and maintenance of detailed and aggregated stock history data. For a specified month or range of months (defaulting to the previous month), it dynamically manages partitions in two permanent history tables: 'STOCK_FTV_HISTORY_MONTH_DET' and 'STOCK_FTV_HISTORY_MONTH_AGG'. It first ensures the corresponding source tables ('STOCK_FTV_HISTORY_DET', 'STOCK_FTV_HISTORY_AGG') are populated for the current month by calling an external procedure. Then, it drops the existing monthly partition in the target history table (if it exists), adds a new empty partition for the current month, and uses an 'ALTER TABLE ... EXCHANGE PARTITION' statement to efficiently move all data from the populated source table into the newly created monthly partition of the target history table. Finally, it gathers statistics on the newly populated partitions.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| DATE_KEY |
| YEAR_MONTH_NUMBER |
- ← [[DUAL]]
- ← [[CLM_ADM.STOCK_FTV_HISTORY_DET]]
- ← [[CLM_ADM.STOCK_FTV_HISTORY_AGG]]

## Target Tables (Outputs)
- → [[CLM_ADM.STOCK_FTV_HISTORY_MONTH_DET]]
- → [[CLM_ADM.STOCK_FTV_HISTORY_MONTH_AGG]]

