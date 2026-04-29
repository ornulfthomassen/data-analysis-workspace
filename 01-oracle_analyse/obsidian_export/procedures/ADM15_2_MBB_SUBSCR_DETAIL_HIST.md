# ADM15_2_MBB_SUBSCR_DETAIL_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure manages the historical detail table for Mobile Broadband (MBB) subscriptions, named ADM_MBB_SUBSCR_DETAIL_HIST. It checks for the table's existence, creating it with necessary partitions and indexes if it's new. It then iterates through specified or determined months (YYYYMM), verifies data completeness from multiple source systems, and if a month's data is not present, it adds a new partition to the target table and inserts aggregated/transformed subscription product details for that month. The inserted data includes subscription IDs, main numbers, product offers, product attributes, and calculated metrics like active days and product changes.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[DUAL]]
| Column Name |
|---|
| SYSDATE |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_PRODUCT_GROUP |
| PRIMARY_PRODUCT_FLAG |
| PRODUCT_NAME |
| PRODUCT_DESC |
| SOURCE_PRODUCT_ID_1 |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_SERVICE |
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| PARENT |
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
| START_DATE |
| SUBSCRIPTION_ID |
| BINDING_END_DATE |
| PRODUCT_OFFER_ID |
| END_DATE |
| INFO_CHG_DATE |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_MBB_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
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

