# VIYA_KIM_SJEKK

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and enriches campaign detail fact data with extended activity information, response details, channel information, and product details. It calculates Key Performance Indicators (KPIs) such as 'Presented' volume (volume for presented responses) and 'All Sales' volume (volume for the primary order, rank 1). The view combines contact and order information, campaign specifics, and product attributes for detailed analysis.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT]]
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
- ← [[CRM_ANALYSE.product_dim_v]]

