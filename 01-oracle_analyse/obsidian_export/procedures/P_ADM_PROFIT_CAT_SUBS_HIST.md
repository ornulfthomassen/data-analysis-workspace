# P_ADM_PROFIT_CAT_SUBS_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Calculates and categorizes subscriber profitability for a given period. It does this by first establishing period details, then aggregating subscription, fee, and usage data into several intermediate tables. Finally, it computes adjusted net revenue, assigns profitability categories to each subscription, and loads this categorized data into a partitioned historical table, using a temporary staging table for the final load.

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
- → [[ADM_PROFIT_CAT_PERIOD]]
- → [[ADM_PROFIT_CAT_SUBS]]
- → [[ADM_PROFIT_CAT_FEE]]
- → [[ADM_PROFIT_CAT_USE]]
- → [[ADM_PROFIT_CAT_USE_ROAMING]]
- → [[ADM_PROFIT_CAT_REVENUE]]
- → [[TMP_PROFIT_CAT_SUBS_HIST]]
- → [[ADM_PROFIT_CAT_SUBS_HIST]]

