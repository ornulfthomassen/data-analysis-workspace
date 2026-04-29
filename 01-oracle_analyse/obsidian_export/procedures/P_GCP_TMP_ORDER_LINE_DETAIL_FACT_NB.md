# P_GCP_TMP_ORDER_LINE_DETAIL_FACT_NB

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Rebuilds or refreshes the CLM_ADM.GCP_ORDER_LINE_MOB_FACT_NB table. The process involves creating a temporary table (CLM_ADM.TMP_ORDER_LINE_MOB_FACT_NB) by copying all data from CCM.VYA_ORDER_LINE_DETAIL_FACT_NB. It then performs a row count validation, ensuring the new data isn't significantly smaller than the existing permanent table. If validation passes and the permanent table exists, it drops the old CLM_ADM.GCP_ORDER_LINE_MOB_FACT_NB table. Finally, it renames the temporary table to CLM_ADM.GCP_ORDER_LINE_MOB_FACT_NB, creates a unique index on the ORDER_LINE_KEY column, and gathers statistics on the newly rebuilt table.

## Data Sources (Inputs)
- ← [[CCM.VYA_ORDER_LINE_DETAIL_FACT_NB]]
- ← [[CLM_ADM.TMP_ORDER_LINE_MOB_FACT_NB]]
- ← [[CLM_ADM.GCP_ORDER_LINE_MOB_FACT_NB]]

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_ORDER_LINE_MOB_FACT_NB]]
- → [[CLM_ADM.GCP_ORDER_LINE_MOB_FACT_NB]]

