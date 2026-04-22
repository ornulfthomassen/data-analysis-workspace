# P_ADM_SUBSCR_DET_HIST_DSW

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure calculates and loads historical subscription details, specifically focusing on 'Data Switch' products, into a partitioned master table named `ADM_SUBSCR_DET_HIST_DSW`. For a given month (`V_YYYYMM`), it first checks the availability and integrity of source data. If checks pass, it creates or ensures the existence of a partition for that month in the target table. It then builds a temporary staging table (`TMP_SUBSCR_DET_HIST_DSW`) containing transformed and aggregated subscription metrics (like `NO_DAYS_FIRST_START`, `NO_DSWITCH`) by joining various dimension and fact tables. Finally, it uses a partition exchange operation to atomically replace the existing or new partition in `ADM_SUBSCR_DET_HIST_DSW` with the data from the temporary staging table, and updates table statistics. The procedure includes robust error handling and logging.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]

## Target Tables (Outputs)
- → [[TMP_SUBSCR_DET_HIST_DSW]]
- → [[ADM_SUBSCR_DET_HIST_DSW]]

