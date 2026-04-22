# P_ADM_DSL_SUBSCR_DETAIL_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure extracts, transforms, and loads (ETL) DSL/VDSL subscription product detail history for a specified month (P_YYYYMM) into a permanent, partitioned history table named ADM_DSL_SUBSCR_DETAIL_HIST. It begins by validating the availability of necessary source data. It then manages the partitions of the target table, creating one if it doesn't exist. Data is first processed and loaded into a temporary staging table, TMP_DSL_SUBSCR_DETAIL_HIST, which aggregates subscription details, product information (especially speed-related and binding products), and calculates active days. Finally, it uses an efficient ALTER TABLE ... EXCHANGE PARTITION operation to move the data from the temporary table into the corresponding partition of the permanent ADM_DSL_SUBSCR_DETAIL_HIST table, and then gathers statistics on the new partition. The procedure includes robust error handling and logging.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[CCDW.PRODUCT_OFFER]]

## Target Tables (Outputs)
- → [[ADM_DSL_SUBSCR_DETAIL_HIST]]
- → [[TMP_DSL_SUBSCR_DETAIL_HIST]]

