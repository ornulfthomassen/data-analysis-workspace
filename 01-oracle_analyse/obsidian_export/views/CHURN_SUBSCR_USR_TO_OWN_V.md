# CHURN_SUBSCR_USR_TO_OWN_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Identifies and tracks events where a user becomes the owner of an MPP product subscription, providing a flag for the event, the date it occurred, and the number of months since the owner change. The view filters data for the last 25 months.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_ADM_SUBSCRIPTION]]
| Column Name |
|---|
| PERIOD_MONTH |
| SUBSCRIPTION_SK |
| CUSTOMER_SK_OWNER |
| CUSTOMER_SK_USER |
| MAIN_NUMBER_SK |
| PERIOD_MONTH_DATE |
| PRODUCT_GROUP |

