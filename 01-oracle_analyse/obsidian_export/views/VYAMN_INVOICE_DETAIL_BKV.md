# VYAMN_INVOICE_DETAIL_BKV

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a comprehensive, denormalized view of invoice line item details by combining core invoice data from `CCDW_INVOICE.INVOICE_DETAIL` with descriptive attributes from various dimension tables (`GALAXY.DATE_DIM_MV`, `GALAXY.PRODUCT_DIM`, `GALAXY.PAYMENT_METHOD_DIM`, `GALAXY.INVOICE_LINE_TYPE_DIM_V`), performing data type conversions, handling potential NULLs for key identifiers, and deriving specific columns like `MULTI_NODE_COL`.

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

