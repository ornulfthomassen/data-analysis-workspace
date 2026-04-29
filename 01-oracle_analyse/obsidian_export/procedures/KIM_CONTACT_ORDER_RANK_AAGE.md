# KIM_CONTACT_ORDER_RANK_AAGE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Calculates and updates `ORDER_RANK`, `ORDER_RANK_GROUP_KEY`, and `SALES_MATRIX` for relevant records in `CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT`. The ranking is based on a complex set of business rules involving customer responses, campaign channels, order channels, product types, and order matching. The procedure also includes logging and status tracking into `CLM_CCM.GOV_DQ_MARTS` and `STLOG.ST_IN` tables.

## Data Sources (Inputs)
- ← [[kim_update_20200226]]
| Column Name |
|---|
| CONTACT_KEY |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| RESPONSE_DATE_KEY |
| ORDER_DT_KEY |
| ORDER_ID |
| ORDER_MATCH_KEY |
| ORDER_FROM_PRODUCT_KEY |
| TREATMENT_PRIORITY |
| RESPONSE_KEY |
| TREATMENT_KEY |
| CHANNEL_KEY |
| ORDER_DEALER_KEY |
| ORDER_TO_PRODUCT_KEY |
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
| CHECK_SUM_TARGET |

