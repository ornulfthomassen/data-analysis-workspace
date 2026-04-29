# P_GCP_TMP_ORDER_LINE_MOB_FACT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure replaces the permanent table 'CLM_ADM.GCP_ORDER_LINE_MOB_FACT' with a fresh copy derived from the 'CCM.VYA_ORDER_LINE_DETAIL_FACT' view. It creates a temporary table, populates it, performs a row count validation to ensure the new data set is not smaller than the existing one, then swaps the temporary table with the permanent one, creates a unique index on 'ORDER_LINE_KEY', and finally gathers statistics on the new permanent table.

## Data Sources (Inputs)
- ← [[CCM.VYA_ORDER_LINE_DETAIL_FACT]]
- ← [[CLM_ADM.TMP_ORDER_LINE_MOB_FACT]]
- ← [[CLM_ADM.GCP_ORDER_LINE_MOB_FACT]]

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_ORDER_LINE_MOB_FACT]]
- → [[CLM_ADM.GCP_ORDER_LINE_MOB_FACT]]

