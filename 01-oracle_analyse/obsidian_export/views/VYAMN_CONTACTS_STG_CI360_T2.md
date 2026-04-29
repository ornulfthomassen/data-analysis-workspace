# VYAMN_CONTACTS_STG_CI360_T2

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and standardizes contact and campaign metadata from various source systems (SAS360, CRM, CLM) into a unified staging structure. It aims to replace an existing view (`CCM.VYAMN_CONTACTS_STG_CI360`) with improved data types, serving as the main source for loading contact and metadata information into the KIM system.

## Data Sources (Inputs)
- ← [[SAS360_COMMON.SAS360_CONTACTS]]
| Column Name |
|---|
| CONTACT_ID |
| CONTACT_DTTM |
| CHANNEL |
| TASK_CD |
| TASK_NM |
| TASK_VERSION_ID |
| RESPONSE_TRACKING_CD |
| BUSINESS_UNIT |
| SEGMENT_VERSION_ID |
| SUBJECT_KEY |
- ← [[SAS360_COMMON.SAS360_CONTACTS_METADATA_KIM]]
| Column Name |
|---|
| CLMPROGRAM |
| ACTIVITYID |
| ACTIVITYDESC |
| ACTIVITYMAINOBJ |
| CAMPAIGNID |
| ACTIVITYOBJ |
| ACTIVITYTP |
| SEGMENT_MAP_CD |
| CAMPAIGNDESC |
| CHANNEL |
| CLMPLAN |
| PRODACT1 |
| PRODID1 |
| TASK_VERSION_ID |
| SEGMENT_VERSION_ID |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_KEY |
- ← [[SAS360_COMMON.SAS360_SUPPL_SUBJECTS]]
| Column Name |
|---|
| SUPPL_SUBJECT_KEY |
| SUBJECT_KEY |
| RESPONSE_TRACKING_CD |
| SUBJECT_TYPE |
| CURRENT_PRODUCT_ID |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| MAIN_NUMBER_SK |
| SUBSCRIPTION_ID |
- ← [[CLM_CCM.PRODUCT_DIM_V]]
| Column Name |
|---|
| PRODUCT_POID |
| PRODUCT_SOURCE_SYSTEM_ID |
| PRODUCT_KEY |

