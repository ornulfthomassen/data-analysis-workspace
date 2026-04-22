# P_ADM_SUBSCR_DETAIL_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The `P_ADM_SUBSCR_DETAIL_HIST` procedure processes and loads monthly subscription detail data into a partitioned historical table. It first validates the availability of source data for a given month (`P_YYYYMM`). If sources are healthy, it dynamically creates a temporary staging table (`TMP_SUBSCR_DETAIL_HIST`) populated with transformed subscription and product details by joining various data sources. Subsequently, it manages partitions within the permanent `ADM_SUBSCR_DETAIL_HIST` table (creating one if it doesn't exist for the target month) and then efficiently moves the data from the temporary table into the corresponding partition using an `ALTER TABLE ... EXCHANGE PARTITION` operation. Finally, it rebuilds local indexes and computes statistics for the updated partition.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[PCAT.PRODUCT_OFFER]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]

## Target Tables (Outputs)
- → [[ADM_SUBSCR_DETAIL_HIST]]
- → [[TMP_SUBSCR_DETAIL_HIST]]

