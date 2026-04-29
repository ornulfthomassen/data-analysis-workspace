# VYA_STOCK_FTV_WEEK_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates stock-related data on a weekly basis, combining historical weekly aggregates with more recent daily aggregates. It calculates 'BALANCE' (UB_WEEK), 'IB_WEEK', and their difference ('NETTO') across various dimensions such as period, primary and sub-product keys, owner/payer/user customer types, lifecycle segment, age groups, and payer counterpart. The data is filtered to include only the last 24 months.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_WEEK_DIM_V]]
| Column Name |
|---|
| YEAR_WEEK_NUMBER |
| LAST_DATE |
| RELATIVE_WEEK |
- ← [[CLM_ADM.STOCK_FTV_HISTORY_WEEK_AGG]]
| Column Name |
|---|
| PERIOD_WEEK_KEY |
| PRIM_PRODUCT_KEY |
| SUB_PRODUCT_KEY |
| CUSTOMER_TYPE_ID_OWNER |
| CUSTOMER_TYPE_ID_PAYER |
| CUSTOMER_TYPE_ID_USER |
| CLM_LIVSFASE_SEGMENT_ID_O |
| OWNER_AGE |
| USER_AGE |
| PAYER_COUNTERPART_KEY |
| ACTIVATED |
| BALANCE |
- ← [[CRM_ANALYSE.ADM_CLM_LIVSFASE_DIM]]
| Column Name |
|---|
| CLM_LIVSFASE_KEY |
| CLM_LIVSFASE_NAME_6C |
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
| Column Name |
|---|
| AGE_GROUP_KEY |
| AGE_GROUP_NAME_10C |
- ← [[CLM_ADM.STOCK_FTV_HISTORY_DAY_AGG]]
| Column Name |
|---|
| PERIOD_WEEK_KEY |
| DAY |
| PRIM_PRODUCT_KEY |
| SUB_PRODUCT_KEY |
| CUSTOMER_TYPE_ID_OWNER |
| CUSTOMER_TYPE_ID_PAYER |
| CUSTOMER_TYPE_ID_USER |
| CLM_LIVSFASE_SEGMENT_ID_O |
| OWNER_AGE |
| USER_AGE |
| PAYER_COUNTERPART_KEY |
| ACTIVATED |
| BALANCE |

