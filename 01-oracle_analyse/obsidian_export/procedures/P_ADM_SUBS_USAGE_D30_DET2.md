# P_ADM_SUBS_USAGE_D30_DET2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure aggregates mobile subscription usage data for a 30-day period. It processes raw usage facts, resolves subscription hierarchies (including parent and twin subscriptions), and calculates various aggregated metrics like usage amount, volume, and duration. The aggregated data is then loaded into a specific partition of a permanent administrative table, `ADM_SUBS_USAGE_MONTH_DET2`, using a temporary staging table, `TMP_SUBS_USAGE_D30_DET`, for intermediate calculations and partition exchange.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.SUBSCR_USAGE_MOBILE_DAY_FACT_V]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CM.REL_SUBSCRIPTION]]

## Target Tables (Outputs)
- → [[TMP_SUBS_USAGE_D30_DET]]
- → [[ADM_SUBS_USAGE_MONTH_DET2]]

