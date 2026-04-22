# P_ADM_PROFIT_CAT_MND_SUBS_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, P_ADM_PROFIT_CAT_MND_SUBS_HIST, performs a monthly (or period-based) ETL process to analyze mobile subscription profitability. It calculates and aggregates subscription details, fees, national usage, roaming usage, and adjusted revenue for mobile telephony customers. Subscriptions are then categorized based on their adjusted revenue's cumulative distribution (CUME_DIST) for both postpaid and prepaid types. The procedure builds several intermediate permanent tables and uses a temporary staging table to populate a partitioned historical table, ADM_PROFIT_CAT_MND_SUBS_HIST, by exchanging partitions.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[STLOG.ST_AGG]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.SUBSCR_FEE_MONTH_FACT_V]]
- ← [[GALAXY.TRAFFIC_MONTH_FACT_V]]
- ← [[CCDW_USAGE.MOBILE_ROAMING_DAILY]]
- ← [[ADM_PROFIT_CAT_MND_PERIOD]]
- ← [[ADM_PROFIT_CAT_MND_SUBS]]
- ← [[ADM_PROFIT_CAT_MND_FEE]]
- ← [[ADM_PROFIT_CAT_MND_USE]]
- ← [[ADM_PROFIT_CAT_MND_USE_ROAMING]]
- ← [[ADM_PROFIT_CAT_MND_REVENUE]]

## Target Tables (Outputs)
- → [[ADM_PROFIT_CAT_MND_PERIOD]]
- → [[ADM_PROFIT_CAT_MND_SUBS]]
- → [[ADM_PROFIT_CAT_MND_FEE]]
- → [[ADM_PROFIT_CAT_MND_USE]]
- → [[ADM_PROFIT_CAT_MND_USE_ROAMING]]
- → [[ADM_PROFIT_CAT_MND_REVENUE]]
- → [[TMP_PROFIT_CAT_MND_SUBS_HIST]]
- → [[ADM_PROFIT_CAT_MND_SUBS_HIST]]

