# MAX_DSL_CHURN_GRUNNLAG_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view determines the earliest of the latest available historical periods (represented by PERIOD_MONTH_KEY) across three different administrative history tables: ADM_SUBSCRIPTION_HISTORY, ADM_SUBSCR_DETAIL_HIST, and ADM_HOUSEHOLD_INFO_KURT_HIST. The resulting 'MAX_PERIODE' serves as a common, consistent reference point for historical analysis, likely for churn calculations (as indicated by 'DSL_CHURN' in the view name), ensuring that all underlying data sources have data up to at least this period.

## Data Sources (Inputs)
- ← [[ADM_SUBSCRIPTION_HISTORY]]
- ← [[ADM_SUBSCR_DETAIL_HIST]]
- ← [[ADM_HOUSEHOLD_INFO_KURT_HIST]]

