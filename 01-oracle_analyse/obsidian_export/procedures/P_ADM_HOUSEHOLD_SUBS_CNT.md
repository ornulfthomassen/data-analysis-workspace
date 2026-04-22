# P_ADM_HOUSEHOLD_SUBS_CNT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADM_HOUSEHOLD_SUBS_CNT` calculates and aggregates household subscription counts and related metrics for a given period (YYYYMM). It first validates the availability of source data for the specified period. It then dynamically manages partitions for the target table `ADM_HOUSEHOLD_SUBS_CNT`, adding a new partition if it doesn't exist. The core logic involves aggregating customer and subscription history data into a temporary table (`TMP_HOUSEHOLD_SUBS_CNT`) based on various subscription types and brands. Finally, it uses an efficient `EXCHANGE PARTITION` operation to move the data from the temporary table into the corresponding partition of the permanent `ADM_HOUSEHOLD_SUBS_CNT` table, updates statistics, and logs the process history.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]

## Target Tables (Outputs)
- → [[TMP_HOUSEHOLD_SUBS_CNT]]
- → [[ADM_HOUSEHOLD_SUBS_CNT]]

