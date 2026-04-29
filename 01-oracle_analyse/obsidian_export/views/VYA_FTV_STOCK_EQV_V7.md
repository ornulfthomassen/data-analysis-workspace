# VYA_FTV_STOCK_EQV_V7

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates comprehensive Key Performance Indicators (KPIs) related to subscriber base movements for various product types (broadband and TV) across different dwelling unit types (MDU, SDU) and technologies. It aggregates stock data with product characteristics and date dimensions to derive metrics such as opening/closing balances, net change, growth (Tilvekst), churn, speed/technology/product changes, and dual-play transitions, providing a detailed analytical view for product and subscriber tracking over time.

## Data Sources (Inputs)
- ← [[CLM_ADM.FTV_STOCK_EQV_V3]]
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
| NUM_SUBS |
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
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| DATE_KEY |
| DAY |
| MONTH_NUMBER |
| YEAR |
| RELATIVE_MONTH |

