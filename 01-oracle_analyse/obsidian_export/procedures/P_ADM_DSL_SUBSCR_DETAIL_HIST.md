# P_ADM_DSL_SUBSCR_DETAIL_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure populates or refreshes monthly partitions of the ADM_DSL_SUBSCR_DETAIL_HIST table. It first validates the existence and data availability in several source tables for the given month (P_YYYYMM). If data is valid, it dynamically creates a temporary table, populates it with DSL subscription detail history aggregated from various data sources, and then exchanges this temporary table with a corresponding partition in the permanent ADM_DSL_SUBSCR_DETAIL_HIST table. It includes logic for creating new partitions if they don't exist and preventing overwrites of existing data unless explicitly allowed.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| DAY |
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
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBS_TYPE |
| SUBSCRIPTION_ID |
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| START_DATE |
| SUBSCRIPTION_ID |
| END_DATE |
| PRODUCT_OFFER_ID |
| INFO_CHG_DATE |
| SUBSCRIPTION_SEQ |
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| LAST_DATE |
- ← [[CCDW.PRODUCT_OFFER]]
| Column Name |
|---|
| PRODUCT_OFFER_NAME |
| PRODUCT_OFFER_DESC |
| PRODUCT_OFFER_ID |

## Target Tables (Outputs)
- → [[TMP_DSL_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
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
- → [[ADM_DSL_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
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

