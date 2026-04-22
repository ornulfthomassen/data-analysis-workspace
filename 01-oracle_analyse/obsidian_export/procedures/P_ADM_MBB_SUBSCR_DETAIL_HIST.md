# P_ADM_MBB_SUBSCR_DETAIL_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure calculates and aggregates monthly subscription detail history for mobile broadband products. It first checks the availability of required source data for the specified month. If sources are ready, it constructs a new partition for the permanent `ADM_MBB_SUBSCR_DETAIL_HIST` table if it doesn't exist. It then populates a temporary staging table, `TMP_MBB_SUBSCR_DETAIL_HIST`, with detailed subscription metrics derived from multiple source systems for the target month. Finally, it uses an `ALTER TABLE ... EXCHANGE PARTITION` command to efficiently load the processed data from the temporary table into the newly created or existing partition of the `ADM_MBB_SUBSCR_DETAIL_HIST` table, then analyzes the new partition. It includes error handling and logging capabilities for the process.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[GALAXY.PRODUCT_DIM]]

## Target Tables (Outputs)
- → [[ADM_MBB_SUBSCR_DETAIL_HIST]]
- → [[TMP_MBB_SUBSCR_DETAIL_HIST]]

