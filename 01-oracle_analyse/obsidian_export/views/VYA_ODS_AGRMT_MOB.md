# VYA_ODS_AGRMT_MOB

**Schema:** `CCM` | **Type:** `View`

## Description
Loads ODS_AGREEMENT-CORE data for mobile services into the Mjøsa data platform, providing detailed agreement and customer mapping information.

## Data Sources (Inputs)
- ← [[CLM_CCM.V_ODS_AGRMT_MOB]]
| Column Name |
|---|
| AGREEMENT_ID |
| SRC_AGRM_AGREEMENT_OFFER_ID |
| SRC_AGREEMENT_TYPE_POID |
| AGREEMENT_TYPE |
| SRC_AGREEMENT_PRODUCT_ID |
| AGREEMENT_PRODUCT_NAME |
| AGREEMENT_STATUS |
| AGREEMENT_DAYS_ACTIVE |
| AGREEMENT_START_DATE_ORIG |
| AGREEMENT_START_DATE |
| AGREEMENT_END_DATE |
| IMEI_FULL |
| IMEI_START_DATE |
| IMEI_END_DATE |
| KURT_ID |
| KURT_ID_USER_REF_ORIG |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |

