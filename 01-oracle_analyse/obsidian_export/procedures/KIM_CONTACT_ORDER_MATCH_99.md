# KIM_CONTACT_ORDER_MATCH_99

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure identifies specific customer campaign detail records that are not yet "order matched" (ORDER_MATCH_KEY <> 99). For these records, it finds the most relevant order details (based on specific date and product category logic) from various order and product-related data sources. It then updates the CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT table, setting the ORDER_MATCH_KEY to 99 and populating associated order attributes derived from the selected order. The procedure also records its execution status and metrics in CLM_CCM.GOV_DQ_MARTS and STLOG.ST_IN.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CONTACT_KEY |
| RESPONSE_DTTM |
| SOURCE_ORDER_ID |
| SOURCE_SYSTEM_KEY |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| ORDER_MATCH_KEY |
| CAMPAIGN_TYPE_DESC |
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| ORDER_DT_KEY |
| ORDER_STATUS_DT_KEY |
| SOURCE_ORDER_ID |
| ORDER_LINE_TYPE_KEY |
| FROM_ORDER_PRODUCT_KEY |
| ORDERLINE_PRODUCT_KEY |
| BINDING_PRODUCT_KEY |
| DEALER_KEY |
| SOURCE_SYSTEM_KEY |
| HANDSET_KEY |
| NUMBER_OF_ORDERS |
| KPI_NEWSALE |
| KPI_PRODUCT_CHANGE |
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
| Column Name |
|---|
| ORDER_LINE_PRODUCT_KEY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
- ← [[GALAXY.BINDING_TYPE_BENEFIT_DIM]]
| Column Name |
|---|
| BINDING_TYPE_BENEFIT_KEY |
| BINDING_BENEFIT_DESC |

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
| CONTACT_KEY |
- → [[STLOG.ST_IN]]
| Column Name |
|---|
| NUM_RECS_IN_TARGET |
| CHECK_SUM_TARGET |

