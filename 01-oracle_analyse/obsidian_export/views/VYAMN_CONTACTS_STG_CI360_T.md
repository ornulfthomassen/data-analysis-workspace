# VYAMN_CONTACTS_STG_CI360_T

**Schema:** `CCM` | **Type:** `View`

## Description
This view serves as a staging layer for contact and contact metadata from the SAS CI360 system. It transforms and combines data from multiple SAS360 tables, customer mapping, and subscription master history, with corrected datatypes, for use in a system referred to as KIM. It's designed to eventually replace an existing view (CCM.VYAMN_CONTACTS_STG_CI360) as the primary source for this data.

## Data Sources (Inputs)
- ← [[SAS360_COMMON.SAS360_CONTACTS]]
| Column Name |
|---|
| CONTACT_ID |
| SUBJECT_KEY |
| CONTACT_DTTM |
| CHANNEL |
| TASK_CD |
| TASK_NM |
| TASK_VERSION_ID |
| RESPONSE_TRACKING_CD |
| BUSINESS_UNIT |
| SEGMENT_VERSION_ID |
- ← [[SAS360_COMMON.SAS360_CONTACTS_METADATA_KIM]]
| Column Name |
|---|
| TASK_VERSION_ID |
| SEGMENT_VERSION_ID |
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
| SEGMENT_CD |
| PRODACT1 |
| PRODID1 |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| KURT_KEY |
| CUSTOMER_SK |
- ← [[SAS360_COMMON.SAS360_SUPPL_SUBJECTS]]
| Column Name |
|---|
| SUBJECT_KEY |
| RESPONSE_TRACKING_CD |
| SUBJECT_TYPE |
| SUPPL_SUBJECT_KEY |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |

