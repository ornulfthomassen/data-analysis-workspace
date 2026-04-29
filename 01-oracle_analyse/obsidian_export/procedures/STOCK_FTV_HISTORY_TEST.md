# STOCK_FTV_HISTORY_TEST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure dynamically creates a helper procedure named 'ASYNC_PROC_KAS' and schedules it for immediate execution using `DBMS_SCHEDULER`. The helper procedure's primary function is to extract detailed subscription and product information for a specified date (passed as `P_YYYY_MM_DD`). It filters for 'Abonnement' type products from the 'KAS' source system, specifically within 'Bredbånd', 'Frihet', and 'TV' categories, while excluding certain product descriptions and IDs. The extracted and joined data from various GALAXY schema dimension and fact tables is then stored into a newly created temporary raw table named `TMP_STOCK_FTV_HIST_RAW_KAS`.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| OWNER_CUSTOMER_KEY |
| PAYER_CUSTOMER_KEY |
| USER_CUSTOMER_KEY |
| PRIM_PRODUCT_KEY |
| SUB_PRODUCT_KEY |
| SUBSCR_TYPE_STATUS_KEY |
| SUB_PROD_START_DT_KEY |
| SUB_PROD_END_DT_KEY |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| DATE_KEY |
| YEAR_WEEK_NUMBER |
| YEAR_MONTH_NUMBER |
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| PARENT_SUBSCRIPTION_KEY |
| PRIM_PROD_ORG_START_DT_KEY |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_DESC |
| PRODUCT_NAME |
| SOURCE_SYSTEM_NAME |
| DRM_COMMON_PRODUCT_CATEGORY |
| PRODUCT_CATEGORY_NAME |
| PRODUCT_CATEGORY_DESC |
| SOURCE_PRODUCT_ID_1 |

## Target Tables (Outputs)
- → [[TMP_STOCK_FTV_HIST_RAW_KAS]]
| Column Name |
|---|
| DAY |
| PERIOD_DATE_KEY |
| PERIOD_WEEK_KEY |
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_KEY |
| PARENT_SUBSCRIPTION_KEY |
| OWNER_CUSTOMER_KEY |
| PAYER_CUSTOMER_KEY |
| USER_CUSTOMER_KEY |
| PRIM_PRODUCT_KEY |
| PRIM_PRODUCT_DESC |
| SUB_PRODUCT_KEY |
| SUB_PRODUCT_NAME |
| SUB_PRODUCT_DESC |
| ACTIVATED_DT_KEY |

