# GCP_HARDWARE_ORDER_EVENTS

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates detailed hardware order event information, including customer, product, service, and agreement details, from various operational systems for analytical consumption (e.g., in Viya or Google Cloud Platform). It enriches hardware order data with GTIN properties, sales information, and related service/agreement order specifics.

## Data Sources (Inputs)
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER]]
| Column Name |
|---|
| HARDWARE_ORDER_ID |
| DEALER_ID |
| ORDER_TYPE |
| STATUS_ID |
| CUSTOMER_ID |
| SALES_REP_NAME |
| INFO_REG_DATE |
| INFO_CHG_DATE |
- ← [[CM.CUSTOMER]]
| Column Name |
|---|
| CUST_ID |
- ← [[FPS.TERMINAL_GTIN_PROPERTIES]]
| Column Name |
|---|
| GTIN |
| MANUFACTURER |
| MODEL_NAME |
| COLOR_NAME |
| TOTAL_SIZE |
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER_PRODUCT_PARAM]]
| Column Name |
|---|
| HARDWARE_ORDER_ID |
| PRODUCT_LINE_ID |
| PARAMETER_ID |
| PARAMETER_VALUE |
- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_ACTION_TYPE_ID |
| ORDER_STATUS_ID |
| ORDER_PROCESSED_DATE |
| ORDER_ARRIVAL_DATE |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_LINE_ID |
| PRODUCT_ACTION_TYPE_ID |
| SUBSCR_ID |
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| PRODUCT_OFFER_CATEGORY_ID |
| ACTION_TYPE_ID |
| PRODUCT_OFFER_ID |
| STATUS_ID |
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]
| Column Name |
|---|
| SOURCE_PRODUCT_ID_1 |
| MONTHLY_FEE |
| PRODUCT_NAME |
| START_DATE |
| END_DATE |
- ← [[ONL_REP.AGREEMENT_ORDER]]
| Column Name |
|---|
| AGREEMENT_ORDER_ID |
- ← [[ONL_REP.AGREEMENT_ORDER_OFFER]]
| Column Name |
|---|
| AGREEMENT_ORDER_ID |
| AGREEMENT_OFFER_ID |
| PRODUCT_OFFER_ID |
- ← [[CM.AGREEMENT_OFFER]]
| Column Name |
|---|
| AGREEMENT_OFFER_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
| PRODUCT_NAME_USE |
| MONTHLY_PRICE |
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
| Column Name |
|---|
| SOURCE_SYSTEM_STATUS_CODE |
| BUSINESS_AREA_NAME |
| ORDER_STATUS_NAME |

