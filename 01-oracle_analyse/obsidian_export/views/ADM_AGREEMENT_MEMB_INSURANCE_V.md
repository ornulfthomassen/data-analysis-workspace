# ADM_AGREEMENT_MEMB_INSURANCE_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view extracts the most recent insurance agreement details for each unique device (identified by IMEI). It filters agreements to include only those marked as 'Forsikring' (Insurance) and belonging to the 'DEVICE' product group, providing the IMEI, root agreement key, product agreement ID, and product name associated with the latest device agreement end date.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_ALL]]
| Column Name |
|---|
| IMEI |
| ROOT_AGREEMENT_KEY |
| PRODUCT_AGREEMENT_ID |
| PRODUCT_AGREEMENT_PRODUCT_NM |
| DEVICE_AGREEMENT_END_DATE |
| PRODUCT_AGREE_DRM_COM_MRK_PROD |
| PRODUCT_AGREE_DRM_COM_PROD_GRP |

