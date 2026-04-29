# VYA_ODS_NUMB_SWAP_OWNED

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates the number of active 'SWAP' type device products owned by each customer, providing the earliest and latest product end dates for these active products.

## Data Sources (Inputs)
- ← [[CLM_CCM.V_ODS_AGRMT_OFFER_MOB_DEVICE]]
| Column Name |
|---|
| PRODUCT_END_DATE |
| PRODUCT_KEY |
| KURT_ID |
| PRODUCT_STATUS |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |

