# KIM_CONTACTS_HIST_STAGE_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates historical contact information, associating it with customer subscriptions, campaign details, treatment attributes, and product information from various source systems, preparing the data for analytical or staging purposes. It leverages data from contact history, customer mapping, dynamic treatment attributes, character and numeric treatment UDFs, product dimensions, and subscription master history to build a comprehensive record of customer interactions and related marketing efforts.

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_CONTACT_HIST_2020]]
| Column Name |
|---|
| contact_key |
| contact_dttm |
| OB_subscription_ID |
| CAMPAIGN_CD |
| CAMPAIGN_SK |
| CAMPAIGN_TYPE_CD |
| campaign_type_desc |
| CAMPAIGN_NM |
| channel_desc |
| CHANNEL_CD |
| CHANNEL_NM |
| COMMUNICATION_CD |
| COMMUNICATION_NM |
| cell_package_sk |
| INSERT_DTTM_STAGE |
| KURT_ID |
| PACKAGE_HASH_VAL |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |
- ← [[CLM_CDM.CI_DYNAMIC_TREATMENT_ATTRIBUTE]]
| Column Name |
|---|
| sequence_no |
| TREATMENT_HASH_VAL |
| TREATMENT_SK |
| PACKAGE_HASH_VAL |
| CELL_PACKAGE_SK |
- ← [[CLM_KIM.CI_TREATMENT_CHAR_UDF_MRG_V]]
| Column Name |
|---|
| clm_program |
| activity_id |
| activity_description |
| campaign_id |
| activity_main_objective |
| dialog_id |
| dialogue_id |
| activity_objective |
| source_subscription_id |
| activity_product_type |
| activity_type |
| campaign_category |
| campaign_description |
| clm_campaign |
| clm_plan |
| customer_flag |
| ocs_campaign_cd |
| PREVIOUS_ACTIVITY_ID |
| trigger_id |
| product_action_1 |
| product_action_2 |
| product_id_2 |
| product_id_1 |
| product_type_1 |
| product_type_2 |
| TREATMENT_HASH_VAL |
| TREATMENT_SK |
| PRODUCTID1 |
- ← [[CLM_CCM.PRODUCT_DIM_V]]
| Column Name |
|---|
| product_key |
| product_name |
| product_area |
| product_technology |
| product_category |
| product_group |
| product_reporting |
| product_payment |
| product_family_name |
| PRODUCT_POID |
| PRODUCT_SOURCE_SYSTEM_ID |
- ← [[CLM_KIM.CI_TREATMENT_NUM_UDF_V]]
| Column Name |
|---|
| subscription_ID |
| arbitration_value |
| propensity |
| TREATMENT_HASH_VAL |
| TREATMENT_SK |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| MAIN_NUMBER_SK |
| SUBSCRIPTION_ID |

