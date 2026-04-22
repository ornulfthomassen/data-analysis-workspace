# P_ADM_SUBSCR_HANDSET_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_SUBSCR_HANDSET_HIST processes monthly subscriber handset historical data. It first performs data availability checks on several source tables for a given month (V_YYYYMM). If checks pass, it ensures a partition exists for the target table ADM_SUBSCR_HANDSET_HIST. It then creates and populates a temporary staging table, TMP_SUBSCR_HANDSET_HIST, by selecting and transforming data from various source systems related to subscriptions and handset types. Finally, it atomically loads the data from the temporary table into the corresponding partition of the permanent ADM_SUBSCR_HANDSET_HIST table using an ALTER TABLE ... EXCHANGE PARTITION operation. This ensures efficient and atomic data loading for partitioned historical data.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[LIVE.SUBSCRIPTION_HANDSET_HIST]]
- ← [[CCDW.HANDSET_TYPE]]
- ← [[CCDW.HANDSET_TYPE_EXT]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CCDW.SUBSCRIPTION_HANDSET]]

## Target Tables (Outputs)
- → [[ADM_SUBSCR_HANDSET_HIST]]
- → [[TMP_SUBSCR_HANDSET_HIST]]

