# KIM_CONTACTS_STG_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and enriches customer contact and interaction event data from multiple staging, master, and dimension tables. It provides a de-duplicated, comprehensive record for each unique contact event, incorporating details about the contact itself, associated campaigns, activities, products, customer subscriptions, and treatment characteristics, including user-defined attributes.

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_CONTACTS_STG]]
| Column Name |
|---|
| contact_key |
| sequence_no |
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
| TREATMENT_HASH_VAL |
| treatment_sk |
| cell_package_sk |
| KURT_ID |
| COMMUNICATION_CD |
| COMMUNICATION_NM |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |
- ← [[CLM_KIM.CI_TREATMENT_CHAR_UDF_MRG_V]]
| Column Name |
|---|
| TREATMENT_HASH_VAL |
| TREATMENT_SK |
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
| channel |
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
- ← [[CLM_CCM.PRODUCT_DIM_V]]
| Column Name |
|---|
| PRODUCT_POID |
| PRODUCT_SOURCE_SYSTEM_ID |
| product_key |
| product_name |
| product_area |
| product_technology |
| product_category |
| product_group |
| product_reporting |
| product_payment |
| product_family_name |
- ← [[CLM_KIM.CI_TREATMENT_NUM_UDF_V]]
| Column Name |
|---|
| TREATMENT_HASH_VAL |
| TREATMENT_SK |
| subscription_ID |
| arbitration_value |
| propensity |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |

