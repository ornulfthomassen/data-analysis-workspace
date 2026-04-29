# BALANCE_MOBILE_SEGMENT_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and unifies mobile segment balance data from `CRM_ANALYSE.BALANCE_MOBILE_SEGMENT_AGG` and `CLM_ADM.BALANCE_TALKMORE_AGG` sources. It includes transformations, data cleaning (e.g., handling NULLs, excluding certain product descriptions), and filtering to focus on consumer/private mobile segments from December 2014 onwards, providing monthly and yearly period keys, product details, and various segment classifications.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.BALANCE_MOBILE_SEGMENT_AGG]]
| Column Name |
|---|
| BALANCE |
| OUT_PORT |
| REFRESH_DATE |
| PERIOD_MONTH_KEY |
| YEAR_MONTH |
| PRIM_PRODUCT_DESC |
| PRODUCT_KEY |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_BRAND |
| BINDINGSSTATUS |
| PROFIT_CAT_NAME2 |
| PROFIT_CAT_NAME4 |
| PROFIT_CAT_NAME7 |
| PROFIT_CAT |
| PROFIT_PERIOD |
| VAR_SEGMENT_NAME |
| CHURN_SEGMENT_NAME |
| CHURN_SEGMENT_GROUP |
| CLM_LIVSFASE_SEGMENT_NAME |
| MAP2_SEGMENT_NAME |
- ← [[ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PREV1_PERIOD_MONTH_KEY |
| PREV2_PERIOD_MONTH_KEY |
| PREV3_PERIOD_MONTH_KEY |
- ← [[CLM_ADM.BALANCE_TALKMORE_AGG]]
| Column Name |
|---|
| BALANCE |
| REFRESH_DATE |
| YEAR_MONTH |
| PERIOD_MONTH_KEY |
| PRIM_PRODUCT_DESC |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_BRAND |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |

