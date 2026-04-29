# GCP_TMP_SUBSCRIPTION_GROSS_FEE_GROSS_USE

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates rounded gross fee and gross usage for subscriptions by joining aggregated and historical subscription data.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| GROSS_FEE |
| GROSS_USE |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |

