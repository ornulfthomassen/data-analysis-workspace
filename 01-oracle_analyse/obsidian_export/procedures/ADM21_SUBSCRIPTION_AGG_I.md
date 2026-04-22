# ADM21_SUBSCRIPTION_AGG_I

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `ADM21_SUBSCRIPTION_AGG_I`, is designed to create and incrementally populate a partitioned aggregate table named `ADM_SUBSCRIPTION_AGG_I`. Its main purpose is to aggregate mobile subscription usage data (such as megabytes, MMS, SMS, and voice duration/number) and associated revenue/fees (gross, net, discounts) for specific monthly periods. The procedure iterates through a range of months, creating new partitions in the target table if they don't exist and then inserting aggregated data from various fact and history tables. It also handles the creation of local partitioned indexes and gathers statistics for the target table and its new partitions.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CRM_ANALYSE.TMP_TRAFFIC_DATA]]
- ← [[GALAXY.TRAFFIC_MONTH_FACT_V]]
- ← [[STLOG.ST_AGG]]
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY_I]]
- ← [[GALAXY.SUBSCR_FEE_MONTH_FACT_V]]
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[DUAL]]

## Target Tables (Outputs)
- → [[ADM_SUBSCRIPTION_AGG_I]]

