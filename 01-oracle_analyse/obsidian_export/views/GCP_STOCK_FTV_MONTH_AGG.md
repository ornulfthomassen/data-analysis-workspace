# GCP_STOCK_FTV_MONTH_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates monthly and daily stock financial transaction value (FTV) data, combining beginning and ending month balances along with current day balances. The purpose is to lift this aggregated and time-filtered data to Google Cloud Platform (GCP) via Denodo, ensuring only recent (last two months) and relevant information is transferred.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| LAST_DATE |
| RELATIVE_MONTH |
- ← [[CLM_ADM.STOCK_FTV_HISTORY_MONTH_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
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
| KAS_DUALPLAY |
| DUALPLAY |
| NO_SYSTEMS |
| NO_PRODUCTS |
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
| PERIOD_MONTH_KEY |
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
| KAS_DUALPLAY |
| DUALPLAY |
| NO_SYSTEMS |
| NO_PRODUCTS |
| BALANCE |

