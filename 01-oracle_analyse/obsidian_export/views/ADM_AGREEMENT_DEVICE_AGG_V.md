# ADM_AGREEMENT_DEVICE_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates agreement-related metrics for devices, providing counts of different agreement types (swap, insurance, downpayment), active agreements, specific insurance product types (Pluss, Skjerm), and the earliest/latest active start/end dates for these agreements, grouped by a root agreement key.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_STOCK_AGREEMENT_DEVICE_ALL]]
| Column Name |
|---|
| ROOT_AGREEMENT_KEY |
| PRODUCT_AGREEMENT_STATUS |
| PRODUCT_AGREEMENT_START_DATE |
| PRODUCT_NAME |
| PRODUCT_AGREEMENT_PRODUCT_KEY |
| RANGERING |
| PRODUCT_AGREE_DRM_COM_PROD_GRP |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| DRM_COMMON_MARKET_PRODUCT |
| PRODUCT_KEY |

