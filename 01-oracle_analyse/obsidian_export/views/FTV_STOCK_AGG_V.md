# FTV_STOCK_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive, aggregated view of product stock and movement metrics ('Stock' KPI_FLAG) over time. It calculates various KPIs such as opening and closing balances, net changes, churn, growth ('tilvekst'), and product changes (e.g., speed, technology, subscription type). Data is enriched with product dimension attributes and grouped by year-month and dwelling unit type, ensuring all time periods and DU types are represented.

## Data Sources (Inputs)
- ← [[DUAL]]
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
- ← [[CCM.FTV_PRODUCT_BB_V_TMP]]
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

