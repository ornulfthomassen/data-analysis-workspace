# KIM_CONTACT_ORDER_RE_RANK

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure calculates and re-ranks marketing campaign contacts based on complex business logic involving response status, channel matching, dealer information, product types, and order details. It assigns a 'RANK_GROUP_KEY', an 'ORDER_RANK', and a 'SALES_MATRIX' to each contact associated with an order. The calculated rank and matrix values are then updated back into the `CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT` table. The procedure processes records in batches, commits regularly, and integrates with a logging system (`STLOG`).

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| CAMPAIGN_TYPE_DESC |
| SOURCE_SYSTEM_KEY |
| RESPONSE_DATE_KEY |
| ORDER_DT_KEY |
| ORDER_ID |
| ORDER_MATCH_KEY |
| CONTACT_DTTM |
| TREATMENT_PRIORITY |
| KURT_ID_OWNER |
| KPI_NEWSALE |
| KPI_PRODUCT_CHANGE |
| ORDER_TO_PRODUCT_KEY |
| ORDER_FROM_PRODUCT_KEY |
| CHANNEL_KEY |
| ORDER_DEALER_KEY |
| RESPONSE_KEY |
| TREATMENT_KEY |
| CONTACT_DATE_KEY |
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
| KPI_TYPE |
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
- ← [[STLOG.ST_IN]]
| Column Name |
|---|
| RUN_ID |
| SEQ_ID |

## Target Tables (Outputs)
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

