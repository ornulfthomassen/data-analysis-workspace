# P_GCP_TMP_ORDER_LINE_DETAIL_FACT_NB

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure rebuilds or refreshes the `GCP_ORDER_LINE_MOB_FACT_NB` fact table in the `CLM_ADM` schema. It achieves this by first creating an intermediate, temporary staging table (`TMP_ORDER_LINE_MOB_FACT_NB`) populated with all data from the `CCM.VYA_ORDER_LINE_DETAIL_FACT_NB` view. Before replacing the existing permanent table, it performs a critical row count validation: if the newly staged data has fewer rows than the currently active `GCP_ORDER_LINE_MOB_FACT_NB` table, an error is raised. If the validation passes, the old `GCP_ORDER_LINE_MOB_FACT_NB` table is dropped, and the temporary table is renamed to become the new permanent `GCP_ORDER_LINE_MOB_FACT_NB`. Finally, a unique index is created on the new table, and table statistics are gathered.

## Data Sources (Inputs)
- ← [[CCM.VYA_ORDER_LINE_DETAIL_FACT_NB]]
- ← [[CLM_ADM.GCP_ORDER_LINE_MOB_FACT_NB]]

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_ORDER_LINE_MOB_FACT_NB]]
- → [[CLM_ADM.GCP_ORDER_LINE_MOB_FACT_NB]]

