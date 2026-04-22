# P_ADM_MOB_CUST_O_TALE_REV_3MO

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure calculates and aggregates mobile customer subscription and revenue data for a specific month (V_YYYYMM). It creates a temporary staging table to process detailed subscription and customer records, performing aggregations like total subscriptions, revenue components, and main subscription types. The aggregated data from this temporary table is then moved into a corresponding partition of a permanent, historized (partitioned) table, `ADM_MOB_CUST_O_TALE_REV_3MO`, using an `EXCHANGE PARTITION` operation. The procedure includes checks for source data availability, handles existing partitions, and logs execution history and errors.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MOB_SUBS_REVENUE_3MO]]
- ← [[CLM_ADM.ADM_MOB_SUBSCRIPTION_CORE]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[TMP_MOB_CUST_O_TALE_REV_3MO]]
- → [[ADM_MOB_CUST_O_TALE_REV_3MO]]

