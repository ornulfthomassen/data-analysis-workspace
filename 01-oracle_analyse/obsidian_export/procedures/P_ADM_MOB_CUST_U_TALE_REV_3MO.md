# P_ADM_MOB_CUST_U_TALE_REV_3MO

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure calculates and aggregates mobile customer subscription and revenue metrics for a specific month (defaulting to the previous month). It first populates an intermediate temporary table (`TMP_MOB_CUST_U_TALE_REV_3MO`) with the aggregated data. Then, it exchanges this temporary table with a specific partition in a permanent, partitioned historical table (`ADM_MOB_CUST_U_TALE_REV_3MO`). The procedure includes checks for the existence and status of source data, ensures the target permanent table exists, and manages the creation or overwrite prevention of partitions within the permanent table. It also gathers statistics and grants select privileges.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_MOB_SUBS_REVENUE_3MO]]
- ← [[CLM_ADM.ADM_MOB_SUBSCRIPTION_CORE]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

## Target Tables (Outputs)
- → [[TMP_MOB_CUST_U_TALE_REV_3MO]]
- → [[ADM_MOB_CUST_U_TALE_REV_3MO]]

