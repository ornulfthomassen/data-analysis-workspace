# VYA_CHURN_WIDE_SUBSCR_PRODUCTS

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a wide dataset of active subscription product details, filtered for 'Voice' and 'Postpaid' primary products, and excluding 'Switch free voice' sub-products. It integrates monthly dimension data, focusing on subscription periods falling within the last 24 months, for specific market areas (2 and 4). The output includes monthly period keys, subscription identifiers, product start/end dates, and various descriptive product attributes. It is likely used for churn analysis or detailed subscription behavior tracking.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_CHAR |
| PERIOD_MONTH_KEY |
| LAST_DATE_KEY |
| FIRST_DATE_KEY |
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| SUB_PROD_START_DT_KEY |
| SUB_PROD_END_DT_KEY |
| SUBSCR_PRODUCT_QUANTITY |
| MARKET_AREA_KEY |
| PRIM_PRODUCT_KEY |
| SUB_PRODUCT_KEY |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_ACCESS_TYPE_NAME |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_MARKET_PRODUCT |
| PRODUCT_NAME |
| PRODUCT_DESC |
| SOURCE_PRODUCT_ID_1 |

