# P_GCP_TMP_ORDER_LINE_DETAIL_FACT_HW

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure implements a "rebuild" strategy for the `GCP_ORDER_LINE_MOB_FACT_HW` table. It first drops any existing temporary table (`TMP_ORDER_LINE_MOB_FACT_HW`). Then, it creates a new temporary table (`CLM_ADM.TMP_ORDER_LINE_MOB_FACT_HW`) by copying all data from the `CCM.VYA_ORDER_LINE_DETAIL_FACT_HW` view. A safety check is performed to ensure the newly created temporary table has at least as many rows as the current `CLM_ADM.GCP_ORDER_LINE_MOB_FACT_HW` table (if it exists). If the row count check passes, the procedure drops the old `CLM_ADM.GCP_ORDER_LINE_MOB_FACT_HW` table and renames the temporary table to `CLM_ADM.GCP_ORDER_LINE_MOB_FACT_HW`. Finally, it creates a unique index and primary key on the `ORDER_LINE_KEY` column of the new `CLM_ADM.GCP_ORDER_LINE_MOB_FACT_HW` table, gathers statistics, and grants SELECT privileges to the CCM user. If the row count check fails, an error is raised, and the existing `GCP_ORDER_LINE_MOB_FACT_HW` table is preserved.

## Data Sources (Inputs)
- ← [[CCM.VYA_ORDER_LINE_DETAIL_FACT_HW]]
- ← [[CLM_ADM.TMP_ORDER_LINE_MOB_FACT_HW]]
- ← [[CLM_ADM.GCP_ORDER_LINE_MOB_FACT_HW]]

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_ORDER_LINE_MOB_FACT_HW]]
- → [[CLM_ADM.GCP_ORDER_LINE_MOB_FACT_HW]]

