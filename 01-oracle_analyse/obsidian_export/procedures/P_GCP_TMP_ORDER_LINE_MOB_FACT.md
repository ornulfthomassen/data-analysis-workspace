# P_GCP_TMP_ORDER_LINE_MOB_FACT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_GCP_TMP_ORDER_LINE_MOB_FACT` rebuilds the `CLM_ADM.GCP_ORDER_LINE_MOB_FACT` table. It first ensures any previous temporary table (`CLM_ADM.TMP_ORDER_LINE_MOB_FACT`) is dropped. Then, it creates a new temporary table (`CLM_ADM.TMP_ORDER_LINE_MOB_FACT`) by selecting all data from `CCM.VYA_ORDER_LINE_DETAIL_FACT`. A validation step compares the row count of this new temporary table with the existing `CLM_ADM.GCP_ORDER_LINE_MOB_FACT` (if it exists) and raises an error if the new table has significantly fewer rows. If validation passes, the existing `CLM_ADM.GCP_ORDER_LINE_MOB_FACT` is dropped, and the temporary table is renamed to `CLM_ADM.GCP_ORDER_LINE_MOB_FACT`. Finally, a unique index is created on the newly established permanent table, and database statistics are gathered for it.

## Data Sources (Inputs)
- ← [[CCM.VYA_ORDER_LINE_DETAIL_FACT]]
- ← [[GCP_ORDER_LINE_MOB_FACT]]

## Target Tables (Outputs)
- → [[TMP_ORDER_LINE_MOB_FACT]]
- → [[GCP_ORDER_LINE_MOB_FACT]]

