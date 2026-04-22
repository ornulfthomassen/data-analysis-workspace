# ADM_PROFIT_CAT_SUBSCRIPTION

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure calculates and categorizes subscription-related profit for a specified month (or the previous month if not specified). It processes data related to subscriptions, fees, and usage (both local and roaming) to derive an 'adjusted net revenue' for each subscription. Based on this adjusted revenue, it assigns a profit category using cumulative distribution. The processed and categorized data is then stored as historical records in a partitioned table.

## Data Sources (Inputs)
- ← [[STLOG.ST_AGG]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.SUBSCR_FEE_MONTH_FACT_V]]
- ← [[GALAXY.TRAFFIC_MONTH_FACT_V]]
- ← [[CCDW_USAGE.MOBILE_ROAMING_DAILY]]

## Target Tables (Outputs)
- → [[ADM_PROFIT_CAT_HIST]]
- → [[ADM_PROFIT_CAT_PERIOD]]
- → [[ADM_PROFIT_CAT_SUBS]]
- → [[ADM_PROFIT_CAT_FEE]]
- → [[ADM_PROFIT_CAT_USE]]
- → [[ADM_PROFIT_CAT_USE_ROAMING]]
- → [[ADM_PROFIT_CAT_REVENUE]]

