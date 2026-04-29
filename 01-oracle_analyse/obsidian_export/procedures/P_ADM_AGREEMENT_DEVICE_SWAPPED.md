# P_ADM_AGREEMENT_DEVICE_SWAPPED

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure identifies and marks 'swapped' device agreements within the ADM_AGREEMENT_DEVICE_SWAPPED table. It first populates the ADM_AGREEMENT_DEVICE_SWAPPED table with initial device agreements from CLM_ADM.ADM_AGREEMENT_DEVICE_ALL that meet specific status and date conditions and are related to 'SWAP' products, incorporating aggregate swap counts. Subsequently, it iteratively updates existing records in ADM_AGREEMENT_DEVICE_SWAPPED by matching agreements based on various criteria (e.g., same root agreement, temporal proximity of agreement end/registration dates, same main number, same device manufacturer, or same OS type), recording the matched agreement ID, match criteria, and days between agreements.

## Data Sources (Inputs)
- ← [[ADM_AGREEMENT_DEVICE_SWAPPED]]
| Column Name |
|---|
| PRODUCT_AGREEMENT_END_DATE |
| ROOT_AGREEMENT_KEY |
| PRODUCT_AGREEMENT_ID |
| NO_AGR_SWAP |
| MATCHED_PRODUKT_AGREEMENT_ID |
| PRODUCT_AGREEMENT_START_DATE |
| ORDER_MAIN_NUMBER_SK |
| HANDSET_KEY |
| PRODUCT_AGREEMENT_PRODUCT_KEY |
| ORDER_CUSTOMER_SK_OWNER |
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_ALL]]
| Column Name |
|---|
| PRODUCT_AGREEMENT_STATUS_INFO |
| RANGERING |
| PRODUCT_AGREEMENT_END_DATE |
| PRODUCT_AGREEMENT_PRODUCT_KEY |
| ROOT_AGREEMENT_KEY |
| PRODUCT_AGREEMENT_ID |
| PRODUCT_AGREEMENT_REG_DATE |
| ORDER_MAIN_NUMBER_SK |
| HANDSET_KEY |
| ORDER_CUSTOMER_SK_OWNER |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_MARKET_PRODUCT |
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_AGG_V]]
| Column Name |
|---|
| NO_AGR_SWAP |
| NO_AGR_SWAP_ACTIVE |
| DEV_AGREEMENT_KEY |
- ← [[CLM_ADM.ADM_DEVICE_DIM]]
| Column Name |
|---|
| DEVICE_KEY |
| DEVICE_MANUFACTURER |

## Target Tables (Outputs)
- → [[ADM_AGREEMENT_DEVICE_SWAPPED]]
| Column Name |
|---|
| MATCHED_DATE |
| MATCH_CRITERIA |
| MATCHED_PRODUKT_AGREEMENT_ID |
| DAYS_BETWEEN_AGREEMENTS |
| NO_AGR_SWAP |
| NO_AGR_SWAP_ACTIVE |
| ROOT_AGREEMENT_KEY |
| PRODUCT_AGREEMENT_ID |
| PRODUCT_AGREEMENT_START_DATE |
| PRODUCT_AGREEMENT_END_DATE |
| ORDER_MAIN_NUMBER_SK |
| HANDSET_KEY |
| ORDER_CUSTOMER_SK_OWNER |
| PRODUCT_AGREEMENT_STATUS_INFO |
| RANGERING |
| PRODUCT_AGREEMENT_PRODUCT_KEY |
| PRODUCT_AGREEMENT_REG_DATE |
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| LOAD_DATE |
| STATUS |
| MESSAGE |

