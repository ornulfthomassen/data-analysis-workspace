# KIM_LASR_FACT_DETAIL_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates and aggregates various Key Performance Indicators (KPIs) related to CRM campaigns, sales, and customer interactions. It combines detailed campaign fact data with attributes from response, campaign, treatment, channel, product, extended campaign details, customer response, activity, household, and location dimensions to provide a comprehensive analytical report.

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
| ORDER_TO_PRODUCT_KEY |
| ORDER_DT_KEY |
| CONTACT_DTTM |
| ORDER_MATCH_KEY |
| ORDER_RANK_GROUP_KEY |
| SALES_MATRIX |
| KPI_PRODUCT_CHANGE |
| ORDER_LINE_TYPE_KEY |
| SWAP_RANK |
| SUBSCRIPTION_KEY |
| MAIN_NUMBER |
| CUSTOMER_SK_OWNER |
| CUSTOMER_SK_PAYER |
| CUSTOMER_SK_USER |
| CUST_AGE |
| CAMPAIGN_KEY |
| CONTACT_DATE_KEY |
| CHANNEL_KEY |
| COMMUNICATION_KEY |
| TREATMENT_KEY |
| ORDER_DAYS |
| RESPONSE_KEY |
| program |
| campaign |
| activity_objective |
| order_dealer_key |
| EFFECT_STATUS |
| EFFECT_TYPE |
| EFFECT_DATE_KEY |
| EFFECT_RANK |
| SWAP_MATCH |
| CONTACT_PRODUCT_KEY |
| cust_household_id |
| RESPONSE_DATE_KEY |
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
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
| Column Name |
|---|
| CHANNEL_KEY |
| CHANNEL_COMMON_NM |
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
| activity_id |
| campaign_desc |
| TRIGGER_ID |
| DIALOG_ID |
| PRODUCT2 |
| ACTIVITY_MAIN_OBJECTIVE |
| ACTIVITY_DESC |
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
- ← [[CLM_KIM.CCM_HOUSEHOLD_INFO]]
| Column Name |
|---|
| household_id |
| start_date |
| end_date |
| ANTALL_I_HUSSTAND |
| BOLIGTYPE |
| HH_PROSPECT_MPP_AGE |
| HH_PROSPECT_MPP_PORTFOLIO_NM |
| HH_NO_DSL_ISP_LINES |
| HH_NO_MPP_USR |
| HH_NO_MPR_USR |
| HH_NO_MBB_USR |
| HH_NO_FIX_BBT_FTV_HH_ADR |
| HH_NO_FIX_BBT_FTV_OTHER_ADR |
| HH_NO_FBB_DSL_HH_ADR |
| HH_NO_FBB_COAX_HH_ADR |
| HH_NO_FBB_FBR_TNN_HH_ADR |
| HH_NO_FBB_FBR_FTV_HH_ADR |
| HH_NO_TV_TNN_HH_ADR |
| HH_NO_TV_FTV_HH_ADR |
| FARID |
- ← [[GALAXY.LOCATION_DIM]]
| Column Name |
|---|
| LOCATION_KEY |
| COUNTY |
| COUNTY_ID |
| MUNICIPAL |
| MUNICIPAL_ID |
| POST_OFFICE |
| POSTCODE_ID |
| COUNTRY_NAME_2 |

