# VYA_ODS_SUBSCRIPTION

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates, transforms, and prepares comprehensive subscription data, including associated customer and product details, for loading into an analytical data system (referred to as 'Mjøsa'). It calculates subscription and product active days, derives customer roles (owner, user, payer) using customer mapping, enriches product attributes, and applies specific business rules for determining subscription end dates for certain product types (e.g., 'Epost' subscriptions) and filters out specific product offers.

## Data Sources (Inputs)
- ← [[ODS.SUBSCRIBED_OFFER_ODS_MOB]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_CCM.ODS_SUBSCRIPTION_MV]]
- ← [[CRM_ANALYSE.PD]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CCDW.SUBSCRIPTION_EXTENSION]]

