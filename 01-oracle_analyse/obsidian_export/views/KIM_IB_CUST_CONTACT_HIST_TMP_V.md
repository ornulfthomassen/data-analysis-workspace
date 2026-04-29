# KIM_IB_CUST_CONTACT_HIST_TMP_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates customer contact history with associated marketing treatment, campaign, and subscription details. It extracts and transforms specific values (like subscription IDs and main numbers) from character UDFs, and filters out records that already exist in a campaign detail fact table or are older than a specific date. It also ranks contact records based on various attributes.

## Data Sources (Inputs)
- ← [[RTDM_CDM.CI_CUST_CONTACT_HISTORY]]
| Column Name |
|---|
| PACKAGE_HASH_VAL |
| CU_KURT_ID_OWNER |
| CONTACT_DTTM |
| EXTERNAL_CONTACT_INFO_ID1 |
| CELL_PACKAGE_SK |
- ← [[RTDM_CDM.CI_PACKAGE_X_TREATMENT]]
| Column Name |
|---|
| PACKAGE_HASH_VAL |
| TREATMENT_SK |
| CONTRIBUTING_CELL_PACKAGE_SK |
| SEQUENCE_NO |
- ← [[RTDM_CDM.CI_DYNAMIC_TREATMENT_ATTRIBUTE]]
| Column Name |
|---|
| TREATMENT_HASH_VAL |
| TREATMENT_SK |
| PACKAGE_HASH_VAL |
- ← [[RTDM_CDM.CI_CELL_PACKAGE]]
| Column Name |
|---|
| CELL_PACKAGE_SK |
| CAMPAIGN_SK |
| COMMUNICATION_SK |
| CHANNEL_CD |
- ← [[RTDM_CDM.CI_TREATMENT_CHAR_UDF]]
| Column Name |
|---|
| CHAR_UDF_VAL |
| TREATMENT_HASH_VAL |
| CHAR_UDF_NM |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| START_DATE |
| END_DATE |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| KURT_ID_OWNER |
| CONTACT_DTTM |
| SOURCE_SYSTEM_KEY |

