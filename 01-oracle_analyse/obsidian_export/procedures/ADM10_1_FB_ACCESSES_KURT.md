# ADM10_1_FB_ACCESSES_KURT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure dynamically prepares and loads monthly aggregated data into a specific partition of a permanent historical table. It first creates a temporary staging table, populates it with filtered and transformed data from multiple source tables for a given month, then uses a partition exchange mechanism to efficiently replace (or insert into) the corresponding partition in the main historical table, and finally gathers statistics on the updated partition.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[AGR.BMGM_ACCESSES_KURT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CM.AGREEMENT_OFFER]]

## Target Tables (Outputs)
- → [[TMP_ADM_FB_ACCESSES_KURT_HIST]]
- → [[ADM_FB_ACCESSES_KURT_HIST]]

