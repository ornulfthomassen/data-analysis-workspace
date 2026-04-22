# P_GCP_TMP_ORDER_LINE_DETAIL_FACT_FT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure refreshes or recreates the 'GCP_ORDER_LINE_MOB_FACT_FT' table. It first creates a temporary table 'TMP_ORDER_LINE_MOB_FACT_FT' by selecting all data from 'CCM.VYA_ORDER_LINE_DETAIL_FACT_FT'. It then performs a data integrity check, raising an error if the new temporary table has fewer rows than the existing 'GCP_ORDER_LINE_MOB_FACT_FT'. If the check passes, it drops the old 'GCP_ORDER_LINE_MOB_FACT_FT' (if it exists) and renames the temporary table to 'GCP_ORDER_LINE_MOB_FACT_FT'. Finally, it creates a unique index on the newly established 'GCP_ORDER_LINE_MOB_FACT_FT' table and gathers statistics.

## Data Sources (Inputs)
- ← [[CCM.VYA_ORDER_LINE_DETAIL_FACT_FT]]
- ← [[GCP_ORDER_LINE_MOB_FACT_FT]]

## Target Tables (Outputs)
- → [[TMP_ORDER_LINE_MOB_FACT_FT]]
- → [[GCP_ORDER_LINE_MOB_FACT_FT]]

