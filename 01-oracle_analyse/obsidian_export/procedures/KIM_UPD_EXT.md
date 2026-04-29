# KIM_UPD_EXT

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Updates campaign detail fact tables (`KIM_CAMPAIGN_DETAIL_FACT` and `KIM_CAMPAIGN_DETAIL_FACT_EXT`) by enriching them with KPI flags, subscription identifiers, main numbers, activity attributes, campaign descriptions, and action categories. The updates are performed based on joined data from `KIM_CAMPAIGN_DETAIL_FACT`, `KIM_CAMPAIGN_DETAIL_FACT_EXT`, `CI_TREATMENT_CHAR_UDF_MRG`, and `SUBSCRIPTION_MAPPING` for records with a `CONTACT_DATE_KEY` greater than or equal to 20190801. The procedure processes records in batches, committing changes periodically.

## Data Sources (Inputs)
- ← [[crm_analyse.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| TREATMENT_HASH_VAL |
| CONTACT_DATE_KEY |
- ← [[crm_analyse.KIM_CAMPAIGN_DETAIL_FACT_ext]]
| Column Name |
|---|
| CONTACT_KEY |
| ACTION_CATEGORY |
- ← [[CLM_KIM.CI_TREATMENT_CHAR_UDF_MRG]]
| Column Name |
|---|
| TREATMENT_HASH_VAL |
| REGARDING_MSISDN |
| activity_id |
| ACTIVITY_DESCRIPTION |
| ACTIVITY_MAIN_OBJECTIVE |
| CAMPAIGN_DESCRIPTION |
| PRODUCT_ACTION_1 |
| SOURCE_SUBSCRIPTION_ID |
| EXISTINGPRODUCTID1 |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| KPI_PRODUCT_CHANGE |
| KPI_NEWSALE |
| SUBSCRIPTION_KEY |
| main_number |
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| activity_id |
| ACTIVITY_DESC |
| ACTIVITY_MAIN_OBJECTIVE |
| CAMPAIGN_DESC |
| ACTION_CATEGORY |
| EXISTING_PRODUCT_ID |

