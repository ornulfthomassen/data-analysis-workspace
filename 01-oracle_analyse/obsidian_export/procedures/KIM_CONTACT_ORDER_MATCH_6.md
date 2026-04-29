# KIM_CONTACT_ORDER_MATCH_6

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure identifies matching orders for contacts by first filtering campaign data into a temporary table based on date range, household ID, and KPI flags. It then joins this temporary data with various dimension and order fact tables (including product, response, treatment, binding, and customer details) based on complex product category, reporting, group, payment, brand, and household matching criteria. The goal is to determine the 'best' order match for each contact using a DENSE_RANK KEEP (FIRST) aggregation. Finally, the procedure updates the main CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT table with these matched order details and logs its execution status and metrics.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_TMP6]]
| Column Name |
|---|
| CONTACT_KEY |
| RESPONSE_KEY |
| CUST_HOUSEHOLD_ID |
| KPI_NEWSALE |
| KPI_PRODUCT_CHANGE |
| CONTACT_DATE_KEY |
| CONTACT_DTTM |
| TREATMENT_KEY |
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
| KPI_TYPE |
- ← [[CRM_ANALYSE.KIM_ORDER_MATCH_PRODUCT_DIM_V]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_SERVICE |
| DRM_COMMON_REPORTING |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_BRAND |
| PTC_PARENT |
| PRIMARY_PRODUCT_FLAG |
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
| KPI_NEWSALE |
| KPI_PRODUCT_CHANGE |
| ORDER_DTTM |
| BINDING_TYPE_BENEFIT_KEY |
| OWNER_CUSTOMER_KEY |
- ← [[GALAXY.BINDING_TYPE_BENEFIT_DIM]]
| Column Name |
|---|
| BINDING_BENEFIT_DESC |
| BINDING_TYPE_BENEFIT_KEY |
- ← [[CLM_CCM.CCM_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| HOUSEHOLD_ID |
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
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_TMP6]]
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

