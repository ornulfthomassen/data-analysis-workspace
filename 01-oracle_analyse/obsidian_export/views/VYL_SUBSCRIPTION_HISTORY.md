# VYL_SUBSCRIPTION_HISTORY

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a monthly snapshot of subscription history details, including subscription identifiers, customer details, market and business area IDs, product information (offer ID, brand, name, key, attributes), and various active/binding period durations. It filters the data to a specific historical month, which is calculated based on the previous month minus five days.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |
| CUSTOMER_SK_OWNER |
| CUSTOMER_SK_USER |
| MARKET_AREA_ID |
| BUSINESS_AREA_ID |
| PRODUCT_OFFER_ID |
| PRODUCT_BRAND |
| PRODUCT_NAME |
| LAST_PRODUCT_OFFER_ID |
| SUBS_NO_DAYS_ACTIVE |
| PROD_NO_DAYS_ACTIVE |
| NO_DAYS_LAST_START |
| NO_DAYS_LAST_CHANGE |
| NO_DAYS_BIND_START |
| NO_DAYS_BIND_END |
| PRODUCT_ATTRIBUTE_KEY |

