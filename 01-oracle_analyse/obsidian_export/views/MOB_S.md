# MOB_S

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive, denormalized record of subscriptions, enriching core subscription details with extensive product information, product classification, and pricing attributes. It combines data from a central subscription table with product definitions and hierarchical product type configurations for analytical and reporting purposes.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CRM_ANALYSE.PD]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]

