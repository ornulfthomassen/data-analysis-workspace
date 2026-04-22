# KIM_LASR_FACT_DETAIL_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named KIM_LASR_FACT_DETAIL_V, provides a comprehensive, aggregated dataset for analyzing CRM campaign performance and customer interactions. It calculates various Key Performance Indicators (KPIs) related to sales (including accepted, new sales, upsells, and retention), anti-churn activities, presented offers, and selected offers. The sales KPIs are categorized and summed based on complex logic involving campaign types, product attributes, order matching, and interaction outcomes. The view also enriches the aggregated data with detailed dimensions such as subscription, customer, campaign, channel, treatment, product, household, and geographical information, allowing for in-depth analysis of campaign effectiveness and results.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
- ← [[KIM_ORDER_MATCH_PRODUCT_DIM_V]]
- ← [[KIM_CAMPAIGN_DETAIL_FACT_EXT]]
- ← [[KIM_CUSTOMER_RESPONSE]]
- ← [[KIM_ACTIVITY_DIM_V]]
- ← [[CLM_KIM.CCM_HOUSEHOLD_INFO]]
- ← [[GALAXY.LOCATION_DIM]]

