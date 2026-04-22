# CM_SP

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Retrieves distinct subscription details, including associated customer information (payer, responsible, user), directory numbers, subscription validity periods, incentive validity periods, and the public name of the product offer. The view specifically filters for product offers belonging to `PRODUCT_OFFER_CATEGORY_ID = 20`.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
- ← [[PCAT.PRODUCT_OFFER]]

