# ADM11_SUBSCR_HANDSET_HIST_I

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This Oracle PL/SQL procedure, ADM11_SUBSCR_HANDSET_HIST_I, is designed to populate and maintain a partitioned historical table named `CRM_ANALYSE.ADM_SUBSCR_HANDSET_HIST_I`. It processes subscription and handset data for a specified range of months (V_YYYYMM_FRA to V_YYYYMM_TIL). For each month, the procedure checks if the main historical table exists, and if not, it creates it with defined columns, partitioning by `PERIOD_MONTH_KEY`, and associated indexes. It then iterates through the months, ensuring a partition for the current month exists in the historical table. Data for each month is gathered by joining multiple source tables (GALAXY.DATE_DIM_MV, CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY_I, CCDW.SUBSCRIPTION_HANDSET, CLM_CCM.CCM_TERMINAL_TAC, CLM_CCM.CCM_TERMINAL_DETAIL) into a temporary table named `CRM_ANALYSE.TMP_ADM_SUBSCR_HANDSET_HIST_I`. Finally, the data is efficiently moved from the temporary table into the corresponding partition of the `CRM_ANALYSE.ADM_SUBSCR_HANDSET_HIST_I` table using an `ALTER TABLE ... EXCHANGE PARTITION` statement. The procedure also manages index creation/dropping and statistical gathering for performance, and includes error logging via `DBMS_OUTPUT` and `CRM_ANALYSE.P_ADM_LOAD_HISTORY`.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY_I]]
- ← [[CCDW.SUBSCRIPTION_HANDSET]]
- ← [[CLM_CCM.CCM_TERMINAL_TAC]]
- ← [[CLM_CCM.CCM_TERMINAL_DETAIL]]

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_SUBSCR_HANDSET_HIST_I]]
- → [[CRM_ANALYSE.TMP_ADM_SUBSCR_HANDSET_HIST_I]]

