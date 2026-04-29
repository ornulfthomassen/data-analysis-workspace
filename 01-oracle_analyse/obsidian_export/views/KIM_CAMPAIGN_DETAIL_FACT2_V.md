# KIM_CAMPAIGN_DETAIL_FACT2_V

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates various Key Performance Indicators (KPIs) related to sales, product changes, new sales, and campaign engagement, based on detailed campaign fact data. It categorizes campaign outcomes (e.g., sales, product changes, new sales, accepted responses) using complex conditional logic involving campaign types, product attributes, response details, and temporal relationships. The view combines data from core campaign fact, product dimension, response dimension, treatment dimension, and campaign extension tables to provide a comprehensive analytical perspective on campaign effectiveness.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| VOLUME |
| ORDER_RANK_GROUP_KEY |
| ORDER_RANK |
| SOURCE_SYSTEM_KEY |
| CAMPAIGN_TYPE_DESC |
| ORDER_MATCH_KEY |
| SALES_MATRIX |
| ORDER_DT_KEY |
| CONTACT_DTTM |
| ORDER_LINE_TYPE_KEY |
| ORDER_FROM_PRODUCT_KEY |
| ORDER_TO_PRODUCT_KEY |
| SWAP_RANK |
| CONTACT_DATE_KEY |
| CHANNEL_KEY |
| CAMPAIGN_KEY |
| COMMUNICATION_KEY |
| TREATMENT_KEY |
| RESPONSE_KEY |
| CUST_RESPONSE_KEY |
| CHURN_GROUP_KEY |
| ORDER_DEALER_KEY |
| EFFECT_DATE_KEY |
| EFFECT_TYPE |
| EFFECT_STATUS |
| EFFECT_RANK |
- ← [[KIM_ORDER_MATCH_PRODUCT_DIM_V]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_BRAND |
| DRM_COMMON_REPORTING |
| DRM_COMMON_PRODUCT_CATEGORY |
| PTC_DESCRIPTION |
| PRODUCT_FAMILY_NAME |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_PAYMENT |
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
| Column Name |
|---|
| RESPONSE_KEY |
| RESPONSE_GROUP |
| RESPONSE_NM |
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
| Column Name |
|---|
| TREATMENT_KEY |
| ACTION_CATEGORY |
| BRAND |
- ← [[KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| CONTACT_KEY |
| ACTION_CATEGORY |
| ACTIVITY_OBJECTIVE |
| PROGRAM |
| ACTIVITY_DESC |
| ACTIVITY_MAIN_OBJECTIVE |
| ACTIVITY_ID |
| CAMPAIGN |
| CAMPAIGN_DESC |
| TRIGGER_ID |
| DIALOGUE_ID |
| PRODUCT2 |
| SWAP_MATCH |
- ← [[KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CUST_RESPONSE_KEY |
| EXTERNAL_RESPONSE_INFO_ID1 |

