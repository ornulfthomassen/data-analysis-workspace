# CM_MOB_SP

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view provides a comprehensive, consolidated overview of active customer subscriptions, specifically linking subscription identifiers to main directory numbers (likely mobile numbers), and then detailing the product offers/incentives associated with each subscription. It enriches this information with product names, specific component names, and hierarchical product category details (parent and grandparent categories). The data is filtered for active records (`INFO_IS_DELETED = 'N'`) and a specific source system ID (9).

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
- ← [[PCAT.COMPONENT]]
- ← [[GPD]]
- ← [[PTC]]

