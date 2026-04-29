# VIYA_TM_SALES

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates and presents sales-related Key Performance Indicators (KPIs) such as new sales, product changes, and owner changes. It combines data from service orders, service order products, subscribed offers, and product dimensions, filtered for specific dealers and order arrival dates to provide a consolidated sales overview.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| ORDER_ACTION_TYPE_ID |
| ORDER_ID |
| ORDER_STATUS_ID |
| SALES_REP_NAME |
| ORDER_ARRIVAL_DATE |
| CUST_TYPE_ID |
| DEALER_ID |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| PRODUCT_ACTION_TYPE_ID |
| ORDER_ID |
| ORDER_LINE_ID |
| DEALER_ID |
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| PRODUCT_OFFER_CATEGORY_ID |
| ACTION_TYPE_ID |
| PRODUCT_OFFER_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_FAMILY_NAME |
| PRODUCT_NAME |
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |

