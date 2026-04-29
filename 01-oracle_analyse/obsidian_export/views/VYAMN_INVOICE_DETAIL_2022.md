# VYAMN_INVOICE_DETAIL_2022

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a detailed view of invoice data specifically for the year 2022. It enriches raw invoice line item details with information from various dimension tables (dates, products, payment methods, invoice line types) and customer mapping, primarily for data loading purposes into a data warehouse or data lake.

## Data Sources (Inputs)
- ← [[CCDW_INVOICE.INVOICE_DETAIL]]
| Column Name |
|---|
| INVOICE_DATE |
| SOURCE_SYSTEM_ID |
| PRODUCT_OFFER_ID |
| TRAFFIC_TYPE_ID |
| SUBSCRIPTION_ID |
| PAYMENT_METHOD_ID |
| AGREEMENT_OFFER_ID |
| INVOICE_TYPE_ID |
| INVOICE_ID |
| INVOICE_LINE_ID |
| MARKET_AREA_ID |
| INVOICE_LINE_TYPE_ID |
| INVOICE_MEDIA_TYPE_ID |
| INVOICE_START_DATE |
| INVOICE_END_DATE |
| INVOICE_LINE_START_DATE |
| INVOICE_LINE_END_DATE |
| GROSS_AMOUNT |
| NET_AMOUNT |
| DURATION |
| DATAVOLUME |
| NUMBER_OF_INVOICE |
| NUMBER_OF_INVOICE_LINES |
| BILL_STYLE_ID |
| DISCOUNT_VALUE |
| NO_OF_INVOICE_ITEMS |
| AGREEMENT_ID |
| AGREEMENT_OFFER_PRODUCT_ID |
| ACCOUNT_ID_BILL |
| KURT_ID_BILL |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DATE_KEY |
| DAY |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| PRODUCT_NAME |
| PRODUCT_DESC |
| PRODUCT_FAMILY_NAME |
| DRM_COMMON_PRODUCT_AREA |
- ← [[GALAXY.PAYMENT_METHOD_DIM]]
| Column Name |
|---|
| PAYMENT_METHOD_KEY |
| PAYMENT_METHOD_DESC |
- ← [[GALAXY.INVOICE_LINE_TYPE_DIM_V]]
| Column Name |
|---|
| INVOICE_LINE_TYPE_KEY |
| INVOICE_LINE_TYPE_DESC |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_KEY |

