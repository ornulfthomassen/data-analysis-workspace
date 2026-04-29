# P_ADM_MBB_SUBSCR_DETAIL_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Populates a monthly partition of the ADM_MBB_SUBSCR_DETAIL_HIST table with aggregated mobile broadband subscription and product details. It calculates metrics such as days a product is active and the number of product changes within a month or across subscriptions. The process includes source data validation, creation of a temporary table with the calculated data, and then an atomic exchange of this temporary table with the target partition for a specified month (P_YYYYMM).

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| PRODUCT_NAME |
| SUBS_TYPE |
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| START_DATE |
| SUBSCRIPTION_ID |
| BINDING_END_DATE |
| PRODUCT_OFFER_ID |
| END_DATE |
| INFO_CHG_DATE |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_DESC |
| SOURCE_PRODUCT_ID_1 |
| DRM_PRODUCT_GROUP |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_SERVICE |
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| LAST_DATE |
| FIRST_DATE |

## Target Tables (Outputs)
- → [[ADM_MBB_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| BINDING_END_DATE |
| PRODUCT_OFFER_ID |
| PRODUCT_OFFER_NAME |
| PRODUCT_OFFER_DESC |
| SOURCE_PRODUCT_ID_1 |
| DRM_PRODUCT_GROUP |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_SERVICE |
| PROD_NO_DAYS_ACTIVE |
| ANT_PROD_CHANGE_MONTH |
| ANT_PROD_CHANGE_SUBSCR |
- → [[TMP_MBB_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| BINDING_END_DATE |
| PRODUCT_OFFER_ID |
| PRODUCT_OFFER_NAME |
| PRODUCT_OFFER_DESC |
| SOURCE_PRODUCT_ID_1 |
| DRM_PRODUCT_GROUP |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_SERVICE |
| PROD_NO_DAYS_ACTIVE |
| ANT_PROD_CHANGE_MONTH |
| ANT_PROD_CHANGE_SUBSCR |

