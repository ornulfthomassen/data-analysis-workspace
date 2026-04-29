# FTV_STOCK_AGG_DEV_V

**Schema:** `CCM` | **Type:** `View`

## Description
The view `FTV_STOCK_AGG_DEV_V` provides a comprehensive monthly aggregate of stock-related Key Performance Indicators (KPIs). It combines detailed stock base data with product and date dimensions. The view calculates various metrics including opening and closing balances for Broadband (BB) and TV services, net changes, churn, growth (tilvekst), and movements related to product speed, technology, subscription type, and dwelling unit (DU) type. It also tracks specific cross-over events like technology changes (e.g., Coax to Fiber). The data is generated for a range of years (2022 to the current year) and ensures all combinations of months and DU types are represented, even if no stock data is available for a given combination.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| DATE_KEY |
| DAY |
| MONTH_NUMBER |
| YEAR |
| RELATIVE_MONTH |
- ← [[CCM.FTV_STOCK_BASE]]
| Column Name |
|---|
| RUN_DT_KEY |
| PERIOD_MONTH_KEY |
| TV_TYPE |
| BB_PRODUCT_KEY |
| P1_BB_PRODUCT_KEY |
| P2_BB_PRODUCT_KEY |
| P3_BB_PRODUCT_KEY |
| P4_BB_PRODUCT_KEY |
| TV_PRODUCT_KEY |
| P1_TV_PRODUCT_KEY |
| P2_TV_PRODUCT_KEY |
| P3_TV_PRODUCT_KEY |
| P4_TV_PRODUCT_KEY |
| BB_PRIM_PRODUCT_KEY |
| P1_BB_PRIM_PRODUCT_KEY |
| P2_BB_PRIM_PRODUCT_KEY |
| NUM_CB_BB |
| NUM_CB_TV |
| NUM_OB_BB |
| NUM_OB_TV |
| CHURN_VULA |
| CHURN_FLYTTING |
| CHURN_RETURN |
| CHURN_KORTVARIG |
| TILVEKST_FLYTTING |
| TILVEKST_RETURN |
| CHURN_TBB_TO_FIBER |
| CHURN_COAX_TO_FIBER |
| TILVEKST_TBB_TO_FIBER |
| TILVEKST_COAX_TO_FIBER |
| TILVEKST_KORTVARIG |
| TILVEKST_UTBYGGING |
| TILVEKST_OFFNET |
- ← [[ccm.FTV_PRODUCT_BB_V_TMP]]
| Column Name |
|---|
| PRODUCT_KEY |
| DWELLING_UNIT_TYPE |
| SUBSCRIPTION_TYPE |
| PRODUCT_NAME_USE |
| SOURCE_PRODUCT_ID_1 |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_REPORTING |
| DRM_COMMON_PRODUCT_CATEGORY |
| TECHNOLOGY |
| PRODUCT_SPEED |
| VALUECHAIN |
| SOURCE_SYSTEM_NAME |

