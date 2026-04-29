# VYA_STOCK_MOBILE_MONTH_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates monthly mobile subscription stock (balance) data over a 24-month rolling period. It combines historical monthly closing balances (UB_MONTH), historical monthly opening balances (IB_MONTH), and current daily closing balances, enriching the data with dimension attributes like profit categories, customer lifecycle segments, and age groups. The view calculates total discounts, balances, and net changes for mobile subscriptions.

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
| PROFIT_CAT_TALE |
| CLM_LIVSFASE_SEGMENT_ID_O |
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
| PERIOD_MONTH_KEY |
| DAY |
| PRODUCT_KEY |
| PROFIT_CAT_TALE |
| CLM_LIVSFASE_SEGMENT_ID_O |
| OWNER_AGE |
| USER_AGE |
| FAMILY_BONUS_FLG |
| DISCOUNT_PRODUCT_KEY |
| DISCOUNT |
| BALANCE |

