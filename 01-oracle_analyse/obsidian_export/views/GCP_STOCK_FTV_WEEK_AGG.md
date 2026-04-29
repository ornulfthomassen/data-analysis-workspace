# GCP_STOCK_FTV_WEEK_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates weekly stock and balance data, combining historical weekly aggregates from `CLM_ADM.STOCK_FTV_HISTORY_WEEK_AGG` with recent daily aggregates from `CLM_ADM.STOCK_FTV_HISTORY_DAY_AGG`. It enriches this data by joining with dimension tables for customer lifecycle (`CRM_ANALYSE.ADM_CLM_LIVSFASE_DIM`) and age groups (`CRM_ANALYSE.ADM_AGE_GROUP_DIM`), and week dimensions (`CRM_ANALYSE.ADM_WEEK_DIM_V`). The view calculates total balance (UB_WEEK), inbooked balance (IB_WEEK), and netto balance (NETTO) for various customer types, products, and age segments. The primary purpose is to prepare and lift this data to Google Cloud Platform (GCP).

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

