# P_GCP_TMP_ORDER_LINE_DETAIL_FACT_HW

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure rebuilds the `GCP_ORDER_LINE_MOB_FACT_HW` table in the `CLM_ADM` schema. It first creates a temporary staging table (`TMP_ORDER_LINE_MOB_FACT_HW`) by selecting all data from the `CCM.VYA_ORDER_LINE_DETAIL_FACT_HW` view. It then performs a data integrity check by comparing the row count of the newly created temporary table with the existing permanent `GCP_ORDER_LINE_MOB_FACT_HW` table. If the new table has fewer rows, it raises an error. Otherwise, it drops the old `GCP_ORDER_LINE_MOB_FACT_HW` table, renames the temporary table to `GCP_ORDER_LINE_MOB_FACT_HW`, creates a unique index and primary key on it, gathers table statistics, and grants SELECT privileges to the `CCM` user.

## Data Sources (Inputs)
- ← [[CCM.VYA_ORDER_LINE_DETAIL_FACT_HW]]
- ← [[CLM_ADM.TMP_ORDER_LINE_MOB_FACT_HW]]
- ← [[CLM_ADM.GCP_ORDER_LINE_MOB_FACT_HW]]

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_ORDER_LINE_MOB_FACT_HW]]
- → [[CLM_ADM.GCP_ORDER_LINE_MOB_FACT_HW]]

