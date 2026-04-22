# MAX_FIX_CHURN_GRUNNLAG_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies the minimum of the maximum available `PERIOD_MONTH_KEY` values across four different historical and aggregated subscription-related tables. It effectively finds the earliest 'latest' period present in all the contributing data sources, ensuring that any analysis based on this view does not exceed the common data availability across these tables.

## Data Sources (Inputs)
- ← [[ADM_SUBSCRIPTION_HISTORY]]
- ← [[ADM_SUBSCR_DETAIL_HIST]]
- ← [[ADM_SUBSCR_USAGE_AGG]]
- ← [[ADM_HOUSEHOLD_INFO_KURT_HIST]]

