# KIM_LASR_FACT_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates various aggregated Key Performance Indicators (KPIs) and volume metrics for CRM campaigns. It provides a detailed breakdown of different types of sales (new sales, upsale, retention, product change, swap), accepted/presented offers, and anti-churn activities. The metrics are aggregated by numerous dimensions related to campaigns, contacts, products, channels, treatments, and customer demographics (e.g., age, role), offering a comprehensive view of campaign performance and customer interactions. The complex CASE statements indicate sophisticated business logic for categorizing and quantifying sales and responses.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
- ← [[KIM_ORDER_MATCH_PRODUCT_DIM_V]]
- ← [[KIM_CAMPAIGN_DETAIL_FACT_EXT]]
- ← [[KIM_CUSTOMER_RESPONSE]]
- ← [[KIM_ACTIVITY_DIM_V]]
- ← [[CLM_CCM.CCM_CUSTOMER]]

