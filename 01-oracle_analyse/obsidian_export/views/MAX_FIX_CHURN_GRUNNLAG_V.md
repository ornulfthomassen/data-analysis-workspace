# MAX_FIX_CHURN_GRUNNLAG_V

**Schema:** `CCM` | **Type:** `View`

## Description
Determines the earliest (minimum) of the latest (maximum) 'PERIOD_MONTH_KEY' values across four different historical data tables: ADM_SUBSCRIPTION_HISTORY, ADM_SUBSCR_DETAIL_HIST, ADM_SUBSCR_USAGE_AGG, and ADM_HOUSEHOLD_INFO_KURT_HIST. This resulting value is labeled as 'MAX_PERIODE' and likely represents a common 'watermark' or reference period for churn analysis or data synchronization.

## Data Sources (Inputs)
- ← [[ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[ADM_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[ADM_SUBSCR_USAGE_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[ADM_HOUSEHOLD_INFO_KURT_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |

