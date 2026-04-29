# VYA_ODS_AGREEMENT_SAFETY

**Schema:** `CCM` | **Type:** `View`

## Description
Provides product offer details related to 'SAFETY AGREEMENTS', including both active and inactive products and agreements. This view is specifically designed for loading ODS_AGREEMENT_SAFETY-data into Viya/MJØSA.

## Data Sources (Inputs)
- ← [[CLM_CCM.V_ODS_AGRMT_OFFER_MOB_SAFETY]]
| Column Name |
|---|
| AGREEMENT_ID |
| SRC_AGREEMENT_ID |
| SRC_AGRM_AGREEMENT_OFFER_ID |
| SRC_AGREEMENT_PRODUCT_ID |
| AGREEMENT_PRODUCT_NAME |
| AGREEMENT_STATUS |
| SRC_PROD_AGREEMENT_OFFER_ID |
| PRODUCT_KEY |
| SRC_PRODUCT_ID |
| PRODUCT_NAME |
| PRODUCT_NAME_MARKET |
| PRODUCT_STATUS |
| PRODUCT_DAYS_ACTIVE |
| PRODUCT_DAYS_LEFT |
| PRODUCT_START_DATE_ORIG |
| PRODUCT_START_DATE |
| PRODUCT_END_DATE |
| DEALER_ID |
| DEALER_NAME |
| DEALER_CHAIN_NAME |
| SALES_ID |
| KURT_ID |
- ← [[CM.AGREEMENT_OFFER_STATUS]]
| Column Name |
|---|
| STATUS_ID |
| AGREEMENT_OFFER_ID |
| VALID_TO_DATE |
| INFO_IS_DELETED |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |

