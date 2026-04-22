# KIM_CAMPAIGN_REPORT_20141204_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `KIM_CAMPAIGN_REPORT_20141204_V`, is designed to generate a comprehensive analytical report or dataset for CRM campaigns. It aggregates various campaign performance metrics (like total volume, sales, presented offers, accepted offers, selected offers, and new sales for Mobile Postpaid products) at a highly granular level. It enriches campaign contact and response data with attributes from several dimension tables, providing detailed insights into customer demographics, product changes (categorizing sales as newsale, upsale, downsale, or neutral), and campaign communication details. The view focuses on specific measure types and contact months from January 2014 onwards, allowing for detailed analysis of campaign effectiveness and outcomes.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[CRM_ANALYSE.KIM_ORDER_RANK_GROUP_DIM]]
- ← [[CRM_ANALYSE.KIM_ORDER_MATCH_DIM]]
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
- ← [[CRM_ANALYSE.KIM_COMMUNICATION_DIM]]
- ← [[CRM_ANALYSE.KIM_CHURN_GROUP_DIM_V]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]

