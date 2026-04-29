# V_MOBILE_FARGO

**Schema:** `CCM` | **Type:** `View`

## Description
This view, V_MOBILE_FARGO, calculates Key Performance Indicators (KPIs) related to mobile service orders, specifically tracking new sales (KPI_NYSALG), product changes (KPI_PRODUCT_CHANGE), and ownership changes (KPI_OWNERCHANGE). It integrates detailed order, product, subscription, and dealer information from various operational and dimensional tables to provide a consolidated dataset for analysis and reporting on specific mobile service actions and their associated attributes.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| ORDER_ACTION_TYPE_ID |
| ORDER_ID |
| ORDER_STATUS_ID |
| PARENT_ORDER_ID |
| ORDER_ARRIVAL_DATE |
| ORDER_PROCESSED_DATE |
| DEALER_ID |
| CUST_TYPE_ID |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_LINE_ID |
| SUBSCR_ID |
| PRODUCT_ID |
| PRODUCT_ACTION_TYPE_ID |
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| PRODUCT_ORDER_LINE_ID |
| PRODUCT_OFFER_ID |
| SUBSCRIBED_OFFER_ID |
| ACTION_TYPE_ID |
| STATUS_ID |
| PRODUCT_OFFER_CATEGORY_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| PRODUCT_NAME |
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
| Column Name |
|---|
| SRC_SUBSCRIPTION_ID_1 |
| CUSTOMER_ROLE_ID |
| SUBSCRIPTION_ID |
| CUSTOMER_ID |
- ← [[CLM_CCM.V_CCM_DEALER_DIM]]
| Column Name |
|---|
| SOURCE_DEALER_ID |
| DEALER_NAME |
| DRM_SALES_CHANNEL_GEN02_DESC |
| DRM_SALES_CHANNEL_GEN03_DESC |
| DRM_SALES_CHANNEL_GEN04_DESC |
| DRM_SALES_CHANNEL_GEN05_DESC |

