# ADM11_SUBSCR_HANDSET_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The Oracle SQL procedure `ADM11_SUBSCR_HANDSET_HIST` is designed to manage and populate a historical table named `ADM_SUBSCR_HANDSET_HIST` with subscription and handset usage data. It first checks for the existence of this table. If the table does not exist, it creates it with defined columns and partitioning by `PERIOD_MONTH_KEY`, along with several indexes. Subsequently, for a specified range of months (`V_YYYYMM_FRA` to `V_YYYYMM_TIL`), it iterates through each month. For every month, it checks if the corresponding table partition exists; if not, it creates it. Finally, it populates the `ADM_SUBSCR_HANDSET_HIST` table for that specific month by extracting, transforming (cleaning, uppercasing, trimming), and joining data from multiple source tables, selecting the most recent handset information for each subscription.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CCDW.SUBSCRIPTION_HANDSET]]
- ← [[CLM_CCM.CCM_TERMINAL_TAC]]
- ← [[CLM_CCM.CCM_TERMINAL_DETAIL]]
- ← [[SYS.ALL_OBJECTS]]

## Target Tables (Outputs)
- → [[ADM_SUBSCR_HANDSET_HIST]]

