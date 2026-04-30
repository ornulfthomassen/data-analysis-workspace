# MAX_DSL_CHURN_GRUNNLAG_V

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates the earliest of the latest available period month keys across three historical data tables: ADM_SUBSCRIPTION_HISTORY, ADM_SUBSCR_DETAIL_HIST, and ADM_HOUSEHOLD_INFO_KURT_HIST. This effectively finds the minimum of the maximum PERIOD_MONTH_KEY from each source, likely to establish a common baseline period for churn analysis.

## Data Sources (Inputs)
- ← [[CCM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |

- ← [[CCM.ADM_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |

- ← [[CCM.ADM_HOUSEHOLD_INFO_KURT_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |


