# KIM_CONTACT_ORDER_RANK_HEH

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Calculates and updates order ranking, rank group, and sales matrix categorization for campaign detail records in CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT, based on complex business rules and interactions with various dimension tables. It also logs the procedure's execution status and record counts to governance and logging tables.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| RESPONSE_KEY |
| CHANNEL_KEY |
| ORDER_DEALER_KEY |
| TREATMENT_KEY |
| ORDER_TO_PRODUCT_KEY |
| ORDER_FROM_PRODUCT_KEY |
| ORDER_MATCH_KEY |
| ORDER_RANK |
| CONTACT_DATE_KEY |
| RESPONSE_DATE_KEY |
| ORDER_DT_KEY |
| CAMPAIGN_TYPE_DESC |
| ORDER_ID |
| CONTACT_DTTM |
| TREATMENT_PRIORITY |
| KURT_ID_OWNER |
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
| Column Name |
|---|
| RESPONSE_KEY |
| RESPONSE_GROUP |
| RESPONSE_CD |
| RESPONSE_RANK |
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
| Column Name |
|---|
| CHANNEL_KEY |
| CHANNEL_NM |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| DEALER_KEY |
| DEALER_NAME |
| DEALER_CHAIN_NAME |
| DRM_SALES_CHANNEL_GEN02_DESC |
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
| Column Name |
|---|
| TREATMENT_KEY |
| PRODUCT_KEY_1 |
- ← [[KIM_ORDER_LINE_PRODUCT_DIM_V]]
| Column Name |
|---|
| ORDER_LINE_PRODUCT_KEY |
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| H_LEVEL |
| SORT_ORDER |

## Target Tables (Outputs)
- → [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| RUNTIME |
| FREQ |
| SYSTEM_NM |
| PROCESS_NM |
| STATUS_NM |
| REASON |
| PRIORITY |
| START_TIME |
| END_TIME |
| PREV_OK_DTTM |
| PREV_OK_RESSULT |
| LAST_RESSULT |
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_RANK |
| ORDER_RANK_GROUP_KEY |
| SALES_MATRIX |
| SEQ_ID_UPD |
- → [[STLOG.ST_IN]]
| Column Name |
|---|
| NUM_RECS_IN_TARGET |

