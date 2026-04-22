# P_ADM_SUBSCR_DET_HIST_FFAM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure populates or refreshes a monthly partition of the `ADM_SUBSCR_DET_HIST_FFAM` table. It calculates subscription-related details, specifically focusing on 'FRIFAM' (family plan) products and their active days, for a given month (`P_YYYYMM`). It performs initial checks on the availability of source data and manages the target table's partition (adding it if it doesn't exist, and preventing overwrite if data is already present and `P_OVERWRITE_PARTITION` is 'NO'). It then creates a temporary table (`TMP_SUBSCR_DET_HIST_FFAM`) with the calculated data and efficiently loads this data into the target table's partition using an `ALTER TABLE ... EXCHANGE PARTITION` operation. The procedure also includes robust error handling and logging via calls to `CRM_ANALYSE.P_ADM_LOAD_HISTORY`.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[ADM_SUBSCR_DET_HIST_FFAM]]
- → [[TMP_SUBSCR_DET_HIST_FFAM]]

