# CM_CCDW_BALANCE_CHECK_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view performs a reconciliation or 'balance check' between active subscription data in the CCDW (Data Warehouse) and CM (Customer Management) systems. It identifies discrepancies in subscription status, categorizing them as 'ACTIVE IN CCDW, INACTIVE IN CM' (meaning the subscription is active in the data warehouse but considered inactive in the customer management system) or 'UNKNOWN/INACTIVE IN CCDW, ACTIVE IN CM' (meaning the subscription is active in the customer management system but either unknown or inactive in the data warehouse). The view consolidates key subscription, product, and customer-related information to highlight these inconsistencies.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MARKET_AREA_ID |
| MAIN_NUMBER |
| START_DATE |
| END_DATE |
| INFO_CHG_DATE |
| PRODUCT_OFFER_ID |
| BUSINESS_AREA_ID |
| SOURCE_SYSTEM_ID |
| PRODUCT_CATEGORY_ID |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| SUBSCR_VALID_TO_DATE |
| INFO_CHG_DATE |
| INFO_IS_DELETED |
| DIRECTORY_NUMBER_ID |
| SUBSCR_VALID_FROM_DATE |
| INFO_REG_DATE |
| S212_REF_ID_RESP |
| S212_PRODUCT_ID |
| CUST_ID_RESP |
| CUST_ID_USER |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| SOURCE_PRODUCT_ID_1 |
| PRODUCT_NAME |
| PRODUCT_BRAND |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_REPORTING |
- ← [[CM.CUSTOMER]]
| Column Name |
|---|
| CUST_ID |
| UNIT_TYPE_ID |
| CUST_FIRST_NAME |

