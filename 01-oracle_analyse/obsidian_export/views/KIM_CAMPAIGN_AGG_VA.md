# KIM_CAMPAIGN_AGG_VA

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates detailed campaign performance metrics (Key Performance Indicators) such as volume, acceptance, churn, new sales, revenue increase, and distinct customer counts. The data is broken down by various dimensions including contact date, time period (year-week, relative week/month), source system, sales matrix, churn group, channel, 'from' and 'to' product details (name, family, monthly price), activity area, action category, brand, offer category, treatment details, response, and campaign attributes. It filters data for the last two years from the beginning of the current year, providing a comprehensive, multi-dimensional view for CRM campaign analysis.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_V]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM_V]]
- ← [[CRM_ANALYSE.KIM_COMMUNICATION_DIM_V]]
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM_V]]
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM_V]]
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
- ← [[CRM_ANALYSE.KIM_DATE_DIM_V]]
- ← [[CRM_ANALYSE.KIM_CHURN_GROUP_DIM_V]]
- ← [[GALAXY.PRODUCT_DIM]]

