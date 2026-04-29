# FTV_STOCK_CAT_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a comprehensive, categorized view of product stock and associated changes. It enriches base stock data from 'FTV_STOCK_BASE_V2' with detailed product attributes (such as dwelling unit type, subscription type, technology, speed, product names, and reporting categories) from multiple joins to 'FTV_PRODUCT_BB_V_TMP'. The view also incorporates temporal dimensions from 'GALAXY.DATE_DIM_MV'. It tracks current, opening balance (OB), and closing balance (CB) states for various product types (BB - broadband, TV - television, and Primary BB) and calculates various flags related to churn, growth ('tilvekst'), product combination changes, and technology shifts (e.g., Coax to Fiber).

## Data Sources (Inputs)
- ← [[CCM.FTV_STOCK_BASE_V2]]
| Column Name |
|---|
| RUN_DT_KEY |
| TV_TYPE |
| P1_BB_PRODUCT_KEY |
| P2_BB_PRODUCT_KEY |
| P3_BB_PRODUCT_KEY |
| P4_BB_PRODUCT_KEY |
| P1_TV_PRODUCT_KEY |
| P2_TV_PRODUCT_KEY |
| P3_TV_PRODUCT_KEY |
| P4_TV_PRODUCT_KEY |
| P1_BB_PRIM_PRODUCT_KEY |
| P2_BB_PRIM_PRODUCT_KEY |
| P3_BB_PRIM_PRODUCT_KEY |
| P4_BB_PRIM_PRODUCT_KEY |
| OB_BB_PRODUCT_KEY |
| CB_BB_PRODUCT_KEY |
| OB_TV_PRODUCT_KEY |
| CB_TV_PRODUCT_KEY |
| OB_BB_PRIM_PRODUCT_KEY |
| CB_BB_PRIM_PRODUCT_KEY |
| BB_PRODUCT_KEY |
| TV_PRODUCT_KEY |
| BB_PRIM_PRODUCT_KEY |
| OB_BB_FLG |
| CB_BB_FLG |
| OB_TV_FLG |
| CB_TV_FLG |
| BB_CHANGE |
| TV_CHANGE |
| CHANGE_CATEGORY |
| TILKNYTNING_CATEGORY |
| OB_PRODUCT_COMBINATION |
| CB_PRODUCT_COMBINATION |
| OB_CB_PRODUCT_COMBINATION |
| PRODUCT_COMBINATION_CHANGE_FLG |
| CHURN_VULA_FLG |
| TILVEKST_UTBYGGING_FLG |
| TILVEKST_OFFNET_FLG |
| CHURN_FLYTTING_FLG |
| CHURN_RETURN_FLG |
| TILVEKST_FLYTTING_FLG |
| TILVEKST_RETURN_FLG |
| CHURN_COAX_TO_FIBER_FLG |
| CHURN_TBB_TO_FIBER_FLG |
| CHURN_KORTVARIG_FLG |
| TILVEKST_COAX_TO_FIBER_FLG |
| TILVEKST_TBB_TO_FIBER_FLG |
| TILVEKST_KORTVARIG_FLG |
| CHANGE_TYPE_SUBS |
| SUBS_OB |
| SUBS_CB |
| SUBS |
| PERIOD_MONTH_KEY |
- ← [[CCM.FTV_PRODUCT_BB_V_TMP]]
| Column Name |
|---|
| PRODUCT_KEY |
| DWELLING_UNIT_TYPE |
| SUBSCRIPTION_TYPE |
| TECHNOLOGY |
| PRODUCT_NAME_USE |
| SOURCE_PRODUCT_ID_1 |
| DRM_COMMON_REPORTING |
| PRODUCT_SPEED |
| VALUECHAIN |
| SOURCE_SYSTEM_NAME |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| DATE_KEY |
| DAY |
| MONTH_NUMBER |
| YEAR |
| RELATIVE_MONTH |

