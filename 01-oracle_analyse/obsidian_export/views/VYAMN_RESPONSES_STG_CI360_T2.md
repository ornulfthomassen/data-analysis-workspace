# VYAMN_RESPONSES_STG_CI360_T2

**Schema:** `CCM` | **Type:** `View`

## Description
This view serves as a staging area, specifically a test version, for loading responses and associated metadata into the KIM system. It is designed to potentially replace an existing view (`CCM.VYAMN_CONTACTS_STG_CI360`) by providing correct datatypes for the data.

## Data Sources (Inputs)
- ← [[SAS360_COMMON.SAS360_RESPONSES]]
| Column Name |
|---|
| RESPONSE_ID |
| SUBJECT_KEY |
| RESPONSE_DTTM |
| RESPONSE_CHANNEL_CD |
| SOURCE_SYSTEM_CD |
| RESPONSE_CD |
| EXTERNAL_RESPONSE_INFO_ID1 |
| RESPONSE_TRACKING_CD |
- ← [[SAS360_COMMON.SAS360_CI_RESPONSE]]
| Column Name |
|---|
| RESPONSE_CD |
| RESPONSE_NM |
| RESPONSE_GROUP |
| RESPONSE_RANK |
- ← [[SAS360_COMMON.SAS360_CCM_RESPONSE_REASON]]
| Column Name |
|---|
| RESPONSE_REASON_ID |
| RESPONSE_REASON_DESC |
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

