# VYA_COMMISSION_DETAIL

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive, aggregated detail of commission data, linking commission records with order line details, product information, and subscription master data. It calculates various commission amounts, tracks payment and voucher dates, and associates commissions with specific orders, products, and dealer entities.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| ORDER_KEY |
| SOURCE_ORDER_ID |
| ORDER_SUBSCR_KEY |
| IMEI |
| HANDSET_KEY |
| DEALER_KEY |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| DEALER_KEY |
| SOURCE_DEALER_ID |
- ← [[CCDW_COMMISSIONS.COMMISSION_DETAIL]]
| Column Name |
|---|
| ORDER_ID |
| COMMISSION_PRODUCT_ID |
| COMMISSION_ORDER_CATEGORY_ID |
| EMPLOYEE_DEALER_ID |
| COMMISSION_STATUS_ID |
| SUBSCRIPTION_ID |
| TAC_ID |
| UNIT_PRICE |
| GROSS_COMMISSION_AMOUNT |
| NET_COMMISSION_AMOUNT |
| GROSS_REVENUE |
| ORDERING_DATE |
| VOUCHER_ID |
| PAYMENT_DATE |
| COMMISSION_DEALER_ID |
| COMMISSION_RECEIVER_ID |
| MARKET_AREA_ID |
| SOURCE_SYSTEM_ID |
- ← [[CCDW_COMMISSIONS.COMMISSION_PRODUCT]]
| Column Name |
|---|
| COMMISSION_PRODUCT_ID |
| COMMISSION_PRODUCT_NAME |
| PRODUCT_GROUP_ID |
| PRODUCT_GROUP_DESC |
| SOURCE_PRODUCT_ID |
| SOURCE_SYSTEM_ID |
- ← [[CCDW_COMMISSIONS.COMMISSION_CATEGORY]]
| Column Name |
|---|
| COMMISSION_CATEGORY_ID |
| COMMISSION_CATEGORY_NAME |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |

