# SAVE_SUBSCRIPTION_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and enriches information regarding customer churn prevention ('save') cases. It links case details with account information, subscription types (TV, broadband), and customer/location keys. The view provides a comprehensive dataset including reasons for saving or termination, associated products, channels, and various identifiers related to these 'save' events. It filters for recent, non-deleted cases with specific product details.

## Data Sources (Inputs)
- ← [[CVIEW_STAGING."CASE"]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[CVIEW_STAGING.ACCOUNT]]
- ← [[CVIEW_STAGING.ADDRESS__C]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.PRODUCT_CATEGORY]]
- ← [[KAS.KUNDE]]
- ← [[KAS.ABONNENTNR_MSISDN]]

