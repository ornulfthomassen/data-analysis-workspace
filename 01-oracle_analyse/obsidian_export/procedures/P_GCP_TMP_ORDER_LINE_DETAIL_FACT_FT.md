# P_GCP_TMP_ORDER_LINE_DETAIL_FACT_FT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Refreshes the `GCP_ORDER_LINE_MOB_FACT_FT` table by creating a temporary copy (`TMP_ORDER_LINE_MOB_FACT_FT`) populated from the `CCM.VYA_ORDER_LINE_DETAIL_FACT_FT` view. It then performs a row count validation, and if successful, replaces the existing permanent table with the new data from the temporary table. Finally, it creates a unique index and gathers statistics on the newly replaced table.

## Data Sources (Inputs)
- ← [[CCM.VYA_ORDER_LINE_DETAIL_FACT_FT]]
- ← [[TMP_ORDER_LINE_MOB_FACT_FT]]
- ← [[GCP_ORDER_LINE_MOB_FACT_FT]]

## Target Tables (Outputs)
- → [[TMP_ORDER_LINE_MOB_FACT_FT]]
- → [[GCP_ORDER_LINE_MOB_FACT_FT]]

