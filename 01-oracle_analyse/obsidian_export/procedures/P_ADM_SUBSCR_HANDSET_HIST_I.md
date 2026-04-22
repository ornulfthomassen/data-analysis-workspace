# P_ADM_SUBSCR_HANDSET_HIST_I

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure populates or updates monthly partitions of the 'ADM_SUBSCR_HANDSET_HIST_I' table. It collects historical subscription handset data for a given month (specified by 'V_YYYYMM') from various source tables. It first ensures the target partition exists, then creates a temporary staging table ('TMP_SUBSCR_HANDSET_HIST_I') with the processed data. Finally, it uses an 'ALTER TABLE ... EXCHANGE PARTITION' statement to efficiently load the data from the temporary table into the corresponding partition of the 'ADM_SUBSCR_HANDSET_HIST_I' table, followed by statistics computation. It includes checks for source data availability and robust error handling.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY_I]]
- ← [[LIVE.SUBSCRIPTION_HANDSET_HIST]]
- ← [[CCDW.HANDSET_TYPE]]
- ← [[CCDW.HANDSET_TYPE_EXT]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CCDW.SUBSCRIPTION_HANDSET]]

## Target Tables (Outputs)
- → [[ADM_SUBSCR_HANDSET_HIST_I]]
- → [[TMP_SUBSCR_HANDSET_HIST_I]]

