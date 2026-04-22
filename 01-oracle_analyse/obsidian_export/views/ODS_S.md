# ODS_S

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view provides a comprehensive and consolidated dataset of customer subscriptions, enriched with detailed product information and customer role translations. It combines subscription-specific details (ID, status, main number, customer and account IDs, dates) with extensive product attributes (name, group, description, class, type, market, brand, fees, etc.) and translates customer role IDs into descriptive text. This view is likely used for reporting, analysis, or downstream systems requiring a joined perspective of subscriptions and the products associated with them.

## Data Sources (Inputs)
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
- ← [[CRM_ANALYSE.PRODUCT_DIM_V]]

