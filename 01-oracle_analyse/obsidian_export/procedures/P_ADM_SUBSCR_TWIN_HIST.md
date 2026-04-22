# P_ADM_SUBSCR_TWIN_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADM_SUBSCR_TWIN_HIST` calculates and loads monthly historical data related to subscriber 'twin' services (such as twin SIMs or data cards) and their associated handsets into a partitioned permanent table. It processes data for a specific month (`P_YYYYMM`) by joining various operational and dimensional tables. The processed data is staged in a temporary table, `TMP_SUBSCR_TWIN_HIST`, before being efficiently loaded into the corresponding partition of the `ADM_SUBSCR_TWIN_HIST` table using an `EXCHANGE PARTITION` operation. The procedure includes preliminary checks for source data availability and target table existence, and prevents overwriting existing partition data unless explicitly authorized.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[LIVE.SUBSCRIPTION_HANDSET_HIST]]
- ← [[CCDW.HANDSET_TYPE]]
- ← [[CCDW.HANDSET_TYPE_EXT]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[ADM_SUBSCR_TWIN_HIST]]
- → [[TMP_SUBSCR_TWIN_HIST]]

