# P_ADM_SUBSCR_DET_HIST_FB

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_SUBSCR_DET_HIST_FB`, calculates and stores family bonus-related subscription details for a specific month (P_YYYYMM) into a partitioned historical table. It performs initial checks to ensure the availability of necessary source data. It manages partitions in the target table `ADM_SUBSCR_DET_HIST_FB`, either creating a new one or verifying an existing one for the target month. The core logic involves populating a temporary staging table (`TMP_SUBSCR_DET_HIST_FB`) with computed metrics by joining various data warehouse tables (subscription history, month dimensions, subscribed products, and product dimensions). Finally, it uses an `ALTER TABLE ... EXCHANGE PARTITION` statement to efficiently load the processed data from the staging table into the corresponding partition of the permanent target table and updates statistics. The procedure includes robust error handling and logging.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]

## Target Tables (Outputs)
- → [[ADM_SUBSCR_DET_HIST_FB]]
- → [[TMP_SUBSCR_DET_HIST_FB]]

