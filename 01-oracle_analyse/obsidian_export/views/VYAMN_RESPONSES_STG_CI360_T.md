# VYAMN_RESPONSES_STG_CI360_T

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and transforms customer response event data from various SAS360 common tables and CRM analytical views. It enriches the core response information with details about the response channel, customer mapping, subscription information, and response reasons, standardizing it into a format suitable for staging or analysis within a Customer Intelligence (CI360) context.

## Data Sources (Inputs)
- ← [[SAS360_COMMON.SAS360_RESPONSES]]
| Column Name |
|---|
| RESPONSE_ID |
| RESPONSE_DTTM |
| RESPONSE_CHANNEL_CD |
| EXTERNAL_RESPONSE_INFO_ID1 |
| EXTERNAL_RESPONSE_INFO_ID2 |
| RESPONSE_TRACKING_CD |
| RESPONSE_CD |
| SUBJECT_KEY |
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
| SUBJECT_TYPE |
| SUPPL_SUBJECT_KEY |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |

