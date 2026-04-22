# KIM_CAMPAIGN_DETAIL_FACT_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates various Key Performance Indicators (KPIs) related to customer campaigns and interactions. It aggregates detailed campaign data with customer, product, and order information to measure the effectiveness of different campaign types (e.g., Treatment, Selection, AST, Outbound). The KPIs include sales (distinguished by product activity, upsale, newsale, retention, etc.), presented offers, accepted offers, selected offers, and success rates, based on complex business logic involving sales matrices, channel matching, and temporal relationships between contact and order dates. It also enriches the data with customer demographics, subscription details, and campaign attributes for comprehensive analysis.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
- ← [[CRM_ANALYSE.KIM_COMMUNICATION_DIM]]
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
- ← [[CRM_ANALYSE.KIM_ORDER_MATCH_PRODUCT_DIM_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_HIST]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT]]
- ← [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CRM_ANALYSE.KIM_ACTIVITY_DIM_V]]

