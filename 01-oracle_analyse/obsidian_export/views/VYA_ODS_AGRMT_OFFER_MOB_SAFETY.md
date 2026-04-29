# VYA_ODS_AGRMT_OFFER_MOB_SAFETY

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a consolidated view of agreement and product safety data, enriching it with customer mapping information. This view appears to be intended for loading into a data warehouse or for reporting purposes, particularly for 'ODS_AGREEMENT_REWARD-DATA'. It includes details about agreements, products, dealers, and a derived customer key.

## Data Sources (Inputs)
- ← [[CLM_CCM.V_ODS_AGRMT_OFFER_MOB_SAFETY]]
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
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |

