# KIM_LASR_FACT_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates detailed customer campaign and interaction data to calculate various Key Performance Indicators (KPIs) related to sales, customer response, anti-churn initiatives, and product changes. It provides an analytical overview of campaign effectiveness by categorizing interactions (e.g., presented, accepted, selected), sales types (newsale, upsale, retention), and product characteristics.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| VOLUME |
| SOURCE_SYSTEM_KEY |
| CAMPAIGN_TYPE_DESC |
| CHURN_GROUP_KEY |
| ORDER_RANK |
| ORDER_FROM_PRODUCT_KEY |
| ORDER_DT_KEY |
| CONTACT_DTTM |
| ORDER_MATCH_KEY |
| ORDER_RANK_GROUP_KEY |
| KPI_PRODUCT_CHANGE |
| ORDER_LINE_TYPE_KEY |
| CAMPAIGN_KEY |
| CONTACT_DATE_KEY |
| RESPONSE_DATE_KEY |
| CHANNEL_KEY |
| COMMUNICATION_KEY |
| TREATMENT_KEY |
| RESPONSE_KEY |
| SALES_MATRIX |
| PROGRAM |
| CAMPAIGN |
| ACTIVITY_OBJECTIVE |
| DIALOGUE_ID |
| ORDER_DEALER_KEY |
| EFFECT_STATUS |
| EFFECT_TYPE |
| EFFECT_DATE_KEY |
| EFFECT_RANK |
| SWAP_MATCH |
| CONTACT_PRODUCT_KEY |
| KURT_ID_USER |
| KURT_ID_OWNER |
| CUST_AGE |
| CONTACT_HANDSET_KEY |
| SWAP_RANK |
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
| Column Name |
|---|
| RESPONSE_KEY |
| RESPONSE_NM |
| RESPONSE_GROUP |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
| Column Name |
|---|
| CAMPAIGN_KEY |
| ACTIVITY_AREA |
| CAMPAIGN_TYPE_DESC |
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
| Column Name |
|---|
| TREATMENT_KEY |
| ACTION_CATEGORY |
| BRAND |
| PRODUCT2 |
- ← [[KIM_ORDER_MATCH_PRODUCT_DIM_V]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_REPORTING |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_BRAND |
| PTC_DESCRIPTION |
| PRODUCT_FAMILY_NAME |
- ← [[KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| CONTACT_KEY |
| PRODUCT_ACT1 |
| ACTION_CATEGORY |
| ACTIVITY_OBJECTIVE |
| ACTIVITY_ID |
| CAMPAIGN_DESC |
| TRIGGER_ID |
| DIALOG_ID |
| PRODUCT2 |
| ACTIVITY_DESC |
| ACTIVITY_MAIN_OBJECTIVE |
| PRODUCT_KEY_1 |
- ← [[KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CUST_RESPONSE_KEY |
| EXTERNAL_RESPONSE_INFO_ID1 |
- ← [[KIM_ACTIVITY_DIM_V]]
| Column Name |
|---|
| ACTIVITY_ID |
| ACTIVITY_DESC |
- ← [[CLM_CCM.CCM_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| AGE |

