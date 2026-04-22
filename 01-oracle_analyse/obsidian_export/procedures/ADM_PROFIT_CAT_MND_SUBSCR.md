# ADM_PROFIT_CAT_MND_SUBSCR

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `ADM_PROFIT_CAT_MND_SUBSCR`, calculates and categorizes adjusted net revenue for mobile subscriptions on a monthly basis. It retrieves subscription, fee, and usage data from various data warehousing sources for a specified month (or the previous month if not specified). It then aggregates and transforms this data into several intermediate tables, computes a 'NET_REVENUE_ADJUSTED' value for each subscription, and finally assigns a profit category based on cumulative distribution of this adjusted revenue. The results, including these categories, are stored in a permanent, partitioned historical table.

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
- → [[ADM_PROFIT_CAT_MND_HIST]]
- → [[ADM_PROFIT_CAT_MND_PERIOD]]
- → [[ADM_PROFIT_CAT_MND_SUBS]]
- → [[ADM_PROFIT_CAT_MND_FEE]]
- → [[ADM_PROFIT_CAT_MND_USE]]
- → [[ADM_PROFIT_CAT_MND_USE_ROAMING]]
- → [[ADM_PROFIT_CAT_MND_REVENUE]]

