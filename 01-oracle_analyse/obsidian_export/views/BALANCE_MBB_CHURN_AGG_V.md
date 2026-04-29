# BALANCE_MBB_CHURN_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates mobile broadband (MBB) subscription historical data. It categorizes subscriptions by market type, product details (product name, product ID, source system key), and binding status. The view handles data from different time periods, potentially indicating a data migration (before/after 201510), and calculates the count of subscriptions ('ANTALL') for each unique combination of these categories, aiding in churn analysis or balance reporting.

## Data Sources (Inputs)
- ← [[ADM_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBS_TYPE |
| PRODUCT_NAME |
| PRODUCT_ID |
| SOURCE_SYSTEM_KEY |
| BINDING_ACTIVE |
| BINDING_TYPE |
| BINDING_NO_DAYS_ACTIVE |
| SUBSCRIPTION_ID |
- ← [[ADM_MBB_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PRODUCT_OFFER_NAME |
| PRODUCT_OFFER_ID |
| SOURCE_PRODUCT_ID_1 |
| SUBSCRIPTION_ID |
| PERIOD_MONTH_KEY |

