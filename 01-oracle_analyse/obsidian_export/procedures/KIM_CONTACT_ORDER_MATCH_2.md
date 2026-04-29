# KIM_CONTACT_ORDER_MATCH_2

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure matches campaign details with order information based on specific product, owner, and KPI criteria. It first creates a temporary table by filtering campaign data. Then, it uses this temporary data along with several other dimension and fact tables to identify the best-matching order for each campaign contact. Finally, it updates the CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT table with the determined order match keys and details. The procedure also incorporates logging into system status tables.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| CONTACT_DATE_KEY |
| ORDER_MATCH_KEY |
| TREATMENT_KEY |
| KPI_PRODUCT_CHANGE |
| KPI_NEWSALE |
- ← [[KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| CONTACT_KEY |
| PRODUCT_ACT1 |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_TMP2]]
| Column Name |
|---|
| CONTACT_KEY |
| RESPONSE_KEY |
| KURT_ID_OWNER |
| KPI_NEWSALE |
| KPI_PRODUCT_CHANGE |
| CONTACT_DATE_KEY |
| CONTACT_DTTM |
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
| Column Name |
|---|
| RESPONSE_KEY |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| CONTACT_KEY |
| OFFER_CATEGORY |
| PRODUCT_ACT1 |
| PRODUCT_KEY_1 |
| PRODUCT_KEY_2 |
| PRODUCT_KEY_3 |
| PRODUCT_KEY_4 |
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
| Column Name |
|---|
| TREATMENT_KEY |
| OFFER_CATEGORY |
| TREATMENT_PRODUCT_KEY |
- ← [[CRM_ANALYSE.ORDER_LINE_DETAIL_FACT_TMP]]
| Column Name |
|---|
| SOURCE_ORDER_ID |
| ORDER_LINE_TYPE_KEY |
| FROM_ORDER_PRODUCT_KEY |
| ORDERLINE_PRODUCT_KEY |
| BINDING_PRODUCT_KEY |
| DEALER_KEY |
| ORDER_DT_KEY |
| ORDER_STATUS_DT_KEY |
| SOURCE_SYSTEM_KEY |
| HANDSET_KEY |
| OWNER_CUSTOMER_KEY |
| KPI_NEWSALE |
| KPI_PRODUCT_CHANGE |
| ORDER_DTTM |
| BINDING_TYPE_BENEFIT_KEY |
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
| Column Name |
|---|
| ORDER_LINE_PRODUCT_KEY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_SERVICE |
| DRM_COMMON_PRODUCT_GROUP |
- ← [[GALAXY.BINDING_TYPE_BENEFIT_DIM]]
| Column Name |
|---|
| BINDING_TYPE_BENEFIT_KEY |
| BINDING_BENEFIT_DESC |
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
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_TMP2]]
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_MATCH_KEY |
| ORDER_RANK |
| ORDER_ID |
| ORDER_LINE_TYPE_KEY |
| ORDER_FROM_PRODUCT_KEY |
| ORDER_TO_PRODUCT_KEY |
| ORDER_BINDING_PRODUCT_KEY |
| ORDER_DEALER_KEY |
| ORDER_DT_KEY |
| ORDER_STATUS_DT_KEY |
| ORDER_SOURCE_SYSTEM_KEY |
| BINDING_BENEFIT_DESC |
| ORDER_HANDSET_KEY |
| SEQ_ID_UPD |
- → [[STLOG.ST_IN]]
| Column Name |
|---|
| NUM_RECS_IN_TARGET |
| CHECK_SUM_TARGET |

