# TST_FTV_STOCK_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and transforms product stock and key performance indicator (KPI) data, including opening and closing balances, net changes, churn, and growth (tilvekst) metrics for broadband and TV products. It categorizes products by dwelling unit type, technology, speed, and derives product combination types (e.g., Dualplay, BB Only, TV Only) to provide a time-series view of product performance and transitions. The view also filters out specific TV-only product scenarios.

## Data Sources (Inputs)
- ← [[CCM.TST_FTV_STOCK_BASE]]
| Column Name |
|---|
| RUN_DT_KEY |
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
| PERIOD_MONTH_KEY |
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
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| DATE_KEY |
| DAY |
| MONTH_NUMBER |
| YEAR |
| RELATIVE_MONTH |

