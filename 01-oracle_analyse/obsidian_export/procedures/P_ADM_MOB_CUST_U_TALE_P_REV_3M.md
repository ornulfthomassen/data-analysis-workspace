# P_ADM_MOB_CUST_U_TALE_P_REV_3M

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure calculates and aggregates mobile customer usage and revenue statistics for a specified month (or the previous month if not specified). It gathers detailed subscription, revenue, and usage data for 'Mobiltelefoni, PostPaid' and 'Mobiltelefoni, PrePaid' product types within specific market areas (2 and 4). The aggregated results are first stored in a temporary staging table, and then efficiently loaded into a permanent, partitioned target table by exchanging partitions. The procedure includes checks for source data availability, handles existing partitions, and performs error logging.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MOB_SUBS_REVENUE_3MO]]
- ← [[CLM_ADM.ADM_MOB_SUBSCRIPTION_CORE]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[TMP_MOB_CUST_U_TALE_P_REV_3MO]]
- → [[ADM_MOB_CUST_U_TALE_P_REV_3MO]]

