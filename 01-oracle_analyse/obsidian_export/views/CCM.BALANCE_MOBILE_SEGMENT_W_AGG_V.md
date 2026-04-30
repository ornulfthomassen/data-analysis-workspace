# BALANCE_MOBILE_SEGMENT_W_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
Combines and transforms mobile balance and segmentation data from `BALANCE_MOBILE_SEGMENT_W_AGG` and `BALANCE_TALKMORE_WEEK_AGG` with product dimension data, applying various filtering, standardization, and calculation rules to create a unified view for CRM analysis of mobile services.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.BALANCE_MOBILE_SEGMENT_W_AGG]]
| Column Name |
|---|
| BALANCE |
| OUT_PORT |
| REFRESH_DATE |
| PERIOD_WEEK_KEY |
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
| CLM_LIVSFASE_SEGMENT_ID |
| MAP2_SEGMENT_ID |

- ← [[CLM_ADM.BALANCE_TALKMORE_WEEK_AGG]]
| Column Name |
|---|
| BALANCE |
| REFRESH_DATE |
| PERIOD_WEEK_KEY |
| YEAR_MONTH |
| PRIM_PRODUCT_DESC |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_BRAND |

- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_DESC |


