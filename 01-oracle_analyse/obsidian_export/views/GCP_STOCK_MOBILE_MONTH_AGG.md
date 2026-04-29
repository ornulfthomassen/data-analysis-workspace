# GCP_STOCK_MOBILE_MONTH_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates mobile stock data on a monthly basis for transfer to Google Cloud Platform (GCP). It combines monthly opening balance (IB_MONTH), closing balance (UB_MONTH), and daily closing balance data for the current month. The view provides aggregated metrics like DISCOUNT, BALANCE, UB_MONTH, IB_MONTH, and NETTO, categorized by period, product, profit categories, customer lifecycle segments, owner/user age groups, and family bonus flags, filtered to include data from the last 24 months.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| LAST_DATE |
| RELATIVE_MONTH |
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_MONTH_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PRODUCT_KEY |
| FAMILY_BONUS_FLG |
| DISCOUNT_PRODUCT_KEY |
| DISCOUNT |
| BALANCE |
| CLM_LIVSFASE_SEGMENT_ID_O |
| PROFIT_CAT_TALE |
| OWNER_AGE |
| USER_AGE |
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
| PERIOD_MONTH_KEY |
| DAY |
| PRODUCT_KEY |
| FAMILY_BONUS_FLG |
| DISCOUNT_PRODUCT_KEY |
| DISCOUNT |
| BALANCE |
| CLM_LIVSFASE_SEGMENT_ID_O |
| PROFIT_CAT_TALE |
| OWNER_AGE |
| USER_AGE |

