# KIM_SALGSTAVLE_UPDATE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure updates a primary sales summary table (`KIM_SALGSTAVLE_T`) by creating a new version of it (`KIM_SALGSTAVLE_T2`) from various CRM campaign and communication data sources. It then performs a 'cut-over' process: the existing primary table is renamed to a backup table (`KIM_SALGSTAVLE_TOLD`), and the newly created table is renamed to become the new primary table (`KIM_SALGSTAVLE_T`). Corresponding indexes are also dropped and renamed to match the new table structure.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| KURT_ID_OWNER |
| MAIN_NUMBER |
| CAMPAIGN_NM |
| CONTACT_DTTM |
| TREATMENT_PRIORITY |
| CAMPAIGN_KEY |
| COMMUNICATION_KEY |
| TREATMENT_KEY |
| CHANNEL_KEY |
| RESPONSE_KEY |
| RESPONSE_DATE_KEY |
| CUST_FLAG_TREATMENT_KEY |
| SUBS_FLAG_TREATMENT_KEY |
| CONTACT_KEY |
| CONTACT_DATE_KEY |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
| Column Name |
|---|
| CAMPAIGN_KEY |
| CAMPAIGN_TYPE_DESC |
- ← [[CRM_ANALYSE.KIM_COMMUNICATION_DIM]]
| Column Name |
|---|
| COMMUNICATION_KEY |
| COMMUNICATION_DESC |
| COMMUNICATION_NM |
| ACTION_CATEGORY |
| OFFER_CATEGORY |
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
| Column Name |
|---|
| TREATMENT_KEY |
| TREATMENT_DESC |
| TREATMENT_NM |
| ACTION_CATEGORY |
| OFFER_CATEGORY |
| TREATMENT_CD |
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
| Column Name |
|---|
| CHANNEL_KEY |
| CHANNEL_COMMON_NM |
| CHANNEL_NM |
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
| Column Name |
|---|
| RESPONSE_KEY |
| RESPONSE_NM |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DATE_KEY |
| DAY |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| CONTACT_KEY |
| CAMPAIGN_DESC |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_SALGSTAVLE_T2]]
| Column Name |
|---|
| KURT_ID_OWNER |
| MAIN_NUMBER |
| CAMPAIGN_NM |
| COMMUNICATION_TXT |
| OFFER_TXT |
| COM_ACTION_CAT |
| COM_OFFER_CAT |
| KILDE_SYSTEM |
| CHANNEL_NM |
| COMMUNICATION_DATETIME |
| RESPONSE_NM |
| RESPONSE_DATE |
| COMMUNICATION_NM |
| TREATMENT_NM |
| TREATMENT_ID |
| RETENTION_FLAG_CUSTOMER |
| RETENTION_FLAG_SUBSCRIPTION |
| SORT_ORDER |
- → [[CRM_ANALYSE.KIM_SALGSTAVLE_TOLD]]
- → [[CRM_ANALYSE.KIM_SALGSTAVLE_T]]
| Column Name |
|---|
| KURT_ID_OWNER |
| MAIN_NUMBER |
| CAMPAIGN_NM |
| COMMUNICATION_TXT |
| OFFER_TXT |
| COM_ACTION_CAT |
| COM_OFFER_CAT |
| KILDE_SYSTEM |
| CHANNEL_NM |
| COMMUNICATION_DATETIME |
| RESPONSE_NM |
| RESPONSE_DATE |
| COMMUNICATION_NM |
| TREATMENT_NM |
| TREATMENT_ID |
| RETENTION_FLAG_CUSTOMER |
| RETENTION_FLAG_SUBSCRIPTION |
| SORT_ORDER |

