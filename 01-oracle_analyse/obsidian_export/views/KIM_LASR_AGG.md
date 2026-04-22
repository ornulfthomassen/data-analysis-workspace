# KIM_LASR_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive, aggregated analytical dataset for CRM and sales activities. It calculates various Key Performance Indicators (KPIs) such as accepted, sales, presented, selected, and volume sums, alongside maximum contact timestamps. These KPIs are enriched with detailed descriptive attributes from multiple dimensions, including activities, campaigns, contacts, products (contact, from-order, to-order, treatment), dates, channels, churn groups, responses, handsets, and dealers. The data is filtered to include records from January 1, 2019, onwards and only those with a valid response key, enabling in-depth analysis of sales performance, campaign effectiveness, and customer interactions.

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_LASR_FACT_AGG]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
- ← [[CRM_ANALYSE.KIM_CHURN_GROUP_DIM]]
- ← [[CRM_ANALYSE.KIM_SOURCE_SYSTEM_DIM_V]]
- ← [[CRM_ANALYSE.PRODUCT_DIM_VA]]
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
- ← [[CRM_ANALYSE.HANDSET_DIM_VA]]
- ← [[CRM_ANALYSE.KIM_DEALER_DIM_V]]

