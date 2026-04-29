# VYAMN_INVOICE_DETAIL_GENEVA

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and enriches invoice line item details from the core `INVOICE_DETAIL` fact table by joining it with various dimension tables (Product, Payment Method, Invoice Line Type, and multiple instances of Date Dimension). It performs data type conversions, handles null values by replacing them with -1, and calculates a `MULTI_NODE_COL` for distributed processing, likely preparing the data for analytical consumption in a data warehouse or analytical platform like SAS Viya, as suggested by the comments ('LOADING Order-DATA TO MJØSA').

## Data Sources (Inputs)
- ← [[CCDW_INVOICE.INVOICE_DETAIL]]
| Column Name |
|---|
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
| INVOICE_DATE |
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

