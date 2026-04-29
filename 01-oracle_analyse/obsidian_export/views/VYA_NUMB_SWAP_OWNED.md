# VYA_NUMB_SWAP_OWNED

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates, for each customer, the total number of currently active 'SWAP' devices they own, along with the earliest and latest end dates for these swap agreements.

## Data Sources (Inputs)
- ← [[CLM_CCM.V_ODS_AGRMT_OFFER_MOB_DEVICE]]
| Column Name |
|---|
| PRODUCT_KEY |
| KURT_ID |
| PRODUCT_END_DATE |
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

