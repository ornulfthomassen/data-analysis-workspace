# KIM_CAMPAIGN_AGG_VA

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates campaign performance metrics by joining a central campaign detail fact table with various dimension tables. It calculates sums of key performance indicators (KPIs) such as accepted, anti-churn, churn, new sales, presented, selected, success, total sales, and all sales. It also computes revenue increase based on product price differences, counts distinct main numbers and owner IDs, and provides various descriptive attributes from campaign, communication, treatment, response, channel, date, churn group, and product dimensions. The data is filtered to include campaign activities from the beginning of the year, two years prior to the current date, onward.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_V]]
| Column Name |
|---|
| VOLUME |
| KPI_ACCEPTED |
| KPI_ANTICHURN |
| KPI_CHURN |
| KPI_NEWSALE_MPP |
| KPI_PRESENTED |
| KPI_SELECTED |
| KPI_SUCCESS |
| KPI_SALES |
| KPI_ALL_SALES |
| MAIN_NUMBER |
| KURT_ID_OWNER |
| CONTACT_DATE |
| CONTACT_DATE_KEY |
| SOURCE_SYSTEM_KEY |
| SALES_MATRIX_GROUP |
| SALES_MATRIX |
| ACTION_CATEGORY |
| OFFER_CATEGORY |
| PLAN |
| PROGRAM |
| ACTIVITY_DESC |
| ACTIVITY_MAIN_OBJECTIVE |
| ACTIVITY_OBJECTIVE |
| CAMPAIGN |
| CAMPAIGN_DESC |
| CAMPAIGN_KEY |
| COMMUNICATION_KEY |
| TREATMENT_KEY |
| RESPONSE_KEY |
| CHANNEL_KEY |
| churn_group_key |
| ORDER_FROM_PRODUCT_KEY |
| ORDER_TO_PRODUCT_KEY |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM_V]]
| Column Name |
|---|
| CAMPAIGN_KEY |
| ACTIVITY_AREA |
| SOURCE_SYSTEM_KEY |
| CAMPAIGN_NM |
| CAMPAIGN_CD |
| CAMPAIGN_TYPE_DESC |
| OFFER_BRAND |
- ← [[CRM_ANALYSE.KIM_COMMUNICATION_DIM_V]]
| Column Name |
|---|
| COMMUNICATION_KEY |
| ACTION_CATEGORY |
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM_V]]
| Column Name |
|---|
| TREATMENT_KEY |
| ACTION_CATEGORY |
| ACTION_CATEGORY_TYPE |
| BRAND |
| OFFER_CATEGORY |
| TREATMENT_CD |
| TREATMENT_NM |
| TREATMENT_GROUP |
| TREATMENT_SUB_GROUP |
| TREATMENT_GROUP_SH |
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM_V]]
| Column Name |
|---|
| RESPONSE_KEY |
| RESPONSE_NM |
| RESPONSE_GROUP |
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
| Column Name |
|---|
| CHANNEL_KEY |
| CHANNEL_COMMON_NM |
- ← [[CRM_ANALYSE.KIM_DATE_DIM_V]]
| Column Name |
|---|
| DATE_KEY |
| LAST_4_WEEKS |
| LAST_WEEK |
| LAST_MONTH |
| YEAR_TO_DATE |
| relative_week |
| relative_month |
- ← [[CRM_ANALYSE.KIM_CHURN_GROUP_DIM_V]]
| Column Name |
|---|
| CHURN_GROUP_KEY |
| CHURN_GROUP_NAME |
| CHURN_GROUP_DESCRIPTION |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| MONTHLY_PRICE |
| PRODUCT_NAME |
| PRODUCT_FAMILY_NAME |

