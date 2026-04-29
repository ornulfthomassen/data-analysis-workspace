# ADM_AGREEMENT_MEMB_SWAP_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Identifies the latest swap agreement details for each unique IMEI, filtering for device-related products, by selecting agreement key, product ID, and product name based on the most recent agreement end date.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_ALL]]
| Column Name |
|---|
| IMEI |
| ROOT_AGREEMENT_KEY |
| PRODUCT_AGREEMENT_ID |
| DEVICE_AGREEMENT_END_DATE |
| PRODUCT_AGREEMENT_PRODUCT_NM |
| PRODUCT_AGREE_DRM_COM_MRK_PROD |
| PRODUCT_AGREE_DRM_COM_PROD_GRP |

