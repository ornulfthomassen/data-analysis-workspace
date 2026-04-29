# BALANCE_MOBILE_SEGMENT_W_AG2_V

**Schema:** `CCM` | **Type:** `View`

## Description
Processes aggregated mobile segment balance data, calculating a refined 'BALANCE' by subtracting 'OUT_PORT' values. It enriches various attributes with default values if null, derives period keys (week, month, year), and categorizes segments using custom functions like `FORMAT_CLM_LIVSFASE` and `FORMAT_MAP2_6C`. The view filters the data to include records from 'PERIOD_WEEK_KEY' 201729 onwards and excludes specific product descriptions ('BEDRIFT', 'DEMO', 'TVILLING', 'SMS AKSESS', 'FASTNETT', 'HJEMME', 'SPONS', 'PRIVAT').

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

