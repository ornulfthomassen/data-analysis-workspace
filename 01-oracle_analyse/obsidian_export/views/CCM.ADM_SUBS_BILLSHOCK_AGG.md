# ADM_SUBS_BILLSHOCK_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates subscription-level bill shock, domestic mobile data usage (in MB), and twin SIM presence metrics for various historical periods relative to a given month (current, previous, two months prior, and cumulative for the last 6 and 12 months). It calculates indicators for 'bill shock' (e.g., NOK > 398), total domestic MB, and the count of twin SIMs for each subscription and reporting month.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PREV1_PERIOD_MONTH_KEY |
| PREV2_PERIOD_MONTH_KEY |
| PREV5_PERIOD_MONTH_KEY |
| RELATIVE_MONTH |

- ← [[CLM_ADM.ADM_BILL_SHOCK]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| NOK |
| ANTALL_TWIN |


