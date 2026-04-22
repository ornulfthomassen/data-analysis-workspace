# KIM_CAMPAIGN_DETAIL_FACT_VOLD

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `KIM_CAMPAIGN_DETAIL_FACT_VOLD`, serves as a detailed fact table for CRM campaign analysis. Its main purpose is to calculate and present various Key Performance Indicators (KPIs) related to campaign effectiveness, sales outcomes (including new sales, upsell, retention), customer responses (presented, accepted, selected), and anti-churn activities. It integrates data from a core campaign detail fact table with product, response, campaign, and treatment dimensions to provide a comprehensive view of campaign performance metrics based on complex business logic and specific criteria.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]

