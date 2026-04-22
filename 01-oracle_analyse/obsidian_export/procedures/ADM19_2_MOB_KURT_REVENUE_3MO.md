# ADM19_2_MOB_KURT_REVENUE_3MO

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The Oracle SQL procedure 'ADM19_2_MOB_KURT_REVENUE_3MO' calculates and stores aggregated mobile subscription revenue data. It processes detailed revenue information for specified monthly periods, computing various metrics such as net revenue, initiation fees, periodic fees, usage amounts, number of subscriptions, and product types. These aggregations are performed at two levels ('Owner' and 'User' IDs) and for different market area and product type combinations (all mobile products vs. mobile voice products only). The procedure dynamically creates monthly partitions for six target tables if they don't exist, then inserts the calculated aggregates into these permanent, partitioned tables. It also gathers table statistics and logs operational history.

## Data Sources (Inputs)
- ← [[ADM_MOB_SUBS_REVENUE_3MO]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[ADM_MOB_KURT_O_TOTAL_REV_3MO]]
- → [[ADM_MOB_KURT_O_TALE_REV_3MO]]
- → [[ADM_MOB_KURT_U_TOTAL_REV_3MO]]
- → [[ADM_MOB_KURT_U_TALE_REV_3MO]]
- → [[ADM_MOB_KURT_U_TOT_P_REV_3MO]]
- → [[ADM_MOB_KURT_U_TALE_P_REV_3MO]]

