# ODS_S

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view combines subscription details from an operational data store (`ODS.SUBSCRIPTION_ODS_MOB`) with comprehensive product information from a CRM analytics product dimension view (`CRM_ANALYSE.PRODUCT_DIM_V`). It creates a unified dataset for subscriptions, including product attributes, customer and account identifiers, subscription status and dates, and a derived customer role, primarily for analytical or reporting purposes.

## Data Sources (Inputs)
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SRC_SUBSCRIPTION_ID_1 |
| SRC_SUBSCRIPTION_STATUS |
| MAIN_NUMBER |
| CUSTOMER_ID |
| CUSTOMER_ROLE_ID |
| MARKET_AREA_ID |
| PRODUCT_CATEGORY_ID |
| SUBSCR_START_DATE |
| SUBSCR_END_DATE |
| INFO_CHG_DATE |
| PRODUCT_OFFER_ID |
| ACCOUNT_ID |
| SRC_ACCOUNT_ID |
| SRC_CUSTOMER_ID |
- ← [[CRM_ANALYSE.PRODUCT_DIM_V]]
| Column Name |
|---|
| PRODUCT_NAME |
| PRODUCT_GROUP |
| PRODUCT_KEY |
| PRODUCT_POID |
| PRODUCT_DESC |
| PRODUCT_CLASS |
| PRODUCT_NEED |
| PRODUCT_PAYTYPE |
| PRODUCT_START_DATE |
| PRODUCT_END_DATE |
| PRODUCT_AREA |
| PRODUCT_TECHNOLOGY |
| PRODUCT_CATEGORY |
| PRODUCT_MARKET_NAME |
| PRODUCT_BRAND |
| PRODUCT_REPORTING |
| PRODUCT_PORTFOLIO |
| PRODUCT_SERVICE |
| PRODUCT_PAYMENT |
| PRODUCT_CATEGORY_NAME |
| PRODUCT_PORTFOLIO_NAME |
| PRODUCT_FAMILY_NAME |
| PRODUCT_ACCESS_TYPE_NAME |
| PRODUCT_PAYMENT_TYPE_NAME |
| PRODUCT_BINDING_TYPE_NAME |
| PRODUCT_STARTUP_FEE |
| PRODUCT_MONTHLY_FEE |
| PRODUCT_INCLUDED_MB |

