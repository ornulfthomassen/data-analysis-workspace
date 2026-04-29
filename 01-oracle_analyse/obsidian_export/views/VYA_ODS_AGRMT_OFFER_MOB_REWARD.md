# VYA_ODS_AGRMT_OFFER_MOB_REWARD

**Schema:** `CCM` | **Type:** `View`

## Description
Prepares and enriches agreement offer mobile reward data by joining it with customer mapping details, calculates customer owner keys, and derives product status, for loading into a data warehouse or reporting system.

## Data Sources (Inputs)
- ← [[CLM_CCM.V_ODS_AGRMT_OFFER_MOB_REWARD]]
| Column Name |
|---|
| AGREEMENT_ID |
| SRC_AGREEMENT_ID |
| SRC_AGRM_AGREEMENT_OFFER_ID |
| SRC_AGREEMENT_PRODUCT_ID |
| AGREEMENT_PRODUCT_NAME |
| SRC_PROD_AGREEMENT_OFFER_ID |
| PRODUCT_KEY |
| SRC_PRODUCT_ID |
| PRODUCT_NAME |
| PRODUCT_FIRST_START_DATE |
| PRODUCT_STATUS |
| PRODUCT_DAYS_ACTIVE |
| PRODUCT_DAYS_LEFT |
| PRODUCT_START_DATE_ORIG |
| PRODUCT_START_DATE |
| PRODUCT_END_DATE |
| KURT_ID |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |

