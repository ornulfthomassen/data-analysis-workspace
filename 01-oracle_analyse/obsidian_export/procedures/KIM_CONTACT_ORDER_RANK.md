# KIM_CONTACT_ORDER_RANK

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Calculates and assigns an 'order rank' and 'sales matrix' to campaign details records based on various criteria related to sales channels, response groups, and product types. It processes records that have an order match and a null order rank, and logs the process status to a data quality mart and a system log table.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| RESPONSE_DATE_KEY |
| ORDER_DT_KEY |
| ORDER_ID |
| ORDER_MATCH_KEY |
| TREATMENT_PRIORITY |
| KURT_ID_OWNER |
| RESPONSE_KEY |
| TREATMENT_KEY |
| CHANNEL_KEY |
| ORDER_DEALER_KEY |
| ORDER_TO_PRODUCT_KEY |
| ORDER_FROM_PRODUCT_KEY |
| ORDER_RANK |
| CONTACT_DATE_KEY |
| CONTACT_DTTM |
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
| Column Name |
|---|
| RESPONSE_KEY |
| RESPONSE_GROUP |
| RESPONSE_CD |
| RESPONSE_RANK |
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
| Column Name |
|---|
| TREATMENT_KEY |
| PRODUCT_KEY_1 |
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
| Column Name |
|---|
| CHANNEL_KEY |
| CHANNEL_NM |
| CHANNEL_COMMON_NM |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| DEALER_KEY |
| DRM_SALES_CHANNEL_GEN02_DESC |
| DRM_SALES_CHANNEL_GEN03_DESC |
| DRM_SALES_CHANNEL_GEN04_DESC |
| SOURCE_DEALER_ID |
| DEALER_CHAIN_NAME |
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
- ← [[STLOG.ST_IN]]
| Column Name |
|---|
| RUN_ID |
| SEQ_ID |
- ← [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| SYSTEM_NM |
| PROCESS_NM |
| STATUS_NM |
| RUNTIME |

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

