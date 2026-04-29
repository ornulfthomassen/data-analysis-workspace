# KIM_CONTACT_ORDER_MATCH_9

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Identifies and matches contact records with specific order details based on various product and campaign criteria. It first filters and copies relevant `KIM_CAMPAIGN_DETAIL_FACT` records into a temporary table. Then, it joins this temporary data with multiple dimension and fact tables to determine the most relevant order attributes for each contact. Finally, it iterates through the matched results and updates the original `KIM_CAMPAIGN_DETAIL_FACT` table with these aggregated order attributes, such as order date, status, product keys, and binding benefits. The procedure also incorporates logging to track its execution status and record counts.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_DATE_KEY |
| ORDER_MATCH_KEY |
| TREATMENT_KEY |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_TMP9]]
| Column Name |
|---|
| CONTACT_KEY |
| KURT_ID_OWNER |
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
| PRODUCT_KEY_1 |
| PRODUCT_KEY_2 |
| PRODUCT_KEY_3 |
| PRODUCT_KEY_4 |
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
| Column Name |
|---|
| TREATMENT_KEY |
| OFFER_CATEGORY |
| PRODUCT_KEY_1 |
| PRODUCT_KEY_2 |
| PRODUCT_KEY_3 |
| PRODUCT_KEY_4 |
| TREATMENT_PRODUCT_KEY |
- ← [[CRM_ANALYSE.KIM_ORDER_MATCH_PRODUCT_DIM_V]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRIMARY_PRODUCT_FLAG |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_REPORTING |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_BRAND |
| DRM_COMMON_SERVICE |
| PTC_PARENT |
- ← [[CRM_ANALYSE.ORDER_LINE_DETAIL_FACT_TMP]]
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
| OWNER_CUSTOMER_KEY |
| KPI_NEWSALE |
| KPI_PRODUCT_CHANGE |
| ORDER_DTTM |
- ← [[GALAXY.BINDING_TYPE_BENEFIT_DIM]]
| Column Name |
|---|
| BINDING_TYPE_BENEFIT_KEY |
| BINDING_BENEFIT_DESC |
- ← [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| SYSTEM_NM |
| PROCESS_NM |
| STATUS_NM |
| RUNTIME |
- ← [[STLOG.ST_IN]]
| Column Name |
|---|
| RUN_ID |
| SEQ_ID |

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
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_TMP9]]
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

