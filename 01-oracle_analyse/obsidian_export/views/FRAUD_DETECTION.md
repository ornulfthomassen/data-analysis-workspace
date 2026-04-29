# FRAUD_DETECTION

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view is designed for fraud detection. It identifies customers and their associated orders within the last 60 days that exhibit suspicious purchasing patterns, such as multiple purchases or distinct main numbers, exceeding certain thresholds. It then consolidates detailed information about these potentially fraudulent orders and customer/subscriber data for further analysis or reporting.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| OWNER_CUSTOMER_KEY |
| RESOURCE_VALUE |
| ORDER_DT_KEY |
| ORDERLINE_PRODUCT_KEY |
| DEALER_KEY |
| HANDSET_KEY |
| KPI_GROSS_SALE |
| MARKET_AREA_KEY |
| USER_CUSTOMER_KEY |
| SOURCE_ORDER_ID |
| SALES_ORDER_INDICATOR_KEY |
| ORDER_LINE_TYPE_KEY |
| IMEI |
| ORDER_SUBSCR_KEY |
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
| Column Name |
|---|
| ORDER_LINE_PRODUCT_KEY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_PRODUCT_CATEGORY |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| DEALER_KEY |
| DEALER_CHAIN_NAME |
| DEALER_NAME |
- ← [[GALAXY.HANDSET_DIM_V]]
| Column Name |
|---|
| HANDSET_KEY |
| MARKETING_NAME |
- ← [[GALAXY.CUSTOMER_DIM]]
| Column Name |
|---|
| CUSTOMER_KEY |
| BIRTH_DATE_AGE |
- ← [[CLM_CCM.CCM_CUSTOMER_V]]
| Column Name |
|---|
| KURT_ID |
| DATE_OF_BIRTH |
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| OWNER_FIRST_NAME |
| OWNER_LAST_NAME |
| OWNER_MAIN_ADDRESS_MUNIC_NO |
| USER_FIRST_NAME |
| USER_LAST_NAME |

