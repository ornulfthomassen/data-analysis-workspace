# KIM_LASR_DET

**Schema:** `CCM` | **Type:** `View`

## Description
This view creates a comprehensive CRM (Customer Relationship Management) analytical dataset. Its main purpose is to consolidate various Key Performance Indicators (KPIs) related to campaign performance, sales, churn, and customer interactions, enriching them with detailed dimensional attributes such as date, campaign details, channels, treatments, products (from/to/treatment/contact), handsets, dealers, and customer demographics. It facilitates detailed analysis of CRM activities, often used for reporting and understanding the effectiveness of different strategies.

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_LASR_FACT]]
- ← [[crm_analyse.KIM_CAMPAIGN_DIM]]
- ← [[galaxy.date_dim_mv]]
- ← [[crm_analyse.kim_channel_dim]]
- ← [[crm_analyse.kim_treatment_dim]]
- ← [[crm_analyse.kim_churn_group_dim]]
- ← [[CRM_ANALYSE.KIM_SOURCE_SYSTEM_DIM_V]]
- ← [[crm_analyse.PRODUCT_DIM_VA]]
- ← [[crm_analyse.kim_response_dim]]
- ← [[CRM_ANALYSE.HANDSET_DIM_VA]]
- ← [[CRM_ANALYSE.KIM_DEALER_DIM_V]]

