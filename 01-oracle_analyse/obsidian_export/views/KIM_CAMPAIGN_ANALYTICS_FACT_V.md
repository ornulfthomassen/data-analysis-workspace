# KIM_CAMPAIGN_ANALYTICS_FACT_V

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates various Key Performance Indicators (KPIs) related to CRM campaign effectiveness, sales, and customer churn. It aggregates detailed campaign contact, response, and order information, classifying sales activities (upsale, newsale, retention, antichurn) based on campaign types, product categories, and order details. The view provides granular data for analyzing campaign performance, including presented, accepted, and selected responses, new sales of specific product types, and churn prevention efforts.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]

