# V_ADM_MONTH_SUBS_CUST_HH

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a monthly historical snapshot of subscription details, customer (owner and user) information, and associated household IDs. It joins various monthly dimension, subscription history, and customer information tables to create a comprehensive view for analytical purposes, deriving numerous keys for monthly and next-month aggregations, while excluding specific test customer data.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PERIOD_MONTH_KEY_CHAR |
| LAST_DATE |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| CUSTOMER_SK_OWNER |
| CUSTOMER_SK_USER |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
| Column Name |
|---|
| CUSTOMER_SK |
| PERIOD_MONTH_KEY |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |

