# GCP_STOCK_MOBILE_WEEK_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates weekly and daily mobile stock data, including discount and balance information, enriched with profit categories, lifecycle segments, and age groups. This data is prepared for lifting through Denodo to GCP, focusing on relevant/fresh data (last two years of weekly data, and recent daily data).

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_WEEK_DIM_V]]
| Column Name |
|---|
| YEAR_WEEK_NUMBER |
| LAST_DATE |
| RELATIVE_WEEK |
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_WEEK_AGG]]
| Column Name |
|---|
| PERIOD_WEEK_KEY |
| PRODUCT_KEY |
| CLM_LIVSFASE_SEGMENT_ID_O |
| PROFIT_CAT_TALE |
| OWNER_AGE |
| USER_AGE |
| FAMILY_BONUS_FLG |
| DISCOUNT_PRODUCT_KEY |
| DISCOUNT |
| BALANCE |
- ← [[CRM_ANALYSE.ADM_CLM_LIVSFASE_DIM]]
| Column Name |
|---|
| CLM_LIVSFASE_KEY |
| CLM_LIVSFASE_NAME_6C |
- ← [[CRM_ANALYSE.ADM_PROFIT_CAT_DIM]]
| Column Name |
|---|
| PROFIT_CAT_KEY |
| PROFIT_CAT_NAME_2C |
| PROFIT_CAT_NAME_4C |
| PROFIT_CAT_NAME_7C |
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
| Column Name |
|---|
| AGE_GROUP_KEY |
| AGE_GROUP_NAME_10C |
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_DAY_AGG]]
| Column Name |
|---|
| PERIOD_WEEK_KEY |
| DAY |
| PRODUCT_KEY |
| CLM_LIVSFASE_SEGMENT_ID_O |
| PROFIT_CAT_TALE |
| OWNER_AGE |
| USER_AGE |
| FAMILY_BONUS_FLG |
| DISCOUNT_PRODUCT_KEY |
| DISCOUNT |
| BALANCE |

