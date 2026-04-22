# KIM_CAMPAIGN_DETAIL_FACT2_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, "KIM_CAMPAIGN_DETAIL_FACT2_V", is designed to analyze and report on the performance of CRM campaigns by calculating various Key Performance Indicators (KPIs) related to sales, product changes, and customer responses. It categorizes different types of sales (e.g., upsale, newsale, retention, VAS, MPP, swap) based on detailed campaign, order, and product attributes, and tracks customer interactions like presentation, acceptance, and selection of offers. The view provides a consolidated dataset for understanding the effectiveness and outcomes of targeted marketing and sales activities across different channels and campaign types.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[KIM_ORDER_MATCH_PRODUCT_DIM_V]]
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
- ← [[KIM_CAMPAIGN_DETAIL_FACT_EXT]]
- ← [[KIM_CUSTOMER_RESPONSE]]

