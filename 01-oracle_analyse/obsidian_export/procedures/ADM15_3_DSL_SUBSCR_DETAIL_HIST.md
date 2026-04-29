# ADM15_3_DSL_SUBSCR_DETAIL_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Populates and maintains a partitioned historical detail table (`CRM_ANALYSE.ADM_DSL_SUBSCR_DETAIL_HIST`) for DSL subscriptions. The procedure iterates through a specified or default year-month range. For each month, it dynamically checks for and creates the target table and its monthly partitions if they don't exist. It then inserts or updates detailed DSL subscription product information, including binding contract details, by joining various data sources such as subscription products, product dimensions, and existing historical data. The process includes data validation checks and logs operational status and errors.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| DRM_COMMON_SERVICE |
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_DESC |
| SOURCE_PRODUCT_ID_1 |
| DRM_PRODUCT_GROUP |
| DRM_COMMON_PRODUCT_CATEGORY |
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[CRM_ANALYSE.ADM_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| SUBS_TYPE |
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |
| PRODUCT_OFFER_ID |
| INFO_CHG_DATE |
| SUBSCRIPTION_SEQ |
- ← [[CCDW.PRODUCT_OFFER]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| PRODUCT_OFFER_NAME |
| PRODUCT_OFFER_DESC |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_DSL_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| START_DATE |
| END_DATE |
| BINDING_END_DATE |
| PRODUCT_OFFER_ID |
| PRODUCT_OFFER_NAME |
| PRODUCT_OFFER_DESC |
| SOURCE_PRODUCT_ID_1 |
| DRM_PRODUCT_GROUP |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_SERVICE |
| NO_DAYS_ACTIVE |

