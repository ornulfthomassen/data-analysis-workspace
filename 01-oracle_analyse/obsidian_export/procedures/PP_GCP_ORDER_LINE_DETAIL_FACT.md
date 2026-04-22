# PP_GCP_ORDER_LINE_DETAIL_FACT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure orchestrates the monthly loading and maintenance of subpartitions within the `GCP_ORDER_LINE_DETAIL_FACT` table. It iterates through a specified date range (YYYYMM), ensuring that a partition exists for each month in the target table, with several predefined subpartitions (AO, FT, HW, NB, SO). For each enabled subpartition, it calls an external procedure (`CLM_ADM.PP_GCP_TMP_ORDER_LINE_DETAIL_FACT`) to populate a temporary staging table (`TMP_ORDER_LINE_DETAIL_FACT`) with relevant data. Finally, it performs a 'partition exchange' operation, swapping the loaded data from the temporary table into the corresponding subpartition of the `GCP_ORDER_LINE_DETAIL_FACT` table. This method is employed for efficient and incremental data loading and updates in a partitioned data warehouse fact table.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CCM.VYA_ORDER_LINE_DETAIL_FACT]]

## Target Tables (Outputs)
- → [[GCP_ORDER_LINE_DETAIL_FACT]]
- → [[TMP_ORDER_LINE_DETAIL_FACT]]

