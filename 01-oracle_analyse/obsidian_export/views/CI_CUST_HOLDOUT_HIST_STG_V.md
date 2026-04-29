# CI_CUST_HOLDOUT_HIST_STG_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a staging view by joining historical customer holdout contact data with customer and subscription master mappings. The view enriches the data by deriving fields and adding static 'CONTROL GROUP' values, likely for analytical purposes related to marketing campaign A/B testing and customer segmentation.

## Data Sources (Inputs)
- ← [[clm_rtdm.CLM_HOLDOUT_CONTACT_HIST_SDWN]]
| Column Name |
|---|
| PROCESSED_DTTM |
| CONTACT_KEY |
| AB_TEST_TYPE |
| ACTIVITY_DESC |
| ACTIVITY_ID |
| ACTIVITY_OBJECTIVE |
| CAMPAIGN_CATEGORY |
| CAMPAIGN |
| CAMPAIGN_ID |
| CHANNEL_CD |
| PLAN |
| PROGRAM |
| CUSTOMER_FLAG |
| DIALOG_ID |
| DIALOGUE_ID |
| EXISTING_PRODUCT_ID |
| PREV_ACTIVITY_ID |
| PRODUCT_ACT1 |
| PRODUCT_ACT2 |
| PRODUCT_ACT3 |
| PRODUCT_ACT4 |
| PRODUCT1 |
| PRODUCT2 |
| PRODUCT3 |
| PRODUCT4 |
| PRODUCT_TP1 |
| PRODUCT_TP2 |
| PRODUCT_TP3 |
| PRODUCT_TP4 |
| TRIGGER_ID |
| ARBITRATION_VALUE |
| SUBSCRIPTION_ID |
| KURT_ID |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |

