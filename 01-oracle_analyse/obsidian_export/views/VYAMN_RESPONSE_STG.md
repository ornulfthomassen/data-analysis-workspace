# VYAMN_RESPONSE_STG

**Schema:** `CCM` | **Type:** `View`

## Description
Prepares and stages detailed marketing response data by combining raw response information with customer and subscription details, formatting various attributes (like event times, channels, and campaign details) for further processing or loading into a downstream system (likely CAS).

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_RESPONSE_STG]]
| Column Name |
|---|
| RESPONSE_KEY |
| RESPONSE_DTTM |
| CHANNEL_NM |
| CAMPAIGN_TYPE_DESC |
| CAMPAIGN_NM |
| CHANNEL_DESC |
| CHANNEL_CD |
| KURT_ID |
| OB_SUBSCRIPTION_ID |
| CAMPAIGN_CD |
| CAMPAIGN_TYPE_CD |
| COMMUNICATION_CD |
| COMMUNICATION_NM |
| EXTERNAL_RESPONSE_INFO_ID1 |
| EXTERNAL_RESPONSE_INFO_ID2 |
| RESPONSE_NM |
| RESPONSE_CHANNEL_RESPONSE_CD |
| RESPONSE_COMMON_NM |
| RESPONSE_GROUP |
| RESPONSE_RANK |
| CELL_PACKAGE_SK |
| TREATMENT_HASH_VAL |
| TREATMENT_SK |
| CAMPAIGN_SK |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| MAIN_NUMBER_SK |
| SUBSCRIPTION_ID |

